#!/usr/bin/env python3
"""
Trade performance report -- aggregates every closed trade across every
symbol's trade_journal in state.json and sends a summary to Telegram:
total trades, win rate, total P&L, average win/loss, best/worst trade.

Grouped by currency (USD for crypto/US, INR for India) rather than
summed together, since combining different currencies into one number
would be meaningless.

Older trade_journal entries (logged before qty tracking was added) may
not have a pnl_total -- those are counted toward win rate but excluded
from the $/Rs P&L sum, which is called out explicitly in the report
rather than silently under/over-counting.

Trigger manually anytime: workflow_dispatch with mode=report. Never
places trades -- read-only reporting.
"""
import sys

import monitor


def currency_for(symbol):
    return "INR" if symbol.endswith(".NS") else "USD"


def main():
    state = monitor.load_state()
    symbols_state = state.get("symbols", {})

    groups = {"USD": [], "INR": []}
    for symbol, sym_state in symbols_state.items():
        cur = currency_for(symbol)
        for trade in sym_state.get("trade_journal", []):
            if trade.get("pnl_per_unit") is None:
                continue
            groups[cur].append({"symbol": symbol, **trade})

    lines = ["TRADE PERFORMANCE REPORT\n"]
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

        lines.append(f"--- {cur} ---")
        lines.append(f"Trades: {len(trades)} | Win rate: {win_rate:.1f}% ({len(wins)}W / {len(losses)}L)")
        lines.append(f"Total P&L: {total_pnl:+,.4g} {cur}" + (
            f" (from {len(priced)} trades with recorded size; {unpriced_count} older trade(s) had no size recorded, excluded from this sum)"
            if unpriced_count else ""
        ))
        if wins:
            lines.append(f"Avg win: {sum(t['pnl_per_unit'] for t in wins) / len(wins):+.4g} per unit")
        if losses:
            lines.append(f"Avg loss: {sum(t['pnl_per_unit'] for t in losses) / len(losses):+.4g} per unit")
        best = max(trades, key=lambda t: t["pnl_per_unit"])
        worst = min(trades, key=lambda t: t["pnl_per_unit"])
        lines.append(f"Best: {best['symbol']} {best['pnl_per_unit']:+.4g}/unit | Worst: {worst['symbol']} {worst['pnl_per_unit']:+.4g}/unit")
        lines.append("")

    if not any_trades:
        lines.append("No closed trades logged yet.")

    monitor.send_telegram("\n".join(lines))


if __name__ == "__main__":
    sys.exit(main())
