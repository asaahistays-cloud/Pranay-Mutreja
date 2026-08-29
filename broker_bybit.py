"""Real (testnet) order execution via Bybit -- crypto only, both long
and short. Built because Alpaca's crypto account is cash/spot only (no
shorting at all, see broker_alpaca.py's module docstring) -- Bybit's
USDT-perpetual futures support real long/short positions with real
leverage, matching how these strategies were actually validated
(LEVERAGE_BY_MARKET["crypto"] = 10).

HARD INVARIANT: BYBIT_BASE_URL is the testnet endpoint, always. Never
point this at api.bybit.com (live trading) -- there is no live-trading
path anywhere in this bot, on purpose.

Structurally different from Alpaca's leg-order model: Bybit attaches
stopLoss/takeProfit directly on the order/position itself (no separate
child order with its own id), and modifying the stop is a position-
level call (POST /v5/position/trading-stop, keyed by symbol) rather
than a PATCH on an order id. So the "stop_order_id" this module hands
back to monitor.py is really just the Bybit-formatted symbol string --
an identifier, not a real order id -- kept under the same field name
as broker_alpaca.py's real leg id so sync_broker_entry() can treat both
brokers uniformly without knowing which one it's talking to.

Resolution works differently too: instead of polling a specific
order's fill status, order_fill_status() here checks whether the
POSITION itself has closed (size back to 0) and reads the real exit
price from closed-pnl history -- there's no reliable separate "which
leg filled" signal to poll otherwise. Kind (stop vs target) isn't
distinguished for Bybit fills; the exit price/pnl themselves are still
100% real, just reported generically.

Fails open, not closed: every public function catches its own
exceptions and returns None/False on failure rather than raising.
enabled() gates all of it on BYBIT_API_KEY/BYBIT_API_SECRET being
present -- a no-op otherwise.

Known rough edge, called out honestly rather than silently: qty is
sent at whatever precision position_size() computed, without checking
Bybit's real per-symbol quantity step size (would need a separate
GET /v5/market/instruments-info lookup per symbol). A precision
mismatch fails the order cleanly (caught, logged, alert-only
fallback) rather than silently misordering -- not a correctness risk,
just a place real orders might bounce that a future pass could tighten.
"""
import hashlib
import hmac
import json
import os
import time
import urllib.error
import urllib.request

BYBIT_BASE_URL = "https://api-testnet.bybit.com"  # TESTNET ONLY -- do not change.
API_KEY_ENV = "BYBIT_API_KEY"
SECRET_KEY_ENV = "BYBIT_API_SECRET"
RECV_WINDOW = "5000"
CATEGORY = "linear"  # USDT-margined perpetuals


def enabled():
    return bool(os.environ.get(API_KEY_ENV)) and bool(os.environ.get(SECRET_KEY_ENV))


def _sign(payload_str, timestamp):
    api_key = os.environ[API_KEY_ENV]
    secret = os.environ[SECRET_KEY_ENV]
    raw = f"{timestamp}{api_key}{RECV_WINDOW}{payload_str}"
    return hmac.new(secret.encode(), raw.encode(), hashlib.sha256).hexdigest()


