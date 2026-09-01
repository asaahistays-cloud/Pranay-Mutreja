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

import broker_bybit  # noqa: F401 -- kept for when crypto auto-execution resumes (see below), not wired in right now.
import broker_dhan  # noqa: F401 -- kept for when India auto-execution resumes (see below), not wired in right now.

# Real broker auto-execution is off entirely right now. US (Alpaca) was
# removed outright, not paused -- explicitly requested: shadow-tracking
# (setup_log below) already tells the user exactly what a fired setup
# would have done, so a real paper account duplicating that same
# outcome added no real information, just infrastructure to maintain.
#
# Crypto auto-execution is PAUSED, not removed -- broker_bybit.py works
# (real long+short futures, matches how these strategies were
# validated), but Bybit's CloudFront setup rejects requests from
# GitHub Actions' US-based runner IPs outright (confirmed directly:
# 403 "The Amazon CloudFront distribution is configured to block
# access from your country"). That's a structural conflict, not a bug
# to fix here: every offshore derivatives exchange checked (Bybit,
# Deribit) blocks US-origin traffic for their own regulatory reasons,
# and GitHub Actions always runs from the US -- resuming this needs
# either a static-IP relay in front of Bybit's calls, or a different
# platform that doesn't block US IPs.
#
# India auto-execution is PAUSED too -- Dhan's SANDBOX is exempt from
# the SEBI static-IP mandate that blocks real Indian broker APIs (see
# broker_dhan.py's module docstring), but confirmed directly that its
# sandbox sits behind an AWS load balancer (Server: awselb/2.0) that
# 403s every request -- GET and POST identically -- from GitHub
# Actions' shared, heavily-reused Azure IPs, almost certainly an
# AWS-managed IP-reputation WAF rule flagging automation-infrastructure
# traffic. A third, structurally different way to hit the same wall as
# crypto: GitHub Actions' cloud IPs read as suspicious to security
# infrastructure regardless of the underlying reason (geo-block,
# regulatory mandate, or reputation list). Resuming either needs a
# static IP that isn't recognizable as shared cloud/automation
# infrastructure. Commodities have no broker at all (alert-only,
# always, by design -- GC=F/NG=F futures aren't offered by any of
# these).
BROKERS = {}
BROKER_NAMES = {"india": "Dhan", "crypto": "Bybit"}  # both paused, names kept for when they resume

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
LEVERAGE_BY_MARKET = {"crypto": 10, "us": 1, "india": 1, "commodity": 1}
# From the real out-of-sample-validated seasonality backtest (2011-2026
# daily GC=F/NG=F, strong/weak months derived from the first half of
# years, tested clean on the held-out second half): gold held up
# (+47.5% compounded, 58.7% win rate), natural gas held up strongly
# (+128.7% compounded, 60.9% win rate). Stop distances below are 2x
# each symbol's real historical monthly return std dev (GC=F 4.77%,
# NG=F 14.81%) -- a monthly-hold position needs a stop calibrated to
# monthly moves, not 15m noise, so this is NOT the usual atr(closed_bars)
# on 15m bars every other setup in this file uses.
SEASONAL_STRONG_MONTHS = {"GC=F": {1, 2, 8}, "NG=F": {4, 6, 11}}
SEASONAL_WEAK_MONTHS = {"GC=F": {5, 9, 11}, "NG=F": {2, 7, 12}}
SEASONAL_STOP_PCT = {"GC=F": 0.095, "NG=F": 0.296}
EIA_STALE_DAYS = 10  # report updates weekly; if eia_check.py hasn't run in this long, treat its data as missing
GAP_THRESHOLD_PCT_US = 0.015  # overnight gap that locks check_watching_us()'s directional bias
# Tuned against real 15m production-code backtests (90 days crypto /
# 60 days US+India, real Coinbase/Yahoo data), not the original
# daily-bar research values -- see check_triple_ma()'s docstring.
# Swept 5-50 range; 8/16/25 was the strongest AND most stable choice
# (same result held across trend=20/30/40 at breakout=20 for Triple
# Threat below, which is itself a good robustness sign). Crypto: all
# 3 symbols individually profitable, split-sample held up in both
# halves. US: strong, improved out-of-sample. India: the weak leg,
# degrades out-of-sample -- known and accepted, not hidden.
TRIPLE_MA_FAST = 8
TRIPLE_MA_MED = 16
TRIPLE_MA_SLOW = 25
# Tuned the same way -- see check_triple_threat()'s docstring. Weaker
# and thinner-sampled than Triple MA (dozens of trades vs hundreds),
# and a GUESSED methodology (AlphaInsider never disclosed a real
# description for this name) -- shipped anyway per explicit direction,
# eyes open about both caveats.
TRIPLE_THREAT_TREND_PERIOD = 30
TRIPLE_THREAT_RSI_PERIOD = 14
TRIPLE_THREAT_BREAKOUT_PERIOD = 20
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
# Gold and natural gas only -- the two commodities where a real
# strategy (seasonality) actually validated out-of-sample. Silver and
# crude oil were tested the same way and failed (see the AlphaInsider/
# commodity strategy review) -- deliberately not included here rather
# than added speculatively.
COMMODITY_WATCHLIST = [{"symbol": s, "market": "commodity", "tradable": True} for s in ["GC=F", "NG=F"]]


def build_watchlist(state):
    watchlist = list(CRYPTO_WATCHLIST) + list(COMMODITY_WATCHLIST)
    for symbol in state.get("active_us_symbols", []):
        watchlist.append({"symbol": symbol, "market": "us", "tradable": True})
    for symbol in state.get("active_india_symbols", []):
        # Back to False -- Dhan sandbox auto-execution exists in code
        # but is paused (BROKERS above, blocked by an AWS WAF rule),
        # so "not paper-tradable, use your own broker" is accurate
        # again for now.
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


