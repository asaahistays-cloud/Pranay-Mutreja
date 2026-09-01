#!/usr/bin/env python3
"""World finance news briefing -- fetches real headlines (Finnhub
general news + Economic Times' India markets RSS feed, both confirmed
live/working) and has an LLM read and assess them for risk relevant to
crypto/India/US markets.

Finnhub's "general" category is US/global-macro skewed -- confirmed
directly: a real live pull returned 40 headlines (Middle East/oil/US
mortgage rates), zero India-specific stories, so "india: elevated" was
being inferred entirely from global spillover, never from actual NSE/
India news. Economic Times' markets RSS (no API key needed, unlike
Finnhub) fixes that -- confirmed live and current (same-day pubDates,
real NIFTY/bond-yield/Indian-company headlines).

Explicitly NOT wired into any trading decision -- no gating, no sizing
change, nothing here touches check_watching()/position_size(). This is
a judgment call ("is this headline bearish"), not a backtestable number
like everything else in this bot, and there's no historical archive of
world news to prove a rule against the way Fear & Greed or the
throttles were tested. Surfacing it as real, live, human-readable
context -- attached to the dashboard and sent as its own Telegram
message -- keeps a person in the loop on the actual judgment, same as
every other alert this bot has ever sent (it never auto-executes).

Runs every scan (same ~15min cadence as monitor.py, no wall-clock
window -- see monitor.yml), but is deliberately cheap on both the LLM
call and Telegram: fetches fresh headlines every time (free, no cost
either way) and always updates state.json so the dashboard's list is
never stale, but only calls the LLM and sends a Telegram message when
at least one headline is genuinely new since the last check (tracked
by id, not text -- immune to formatting differences; Finnhub's own
numeric id for its items, a stable hash of the article link for ET's
RSS items since RSS has no numeric id). Most 15-min windows won't have
new world-news items, so this naturally rate-limits itself without an
arbitrary schedule."""
import hashlib
import json
import os
import re
import sys
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime

import monitor

FINNHUB_KEY = os.environ.get("FINNHUB_API_KEY", "")
# Free LLM call via the Cloudflare Worker's Workers AI binding -- no API
# key needed here at all (unlike Anthropic, which needs a funded
# account). The Worker gets AI access through its own deploy-time
# binding; this script just POSTs a prompt to the same Worker URL
# already used for Taken/Log Trade/Close/price-proxy tonight.
WORKER_URL = "https://multi-market-monitor-taken.asaahistays.workers.dev"


def fetch_world_news(limit=40):
    url = f"https://finnhub.io/api/v1/news?category=general&token={FINNHUB_KEY}"
    req = urllib.request.Request(url, headers={"User-Agent": "btc-monitor-bot"})
    with urllib.request.urlopen(req, timeout=15) as resp:
        items = json.loads(resp.read())
    items.sort(key=lambda x: x.get("datetime", 0), reverse=True)
    return [{
        "id": i.get("id"), "headline": i["headline"], "summary": i.get("summary", "")[:200],
        "url": i.get("url", ""), "source": i.get("source", ""),
        "datetime": i.get("datetime", 0),
    } for i in items[:limit]]


def fetch_india_news(limit=25):
    """Economic Times' markets RSS -- no API key needed. Item ids are a
    stable hash of the article link (RSS has no numeric id like
    Finnhub's), so the same article always dedups to the same id across
    runs even if the title text gets re-cased/re-punctuated upstream."""
    url = "https://economictimes.indiatimes.com/markets/rssfeeds/1977021501.cms"
    req = urllib.request.Request(url, headers={"User-Agent": "btc-monitor-bot"})
    with urllib.request.urlopen(req, timeout=15) as resp:
        root = ET.fromstring(resp.read())
    items = []
    for item in root.findall(".//item"):
        title = (item.findtext("title") or "").strip()
        link = (item.findtext("link") or "").strip()
        if not title or not link:
            continue
        desc = re.sub(r"<[^>]+>", "", item.findtext("description") or "").strip()
        pubdate_raw = item.findtext("pubDate")
        try:
            dt = int(parsedate_to_datetime(pubdate_raw).timestamp()) if pubdate_raw else 0
        except (TypeError, ValueError):
            dt = 0
        items.append({
            "id": "et_" + hashlib.md5(link.encode()).hexdigest()[:12],
            "headline": title, "summary": desc[:200], "url": link,
            "source": "Economic Times", "datetime": dt,
        })
    items.sort(key=lambda x: x["datetime"], reverse=True)
    return items[:limit]


