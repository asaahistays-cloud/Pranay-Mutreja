#!/usr/bin/env python3
"""
BTC 15m range/breakout monitor -- v2.

Fetches candles from Coinbase's public API (Binance geo-blocks US IPs,
which is where GitHub's free runners live) and applies the same decision
rules used in manual chat-based monitoring, synthesized from several
classic frameworks:

  - Confirmed-close breakout/breakdown with volume confirmation
    (Livermore pivotal points / Darvas box breakout)
  - Range-boundary rejection trades (Darvas box range-trading)
  - ATR-based stops and position sizing (Turtle Trader "N")
  - 10-EMA trend filter on breakouts (Schwartz discipline -- only take
    breakouts in the direction of the near-term trend)
  - Trailing stop as new swing extremes form
  - Take-profit/reversal heuristic on open positions
  - "Never increase risk after a loss" -- consecutive-loss throttle

Deliberately NOT implemented, and why:
  - CANSLIM: needs fundamentals/earnings data, doesn't apply to a single
    crypto pair's price action
  - Soros reflexivity / Livermore "market tone": genuinely discretionary
    judgment, not a codifiable rule
  - Weinstein weekly Stage Analysis: needs a higher timeframe than this
    bot pulls -- a real future enhancement, not faked with a fake proxy
  - ORB (Opening Range Breakout): defined around a single market open;
    crypto trades 24/7 with no equivalent session

Never places trades -- alert only. State is persisted to state.json,
committed back to the repo by the GitHub Actions workflow after each run.
"""
import json
import os
import sys
import urllib.request
import urllib.error

PRODUCT = "BTC-USD"
GRANULARITY_SECONDS = 900  # 15 minutes
STATE_FILE = os.path.join(os.path.dirname(__file__), "state.json")

BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID")

ATR_PERIOD = 14
EMA_PERIOD = 10
REJECTION_BUFFER_PCT = 0.0015  # how close to the boundary counts as "at" it
RISK_PCT_PER_TRADE = 0.01      # 1% of capital risked per trade (Tudor Jones)
LOSS_THROTTLE_AFTER = 2        # consecutive losses before halving size


# ---------------------------------------------------------------- data ----

def fetch_klines(limit=60):
    url = (
        f"https://api.exchange.coinbase.com/products/{PRODUCT}/candles"
        f"?granularity={GRANULARITY_SECONDS}"
    )
    req = urllib.request.Request(url, headers={"User-Agent": "btc-monitor-bot"})
    with urllib.request.urlopen(req, timeout=15) as resp:
        raw = json.loads(resp.read())
    # Coinbase returns newest-first: [time, low, high, open, close, volume]
    raw.sort(key=lambda r: r[0])  # oldest -> newest
    bars = []
    for r in raw[-limit:]:
        bars.append({
            "open_time": r[0] * 1000,
            "open": float(r[3]),
            "high": float(r[2]),
            "low": float(r[1]),
            "close": float(r[4]),
            "volume": float(r[5]),
            "close_time": r[0] * 1000,
        })
    return bars


def load_state():
    with open(STATE_FILE) as f:
        return json.load(f)


def save_state(state):
    with open(STATE_FILE, "w") as f:
        json.dump(state, f, indent=2)


def send_telegram(text):
    if not BOT_TOKEN or not CHAT_ID:
        print("WARNING: TELEGRAM_BOT_TOKEN/TELEGRAM_CHAT_ID not set, skipping send.")
        print(text)
        return
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = json.dumps({"chat_id": CHAT_ID, "text": text}).encode()
    req = urllib.request.Request(
        url, data=payload, headers={"Content-Type": "application/json"}
    )
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
    """Average True Range over the last `period` bars (Turtle Trader's N)."""
    trs = []
    for i in range(1, len(bars)):
        h, l, prev_close = bars[i]["high"], bars[i]["low"], bars[i - 1]["close"]
        tr = max(h - l, abs(h - prev_close), abs(l - prev_close))
        trs.append(tr)
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
    """Risk RISK_PCT_PER_TRADE of capital per trade (Tudor Jones' 1% rule).
    Never increases size after a loss -- only holds steady or throttles
    down after LOSS_THROTTLE_AFTER consecutive losses (the 'no martingale,
    no averaging down' discipline)."""
    risk_amount = capital_usd * RISK_PCT_PER_TRADE
    if consecutive_losses >= LOSS_THROTTLE_AFTER:
        risk_amount *= 0.5
    stop_distance = abs(entry - stop)
    if stop_distance <= 0:
        return 0
    return risk_amount / stop_distance