def check_triple_ma(symbol, tradable, sym_state, closed_bars, last_closed, capital, market):
    """Three Moving Averages -- the second cross-market candidate from
    the AlphaInsider strategy review (after DMI+DPO, crypto-only, still
    unshipped, and LINREG_CHANNEL, which failed its own 15m validation
    and was fully reverted). Daily-bar backtest: best Sharpe of all 12
    tested strategies on crypto (2.71), positive on US and India too,
    though weaker there. Simplest rules of anything tested (3 EMA
    lengths, no other parameters) -- lower overfitting surface than
    most of the others.

    Long when fast EMA > medium EMA > slow EMA AND this is a FRESH
    alignment (wasn't already true last call) -- catches the moment a
    trend starts, not every bar it continues. Short is the mirror.
    Applying both lessons already learned the hard way this session
    before this ever runs for real, not after:
      - own dedicated dedup field (triple_ma_regime), not the shared
        last_alert (DMI+DPO shipped with that bug first, confirmed via
        a live 15m backtest showing 3,498 spam trades in 90 days).
      - stop anchored to the actual bar (last_closed low/high), not an
        indicator level (LINREG_CHANNEL's first version anchored to
        the regression band itself, which a single extreme bar could
        push to the wrong side of entry).
    Periods (TRIPLE_MA_FAST/MED/SLOW) are the daily-bar-validated
    10/20/50 as placeholders ONLY -- not yet backtested at 15m. Same
    discipline as DMI+DPO and LINREG_CHANNEL: tune against real 15m
    data before this fires for real, don't assume the daily window
    transfers."""
    closes = [b["close"] for b in closed_bars]
    if len(closes) < TRIPLE_MA_SLOW:
        return None
    fast = ema(closes[-(TRIPLE_MA_FAST * 3):], TRIPLE_MA_FAST)
    med = ema(closes[-(TRIPLE_MA_MED * 3):], TRIPLE_MA_MED)
    slow = ema(closes[-(TRIPLE_MA_SLOW * 3):], TRIPLE_MA_SLOW)

    current_regime = None
    if fast > med > slow:
        current_regime = "long"
    elif fast < med < slow:
        current_regime = "short"
    prev_regime = sym_state.get("triple_ma_regime")
    sym_state["triple_ma_regime"] = current_regime
    if not current_regime or current_regime == prev_regime:
        return None

    close = last_closed["close"]
    losses = sym_state.get("consecutive_losses", 0)
    wins = sym_state.get("consecutive_wins", 0)
    leverage = LEVERAGE_BY_MARKET.get(market, 1)
    currency = "Rs" if symbol.endswith(".NS") else "$"
    n = atr(closed_bars)
    tag = "" if tradable else " (analysis only -- not paper-tradable, use your own broker if acting on this)"

    if current_regime == "long":
        # Candlestick confirmation gate -- crypto only, long only (see
        # bullish_candle_confirmed()'s docstring for the real 15m
        # validation behind this: a genuine, majority-positive edge
        # specifically for triple_ma_long on crypto, measurably HURT
        # elsewhere so deliberately not applied to US/India or to
        # triple_ma_short). Silently skips this fresh-alignment event
        # if unconfirmed -- triple_ma_regime is already set above, so
        # it won't retry until the next real regime change.
        if market == "crypto" and not bullish_candle_confirmed(closed_bars[-3:]):
            return None
        stop = last_closed["low"] - 2 * n
        if stop >= close:
            return None
        qty = position_size(capital, close, stop, losses, leverage=leverage, consecutive_wins=wins)
        confirm_note = ", candlestick-confirmed" if market == "crypto" else ""
        text = build_alert_text(
            f"{symbol} TRIPLE MA (long){tag}\n\n"
            f"BUY\nEntry: {close:,.4g}\nStoploss: {stop:,.4g}\nVolume: ~{qty:.6g} units\n"
            f"Take profit: Keep trailing (no fixed target)\n"
            f"{expected_profit_line(close, stop, qty, currency=currency)}\n\n"
            f"Fast EMA({TRIPLE_MA_FAST}) > med EMA({TRIPLE_MA_MED}) > slow EMA({TRIPLE_MA_SLOW}) -- fresh bullish alignment{confirm_note}.",
            symbol=symbol, price=close,
        )
        trigger_context = {
            "fast_ema": round(fast, 6), "med_ema": round(med, 6), "slow_ema": round(slow, 6),
            "periods": {"fast": TRIPLE_MA_FAST, "med": TRIPLE_MA_MED, "slow": TRIPLE_MA_SLOW},
        }
        return {"text": text, "type": "triple_ma_long", "direction": "long", "entry": close, "stop": stop, "qty": qty, "target": None, "vol_ratio": 1.0, "trigger_context": trigger_context}
    else:
        stop = last_closed["high"] + 2 * n
        if stop <= close:
            return None
        qty = position_size(capital, close, stop, losses, leverage=leverage, consecutive_wins=wins)
        text = build_alert_text(
            f"{symbol} TRIPLE MA (short){tag}\n\n"
            f"SELL\nEntry: {close:,.4g}\nStoploss: {stop:,.4g}\nVolume: ~{qty:.6g} units\n"
            f"Take profit: Keep trailing (no fixed target)\n"
            f"{expected_profit_line(close, stop, qty, currency=currency)}\n\n"
            f"Fast EMA({TRIPLE_MA_FAST}) < med EMA({TRIPLE_MA_MED}) < slow EMA({TRIPLE_MA_SLOW}) -- fresh bearish alignment.",
            symbol=symbol, price=close,
        )
        trigger_context = {
            "fast_ema": round(fast, 6), "med_ema": round(med, 6), "slow_ema": round(slow, 6),
            "periods": {"fast": TRIPLE_MA_FAST, "med": TRIPLE_MA_MED, "slow": TRIPLE_MA_SLOW},
        }
        return {"text": text, "type": "triple_ma_short", "direction": "short", "entry": close, "stop": stop, "qty": qty, "target": None, "vol_ratio": 1.0, "trigger_context": trigger_context}


def check_triple_threat(symbol, tradable, sym_state, closed_bars, last_closed, capital, market):
    """Triple Threat -- GUESSED methodology (AlphaInsider disclosed no
    real description for this one, just a name -- see the community
    strategy review). Interpreted as a 3-confirmation system since
    that's what "Triple Threat" most commonly names in retail TA: trend
    filter (price vs EMA) + momentum trigger (RSI crossing 50) +
    breakout confirmation (price breaking the recent N-bar high/low).
    Real 15m screen (pandas-engine, not yet this production version):
    best India result of anything tested (PF 2.11, 3/3 symbols), strong
    on US (PF 1.38, 3/3) and crypto (PF 1.21, 2/3) -- the only other
    candidate alongside Triple MA that looked genuinely positive across
    all 3 markets, hence the follow-up to the same production-code
    treatment. Being a GUESSED strategy stays true regardless of these
    numbers -- a good backtest of an invented rule isn't the same as
    validating AlphaInsider's actual (unknown) Triple Threat.

    RSI-crossing-50 is already a discrete single-bar event by
    construction (unlike DMI+DPO/Triple MA/LINREG_CHANNEL's persistent
    regime conditions), so it doesn't carry the same "fires every bar
    a condition holds true" risk those did -- confirmed empirically via
    the real 15m production validation before trusting that reasoning
    alone. Still uses a dedicated cross-direction field rather than the
    shared last_alert, on principle, matching the other 3 additions.
    Stop anchored to the actual bar, not an indicator level -- same
    fix applied to LINREG_CHANNEL after its first version got this
    wrong."""
    closes = [b["close"] for b in closed_bars]
    if len(closes) < TRIPLE_THREAT_TREND_PERIOD:
        return None
    trend = ema(closes[-(TRIPLE_THREAT_TREND_PERIOD * 3):], TRIPLE_THREAT_TREND_PERIOD)
    r_now = rsi(closed_bars, period=TRIPLE_THREAT_RSI_PERIOD)
    r_prev = rsi(closed_bars[:-1], period=TRIPLE_THREAT_RSI_PERIOD)
    lookback = closed_bars[-(TRIPLE_THREAT_BREAKOUT_PERIOD + 1):-1]
    if len(lookback) < TRIPLE_THREAT_BREAKOUT_PERIOD:
        return None
    roll_hi = max(b["high"] for b in lookback)
    roll_lo = min(b["low"] for b in lookback)
    close = last_closed["close"]

    r_cross_up = r_prev <= 50 < r_now
    r_cross_dn = r_prev >= 50 > r_now

    current_cross = "up" if r_cross_up else ("down" if r_cross_dn else None)
    prev_cross = sym_state.get("triple_threat_cross")
    if current_cross:
        sym_state["triple_threat_cross"] = current_cross

    fires_long = r_cross_up and current_cross != prev_cross and close > trend and close > roll_hi
    fires_short = r_cross_dn and current_cross != prev_cross and close < trend and close < roll_lo
    if not (fires_long or fires_short):
        return None

    losses = sym_state.get("consecutive_losses", 0)
    wins = sym_state.get("consecutive_wins", 0)
    leverage = LEVERAGE_BY_MARKET.get(market, 1)
    currency = "Rs" if symbol.endswith(".NS") else "$"
    n = atr(closed_bars)
    tag = "" if tradable else " (analysis only -- not paper-tradable, use your own broker if acting on this)"

    if fires_long:
        stop = last_closed["low"] - 2 * n
        if stop >= close:
            return None
        qty = position_size(capital, close, stop, losses, leverage=leverage, consecutive_wins=wins)
        text = build_alert_text(
            f"{symbol} TRIPLE THREAT (long){tag}\n\n"
            f"BUY\nEntry: {close:,.4g}\nStoploss: {stop:,.4g}\nVolume: ~{qty:.6g} units\n"
            f"Take profit: Keep trailing (no fixed target)\n"
            f"{expected_profit_line(close, stop, qty, currency=currency)}\n\n"
            f"Above EMA({TRIPLE_THREAT_TREND_PERIOD}) trend, RSI crossed above 50, broke the {TRIPLE_THREAT_BREAKOUT_PERIOD}-bar high {roll_hi:,.4g}.",
            symbol=symbol, price=close,
        )
        trigger_context = {
            "trend_ema": round(trend, 6), "rsi_prev": round(r_prev, 2), "rsi_now": round(r_now, 2),
            "breakout_level": roll_hi,
            "periods": {"trend": TRIPLE_THREAT_TREND_PERIOD, "rsi": TRIPLE_THREAT_RSI_PERIOD, "breakout": TRIPLE_THREAT_BREAKOUT_PERIOD},
        }
        return {"text": text, "type": "triple_threat_long", "direction": "long", "entry": close, "stop": stop, "qty": qty, "target": None, "vol_ratio": 1.0, "trigger_context": trigger_context}
    else:
        stop = last_closed["high"] + 2 * n
        if stop <= close:
            return None
        qty = position_size(capital, close, stop, losses, leverage=leverage, consecutive_wins=wins)
        text = build_alert_text(
            f"{symbol} TRIPLE THREAT (short){tag}\n\n"
            f"SELL\nEntry: {close:,.4g}\nStoploss: {stop:,.4g}\nVolume: ~{qty:.6g} units\n"
            f"Take profit: Keep trailing (no fixed target)\n"
            f"{expected_profit_line(close, stop, qty, currency=currency)}\n\n"
            f"Below EMA({TRIPLE_THREAT_TREND_PERIOD}) trend, RSI crossed below 50, broke the {TRIPLE_THREAT_BREAKOUT_PERIOD}-bar low {roll_lo:,.4g}.",
            symbol=symbol, price=close,
        )
        trigger_context = {
            "trend_ema": round(trend, 6), "rsi_prev": round(r_prev, 2), "rsi_now": round(r_now, 2),
            "breakout_level": roll_lo,
            "periods": {"trend": TRIPLE_THREAT_TREND_PERIOD, "rsi": TRIPLE_THREAT_RSI_PERIOD, "breakout": TRIPLE_THREAT_BREAKOUT_PERIOD},
        }
        return {"text": text, "type": "triple_threat_short", "direction": "short", "entry": close, "stop": stop, "qty": qty, "target": None, "vol_ratio": 1.0, "trigger_context": trigger_context}


