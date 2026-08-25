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


def send_heartbeat(symbol, sym_state, close):
    """Unconditional status update, every run, regardless of whether
    anything's actionable -- mirrors the running commentary given in chat
    each cycle ('still range-bound, staying silent' etc). Used for BTC-USD
    always (per the user's original request), and for any symbol while
    it's in an open position (per a later request to get 5-minute updates
    on whatever's actually open, not just BTC). Everything else (watching,
    non-BTC) stays alert-only to avoid noise."""
    status = sym_state.get("status", "watching")
    if status == "open":
        direction = sym_state["direction"]
        entry = sym_state["entry_price"]
        stop = sym_state["stop_loss"]
        qty = sym_state.get("entry_qty")
        pnl_per_unit = (close - entry) if direction == "long" else (entry - close)
        pnl_pct = (pnl_per_unit / entry * 100) if entry else 0
        if qty:
            pnl_str = f"{pnl_per_unit * qty:+,.4g} ({pnl_pct:+.2f}%)"
        else:
            pnl_str = f"{pnl_pct:+.2f}% (qty not set, no $ figure)"
        text = (
            f"{symbol} update -- {direction} open\n"
            f"Entry: {entry:,.4g} | Current: {close:,.4g} | Stop: {stop:,.4g}\n"
            f"Unrealized P&L: {pnl_str}"
        )
    else:
        text = (
            f"{symbol} update -- watching\n"
            f"Current: {close:,.4g} | Range: {sym_state.get('range_low'):,.4g} - {sym_state.get('range_high'):,.4g}"
        )
    send_telegram(text)


def market_for(symbol):
    if any(e["symbol"] == symbol for e in CRYPTO_WATCHLIST):
        return "crypto"
    if symbol.endswith(".NS"):
        return "india"
    return "us"


def resolve_symbol(raw, symbols_state):
    raw = raw.strip().upper()
    for candidate in (raw, f"{raw}-USD", f"{raw}.NS"):
        if candidate in symbols_state:
            return candidate
    open_matches = [s for s in symbols_state if symbols_state[s].get("status") == "open" and raw in s]
    return open_matches[0] if len(open_matches) == 1 else None


