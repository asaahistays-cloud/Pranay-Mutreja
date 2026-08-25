#!/usr/bin/env python3
"""
Multi-market monitor -- v3.

Covers three watchlists: crypto (Coinbase), US equities (Yahoo Finance),
Indian equities (Yahoo Finance, .NS suffix). Applies the same decision
rules to every symbol: confirmed-close breakout/breakdown with volume and
trend confirmation, range-boundary rejection, ATR-based stops/sizing,
trailing stops, take-profit heuristic, loss-throttled sizing, alert
de-duplication. See the original v2 notes below for what's deliberately
NOT implemented and why -- still true here, just applied per-symbol now.

Indian equities are NOT tradable on TradingView's paper account (confirmed
during manual testing -- NSE symbols aren't supported there), so alerts
for those are clearly labeled analysis-only.

US and Indian markets have trading hours, unlike crypto's 24/7 -- a
staleness check skips a symbol for the cycle if its latest bar is old
(market closed), rather than firing a false signal off stale data.

Never places trades -- alert only. State is persisted to state.json,
committed back to the repo by the GitHub Actions workflow after each run.
"""
import json
import os
import sys
import time
import urllib.request
import urllib.error

STATE_FILE = os.path.join(os.path.dirname(__file__), "state.json")
BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID")

ATR_PERIOD = 14
EMA_PERIOD = 10
REJECTION_BUFFER_PCT = 0.0015
RISK_PCT_PER_TRADE = 0.01
LOSS_THROTTLE_AFTER = 2
STALE_THRESHOLD_SECONDS = 45 * 60  # skip a symbol if its latest bar is older than this

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


def send_telegram(text, symbol=None, price=None):
    if symbol is not None and price is not None:
        text += f"\n\nCurrent price: {price:,.4g}"
        headlines = fetch_news(symbol)
        if headlines:
            text += "\nRecent news:\n" + "\n".join(f"- {h}" for h in headlines)

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


def send_heartbeat(symbol, sym_state, close):
    """Unconditional status update, every run, regardless of whether
    anything's actionable -- mirrors the running commentary given in chat
    each cycle ('still range-bound, staying silent' etc). Only used for
    BTC-USD per the user's explicit request -- everything else stays
    alert-only to avoid noise."""
    status = sym_state.get("status", "watching")
    if status == "open":
        direction = sym_state["direction"]
        entry = sym_state["entry_price"]
        stop = sym_state["stop_loss"]
        text = (
            f"{symbol} update -- {direction} open\n"
            f"Entry: {entry:,.4g} | Current: {close:,.4g} | Stop: {stop:,.4g}"
        )
    else:
        text = (
            f"{symbol} update -- watching\n"
            f"Current: {close:,.4g} | Range: {sym_state.get('range_low'):,.4g} - {sym_state.get('range_high'):,.4g}"
        )
    send_telegram(text)


def default_symbol_state(closed_bars):
    recent_high = max(b["high"] for b in closed_bars[-10:])
    recent_low = min(b["low"] for b in closed_bars[-10:])
    return {
        "status": "watching", "range_high": recent_high, "range_low": recent_low,
        "direction": None, "entry_price": None, "stop_loss": None,
        "extreme_since_entry": None, "consecutive_losses": 0, "last_alert": {},
        "trade_journal": [],
    }


# ---------------------------------------------------------------- logic ----

