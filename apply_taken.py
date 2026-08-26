#!/usr/bin/env python3
"""Like mark_taken.py, but matches a setup_log entry precisely by
symbol + fired_at instead of "most recent unresolved for this symbol"
-- driven by the dashboard's "Taken" button (docs/index.html) via a
Cloudflare Worker bridge and a repository_dispatch-triggered GitHub
Actions workflow (.github/workflows/mark_taken.yml), not run by hand.
Precise matching matters here since the dashboard button is tied to
one specific row, and by the time this runs a newer setup for the
same symbol may already exist.

Takes a single JSON argument (from the repository_dispatch
client_payload) with: symbol, fired_at (exact match), and optionally
entry, qty, stop, target -- any of those present override the bot's
suggested values, same correction pattern used by hand all night
(logged entry vs. actual fill price/qty/stop can differ)."""
import json
import sys

import monitor


def main():
    if len(sys.argv) < 2:
        print("Usage: apply_taken.py '<json payload>'")
        return 1
    try:
        payload = json.loads(sys.argv[1])
    except json.JSONDecodeError as e:
        print(f"Invalid JSON payload: {e}")
        return 1

    symbol = payload.get("symbol")
    fired_at = payload.get("fired_at")
    if not symbol or not fired_at:
        print("Payload must include symbol and fired_at")
        return 1

    state = monitor.load_state()
    log = state.get("setup_log", [])
    matches = [e for e in log if e["symbol"] == symbol and e["fired_at"] == fired_at]
    if not matches:
        print(f"No setup_log entry found for {symbol} fired_at={fired_at}")
        return 1
    entry = matches[0]

    if entry["resolved"]:
        print(f"{symbol} fired_at={fired_at} is already resolved, not marking taken")
        return 1

    entry["taken"] = True

    for field, shadow_field in [("entry", "entry_price"), ("stop", "stop_loss"), ("target", "take_profit_target")]:
        val = payload.get(field)
        if val is not None:
            entry[field] = val
            entry["shadow"][shadow_field] = val
    qty = payload.get("qty")
    if qty is not None:
        entry["qty"] = qty
        entry["shadow"]["entry_qty"] = qty

    # If entry price was corrected, extreme_since_entry (the trail's
    # anchor) should reset to it too -- otherwise a stale bot-suggested
    # extreme can imply profit/loss that never actually happened at the
    # real fill price. Same fix applied by hand earlier tonight.
    if payload.get("entry") is not None:
        entry["shadow"]["extreme_since_entry"] = payload["entry"]

    monitor.save_state(state)
    print(f"Marked taken: {entry['symbol']} {entry['type']} ({entry['direction']}) "
          f"fired {entry['fired_at']} entry={entry['entry']} stop={entry['stop']} qty={entry['qty']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