# ---------------------------------------------------------------- logic ----

def check_watching(state, closed_bars, last_closed):
    range_high = state["range_high"]
    range_low = state["range_low"]
    close = last_closed["close"]
    vol = last_closed["volume"]
    vol_avg = avg_volume(closed_bars[-10:-1])
    trend_ema = ema([b["close"] for b in closed_bars[-(EMA_PERIOD * 3):]], EMA_PERIOD)
    n = atr(closed_bars)
    capital = state.get("capital_usd", 100)
    losses = state.get("consecutive_losses", 0)

    already_alerted = state.get("last_alert", {})
    bar_time = last_closed["close_time"]

    # --- Breakout / breakdown, confirmed close + volume + trend filter ---
    if close > range_high and vol > vol_avg:
        # Schwartz-style trend filter: only take the breakout if price is
        # also above its own near-term trend (10-EMA), i.e. the breakout
        # agrees with the prevailing direction rather than fighting it.
        if trend_ema and close < trend_ema:
            return  # breakout against the trend -- skip, stay silent
        # De-dup: only alert once per distinct breakout level, not every
        # single run while price stays elevated.
        if already_alerted.get("type") == "breakout_long" and already_alerted.get("level") == range_high:
            return
        stop = last_closed["low"] - 0.5 * n
        qty = position_size(capital, close, stop, losses)
        msg = (
            f"BTC BREAKOUT (confirmed close)\n\n"
            f"15m close {close:,.2f} broke above range high {range_high:,.2f}, "
            f"volume {vol:,.1f} vs avg {vol_avg:,.1f}. Above 10-EMA ({trend_ema:,.2f}), "
            f"trend-aligned.\n\n"
            f"Consider a LONG here.\n"
            f"Stop: {stop:,.2f} (breakout bar low - 0.5x ATR)\n"
            f"Suggested size: ~{qty:.6f} BTC (risking {RISK_PCT_PER_TRADE*100:.0f}% of ${capital:,.0f}"
            f"{', halved after consecutive losses' if losses >= LOSS_THROTTLE_AFTER else ''})\n\n"
            f"Place manually if it fits your plan."
        )
        send_telegram(msg)
        state["last_alert"] = {"type": "breakout_long", "level": range_high, "bar_time": bar_time}
        state["proposed_setup"] = {
            "type": "breakout_long", "trigger_close": close, "suggested_stop": stop, "suggested_qty": qty,
        }
        return

    if close < range_low and vol > vol_avg:
        if trend_ema and close > trend_ema:
            return
        if already_alerted.get("type") == "breakdown_short" and already_alerted.get("level") == range_low:
            return
        stop = last_closed["high"] + 0.5 * n
        qty = position_size(capital, close, stop, losses)
        msg = (
            f"BTC BREAKDOWN (confirmed close)\n\n"
            f"15m close {close:,.2f} broke below range low {range_low:,.2f}, "
            f"volume {vol:,.1f} vs avg {vol_avg:,.1f}. Below 10-EMA ({trend_ema:,.2f}), "
            f"trend-aligned.\n\n"
            f"Consider a SHORT here.\n"
            f"Stop: {stop:,.2f} (breakdown bar high + 0.5x ATR)\n"
            f"Suggested size: ~{qty:.6f} BTC (risking {RISK_PCT_PER_TRADE*100:.0f}% of ${capital:,.0f}"
            f"{', halved after consecutive losses' if losses >= LOSS_THROTTLE_AFTER else ''})\n\n"
            f"Place manually if it fits your plan."
        )
        send_telegram(msg)
        state["last_alert"] = {"type": "breakdown_short", "level": range_low, "bar_time": bar_time}
        state["proposed_setup"] = {
            "type": "breakdown_short", "trigger_close": close, "suggested_stop": stop, "suggested_qty": qty,
        }
        return

    # --- Range-boundary rejection (Darvas box range-trading) ---
    near_low = last_closed["low"] <= range_low * (1 + REJECTION_BUFFER_PCT)
    bullish_rejection = close > (last_closed["low"] + last_closed["high"]) / 2
    if near_low and bullish_rejection and close < range_high:
        if already_alerted.get("type") != "range_long_rejection" or already_alerted.get("bar_time") != bar_time:
            stop = last_closed["low"] - 0.3 * n
            qty = position_size(capital, close, stop, losses)
            msg = (
                f"BTC RANGE REJECTION (bullish)\n\n"
                f"15m bar wicked down to {last_closed['low']:,.2f} near range low "
                f"{range_low:,.2f} and closed at {close:,.2f}, in the upper half of "
                f"the bar -- rejection, not a breakdown.\n\n"
                f"Consider a range-trade LONG toward {range_high:,.2f}.\n"
                f"Stop: {stop:,.2f}\n"
                f"Suggested size: ~{qty:.6f} BTC\n\n"
                f"Place manually if it fits your plan."
            )
            send_telegram(msg)
            state["last_alert"] = {"type": "range_long_rejection", "bar_time": bar_time}
            state["proposed_setup"] = {
                "type": "range_long_rejection", "trigger_close": close, "suggested_stop": stop, "suggested_qty": qty,
            }
        return

    near_high = last_closed["high"] >= range_high * (1 - REJECTION_BUFFER_PCT)
    bearish_rejection = close < (last_closed["low"] + last_closed["high"]) / 2
    if near_high and bearish_rejection and close > range_low:
        if already_alerted.get("type") != "range_short_rejection" or already_alerted.get("bar_time") != bar_time:
            stop = last_closed["high"] + 0.3 * n
            qty = position_size(capital, close, stop, losses)
            msg = (
                f"BTC RANGE REJECTION (bearish)\n\n"
                f"15m bar wicked up to {last_closed['high']:,.2f} near range high "
                f"{range_high:,.2f} and closed at {close:,.2f}, in the lower half of "
                f"the bar -- rejection, not a breakout.\n\n"
                f"Consider a range-trade SHORT toward {range_low:,.2f}.\n"
                f"Stop: {stop:,.2f}\n"
                f"Suggested size: ~{qty:.6f} BTC\n\n"
                f"Place manually if it fits your plan."
            )
            send_telegram(msg)
            state["last_alert"] = {"type": "range_short_rejection", "bar_time": bar_time}
            state["proposed_setup"] = {
                "type": "range_short_rejection", "trigger_close": close, "suggested_stop": stop, "suggested_qty": qty,
            }
        return

    # --- Nothing actionable: reset the breakout de-dup once price is back
    # inside the range, and silently widen the range on a genuine new
    # swing extreme. ---
    if range_low < close < range_high:
        state["last_alert"] = {}
    recent_high = max(b["high"] for b in closed_bars[-10:])
    recent_low = min(b["low"] for b in closed_bars[-10:])
    if recent_high > range_high:
        state["range_high"] = recent_high
    if recent_low < range_low:
        state["range_low"] = recent_low