def sync_fills(state):
    """Auto-tracking opens a position off the alert's snapshot price the
    instant a signal fires -- but the trade is placed manually, seconds to
    minutes later, so the real fill price is almost never exactly that.
    Rather than requiring a chat session to correct it, the user can just
    reply directly in the Telegram thread and this picks it up on the next
    cycle (every ~5 min), from wherever they are:

      fill SYMBOL price [qty]         -- correct entry_price (and
                                         entry_qty, or qty is re-derived
                                         from the existing stop-loss and
                                         current risk settings)
      skip SYMBOL                      -- this alert wasn't actually
                                         taken; stop tracking it without
                                         logging a fake trade
      open SYMBOL long|short           -- register a trade that didn't
                                         come from a bot alert at all
                                         (started entirely off your own
                                         read of the chart) so it still
                                         gets trailing-stop/stop-hit
                                         tracking from here on. Entry is
                                         fetched off the latest closed
                                         bar and the stop is the same
                                         ATR-based formula a real signal
                                         would have used.
      open SYMBOL long|short entry stop [qty]
                                        -- same, but with exact entry/stop
                                         (and optionally qty) instead of
                                         the auto-fetched approximation
      close SYMBOL [price]             -- you exited manually (took
                                         profit, changed your mind, etc.)
                                         outside of a stop/target hit --
                                         logs it as a real trade and
                                         re-arms to watching. Price
                                         defaults to the latest fetched
                                         price if omitted.

    Runs at the top of every invocation, regardless of mode, so a
    correction lands as fast as possible. Only messages from the
    configured TELEGRAM_CHAT_ID are honored."""
    if not BOT_TOKEN or not CHAT_ID:
        return
    offset = state.get("telegram_update_offset", 0)
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/getUpdates?offset={offset}&timeout=0"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "btc-monitor-bot"})
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read())
    except Exception as e:
        print(f"sync_fills: getUpdates failed ({e})")
        return
    if not data.get("ok"):
        return

    symbols_state = state.setdefault("symbols", {})
    for update in data["result"]:
        state["telegram_update_offset"] = update["update_id"] + 1
        msg = update.get("message") or update.get("edited_message")
        if not msg or str(msg.get("chat", {}).get("id")) != str(CHAT_ID):
            continue
        parts = (msg.get("text") or "").strip().split()
        if not parts:
            continue
        cmd = parts[0].lower()

        if cmd == "fill" and len(parts) >= 3:
            symbol = resolve_symbol(parts[1], symbols_state)
            sym_state = symbols_state.get(symbol) if symbol else None
            if not sym_state or sym_state.get("status") != "open":
                send_telegram(f"sync: no open position found for '{parts[1]}'")
                continue
            try:
                price = float(parts[2])
                qty = float(parts[3]) if len(parts) >= 4 else None
            except ValueError:
                send_telegram(f"sync: couldn't parse '{' '.join(parts)}' -- use: fill SYMBOL price [qty]")
                continue
            sym_state["entry_price"] = price
            sym_state["extreme_since_entry"] = price
            sym_state["peak_profit_per_unit"] = 0
            if qty is not None:
                sym_state["entry_qty"] = qty
            elif sym_state.get("stop_loss") is not None:
                capital = state.get("capital_inr", 100) if symbol.endswith(".NS") else state.get("capital_usd", 100)
                sym_state["entry_qty"] = position_size(
                    capital, price, sym_state["stop_loss"], sym_state.get("consecutive_losses", 0))
            qty_str = f", qty {sym_state['entry_qty']:.6g}" if sym_state.get("entry_qty") else ""
            send_telegram(f"{symbol} entry corrected -> {price:,.4g}{qty_str}")

        elif cmd == "skip" and len(parts) >= 2:
            symbol = resolve_symbol(parts[1], symbols_state)
            sym_state = symbols_state.get(symbol) if symbol else None
            if not sym_state or sym_state.get("status") != "open":
                send_telegram(f"sync: no open position found for '{parts[1]}'")
                continue
            rearm_to_watching(sym_state)
            send_telegram(f"{symbol}: marked not taken, back to watching (no trade logged).")

        elif cmd == "open" and len(parts) >= 3:
            symbol = resolve_symbol(parts[1], symbols_state)
            sym_state = symbols_state.get(symbol) if symbol else None
            if not sym_state:
                send_telegram(f"sync: unknown symbol '{parts[1]}'")
                continue
            if sym_state.get("status") == "open":
                send_telegram(f"sync: {symbol} is already open -- use 'fill {symbol} price [qty]' to correct it instead.")
                continue
            direction = parts[2].lower()
            if direction not in ("long", "short"):
                send_telegram(f"sync: couldn't parse '{' '.join(parts)}' -- use: open SYMBOL long|short [entry stop [qty]]")
                continue

            qty = None
            if len(parts) >= 5:
                try:
                    entry = float(parts[3])
                    stop = float(parts[4])
                    qty = float(parts[5]) if len(parts) >= 6 else None
                except ValueError:
                    send_telegram(f"sync: couldn't parse '{' '.join(parts)}' -- use: open SYMBOL long|short [entry stop [qty]]")
                    continue
            else:
                # No entry/stop given -- fetch the latest price and derive
                # a stop with the same ATR-based formula a real breakout
                # signal would have used, so a purely self-initiated trade
                # gets a sane stop instead of none at all.
                market = market_for(symbol)
                try:
                    bars = fetch_klines(symbol, market, limit=30)
                except Exception as e:
                    send_telegram(f"sync: couldn't fetch price for {symbol} ({e}) -- try: open {symbol} {direction} entry stop [qty]")
                    continue
                if len(bars) < 15:
                    send_telegram(f"sync: not enough data for {symbol} -- try: open {symbol} {direction} entry stop [qty]")
                    continue
                closed_bars = bars[:-1]
                last_closed = closed_bars[-1]
                entry = last_closed["close"]
                n = atr(closed_bars)
                stop = last_closed["low"] - 0.5 * n if direction == "long" else last_closed["high"] + 0.5 * n

            if qty is None:
                capital = state.get("capital_inr", 100) if symbol.endswith(".NS") else state.get("capital_usd", 100)
                qty = position_size(capital, entry, stop, sym_state.get("consecutive_losses", 0))
            open_position(sym_state, direction, entry, stop, qty, None)
            send_telegram(f"{symbol} now tracked -- {direction}, entry {entry:,.4g}, stop {stop:,.4g}, qty {qty:.6g}. You'll get trail/stop updates until it closes.")

        elif cmd == "close" and len(parts) >= 2:
            symbol = resolve_symbol(parts[1], symbols_state)
            sym_state = symbols_state.get(symbol) if symbol else None
            if not sym_state or sym_state.get("status") != "open":
                send_telegram(f"sync: no open position found for '{parts[1]}'")
                continue
            if len(parts) >= 3:
                try:
                    close_price = float(parts[2])
                except ValueError:
                    send_telegram(f"sync: couldn't parse '{' '.join(parts)}' -- use: close SYMBOL [price]")
                    continue
            else:
                market = market_for(symbol)
                try:
                    bars = fetch_klines(symbol, market, limit=5)
                    close_price = bars[-1]["close"]
                except Exception as e:
                    send_telegram(f"sync: couldn't fetch price for {symbol} ({e}) -- try: close {symbol} price")
                    continue
            direction = sym_state["direction"]
            entry = sym_state["entry_price"]
            qty = sym_state.get("entry_qty")
            pnl = (close_price - entry) if direction == "long" else (entry - close_price)
            log_trade(sym_state, direction, entry, close_price, pnl, "manual_close")
            sym_state["consecutive_losses"] = 0 if pnl >= 0 else sym_state.get("consecutive_losses", 0) + 1
            rearm_to_watching(sym_state)
            pnl_str = f"{pnl * qty:+,.4g}" if qty else f"{pnl:+,.4g}/unit"
            send_telegram(f"{symbol} closed manually @ {close_price:,.4g} -- P&L {pnl_str}. Back to watching.")

        elif cmd in ("fill", "skip", "open", "close"):
            # Right command, wrong number of args -- e.g. "fill dot" with
            # no price. Anything unmatched falls all the way through
            # silently otherwise (the offset still advances so the update
            # isn't retried), which is exactly what could hide a real sync
            # failure. Always reply so a mistyped command is visibly a
            # mistyped command, not radio silence.
            send_telegram(f"sync: '{' '.join(parts)}' is missing arguments -- see the command formats in any recent alert, or ask Claude.")

        elif cmd not in ("fill", "skip", "open"):
            continue  # not a bot command at all -- ordinary chat, ignore quietly


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


