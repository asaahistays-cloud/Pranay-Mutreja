#!/usr/bin/env python3
"""One-off remediation: places real broker paper orders for setup_log
entries that already fired and surfaced (a real alert went out) but
never got broker-executed -- e.g. a broker was briefly disabled/paused
when the setup fired, or an earlier bug (see git history) silently
skipped automation for entries that should have gotten it.

Only touches entries that are: unresolved, surfaced, in a market that
currently has an enabled broker wired in monitor.BROKERS, and missing
a broker_order_id already -- never re-executes something that already
went through, and never touches a market with no broker (currently
all of them -- see BROKERS in monitor.py) or non-surfaced setups
(never earned real capital in the first place). Not part of the
regular scan; run manually (workflow_dispatch mode=backfill_broker)
only when needed."""
import sys

import monitor


def market_of(symbol):
    if symbol.endswith(".NS"):
        return "india"
    if "-USD" in symbol:
        return "crypto"
    return "us"


def main():
    if not any(b.enabled() for b in monitor.BROKERS.values()):
        print("No broker keys set, nothing to backfill.")
        return 0

    state = monitor.load_state()
    setup_log = state.get("setup_log", [])
    placed = 0
    for entry in setup_log:
        if entry.get("resolved") or not entry.get("surfaced") or entry.get("broker_order_id"):
            continue
        market = market_of(entry["symbol"])
        broker = monitor.BROKERS.get(market)
        if not broker or not broker.enabled():
            continue
        order = broker.place_bracket_order(
            entry["symbol"], market, entry["direction"], entry["entry"],
            entry["stop"], entry.get("target"), entry["qty"],
        )
        if order is None:
            print(f"{entry['symbol']}: backfill order failed, leaving as alert-only")
            continue
        entry["broker_order_id"] = order["id"]
        entry["broker_stop_order_id"] = order["stop_order_id"]
        entry["broker_take_profit_order_id"] = order["take_profit_order_id"]
        entry["taken"] = True
        placed += 1
        print(f"{entry['symbol']} {entry['type']} {entry['direction']}: placed order {order['id']}")

    monitor.save_state(state)
    print(f"Backfilled {placed} order(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
