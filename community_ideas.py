#!/usr/bin/env python3
"""Checks TradingView's public per-symbol "Ideas" pages -- real community
trade-setup posts, not just news -- for the bot's active watchlist.
Confirmed live and free: no auth, no API key, not rate-limited on
repeated requests, real post content (title + body text), not a JS
shell (verified by pulling real post text directly out of a raw
fetch). robots.txt disallows the generic /ideas/ hub but NOT the
per-symbol /symbols/{SYMBOL}/ideas/ path used here.

Explicitly does NOT blindly follow community setups -- an LLM reads
every new idea and judges whether it's a genuine, coherent, ACTIONABLE
trade setup (clear direction, a concrete entry condition already met,
real technical reasoning) versus generic content (motivational posts,
vague commentary, no actual setup, or a setup conditional on something
that hasn't happened yet). The bar is deliberately strict -- most ideas
are expected to fail it.

Explicit design choice (direct feedback after an earlier version just
relayed the raw community post as its own message type): a genuine
match is NOT forwarded as a "here's an idea, you decide" post. Instead
it flows through the bot's own real alert pipeline -- fetches the
symbol's actual current price/ATR, computes a real entry/stop/qty the
same way check_watching_crypto()'s breakout logic does, sends the
EXACT same alert format as any other fired setup, and logs it into
setup_log with type="community_idea" so it's tracked, shadowed, and
contributes to confidence scoring identically to every other setup
type. The only difference from a normal alert is one attribution line
at the end. No historical archive of community ideas exists to
backtest a rule against (same reason Fear & Greed and world news stay
informational-only), so this is real-time judgment applied through the
bot's existing, already-validated sizing/risk machinery -- not a new,
unvalidated decision mechanism of its own.

Dedup by idea URL (each TradingView idea has a unique permalink), same
seen-tracking pattern as news_briefing.py's seen_ids."""
import json
import os
import re
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone
from html import unescape

import monitor

WORKER_URL = "https://multi-market-monitor-taken.asaahistays.workers.dev"
US_EXCHANGES = ["NASDAQ", "NYSE", "AMEX"]


COMMODITY_TV_SYMBOLS = {"GC=F": "COMEX-GC1!", "NG=F": "NYMEX-NG1!"}  # confirmed live directly


def tv_symbol_path(symbol, market):
    """Maps this bot's own symbol format to TradingView's URL scheme.
    Crypto (BTC-USD) -> BTCUSD. India (RECLTD.NS) -> NSE-RECLTD. US
    (AAPL) -> try NASDAQ/NYSE/AMEX in turn since the bot doesn't track
    which exchange each symbol trades on. Commodity futures use their
    continuous-contract symbol (GC1!/NG1!), not the Yahoo GC=F/NG=F
    format the rest of the bot uses internally."""
    if market == "crypto":
        return [symbol.replace("-", "")]
    if market == "india":
        return [f"NSE-{symbol[:-3]}"]
    if market == "commodity":
        return [COMMODITY_TV_SYMBOLS[symbol]] if symbol in COMMODITY_TV_SYMBOLS else []
    return [f"{ex}-{symbol}" for ex in US_EXCHANGES]


def fetch_ideas_page(tv_symbol):
    url = f"https://www.tradingview.com/symbols/{tv_symbol}/ideas/"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (compatible; btc-monitor-bot/1.0)"})
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            if resp.status != 200:
                return None
            return resp.read().decode("utf-8", errors="ignore")
    except urllib.error.HTTPError:
        return None
    except Exception:
        return None


def parse_ideas(html_content, limit=8):
    titles = re.findall(r'data-qa-id="ui-lib-card-link-title"[^>]*>([^<]+)</a>', html_content)
    urls = re.findall(r'<a href="(https://www\.tradingview\.com/chart/[^"]+)" data-qa-id="ui-lib-card-link-title"', html_content)
    bodies = re.findall(r'data-qa-id="ui-lib-card-link-paragraph"[^>]*><span[^>]*><span[^>]*>(.*?)</span>', html_content, re.DOTALL)
    ideas = []
    for t, u, b in zip(titles, urls, bodies):
        body_clean = re.sub(r"<[^>]+>", " ", b)
        body_clean = unescape(re.sub(r"\s+", " ", body_clean)).strip()
        ideas.append({"title": unescape(t).strip(), "url": u, "body": body_clean[:500]})
    return ideas[:limit]


def fetch_symbol_ideas(symbol, market):
    for tv_symbol in tv_symbol_path(symbol, market):
        html_content = fetch_ideas_page(tv_symbol)
        if html_content:
            ideas = parse_ideas(html_content)
            if ideas:
                return ideas
    return []


