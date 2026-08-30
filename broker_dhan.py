"""Real (sandbox/mock) order execution via DhanHQ -- India equities
only. Built because both crypto (Bybit blocks US-origin traffic) and
real Indian broker LIVE trading APIs (SEBI mandates static IP
whitelisting for order placement, confirmed directly against Dhan's
own live-order docs) are structurally incompatible with GitHub
Actions' rotating, US-based runner IPs.

Dhan's SANDBOX is the one path that actually works: confirmed directly
(a real walkthrough guide, not just API docs) that static IP
whitelisting is NOT required for sandbox orders specifically -- "As it
is not a live trading, static IP compliance is not required." Sandbox
orders are mock (never routed to the real exchange), reset to a fresh
Rs 10,00,000 daily, and the whole sandbox is free with no KYC and no
existing Dhan account needed (separate signup at developer.dhanhq.co).

HARD INVARIANT: DHAN_BASE_URL is the sandbox endpoint, always. Never
point this at api.dhan.co (live trading) -- there is no live-trading
path anywhere in this bot, on purpose.

Fails open, not closed: every public function catches its own
exceptions and returns None/False on failure rather than raising.
enabled() gates all of it on DHAN_CLIENT_ID/DHAN_ACCESS_TOKEN being
present -- a no-op otherwise.

Two-order pattern (entry + separate stop, like broker_bybit.py's
crypto path) rather than a single bracket call -- Dhan's BO
(productType=BO) bracket order type has its own eligibility/exchange
restrictions that aren't worth depending on when a plain INTRADAY
market entry + a separate STOP_LOSS_MARKET order covers every setup
this bot actually fires (target is None for the trailing-stop-only
strategies that make up almost everything surfaced; a real target, if
present, becomes a third plain LIMIT order on the opposite side).
"""
import csv
import io
import json
import os
import urllib.error
import urllib.request

DHAN_BASE_URL = "https://sandbox.dhan.co"  # SANDBOX ONLY -- do not change.
CLIENT_ID_ENV = "DHAN_CLIENT_ID"
ACCESS_TOKEN_ENV = "DHAN_ACCESS_TOKEN"
SCRIP_MASTER_URL = "https://images.dhan.co/api-data/api-scrip-master-detailed.csv"

_security_id_cache = None  # lazy, populated once per process (module-level, not per-call)


def enabled():
    return bool(os.environ.get(CLIENT_ID_ENV)) and bool(os.environ.get(ACCESS_TOKEN_ENV))


def _headers():
    return {
        "access-token": os.environ[ACCESS_TOKEN_ENV],
        "Content-Type": "application/json",
        "Accept": "application/json",
        # Confirmed directly: a bare Python urllib request (no
        # User-Agent, or the default "Python-urllib/3.x") gets a plain
        # 403 Forbidden HTML page back -- a WAF-level bot-detection
        # block, not a Dhan-application-level error (those come back
        # as JSON). A realistic browser-style User-Agent clears it.
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    }


def _request(method, path, body=None):
    url = f"{DHAN_BASE_URL}{path}"
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(url, data=data, headers=_headers(), method=method)
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            raw = resp.read()
            return json.loads(raw) if raw else {}
    except urllib.error.HTTPError as e:
        print(f"Dhan {method} {path} failed: {e.code} {e.read()}")
        print(f"Dhan response headers: {dict(e.headers)}")
        return None
    except Exception as e:
        print(f"Dhan {method} {path} failed: {e}")
        return None


def tradable_on_dhan(market):
    return market == "india"


def _load_security_ids():
    """Downloads Dhan's real instrument master CSV (NSE cash-equity
    rows only) and caches symbol -> security_id for this process.
    UNDERLYING_SYMBOL (column 7) is the clean bare-ticker match --
    confirmed directly against a real row: RELIANCE.NS's ".NS"-stripped
    symbol 'RELIANCE' matches UNDERLYING_SYMBOL exactly, security_id
    2885. DISPLAY_NAME/SYMBOL_NAME carry extra descriptive text and
    aren't reliable exact-match keys."""
    global _security_id_cache
    if _security_id_cache is not None:
        return _security_id_cache
    try:
        req = urllib.request.Request(SCRIP_MASTER_URL, headers={"User-Agent": "btc-monitor-bot"})
        with urllib.request.urlopen(req, timeout=30) as resp:
            raw = resp.read().decode()
    except Exception as e:
        print(f"Dhan scrip master download failed: {e}")
        _security_id_cache = {}
        return _security_id_cache

    ids = {}
    reader = csv.DictReader(io.StringIO(raw))
    for row in reader:
        if row.get("EXCH_ID") == "NSE" and row.get("SEGMENT") == "E" and row.get("INSTRUMENT_TYPE") == "ES":
            sym = row.get("UNDERLYING_SYMBOL")
            if sym:
                ids[sym] = row.get("SECURITY_ID")
    _security_id_cache = ids
    return ids


def to_security_id(symbol):
    """symbol is the bot's watchlist form, e.g. 'RELIANCE.NS'."""
    bare = symbol[:-3] if symbol.endswith(".NS") else symbol
    return _load_security_ids().get(bare)


