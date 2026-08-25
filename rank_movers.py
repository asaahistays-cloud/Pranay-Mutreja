#!/usr/bin/env python3
"""
Daily opening-range mover scanner.

Run once shortly after a market's opening range closes:
  - India: ~9:45 IST (scans right after the 9:15-9:45 opening range)
  - US: ~9:30-10:00 AM ET / ~7:00-7:30 PM IST (during EDT -- shifts an
    hour during US winter/EST, the workflow cron will need a manual
    nudge around the DST transitions)

Scans a broad universe of liquid large-caps for that market, ranks by
absolute % move from today's open, and sets the top 15 as that market's
active watchlist in state.json for the rest of the session. monitor.py
then applies the normal breakout/range/trailing logic to exactly those
15 symbols, same as it already does for crypto.

This is the ORB (Opening Range Breakout) framework applied at the
watchlist-selection level -- crypto has no session to anchor an ORB to,
but equities markets do, so this is where that framework actually fits.

If the scan can't get enough valid data (market holiday, feed hiccup),
it leaves the previous day's watchlist untouched rather than wiping it
with an empty/garbage list.
"""
import sys

import monitor

TOP_N = 15
MIN_VALID_RESULTS = 5  # don't overwrite the watchlist on a thin/bad scan

# India has no fractional-share support on the user's broker -- these are
# genuinely liquid large/mid-caps that happen to trade at low absolute
# prices (mostly PSU banks, PSU energy/infra, and other high-share-count
# names), not thin/manipulable penny stocks. Roughly Rs.10-500/share.
INDIA_UNIVERSE = [
    "PNB.NS", "BANKBARODA.NS", "CANBK.NS", "UNIONBANK.NS", "BANKINDIA.NS",
    "IDFCFIRSTB.NS", "FEDERALBNK.NS", "INDIANB.NS", "IOB.NS", "IOC.NS",
    "ONGC.NS", "GAIL.NS", "NTPC.NS", "POWERGRID.NS", "COALINDIA.NS",
    "SAIL.NS", "NATIONALUM.NS", "NHPC.NS", "TATAPOWER.NS", "VEDL.NS",
    "NMDC.NS", "HINDCOPPER.NS", "RECLTD.NS", "PFC.NS", "IRFC.NS",
    "SUZLON.NS", "ETERNAL.NS", "PAYTM.NS", "IDEA.NS", "YESBANK.NS",
    "RVNL.NS", "IRCON.NS", "HUDCO.NS", "BEL.NS", "BHEL.NS",
    "GMRAIRPORT.NS", "JPPOWER.NS", "RPOWER.NS", "TRIDENT.NS", "JSWENERGY.NS",
]

# User's broker supports fractional US shares, but they still want the
# universe kept affordable per-share for consistency -- liquid names
# mostly under ~$60-70.
US_UNIVERSE = [
    "F", "GM", "INTC", "T", "VZ", "CSCO", "BAC", "WFC", "PFE", "KO",
    "SOFI", "PLTR", "RIVN", "NIO", "SNAP", "PINS", "LYFT", "RIOT",
    "MARA", "AAL", "CCL", "GOLD", "NCLH", "WBD", "CLF", "OXY", "KMI",
    "NEM", "HBAN", "KEY", "RF", "SIRI", "DKNG", "HOOD", "UBER", "PYPL",
    "NKE", "C", "DAL", "MO",
]


def rank(symbols):
    ranked = []
    for symbol in symbols:
        try:
            bars = monitor.fetch_yahoo(symbol, limit=5)
        except Exception as e:
            print(f"{symbol}: fetch failed ({e}), skipping")
            continue
        if len(bars) < 2:
            print(f"{symbol}: not enough bars (market likely closed), skipping")
            continue
        day_open = bars[0]["open"]
        last = bars[-1]["close"]
        if not day_open:
            continue
        pct_move = (last - day_open) / day_open * 100
        ranked.append((symbol, pct_move, bars))
    ranked.sort(key=lambda x: abs(x[1]), reverse=True)
    return ranked[:TOP_N]


def main():
    market = sys.argv[1] if len(sys.argv) > 1 else None
    if market not in ("india", "us"):
        print("Usage: rank_movers.py [india|us]")
        return 1

    universe = INDIA_UNIVERSE if market == "india" else US_UNIVERSE
    tradable = market == "us"
    top = rank(universe)

    if len(top) < MIN_VALID_RESULTS:
        print(f"{market}: only {len(top)} valid results, leaving existing watchlist untouched")
        return 0

    state = monitor.load_state()
    symbols_state = state.setdefault("symbols", {})
    active_key = f"active_{market}_symbols"
    state[active_key] = [s for s, _, _ in top]

    lines = [f"{market.upper()} -- today's watchlist (top {len(top)} opening-range movers):\n"]
    for symbol, pct, bars in top:
        recent_high = max(b["high"] for b in bars)
        recent_low = min(b["low"] for b in bars)
        symbols_state[symbol] = {
            "status": "watching", "range_high": recent_high, "range_low": recent_low,
            "direction": None, "entry_price": None, "stop_loss": None,
            "extreme_since_entry": None, "consecutive_losses": 0, "last_alert": {},
            "trade_journal": [],
        }
        lines.append(f"{symbol}: {pct:+.2f}%")
    if not tradable:
        lines.append("\n(Analysis only -- not paper-tradable on TradingView, use your own broker if acting on any of these.)")

    monitor.send_telegram("\n".join(lines))
    monitor.save_state(state)
    return 0


if __name__ == "__main__":
    sys.exit(main())