def build_eval_prompt(symbol, ideas):
    blocks = []
    for i, idea in enumerate(ideas):
        blocks.append(f"[{i}] Title: {idea['title']}\nBody: {idea['body']}")
    joined = "\n\n".join(blocks)
    return f"""You are a strict filter deciding which community-submitted trade ideas for {symbol} \
(from TradingView) are worth interrupting a real trader with a Telegram alert. The bar is HIGH -- \
this is not "does this have some technical reasoning", it's "would a disciplined trader actually take \
this specific trade right now". Expect MOST ideas to fail this bar; that is normal and correct, not a \
sign you're being too harsh.

REJECT if any of these apply:
- No clear, specific entry trigger or level (a "long-term view", a general trend opinion, or "watching \
this level" without a concrete plan does not count)
- Vague or generic reasoning that could apply to almost any chart (e.g. "strong momentum", "looks bullish")
- Educational/lesson content, motivational posts, or market commentary not tied to a live, actionable setup
- The setup depends on something that hasn't happened yet ("if it breaks X then Y") rather than a \
condition that's already true right now
- You are not genuinely confident a disciplined trader would act on this today

ONLY ACCEPT if the idea has a specific, current, actionable trade plan: a clear direction, a concrete \
entry condition that's already met (not conditional on a future break), and real technical reasoning \
tied to the actual current price structure (specific levels, confirmed pattern, or indicator state).

Ideas:
{joined}

Respond with ONLY valid JSON, no other text, in this exact shape:
{{"genuine_setups": [{{"index": 0, "direction": "long|short", "reasoning": "one sentence on the specific, current, actionable entry condition"}}]}}

Default to an empty genuine_setups list. Only include an idea if you would genuinely stake your own \
judgment on it being a real, doable trade right now -- not merely plausible-sounding."""


def call_llm(prompt):
    payload = json.dumps({"action": "news_briefing", "prompt": prompt}).encode()
    req = urllib.request.Request(WORKER_URL, data=payload, headers={
        "Content-Type": "application/json",
        "User-Agent": "btc-monitor-bot",
    })
    with urllib.request.urlopen(req, timeout=30) as resp:
        data = json.loads(resp.read())
    if "error" in data:
        raise RuntimeError(data["error"])
    return data["text"]


def parse_llm_json(raw):
    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        start, end = raw.find("{"), raw.rfind("}")
        if start == -1 or end == -1:
            return None
        try:
            return json.loads(raw[start:end + 1])
        except json.JSONDecodeError:
            return None


def bot_agrees_with_direction(symbol, market, direction):
    """Explicit second gate, requested directly: "only the ones the bot
    finds predictable too" -- an LLM judging a post's writeup as
    coherent isn't the same as the bot's own numbers actually agreeing.
    This is a lightweight sanity check, NOT a validated per-market
    strategy like check_watching_crypto()/india()/us() -- those each
    needed real backtesting before shipping; this is intentionally just
    "does current momentum and trend strength at least not contradict
    the suggested direction", reusing the exact rsi()/adx() functions
    already in this bot. Returns (agrees, rsi_value, adx_value)."""
    try:
        bars = monitor.fetch_klines(symbol, market, limit=60)
    except Exception:
        return False, None, None
    if len(bars) < 30:
        return False, None, None
    closed_bars = bars[:-1]
    if monitor.is_stale(closed_bars[-1]):
        return False, None, None
    r = monitor.rsi(closed_bars)
    a = monitor.adx(closed_bars)
    if a is None or a < 20:  # too choppy/directionless to trust either way
        return False, r, a
    if direction == "long" and r > 55:
        return True, r, a
    if direction == "short" and r < 45:
        return True, r, a
    return False, r, a