def check_secondary_strategies(symbol, tradable, sym_state, closed_bars, last_closed, capital, market):
    """Tries the cross-market secondary strategies in order (Triple MA,
    then Triple Threat), used as the shared fallback at every point in
    check_watching_crypto()/india()/us() where the market's own primary
    logic didn't fire. Centralized here so adding a future candidate
    means editing one place, not four."""
    alert = check_triple_ma(symbol, tradable, sym_state, closed_bars, last_closed, capital, market)
    if alert:
        return alert
    return check_triple_threat(symbol, tradable, sym_state, closed_bars, last_closed, capital, market)


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


def dmi(bars, period=14):
    """+DI/-DI alongside ADX (same Wilder smoothing as adx() above) --
    needed for check_watching_crypto()'s DMI+DPO trend setup, which has
    to know WHICH way a trend is running, not just how strong it is."""
    if len(bars) < period * 2 + 1:
        return None, None, None
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
    adx_val = sum(sample) / len(sample) if sample else None
    return plus_di[-1], minus_di[-1], adx_val


def dpo(bars, period=20):
    """Detrended Price Oscillator -- price from `shift` bars ago minus
    the current period-SMA. Counterintuitive sign in a clean trend: a
    steady uptrend has an OLDER, lower reference price minus a newer,
    higher average -> DPO is NEGATIVE while the trend is accelerating,
    and only flips POSITIVE once price has recently pulled back/cooled
    off relative to that earlier level. So "DPO > 0" alongside a
    confirmed +DI bias (see dmi()) reads as "established uptrend, buy
    the pullback" -- not "price above its average" -- which is exactly
    the entry check_watching_crypto()'s DMI+DPO setup wants: don't chase
    the initial move, enter on the retracement."""
    shift = period // 2 + 1
    closes = [b["close"] for b in bars]
    if len(closes) < max(period, shift + 1):
        return None
    sma_now = sum(closes[-period:]) / period
    price_then = closes[-1 - shift]
    return price_then - sma_now


def _candle_body(bar):
    return abs(bar["close"] - bar["open"])


def _candle_lower_wick(bar):
    return min(bar["open"], bar["close"]) - bar["low"]


def bullish_candle_confirmed(recent_bars):
    """Real 15m production-code backtest (1yr, 7-symbol crypto
    watchlist, out-of-sample split both halves): requiring one of these
    5 bullish candlestick patterns on the fire bar improved
    triple_ma_long specifically -- n=1,386 confirmed (avg R +0.020) vs
    n=4,095 unconfirmed (avg R -0.012), consistently better on both
    halves for BTC/XRP/AVAX, consistently worse for SOL/NEAR, mixed on
    ETH/FET. A real, majority-positive edge, not a one-symbol fluke
    (unlike LINREG_CHANNEL, reverted earlier for exactly that failure
    mode) -- but modest and not universal, which is exactly why this
    gates ONLY triple_ma_long on crypto specifically, not every setup
    or every market (candlestick confirmation measurably HURT US and
    India performance in the same real-data testing -- these are
    reversal-pattern signals layered on trend-CONTINUATION setups, a
    logical mismatch outside this one validated case).

    Deliberately narrow pattern set (5 of the ~20 well-known bullish
    candlestick patterns) -- the ones this validation actually tested,
    not every pattern that exists."""
    if len(recent_bars) < 3:
        return False
    b1, b2, b3 = recent_bars[-3], recent_bars[-2], recent_bars[-1]

    # hammer: small body near the top, long lower wick, little/no upper wick
    r = b3["high"] - b3["low"]
    bd = _candle_body(b3)
    if r > 0 and bd > 0 and _candle_lower_wick(b3) >= 2 * bd and (b3["high"] - max(b3["open"], b3["close"])) <= 0.15 * r:
        return True
    # bullish engulfing
    if (b2["close"] < b2["open"] and b3["close"] > b3["open"]
            and b3["open"] <= b2["close"] and b3["close"] >= b2["open"] and _candle_body(b3) > _candle_body(b2)):
        return True
    # bullish harami
    if (b2["close"] < b2["open"] and b3["close"] > b3["open"]
            and b3["open"] >= b2["close"] and b3["close"] <= b2["open"]):
        return True
    # piercing line
    if b2["close"] < b2["open"] and b3["close"] > b3["open"]:
        prev_mid = (b2["open"] + b2["close"]) / 2
        if b3["open"] < b2["close"] and prev_mid < b3["close"] < b2["open"]:
            return True
    # morning star
    if b1["close"] < b1["open"] and _candle_body(b2) < _candle_body(b1) * 0.5 and b3["close"] > b3["open"]:
        b1_mid = (b1["open"] + b1["close"]) / 2
        if b3["close"] > b1_mid:
            return True
    return False


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
    positions sharing this capital pool -- crypto, US, and India each
    draw from their own separate pot (see main()'s capital assignment
    below). Without this, every new
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

def check_watching(symbol, tradable, sym_state, closed_bars, last_closed, capital, market, setup_log=None, eia_surprise=None):
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
    eia_surprise is optional and only used by check_watching_commodity()
    for NG=F's news-confirmation gate -- fetched by a separate script
    (eia_check.py) before the scan, same pattern as news_briefing.py.
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
        alert = check_watching_us(symbol, tradable, sym_state, closed_bars, last_closed, capital, market, setup_log)
        # The user's broker can't short US equities -- filter out any
        # short-direction alert regardless of source (Gap and Go, or
        # the Triple MA/Triple Threat fallback via
        # check_secondary_strategies both still fire short signals
        # internally). check_watching_us()'s own dedup state (gap_fired
        # etc.) already updated normally before this runs, so nothing
        # retries every scan trying to re-fire the filtered signal.
        return None if alert and alert.get("direction") == "short" else alert
    if market == "commodity":
        return check_watching_commodity(symbol, tradable, sym_state, closed_bars, last_closed, capital, market, eia_surprise)
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
    if alert is not None:
        r = rsi(closed_bars)
        vwap = day_vwap(closed_bars, last_closed)
        close = last_closed["close"]
        if alert["direction"] == "long" and (r > 60 and close >= vwap):
            alert["trigger_context"] = {**alert.get("trigger_context", {}), "rsi": round(r, 2), "vwap": round(vwap, 4), "gate": "rsi>60 and close>=vwap"}
            return alert
        if alert["direction"] == "short" and (r < 40 and close <= vwap):
            alert["trigger_context"] = {**alert.get("trigger_context", {}), "rsi": round(r, 2), "vwap": round(vwap, 4), "gate": "rsi<40 and close<=vwap"}
            return alert
    return check_secondary_strategies(symbol, tradable, sym_state, closed_bars, last_closed, capital, market)


