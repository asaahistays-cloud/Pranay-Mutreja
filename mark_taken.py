#!/usr/bin/env python3
"""Flags the most recent unresolved fired setup for a symbol as
"taken" -- from the next scan onward, check_open() sends real exit
alerts (trail-stop, profit-lock, target hit, stop hit) for that setup
instead of shadow-tracking it silently, since it's now a real position.

Not wired to a Telegram command (that was deliberately ripped out
earlier -- "leave it then, i don't want more bugs"). Run manually,
then commit + push state.json so the next scan picks up the flag.
"""
import sys

import monitor


def main():
    if len(sys.argv) < 2:
        print("Usage: mark_taken.py <symbol> [actual_qty]")
        return 1
    symbol = sys.argv[1]
    qty_override = float(sys.argv[2]) if len(sys.argv) > 2 else None

    state = monitor.load_state()
    log = state.get("setup_log", [])
    candidates = [e for e in log if e["symbol"] == symbol and not e["resolved"]]
    if not candidates:
        print(f"No unresolved fired setup found for {symbol}")
        return 1
    entry = max(candidates, key=lambda e: e["fired_at"])
    entry["taken"] = True
    if qty_override is not None:
        entry["qty"] = qty_override
        entry["shadow"]["entry_qty"] = qty_override

    monitor.save_state(state)
    print(f"Marked taken: {entry['symbol']} {entry['type']} ({entry['direction']}) "
          f"fired {entry['fired_at']} entry={entry['entry']} stop={entry['stop']} qty={entry['qty']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