def check_watching(symbol, tradable, sym_state, closed_bars, last_closed, capital):
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

    if close > range_high and vol > vol_avg:
        if trend_ema and close < trend_ema:
            return
        if already_alerted.get("type") == "breakout_long" and already_alerted.get("level") == range_high:
            return
        stop = last_closed["low"] - 0.5 * n
        qty = position_size(capital, close, stop, losses)
        send_telegram(
            f"{symbol} BREAKOUT (confirmed close){tag}\n\n"
            f"BUY\nEntry: {close:,.4g}\nStoploss: {stop:,.4g}\nVolume: ~{qty:.6g} units\n"
            f"Take profit: Keep trailing (no fixed target)\n\n"
            f"Vol {vol:,.1f} vs avg {vol_avg:,.1f}, above 10-EMA ({trend_ema:,.4g}).",
            symbol=symbol, price=close,
        )
        sym_state["last_alert"] = {"type": "breakout_long", "level": range_high, "bar_time": bar_time}
        return

    if close < range_low and vol > vol_avg:
        if trend_ema and close > trend_ema:
            return
        if already_alerted.get("type") == "breakdown_short" and already_alerted.get("level") == range_low:
            return
        stop = last_closed["high"] + 0.5 * n
        qty = position_size(capital, close, stop, losses)
        send_telegram(
            f"{symbol} BREAKDOWN (confirmed close){tag}\n\n"
            f"SELL\nEntry: {close:,.4g}\nStoploss: {stop:,.4g}\nVolume: ~{qty:.6g} units\n"
            f"Take profit: Keep trailing (no fixed target)\n\n"
            f"Vol {vol:,.1f} vs avg {vol_avg:,.1f}, below 10-EMA ({trend_ema:,.4g}).",
            symbol=symbol, price=close,
        )
        sym_state["last_alert"] = {"type": "breakdown_short", "level": range_low, "bar_time": bar_time}
        return

    near_low = last_closed["low"] <= range_low * (1 + REJECTION_BUFFER_PCT)
    bullish_rejection = close > (last_closed["low"] + last_closed["high"]) / 2
    if near_low and bullish_rejection and close < range_high:
        if already_alerted.get("type") != "range_long_rejection" or already_alerted.get("bar_time") != bar_time:
            stop = last_closed["low"] - 0.3 * n
            qty = position_size(capital, close, stop, losses)
            send_telegram(
                f"{symbol} RANGE REJECTION (bullish){tag}\n\n"
                f"BUY\nEntry: {close:,.4g}\nStoploss: {stop:,.4g}\nVolume: ~{qty:.6g} units\n"
                f"Take profit: {range_high:,.4g} (range high)\n\n"
                f"Wicked to {last_closed['low']:,.4g} near range low {range_low:,.4g}, closed upper half.",
                symbol=symbol, price=close,
            )
            sym_state["last_alert"] = {"type": "range_long_rejection", "bar_time": bar_time}
        return

    near_high = last_closed["high"] >= range_high * (1 - REJECTION_BUFFER_PCT)
    bearish_rejection = close < (last_closed["low"] + last_closed["high"]) / 2
    if near_high and bearish_rejection and close > range_low:
        if already_alerted.get("type") != "range_short_rejection" or already_alerted.get("bar_time") != bar_time:
            stop = last_closed["high"] + 0.3 * n
            qty = position_size(capital, close, stop, losses)
            send_telegram(
                f"{symbol} RANGE REJECTION (bearish){tag}\n\n"
                f"SELL\nEntry: {close:,.4g}\nStoploss: {stop:,.4g}\nVolume: ~{qty:.6g} units\n"
                f"Take profit: {range_low:,.4g} (range low)\n\n"
                f"Wicked to {last_closed['high']:,.4g} near range high {range_high:,.4g}, closed lower half.",
                symbol=symbol, price=close,
            )
            sym_state["last_alert"] = {"type": "range_short_rejection", "bar_time": bar_time}
        return

    if range_low < close < range_high:
        sym_state["last_alert"] = {}
    recent_high = max(b["high"] for b in closed_bars[-10:])
    recent_low = min(b["low"] for b in closed_bars[-10:])
    if recent_high > range_high:
        sym_state["range_high"] = recent_high
    if recent_low < range_low:
        sym_state["range_low"] = recent_low