def check_watching_us(symbol, tradable, sym_state, closed_bars, last_closed, capital, market, setup_log=None):
    """Gap and Go, short-only -- a standalone entry strategy, not a filter
    on check_watching_default() (that base breakout/breakdown/range-
    rejection logic backtested as a net LOSER on US data, PF 0.78, and
    neither India's RSI+VWAP combo nor an approximation of crypto's
    retest/2-bar/ADX combo rescued it when transplanted here -- US
    genuinely needed its own strategy, researched from real US
    day-trading practice rather than reused from another market).

    User's broker can't short US equities -- check_watching()'s
    dispatcher now filters out ANY short-direction alert for market
    "us" (this function's own Gap and Go short, and the Triple MA/
    Triple Threat fallback's short side too), so despite everything
    below, no short signal for US ever actually reaches the user
    anymore. Left running internally rather than ripped out: its
    gap_fired/gap_direction state tracking is unaffected either way,
    and every long-only replacement tried so far (see git history --
    gap_and_go_long, breakout_long isolated/retest-confirmed,
    range_long_rejection isolated, VWAP/RSI mean-reversion both
    directions -- 10 candidates total on real 40-symbol US_UNIVERSE
    60-day 15m data) came back flat or negative (PF 0.53-0.98), so
    there's nothing validated yet to replace it with. Real production
    triple_ma_long's own live track record on US is thin and weak too
    (14.3% win, n=7) -- the honest state of things right now is US has
    no validated long-only edge, watched via the unfiltered fallback
    in the meantime rather than gone completely quiet.

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
        sym_state["gap_pct"] = None
        if prior_bars and today_bars:
            prior_close = prior_bars[-1]["close"]
            today_open = today_bars[0]["open"]
            gap_pct = (today_open - prior_close) / prior_close if prior_close else 0
            sym_state["gap_pct"] = gap_pct
            if gap_pct <= -GAP_THRESHOLD_PCT_US:
                sym_state["gap_direction"] = "short"

    # Every early exit below falls through to Triple MA (see its
    # docstring) as a second, independent strategy -- Gap and Go is
    # deliberately narrow (short-only, gap days only).
    if sym_state.get("gap_direction") != "short" or sym_state.get("gap_fired"):
        return check_secondary_strategies(symbol, tradable, sym_state, closed_bars, last_closed, capital, market)
    if len(today_bars) < 2:
        return check_secondary_strategies(symbol, tradable, sym_state, closed_bars, last_closed, capital, market)  # opening range not established yet

    if setup_log:
        for e in setup_log:
            if e["symbol"] != symbol or e["type"] != "gap_and_go_short":
                continue
            fired_ms = int(datetime.fromisoformat(e["fired_at"]).timestamp() * 1000)
            if us_date(fired_ms) == day:
                sym_state["gap_fired"] = True  # resync the flag since setup_log caught what it missed
                return check_secondary_strategies(symbol, tradable, sym_state, closed_bars, last_closed, capital, market)

    range_high = max(b["high"] for b in today_bars[:2])
    range_low = min(b["low"] for b in today_bars[:2])
    close = last_closed["close"]
    if close >= range_low:
        return check_secondary_strategies(symbol, tradable, sym_state, closed_bars, last_closed, capital, market)

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
    gap_pct = sym_state.get("gap_pct")
    trigger_context = {
        "gap_pct": round(gap_pct * 100, 3) if gap_pct is not None else None,
        "opening_range_high": range_high, "opening_range_low": range_low,
        "volume": vol, "avg_volume": vol_avg,
    }
    return {"text": text, "type": "gap_and_go_short", "direction": "short", "entry": close, "stop": stop, "qty": qty, "target": None, "vol_ratio": vol / vol_avg if vol_avg else 0, "trigger_context": trigger_context}


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
        trigger_context = {
            "range_high": range_high, "volume": vol, "avg_volume": vol_avg,
            "trend_ema": round(trend_ema, 6) if trend_ema else None, "confirmation": "2-bar + retest",
        }
        return {"text": text, "type": "breakout_long", "direction": "long", "entry": close, "stop": stop, "qty": qty, "target": None, "vol_ratio": vol / vol_avg if vol_avg else 0, "trigger_context": trigger_context}

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
        trigger_context = {
            "range_low": range_low, "volume": vol, "avg_volume": vol_avg,
            "trend_ema": round(trend_ema, 6) if trend_ema else None, "confirmation": "2-bar + retest",
        }
        return {"text": text, "type": "breakdown_short", "direction": "short", "entry": close, "stop": stop, "qty": qty, "target": None, "vol_ratio": vol / vol_avg if vol_avg else 0, "trigger_context": trigger_context}

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
            trigger_context = {
                "range_low": range_low, "range_high": range_high, "wick_low": last_closed["low"],
                "adx": round(adx_val, 1) if adx_val is not None else None,
            }
            return {"text": text, "type": "range_long_rejection", "direction": "long", "entry": close, "stop": stop, "qty": qty, "target": range_high, "vol_ratio": vol / vol_avg if vol_avg else 0, "trigger_context": trigger_context}
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
            trigger_context = {
                "range_low": range_low, "range_high": range_high, "wick_high": last_closed["high"],
                "adx": round(adx_val, 1) if adx_val is not None else None,
            }
            return {"text": text, "type": "range_short_rejection", "direction": "short", "entry": close, "stop": stop, "qty": qty, "target": range_low, "vol_ratio": vol / vol_avg if vol_avg else 0, "trigger_context": trigger_context}
        return None

    # DMI+DPO trend setup -- independent of the range-based setups above
    # (fires whether price is inside or outside range_high/range_low),
    # added as a second, separate crypto strategy per explicit request
    # rather than replacing the range/breakout system.
    #
    # Dedup uses its OWN dedicated field (dmi_dpo_regime), not the
    # shared last_alert the other 4 setups use -- confirmed directly via
    # a real 15m production-code backtest (90 days, real Coinbase data,
    # not the daily-bar research backtest) that reusing last_alert was
    # broken: the unrelated "if range_low < close < range_high:
    # last_alert = {}" housekeeping a few lines below fires on nearly
    # every bar where price sits inside the base range, wiping the dedup
    # one bar after it was set and letting this refire every single bar
    # the trend condition held. Fixed by tracking the DMI/DPO regime in
    # its own field, updated every call regardless of whether anything
    # fires, so a fire only happens on an actual long<->short/neutral
    # transition -- not on every bar the condition still holds.
    #
    # Period=50 (not the 14/20 defaults) -- also confirmed via the same
    # real 15m backtest: the daily-bar research version (period 14/20)
    # doesn't transfer to 15m at all (PF ~1.0, pure noise -- a 14-period
    # ADX at 15m only spans 3.5 hours, nowhere near the multi-day trend
    # structure the daily version was actually reading). Swept periods
    # 20-150 against 90 days of real Coinbase 15m data; period=50 (12.5
    # hours) was the best AND most robust: profitable on all 3 symbols
    # individually, and an out-of-sample split (first 60 days vs. held-
    # out last 30) held up rather than degrading -- first-60d PF 1.34,
    # last-30d PF 1.47, win rate 54.5% -> 63.4%. Needs the wider 300-bar
    # crypto fetch (see main()) since period=50 needs 2*50+1=101 bars
    # minimum for dmi() alone. Real, but modest edge -- nowhere near the
    # daily backtest's PF 2.42, and thin enough that real exchange fees
    # could meaningfully eat into it; treat as unproven until it's built
    # its own live track record.
    ADX_MIN_TRENDING = 20
    DMI_DPO_PERIOD = 50
    plus_di, minus_di, adx_trend = dmi(closed_bars, period=DMI_DPO_PERIOD)
    d_po = dpo(closed_bars, period=DMI_DPO_PERIOD)
    current_regime = None
    if adx_trend is not None and d_po is not None and adx_trend > ADX_MIN_TRENDING:
        if plus_di > minus_di and d_po > 0:
            current_regime = "long"
        elif minus_di > plus_di and d_po < 0:
            current_regime = "short"
    prev_regime = sym_state.get("dmi_dpo_regime")
    sym_state["dmi_dpo_regime"] = current_regime
    if current_regime and current_regime != prev_regime:
        if current_regime == "long":
            stop = close - 2 * n
            qty = position_size(capital, close, stop, losses, leverage=leverage, consecutive_wins=wins)
            text = build_alert_text(
                f"{symbol} DMI+DPO TREND (long)\n\n"
                f"BUY\nEntry: {close:,.4g}\nStoploss: {stop:,.4g}\nVolume: ~{qty:.6g} units\n"
                f"Take profit: Keep trailing (no fixed target)\n"
                f"{expected_profit_line(close, stop, qty, currency=currency)}\n\n"
                f"+DI {plus_di:.1f} > -DI {minus_di:.1f}, ADX {adx_trend:.0f} confirms trend, DPO {d_po:,.4g} (recent pullback within the trend).",
                symbol=symbol, price=close,
            )
            trigger_context = {
                "plus_di": round(plus_di, 2), "minus_di": round(minus_di, 2),
                "adx": round(adx_trend, 2), "dpo": round(d_po, 6), "period": DMI_DPO_PERIOD,
            }
            return {"text": text, "type": "dmi_dpo_long", "direction": "long", "entry": close, "stop": stop, "qty": qty, "target": None, "vol_ratio": vol / vol_avg if vol_avg else 0, "trigger_context": trigger_context}
        else:
            stop = close + 2 * n
            qty = position_size(capital, close, stop, losses, leverage=leverage, consecutive_wins=wins)
            text = build_alert_text(
                f"{symbol} DMI+DPO TREND (short)\n\n"
                f"SELL\nEntry: {close:,.4g}\nStoploss: {stop:,.4g}\nVolume: ~{qty:.6g} units\n"
                f"Take profit: Keep trailing (no fixed target)\n"
                f"{expected_profit_line(close, stop, qty, currency=currency)}\n\n"
                f"-DI {minus_di:.1f} > +DI {plus_di:.1f}, ADX {adx_trend:.0f} confirms trend, DPO {d_po:,.4g} (recent bounce within the trend).",
                symbol=symbol, price=close,
            )
            trigger_context = {
                "plus_di": round(plus_di, 2), "minus_di": round(minus_di, 2),
                "adx": round(adx_trend, 2), "dpo": round(d_po, 6), "period": DMI_DPO_PERIOD,
            }
            return {"text": text, "type": "dmi_dpo_short", "direction": "short", "entry": close, "stop": stop, "qty": qty, "target": None, "vol_ratio": vol / vol_avg if vol_avg else 0, "trigger_context": trigger_context}

    triple_ma_alert = check_secondary_strategies(symbol, tradable, sym_state, closed_bars, last_closed, capital, market)
    if triple_ma_alert:
        return triple_ma_alert

    if range_low < close < range_high:
        sym_state["last_alert"] = {}
    recent_high = max(b["high"] for b in closed_bars[-10:])
    recent_low = min(b["low"] for b in closed_bars[-10:])
    if recent_high > range_high:
        sym_state["range_high"] = recent_high
    if recent_low < range_low:
        sym_state["range_low"] = recent_low
    return None


def check_watching_commodity(symbol, tradable, sym_state, closed_bars, last_closed, capital, market, eia_surprise=None):
    """Gold and natural gas only (see COMMODITY_WATCHLIST) -- a
    monthly-hold SEASONALITY setup, not a 15m technical condition like
    every other setup in this file. From the full commodity strategy
    review: generic trend-following (Triple MA/Threat) failed on all 4
    commodities tested; a real, out-of-sample-validated edge only
    showed up for calendar-month seasonality on gold and natural gas
    specifically (silver and crude oil seasonality did NOT hold up and
    are deliberately excluded). Real 2011-2026 daily backtest, strong/
    weak months derived from the first half of years, tested clean on
    the held-out second half:
      - GC=F: +47.5% compounded, 58.7% win rate (14 years, split 2019)
      - NG=F: +128.7% compounded, 60.9% win rate, alone -- BUT requiring
        EIA storage-surprise confirmation (see eia_check.py) narrowed
        it to 13 of 46 trades at a much higher 76.9% win rate. That's
        the validated recipe for NG=F specifically -- not seasonality
        alone -- so the EIA gate below is REQUIRED (fails closed if the
        data's missing/stale), not an optional bonus filter.
    A COT-positioning filter was also tested and made gold WORSE and
    was a wash for natural gas -- deliberately not included here.

    Only fires once per calendar month (own dedicated dedup field,
    stored as a "YYYY-MM" string -- a tuple would silently break after
    round-tripping through state.json's JSON, which turns tuples into
    lists that no longer equality-match on the next scan). Stop is 2x
    the symbol's real historical MONTHLY return std dev (GC=F 4.77%,
    NG=F 14.81%), not the usual atr(closed_bars) on 15m bars every
    other setup uses -- a month-long hold needs a stop sized to monthly
    moves, not 15-minute noise."""
    now = datetime.fromtimestamp(last_closed["close_time"] / 1000, tz=timezone.utc)
    period = f"{now.year}-{now.month:02d}"
    if sym_state.get("seasonal_fired_period") == period:
        return None

    strong = SEASONAL_STRONG_MONTHS.get(symbol, set())
    weak = SEASONAL_WEAK_MONTHS.get(symbol, set())
    direction = "long" if now.month in strong else ("short" if now.month in weak else None)
    if direction is None:
        return None

    news_note = ""
    if symbol == "NG=F":
        if not eia_surprise or eia_surprise.get("surprise_bcf") is None:
            return None  # required confirmation missing -- fails closed, not open
        fetched_at = eia_surprise.get("fetched_at")
        if not fetched_at or (now - datetime.fromisoformat(fetched_at)).days > EIA_STALE_DAYS:
            return None  # eia_check.py hasn't run recently -- treat stale data as missing, not trustworthy
        surprise = eia_surprise["surprise_bcf"]
        if direction == "long" and surprise >= 0:
            return None  # need a bigger draw / smaller build than seasonal norm
        if direction == "short" and surprise <= 0:
            return None  # need a bigger build / smaller draw than seasonal norm
        news_note = f" EIA storage {surprise:+.0f} Bcf vs. seasonal norm confirms."

    close = last_closed["close"]
    stop_pct = SEASONAL_STOP_PCT.get(symbol, 0.10)
    stop = close * (1 - stop_pct) if direction == "long" else close * (1 + stop_pct)
    losses = sym_state.get("consecutive_losses", 0)
    wins = sym_state.get("consecutive_wins", 0)
    leverage = LEVERAGE_BY_MARKET.get(market, 1)
    qty = position_size(capital, close, stop, losses, leverage=leverage, consecutive_wins=wins)
    if qty <= 0:
        return None
    tag = "" if tradable else " (analysis only -- not paper-tradable, use your own broker if acting on this)"

    sym_state["seasonal_fired_period"] = period
    action = "BUY" if direction == "long" else "SELL"
    text = build_alert_text(
        f"{symbol} SEASONAL ({direction}){tag}\n\n"
        f"{action}\nEntry: {close:,.4g}\nStoploss: {stop:,.4g}\nVolume: ~{qty:.6g} units\n"
        f"Take profit: Keep trailing (no fixed target -- roughly a 1-month hold)\n"
        f"{expected_profit_line(close, stop, qty, currency='$')}\n\n"
        f"Month {now.month} is a historically {'strong' if direction=='long' else 'weak'} month for {symbol} "
        f"(validated out-of-sample on 14 years of real data).{news_note}",
        symbol=symbol, price=close,
    )
    trigger_context = {
        "month": now.month,
        "eia_surprise_bcf": eia_surprise.get("surprise_bcf") if symbol == "NG=F" and eia_surprise else None,
    }
    return {"text": text, "type": f"seasonal_{direction}", "direction": direction, "entry": close, "stop": stop, "qty": qty, "target": None, "vol_ratio": 1.0, "trigger_context": trigger_context}


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
        trigger_context = {
            "range_high": range_high, "volume": vol, "avg_volume": vol_avg,
            "trend_ema": round(trend_ema, 6) if trend_ema else None,
        }
        return {"text": text, "type": "breakout_long", "direction": "long", "entry": close, "stop": stop, "qty": qty, "target": None, "vol_ratio": vol / vol_avg if vol_avg else 0, "trigger_context": trigger_context}

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
        trigger_context = {
            "range_low": range_low, "volume": vol, "avg_volume": vol_avg,
            "trend_ema": round(trend_ema, 6) if trend_ema else None,
        }
        return {"text": text, "type": "breakdown_short", "direction": "short", "entry": close, "stop": stop, "qty": qty, "target": None, "vol_ratio": vol / vol_avg if vol_avg else 0, "trigger_context": trigger_context}

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
            trigger_context = {"range_low": range_low, "range_high": range_high, "wick_low": last_closed["low"]}
            return {"text": text, "type": "range_long_rejection", "direction": "long", "entry": close, "stop": stop, "qty": qty, "target": range_high, "vol_ratio": vol / vol_avg if vol_avg else 0, "trigger_context": trigger_context}
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
            trigger_context = {"range_low": range_low, "range_high": range_high, "wick_high": last_closed["high"]}
            return {"text": text, "type": "range_short_rejection", "direction": "short", "entry": close, "stop": stop, "qty": qty, "target": range_low, "vol_ratio": vol / vol_avg if vol_avg else 0, "trigger_context": trigger_context}
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
        # "stale_shadow_state" entries are administrative cleanup for
        # broken shadow dicts, not real trade outcomes -- they carry
        # pnl_per_unit=None, which crashes the `> 0` comparison below.
        and e["outcome"].get("exit_reason") != "stale_shadow_state"
    ]
    total = len(matches)
    wins = sum(1 for e in matches if e["outcome"]["pnl_per_unit"] > 0)
    confidence = (wins + 1) / (total + 2)
    return {"wins": wins, "total": total, "confidence": round(confidence, 4)}


def estimate_india_intraday_charges(direction, entry, exit_price, qty):
    """Real NSE intraday equity charges (brokerage + STT + exchange
    transaction charge + stamp duty + SEBI fee + GST) -- reverse-engineered
    from a real trade confirmation and verified to match every line item
    exactly: PFC.NS short, entry 351.60, exit 351.00, qty 1421 -> brokerage
    40.00, SEBI fee 1.00, exchange txn 29.65, stamp duty 14.96, STT 124.91,
    GST 12.72, total 223.24 (all six matched to the rupee).

    On a small intraday move these charges can be the difference between
    a real profit and a real loss (confirmed directly: a trade the bot's
    gross math showed as +0.50 was actually a real -46.82 loss once
    charges applied) -- India-specific; crypto/US don't have this problem
    at anywhere near this magnitude on this bot's position sizes."""
    buy_turnover = (exit_price if direction == "short" else entry) * qty
    sell_turnover = (entry if direction == "short" else exit_price) * qty
    total_turnover = buy_turnover + sell_turnover

    brokerage = 40.0  # Rs 20 flat per executed order x 2 legs
    sebi_fee = total_turnover * 0.0000010  # Rs 10 per crore
    exchange_txn = total_turnover * 0.0000297  # NSE intraday equity rate
    stamp_duty = buy_turnover * 0.00003  # 0.003%, buy side only
    stt = sell_turnover * 0.00025  # 0.025%, sell side only
    gst = 0.18 * (brokerage + sebi_fee + exchange_txn)
    return round(brokerage + sebi_fee + exchange_txn + stamp_duty + stt + gst, 2)


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
    took it, without generating a single extra Telegram message.

    notify=True (a real, taken position) is asymmetric with notify=False
    on stop/target hits specifically: it sends the STOP HIT / TAKE PROFIT
    HIT alert (once, not every scan -- see exit_alert_sent) but does NOT
    call log_trade() or rearm_to_watching() -- the position stays
    unresolved in setup_log until the user explicitly closes it via the
    dashboard's Closed button (apply_close_trade.py). Reported directly:
    the bot's own simulated exit (price/time it thinks the stop/target
    was hit) doesn't always match what the user's real broker actually
    filled at, so auto-resolving a taken position from the simulation
    alone was recording the wrong outcome. Trailing-stop suggestions and
    the giveback heads-up below are unaffected either way -- still fire
    normally for a taken position, only the terminal stop/target-hit
    branches changed."""
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
                # Real, taken position -- alert only, never auto-resolve.
                # The bot's own simulated exit can diverge from the
                # user's real fill (confirmed directly: a taken position
                # auto-resolved at a simulated price/time that didn't
                # match what the user actually got from their broker).
                # Only the dashboard's Closed button (apply_close_trade.py)
                # marks a taken position resolved now. Alerts once per
                # exit signal, not every scan, via exit_alert_sent.
                if not sym_state.get("exit_alert_sent"):
                    send_telegram(f"{symbol} TAKE PROFIT HIT -- long{tag}\n\nClose {close:,.4g} reached target {tp:,.4g}. Close now if you haven't already.", symbol=symbol, price=close)
                    sym_state["exit_alert_sent"] = True
                return
            pnl = close - entry
            log_trade(sym_state, "long", entry, close, pnl, "take_profit")
            sym_state["consecutive_losses"] = 0
            sym_state["consecutive_wins"] = sym_state.get("consecutive_wins", 0) + 1
            rearm_to_watching(sym_state, closed_bars)
            return

        if close < stop:
            if notify:
                if not sym_state.get("exit_alert_sent"):
                    send_telegram(f"{symbol} STOP HIT -- long{tag}\n\nClose {close:,.4g} broke below stop {stop:,.4g}. Sell now if you haven't already.", symbol=symbol, price=close)
                    sym_state["exit_alert_sent"] = True
                return
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
        # candidate_stop must stay BELOW the current close for a long --
        # the profit-lock floor is anchored to the peak (the best price
        # since entry), which can sit well above where price has since
        # retraced to within the same bar. If price pulled back enough,
        # "lock 70% of peak gain" can compute a candidate ABOVE the
        # current close -- a stop already on the wrong side of price,
        # which would fire a false STOP HIT on the very next check even
        # though nothing has moved against the position since. Reported
        # directly against the mirrored short case (HINDCOPPER.NS: a
        # trail suggested moving stop to 537.9 while price was at 538.9
        # -- already broken the moment it was suggested).
        if candidate_stop > stop * 1.001 and candidate_stop < close:
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
                if not sym_state.get("exit_alert_sent"):
                    send_telegram(f"{symbol} TAKE PROFIT HIT -- short{tag}\n\nClose {close:,.4g} reached target {tp:,.4g}. Close now if you haven't already.", symbol=symbol, price=close)
                    sym_state["exit_alert_sent"] = True
                return
            pnl = entry - close
            log_trade(sym_state, "short", entry, close, pnl, "take_profit")
            sym_state["consecutive_losses"] = 0
            rearm_to_watching(sym_state, closed_bars)
            return

        if close > stop:
            if notify:
                if not sym_state.get("exit_alert_sent"):
                    send_telegram(f"{symbol} STOP HIT -- short{tag}\n\nClose {close:,.4g} broke above stop {stop:,.4g}. Buy back / close now if you haven't already.", symbol=symbol, price=close)
                    sym_state["exit_alert_sent"] = True
                return
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
        # candidate_stop must stay ABOVE the current close for a short --
        # confirmed real bug: the profit-lock floor is anchored to the
        # peak (deepest low since entry), which can sit well below where
        # price has since retraced to within the same bar. HINDCOPPER.NS
        # hit a low of 537.5 but closed the bar at 538.9; "lock 70% of
        # peak gain" from that 537.5 extreme computed a candidate stop of
        # 537.9 -- already BELOW the 538.9 current price the moment it
        # was suggested, which would fire a false STOP HIT on the very
        # next check even though nothing had moved against the position.
        if candidate_stop < stop * 0.999 and candidate_stop > close:
            sym_state["stop_loss"] = candidate_stop
            locked_pct = (entry - candidate_stop) / peak_profit * 100 if peak_profit > 0 else 0
            if notify:
                send_telegram(f"{symbol} short -- trail your stop{tag}\n\nNew low {extreme:,.4g}. Move stop from {stop:,.4g} to {candidate_stop:,.4g} (locks ~{locked_pct:.0f}% of peak gain).", symbol=symbol, price=close)
            return

        giveback_pct = (peak_profit - current_profit) / peak_profit if peak_profit > 0 else 0
        if peak_profit > 0.5 * n and giveback_pct > 0.25:
            if notify:
                send_telegram(f"{symbol} short -- consider taking profit{tag}\n\nPeak gain was {peak_profit:,.4g}/unit, now {current_profit:,.4g}/unit -- given back {giveback_pct*100:.0f}%. Still in profit; your call.", symbol=symbol, price=close)


def trend_reversed(setup_type, direction, closed_bars, market=None, trigger_context=None):
    """Explicitly requested: check_open()'s trailing stop only reacts
    to PRICE -- if a position's own underlying signal has already
    flipped against it, the bot still just waits for price to
    eventually wander down to the trailing stop, giving back far more
    than necessary and sometimes turning a real winner into a loser.
    This recomputes each strategy's own directional bias/entry
    condition FRESH from the current bars/context (not a possibly-
    stale sym_state field) and flags a reversal the moment it would no
    longer hold -- including fading to neutral, not just a hard flip
    to the opposite side, since a strategy's own conviction
    evaporating is itself grounds to exit.

    Two real, backtest-validated pieces:
      - Triple MA / Triple Threat / DMI+DPO: their own regime
        definition, recomputed fresh. Applies identically across all
        3 markets these run in.
      - India-only breakout_long/breakdown_short: price closing back
        on the wrong side of the actual range level the setup broke
        out/down through (from trigger_context), not price vs an EMA.

    Explicitly tried extending this further -- first with the same
    10-EMA (EMA_PERIOD) that gates breakout/breakdown/range-rejection
    entry as the reversal signal, then with the range-level version
    above applied to EVERY market instead of just India -- and
    backtested both against 5,189 real trades on real historical data
    (7 crypto symbols ~1yr 15m, 26 India + 13 US symbols 60d 15m):
      - EMA version: net negative everywhere (overall avg R -0.0119 ->
        -0.0146, win rate 49.9% -> 39.1%). It fired on 57% of all
        trades, didn't catch losers any earlier than just letting them
        ride to the stop (avg R ~-0.63 either way on that subset), and
        cut short 207 real winners that would have hit target.
      - Range-level version, all markets: crypto was a wash both
        out-of-sample halves (-0.008/+0.007 delta -- the level sits so
        close to the stop it barely fires before the stop would have
        anyway), US gap_and_go stayed net negative on a thin 65-trade
        sample, India's range-rejection types had too few trades/half
        (11-13) to mean anything. Only India breakout_long/
        breakdown_short held up: consistently positive on BOTH
        out-of-sample halves (+0.031/+0.028 and +0.048/+0.083 delta
        avg R respectively), majority-positive per-symbol (17-better/
        9-worse across 26 symbols) -- a real, narrow edge, scoped here
        exactly that narrowly rather than shipped broad on the
        strength of a mixed/negative result elsewhere. Seasonal
        wasn't testable at all (2 symbols, a couple fires/year --
        nowhere near enough sample) -- left uncovered.

    Not defined for anything else (manually-logged entries like
    "community_idea" or hand-tracked India futures) -- no strategy
    logic exists to recompute for those, so they fall through to
    check_open()'s normal stop/target handling untouched."""
    closes = [b["close"] for b in closed_bars]

    if setup_type in ("triple_ma_long", "triple_ma_short"):
        if len(closes) < TRIPLE_MA_SLOW:
            return False
        fast = ema(closes[-(TRIPLE_MA_FAST * 3):], TRIPLE_MA_FAST)
        med = ema(closes[-(TRIPLE_MA_MED * 3):], TRIPLE_MA_MED)
        slow = ema(closes[-(TRIPLE_MA_SLOW * 3):], TRIPLE_MA_SLOW)
        current_regime = "long" if fast > med > slow else ("short" if fast < med < slow else None)
        return current_regime != direction

    if setup_type in ("dmi_dpo_long", "dmi_dpo_short"):
        # Same regime definition as check_watching_crypto()'s DMI+DPO
        # block -- ADX_MIN_TRENDING/DMI_DPO_PERIOD kept in sync with
        # that function by hand (both small, stable constants).
        adx_min_trending, dmi_dpo_period = 20, 50
        plus_di, minus_di, adx_trend = dmi(closed_bars, period=dmi_dpo_period)
        d_po = dpo(closed_bars, period=dmi_dpo_period)
        current_regime = None
        if adx_trend is not None and d_po is not None and adx_trend > adx_min_trending:
            if plus_di > minus_di and d_po > 0:
                current_regime = "long"
            elif minus_di > plus_di and d_po < 0:
                current_regime = "short"
        return current_regime != direction

    if setup_type in ("triple_threat_long", "triple_threat_short"):
        if len(closes) < TRIPLE_THREAT_TREND_PERIOD:
            return False
        trend = ema(closes[-(TRIPLE_THREAT_TREND_PERIOD * 3):], TRIPLE_THREAT_TREND_PERIOD)
        close = closed_bars[-1]["close"]
        return close < trend if direction == "long" else close > trend

    if market == "india" and setup_type in ("breakout_long", "breakdown_short"):
        tc = trigger_context or {}
        close = closed_bars[-1]["close"]
        if setup_type == "breakout_long":
            level = tc.get("range_high")
            return level is not None and close < level
        level = tc.get("range_low")
        return level is not None and close > level

    return False