def check_open(state, closed_bars, last_closed):
    direction = state["direction"]
    stop = state["stop_loss"]
    entry = state["entry_price"]
    close = last_closed["close"]
    n = atr(closed_bars)
    extreme = state.get("extreme_since_entry", entry)

    if direction == "long":
        extreme = max(extreme, last_closed["high"])
        state["extreme_since_entry"] = extreme

        if close < stop:
            send_telegram(
                f"STOP HIT -- BTC long\n\n"
                f"15m confirmed close {close:,.2f} broke below stop {stop:,.2f}. "
                f"Sell now if you haven't already."
            )
            state["status"] = "closed"
            pnl = close - entry
            state.setdefault("trade_journal", []).append({
                "direction": "long", "entry": entry, "exit": close, "pnl_per_unit": pnl,
                "exit_reason": "stop_hit",
            })
            state["consecutive_losses"] = state.get("consecutive_losses", 0) + (1 if pnl < 0 else 0)
            if pnl >= 0:
                state["consecutive_losses"] = 0
            return

        # Trailing stop: only ever move it up, in the direction of profit,
        # once a genuine new swing high has formed since entry.
        candidate_stop = extreme - 1.5 * n
        if candidate_stop > stop * 1.001:
            state["stop_loss"] = candidate_stop
            send_telegram(
                f"BTC long -- trail your stop\n\n"
                f"New high {extreme:,.2f} since entry. Move stop from {stop:,.2f} "
                f"to {candidate_stop:,.2f} (1.5x ATR below the new high)."
            )
            return

        # Take-profit heuristic: in solid profit, and the last close gave
        # back a meaningful chunk of the move from the extreme -- flag for
        # manual review, don't auto-close.
        profit = close - entry
        giveback = extreme - close
        if profit > 1.5 * n and giveback > 0.5 * (extreme - entry):
            send_telegram(
                f"BTC long -- consider taking profit\n\n"
                f"Ran up to {extreme:,.2f}, now back to {close:,.2f} -- given back "
                f"over half the move from entry ({entry:,.2f}). Still in profit, but "
                f"momentum looks like it's fading. Your call -- not a stop hit."
            )

    elif direction == "short":
        extreme = min(extreme, last_closed["low"])
        state["extreme_since_entry"] = extreme

        if close > stop:
            send_telegram(
                f"STOP HIT -- BTC short\n\n"
                f"15m confirmed close {close:,.2f} broke above stop {stop:,.2f}. "
                f"Buy back / close now if you haven't already."
            )
            state["status"] = "closed"
            pnl = entry - close
            state.setdefault("trade_journal", []).append({
                "direction": "short", "entry": entry, "exit": close, "pnl_per_unit": pnl,
                "exit_reason": "stop_hit",
            })
            state["consecutive_losses"] = state.get("consecutive_losses", 0) + (1 if pnl < 0 else 0)
            if pnl >= 0:
                state["consecutive_losses"] = 0
            return

        candidate_stop = extreme + 1.5 * n
        if candidate_stop < stop * 0.999:
            state["stop_loss"] = candidate_stop
            send_telegram(
                f"BTC short -- trail your stop\n\n"
                f"New low {extreme:,.2f} since entry. Move stop from {stop:,.2f} "
                f"to {candidate_stop:,.2f} (1.5x ATR above the new low)."
            )
            return

        profit = entry - close
        giveback = close - extreme
        if profit > 1.5 * n and giveback > 0.5 * (entry - extreme):
            send_telegram(
                f"BTC short -- consider taking profit\n\n"
                f"Ran down to {extreme:,.2f}, now back to {close:,.2f} -- given back "
                f"over half the move from entry ({entry:,.2f}). Still in profit, but "
                f"momentum looks like it's fading. Your call -- not a stop hit."
            )


def main():
    bars = fetch_klines(limit=60)
    # Last bar may still be forming; only closed bars count for
    # "confirmed close" decisions -- never act on an unclosed bar's wick,
    # for entries, stops, trailing, or profit-taking alike.
    closed_bars = bars[:-1]
    last_closed = closed_bars[-1]
    state = load_state()

    status = state.get("status", "watching")
    if status == "watching":
        check_watching(state, closed_bars, last_closed)
    elif status == "open":
        check_open(state, closed_bars, last_closed)
    # "closed" status resets on the next manual/chat-driven review --
    # left alone here so a human (or chat) consciously picks the next
    # range rather than the bot silently re-arming itself.

    save_state(state)


if __name__ == "__main__":
    sys.exit(main())
