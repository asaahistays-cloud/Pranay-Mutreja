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
    stop-loss, sized at qty. Returns the parsed Alpaca order dict (with
    nested legs, each carrying its own 'id') on success, or None if
    disabled/failed -- callers must treat None as "not automated this
    time, alert-only," never as a reason to abort the scan.

    target is None for most of this bot's setups (Triple MA, Triple
    Threat, DMI+DPO -- deliberately "trail your stop, no fixed target,"
    see check_open()'s docstring) -- confirmed directly: gating this on
    target is not None meant broker execution silently never fired for
    any of the 3 setups actually surfaced during real testing, only for
    the older range-rejection setups that do carry a real target. So:
    order_class="oto" (stop_loss leg only) when target is None -- the
    position then lives purely on the trailing stop that
    sync_broker_entry() keeps replacing via check_open()'s existing
    trailing math, exactly matching how these setups already behave in
    the alert-only/manual flow. order_class="bracket" (both legs) only
    when a real target exists.
    """
    if not enabled() or not tradable_on_alpaca(market):
        return None
    order_qty = _qty_for_order(qty, market)
    if not order_qty or order_qty <= 0:
        print(f"{symbol}: qty {qty} rounds to 0 for {market}, skipping broker order")
        return None

    side = "buy" if direction == "long" else "sell"
    body = {
        "symbol": to_alpaca_symbol(symbol, market),
        "qty": str(order_qty),
        "side": side,
        "type": "market",
        "time_in_force": "gtc",
        "stop_loss": {"stop_price": f"{stop:.6g}"},
    }
    if target is not None:
        body["order_class"] = "bracket"
        body["take_profit"] = {"limit_price": f"{target:.6g}"}
    else:
        body["order_class"] = "oto"
    result = _request("POST", "/v2/orders", body)
    if result is None:
        print(f"{symbol}: Alpaca order failed, falling back to alert-only for this setup")
    return result


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


def leg_fill_outcome(order):
    """Given a re-fetched parent bracket order, returns ('stop'|'target',
    filled_avg_price) if either leg has filled, else None. Used as the
    ground-truth resolution source for an automated position -- real
    exchange fill data, not the bot's own 15m-bar close simulation."""
    if not order:
        return None
    for leg in order.get("legs") or []:
        if leg.get("status") == "filled" and leg.get("filled_avg_price"):
            kind = "stop" if leg.get("stop_price") else "target"
            return kind, float(leg["filled_avg_price"])
    return None


def cancel_order(order_id):
    if not enabled() or not order_id:
        return None
    return _request("DELETE", f"/v2/orders/{order_id}")