def settle_end_of_day(symbol, setup_log, last_closed, sym_state):
    """Explicitly requested: US/India markets close for the day (no
    new bars until the next session), so an unresolved position just
    sat exactly as it was at the close -- for hours, overnight, or over
    a weekend -- showing "unresolved" when the trading day for that
    symbol has genuinely ended. Settles every still-open setup_log
    entry for this symbol at the market's actual last close price
    (mirrors how real intraday/MIS positions are auto-squared-off at
    end of day, not carried over) instead of leaving it in limbo until
    fresh bars eventually arrive next session.

    Called once per scan for a symbol whose latest bar is_stale() --
    idempotent: a shadow-only entry resolves once and is skipped on
    every subsequent stale scan (log_entry["resolved"]); a taken entry
    gets one settlement alert per stale period (exit_alert_sent), not
    one every 15 minutes overnight. US/India only -- crypto trades
    24/7 (never legitimately "stale" outside a real outage) and
    commodities aren't in scope of this request."""
    close = last_closed["close"]
    for log_entry in setup_log:
        if log_entry["resolved"] or log_entry["symbol"] != symbol:
            continue
        shadow = log_entry["shadow"]
        entry_price = shadow.get("entry_price")
        direction = shadow.get("direction")
        if entry_price is None or direction is None:
            # A shadow already rearm_to_watching()'d (direction/
            # entry_price reset to None) but whose outer log_entry
            # was never marked resolved -- a real, separate data
            # inconsistency from some earlier resolution path, not
            # something to settle again. Close it out here rather
            # than crash or leave it stuck "unresolved" forever
            # (exactly the symptom this function exists to fix).
            log_entry["resolved"] = True
            log_entry["outcome"] = {"exit_reason": "stale_shadow_state", "pnl_per_unit": None, "pnl_total": None}
            continue
        pnl = (close - entry_price) if direction == "long" else (entry_price - close)
        if log_entry.get("taken"):
            if not shadow.get("exit_alert_sent"):
                send_telegram(
                    f"{symbol} MARKET CLOSED -- settling {shadow['direction']} at today's close\n\n"
                    f"Close {close:,.4g}. The session ended before this hit stop/target -- "
                    f"close now if you haven't already.",
                    symbol=symbol, price=close,
                )
                shadow["exit_alert_sent"] = True
        else:
            log_trade(shadow, shadow["direction"], entry_price, close, pnl, "eod_settlement")
            log_entry["resolved"] = True
            log_entry["outcome"] = shadow["trade_journal"][-1]
            rearm_to_watching(shadow, None)
            if pnl >= 0:
                sym_state["consecutive_losses"] = 0
                sym_state["consecutive_wins"] = sym_state.get("consecutive_wins", 0) + 1
            else:
                sym_state["consecutive_losses"] = sym_state.get("consecutive_losses", 0) + 1
                sym_state["consecutive_wins"] = 0


