#!/usr/bin/env python3
"""One-off manual verification: places a single small real Dhan
sandbox order (RELIANCE.NS long, tiny size) directly through
broker_dhan.place_bracket_order() to confirm auth, security_id lookup,
and order creation actually work against the live sandbox API -- not
just mocked unit tests. Prints the full result. Not part of regular
operation; run manually only (workflow_dispatch mode=test_dhan)."""
import sys

import broker_dhan


def main():
    if not broker_dhan.enabled():
        print("DHAN keys not set.")
        return 1

    print("--- read-only GET check first (narrows down whether it's a blanket origin block) ---")
    orders_list = broker_dhan._request("GET", "/v2/orders")
    print("GET /v2/orders result:", orders_list)
    print("--- now the real POST order placement ---")

    result = broker_dhan.place_bracket_order(
        "RELIANCE.NS", "india", "long", entry=None, stop=1200, target=None, qty=1,
    )
    print("place_bracket_order result:", result)
    if result is None:
        return 1

    order = broker_dhan.get_order(result["id"])
    print("entry order status:", order)
    return 0


if __name__ == "__main__":
    sys.exit(main())