def open_position(sym_state, direction, entry_price, stop, qty, take_profit_target):
    """Flip a symbol from 'watching' to 'open' the moment its signal
    fires, with the exact entry/stop/qty the alert quoted. Previously
    check_watching() computed these values only to print them in the
    alert text and then discard them -- nothing ever set status="open",
    so check_open() (trailing stop, stop-hit detection, heartbeats) never
    ran unless a human manually copied the alert's numbers into
    state.json after the fact. That's now automatic."""
    sym_state.update({
        "status": "open", "direction": direction, "entry_price": entry_price,
        "entry_qty": qty, "stop_loss": stop, "extreme_since_entry": entry_price,
        "peak_profit_per_unit": 0, "take_profit_target": take_profit_target,
    })


# ---------------------------------------------------------------- logic ----

def check_watching(symbol, tradable, sym_state, closed_bars, last_closed, capital):
    """Returns the fully-formed alert text for a fired signal (with price
    and news already baked in via build_alert_text), or None if nothing
    fired. Does NOT send -- main() collects these across the whole scan
    and sends them as one batched message, instead of one Telegram
    message per symbol."""
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
        return text

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
        return text

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
            return text
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
            return text
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


def check_open(symbol, tradable, sym_state, closed_bars, last_closed):
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
            send_telegram(f"{symbol} TAKE PROFIT HIT -- long{tag}\n\nClose {close:,.4g} reached target {tp:,.4g}. Close now if you haven't already.", symbol=symbol, price=close)
            pnl = close - entry
            log_trade(sym_state, "long", entry, close, pnl, "take_profit")
            sym_state["consecutive_losses"] = 0
            rearm_to_watching(sym_state, closed_bars)
            return

        if close < stop:
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
            send_telegram(f"{symbol} long -- trail your stop{tag}\n\nNew high {extreme:,.4g}. Move stop from {stop:,.4g} to {candidate_stop:,.4g} (locks ~{locked_pct:.0f}% of peak gain).", symbol=symbol, price=close)
            return

        # Take-profit heads-up: based on giveback from the peak profit
        # actually reached, not an ATR-relative floor that can
        # contradict itself in a fast reversal. Fires earlier (25%
        # giveback) than the hard profit-lock stop above -- an early
        # warning before the guaranteed floor even matters.
        giveback_pct = (peak_profit - current_profit) / peak_profit if peak_profit > 0 else 0
        if peak_profit > 0.5 * n and giveback_pct > 0.25:
            send_telegram(f"{symbol} long -- consider taking profit{tag}\n\nPeak gain was {peak_profit:,.4g}/unit, now {current_profit:,.4g}/unit -- given back {giveback_pct*100:.0f}%. Still in profit; your call.", symbol=symbol, price=close)

    elif direction == "short":
        extreme = min(extreme, last_closed["low"])
        sym_state["extreme_since_entry"] = extreme
        current_profit = entry - close
        peak_profit = max(sym_state.get("peak_profit_per_unit", 0), entry - extreme, current_profit)
        sym_state["peak_profit_per_unit"] = peak_profit

        if tp is not None and close <= tp:
            send_telegram(f"{symbol} TAKE PROFIT HIT -- short{tag}\n\nClose {close:,.4g} reached target {tp:,.4g}. Close now if you haven't already.", symbol=symbol, price=close)
            pnl = entry - close
            log_trade(sym_state, "short", entry, close, pnl, "take_profit")
            sym_state["consecutive_losses"] = 0
            rearm_to_watching(sym_state, closed_bars)
            return

        if close > stop:
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
            send_telegram(f"{symbol} short -- trail your stop{tag}\n\nNew low {extreme:,.4g}. Move stop from {stop:,.4g} to {candidate_stop:,.4g} (locks ~{locked_pct:.0f}% of peak gain).", symbol=symbol, price=close)
            return

        giveback_pct = (peak_profit - current_profit) / peak_profit if peak_profit > 0 else 0
        if peak_profit > 0.5 * n and giveback_pct > 0.25:
            send_telegram(f"{symbol} short -- consider taking profit{tag}\n\nPeak gain was {peak_profit:,.4g}/unit, now {current_profit:,.4g}/unit -- given back {giveback_pct*100:.0f}%. Still in profit; your call.", symbol=symbol, price=close)


