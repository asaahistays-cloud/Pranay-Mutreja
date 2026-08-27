#!/usr/bin/env python3
"""Creates a brand-new setup_log entry for a trade the user took on their
own -- one the bot never suggested -- driven by the dashboard's "+ Log
Trade" button (docs/index.html) via the same Cloudflare Worker bridge and
repository_dispatch pattern as apply_taken.py, not run by hand.

Unlike apply_taken.py (which edits an EXISTING entry matched by symbol +
fired_at), there is no existing entry here -- this builds one from
scratch, tagged type="manual" so it stays in its own confidence/report
bucket and is never confused with a bot-fired setup.

The symbol must be one the bot is already actively scanning (crypto
watchlist, or today's active India/US symbols) -- only symbols in that
set get walked by main()'s shadow-resolution loop each scan, so a symbol
outside it would never resolve (no stop/target tracking, stuck open
forever). Rejecting anything else here, loudly, up front, is better than
silently creating a trade that can never close.

Takes a single JSON argument (from the repository_dispatch
client_payload) with: symbol, direction ("long"/"short"), entry, stop,
qty (all required), and optionally target."""
import json
import sys
from datetime import datetime, timezone

import monitor


def main():
    if len(sys.argv) < 2:
        print("Usage: apply_manual_trade.py '<json payload>'")
        return 1
    try:
        payload = json.loads(sys.argv[1])
    except json.JSONDecodeError as e:
        print(f"Invalid JSON payload: {e}")
        return 1

    symbol = payload.get("symbol")
    direction = payload.get("direction")
    entry_price = payload.get("entry")
    stop = payload.get("stop")
    qty = payload.get("qty")
    target = payload.get("target")

    if not symbol or direction not in ("long", "short"):
        print("Payload must include symbol and direction ('long' or 'short')")
        return 1
    for name, val in [("entry", entry_price), ("stop", stop), ("qty", qty)]:
        if not isinstance(val, (int, float)):
            print(f"Payload field '{name}' must be a number, got: {val!r}")
            return 1
    if target is not None and not isinstance(target, (int, float)):
        print(f"Payload field 'target' must be a number if provided, got: {target!r}")
        return 1

    state = monitor.load_state()

    crypto_symbols = {s["symbol"] for s in monitor.CRYPTO_WATCHLIST}
    active_symbols = crypto_symbols | set(state.get("active_india_symbols", [])) | set(state.get("active_us_symbols", []))
    if symbol not in active_symbols:
        print(f"'{symbol}' is not in the bot's active watchlist, so it would never be resolved. "
              f"Active symbols: {sorted(active_symbols)}")
        return 1

    market = monitor.market_of(symbol)
    setup_log = state.setdefault("setup_log", [])
    fired_at_dt = datetime.now(timezone.utc)

    setup_log.append({
        "symbol": symbol, "type": "manual", "direction": direction,
        "entry": entry_price, "stop": stop, "target": target,
        "qty": qty, "fired_at": fired_at_dt.isoformat(),
        "resolved": False, "outcome": None, "surfaced": True, "taken": True,
        "confidence_at_fire": monitor.compute_bucket_confidence(setup_log, market, "manual", direction),
        "fired_hour_utc": fired_at_dt.hour,
        "fired_weekday_utc": fired_at_dt.weekday(),
        "shadow": {
            "direction": direction, "entry_price": entry_price,
            "entry_qty": qty, "stop_loss": stop,
            "extreme_since_entry": entry_price, "peak_profit_per_unit": 0,
            "take_profit_target": target, "consecutive_losses": 0, "consecutive_wins": 0,
            "trade_journal": [],
        },
    })

    monitor.save_state(state)
    print(f"Logged manual trade: {symbol} {direction} entry={entry_price} stop={stop} "
          f"target={target} qty={qty}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
