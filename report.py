#!/usr/bin/env python3
"""
Signal quality report -- answers one question: "if I had taken every
trade the bot suggested today, would I be up or down, and how many
were actually right vs wrong?" Every fired setup is shadow-tracked to
a real outcome (hit its target/trailing-stop lock, or stopped out)
using the exact same check_open() logic as a real position -- just
silent -- regardless of whether the user actually took the trade.
Sends to Telegram and appends a dated snapshot to Trade Results.md (a
permanent, ever-growing log committed to the repo -- laptop-independent,
unlike a literal file on the Desktop which GitHub's cloud runners have
no way to write to).

Scoped to the current IST calendar day, not all-time -- a setup fired
minutes ago hasn't had time to hit its target or stop yet, so lumping
it in with weeks of history would bury today's actual answer. Runs
nightly at 12:00 AM IST via an external cron-job.org trigger
(workflow_dispatch, mode=report). Can also be triggered manually
anytime for an on-demand snapshot. Never places trades -- read-only
reporting.
"""
import os
import sys
from datetime import datetime, timezone, timedelta

import monitor

RESULTS_FILE = os.path.join(os.path.dirname(__file__), "Trade Results.md")
IST_OFFSET = timedelta(hours=5, minutes=30)


def currency_for(symbol):
    return "INR" if symbol.endswith(".NS") else "USD"


def to_ist_date(iso_str):
    dt = datetime.fromisoformat(iso_str)
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return (dt + IST_OFFSET).strftime("%Y-%m-%d")


def market_of(symbol):
    if symbol.endswith(".NS"):
        return "india"
    if "-USD" in symbol:
        return "crypto"
    return "us"


def build_daily_report(state, log_key="setup_log", label="TODAY'S SIGNAL QUALITY", day_ist=None, market=None):
    """If you'd taken every trade the bot fired today, taken or not --
    what's the real win/loss count and net P&L? Only setups fired
    during the given IST calendar day (default: today) are counted, so
    a fresh setup that hasn't had time to hit its target/stop yet shows
    up as pending, not lumped into a stale all-time average. Pass
    market="india"/"crypto"/"us" to scope the report to just that
    market -- each one now runs different entry logic (see
    monitor.check_watching()), so blending them into one number hides
    which market is actually driving the result. Only counts setups
    that were actually surfaced to Telegram -- when several fire in
    one scan, only the top few by conviction get sent (see main()'s
    best-of-N selection), so "suggested" means what you actually saw,
    not everything that structurally fired. Older entries predating
    that change have no "surfaced" field and default to counted."""
    day_ist = day_ist or (datetime.now(timezone.utc) + IST_OFFSET).strftime("%Y-%m-%d")
    log = [e for e in state.get(log_key, []) if to_ist_date(e["fired_at"]) == day_ist and e.get("surfaced", True)]
    if market:
        log = [e for e in log if market_of(e["symbol"]) == market]

    if not log:
        return f"**{label}** ({day_ist})\nNo setups fired today."

    resolved = [e for e in log if e["resolved"]]
    pending = len(log) - len(resolved)
    lines = [f"**{label}** ({day_ist})",
              f"- Suggested: {len(log)} trade(s) | Resolved: {len(resolved)} | Still playing out: {pending}"]

    if resolved:
        wins = [e for e in resolved if e["outcome"]["pnl_per_unit"] > 0]
        losses = len(resolved) - len(wins)
        win_rate = len(wins) / len(resolved) * 100
        lines.append(f"- If you'd taken all {len(resolved)} resolved trades: {len(wins)} right, {losses} wrong ({win_rate:.0f}% correct)")

        by_currency = {}
        for e in resolved:
            pnl_total = e["outcome"].get("pnl_total")
            if pnl_total is not None:
                cur = currency_for(e["symbol"])
                by_currency[cur] = by_currency.get(cur, 0) + pnl_total
        for cur, total in by_currency.items():
            sign = "profit" if total >= 0 else "loss"
            lines.append(f"- Net {sign} ({cur}): {total:+,.4g}")

        for e in resolved:
            mark = "+" if e["outcome"]["pnl_per_unit"] > 0 else "-"
            lines.append(f"  [{mark}] {e['symbol']} {e['type']} ({e['direction']}): {e['outcome']['pnl_total']:+,.4g}" if e["outcome"].get("pnl_total") is not None else f"  [{mark}] {e['symbol']} {e['type']} ({e['direction']})")
    else:
        lines.append("- None have hit their target or stop yet -- too soon to call any of them right or wrong.")

    if pending:
        lines.append(f"- {pending} trade(s) still open, not yet counted above: " +
                      ", ".join(f"{e['symbol']} ({e['type']})" for e in log if not e["resolved"]))

    return "\n".join(lines)


def append_to_file(report_text):
    ist_now = datetime.now(timezone.utc) + IST_OFFSET
    header = f"## {ist_now.strftime('%Y-%m-%d %H:%M')} IST\n\n"
    entry = header + report_text + "\n\n---\n\n"

    if not os.path.exists(RESULTS_FILE):
        with open(RESULTS_FILE, "w") as f:
            f.write("# Trade Results\n\nRunning log of trade performance, appended nightly at 12:00 AM IST (and on any manual report request).\n\n---\n\n")

    with open(RESULTS_FILE, "a") as f:
        f.write(entry)


def main():
    state = monitor.load_state()
    sections = [
        build_daily_report(state, label="INDIA -- SIGNAL QUALITY", market="india"),
        build_daily_report(state, label="CRYPTO -- SIGNAL QUALITY", market="crypto"),
        build_daily_report(state, label="US -- SIGNAL QUALITY", market="us"),
    ]
    report_text = "\n\n".join(sections)
    append_to_file(report_text)
    monitor.send_telegram("TRADE PERFORMANCE REPORT\n\n" + report_text)


if __name__ == "__main__":
    sys.exit(main())
