#!/usr/bin/env python3
"""
Multi-market monitor -- v4.

Covers three watchlists: crypto (Coinbase), US equities (Yahoo Finance),
Indian equities (Yahoo Finance, .NS suffix). Applies the same decision
rules to every symbol: confirmed-close breakout/breakdown with volume and
trend confirmation, range-boundary rejection, ATR-based stops/sizing,
trailing stops, take-profit heuristic, loss-throttled sizing, alert
de-duplication.

Indian equities are NOT tradable on TradingView's paper account (confirmed
during manual testing -- NSE symbols aren't supported there), so alerts
for those are clearly labeled analysis-only.

US and Indian markets have trading hours, unlike crypto's 24/7 -- a
staleness check skips a symbol for the cycle if its latest bar is old
(market closed), rather than firing a false signal off stale data.

Alert only -- no live tracking of the user's real trades anymore (the
open/fill/skip/close Telegram commands were removed; the user places
real stop-loss/take-profit orders on the exchange and self-manages
entries/exits entirely outside this bot). The only thing this still
tracks going forward is setup_log: a silent, automatic shadow simulation
of every fired setup's real outcome, used purely for the nightly signal
quality report (report.py) -- not a substitute for the user's own
records. State is persisted to state.json, committed back to the repo
by the GitHub Actions workflow after each run.
"""
import json
import os
import sys
import time
import urllib.request
import urllib.error
from datetime import datetime, timedelta, timezone
from zoneinfo import ZoneInfo

STATE_FILE = os.path.join(os.path.dirname(__file__), "state.json")
BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID")

ATR_PERIOD = 14
EMA_PERIOD = 10
REJECTION_BUFFER_PCT = 0.0015
RISK_PCT_PER_TRADE = 0.01

# Max notional per unit of capital, by market -- the user's actual
# available leverage on each platform. Risk amount ($ willing to lose)
# stays tied to real capital regardless of leverage; only the ceiling on
# how much notional that risk can control changes.
# India is 1, not the broker's real 5x -- the virtual paper trader only
# ever hands out capital_inr (Rs 10,00,000) total, so even with leverage
# available, a suggested position's notional must never exceed that
# balance or the sizing would suggest more money than the account has.
LEVERAGE_BY_MARKET = {"crypto": 10, "us": 1, "india": 1}
GAP_THRESHOLD_PCT_US = 0.015  # overnight gap that locks check_watching_us()'s directional bias
# Not currently applied to sizing (see position_size()'s docstring --
# backtested, both cost real profit for no measured drawdown benefit).
# Left defined since consecutive_wins/losses are still tracked and
# these were the actual thresholds tested, in case a re-tuned version
# is worth revisiting later.
LOSS_THROTTLE_AFTER = 2
WIN_THROTTLE_AFTER = 3
STALE_THRESHOLD_SECONDS = 45 * 60  # skip a symbol if its latest bar is older than this

# Trailing-stop tuning -- backtested against 60 days / 2,127 trades across
# BTC/ETH/SOL/XRP (15m bars). These values (vs. the prior 1.0/1.0/0.6)
# came out on top of a 48-combo sweep: total P&L $4.86 -> $55.29, win rate
# 44.9% -> 52.1%, profit factor 1.00 -> 1.15, avg giveback on winners
# 58% -> 55%. See btc-monitor-bot backtest notes.
TRAIL_ATR_MULT = 1.25
PROFIT_LOCK_FLOOR_ATR_MULT = 0.5  # peak profit must exceed this x ATR before the lock floor engages
PROFIT_LOCK_FRACTION = 0.7  # once engaged, guarantee at least this fraction of peak profit

# Crypto is static (24/7, no session to anchor a daily selection to).
# US and India are NOT static -- their active watchlists are chosen fresh
# each day by rank_movers.py from that market's opening-range move (the
# ORB framework, applied at the watchlist-selection level since crypto
# has no session but equities do). See build_watchlist() below.
# Trimmed from the original 12 to the 6 that held up out-of-sample
# (data split in half, symbols picked on the first half, re-tested on
# the second half they'd never seen): BTC/ETH/SOL/AVAX looked strong
# in-sample but flipped to losing money out-of-sample, while XRP and
# NEAR held. Combined with the entry filters below, this watchlist is
# a genuine backtested choice, not a guess.
# FET-USD added per explicit user instruction despite a thin sample --
# a later sweep of 31 more candidates found it was the only one that
# didn't collapse out-of-sample (71.4%/PF2.09 in-sample -> 66.7%/PF1.79
# out-of-sample), but that's only 13 total trades across both halves,
# nowhere near XRP/NEAR's validation depth. Added anyway, caveat on
# record: this is a watch-and-see addition, not a fully validated one.
CRYPTO_WATCHLIST = [{"symbol": s, "market": "crypto", "tradable": True} for s in [
    "BTC-USD", "ETH-USD", "SOL-USD", "XRP-USD", "AVAX-USD", "NEAR-USD", "FET-USD",
]]


def build_watchlist(state):
    watchlist = list(CRYPTO_WATCHLIST)
    for symbol in state.get("active_us_symbols", []):
        watchlist.append({"symbol": symbol, "market": "us", "tradable": True})
    for symbol in state.get("active_india_symbols", []):
        watchlist.append({"symbol": symbol, "market": "india", "tradable": False})
    return watchlist


# ---------------------------------------------------------------- data ----

def fetch_coinbase(symbol, limit=60, granularity=900):
    url = f"https://api.exchange.coinbase.com/products/{symbol}/candles?granularity={granularity}"
    req = urllib.request.Request(url, headers={"User-Agent": "btc-monitor-bot"})
    with urllib.request.urlopen(req, timeout=15) as resp:
        raw = json.loads(resp.read())
    raw.sort(key=lambda r: r[0])
    bars = []
    for r in raw[-limit:]:
        bars.append({
            "open_time": r[0] * 1000, "open": float(r[3]), "high": float(r[2]),
            "low": float(r[1]), "close": float(r[4]), "volume": float(r[5]),
            "close_time": r[0] * 1000,
        })
    return bars


def fetch_yahoo(symbol, limit=60, interval="15m", range_="5d"):
    url = f"https://query1.finance.yahoo.com/v8/finance/chart/{symbol}?interval={interval}&range={range_}"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=15) as resp:
        data = json.loads(resp.read())
    result = data["chart"]["result"][0]
    timestamps = result["timestamp"]
    quote = result["indicators"]["quote"][0]
    bars = []
    for i, ts in enumerate(timestamps):
        o, h, l, c = quote["open"][i], quote["high"][i], quote["low"][i], quote["close"][i]
        if None in (o, h, l, c):
            continue  # Yahoo leaves nulls for gaps outside market hours
        v = quote["volume"][i] or 0
        bars.append({
            "open_time": ts * 1000, "open": float(o), "high": float(h),
            "low": float(l), "close": float(c), "volume": float(v),
            "close_time": ts * 1000,
        })
    return bars[-limit:]


def fetch_klines(symbol, market, limit=60):
    if market == "crypto":
        return fetch_coinbase(symbol, limit)
    return fetch_yahoo(symbol, limit)


def is_stale(last_closed):
    return (time.time() * 1000 - last_closed["close_time"]) > STALE_THRESHOLD_SECONDS * 1000


def load_state():
    with open(STATE_FILE) as f:
        return json.load(f)


def save_state(state):
    with open(STATE_FILE, "w") as f:
        json.dump(state, f, indent=2)


def build_alert_text(text, symbol=None, price=None):
    """The price enrichment send_telegram() does, split out so a caller
    can build a fully-formed alert without sending it immediately --
    needed to batch several setup alerts from one scan into a single
    Telegram message instead of one send per symbol."""
    if symbol is not None and price is not None:
        text += f"\n\nCurrent price: {price:,.4g}"
    return text


