#!/usr/bin/env python3
"""
BTC 15m range/breakout monitor.
Fetches candles from Coinbase's public API, checks for a confirmed-close
breakout or range-boundary rejection, and sends a Telegram alert when one
happens. Never places trades -- alert only.

Uses Coinbase rather than Binance because Binance geo-blocks requests from
US-based IPs (HTTP 451), which is exactly where GitHub's free runners live.
Coinbase has no such restriction on its public market-data endpoints.

State is persisted to state.json (committed back to the repo by the
GitHub Actions workflow after each run).
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


def fetch_klines(limit=20):
    url = (
        f"https://api.exchange.coinbase.com/products/{PRODUCT}/candles"
        f"?granularity={GRANULARITY_SECONDS}"
    )
    req = urllib.request.Request(url, headers={"User-Agent": "btc-monitor-bot"})
    with urllib.request.urlopen(req, timeout=15) as resp:
        raw = json.loads(resp.read())
    # Coinbase returns newest-first: [time, low, high, open, close, volume]
    raw.sort(key=lambda r: r[0])  # oldest -> newest, to match Binance ordering
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


def avg_volume(bars, exclude_last=1):
    sample = bars[:-exclude_last] if exclude_last else bars
    if not sample:
        return 0
    return sum(b["volume"] for b in sample) / len(sample)


def main():
    bars = fetch_klines(limit=20)
    # Last bar may still be forming; only the closed ones count for
    # "confirmed close" decisions (mirrors the discipline learned the
    # hard way in manual trading: never act on an unclosed bar's wick).
    closed_bars = bars[:-1]
    last_closed = closed_bars[-1]
    state = load_state()

    status = state.get("status", "watching")

    if status == "watching":
        range_high = state["range_high"]
        range_low = state["range_low"]
        vol_avg = avg_volume(closed_bars[-10:-1])
        close = last_closed["close"]
        vol = last_closed["volume"]

        if close > range_high and vol > vol_avg:
            msg = (
                f"BTC BREAKOUT (confirmed close)\n\n"
                f"15m close {close:,.2f} broke above range high {range_high:,.2f}, "
                f"volume {vol:,.1f} vs avg {vol_avg:,.1f}.\n\n"
                f"Consider a LONG here with a stop below the breakout bar's low "
                f"({last_closed['low']:,.2f}). Place manually if it fits your plan."
            )
            send_telegram(msg)
            state["proposed_setup"] = {
                "type": "breakout_long",
                "trigger_close": close,
                "trigger_volume": vol,
                "avg_volume": vol_avg,
                "suggested_stop": last_closed["low"],
            }
        elif close < range_low and vol > vol_avg:
            msg = (
                f"BTC BREAKDOWN (confirmed close)\n\n"
                f"15m close {close:,.2f} broke below range low {range_low:,.2f}, "
                f"volume {vol:,.1f} vs avg {vol_avg:,.1f}.\n\n"
                f"Consider a SHORT here with a stop above the breakdown bar's high "
                f"({last_closed['high']:,.2f}). Place manually if it fits your plan."
            )
            send_telegram(msg)
            state["proposed_setup"] = {
                "type": "breakdown_short",
                "trigger_close": close,
                "trigger_volume": vol,
                "avg_volume": vol_avg,
                "suggested_stop": last_closed["high"],
            }
        else:
            # Silently widen the range on a genuine new swing extreme,
            # same as the manual monitor does.
            recent_high = max(b["high"] for b in closed_bars[-10:])
            recent_low = min(b["low"] for b in closed_bars[-10:])
            if recent_high > range_high:
                state["range_high"] = recent_high
            if recent_low < range_low:
                state["range_low"] = recent_low

    elif status == "open":
        direction = state["direction"]
        stop = state["stop_loss"]
        close = last_closed["close"]

        if direction == "long" and close < stop:
            send_telegram(
                f"STOP HIT -- BTC long\n\n"
                f"15m confirmed close {close:,.2f} broke below stop {stop:,.2f}. "
                f"Sell now if you haven't already."
            )
            state["status"] = "closed"
        elif direction == "short" and close > stop:
            send_telegram(
                f"STOP HIT -- BTC short\n\n"
                f"15m confirmed close {close:,.2f} broke above stop {stop:,.2f}. "
                f"Buy back / close now if you haven't already."
            )
            state["status"] = "closed"
        # Trailing-stop and take-profit suggestions are intentionally left
        # for manual chat review -- this script only handles the
        # unambiguous, high-stakes case (stop hit) autonomously.

    save_state(state)


if __name__ == "__main__":
    sys.exit(main())
