#!/usr/bin/env python3
"""Checks TradingView's public per-symbol "Ideas" pages -- real community
trade-setup posts, not just news -- for the bot's active watchlist.
Confirmed live and free: no auth, no API key, not rate-limited on
repeated requests, real post content (title + body text), not a JS
shell (verified by pulling real post text directly out of a raw
fetch). robots.txt disallows the generic /ideas/ hub but NOT the
per-symbol /symbols/{SYMBOL}/ideas/ path used here.

Explicitly does NOT blindly follow community setups -- the whole point
is the opposite: an LLM reads each new idea and judges whether it's a
genuine, coherent trade setup worth your attention (clear direction,
real technical reasoning) versus generic content (motivational posts,
vague commentary, no actual setup). Only ideas the LLM judges as
genuine get surfaced, clearly labeled as a community idea, not the
bot's own signal -- this never fires an alert, changes sizing, or
touches any trading decision, same rule as everything else non-price-
based in this bot. No historical archive of community ideas exists to
backtest a rule against (same reason Fear & Greed and world news stay
informational), so surfacing worthwhile ideas for you to evaluate is
the ceiling here, not autonomous decision-making.

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


def tv_symbol_path(symbol, market):
    """Maps this bot's own symbol format to TradingView's URL scheme.
    Crypto (BTC-USD) -> BTCUSD. India (RECLTD.NS) -> NSE-RECLTD. US
    (AAPL) -> try NASDAQ/NYSE/AMEX in turn since the bot doesn't track
    which exchange each symbol trades on."""
    if market == "crypto":
        return [symbol.replace("-", "")]
    if market == "india":
        return [f"NSE-{symbol[:-3]}"]
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
    return f"""You are evaluating community-submitted trade ideas for {symbol} from TradingView. \
Some are genuine trade setups with real technical reasoning (a clear direction, specific levels, \
market structure/indicator-based reasoning). Others are generic content: motivational posts, vague \
commentary, educational lessons not tied to a live setup, or pure hype with no actual reasoning. \
Only genuine setups are worth surfacing.

Ideas:
{joined}

Respond with ONLY valid JSON, no other text, in this exact shape:
{{"genuine_setups": [{{"index": 0, "direction": "long|short|neutral", "reasoning": "one sentence on why this looks like a real, coherent setup"}}]}}

Only include ideas that are genuinely coherent trade setups with real reasoning behind them. If none \
of the ideas qualify, return an empty genuine_setups list -- do not force a match where there isn't one."""


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


def format_telegram(symbol, market, idea, direction, reasoning):
    return (
        f"COMMUNITY IDEA -- {symbol} ({market})\n\n"
        f"{idea['title']}\n"
        f"Direction (community): {direction}\n"
        f"Why it looked coherent: {reasoning}\n\n"
        f"{idea['url']}\n\n"
        f"(Not the bot's own signal -- a real community post an LLM judged coherent. "
        f"Your call entirely; doesn't fire an alert or affect sizing.)"
    )


def main():
    state = monitor.load_state()
    seen_urls = set(state.get("community_ideas_seen", []))
    new_seen = list(seen_urls)

    watchlist = [(s["symbol"], "crypto") for s in monitor.CRYPTO_WATCHLIST]
    watchlist += [(s, "india") for s in state.get("active_india_symbols", [])]
    watchlist += [(s, "us") for s in state.get("active_us_symbols", [])]

    surfaced_today = state.get("community_ideas_surfaced") or []
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
            idea = new_ideas[idx]
            text = format_telegram(symbol, market, idea, match.get("direction", "unknown"), match.get("reasoning", ""))
            monitor.send_telegram(text)
            surfaced_today.append({
                "symbol": symbol, "market": market, "title": idea["title"],
                "url": idea["url"], "direction": match.get("direction"),
                "reasoning": match.get("reasoning"),
                "date": datetime.now(timezone.utc).isoformat(),
            })
            sent_count += 1

    state["community_ideas_seen"] = new_seen[-2000:]
    state["community_ideas_surfaced"] = surfaced_today[-50:]
    monitor.save_state(state)
    print(f"Checked {checked_count} symbols, surfaced {sent_count} genuine community idea(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