def send_telegram(text, symbol=None, price=None):
    text = build_alert_text(text, symbol, price)

    if not BOT_TOKEN or not CHAT_ID:
        print("WARNING: TELEGRAM_BOT_TOKEN/TELEGRAM_CHAT_ID not set, skipping send.")
        print(text)
        return
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = json.dumps({"chat_id": CHAT_ID, "text": text}).encode()
    req = urllib.request.Request(url, data=payload, headers={"Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            resp.read()
    except urllib.error.HTTPError as e:
        print(f"Telegram send failed: {e.read()}")


# ----------------------------------------------------------- indicators ----

def avg_volume(bars):
    if not bars:
        return 0
    return sum(b["volume"] for b in bars) / len(bars)


def atr(bars, period=ATR_PERIOD):
    trs = []
    for i in range(1, len(bars)):
        h, l, prev_close = bars[i]["high"], bars[i]["low"], bars[i - 1]["close"]
        trs.append(max(h - l, abs(h - prev_close), abs(l - prev_close)))
    sample = trs[-period:]
    return sum(sample) / len(sample) if sample else 0


def ema(values, period):
    if not values:
        return None
    k = 2 / (period + 1)
    e = values[0]
    for v in values[1:]:
        e = v * k + e * (1 - k)
    return e


def adx(bars, period=14):
    """Trend-strength regime filter (Wilder's ADX) -- used only by the
    backtest sweep's ADX-ranging-filter variant, not by production
    check_watching()/check_open()."""
    if len(bars) < period * 2 + 1:
        return None
    plus_dm, minus_dm, trs = [], [], []
    for i in range(1, len(bars)):
        up = bars[i]["high"] - bars[i - 1]["high"]
        down = bars[i - 1]["low"] - bars[i]["low"]
        plus_dm.append(up if (up > down and up > 0) else 0)
        minus_dm.append(down if (down > up and down > 0) else 0)
        h, l, prev_close = bars[i]["high"], bars[i]["low"], bars[i - 1]["close"]
        trs.append(max(h - l, abs(h - prev_close), abs(l - prev_close)))

    def wilder_smooth(vals, period):
        smoothed = [sum(vals[:period])]
        for v in vals[period:]:
            smoothed.append(smoothed[-1] - smoothed[-1] / period + v)
        return smoothed

    tr_s = wilder_smooth(trs, period)
    plus_s = wilder_smooth(plus_dm, period)
    minus_s = wilder_smooth(minus_dm, period)
    plus_di = [100 * p / t if t else 0 for p, t in zip(plus_s, tr_s)]
    minus_di = [100 * m / t if t else 0 for m, t in zip(minus_s, tr_s)]
    dx = [100 * abs(p - m) / (p + m) if (p + m) else 0 for p, m in zip(plus_di, minus_di)]
    sample = dx[-period:]
    return sum(sample) / len(sample) if sample else None


def rsi(bars, period=14):
    """Momentum filter used only by check_watching_india() -- not by
    production check_watching_crypto()/check_watching_default()."""
    closes = [b["close"] for b in bars]
    if len(closes) < period + 1:
        return 50
    gains, losses = [], []
    for i in range(1, len(closes)):
        change = closes[i] - closes[i - 1]
        gains.append(max(change, 0))
        losses.append(max(-change, 0))
    avg_gain = sum(gains[-period:]) / period
    avg_loss = sum(losses[-period:]) / period
    if avg_loss == 0:
        return 100
    rs = avg_gain / avg_loss
    return 100 - (100 / (1 + rs))


def ist_date(open_time_ms):
    return (datetime.fromtimestamp(open_time_ms / 1000, tz=timezone.utc) + timedelta(hours=5, minutes=30)).date()


def us_date(open_time_ms):
    """NYSE-session calendar date (America/New_York wall clock) -- used
    only by check_watching_us()'s gap/opening-range day-boundary logic.
    Separate from ist_date() since India and US run on different session
    clocks; DST-aware via zoneinfo, unlike the fixed IST offset above."""
    return datetime.fromtimestamp(open_time_ms / 1000, tz=timezone.utc).astimezone(ZoneInfo("America/New_York")).date()


def day_vwap(closed_bars, last_closed):
    """Cumulative volume-weighted average price from the start of the
    current IST trading day through last_closed -- production only
    ever fetches ~60 bars (limit=60), comfortably more than a full
    NSE session's ~25 bars, so today's bars are always fully
    contained in closed_bars."""
    today = ist_date(last_closed["open_time"])
    today_bars = [b for b in closed_bars if ist_date(b["open_time"]) == today and b["open_time"] <= last_closed["open_time"]]
    cum_pv = sum((b["high"] + b["low"] + b["close"]) / 3 * b["volume"] for b in today_bars)
    cum_vol = sum(b["volume"] for b in today_bars)
    return cum_pv / cum_vol if cum_vol else last_closed["close"]


def committed_capital(setup_log, pool_markets):
    """Sum of entry*qty across currently open (taken, unresolved)
    positions sharing this capital pool -- crypto and US draw from the
    same capital_usd pot (see main()'s capital assignment below), India
    has its own separate capital_inr pot. Without this, every new
    suggestion was sized off the FULL pot regardless of what's already
    committed to other open positions -- as if 100% of capital were
    always free, when in reality taking one trade should leave less
    room for the next (a different symbol, or adding to the same one),
    not none tracked at all. Only accounts for positions open as of the
    START of this scan -- multiple new fires within the same scan don't
    reduce each other's sizing, a minor gap vs. a much larger refactor
    for a case best-of-N filtering already keeps rare."""
    total = 0
    for e in setup_log:
        if e.get("taken") and not e.get("resolved") and market_of(e["symbol"]) in pool_markets:
            total += abs((e.get("entry") or 0) * (e.get("qty") or 0))
    return total


def position_size(capital_usd, entry, stop, consecutive_losses, leverage=1, consecutive_wins=0):
    """Risk-based sizing (fixed % of capital / stop distance) alone can
    suggest a qty whose notional value exceeds what the account can
    actually hold -- e.g. a $0.30 stop on an $87 stock sizes to $290
    notional off $100 capital, 2.9x, more than the 1x the user actually
    has for US stocks. leverage is the max notional per unit of capital
    actually available on that market (LEVERAGE_BY_MARKET); the
    risk-based qty is capped at what that leverage can actually hold.
    consecutive_wins/consecutive_losses are tracked (see check_open()'s
    propagation to the real per-symbol sym_state) but deliberately NOT
    used to throttle size here anymore -- backtested on 2 years of real
    crypto data (7-symbol watchlist, both throttles correctly wired,
    the first time either was ever actually tested end to end) and both
    cost real profit for no measured drawdown benefit: loss-throttle
    alone cut net P&L ~7% with zero drawdown improvement, win-throttle
    alone cut it ~21%. Several symbols had genuine serial correlation in
    win streaks (AVAX hit 9-in-a-row) rather than reversion, so halving
    size after a streak mostly just shaved profit off the best
    stretches instead of protecting against a reversal that usually
    didn't come. Left as tracked-but-inert rather than deleted, in case
    a properly-tuned version (different threshold, different reduction
    fraction) is worth revisiting later with real evidence behind it."""
    risk_amount = capital_usd * RISK_PCT_PER_TRADE
    stop_distance = abs(entry - stop)
    if stop_distance <= 0 or entry <= 0:
        return 0
    risk_based_qty = risk_amount / stop_distance
    max_affordable_qty = (capital_usd * leverage) / entry
    return min(risk_based_qty, max_affordable_qty)


def expected_profit_line(entry, stop, qty, target=None, currency="$"):
    """Range-rejection trades have a real fixed target, so the expected
    profit is exact. Breakout/breakdown trades don't (they're trail-only
    by design -- a fixed target would contradict "let it run"), so this
    quotes a 2R estimate off the known risk instead, clearly labeled as
    an estimate rather than implying a real target exists. currency is
    "$" for crypto/US or "Rs" for India -- capital_usd and capital_inr
    are different currencies, so a bare number would be misleading."""
    risk_per_unit = abs(entry - stop)
    if target is not None:
        reward_per_unit = abs(target - entry)
        r_multiple = reward_per_unit / risk_per_unit if risk_per_unit else 0
        return f"Expected profit: +{currency}{reward_per_unit * qty:,.4g} at target ({r_multiple:.1f}R)"
    reward_per_unit = 2 * risk_per_unit
    return f"Expected profit: ~{currency}{reward_per_unit * qty:,.4g} at 2R (no fixed target -- keep trailing, actual depends on how far it runs)"


def default_symbol_state(closed_bars):
    recent_high = max(b["high"] for b in closed_bars[-10:])
    recent_low = min(b["low"] for b in closed_bars[-10:])
    return {
        "status": "watching", "range_high": recent_high, "range_low": recent_low,
        "direction": None, "entry_price": None, "entry_qty": None, "stop_loss": None,
        "extreme_since_entry": None, "peak_profit_per_unit": 0, "take_profit_target": None,
        "consecutive_losses": 0, "consecutive_wins": 0, "last_alert": {},
        "trade_journal": [],
    }


def rearm_to_watching(sym_state, closed_bars=None):
    """Re-arm a symbol to 'watching' right after a trade closes (or is
    marked as never actually taken -- see sync_fills' "skip" command), so
    the bot keeps tracking the next signal on its own -- no human has to
    manually flip state.json back to watching. Range resets off the most
    recent 10 bars when they're available (a real close); when they're
    not (a chat-driven "skip"), the existing range is left as-is and will
    self-correct on the next check_watching() pass."""
    sym_state.update({
        "status": "watching",
        "direction": None, "entry_price": None, "entry_qty": None, "stop_loss": None,
        "extreme_since_entry": None, "peak_profit_per_unit": 0, "take_profit_target": None,
        "last_alert": {}, "pending": None,
    })
    if closed_bars:
        recent = closed_bars[-10:]
        sym_state["range_high"] = max(b["high"] for b in recent)
        sym_state["range_low"] = min(b["low"] for b in recent)


# ---------------------------------------------------------------- logic ----

def check_watching(symbol, tradable, sym_state, closed_bars, last_closed, capital, market, setup_log=None):
    """Dispatches to the market-specific entry logic -- each market got
    its own backtested filter set (crypto: retest/2-bar/ADX; India:
    RSI momentum + VWAP alignment; US: Gap and Go, short-only) since a
    combo that helps one market can actively hurt another (confirmed:
    the crypto combo hurt India, the India combo and an approximation
    of the crypto combo both did nothing/hurt on US data, and US's own
    Gap and Go strategy didn't transfer to India either -- every market
    genuinely needed its own from-scratch strategy, not a shared one).
    setup_log is optional and only used by check_watching_us() (see its
    docstring) -- crypto/India ignore it, unchanged from before.
    capital already has committed_capital() subtracted by the caller
    (main()) -- if that leaves nothing free, skip outright rather than
    let position_size() size a qty=0 alert (no minimum-qty guard exists
    downstream, so a fully-committed pool would otherwise still fire a
    signal suggesting 0 units, which isn't a real trade)."""
    if capital <= 0:
        return None
    if market == "crypto":
        return check_watching_crypto(symbol, tradable, sym_state, closed_bars, last_closed, capital, market)
    if market == "india":
        return check_watching_india(symbol, tradable, sym_state, closed_bars, last_closed, capital, market)
    if market == "us":
        return check_watching_us(symbol, tradable, sym_state, closed_bars, last_closed, capital, market, setup_log)
    return check_watching_default(symbol, tradable, sym_state, closed_bars, last_closed, capital, market)


def check_watching_india(symbol, tradable, sym_state, closed_bars, last_closed, capital, market):
    """India-specific gate on top of the same base breakout/breakdown/
    range-rejection logic as check_watching_default() -- selected via
    a 10-filter sweep (Supertrend, CPR, 5-EMA, prior-day levels, RSI,
    Bollinger, VWAP -- techniques grounded in actual NSE retail/algo
    trading practice, not the crypto filter set, which backtesting
    showed actively hurts this market) plus a combinatorial search
    over the promising ones. Winner: RSI momentum + VWAP alignment --
    only let a fired setup through if RSI(14) confirms momentum in the
    trade's direction (>60 long / <40 short) AND price is on the
    correct side of the day's running VWAP.
    Backtest (40-symbol real opening-range-mover universe, 60 days of
    15m data -- Yahoo's history cap for NSE): 50.0% win rate, PF 1.18,
    +Rs30.82 per Rs100 vs the unfiltered baseline's 49.5%/1.08/+Rs23.37
    -- a real, meaningful improvement, not just noise (488 of 780
    baseline trades survive the gate, not a drastic cut)."""
    alert = check_watching_default(symbol, tradable, sym_state, closed_bars, last_closed, capital, market)
    if alert is None:
        return None
    r = rsi(closed_bars)
    vwap = day_vwap(closed_bars, last_closed)
    close = last_closed["close"]
    if alert["direction"] == "long" and not (r > 60 and close >= vwap):
        return None
    if alert["direction"] == "short" and not (r < 40 and close <= vwap):
        return None
    return alert


def check_watching_us(symbol, tradable, sym_state, closed_bars, last_closed, capital, market, setup_log=None):
    """Gap and Go, short-only -- a standalone entry strategy, not a filter
    on check_watching_default() (that base breakout/breakdown/range-
    rejection logic backtested as a net LOSER on US data, PF 0.78, and
    neither India's RSI+VWAP combo nor an approximation of crypto's
    retest/2-bar/ADX combo rescued it when transplanted here -- US
    genuinely needed its own strategy, researched from real US
    day-trading practice rather than reused from another market).

    Mechanic: an overnight gap down of >=1.5% (today's session open vs.
    the prior session's close) locks the day to short-only. Once the
    first 30 minutes (first two 15m bars) of the session complete,
    their high/low become the confirmation range. A confirmed close
    below that range's low fires the entry (stop = range high + 0.5x
    ATR, no fixed target -- trail via check_open(), same as every other
    strategy in this file). Only long-only fired more (56.9% win, PF
    1.14) but was much weaker and isn't implemented -- this is short
    only, deliberately.

    Backtest (real 40-symbol US_UNIVERSE, 60 days of 15m data -- Yahoo's
    history cap): 113 trades, 64.6% win, PF 2.17, +$9.48 per $100.
    Held up on a chronological first/second-half out-of-sample split
    (PF 1.94 -> 2.38, improved rather than decayed) and isn't driven by
    one lucky trade (PF only drops to 1.89 with the single largest
    trade removed). The real caveat, shipped anyway with eyes open:
    it IS symbol-concentrated -- MARA/AAL/GM alone are ~76% of the net
    profit, and the full long+short combo (not what's implemented here)
    was 85% concentrated in just 3 symbols. n=113 is also thin next to
    crypto's 2,127-trade or India's 488-trade validation. Tested and
    explicitly does NOT transfer to India (gap frequency there is 4.9%
    of symbol-days vs US's 24.3% -- PSU banks/energy stocks don't gap
    like US mid-caps -- so this function is US-only by design, not
    reused for India's dispatch path).

    setup_log (optional) is a defense-in-depth guard on top of the
    sym_state.gap_fired flag above: on 2026-08-26, MARA fired twice on
    the same NY trading day (20:30 and 22:25 IST) despite gap_fired
    being correctly True and persisted the whole time -- confirmed via
    git history that state.json was NOT stale or racing (the second
    run's push landed cleanly on top of the first, no rejected push,
    no retry). The exact mechanism was never pinned down (reproducing
    with fresh live data doesn't trigger it, so it likely depended on
    the specific bar window Yahoo returned at that moment), but the
    fix doesn't require knowing why: cross-checking the append-only
    setup_log for an existing gap_and_go_short fired for this symbol
    on this NY date is a second, independent check that can't desync
    from sym_state the same way, whatever the original cause was."""
    day = us_date(last_closed["open_time"])
    day_str = day.isoformat()
    today_bars = [b for b in closed_bars if us_date(b["open_time"]) == day]

    if sym_state.get("gap_date") != day_str:
        prior_bars = [b for b in closed_bars if us_date(b["open_time"]) != day]
        sym_state["gap_date"] = day_str
        sym_state["gap_direction"] = None
        sym_state["gap_fired"] = False
        if prior_bars and today_bars:
            prior_close = prior_bars[-1]["close"]
            today_open = today_bars[0]["open"]
            gap_pct = (today_open - prior_close) / prior_close if prior_close else 0
            if gap_pct <= -GAP_THRESHOLD_PCT_US:
                sym_state["gap_direction"] = "short"

    if sym_state.get("gap_direction") != "short" or sym_state.get("gap_fired"):
        return None
    if len(today_bars) < 2:
        return None  # opening range not established yet

    if setup_log:
        for e in setup_log:
            if e["symbol"] != symbol or e["type"] != "gap_and_go_short":
                continue
            fired_ms = int(datetime.fromisoformat(e["fired_at"]).timestamp() * 1000)
            if us_date(fired_ms) == day:
                sym_state["gap_fired"] = True  # resync the flag since setup_log caught what it missed
                return None

    range_high = max(b["high"] for b in today_bars[:2])
    range_low = min(b["low"] for b in today_bars[:2])
    close = last_closed["close"]
    if close >= range_low:
        return None

    n = atr(closed_bars)
    stop = range_high + 0.5 * n
    losses = sym_state.get("consecutive_losses", 0)
    wins = sym_state.get("consecutive_wins", 0)
    qty = position_size(capital, close, stop, losses, leverage=LEVERAGE_BY_MARKET.get(market, 1), consecutive_wins=wins)
    vol = last_closed["volume"]
    vol_avg = avg_volume(closed_bars[-10:-1])
    tag = "" if tradable else " (analysis only)"
    text = build_alert_text(
        f"{symbol} GAP AND GO (breakdown){tag}\n\n"
        f"SELL\nEntry: {close:,.4g}\nStoploss: {stop:,.4g}\nVolume: ~{qty:.6g} units\n"
        f"Take profit: Keep trailing (no fixed target)\n"
        f"{expected_profit_line(close, stop, qty, currency='$')}\n\n"
        f"Gapped down and broke the opening-range low {range_low:,.4g} on a confirmed close.",
        symbol=symbol, price=close,
    )
    sym_state["gap_fired"] = True
    return {"text": text, "type": "gap_and_go_short", "direction": "short", "entry": close, "stop": stop, "qty": qty, "target": None, "vol_ratio": vol / vol_avg if vol_avg else 0}


def check_watching_crypto(symbol, tradable, sym_state, closed_bars, last_closed, capital, market):
    """Crypto-only entry logic -- three filters layered on the same base
    breakout/breakdown/range-rejection setups, selected via a 176-combo
    backtest sweep (2 years of 15m data, 12-symbol watchlist) and then
    validated out-of-sample (picked on year 1, re-tested on year 2 to
    confirm the edge wasn't a fluke of the selection window):
      - 2-bar confirmation: a breakout/breakdown must hold for a second
        consecutive closed bar, not just one, before it's treated as real.
      - Retest entry: after that 2-bar confirmation, wait for price to
        pull back to the broken level and hold before entering, instead
        of chasing the confirmation bar itself.
      - ADX ranging-regime gate (ADX <= 25) on range-rejection trades
        only -- mean-reversion setups lose disproportionately when a
        real trend is running; skip them on strong-trend days.
    In-sample: 55.2% win rate, PF 1.22, +$16.02 across 201 setups (12
    symbols, 2yr). Out-of-sample validation on a 6-symbol subset that
    looked strong in year 1: only 51.2% win / PF 1.24 held up in year
    2 -- the honest expectation going forward is closer to that number
    than the in-sample one."""
    range_high = sym_state["range_high"]
    range_low = sym_state["range_low"]
    close = last_closed["close"]
    vol = last_closed["volume"]
    vol_avg = avg_volume(closed_bars[-10:-1])
    trend_ema = ema([b["close"] for b in closed_bars[-(EMA_PERIOD * 3):]], EMA_PERIOD)
    n = atr(closed_bars)
    losses = sym_state.get("consecutive_losses", 0)
    wins = sym_state.get("consecutive_wins", 0)
    leverage = LEVERAGE_BY_MARKET.get(market, 1)
    already_alerted = sym_state.get("last_alert", {})
    bar_time = last_closed["close_time"]
    currency = "$"
    RETEST_EXPIRY_MS = 8 * 15 * 60 * 1000  # give a confirmed breakout up to 8 bars to retest before giving up
    ADX_MAX_FOR_REJECTION = 25

    if close > range_high and vol > vol_avg:
        if trend_ema and close < trend_ema:
            return None
        if already_alerted.get("type") == "breakout_long" and already_alerted.get("level") == range_high:
            return None
        if len(closed_bars) < 2 or not (closed_bars[-2]["close"] > range_high * 0.999):
            return None  # 2-bar confirmation not met yet
        pending = sym_state.get("pending") or {}
        if pending.get("type") != "breakout_long" or pending.get("level") != range_high:
            sym_state["pending"] = {"type": "breakout_long", "level": range_high, "expires": bar_time + RETEST_EXPIRY_MS}
            return None
        if not (last_closed["low"] <= range_high * 1.003 and close > range_high):
            if bar_time > pending.get("expires", 0):
                sym_state["pending"] = None
            return None
        sym_state["pending"] = None
        stop = last_closed["low"] - 0.5 * n
        qty = position_size(capital, close, stop, losses, leverage=leverage, consecutive_wins=wins)
        text = build_alert_text(
            f"{symbol} BREAKOUT (confirmed + retest held)\n\n"
            f"BUY\nEntry: {close:,.4g}\nStoploss: {stop:,.4g}\nVolume: ~{qty:.6g} units\n"
            f"Take profit: Keep trailing (no fixed target)\n"
            f"{expected_profit_line(close, stop, qty, currency=currency)}\n\n"
            f"Vol {vol:,.1f} vs avg {vol_avg:,.1f}, above 10-EMA ({trend_ema:,.4g}).",
            symbol=symbol, price=close,
        )
        sym_state["last_alert"] = {"type": "breakout_long", "level": range_high, "bar_time": bar_time}
        return {"text": text, "type": "breakout_long", "direction": "long", "entry": close, "stop": stop, "qty": qty, "target": None, "vol_ratio": vol / vol_avg if vol_avg else 0}

    if close < range_low and vol > vol_avg:
        if trend_ema and close > trend_ema:
            return None
        if already_alerted.get("type") == "breakdown_short" and already_alerted.get("level") == range_low:
            return None
        if len(closed_bars) < 2 or not (closed_bars[-2]["close"] < range_low * 1.001):
            return None
        pending = sym_state.get("pending") or {}
        if pending.get("type") != "breakdown_short" or pending.get("level") != range_low:
            sym_state["pending"] = {"type": "breakdown_short", "level": range_low, "expires": bar_time + RETEST_EXPIRY_MS}
            return None
        if not (last_closed["high"] >= range_low * 0.997 and close < range_low):
            if bar_time > pending.get("expires", 0):
                sym_state["pending"] = None
            return None
        sym_state["pending"] = None
        stop = last_closed["high"] + 0.5 * n
        qty = position_size(capital, close, stop, losses, leverage=leverage, consecutive_wins=wins)
        text = build_alert_text(
            f"{symbol} BREAKDOWN (confirmed + retest held)\n\n"
            f"SELL\nEntry: {close:,.4g}\nStoploss: {stop:,.4g}\nVolume: ~{qty:.6g} units\n"
            f"Take profit: Keep trailing (no fixed target)\n"
            f"{expected_profit_line(close, stop, qty, currency=currency)}\n\n"
            f"Vol {vol:,.1f} vs avg {vol_avg:,.1f}, below 10-EMA ({trend_ema:,.4g}).",
            symbol=symbol, price=close,
        )
        sym_state["last_alert"] = {"type": "breakdown_short", "level": range_low, "bar_time": bar_time}
        return {"text": text, "type": "breakdown_short", "direction": "short", "entry": close, "stop": stop, "qty": qty, "target": None, "vol_ratio": vol / vol_avg if vol_avg else 0}

    near_low = last_closed["low"] <= range_low * (1 + REJECTION_BUFFER_PCT)
    bullish_rejection = close > (last_closed["low"] + last_closed["high"]) / 2
    if near_low and bullish_rejection and close < range_high:
        if trend_ema and close < trend_ema:
            return None
        adx_val = adx(closed_bars)
        if adx_val is not None and adx_val > ADX_MAX_FOR_REJECTION:
            return None
        if already_alerted.get("type") != "range_long_rejection" or already_alerted.get("bar_time") != bar_time:
            if len(closed_bars) >= 2 and not (closed_bars[-2]["low"] <= range_low * (1 + REJECTION_BUFFER_PCT * 3)):
                return None
            stop = last_closed["low"] - 0.3 * n
            qty = position_size(capital, close, stop, losses, leverage=leverage, consecutive_wins=wins)
            adx_display = f"{adx_val:.0f}" if adx_val is not None else "n/a"
            text = build_alert_text(
                f"{symbol} RANGE REJECTION (bullish)\n\n"
                f"BUY\nEntry: {close:,.4g}\nStoploss: {stop:,.4g}\nVolume: ~{qty:.6g} units\n"
                f"Take profit: {range_high:,.4g} (range high)\n"
                f"{expected_profit_line(close, stop, qty, range_high, currency=currency)}\n\n"
                f"Wicked to {last_closed['low']:,.4g} near range low {range_low:,.4g}, closed upper half. "
                f"ADX {adx_display} confirms ranging regime.",
                symbol=symbol, price=close,
            )
            sym_state["last_alert"] = {"type": "range_long_rejection", "bar_time": bar_time}
            return {"text": text, "type": "range_long_rejection", "direction": "long", "entry": close, "stop": stop, "qty": qty, "target": range_high, "vol_ratio": vol / vol_avg if vol_avg else 0}
        return None

    near_high = last_closed["high"] >= range_high * (1 - REJECTION_BUFFER_PCT)
    bearish_rejection = close < (last_closed["low"] + last_closed["high"]) / 2
    if near_high and bearish_rejection and close > range_low:
        if trend_ema and close > trend_ema:
            return None
        adx_val = adx(closed_bars)
        if adx_val is not None and adx_val > ADX_MAX_FOR_REJECTION:
            return None
        if already_alerted.get("type") != "range_short_rejection" or already_alerted.get("bar_time") != bar_time:
            if len(closed_bars) >= 2 and not (closed_bars[-2]["high"] >= range_high * (1 - REJECTION_BUFFER_PCT * 3)):
                return None
            stop = last_closed["high"] + 0.3 * n
            qty = position_size(capital, close, stop, losses, leverage=leverage, consecutive_wins=wins)
            adx_display = f"{adx_val:.0f}" if adx_val is not None else "n/a"
            text = build_alert_text(
                f"{symbol} RANGE REJECTION (bearish)\n\n"
                f"SELL\nEntry: {close:,.4g}\nStoploss: {stop:,.4g}\nVolume: ~{qty:.6g} units\n"
                f"Take profit: {range_low:,.4g} (range low)\n"
                f"{expected_profit_line(close, stop, qty, range_low, currency=currency)}\n\n"
                f"Wicked to {last_closed['high']:,.4g} near range high {range_high:,.4g}, closed lower half. "
                f"ADX {adx_display} confirms ranging regime.",
                symbol=symbol, price=close,
            )
            sym_state["last_alert"] = {"type": "range_short_rejection", "bar_time": bar_time}
            return {"text": text, "type": "range_short_rejection", "direction": "short", "entry": close, "stop": stop, "qty": qty, "target": range_low, "vol_ratio": vol / vol_avg if vol_avg else 0}
        return None

    if range_low < close < range_high:
        sym_state["last_alert"] = {}
    recent_high = max(b["high"] for b in closed_bars[-10:])
    recent_low = min(b["low"] for b in closed_bars[-10:])
    if recent_high > range_high:
        sym_state["range_high"] = recent_high
    if recent_low < range_low:
        sym_state["range_low"] = recent_low
    return None


def check_watching_default(symbol, tradable, sym_state, closed_bars, last_closed, capital, market):
    """Returns None if nothing fired, or a dict for a fired signal:
    {"text": <fully-formed alert text, price/news already baked in>,
     "type", "direction", "entry", "stop", "qty", "target"} -- the
    structured fields are what main() uses to open a shadow-tracking
    entry (see setup_log) so every fired setup's real outcome gets
    recorded whether or not the user takes it. Does NOT send -- main()
    collects the text across the whole scan and sends it as one batched
    message instead of one Telegram send per symbol."""
    range_high = sym_state["range_high"]
    range_low = sym_state["range_low"]
    close = last_closed["close"]
    vol = last_closed["volume"]
    vol_avg = avg_volume(closed_bars[-10:-1])
    trend_ema = ema([b["close"] for b in closed_bars[-(EMA_PERIOD * 3):]], EMA_PERIOD)
    n = atr(closed_bars)
    losses = sym_state.get("consecutive_losses", 0)
    wins = sym_state.get("consecutive_wins", 0)
    leverage = LEVERAGE_BY_MARKET.get(market, 1)
    already_alerted = sym_state.get("last_alert", {})
    bar_time = last_closed["close_time"]
    tag = "" if tradable else " (analysis only -- not paper-tradable, use your own broker if acting on this)"
    currency = "Rs" if symbol.endswith(".NS") else "$"

    if close > range_high and vol > vol_avg:
        if trend_ema and close < trend_ema:
            return None
        if already_alerted.get("type") == "breakout_long" and already_alerted.get("level") == range_high:
            return None
        stop = last_closed["low"] - 0.5 * n
        qty = position_size(capital, close, stop, losses, leverage=leverage, consecutive_wins=wins)
        text = build_alert_text(
            f"{symbol} BREAKOUT (confirmed close){tag}\n\n"
            f"BUY\nEntry: {close:,.4g}\nStoploss: {stop:,.4g}\nVolume: ~{qty:.6g} units\n"
            f"Take profit: Keep trailing (no fixed target)\n"
            f"{expected_profit_line(close, stop, qty, currency=currency)}\n\n"
            f"Vol {vol:,.1f} vs avg {vol_avg:,.1f}, above 10-EMA ({trend_ema:,.4g}).",
            symbol=symbol, price=close,
        )
        sym_state["last_alert"] = {"type": "breakout_long", "level": range_high, "bar_time": bar_time}
        return {"text": text, "type": "breakout_long", "direction": "long", "entry": close, "stop": stop, "qty": qty, "target": None, "vol_ratio": vol / vol_avg if vol_avg else 0}

    if close < range_low and vol > vol_avg:
        if trend_ema and close > trend_ema:
            return None
        if already_alerted.get("type") == "breakdown_short" and already_alerted.get("level") == range_low:
            return None
        stop = last_closed["high"] + 0.5 * n
        qty = position_size(capital, close, stop, losses, leverage=leverage, consecutive_wins=wins)
        text = build_alert_text(
            f"{symbol} BREAKDOWN (confirmed close){tag}\n\n"
            f"SELL\nEntry: {close:,.4g}\nStoploss: {stop:,.4g}\nVolume: ~{qty:.6g} units\n"
            f"Take profit: Keep trailing (no fixed target)\n"
            f"{expected_profit_line(close, stop, qty, currency=currency)}\n\n"
            f"Vol {vol:,.1f} vs avg {vol_avg:,.1f}, below 10-EMA ({trend_ema:,.4g}).",
            symbol=symbol, price=close,
        )
        sym_state["last_alert"] = {"type": "breakdown_short", "level": range_low, "bar_time": bar_time}
        return {"text": text, "type": "breakdown_short", "direction": "short", "entry": close, "stop": stop, "qty": qty, "target": None, "vol_ratio": vol / vol_avg if vol_avg else 0}

    near_low = last_closed["low"] <= range_low * (1 + REJECTION_BUFFER_PCT)
    bullish_rejection = close > (last_closed["low"] + last_closed["high"]) / 2
    if near_low and bullish_rejection and close < range_high:
        # Same trend filter as breakouts -- backtesting showed rejection
        # trades taken against the prevailing trend (esp. bearish/short
        # rejections in an uptrend) were the single biggest source of
        # losses (-$38 combined, vs +$53 for the trend-agreeing long
        # rejections, over the same 60-day sample).
        if trend_ema and close < trend_ema:
            return None
        if already_alerted.get("type") != "range_long_rejection" or already_alerted.get("bar_time") != bar_time:
            stop = last_closed["low"] - 0.3 * n
            qty = position_size(capital, close, stop, losses, leverage=leverage, consecutive_wins=wins)
            text = build_alert_text(
                f"{symbol} RANGE REJECTION (bullish){tag}\n\n"
                f"BUY\nEntry: {close:,.4g}\nStoploss: {stop:,.4g}\nVolume: ~{qty:.6g} units\n"
                f"Take profit: {range_high:,.4g} (range high)\n"
                f"{expected_profit_line(close, stop, qty, range_high, currency=currency)}\n\n"
                f"Wicked to {last_closed['low']:,.4g} near range low {range_low:,.4g}, closed upper half.",
                symbol=symbol, price=close,
            )
            sym_state["last_alert"] = {"type": "range_long_rejection", "bar_time": bar_time}
            return {"text": text, "type": "range_long_rejection", "direction": "long", "entry": close, "stop": stop, "qty": qty, "target": range_high, "vol_ratio": vol / vol_avg if vol_avg else 0}
        return None

    near_high = last_closed["high"] >= range_high * (1 - REJECTION_BUFFER_PCT)
    bearish_rejection = close < (last_closed["low"] + last_closed["high"]) / 2
    if near_high and bearish_rejection and close > range_low:
        if trend_ema and close > trend_ema:
            return None
        if already_alerted.get("type") != "range_short_rejection" or already_alerted.get("bar_time") != bar_time:
            stop = last_closed["high"] + 0.3 * n
            qty = position_size(capital, close, stop, losses, leverage=leverage, consecutive_wins=wins)
            text = build_alert_text(
                f"{symbol} RANGE REJECTION (bearish){tag}\n\n"
                f"SELL\nEntry: {close:,.4g}\nStoploss: {stop:,.4g}\nVolume: ~{qty:.6g} units\n"
                f"Take profit: {range_low:,.4g} (range low)\n"
                f"{expected_profit_line(close, stop, qty, range_low, currency=currency)}\n\n"
                f"Wicked to {last_closed['high']:,.4g} near range high {range_high:,.4g}, closed lower half.",
                symbol=symbol, price=close,
            )
            sym_state["last_alert"] = {"type": "range_short_rejection", "bar_time": bar_time}
            return {"text": text, "type": "range_short_rejection", "direction": "short", "entry": close, "stop": stop, "qty": qty, "target": range_low, "vol_ratio": vol / vol_avg if vol_avg else 0}
        return None

    if range_low < close < range_high:
        sym_state["last_alert"] = {}
    recent_high = max(b["high"] for b in closed_bars[-10:])
    recent_low = min(b["low"] for b in closed_bars[-10:])
    if recent_high > range_high:
        sym_state["range_high"] = recent_high
    if recent_low < range_low:
        sym_state["range_low"] = recent_low
    return None


def market_of(symbol):
    """Same derivation as report.py's market_of() -- duplicated rather than
    imported since monitor.py and report.py are meant to stay independently
    runnable. Used here only to recover which market a HISTORICAL setup_log
    entry belongs to (entries don't store market explicitly), for
    compute_bucket_confidence() below."""
    if symbol.endswith(".NS"):
        return "india"
    if "-USD" in symbol:
        return "crypto"
    if symbol.endswith("-FUT"):
        return "india_futures"
    return "us"


def compute_bucket_confidence(setup_log, market, setup_type, direction):
    """Self-learning groundwork, step 1: a smoothed historical win rate for
    this exact (market, setup_type, direction) bucket -- e.g. "crypto
    breakdown_short" or "us gap_and_go_short". Beta(1,1)/Laplace-smoothed
    ((wins+1)/(total+2)) so it starts neutral at 0.5 with zero data and can
    never read as false 100%/0% certainty off a thin sample -- the exact
    NIFTY-futures trap (a 20-trade sample read as validated) this project
    already got burned by once.

    Deliberately NOT wired into which setups fire, get surfaced, or how
    they're sized -- purely observational, logged on every new setup so a
    real history exists to eventually design a confidence-weighted ranking
    from. Doing that FOR REAL requires the same backtested proof every
    other live change in this bot needed (see tonight's win-throttle: an
    idea that sounded obviously right and measurably wasn't once tested).
    There isn't remotely enough accumulated data yet for that -- this
    function's whole job right now is making sure that data starts
    existing, not making decisions with it prematurely."""
    matches = [
        e for e in setup_log
        if e.get("resolved") and e.get("outcome") is not None
        and e.get("type") == setup_type and e.get("direction") == direction
        and market_of(e["symbol"]) == market
    ]
    total = len(matches)
    wins = sum(1 for e in matches if e["outcome"]["pnl_per_unit"] > 0)
    confidence = (wins + 1) / (total + 2)
    return {"wins": wins, "total": total, "confidence": round(confidence, 4)}


def log_trade(sym_state, direction, entry, exit_price, pnl_per_unit, exit_reason):
    qty = sym_state.get("entry_qty")
    sym_state.setdefault("trade_journal", []).append({
        "direction": direction, "entry": entry, "exit": exit_price,
        "qty": qty, "pnl_per_unit": pnl_per_unit,
        "pnl_total": pnl_per_unit * qty if qty else None,
        "exit_reason": exit_reason,
        "closed_at": datetime.now(timezone.utc).isoformat(),
    })


def check_open(symbol, tradable, sym_state, closed_bars, last_closed, notify=True):
    """notify=False runs the exact same trailing-stop/target/stop-hit
    logic silently -- used to shadow-track every fired setup's real
    outcome (hit target vs stopped out) whether or not the user actually
    took it, without generating a single extra Telegram message."""
    direction = sym_state["direction"]
    stop = sym_state["stop_loss"]
    entry = sym_state["entry_price"]
    close = last_closed["close"]
    n = atr(closed_bars)
    extreme = sym_state.get("extreme_since_entry", entry)
    # Real-money tag uses `notify`, not the static per-market `tradable`
    # flag -- this function only ever notifies (sends a real Telegram
    # message) for a position the user has actually taken (see main()'s
    # notify=log_entry.get("taken", False)), so a message that reaches
    # the user here is never "analysis only" regardless of which market
    # it's in. `tradable` still governs the tag on a setup's FIRST-fire
    # alert (check_watching_*), where nothing has been taken yet and the
    # warning is genuinely correct.
    tag = "" if notify else " (analysis only)"

    tp = sym_state.get("take_profit_target")

    if direction == "long":
        extreme = max(extreme, last_closed["high"])
        sym_state["extreme_since_entry"] = extreme
        current_profit = close - entry
        peak_profit = max(sym_state.get("peak_profit_per_unit", 0), extreme - entry, current_profit)
        sym_state["peak_profit_per_unit"] = peak_profit

        # Take-profit target (range-rejection trades only -- breakouts
        # have none, "keep trailing"). Checked before the stop so a bar
        # that gaps through both hits the better-for-the-trade exit.
        # Previously this target was quoted in the entry alert text but
        # never actually enforced -- backtesting showed that dead-code
        # gap was letting winners ride the same loose trail as everything
        # else instead of banking at the promised level.
        if tp is not None and close >= tp:
            if notify:
                send_telegram(f"{symbol} TAKE PROFIT HIT -- long{tag}\n\nClose {close:,.4g} reached target {tp:,.4g}. Close now if you haven't already.", symbol=symbol, price=close)
            pnl = close - entry
            log_trade(sym_state, "long", entry, close, pnl, "take_profit")
            sym_state["consecutive_losses"] = 0
            sym_state["consecutive_wins"] = sym_state.get("consecutive_wins", 0) + 1
            rearm_to_watching(sym_state, closed_bars)
            return

        if close < stop:
            if notify:
                send_telegram(f"{symbol} STOP HIT -- long{tag}\n\nClose {close:,.4g} broke below stop {stop:,.4g}. Sell now if you haven't already.", symbol=symbol, price=close)
            pnl = close - entry
            log_trade(sym_state, "long", entry, close, pnl, "stop_hit")
            if pnl >= 0:
                sym_state["consecutive_losses"] = 0
                sym_state["consecutive_wins"] = sym_state.get("consecutive_wins", 0) + 1
            else:
                sym_state["consecutive_losses"] = sym_state.get("consecutive_losses", 0) + 1
                sym_state["consecutive_wins"] = 0
            rearm_to_watching(sym_state, closed_bars)
            return

        # Trailing stop: ATR-based baseline, PLUS a profit-lock floor once
        # there's meaningful profit -- guarantees protecting at least
        # PROFIT_LOCK_FRACTION of the peak gain once peak profit exceeds
        # PROFIT_LOCK_FLOOR_ATR_MULT x ATR, instead of a pure ATR trail
        # that can give back most of a big move before it catches up
        # (the original SOL problem). Backtested (60d, 2,127 trades) to
        # cut average giveback on winners from 58% to 55%.
        candidate_stop = extreme - TRAIL_ATR_MULT * n
        if peak_profit > PROFIT_LOCK_FLOOR_ATR_MULT * n:
            candidate_stop = max(candidate_stop, entry + PROFIT_LOCK_FRACTION * peak_profit)
        if candidate_stop > stop * 1.001:
            sym_state["stop_loss"] = candidate_stop
            locked_pct = (candidate_stop - entry) / peak_profit * 100 if peak_profit > 0 else 0
            if notify:
                send_telegram(f"{symbol} long -- trail your stop{tag}\n\nNew high {extreme:,.4g}. Move stop from {stop:,.4g} to {candidate_stop:,.4g} (locks ~{locked_pct:.0f}% of peak gain).", symbol=symbol, price=close)
            return

        # Take-profit heads-up: based on giveback from the peak profit
        # actually reached, not an ATR-relative floor that can
        # contradict itself in a fast reversal. Fires earlier (25%
        # giveback) than the hard profit-lock stop above -- an early
        # warning before the guaranteed floor even matters.
        giveback_pct = (peak_profit - current_profit) / peak_profit if peak_profit > 0 else 0
        if peak_profit > 0.5 * n and giveback_pct > 0.25:
            if notify:
                send_telegram(f"{symbol} long -- consider taking profit{tag}\n\nPeak gain was {peak_profit:,.4g}/unit, now {current_profit:,.4g}/unit -- given back {giveback_pct*100:.0f}%. Still in profit; your call.", symbol=symbol, price=close)

    elif direction == "short":
        extreme = min(extreme, last_closed["low"])
        sym_state["extreme_since_entry"] = extreme
        current_profit = entry - close
        peak_profit = max(sym_state.get("peak_profit_per_unit", 0), entry - extreme, current_profit)
        sym_state["peak_profit_per_unit"] = peak_profit

        if tp is not None and close <= tp:
            if notify:
                send_telegram(f"{symbol} TAKE PROFIT HIT -- short{tag}\n\nClose {close:,.4g} reached target {tp:,.4g}. Close now if you haven't already.", symbol=symbol, price=close)
            pnl = entry - close
            log_trade(sym_state, "short", entry, close, pnl, "take_profit")
            sym_state["consecutive_losses"] = 0
            rearm_to_watching(sym_state, closed_bars)
            return

        if close > stop:
            if notify:
                send_telegram(f"{symbol} STOP HIT -- short{tag}\n\nClose {close:,.4g} broke above stop {stop:,.4g}. Buy back / close now if you haven't already.", symbol=symbol, price=close)
            pnl = entry - close
            log_trade(sym_state, "short", entry, close, pnl, "stop_hit")
            if pnl >= 0:
                sym_state["consecutive_losses"] = 0
                sym_state["consecutive_wins"] = sym_state.get("consecutive_wins", 0) + 1
            else:
                sym_state["consecutive_losses"] = sym_state.get("consecutive_losses", 0) + 1
                sym_state["consecutive_wins"] = 0
            rearm_to_watching(sym_state, closed_bars)
            return

        candidate_stop = extreme + TRAIL_ATR_MULT * n
        if peak_profit > PROFIT_LOCK_FLOOR_ATR_MULT * n:
            candidate_stop = min(candidate_stop, entry - PROFIT_LOCK_FRACTION * peak_profit)
        if candidate_stop < stop * 0.999:
            sym_state["stop_loss"] = candidate_stop
            locked_pct = (entry - candidate_stop) / peak_profit * 100 if peak_profit > 0 else 0
            if notify:
                send_telegram(f"{symbol} short -- trail your stop{tag}\n\nNew low {extreme:,.4g}. Move stop from {stop:,.4g} to {candidate_stop:,.4g} (locks ~{locked_pct:.0f}% of peak gain).", symbol=symbol, price=close)
            return

        giveback_pct = (peak_profit - current_profit) / peak_profit if peak_profit > 0 else 0
        if peak_profit > 0.5 * n and giveback_pct > 0.25:
            if notify:
                send_telegram(f"{symbol} short -- consider taking profit{tag}\n\nPeak gain was {peak_profit:,.4g}/unit, now {current_profit:,.4g}/unit -- given back {giveback_pct*100:.0f}%. Still in profit; your call.", symbol=symbol, price=close)


def main():
    # No more "open"/"fill"/"skip"/"close" Telegram tracking, and no more
    # fast 5-min "open positions only" cadence -- the user places real
    # stop-loss/take-profit orders on the exchange and self-manages
    # entries/exits entirely outside this bot now. Every run is a full
    # scan for new setups; shadow-tracking (setup_log) is the only thing
    # that still needs check_open()'s logic, purely as a silent
    # simulation.
    state = load_state()
    symbols_state = state.setdefault("symbols", {})
    capital_usd = state.get("capital_usd", 100)
    capital_inr = state.get("capital_inr", 100)
    watchlist = build_watchlist(state)

    setup_log = state.setdefault("setup_log", [])
    fired_this_scan = []  # (market, alert dict) -- ranked and trimmed after the full watchlist loop
    for entry in watchlist:
        symbol, market, tradable = entry["symbol"], entry["market"], entry["tradable"]
        try:
            bars = fetch_klines(symbol, market, limit=60)
        except Exception as e:
            print(f"{symbol}: fetch failed ({e}), skipping")
            continue
        if len(bars) < 15:
            print(f"{symbol}: not enough bars, skipping")
            continue
        closed_bars = bars[:-1]
        last_closed = closed_bars[-1]
        if is_stale(last_closed):
            print(f"{symbol}: stale (market likely closed), skipping")
            continue

        if symbol not in symbols_state:
            symbols_state[symbol] = default_symbol_state(closed_bars)
        sym_state = symbols_state[symbol]
        capital = capital_inr if market == "india" else capital_usd
        pool_markets = ("india",) if market == "india" else ("crypto", "us")
        capital = max(capital - committed_capital(setup_log, pool_markets), 0)

        # Shadow-track every setup this symbol has ever fired, whether or
        # not the user took it -- reuses check_open()'s exact trailing
        # stop/target/stop-hit logic against the bars already fetched
        # this cycle, so "did it actually reach the expected profit" has
        # a real answer instead of just the alert's promise. Silent
        # (notify=False) unless the entry is flagged "taken" (see
        # mark_taken.py) -- then the exact same trail/profit-lock/
        # stop/target Telegram messages check_open() already sends for
        # a real position fire for real, since this now IS the position
        # the user is actually in.
        for log_entry in setup_log:
            if log_entry["resolved"] or log_entry["symbol"] != symbol:
                continue
            shadow = log_entry["shadow"]
            before = len(shadow["trade_journal"])
            check_open(symbol, tradable, shadow, closed_bars, last_closed, notify=log_entry.get("taken", False))
            if len(shadow["trade_journal"]) > before:
                log_entry["resolved"] = True
                log_entry["outcome"] = shadow["trade_journal"][-1]
                # check_open() only updates the throttle counters on the
                # ephemeral shadow dict it was handed, not the real
                # per-symbol sym_state that position_size() actually
                # reads (a leftover from the older live-position-tracking
                # architecture) -- so the loss/win throttle in
                # position_size() was permanently inert regardless of
                # real streaks. Propagate the resolution to sym_state
                # here, the one place that's guaranteed to run for every
                # resolution regardless of whether the user took it.
                pnl = log_entry["outcome"]["pnl_per_unit"]
                if pnl >= 0:
                    sym_state["consecutive_losses"] = 0
                    sym_state["consecutive_wins"] = sym_state.get("consecutive_wins", 0) + 1
                else:
                    sym_state["consecutive_losses"] = sym_state.get("consecutive_losses", 0) + 1
                    sym_state["consecutive_wins"] = 0

        alert = check_watching(symbol, tradable, sym_state, closed_bars, last_closed, capital, market, setup_log)
        if alert:
            fired_this_scan.append((market, symbol, alert))

    # Best-of-N per market per scan: when multiple setups fire in the
    # same cycle, only the top 2 by volume ratio (how unusual this
    # bar's volume is vs. its own recent average -- the one conviction
    # signal every setup type already computes) actually get surfaced
    # to Telegram. Every fired setup still gets logged and shadow-
    # tracked regardless ("surfaced": False for the rest), so the
    # nightly report can later show whether this filtering is actually
    # picking better trades or just fewer of them. Ranked per market,
    # not globally -- crypto/India/US are separate capital pools, so a
    # strong US signal shouldn't crowd out an India one.
    #
    # Correlation guard: at most 1 surfaced per direction per market per
    # scan. Two same-direction fires in one market in one cycle (e.g.
    # BTC and ETH both breaking down together) usually means one macro
    # move set off multiple correlated symbols, not two independent
    # opportunities -- surfacing both would look like double conviction
    # when it's really the same bet twice. A different direction still
    # gets its own slot, since that's a genuinely different position.
    SURFACE_TOP_N = 2
    by_market = {}
    for market, symbol, alert in fired_this_scan:
        by_market.setdefault(market, []).append((symbol, alert))
    surfaced_keys = set()
    for market, items in by_market.items():
        ranked = sorted(items, key=lambda x: x[1].get("vol_ratio", 0), reverse=True)
        directions_used = set()
        picked = 0
        for symbol, alert in ranked:
            if picked >= SURFACE_TOP_N:
                break
            if alert["direction"] in directions_used:
                continue
            directions_used.add(alert["direction"])
            surfaced_keys.add((symbol, alert["type"], alert["entry"]))
            picked += 1

    fired_setups = []
    for market, symbol, alert in fired_this_scan:
        surfaced = (symbol, alert["type"], alert["entry"]) in surfaced_keys
        if surfaced:
            fired_setups.append(alert["text"])
        fired_at_dt = datetime.now(timezone.utc)
        setup_log.append({
            "symbol": symbol, "type": alert["type"], "direction": alert["direction"],
            "entry": alert["entry"], "stop": alert["stop"], "target": alert["target"],
            "qty": alert["qty"], "fired_at": fired_at_dt.isoformat(),
            "resolved": False, "outcome": None, "surfaced": surfaced, "taken": False,
            # Self-learning groundwork -- see compute_bucket_confidence()'s
            # docstring. Purely observational: not read anywhere that
            # affects which setups fire, surface, or how they're sized.
            # confidence_at_fire is computed from history strictly BEFORE
            # this entry (setup_log doesn't include it yet at append time),
            # so it can never leak this trade's own outcome into itself.
            # fired_hour_utc/fired_weekday_utc are cheap now, expensive to
            # reconstruct retroactively later if a time-of-day/day-of-week
            # pattern turns out to matter.
            "confidence_at_fire": compute_bucket_confidence(setup_log, market, alert["type"], alert["direction"]),
            "fired_hour_utc": fired_at_dt.hour,
            "fired_weekday_utc": fired_at_dt.weekday(),
            "shadow": {
                "direction": alert["direction"], "entry_price": alert["entry"],
                "entry_qty": alert["qty"], "stop_loss": alert["stop"],
                "extreme_since_entry": alert["entry"], "peak_profit_per_unit": 0,
                "take_profit_target": alert["target"], "consecutive_losses": 0, "consecutive_wins": 0,
                "trade_journal": [],
            },
        })

    if fired_setups:
        # One message per scan covering every surfaced setup, instead
        # of a separate Telegram send per symbol -- so several setups
        # in one scan is 1 notification to react to, not several.
        divider = "\n\n" + ("=" * 20) + "\n\n"
        header = f"{len(fired_setups)} setup(s) this scan:\n\n"
        send_telegram(header + divider.join(fired_setups))

    save_state(state)


if __name__ == "__main__":
    sys.exit(main())