def _qty_for_order(qty):
    """NSE equities trade in whole shares only."""
    whole = int(qty)
    return whole if whole >= 1 else None


def place_bracket_order(symbol, market, direction, entry, stop, target, qty):
    """Places a real (sandbox) market-entry INTRADAY order protected by
    a separate STOP_LOSS_MARKET order (and a LIMIT order on the
    opposite side if target is given). Returns {"id": entry_order_id,
    "stop_order_id": ... or None, "take_profit_order_id": ... or None}
    on success, or None if disabled/failed -- callers must treat None
    as "not automated this time, alert-only," never as a reason to
    abort the scan."""
    if not enabled() or not tradable_on_dhan(market):
        return None
    order_qty = _qty_for_order(qty)
    if not order_qty:
        print(f"{symbol}: qty {qty} rounds to 0 shares, skipping broker order")
        return None
    security_id = to_security_id(symbol)
    if not security_id:
        print(f"{symbol}: no Dhan security_id found (not an NSE cash-equity symbol?), skipping broker order")
        return None

    client_id = os.environ[CLIENT_ID_ENV]
    side = "BUY" if direction == "long" else "SELL"
    exit_side = "SELL" if direction == "long" else "BUY"

    entry_body = {
        "dhanClientId": client_id, "transactionType": side, "exchangeSegment": "NSE_EQ",
        "productType": "INTRADAY", "orderType": "MARKET", "validity": "DAY",
        "securityId": security_id, "quantity": order_qty,
    }
    entry_order = _request("POST", "/v2/orders", entry_body)
    if entry_order is None or not entry_order.get("orderId"):
        print(f"{symbol}: Dhan entry order failed, falling back to alert-only for this setup")
        return None
    entry_order_id = entry_order["orderId"]

    stop_price_f = float(f"{stop:.6g}")
    stop_body = {
        "dhanClientId": client_id, "transactionType": exit_side, "exchangeSegment": "NSE_EQ",
        "productType": "INTRADAY", "orderType": "STOP_LOSS_MARKET", "validity": "DAY",
        "securityId": security_id, "quantity": order_qty,
        "triggerPrice": f"{stop_price_f:.6g}", "price": f"{stop_price_f:.6g}",
    }
    stop_order = _request("POST", "/v2/orders", stop_body)
    stop_order_id = stop_order.get("orderId") if stop_order else None
    if not stop_order_id:
        print(f"{symbol}: entry placed (order {entry_order_id}) but the protective "
              f"stop order FAILED -- position is real but unprotected, check Dhan manually.")

    tp_order_id = None
    if target is not None:
        target_price_f = float(f"{target:.6g}")
        tp_body = {
            "dhanClientId": client_id, "transactionType": exit_side, "exchangeSegment": "NSE_EQ",
            "productType": "INTRADAY", "orderType": "LIMIT", "validity": "DAY",
            "securityId": security_id, "quantity": order_qty, "price": f"{target_price_f:.6g}",
        }
        tp_order = _request("POST", "/v2/orders", tp_body)
        tp_order_id = tp_order.get("orderId") if tp_order else None

    return {"id": entry_order_id, "stop_order_id": stop_order_id, "take_profit_order_id": tp_order_id}


def replace_stop_price(order_id, new_stop_price):
    """Moves a resting STOP_LOSS_MARKET order to a new (tighter)
    trigger price -- how the bot's existing trailing-stop logic
    (check_open()'s candidate_stop math, unchanged) gets enforced on
    the real sandbox account instead of just being texted to the
    user."""
    if not enabled() or not order_id:
        return None
    client_id = os.environ[CLIENT_ID_ENV]
    price_f = float(f"{new_stop_price:.6g}")
    body = {
        "dhanClientId": client_id, "orderId": order_id,
        "orderType": "STOP_LOSS_MARKET", "validity": "DAY",
        "triggerPrice": f"{price_f:.6g}", "price": f"{price_f:.6g}",
    }
    result = _request("PUT", f"/v2/orders/{order_id}", body)
    # Modification is in-place (same order id), unlike Alpaca's
    # cancel+replace -- but callers (sync_broker_entry) expect an
    # "id" key back either way.
    return {"id": order_id} if result is not None else None


def get_order(order_id):
    if not enabled() or not order_id:
        return None
    return _request("GET", f"/v2/orders/{order_id}")


def order_fill_status(order_id):
    """Polls one specific order id directly for its own fill status.
    Returns the real averageTradedPrice if filled (orderStatus ==
    'TRADED'), else None. Ground truth for resolving an automated
    position -- real (mock) exchange fill data, not the bot's own
    15m-bar close simulation."""
    order = get_order(order_id)
    if order and order.get("orderStatus") == "TRADED" and order.get("averageTradedPrice"):
        return float(order["averageTradedPrice"])
    return None


def cancel_order(order_id):
    if not enabled() or not order_id:
        return None
    return _request("DELETE", f"/v2/orders/{order_id}")
