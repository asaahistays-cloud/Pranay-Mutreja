"""Real (paper) order execution via Alpaca -- crypto + US stocks only.

HARD INVARIANT: ALPACA_BASE_URL is the paper endpoint, always. Never point
this at api.alpaca.markets (live trading) -- there is no live-trading path
anywhere in this bot, on purpose. India and commodities are NOT wired to
this module at all (Alpaca doesn't offer India equities, and the
commodities feature trades GC=F/NG=F futures directly, which Alpaca
doesn't support) -- those two markets stay alert-only, unchanged.

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
# Crypto's standalone protective order must be stop_limit (plain "stop"
# is rejected outright, see place_bracket_order()) -- this is how far
# past the stop trigger the limit is allowed to fill, so a fast drop
# doesn't leave the order resting unfilled past its trigger price.
STOP_LIMIT_SLIPPAGE_PCT = 0.005


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


def to_alpaca_symbol(symbol, market):
    """Crypto watchlist symbols are 'BTC-USD' style; Alpaca crypto pairs
    use a slash ('BTC/USD'). US tickers are already Alpaca-compatible."""
    if market == "crypto":
        return symbol.replace("-", "/")
    return symbol


def tradable_on_alpaca(market):
    return market in ("crypto", "us")


def _qty_for_order(qty, market):
    """Alpaca bracket/OCO orders on US equities require whole shares --
    fractional shares can't carry attached stop/take-profit legs. Crypto
    bracket orders do support fractional quantities. Round down (never
    up -- never risk more size than position_size() actually approved)
    and refuse to place a US order that would round to 0 shares."""
    if market == "us":
        whole = float(int(qty))
        return whole if whole >= 1 else None
    return qty


def place_bracket_order(symbol, market, direction, entry, stop, target, qty):
    """Places a real (paper) market-entry order protected by a resting
    stop-loss, sized at qty. Returns {"id": entry_order_id,
    "stop_order_id": ... or None, "take_profit_order_id": ... or None}
    on success, or None if disabled/failed -- callers must treat None
    as "not automated this time, alert-only," never as a reason to
    abort the scan.

    target is None for most of this bot's setups (Triple MA, Triple
    Threat, DMI+DPO -- deliberately "trail your stop, no fixed target,"
    see check_open()'s docstring) -- confirmed directly: gating this on
    target is not None meant broker execution silently never fired for
    any of the 3 setups actually surfaced during real testing, only for
    the older range-rejection setups that do carry a real target.

    order_class="bracket" (both legs) when a real target exists -- this
    works for both crypto and equities. When target is None, equities
    use order_class="oto" (stop leg only). Crypto CANNOT use oto/oco at
    all -- confirmed directly against the real API: 422 "crypto orders
    not allowed for advanced order_class: oto". So for crypto with no
    target, this places two independent top-level orders instead: a
    plain market entry, then a separate standalone stop order. There's
    no parent/leg relationship between them, but replace_stop_price()
    and order_fill_status() both operate on a plain order id either
    way, so the rest of the pipeline (trailing-stop enforcement,
    fill-based resolution) doesn't need to know which shape it got.
    """
    if not enabled() or not tradable_on_alpaca(market):
        return None
    order_qty = _qty_for_order(qty, market)
    if not order_qty or order_qty <= 0:
        print(f"{symbol}: qty {qty} rounds to 0 for {market}, skipping broker order")
        return None

    side = "buy" if direction == "long" else "sell"
    alpaca_symbol = to_alpaca_symbol(symbol, market)

    if target is not None:
        body = {
            "symbol": alpaca_symbol, "qty": str(order_qty), "side": side,
            "type": "market", "time_in_force": "gtc", "order_class": "bracket",
            "take_profit": {"limit_price": f"{target:.6g}"},
            "stop_loss": {"stop_price": f"{stop:.6g}"},
        }
        result = _request("POST", "/v2/orders", body)
        if result is None:
            print(f"{symbol}: Alpaca bracket order failed, falling back to alert-only for this setup")
            return None
        stop_id, tp_id = extract_leg_ids(result)
        return {"id": result["id"], "stop_order_id": stop_id, "take_profit_order_id": tp_id}

    if market == "crypto":
        if direction == "short":
            # Alpaca's crypto account is cash/spot only -- no margin, no
            # shorting. Confirmed directly: a short attempt 403'd with
            # "insufficient balance for ETH ... available: 0" (it was
            # trying to sell coin it doesn't hold). Fail closed here
            # rather than let every crypto short setup hit that error
            # every single scan -- alert-only is the correct behavior
            # for these, not a bug to route around.
            print(f"{symbol}: crypto shorts aren't supported on Alpaca's cash account, alert-only")
            return None
        entry_body = {
            "symbol": alpaca_symbol, "qty": str(order_qty), "side": side,
            "type": "market", "time_in_force": "gtc",
        }
        entry_order = _request("POST", "/v2/orders", entry_body)
        if entry_order is None:
            print(f"{symbol}: Alpaca crypto entry order failed, falling back to alert-only for this setup")
            return None
        # Crypto rejects plain type="stop" outright (confirmed directly:
        # 422 "invalid order type for crypto order") -- only stop_limit
        # is supported. limit_price sits a small buffer past stop_price
        # (in the direction that still lets it fill) so a fast-moving
        # market doesn't leave the order resting unfilled past its
        # trigger -- crypto shorts are excluded above, so this is
        # always a "sell to close a long" stop.
        stop_price_f = float(f"{stop:.6g}")
        limit_price_f = stop_price_f * (1 - STOP_LIMIT_SLIPPAGE_PCT)
        stop_body = {
            "symbol": alpaca_symbol, "qty": str(order_qty), "side": "sell",
            "type": "stop_limit", "stop_price": f"{stop_price_f:.6g}",
            "limit_price": f"{limit_price_f:.6g}", "time_in_force": "gtc",
        }
        stop_order = _request("POST", "/v2/orders", stop_body)
        if stop_order is None:
            print(f"{symbol}: entry placed (order {entry_order['id']}) but the protective "
                  f"stop order FAILED -- position is real but unprotected, check Alpaca manually.")
            return {"id": entry_order["id"], "stop_order_id": None, "take_profit_order_id": None}
        return {"id": entry_order["id"], "stop_order_id": stop_order["id"], "take_profit_order_id": None}

    # US equities, no target: OTO (stop leg only) is supported.
    body = {
        "symbol": alpaca_symbol, "qty": str(order_qty), "side": side,
        "type": "market", "time_in_force": "gtc", "order_class": "oto",
        "stop_loss": {"stop_price": f"{stop:.6g}"},
    }
    result = _request("POST", "/v2/orders", body)
    if result is None:
        print(f"{symbol}: Alpaca order failed, falling back to alert-only for this setup")
        return None
    stop_id, _ = extract_leg_ids(result)
    return {"id": result["id"], "stop_order_id": stop_id, "take_profit_order_id": None}


def replace_stop_price(stop_order_id, new_stop_price, market=None):
    """Moves a resting stop order to a new (tighter) price -- how the
    bot's existing trailing-stop logic (check_open()'s candidate_stop
    math, unchanged) gets enforced on the real paper account instead of
    just being texted to the user.

    market="crypto" also updates limit_price alongside stop_price --
    crypto's standalone protective order is stop_limit (see
    place_bracket_order()), and a PATCH that only moves stop_price
    while leaving a now-stale limit_price behind could leave the order
    unable to fill past its new trigger. Every other order shape here
    (bracket/OTO legs on crypto or equities) is a plain stop, where
    limit_price isn't a valid field at all."""
    if not enabled() or not stop_order_id:
        return None
    body = {"stop_price": f"{new_stop_price:.6g}"}
    if market == "crypto":
        body["limit_price"] = f"{new_stop_price * (1 - STOP_LIMIT_SLIPPAGE_PCT):.6g}"
    return _request("PATCH", f"/v2/orders/{stop_order_id}", body)


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
    """Polls one specific order id directly for its own fill status --
    works identically whether that id is a real bracket/OTO leg or one
    of crypto's standalone stop orders (see place_bracket_order()),
    since both are just plain orders from the API's point of view.
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
