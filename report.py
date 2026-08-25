#!/usr/bin/env python3
"""
Trade performance report -- aggregates every closed trade across every
symbol's trade_journal in state.json, sends a summary to Telegram, and
appends a dated snapshot to Trade Results.md (a permanent, ever-growing
log committed to the repo -- laptop-independent, unlike a literal file
on the Desktop which GitHub's cloud runners have no way to write to).

Grouped by currency (USD for crypto/US, INR for India) rather than
summed together, since combining different currencies into one number
would be meaningless.

Older trade_journal entries (logged before qty tracking was added) may
not have a pnl_total -- those are counted toward win rate but excluded
from the $/Rs P&L sum, which is called out explicitly in the report
rather than silently under/over-counting.

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


def build_report():
    state = monitor.load_state()
    symbols_state = state.get("symbols", {})

    groups = {"USD": [], "INR": []}
    for symbol, sym_state in symbols_state.items():
        cur = currency_for(symbol)
        for trade in sym_state.get("trade_journal", []):
            if trade.get("pnl_per_unit") is None:
                continue
            groups[cur].append({"symbol": symbol, **trade})

    lines = []
    any_trades = False

    for cur, trades in groups.items():
        if not trades:
            continue
        any_trades = True
        wins = [t for t in trades if t["pnl_per_unit"] > 0]
        losses = [t for t in trades if t["pnl_per_unit"] <= 0]
        win_rate = len(wins) / len(trades) * 100 if trades else 0

        priced = [t for t in trades if t.get("pnl_total") is not None]
        unpriced_count = len(trades) - len(priced)
        total_pnl = sum(t["pnl_total"] for t in priced)

        lines.append(f"**{cur}**")
        lines.append(f"- Trades: {len(trades)} | Win rate: {win_rate:.1f}% ({len(wins)}W / {len(losses)}L)")
        lines.append(f"- Total P&L: {total_pnl:+,.4g} {cur}" + (
            f" (from {len(priced)} trades with recorded size; {unpriced_count} older trade(s) had no size recorded, excluded)"
            if unpriced_count else ""
        ))
        if wins:
            lines.append(f"- Avg win: {sum(t['pnl_per_unit'] for t in wins) / len(wins):+.4g} per unit")
        if losses:
            lines.append(f"- Avg loss: {sum(t['pnl_per_unit'] for t in losses) / len(losses):+.4g} per unit")
        best = max(trades, key=lambda t: t["pnl_per_unit"])
        worst = min(trades, key=lambda t: t["pnl_per_unit"])
        lines.append(f"- Best: {best['symbol']} {best['pnl_per_unit']:+.4g}/unit | Worst: {worst['symbol']} {worst['pnl_per_unit']:+.4g}/unit")
        lines.append("")

    if not any_trades:
        lines.append("No closed trades logged yet.")

    return "\n".join(lines)


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


def build_you_vs_bot_report():
    """Your real trades (trade_journal, only what you registered via
    open/fill/close) against every setup the bot fired at all, taken or
    not (setup_log, shadow-tracked). Answers "am I beating the raw
    signal quality, or would I have done better just taking everything."
    """
    state = monitor.load_state()
    symbols_state = state.get("symbols", {})
    setup_log = state.get("setup_log", [])

    your_by_currency = {}
    for symbol, sym_state in symbols_state.items():
        cur = currency_for(symbol)
        for t in sym_state.get("trade_journal", []):
            if t.get("pnl_per_unit") is None:
                continue
            d = your_by_currency.setdefault(cur, {"n": 0, "wins": 0, "pnl": 0})
            d["n"] += 1
            d["wins"] += 1 if t["pnl_per_unit"] > 0 else 0
            if t.get("pnl_total") is not None:
                d["pnl"] += t["pnl_total"]

    bot_by_currency = {}
    for e in setup_log:
        if not e["resolved"]:
            continue
        cur = currency_for(e["symbol"])
        outcome = e["outcome"]
        d = bot_by_currency.setdefault(cur, {"n": 0, "wins": 0, "pnl": 0})
        d["n"] += 1
        d["wins"] += 1 if outcome["pnl_per_unit"] > 0 else 0
        if outcome.get("pnl_total") is not None:
            d["pnl"] += outcome["pnl_total"]

    currencies = set(your_by_currency) | set(bot_by_currency)
    if not currencies:
        return "**YOU vs BOT**\nNo data yet on either side."

    lines = ["**YOU vs BOT** (your registered trades vs. every setup the bot fired, taken or not)"]
    for cur in sorted(currencies):
        y = your_by_currency.get(cur, {"n": 0, "wins": 0, "pnl": 0})
        b = bot_by_currency.get(cur, {"n": 0, "wins": 0, "pnl": 0})
        y_wr = y["wins"] / y["n"] * 100 if y["n"] else 0
        b_wr = b["wins"] / b["n"] * 100 if b["n"] else 0
        lines.append(f"**{cur}**")
        lines.append(f"- You: {y['n']} trades | {y_wr:.1f}% win rate | {y['pnl']:+,.4g} {cur}")
        lines.append(f"- Bot (every setup): {b['n']} resolved | {b_wr:.1f}% hit rate | {b['pnl']:+,.4g} {cur}")
        if y["n"] and b["n"]:
            diff = y["pnl"] - b["pnl"]
            verdict = "ahead of" if diff > 0 else "behind" if diff < 0 else "matching"
            lines.append(f"- You're {verdict} the bot's overall signal quality by {abs(diff):+,.4g} {cur}")

    return "\n".join(lines)


def main():
    report_text = (
        build_report() + "\n\n" + build_setup_log_report() + "\n\n" + build_you_vs_bot_report()
    )
    append_to_file(report_text)
    monitor.send_telegram("TRADE PERFORMANCE REPORT\n\n" + report_text)


if __name__ == "__main__":
    sys.exit(main())