def surface_community_setup(symbol, market, direction, state):
    """Fires a REAL alert through the bot's own pipeline -- explicit
    design choice after direct feedback: not a separate "here's an
    idea" message, the exact same format/mechanics as any other fired
    setup (real entry/stop/qty via the same position_size()/
    committed_capital() logic every other setup uses, logged into
    setup_log so it's tracked and shadowed identically), just with one
    attribution line. Returns True if it actually fired."""
    try:
        bars = monitor.fetch_klines(symbol, market, limit=60)
    except Exception as e:
        print(f"{symbol}: fetch failed for community setup ({e})")
        return False
    if len(bars) < 15:
        return False
    closed_bars = bars[:-1]
    last_closed = closed_bars[-1]
    if monitor.is_stale(last_closed):
        return False

    n = monitor.atr(closed_bars)
    close = last_closed["close"]
    stop = (last_closed["low"] - 0.5 * n) if direction == "long" else (last_closed["high"] + 0.5 * n)

    symbols_state = state.setdefault("symbols", {})
    sym_state = symbols_state.setdefault(symbol, monitor.default_symbol_state(closed_bars))
    losses = sym_state.get("consecutive_losses", 0)
    wins = sym_state.get("consecutive_wins", 0)
    leverage = monitor.LEVERAGE_BY_MARKET.get(market, 1)

    if market == "india":
        base_capital, pool_markets = state.get("capital_inr", 100), ("india",)
    elif market == "commodity":
        base_capital, pool_markets = state.get("capital_usd_commodity", 100), ("commodity",)
    else:
        base_capital, pool_markets = state.get("capital_usd", 100), ("crypto", "us")
    setup_log = state.setdefault("setup_log", [])
    capital = max(base_capital - monitor.committed_capital(setup_log, pool_markets), 0)
    if capital <= 0:
        return False

    qty = monitor.position_size(capital, close, stop, losses, leverage=leverage, consecutive_wins=wins)
    if qty <= 0:
        return False

    currency = "Rs" if market == "india" else "$"
    action = "BUY" if direction == "long" else "SELL"
    text = monitor.build_alert_text(
        f"{symbol} {action} (community idea, confirmed)\n\n"
        f"{action}\nEntry: {close:,.4g}\nStoploss: {stop:,.4g}\nVolume: ~{qty:.6g} units\n"
        f"Take profit: Keep trailing (no fixed target)\n"
        f"{monitor.expected_profit_line(close, stop, qty, currency=currency)}\n\n"
        f"Setup taken by analysing a trade suggested on TradingView social debate.",
        symbol=symbol, price=close,
    )
    monitor.send_telegram(text)

    fired_at_dt = datetime.now(timezone.utc)
    setup_log.append({
        "symbol": symbol, "type": "community_idea", "direction": direction,
        "entry": close, "stop": stop, "target": None, "qty": qty,
        "fired_at": fired_at_dt.isoformat(),
        "resolved": False, "outcome": None, "surfaced": True, "taken": False,
        "confidence_at_fire": monitor.compute_bucket_confidence(setup_log, market, "community_idea", direction),
        "fired_hour_utc": fired_at_dt.hour, "fired_weekday_utc": fired_at_dt.weekday(),
        "shadow": {
            "direction": direction, "entry_price": close, "entry_qty": qty, "stop_loss": stop,
            "extreme_since_entry": close, "peak_profit_per_unit": 0, "take_profit_target": None,
            "consecutive_losses": 0, "consecutive_wins": 0, "trade_journal": [],
        },
    })
    return True


def main():
    state = monitor.load_state()
    seen_urls = set(state.get("community_ideas_seen", []))
    new_seen = list(seen_urls)

    watchlist = [(s["symbol"], "crypto") for s in monitor.CRYPTO_WATCHLIST]
    watchlist += [(s["symbol"], "commodity") for s in monitor.COMMODITY_WATCHLIST]
    watchlist += [(s, "india") for s in state.get("active_india_symbols", [])]
    watchlist += [(s, "us") for s in state.get("active_us_symbols", [])]

    sent_count = 0
    checked_count = 0

    for symbol, market in watchlist:
        ideas = fetch_symbol_ideas(symbol, market)
        if not ideas:
            continue
        checked_count += 1
        new_ideas = [idea for idea in ideas if idea["url"] not in seen_urls]
        if not new_ideas:
            continue

        for idea in new_ideas:
            new_seen.append(idea["url"])
            seen_urls.add(idea["url"])

        prompt = build_eval_prompt(symbol, new_ideas)
        try:
            raw = call_llm(prompt)
        except (urllib.error.HTTPError, RuntimeError) as e:
            print(f"{symbol}: LLM eval failed: {e}")
            continue

        result = parse_llm_json(raw)
        if not result or not result.get("genuine_setups"):
            continue

        for match in result["genuine_setups"]:
            idx = match.get("index")
            if idx is None or idx >= len(new_ideas):
                continue
            direction = match.get("direction")
            if direction not in ("long", "short"):
                continue

            agrees, r, a = bot_agrees_with_direction(symbol, market, direction)
            if not agrees:
                print(f"{symbol}: LLM approved a {direction} idea but bot's own read disagrees (rsi={r}, adx={a}) -- not surfacing.")
                continue

            if surface_community_setup(symbol, market, direction, state):
                sent_count += 1

    state["community_ideas_seen"] = new_seen[-2000:]
    monitor.save_state(state)
    print(f"Checked {checked_count} symbols, surfaced {sent_count} genuine community idea(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
