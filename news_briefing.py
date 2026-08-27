#!/usr/bin/env python3
"""Daily world finance news briefing -- fetches that day's real headlines
(Finnhub general news, confirmed live/working, no historical claim
needed since this only ever reads TODAY's news) and has an LLM read and
assess them for risk relevant to crypto/India/US markets.

Explicitly NOT wired into any trading decision -- no gating, no sizing
change, nothing here touches check_watching()/position_size(). This is
a judgment call ("is this headline bearish"), not a backtestable number
like everything else in this bot, and there's no historical archive of
world news to prove a rule against the way Fear & Greed or the
throttles were tested. Surfacing it as real, live, human-readable
context -- attached to the dashboard and sent as its own daily Telegram
message -- keeps a person in the loop on the actual judgment, same as
every other alert this bot has ever sent (it never auto-executes).

Run once daily, gated the same wall-clock way as the other special
steps in monitor.yml (see that file's comment on why -- github's
`schedule` trigger alone isn't reliable enough for this repo's actual
trigger mix of native schedule + external cron-job.org backup)."""
import json
import os
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone

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
    return [{"headline": i["headline"], "summary": i.get("summary", "")[:200]} for i in items[:limit]]


def build_prompt(headlines):
    lines = "\n".join(f"- {h['headline']}" for h in headlines)
    return f"""You are a market risk analyst. Below are today's real finance/world news headlines. \
Assess them for risk relevant to three specific markets this trading bot watches: \
crypto (BTC/ETH/SOL/XRP/AVAX/NEAR/FET), Indian equities (NSE), and US equities.

Headlines:
{lines}

Respond with ONLY valid JSON, no other text, in this exact shape:
{{
  "summary": "2-3 sentence plain-English overview of what matters today",
  "risk": {{"crypto": "elevated|normal|positive", "india": "elevated|normal|positive", "us": "elevated|normal|positive"}},
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
    for market in ("crypto", "india", "us"):
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
    if not headlines:
        print("No headlines fetched, skipping.")
        return 1

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

    state = monitor.load_state()
    state["news_briefing"] = {
        "date": datetime.now(timezone.utc).isoformat(),
        "assessment": assessment,
    }
    monitor.save_state(state)

    monitor.send_telegram(format_telegram(assessment))
    print("Briefing sent and saved.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
