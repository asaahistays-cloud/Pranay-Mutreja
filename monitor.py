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
from datetime import datetime, timezone

STATE_FILE = os.path.join(os.path.dirname(__file__), "state.json")
BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID")

ATR_PERIOD = 14
EMA_PERIOD = 10
REJECTION_BUFFER_PCT = 0.0015
RISK_PCT_PER_TRADE = 0.01
LOSS_THROTTLE_AFTER = 2
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
CRYPTO_WATCHLIST = [{"symbol": s, "market": "crypto", "tradable": True} for s in [
    "BTC-USD", "ETH-USD", "SOL-USD", "XRP-USD", "ADA-USD", "DOGE-USD",
    "AVAX-USD", "LINK-USD", "DOT-USD", "LTC-USD", "NEAR-USD", "SUI-USD",
]]


def build_watchlist(state):
    watchlist = list(CRYPTO_WATCHLIST)
    for symbol in state.get("active_us_symbols", []):
        watchlist.append({"symbol": symbol, "market": "us", "tradable": True})
    for symbol in state.get("active_india_symbols", []):
        watchlist.append({"symbol": symbol, "market": "india", "tradable": False})
    return watchlist


# ---------------------------------------------------------------- data ----

def fetch_coinbase(symbol, limit=60):
    url = f"https://api.exchange.coinbase.com/products/{symbol}/candles?granularity=900"
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


def fetch_yahoo(symbol, limit=60):
    url = f"https://query1.finance.yahoo.com/v8/finance/chart/{symbol}?interval=15m&range=5d"
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


def fetch_news(symbol, limit=2):
    """Recent headlines for the symbol, via Yahoo's free search endpoint
    (same data source already used for equity prices -- no new API/key
    needed) -- but ONLY headlines Yahoo itself tags as related to this
    exact ticker (via the response's relatedTickers field), not just
    whatever comes back from the query. Yahoo's news search is generic
    and often returns unrelated global finance news for a plain query;
    the relatedTickers check is what actually filters for relevance.
    In practice this means real matches for most US tickers, and
    honestly nothing for most Indian ones (Yahoo doesn't have matched
    coverage for NSE symbols) -- silence is the correct, honest result
    there rather than showing a wrong headline.
    Best-effort: returns [] on any failure or when nothing genuinely
    matches, rather than forcing an irrelevant headline into an alert."""
    query = symbol.replace("-USD", "").replace(".NS", "")
    url = f"https://query1.finance.yahoo.com/v1/finance/search?q={query}&newsCount=8&quotesCount=0"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read())
        matched = []
        for item in data.get("news", []):
            related = item.get("relatedTickers") or []
            if (symbol in related or query in related) and item.get("title"):
                matched.append(item["title"])
        return matched[:limit]
    except Exception as e:
        print(f"{symbol}: news fetch failed ({e})")
        return []


def build_alert_text(text, symbol=None, price=None):
    """The price/news enrichment send_telegram() does, split out so a
    caller can build a fully-formed alert without sending it immediately
    -- needed to batch several setup alerts from one scan into a single
    Telegram message instead of one send per symbol."""
    if symbol is not None and price is not None:
        text += f"\n\nCurrent price: {price:,.4g}"
        headlines = fetch_news(symbol)
        if headlines:
            text += "\nRecent news:\n" + "\n".join(f"- {h}" for h in headlines)
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


def position_size(capital_usd, entry, stop, consecutive_losses):
    risk_amount = capital_usd * RISK_PCT_PER_TRADE
    if consecutive_losses >= LOSS_THROTTLE_AFTER:
        risk_amount *= 0.5
    stop_distance = abs(entry - stop)
    if stop_distance <= 0:
        return 0
    return risk_amount / stop_distance


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
        "consecutive_losses": 0, "last_alert": {},
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
        "last_alert": {},
    })
    if closed_bars:
        recent = closed_bars[-10:]
        sym_state["range_high"] = max(b["high"] for b in recent)
        sym_state["range_low"] = min(b["low"] for b in recent)


# ---------------------------------------------------------------- logic ----