def sync_broker_entry(symbol, market, log_entry, shadow, sym_state):
    """For a setup_log entry that was auto-executed on a real broker
    (see the broker_order block in main()'s fire loop -- see BROKERS,
    currently empty, both crypto/Bybit and india/Dhan paused):
    resolves it against the broker's REAL fill data the instant either
    the stop or take-profit fills (ground truth, not the bot's own
    bar-close simulation check_open() runs for every other entry), and
    mirrors the shadow's own trailing-stop math -- check_open() already
    ran on `shadow` this same scan and may have moved
    shadow['stop_loss'] -- onto the real resting stop.

    Polls broker_stop_order_id/broker_take_profit_order_id directly --
    for Dhan these are real order ids; for Bybit, stop_order_id is
    really just the symbol (Bybit's stop-loss is a position attribute,
    not a separate order -- see broker_bybit.py's module docstring).
    Each broker's order_fill_status() accepts whichever shape it
    returned from place_bracket_order(), so this code doesn't need to
    know which broker it's talking to.

    No-ops entirely if the market has no broker wired, that broker is
    disabled, this entry was never broker-executed, or it's already
    resolved."""
    broker = BROKERS.get(market)
    if log_entry.get("resolved") or not log_entry.get("broker_order_id") or not broker or not broker.enabled():
        return

    outcome = None
    for order_id, kind in ((log_entry.get("broker_take_profit_order_id"), "target"),
                            (log_entry.get("broker_stop_order_id"), "stop")):
        fill_price = broker.order_fill_status(order_id)
        if fill_price is not None:
            outcome = (kind, fill_price)
            break

    if outcome:
        kind, fill_price = outcome
        direction, entry_price, qty = log_entry["direction"], log_entry["entry"], log_entry["qty"]
        pnl = (fill_price - entry_price) if direction == "long" else (entry_price - fill_price)
        log_entry["resolved"] = True
        log_entry["outcome"] = {
            "direction": direction, "entry": entry_price, "exit": fill_price, "qty": qty,
            "pnl_per_unit": pnl, "pnl_total": pnl * qty if qty else None,
            "exit_reason": f"broker_{kind}_fill",
            "closed_at": datetime.now(timezone.utc).isoformat(),
        }
        if pnl >= 0:
            sym_state["consecutive_losses"] = 0
            sym_state["consecutive_wins"] = sym_state.get("consecutive_wins", 0) + 1
        else:
            sym_state["consecutive_losses"] = sym_state.get("consecutive_losses", 0) + 1
            sym_state["consecutive_wins"] = 0
        total_txt = f", {pnl * qty:,.4g} total" if qty else ""
        broker_name = BROKER_NAMES.get(market, market)
        send_telegram(
            f"{symbol} PAPER TRADE CLOSED ({broker_name}) -- {'WIN' if pnl >= 0 else 'LOSS'}\n\n"
            f"{direction} {entry_price:,.4g} -> {fill_price:,.4g} ({kind} fill)\n"
            f"P&L: {pnl:,.4g}/unit{total_txt}",
            symbol=symbol, price=fill_price,
        )
        return

    new_stop = shadow.get("stop_loss")
    if (new_stop and log_entry.get("broker_stop_order_id")
            and new_stop != log_entry.get("_last_pushed_stop")):
        result = broker.replace_stop_price(log_entry["broker_stop_order_id"], new_stop)
        if result is not None:
            log_entry["_last_pushed_stop"] = new_stop
            # Dhan's PUT modifies in place (same order id back); Bybit
            # just echoes the same symbol -- track whatever comes back
            # either way, in case that ever changes.
            new_id = result.get("id")
            if new_id:
                log_entry["broker_stop_order_id"] = new_id


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
    # crypto and US are separate pools now, not one shared capital_usd
    # pot -- crypto capital is real cash backing 10x leverage (matches
    # LEVERAGE_BY_MARKET and how these strategies were originally
    # validated), US is unleveraged cash. Confirmed directly against a
    # real paper broker account (since removed, see BROKERS above):
    # sizing crypto off the full $100k pot at 10x produced order
    # notionals a real spot/cash account couldn't actually hold
    # (insufficient balance, and a real per-order notional cap) --
    # $10k crypto capital keeps intended notional (10x = $100k) within
    # what a real account can realistically support.
    capital_usd_crypto = state.get("capital_usd_crypto", 100)
    capital_usd_us = state.get("capital_usd_us", 100)
    capital_inr = state.get("capital_inr", 100)
    capital_commodity = state.get("capital_usd_commodity", 100)
    # eia_check.py (run as its own step, same pattern as news_briefing.py)
    # fetches this before the scan and saves it into state.json --
    # required for NG=F's seasonal setup to fire at all, see
    # check_watching_commodity()'s docstring.
    eia_surprise = state.get("eia_ng_surprise")
    watchlist = build_watchlist(state)

    setup_log = state.setdefault("setup_log", [])
    fired_this_scan = []  # (market, alert dict) -- ranked and trimmed after the full watchlist loop
    for entry in watchlist:
        symbol, market, tradable = entry["symbol"], entry["market"], entry["tradable"]
        try:
            # Crypto fetches more history (300 vs 60) so the DMI+DPO
            # trend setup has enough bars for a period=50 lookback (12.5
            # hours) -- confirmed via a real 15m backtest that period=20
            # over a 60-bar/15hr window was pure noise (PF ~1.0), while
            # period=50 over 300 bars held up both per-symbol and on an
            # out-of-sample split. The other 4 crypto setups are
            # unaffected: they only ever look at bounded tail slices
            # (last 2/10/30 bars) regardless of how much history
            # precedes them, so the extra bars are free for them.
            fetch_limit = 300 if market == "crypto" else 60
            bars = fetch_klines(symbol, market, limit=fetch_limit)
        except Exception as e:
            print(f"{symbol}: fetch failed ({e}), skipping")
            continue
        if len(bars) < 15:
            print(f"{symbol}: not enough bars, skipping")
            continue
        closed_bars = bars[:-1]
        last_closed = closed_bars[-1]
        if is_stale(last_closed):
            if market in ("us", "india"):
                if symbol not in symbols_state:
                    symbols_state[symbol] = default_symbol_state(closed_bars)
                settle_end_of_day(symbol, setup_log, last_closed, symbols_state[symbol])
            print(f"{symbol}: stale (market likely closed), skipping")
            continue

        if symbol not in symbols_state:
            symbols_state[symbol] = default_symbol_state(closed_bars)
        sym_state = symbols_state[symbol]
        if market == "india":
            capital, pool_markets = capital_inr, ("india",)
        elif market == "commodity":
            capital, pool_markets = capital_commodity, ("commodity",)
        elif market == "crypto":
            capital, pool_markets = capital_usd_crypto, ("crypto",)
        else:
            capital, pool_markets = capital_usd_us, ("us",)
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

            # Proactive trend-reversal exit -- checked BEFORE
            # check_open()'s trailing-stop wait, explicitly requested:
            # waiting for price to reach the trailing stop after the
            # underlying signal had already flipped was giving back
            # far more than necessary, sometimes turning a real winner
            # into a loser. See trend_reversed()'s docstring.
            #
            # Guard against a shadow already rearm_to_watching()'d
            # (direction/entry_price reset to None) whose outer
            # log_entry was never marked resolved -- a real, separate
            # data inconsistency from some earlier resolution path
            # (confirmed directly: 8 old India/US entries had this).
            # Close it out here rather than crash or leave it stuck.
            if shadow.get("direction") is None or shadow.get("entry_price") is None:
                log_entry["resolved"] = True
                log_entry["outcome"] = {"exit_reason": "stale_shadow_state", "pnl_per_unit": None, "pnl_total": None}
                continue

            if trend_reversed(log_entry["type"], shadow["direction"], closed_bars, market=market, trigger_context=log_entry.get("trigger_context")):
                close = last_closed["close"]
                entry_price = shadow["entry_price"]
                pnl = (close - entry_price) if shadow["direction"] == "long" else (entry_price - close)
                if log_entry.get("taken"):
                    if not shadow.get("exit_alert_sent"):
                        send_telegram(
                            f"{symbol} TREND REVERSED -- {shadow['direction']}\n\n"
                            f"Close {close:,.4g}. The strategy that fired this trade no longer "
                            f"sees this trend -- close now if you haven't already.",
                            symbol=symbol, price=close,
                        )
                        shadow["exit_alert_sent"] = True
                else:
                    log_trade(shadow, shadow["direction"], entry_price, close, pnl, "trend_reversed")
                    log_entry["resolved"] = True
                    log_entry["outcome"] = shadow["trade_journal"][-1]
                    rearm_to_watching(shadow, closed_bars)
                    if pnl >= 0:
                        sym_state["consecutive_losses"] = 0
                        sym_state["consecutive_wins"] = sym_state.get("consecutive_wins", 0) + 1
                    else:
                        sym_state["consecutive_losses"] = sym_state.get("consecutive_losses", 0) + 1
                        sym_state["consecutive_wins"] = 0
                continue

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

            # Broker-tracked entries (see broker_order in the fire loop
            # below) never resolve via the shadow block above -- notify=
            # True there means check_open() only ever alerts, never
            # calls log_trade() (see its docstring). Real resolution and
            # stop-trailing enforcement for those live here instead,
            # against the real broker's actual fill data. No-ops for
            # every entry that was never broker-executed.
            sync_broker_entry(symbol, market, log_entry, shadow, sym_state)

        alert = check_watching(symbol, tradable, sym_state, closed_bars, last_closed, capital, market, setup_log, eia_surprise)
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

        # Real (paper) auto-execution -- crypto + US only, and only for
        # setups that actually get surfaced (best-of-N filtering above
        # already decides what's worth acting on; a non-surfaced setup
        # shouldn't get real capital either). alert["target"] is None
        # for most of this bot's setups (Triple MA, Triple Threat,
        # DMI+DPO -- deliberately trailing-stop-only, see check_open()'s
        # docstring) -- place_bracket_order() itself branches on this
        # (order_class="oto", stop leg only, vs "bracket" with both
        # legs), so target being None must NOT gate execution here.
        # Confirmed directly: an earlier version of this guard required
        # a real target, which meant broker execution silently never
        # fired for any of the 3 setups actually surfaced in real
        # testing -- only the alert went out, no automation. BROKERS is
        # currently empty (US auto-execution removed outright, crypto/
        # india paused -- see BROKERS' definition above) -- every
        # market looks up to None and stays alert-only. Each broker's
        # enabled() is False (pure no-op) until its own API key secrets
        # are set, same fail-open behavior either way.
        broker_order = None
        broker_mod = BROKERS.get(market)
        if surfaced and broker_mod and broker_mod.enabled():
            broker_order = broker_mod.place_bracket_order(
                symbol, market, alert["direction"], alert["entry"], alert["stop"], alert["target"], alert["qty"],
            )

        if surfaced:
            text = alert["text"]
            if broker_order is not None:
                broker_name = BROKER_NAMES.get(market, market)
                text += f"\n\n[Auto-executed: real {broker_name} paper order placed]"
            fired_setups.append(text)
        fired_at_dt = datetime.now(timezone.utc)
        setup_log.append({
            "symbol": symbol, "type": alert["type"], "direction": alert["direction"],
            "entry": alert["entry"], "stop": alert["stop"], "target": alert["target"],
            "qty": alert["qty"], "fired_at": fired_at_dt.isoformat(),
            "resolved": False, "outcome": None, "surfaced": surfaced,
            "taken": broker_order is not None,
            "broker_order_id": broker_order["id"] if broker_order else None,
            "broker_stop_order_id": broker_order["stop_order_id"] if broker_order else None,
            "broker_take_profit_order_id": broker_order["take_profit_order_id"] if broker_order else None,
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
            # Self-learning groundwork, step 2: the specific indicator
            # values that caused THIS fire (see each check_*() function's
            # own trigger_context construction, right where it already
            # computes them for the alert text) -- so a later review of
            # why a setup won or lost can look at the actual conditions
            # at entry, not just infer from the exit mechanics. Purely
            # observational like confidence_at_fire above; alert.get()
            # since setup types not yet updated to attach one (manual/
            # community_idea entries, which have no algorithmic trigger)
            # simply log None.
            "trigger_context": alert.get("trigger_context"),
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