def main():
    # "open" mode: only check symbols currently in an open position, for
    # a fast 5-minute cadence that reacts quickly to a stop hit or
    # reversal, without re-scanning the full watchlist needlessly.
    # Default (no arg): full scan on the normal 15-minute cadence.
    mode = sys.argv[1] if len(sys.argv) > 1 else "full"

    state = load_state()
    # DISABLED 2026-08-25: sync_fills() was replaying the user's entire
    # historical command backlog on every run (12+ repeated Telegram
    # messages in a single burst) instead of processing only new ones --
    # the telegram_update_offset it relies on was not reliably surviving
    # between runs. Turned off entirely until that's root-caused with the
    # user not being spammed in the meantime. fill/skip/open/close no
    # longer work over Telegram while this is off.
    # sync_fills(state)
    symbols_state = state.setdefault("symbols", {})
    capital_usd = state.get("capital_usd", 100)
    capital_inr = state.get("capital_inr", 100)
    watchlist = build_watchlist(state)

    if mode == "open":
        watchlist = [e for e in watchlist if symbols_state.get(e["symbol"], {}).get("status") == "open"]
        if not watchlist:
            print("open mode: no open positions, nothing to check")
            # NOT an early return -- sync_fills() already ran above and
            # may have changed state (a "skip" rearming a position back to
            # watching, an "open" that a later command then undid, an
            # advanced telegram_update_offset). An early return here used
            # to skip save_state() below and silently discard all of that.

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
        status = sym_state.get("status", "watching")
        capital = capital_inr if market == "india" else capital_usd
        if status == "watching":
            alert = check_watching(symbol, tradable, sym_state, closed_bars, last_closed, capital)
            if alert:
                fired_setups.append(alert)
        elif status == "open":
            check_open(symbol, tradable, sym_state, closed_bars, last_closed)
        # No "closed" status anymore -- check_open() re-arms straight back
        # to "watching" via rearm_to_watching() the moment a trade exits
        # (stop or take-profit), so the bot picks up the next signal on
        # its own instead of waiting on a human to re-arm it.

        if symbol == "BTC-USD" or sym_state.get("status") == "open":
            send_heartbeat(symbol, sym_state, last_closed["close"])

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