def check_watching(symbol, tradable, sym_state, closed_bars, last_closed, capital):
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
        qty = position_size(capital, close, stop, losses)
        text = build_alert_text(
            f"{symbol} BREAKOUT (confirmed close){tag}\n\n"
            f"BUY\nEntry: {close:,.4g}\nStoploss: {stop:,.4g}\nVolume: ~{qty:.6g} units\n"
            f"Take profit: Keep trailing (no fixed target)\n"
            f"{expected_profit_line(close, stop, qty, currency=currency)}\n\n"
            f"Vol {vol:,.1f} vs avg {vol_avg:,.1f}, above 10-EMA ({trend_ema:,.4g}).\n\n"
            f"Took this? Reply: open {symbol} long",
            symbol=symbol, price=close,
        )
        sym_state["last_alert"] = {"type": "breakout_long", "level": range_high, "bar_time": bar_time}
        return {"text": text, "type": "breakout_long", "direction": "long", "entry": close, "stop": stop, "qty": qty, "target": None}

    if close < range_low and vol > vol_avg:
        if trend_ema and close > trend_ema:
            return None
        if already_alerted.get("type") == "breakdown_short" and already_alerted.get("level") == range_low:
            return None
        stop = last_closed["high"] + 0.5 * n
        qty = position_size(capital, close, stop, losses)
        text = build_alert_text(
            f"{symbol} BREAKDOWN (confirmed close){tag}\n\n"
            f"SELL\nEntry: {close:,.4g}\nStoploss: {stop:,.4g}\nVolume: ~{qty:.6g} units\n"
            f"Take profit: Keep trailing (no fixed target)\n"
            f"{expected_profit_line(close, stop, qty, currency=currency)}\n\n"
            f"Vol {vol:,.1f} vs avg {vol_avg:,.1f}, below 10-EMA ({trend_ema:,.4g}).\n\n"
            f"Took this? Reply: open {symbol} short",
            symbol=symbol, price=close,
        )
        sym_state["last_alert"] = {"type": "breakdown_short", "level": range_low, "bar_time": bar_time}
        return {"text": text, "type": "breakdown_short", "direction": "short", "entry": close, "stop": stop, "qty": qty, "target": None}

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
            qty = position_size(capital, close, stop, losses)
            text = build_alert_text(
                f"{symbol} RANGE REJECTION (bullish){tag}\n\n"
                f"BUY\nEntry: {close:,.4g}\nStoploss: {stop:,.4g}\nVolume: ~{qty:.6g} units\n"
                f"Take profit: {range_high:,.4g} (range high)\n"
                f"{expected_profit_line(close, stop, qty, range_high, currency=currency)}\n\n"
                f"Wicked to {last_closed['low']:,.4g} near range low {range_low:,.4g}, closed upper half.\n\n"
                f"Took this? Reply: open {symbol} long",
                symbol=symbol, price=close,
            )
            sym_state["last_alert"] = {"type": "range_long_rejection", "bar_time": bar_time}
            return {"text": text, "type": "range_long_rejection", "direction": "long", "entry": close, "stop": stop, "qty": qty, "target": range_high}
        return None

    near_high = last_closed["high"] >= range_high * (1 - REJECTION_BUFFER_PCT)
    bearish_rejection = close < (last_closed["low"] + last_closed["high"]) / 2
    if near_high and bearish_rejection and close > range_low:
        if trend_ema and close > trend_ema:
            return None
        if already_alerted.get("type") != "range_short_rejection" or already_alerted.get("bar_time") != bar_time:
            stop = last_closed["high"] + 0.3 * n
            qty = position_size(capital, close, stop, losses)
            text = build_alert_text(
                f"{symbol} RANGE REJECTION (bearish){tag}\n\n"
                f"SELL\nEntry: {close:,.4g}\nStoploss: {stop:,.4g}\nVolume: ~{qty:.6g} units\n"
                f"Take profit: {range_low:,.4g} (range low)\n"
                f"{expected_profit_line(close, stop, qty, range_low, currency=currency)}\n\n"
                f"Wicked to {last_closed['high']:,.4g} near range high {range_high:,.4g}, closed lower half.\n\n"
                f"Took this? Reply: open {symbol} short",
                symbol=symbol, price=close,
            )
            sym_state["last_alert"] = {"type": "range_short_rejection", "bar_time": bar_time}
            return {"text": text, "type": "range_short_rejection", "direction": "short", "entry": close, "stop": stop, "qty": qty, "target": range_low}
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
    tag = "" if tradable else " (analysis only)"

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
            rearm_to_watching(sym_state, closed_bars)
            return

        if close < stop:
            if notify:
                send_telegram(f"{symbol} STOP HIT -- long{tag}\n\nClose {close:,.4g} broke below stop {stop:,.4g}. Sell now if you haven't already.", symbol=symbol, price=close)
            pnl = close - entry
            log_trade(sym_state, "long", entry, close, pnl, "stop_hit")
            sym_state["consecutive_losses"] = 0 if pnl >= 0 else sym_state.get("consecutive_losses", 0) + 1
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
            sym_state["consecutive_losses"] = 0 if pnl >= 0 else sym_state.get("consecutive_losses", 0) + 1
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
    fired_setups = []
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

        # Shadow-track every setup this symbol has ever fired, whether or
        # not the user took it -- reuses check_open()'s exact trailing
        # stop/target/stop-hit logic (notify=False, so zero extra
        # Telegram messages) against the bars already fetched this cycle,
        # so "did it actually reach the expected profit" has a real
        # answer instead of just the alert's promise.
        for log_entry in setup_log:
            if log_entry["resolved"] or log_entry["symbol"] != symbol:
                continue
            shadow = log_entry["shadow"]
            before = len(shadow["trade_journal"])
            check_open(symbol, tradable, shadow, closed_bars, last_closed, notify=False)
            if len(shadow["trade_journal"]) > before:
                log_entry["resolved"] = True
                log_entry["outcome"] = shadow["trade_journal"][-1]

        alert = check_watching(symbol, tradable, sym_state, closed_bars, last_closed, capital)
        if alert:
            fired_setups.append(alert["text"])
            setup_log.append({
                "symbol": symbol, "type": alert["type"], "direction": alert["direction"],
                "entry": alert["entry"], "stop": alert["stop"], "target": alert["target"],
                "qty": alert["qty"], "fired_at": datetime.now(timezone.utc).isoformat(),
                "resolved": False, "outcome": None,
                "shadow": {
                    "direction": alert["direction"], "entry_price": alert["entry"],
                    "entry_qty": alert["qty"], "stop_loss": alert["stop"],
                    "extreme_since_entry": alert["entry"], "peak_profit_per_unit": 0,
                    "take_profit_target": alert["target"], "consecutive_losses": 0,
                    "trade_journal": [],
                },
            })

    if fired_setups:
        # One message per scan covering every setup that fired, instead
        # of a separate Telegram send per symbol -- so 5 setups in one
        # scan is 1 notification to react to, not 5.
        divider = "\n\n" + ("=" * 20) + "\n\n"
        header = f"{len(fired_setups)} setup(s) this scan:\n\n"
        send_telegram(header + divider.join(fired_setups))

    save_state(state)


if __name__ == "__main__":
    sys.exit(main())
