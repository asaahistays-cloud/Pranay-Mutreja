#!/usr/bin/env python3
"""One-off manual verification: places a single small real Bybit
testnet order (BTC-USD long, tiny size) directly through
broker_bybit.place_bracket_order() to confirm auth/signing, symbol
mapping, leverage-setting, and order creation all actually work
against the live API -- not just mocked unit tests. Prints the full
result. Not part of regular operation; run manually only
(workflow_dispatch mode=test_bybit)."""
import sys

import broker_bybit


def main():
    if not broker_bybit.enabled():
        print("BYBIT keys not set.")
        return 1

    # Tiny size, wide-ish stop (real BTC price context) -- this is a
    # real testnet order, harmless (fake funds), but still real enough
    # to prove the whole path works.
    result = broker_bybit.place_bracket_order(
        "BTC-USD", "crypto", "long", entry=None, stop=70000, target=None, qty=0.001,
    )
    print("place_bracket_order result:", result)
    if result is None:
        return 1

    status = broker_bybit._request("GET", "/v5/position/list", {"category": "linear", "symbol": "BTCUSDT"})
    print("position status:", status)
    return 0


if __name__ == "__main__":
    sys.exit(main())
