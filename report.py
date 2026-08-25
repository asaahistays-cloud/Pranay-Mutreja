#!/usr/bin/env python3
"""
Signal quality report -- every setup the bot has fired, whether or not
the user took it, shadow-tracked to a real outcome and summarized: hit
rate, P&L by currency, breakdown by setup type. Sends to Telegram and
appends a dated snapshot to Trade Results.md (a permanent, ever-growing
log committed to the repo -- laptop-independent, unlike a literal file
on the Desktop which GitHub's cloud runners have no way to write to).

There used to also be a real-trade-performance section (from manually
registering trades via Telegram commands) and a YOU vs BOT comparison,
but the whole open/fill/skip/close tracking system was removed --
trade_journal will never gain new entries, so those sections would only
ever show stale data. Signal quality is the one section with real,
current data every night, since it's fully automatic.

Runs nightly at 12:00 AM IST via an external cron-job.org trigger
(workflow_dispatch, mode=report), same reliable pattern as the other
scheduled checks. Can also be triggered manually anytime for an
on-demand snapshot. Never places trades -- read-only reporting.
"""
import os
import sys
from datetime import datetime, timezone, timedelta

import monitor

RESULTS_FILE = os.path.join(os.path.dirname(__file__), "Trade Results.md")


def currency_for(symbol):
    return "INR" if symbol.endswith(".NS") else "USD"


def build_setup_log_report():
    """Every setup the bot has fired, whether or not the user took it,
    shadow-tracked to a real outcome (hit its target / trailing stop
    lock, or stopped out) using the exact same check_open() logic as a
    real position -- just silent. Answers "does it actually reach the
    expected profit" with real numbers instead of the alert's promise."""
    state = monitor.load_state()
    log = state.get("setup_log", [])
    if not log:
        return "**SIGNAL QUALITY**\nNo setups logged yet."

    resolved = [e for e in log if e["resolved"]]
    pending = len(log) - len(resolved)
    lines = ["**SIGNAL QUALITY** (every setup fired, taken or not -- shadow-tracked automatically)",
              f"- Fired: {len(log)} | Resolved: {len(resolved)} | Still open: {pending}"]

    if resolved:
        wins = [e for e in resolved if e["outcome"]["pnl_per_unit"] > 0]
        win_rate = len(wins) / len(resolved) * 100
        lines.append(f"- Hit rate: {win_rate:.1f}% ({len(wins)}W / {len(resolved) - len(wins)}L)")

        by_currency = {}
        for e in resolved:
            pnl_total = e["outcome"].get("pnl_total")
            if pnl_total is not None:
                cur = currency_for(e["symbol"])
                by_currency[cur] = by_currency.get(cur, 0) + pnl_total
        for cur, total in by_currency.items():
            lines.append(f"- Simulated P&L ({cur}): {total:+,.4g}")

        by_type = {}
        for e in resolved:
            d = by_type.setdefault(e["type"], {"n": 0, "wins": 0})
            d["n"] += 1
            d["wins"] += 1 if e["outcome"]["pnl_per_unit"] > 0 else 0
        for t, d in by_type.items():
            wr = d["wins"] / d["n"] * 100 if d["n"] else 0
            lines.append(f"  {t}: {d['n']} fired, {wr:.0f}% hit rate")

    return "\n".join(lines)


def append_to_file(report_text):
    ist_now = datetime.now(timezone.utc) + timedelta(hours=5, minutes=30)
    header = f"## {ist_now.strftime('%Y-%m-%d %H:%M')} IST\n\n"
    entry = header + report_text + "\n\n---\n\n"

    if not os.path.exists(RESULTS_FILE):
        with open(RESULTS_FILE, "w") as f:
            f.write("# Trade Results\n\nRunning log of trade performance, appended nightly at 12:00 AM IST (and on any manual report request).\n\n---\n\n")

    with open(RESULTS_FILE, "a") as f:
        f.write(entry)


def main():
    report_text = build_setup_log_report()
    append_to_file(report_text)
    monitor.send_telegram("TRADE PERFORMANCE REPORT\n\n" + report_text)


if __name__ == "__main__":
    sys.exit(main())
