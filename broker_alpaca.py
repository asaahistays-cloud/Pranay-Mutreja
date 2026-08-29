"""Real (paper) order execution via Alpaca -- US stocks only.

Crypto used to route through here too, but Alpaca's crypto account is
cash/spot only: no shorting at all (confirmed directly: 403
"insufficient balance for ETH ... available: 0" trying to sell coin it
doesn't hold), no leverage, a handful of watchlist coins not even
listed (NEAR), and no oto/oco order classes for crypto specifically.
That's a real capability gap, not a bug to route around -- crypto now
goes through broker_bybit.py instead (real long+short futures, real
leverage). Alpaca stays for US equities, which have none of these
restrictions.

HARD INVARIANT: ALPACA_BASE_URL is the paper endpoint, always. Never
point this at api.alpaca.markets (live trading) -- there is no
live-trading path anywhere in this bot, on purpose. India and
commodities are NOT wired to this module at all (Alpaca doesn't offer
India equities, and the commodities feature trades GC=F/NG=F futures
directly, which Alpaca doesn't support) -- those two markets stay
alert-only, unchanged.

Fails open, not closed: every public function catches its own exceptions
and returns None on failure (auth missing, network error, Alpaca-side
rejection) rather than raising -- a broker hiccup must never take down the
real scan (same continue-on-error philosophy as every auxiliary step in
the workflow). enabled() gates all of it on ALPACA_API_KEY/
ALPACA_SECRET_KEY being present at all -- until the user adds those two
GitHub secrets themselves, this module is a complete no-op and the bot
behaves exactly as it did before (alert + manual mark_taken).
"""
import json
import os
import urllib.error
import urllib.request

ALPACA_BASE_URL = "https://paper-api.alpaca.markets"  # PAPER ONLY -- do not change.
API_KEY_ENV = "ALPACA_API_KEY"
SECRET_KEY_ENV = "ALPACA_SECRET_KEY"


def enabled():
    return bool(os.environ.get(API_KEY_ENV)) and bool(os.environ.get(SECRET_KEY_ENV))


def _headers():
    return {
        "APCA-API-KEY-ID": os.environ[API_KEY_ENV],
        "APCA-API-SECRET-KEY": os.environ[SECRET_KEY_ENV],
        "Content-Type": "application/json",
    }


def _request(method, path, body=None):
    url = f"{ALPACA_BASE_URL}{path}"
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(url, data=data, headers=_headers(), method=method)
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            raw = resp.read()
            return json.loads(raw) if raw else {}
    except urllib.error.HTTPError as e:
        print(f"Alpaca {method} {path} failed: {e.code} {e.read()}")
        return None
    except Exception as e:
        print(f"Alpaca {method} {path} failed: {e}")
        return None


def tradable_on_alpaca(market):
    return market == "us"


def _qty_for_order(qty):
    """Alpaca bracket/OTO orders on US equities require whole shares --
    fractional shares can't carry attached stop/take-profit legs. Round
    down (never up -- never risk more size than position_size()
    actually approved) and refuse an order that would round to 0
    shares."""
    whole = float(int(qty))
    return whole if whole >= 1 else None


def place_bracket_order(symbol, market, direction, entry, stop, target, qty):
    """Places a real (paper) market-entry US equity order protected by
    a resting stop-loss, sized at qty. Returns {"id": entry_order_id,
    "stop_order_id": ... or None, "take_profit_order_id": ... or None}
    on success, or None if disabled/failed -- callers must treat None
    as "not automated this time, alert-only," never as a reason to
    abort the scan.

    target is None for most of this bot's setups (Triple MA, Triple
    Threat, DMI+DPO -- deliberately "trail your stop, no fixed target,"
    see check_open()'s docstring): order_class="oto" (stop leg only).
    order_class="bracket" (both legs) when a real target exists (the
    older range-rejection setups)."""
    if not enabled() or not tradable_on_alpaca(market):
        return None
    order_qty = _qty_for_order(qty)
    if not order_qty:
        print(f"{symbol}: qty {qty} rounds to 0 shares, skipping broker order")
        return None

    side = "buy" if direction == "long" else "sell"
    body = {
        "symbol": symbol, "qty": str(order_qty), "side": side,
        "type": "market", "time_in_force": "gtc",
        "order_class": "bracket" if target is not None else "oto",
        "stop_loss": {"stop_price": f"{stop:.6g}"},
    }
    if target is not None:
        body["take_profit"] = {"limit_price": f"{target:.6g}"}
    result = _request("POST", "/v2/orders", body)
    if result is None:
        print(f"{symbol}: Alpaca order failed, falling back to alert-only for this setup")
        return None
    stop_id, tp_id = extract_leg_ids(result)
    return {"id": result["id"], "stop_order_id": stop_id, "take_profit_order_id": tp_id}


def replace_stop_price(stop_order_id, new_stop_price):
    """Moves a resting stop-loss leg to a new (tighter) price -- how the
    bot's existing trailing-stop logic (check_open()'s candidate_stop
    math, unchanged) gets enforced on the real paper account instead of
    just being texted to the user."""
    if not enabled() or not stop_order_id:
        return None
    return _request("PATCH", f"/v2/orders/{stop_order_id}", {"stop_price": f"{new_stop_price:.6g}"})


def get_order(order_id):
    if not enabled() or not order_id:
        return None
    return _request("GET", f"/v2/orders/{order_id}")


def extract_leg_ids(order):
    """Pulls the stop_loss/take_profit child-order ids out of a bracket
    order's 'legs' array. Alpaca doesn't tag legs with an explicit
    "this is the stop leg" field -- distinguish by which price field is
    populated (the stop leg carries stop_price, the take-profit leg
    carries limit_price and no stop_price). Legs can be briefly absent
    right after submission before the parent order transitions out of
    'accepted' -- callers must treat (None, None) as "not ready yet, try
    again next scan," not as a failure."""
    if not order:
        return None, None
    stop_id = tp_id = None
    for leg in order.get("legs") or []:
        if leg.get("stop_price"):
            stop_id = leg.get("id")
        elif leg.get("limit_price"):
            tp_id = leg.get("id")
    return stop_id, tp_id


def order_fill_status(order_id):
    """Polls one specific order id directly for its own fill status.
    Returns the real filled_avg_price if filled, else None. Ground
    truth for resolving an automated position -- real exchange fill
    data, not the bot's own 15m-bar close simulation."""
    order = get_order(order_id)
    if order and order.get("status") == "filled" and order.get("filled_avg_price"):
        return float(order["filled_avg_price"])
    return None


def cancel_order(order_id):
    if not enabled() or not order_id:
        return None
    return _request("DELETE", f"/v2/orders/{order_id}")