def _request(method, path, params=None):
    timestamp = str(int(time.time() * 1000))
    if method == "GET":
        query = "&".join(f"{k}={v}" for k, v in (params or {}).items())
        url = f"{BYBIT_BASE_URL}{path}" + (f"?{query}" if query else "")
        sig = _sign(query, timestamp)
        data = None
    else:
        body_str = json.dumps(params or {})
        url = f"{BYBIT_BASE_URL}{path}"
        sig = _sign(body_str, timestamp)
        data = body_str.encode()

    headers = {
        "X-BAPI-API-KEY": os.environ[API_KEY_ENV],
        "X-BAPI-TIMESTAMP": timestamp,
        "X-BAPI-SIGN": sig,
        "X-BAPI-RECV-WINDOW": RECV_WINDOW,
        "Content-Type": "application/json",
    }
    req = urllib.request.Request(url, data=data, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            result = json.loads(resp.read())
    except urllib.error.HTTPError as e:
        print(f"Bybit {method} {path} failed: {e.code} {e.read()}")
        return None
    except Exception as e:
        print(f"Bybit {method} {path} failed: {e}")
        return None

    if result.get("retCode") != 0:
        print(f"Bybit {method} {path} failed: {result.get('retCode')} {result.get('retMsg')}")
        return None
    return result.get("result")


def to_bybit_symbol(symbol):
    """Crypto watchlist symbols are 'BTC-USD' style; Bybit USDT-perp
    symbols are 'BTCUSDT' (no separator, USDT not USD)."""
    return symbol.replace("-USD", "USDT")


def tradable_on_bybit(market):
    return market == "crypto"


def set_leverage(symbol, leverage):
    """Idempotent -- Bybit returns retCode 110043 ("leverage not
    modified") if it's already set to this value, which _request()
    would otherwise log as a failure on every single scan for a
    symbol whose leverage was already set correctly. Treated as
    success, not an error."""
    bybit_symbol = to_bybit_symbol(symbol)
    timestamp = str(int(time.time() * 1000))
    body = {
        "category": CATEGORY, "symbol": bybit_symbol,
        "buyLeverage": str(leverage), "sellLeverage": str(leverage),
    }
    body_str = json.dumps(body)
    sig = _sign(body_str, timestamp)
    headers = {
        "X-BAPI-API-KEY": os.environ[API_KEY_ENV], "X-BAPI-TIMESTAMP": timestamp,
        "X-BAPI-SIGN": sig, "X-BAPI-RECV-WINDOW": RECV_WINDOW, "Content-Type": "application/json",
    }
    req = urllib.request.Request(f"{BYBIT_BASE_URL}/v5/position/set-leverage",
                                  data=body_str.encode(), headers=headers, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            result = json.loads(resp.read())
    except Exception as e:
        print(f"Bybit set_leverage({symbol}) failed: {e}")
        return False
    if result.get("retCode") not in (0, 110043):
        print(f"Bybit set_leverage({symbol}) failed: {result.get('retCode')} {result.get('retMsg')}")
        return False
    return True


def place_bracket_order(symbol, market, direction, entry, stop, target, qty):
    """Places a real (testnet) market-entry Bybit position with
    stopLoss/takeProfit attached directly on the order -- both long and
    short work identically here, unlike Alpaca's crypto cash account.
    Returns {"id": order_id, "stop_order_id": bybit_symbol,
    "take_profit_order_id": None} on success (stop_order_id is really
    the symbol, used by replace_stop_price()/order_fill_status() to
    address the position -- see module docstring), or None if
    disabled/failed."""
    if not enabled() or not tradable_on_bybit(market):
        return None
    if qty <= 0:
        print(f"{symbol}: qty {qty} <= 0, skipping broker order")
        return None

    bybit_symbol = to_bybit_symbol(symbol)
    leverage = 10  # matches LEVERAGE_BY_MARKET["crypto"] in monitor.py
    set_leverage(bybit_symbol, leverage)

    side = "Buy" if direction == "long" else "Sell"
    body = {
        "category": CATEGORY, "symbol": bybit_symbol, "side": side,
        "orderType": "Market", "qty": f"{qty:.6g}",
        "stopLoss": f"{stop:.6g}", "tpslMode": "Full", "slOrderType": "Market",
    }
    if target is not None:
        body["takeProfit"] = f"{target:.6g}"
        body["tpOrderType"] = "Market"

    result = _request("POST", "/v5/order/create", body)
    if result is None:
        print(f"{symbol}: Bybit order failed, falling back to alert-only for this setup")
        return None
    return {"id": result.get("orderId"), "stop_order_id": bybit_symbol, "take_profit_order_id": None}


def replace_stop_price(identifier, new_stop_price):
    """identifier is the Bybit symbol (see place_bracket_order()) --
    moves the position's stop-loss in place via /v5/position/trading-stop,
    how the bot's existing trailing-stop logic gets enforced on the
    real testnet account."""
    if not enabled() or not identifier:
        return None
    body = {
        "category": CATEGORY, "symbol": identifier,
        "stopLoss": f"{new_stop_price:.6g}", "positionIdx": 0,
    }
    result = _request("POST", "/v5/position/trading-stop", body)
    # No real "new id" to track (unlike Alpaca's cancel+replace) --
    # same identifier (symbol) stays valid for every future call.
    return {"id": identifier} if result is not None else None


def order_fill_status(identifier):
    """identifier is the Bybit symbol. Checks whether the POSITION has
    closed (size back to 0) rather than polling a specific order --
    Bybit's attached TP/SL doesn't expose a reliably pollable child
    order id the way Alpaca's legs do. Returns the real average exit
    price from closed-pnl history if closed, else None."""
    if not enabled() or not identifier:
        return None
    position = _request("GET", "/v5/position/list", {"category": CATEGORY, "symbol": identifier})
    if position is None:
        return None
    positions_list = position.get("list") or []
    still_open = any(float(p.get("size", 0)) > 0 for p in positions_list)
    if still_open:
        return None

    closed = _request("GET", "/v5/position/closed-pnl", {"category": CATEGORY, "symbol": identifier, "limit": 1})
    if not closed or not closed.get("list"):
        return None
    record = closed["list"][0]
    avg_exit = record.get("avgExitPrice")
    return float(avg_exit) if avg_exit else None


def cancel_order(order_id):
    return None  # Not used -- Bybit's SL/TP are position attributes, not cancelable child orders here.