def build_prompt(headlines):
    lines = "\n".join(f"- {h['headline']}" for h in headlines)
    return f"""You are a market risk analyst. Below are today's real finance/world news headlines. \
Assess them for risk relevant to four specific markets this trading bot watches: \
crypto (BTC/ETH/SOL/XRP/AVAX/NEAR/FET -- spot and leveraged futures both move on the same news, \
read as one market), Indian equities including NIFTY/BankNifty/Sensex index futures (NSE cash and \
derivatives move on the same macro/news drivers -- RBI policy, budget, FII flows, global cues -- so \
read these as one market, not two), US equities, and commodities (Gold GC=F, Natural Gas NG=F -- \
driven by inflation expectations, USD strength, and safe-haven demand for gold; weather and EIA \
storage data for natural gas -- genuinely different drivers from the equity/crypto markets above, \
assess separately).

Headlines:
{lines}

Respond with ONLY valid JSON, no other text, in this exact shape:
{{
  "summary": "2-3 sentence plain-English overview of what matters today",
  "risk": {{"crypto": "elevated|normal|positive", "india": "elevated|normal|positive", "us": "elevated|normal|positive", "commodity": "elevated|normal|positive"}},
  "key_events": [{{"headline": "...", "why_it_matters": "one sentence"}}]
}}

Only include up to 3 key_events -- the ones that could genuinely move markets, not routine news. \
If nothing stands out as risk-relevant, say so plainly in the summary and use "normal" for all three -- \
do not manufacture urgency where there isn't any."""


def call_llm(prompt):
    # Cloudflare's own bot protection blocks the default Python-urllib
    # User-Agent with a 403 (confirmed directly: works from curl's
    # default UA, 403s with Python's) -- a real header sidesteps it.
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


def format_telegram(assessment):
    risk = assessment["risk"]
    risk_emoji = {"elevated": "\U0001F534", "normal": "\U0001F7E2", "positive": "\U0001F535"}
    lines = ["DAILY NEWS BRIEFING", "", assessment["summary"], ""]
    for market in ("crypto", "india", "us", "commodity"):
        lvl = risk.get(market, "normal")
        lines.append(f"{risk_emoji.get(lvl, '')} {market.upper()}: {lvl}")
    if assessment.get("key_events"):
        lines.append("")
        lines.append("Key events:")
        for e in assessment["key_events"]:
            lines.append(f"- {e['headline']}")
            lines.append(f"  -> {e['why_it_matters']}")
    lines.append("")
    lines.append("(Context only -- doesn't change what fires or how it's sized.)")
    return "\n".join(lines)


def main():
    if not FINNHUB_KEY:
        print("FINNHUB_API_KEY not set, skipping.")
        return 1

    headlines = fetch_world_news()
    # ET's RSS is a second, independent source -- a failure here (feed
    # down, schema change, network blip) must not take down the whole
    # script the same way a Finnhub non-zero exit once took down 3 real
    # monitor scans (see below). Falls back to Finnhub-only for this
    # cycle rather than failing closed.
    try:
        india_headlines = fetch_india_news()
    except Exception as e:
        print(f"India news fetch failed ({e}), continuing with Finnhub only.")
        india_headlines = []
    headlines = sorted(headlines + india_headlines, key=lambda h: h.get("datetime", 0), reverse=True)
    if not headlines:
        # Not a real failure -- an empty/transient response from Finnhub
        # this cycle is expected sometimes and nothing is actually wrong.
        # Exiting 0 here matters: this step has no failure isolation of
        # its own in monitor.yml (see that file's comment), so a non-zero
        # exit here used to skip every subsequent step in the job,
        # including the real monitor scan -- confirmed directly: this
        # exact line took down 3 full scans today, meaning no trading
        # alerts fired those cycles at all.
        print("No headlines fetched this cycle -- nothing wrong, just nothing new to report.")
        return 0

    state = monitor.load_state()
    seen_ids_list = state.get("news_seen_ids", [])
    seen_ids_set = set(seen_ids_list)
    new_headlines = [h for h in headlines if h.get("id") is not None and h["id"] not in seen_ids_set]

    # Always refresh the full readable list + fetch timestamp, even with
    # nothing new to assess -- explicitly requested: the user wants to
    # read the real headlines themselves, so the dashboard's list should
    # never go stale even on a quiet scan with no new items.
    existing_briefing = state.get("news_briefing") or {}
    state["news_briefing"] = {
        "date": datetime.now(timezone.utc).isoformat(),
        "assessment": existing_briefing.get("assessment"),
        "headlines": headlines,
    }

    if not new_headlines:
        monitor.save_state(state)
        print(f"No new headlines since last check ({len(headlines)} fetched, all already seen) -- list refreshed, LLM/Telegram skipped.")
        return 0

    prompt = build_prompt(headlines)
    try:
        raw = call_llm(prompt)
    except (urllib.error.HTTPError, RuntimeError) as e:
        print(f"LLM call failed: {e}")
        return 1

    try:
        assessment = json.loads(raw)
    except json.JSONDecodeError:
        # occasionally a model wraps JSON in prose/fencing despite instructions
        start, end = raw.find("{"), raw.rfind("}")
        if start == -1 or end == -1:
            print(f"Could not parse LLM response as JSON: {raw[:300]}")
            return 1
        assessment = json.loads(raw[start:end + 1])

    state["news_briefing"]["assessment"] = assessment
    # Chronological list (not a set) so "keep the most recent 1000" via
    # a plain slice actually keeps the most recent ones, not an
    # arbitrary subset -- a set has no reliable insertion order.
    seen_ids_list = seen_ids_list + [h["id"] for h in new_headlines]
    state["news_seen_ids"] = seen_ids_list[-1000:]
    monitor.save_state(state)

    monitor.send_telegram(format_telegram(assessment))
    print(f"{len(new_headlines)} new headline(s) -- briefing sent and saved.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
