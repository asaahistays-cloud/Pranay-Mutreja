#!/usr/bin/env python3
"""Manually closes an open setup_log entry -- driven by the dashboard's
"Closed" button (docs/index.html) via the same Cloudflare Worker bridge
and repository_dispatch pattern as apply_taken.py / apply_manual_trade.py,
not run by hand.

The bot's own shadow-tracking already resolves an entry automatically
once real price hits the stop or take-profit target (see check_open() in
monitor.py, run every scan). This script exists for the gap that leaves
open: a position the user exits themselves, at a price that never
actually touched either line -- without this, that entry would sit in
"Open Positions" forever, since nothing else would ever mark it
resolved.

Matches a setup_log entry precisely by symbol + fired_at, same reasoning
as apply_taken.py (the dashboard button is tied to one specific row, and
a newer setup for the same symbol may exist by the time this runs).

Takes a single JSON argument (from the repository_dispatch
client_payload) with: symbol, fired_at (exact match), exit (required).
pnl is computed the same way log_trade() computes it in monitor.py, so
this entry reads identically to an automatically-resolved one everywhere
(dashboard stats, report.py)."""
import json
import sys
from datetime import datetime, timezone


def main():
    if len(sys.argv) < 2:
        print("Usage: apply_close_trade.py '<json payload>'")
        return 1
    try:
        payload = json.loads(sys.argv[1])
    except json.JSONDecodeError as e:
        print(f"Invalid JSON payload: {e}")
        return 1

    symbol = payload.get("symbol")
    fired_at = payload.get("fired_at")
    exit_price = payload.get("exit")
    if not symbol or not fired_at:
        print("Payload must include symbol and fired_at")
        return 1
    if not isinstance(exit_price, (int, float)):
        print(f"Payload field 'exit' must be a number, got: {exit_price!r}")
        return 1

    import monitor
    state = monitor.load_state()
    log = state.get("setup_log", [])
    matches = [e for e in log if e["symbol"] == symbol and e["fired_at"] == fired_at]
    if not matches:
        print(f"No setup_log entry found for {symbol} fired_at={fired_at}")
        return 1
    entry = matches[0]

    if entry["resolved"]:
        print(f"{symbol} fired_at={fired_at} is already resolved, not closing again")
        return 1

    shadow = entry["shadow"]
    direction = shadow["direction"]
    entry_price = shadow["entry_price"]
    qty = shadow.get("entry_qty")

    pnl_per_unit = (exit_price - entry_price) if direction == "long" else (entry_price - exit_price)
    outcome = {
        "direction": direction, "entry": entry_price, "exit": exit_price,
        "qty": qty, "pnl_per_unit": pnl_per_unit,
        "pnl_total": pnl_per_unit * qty if qty else None,
        "exit_reason": "manual_close",
        "closed_at": datetime.now(timezone.utc).isoformat(),
    }

    entry["resolved"] = True
    entry["outcome"] = outcome

    monitor.save_state(state)
    print(f"Closed: {entry['symbol']} {entry['type']} ({direction}) fired {entry['fired_at']} "
          f"entry={entry_price} exit={exit_price} pnl_per_unit={pnl_per_unit:.4g} "
          f"pnl_total={outcome['pnl_total']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