def check_open(symbol, tradable, sym_state, closed_bars, last_closed):
    direction = sym_state["direction"]
    stop = sym_state["stop_loss"]
    entry = sym_state["entry_price"]
    close = last_closed["close"]
    n = atr(closed_bars)
    extreme = sym_state.get("extreme_since_entry", entry)
    tag = "" if tradable else " (analysis only)"

    if direction == "long":
        extreme = max(extreme, last_closed["high"])
        sym_state["extreme_since_entry"] = extreme
        if close < stop:
            send_telegram(f"{symbol} STOP HIT -- long{tag}\n\nClose {close:,.4g} broke below stop {stop:,.4g}. Sell now if you haven't already.", symbol=symbol, price=close)
            sym_state["status"] = "closed"
            pnl = close - entry
            sym_state.setdefault("trade_journal", []).append({"direction": "long", "entry": entry, "exit": close, "pnl_per_unit": pnl, "exit_reason": "stop_hit"})
            sym_state["consecutive_losses"] = 0 if pnl >= 0 else sym_state.get("consecutive_losses", 0) + 1
            return
        candidate_stop = extreme - 1.5 * n
        if candidate_stop > stop * 1.001:
            sym_state["stop_loss"] = candidate_stop
            send_telegram(f"{symbol} long -- trail your stop{tag}\n\nNew high {extreme:,.4g}. Move stop from {stop:,.4g} to {candidate_stop:,.4g}.", symbol=symbol, price=close)
            return
        profit = close - entry
        giveback = extreme - close
        if profit > 1.5 * n and giveback > 0.5 * (extreme - entry):
            send_telegram(f"{symbol} long -- consider taking profit{tag}\n\nRan to {extreme:,.4g}, now {close:,.4g} -- given back over half the move. Still in profit; your call.", symbol=symbol, price=close)

    elif direction == "short":
        extreme = min(extreme, last_closed["low"])
        sym_state["extreme_since_entry"] = extreme
        if close > stop:
            send_telegram(f"{symbol} STOP HIT -- short{tag}\n\nClose {close:,.4g} broke above stop {stop:,.4g}. Buy back / close now if you haven't already.", symbol=symbol, price=close)
            sym_state["status"] = "closed"
            pnl = entry - close
            sym_state.setdefault("trade_journal", []).append({"direction": "short", "entry": entry, "exit": close, "pnl_per_unit": pnl, "exit_reason": "stop_hit"})
            sym_state["consecutive_losses"] = 0 if pnl >= 0 else sym_state.get("consecutive_losses", 0) + 1
            return
        candidate_stop = extreme + 1.5 * n
        if candidate_stop < stop * 0.999:
            sym_state["stop_loss"] = candidate_stop
            send_telegram(f"{symbol} short -- trail your stop{tag}\n\nNew low {extreme:,.4g}. Move stop from {stop:,.4g} to {candidate_stop:,.4g}.", symbol=symbol, price=close)
            return
        profit = entry - close
        giveback = close - extreme
        if profit > 1.5 * n and giveback > 0.5 * (entry - extreme):
            send_telegram(f"{symbol} short -- consider taking profit{tag}\n\nRan to {extreme:,.4g}, now {close:,.4g} -- given back over half the move. Still in profit; your call.", symbol=symbol, price=close)


def main():
    # "open" mode: only check symbols currently in an open position, for
    # a fast 5-minute cadence that reacts quickly to a stop hit or
    # reversal, without re-scanning the full watchlist needlessly.
    # Default (no arg): full scan on the normal 15-minute cadence.
    mode = sys.argv[1] if len(sys.argv) > 1 else "full"

    state = load_state()
    symbols_state = state.setdefault("symbols", {})
    capital_usd = state.get("capital_usd", 100)
    capital_inr = state.get("capital_inr", 100)
    watchlist = build_watchlist(state)

    if mode == "open":
        watchlist = [e for e in watchlist if symbols_state.get(e["symbol"], {}).get("status") == "open"]
        if not watchlist:
            print("open mode: no open positions, nothing to check")
            return

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
        status = sym_state.get("status", "watching")
        capital = capital_inr if market == "india" else capital_usd
        if status == "watching":
            check_watching(symbol, tradable, sym_state, closed_bars, last_closed, capital)
        elif status == "open":
            check_open(symbol, tradable, sym_state, closed_bars, last_closed)
        # "closed" left alone -- a human/chat consciously re-arms it

        if symbol == "BTC-USD":
            send_heartbeat(symbol, sym_state, last_closed["close"])

    save_state(state)


if __name__ == "__main__":
    sys.exit(main())
