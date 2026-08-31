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

# Per-market UTC timestamp of when that market's CURRENTLY-LIVE entry
# strategy went live. Entries fired before this are from a superseded
# strategy (e.g. US's old unfiltered check_watching_default() logic,
# replaced by Gap and Go on 2026-08-26) -- blending them into "today's"
# numbers would misrepresent how the strategy actually in production
# right now is performing. A market with no entry here has run its
# current strategy for the whole day, so no cutoff is needed. Update
# this whenever a market's strategy changes.
STRATEGY_LAUNCHED_AT = {
    "us": "2026-08-26T14:35:00+00:00",  # Gap and Go (short-only)
}


def currency_for(symbol):
    return "INR" if symbol.endswith(".NS") or symbol.endswith("-FUT") else "USD"


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
    if symbol.endswith("-FUT"):
        return "india_futures"
    return "us"


def explain_trigger(setup_type, trigger_context):
    """Self-learning groundwork, step 2: turn a logged trigger_context
    (see monitor.py's check_*() functions -- each attaches the specific
    indicator values behind its own fire) into one plain-language line
    of "why this fired". Purely a formatter over already-logged numbers,
    same spirit as monitor.py's build_alert_text() at entry time, just
    reconstructed after the fact for the report instead of live. Entries
    fired before trigger_context started being logged have none -- say
    so rather than guessing."""
    if not trigger_context:
        return "no trigger detail logged (fired before trigger_context tracking started)"
    tc = trigger_context
    parts = []

    if setup_type in ("triple_ma_long", "triple_ma_short"):
        p = tc.get("periods", {})
        parts.append(f"EMA({p.get('fast')}/{p.get('med')}/{p.get('slow')}) = {tc.get('fast_ema'):,.4g}/{tc.get('med_ema'):,.4g}/{tc.get('slow_ema'):,.4g}, freshly aligned")
    elif setup_type in ("triple_threat_long", "triple_threat_short"):
        parts.append(f"RSI {tc.get('rsi_prev'):.0f}->{tc.get('rsi_now'):.0f} crossed 50, broke {tc.get('breakout_level'):,.4g}, trend EMA {tc.get('trend_ema'):,.4g}")
    elif setup_type == "gap_and_go_short":
        gap = tc.get("gap_pct")
        parts.append(f"gapped {gap:+.2f}% overnight, broke opening-range low {tc.get('opening_range_low'):,.4g}, vol {tc.get('volume'):,.0f} vs avg {tc.get('avg_volume'):,.0f}" if gap is not None else "gap setup (gap_pct not logged)")
    elif setup_type in ("breakout_long", "breakdown_short"):
        level_key = "range_high" if setup_type == "breakout_long" else "range_low"
        level = tc.get(level_key)
        conf = f", {tc['confirmation']}" if tc.get("confirmation") else ""
        trend = tc.get("trend_ema")
        parts.append(f"broke {level_key.replace('_', ' ')} {level:,.4g} on vol {tc.get('volume'):,.0f} vs avg {tc.get('avg_volume'):,.0f}, trend EMA {trend:,.4g}{conf}" if trend else f"broke {level_key.replace('_', ' ')} {level:,.4g} on vol {tc.get('volume'):,.0f} vs avg {tc.get('avg_volume'):,.0f}{conf}")
    elif setup_type in ("range_long_rejection", "range_short_rejection"):
        wick_key = "wick_low" if setup_type == "range_long_rejection" else "wick_high"
        near = "low" if setup_type == "range_long_rejection" else "high"
        adx = tc.get("adx")
        adx_part = f", ADX {adx} confirmed ranging" if adx is not None else ""
        parts.append(f"wicked to {tc.get(wick_key):,.4g} near range {near} [{tc.get('range_low'):,.4g}, {tc.get('range_high'):,.4g}], closed back inside{adx_part}")
    elif setup_type in ("dmi_dpo_long", "dmi_dpo_short"):
        parts.append(f"+DI {tc.get('plus_di')} vs -DI {tc.get('minus_di')}, ADX {tc.get('adx')}, DPO {tc.get('dpo'):,.4g} (period {tc.get('period')})")
    elif setup_type.startswith("seasonal_"):
        eia = tc.get("eia_surprise_bcf")
        parts.append(f"month {tc.get('month')} seasonal edge" + (f", EIA surprise {eia:+.0f} Bcf confirmed" if eia is not None else ""))
    else:
        parts.append(", ".join(f"{k}={v}" for k, v in tc.items() if k not in ("rsi", "vwap", "gate")))

    if tc.get("gate"):
        parts.append(f"India gate: RSI {tc.get('rsi')} / VWAP {tc.get('vwap'):,.4g} ({tc['gate']})")

    return "; ".join(parts)


def explain_outcome(exit_reason, pnl_per_unit):
    """The other half of "why" -- not the entry condition but how the
    trade actually resolved. stop_hit splits into two very different
    stories depending on pnl sign (see the bot-selflearning-checkin
    scheduled task, which established this same split at the bucket
    level): trail-locked win means price moved favorably first and the
    trailing stop rode it into profit (the entry had real follow-
    through); real stop-loss means it went against the entry with no
    favorable move first (no edge at that moment). Reused here per-trade
    instead of aggregated per-bucket."""
    if exit_reason == "stop_hit":
        if pnl_per_unit > 0:
            return "trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)"
        return "real stop-loss -- no favorable move before the stop hit (no edge at entry)"
    if exit_reason == "take_profit":
        return "hit fixed target -- clean win"
    if exit_reason in ("manual_close", "manual_exit"):
        return f"manual close ({'win' if pnl_per_unit > 0 else 'loss'})"
    if exit_reason and exit_reason.startswith("broker_"):
        return f"{exit_reason.replace('_', ' ')} ({'win' if pnl_per_unit > 0 else 'loss'})"
    return exit_reason or "unknown exit"


def check_trigger_consistency(setup_type, trigger_context):
    """Self-learning groundwork, step 3, part 1: re-derive each setup
    type's own firing condition from its logged trigger_context and
    check it actually held. monitor.py's check_*() functions already
    gate on these exact conditions before ever constructing the alert
    (see e.g. check_triple_ma()'s `if fast > med > slow`), so this
    should essentially never fire in practice -- if it ever does, that
    is a real, high-confidence bug signal (the bot logged a setup type
    whose own defining condition the logged numbers contradict), not
    a guess about market behavior. Returns None when nothing's wrong
    (the overwhelmingly common case) or a string describing exactly
    what's inconsistent.

    trigger_context values are rounded (see monitor.py's trigger_context
    construction, e.g. round(fast_ema, 6)) so a razor-thin equality
    case could theoretically read as a false positive after rounding --
    accepted as a rare, low-cost risk given how many decimal places
    survive."""
    if not trigger_context:
        return None
    tc = trigger_context

    if setup_type == "triple_ma_long":
        f, m, s = tc.get("fast_ema"), tc.get("med_ema"), tc.get("slow_ema")
        if None not in (f, m, s) and not (f > m > s):
            return f"fired as triple_ma_long but logged EMAs ({f}/{m}/{s}) aren't fast>med>slow"
    elif setup_type == "triple_ma_short":
        f, m, s = tc.get("fast_ema"), tc.get("med_ema"), tc.get("slow_ema")
        if None not in (f, m, s) and not (f < m < s):
            return f"fired as triple_ma_short but logged EMAs ({f}/{m}/{s}) aren't fast<med<slow"
    elif setup_type == "dmi_dpo_long":
        p, mn = tc.get("plus_di"), tc.get("minus_di")
        if p is not None and mn is not None and not (p > mn):
            return f"fired as dmi_dpo_long but logged +DI {p} isn't > -DI {mn}"
    elif setup_type == "dmi_dpo_short":
        p, mn = tc.get("plus_di"), tc.get("minus_di")
        if p is not None and mn is not None and not (mn > p):
            return f"fired as dmi_dpo_short but logged -DI {mn} isn't > +DI {p}"
    elif setup_type in ("range_long_rejection", "range_short_rejection"):
        adx = tc.get("adx")
        if adx is not None and adx > 25:
            return f"range rejection fired with ADX {adx} > 25 -- should be gated to a ranging regime only"

    return None


def diagnose_loss(setup_type, entry, stop, pnl_per_unit, exit_reason, trigger_context, overshoot_multiple=1.5):
    """Self-learning groundwork, step 3, part 2: for a losing trade, was
    this a genuine bot-side issue or did the market simply move opposite
    to a validly-fired setup? Two independent, mechanically-grounded
    checks (not a guess at market sentiment, which the logged data can't
    support):
      1. Internal consistency (check_trigger_consistency() above) -- did
         the setup actually meet its own firing condition? If not, real
         bug, high confidence.
      2. Stop overshoot -- for a stop_hit exit, does the realized loss
         exceed the intended risk (entry-to-stop distance) by more than
         overshoot_multiple? check_open() resolves against bar closes,
         not tick-by-tick, so a fast/gappy move can blow through the
         stop level before the bot's next check -- a real market-
         violence event, but also a known limitation of bar-close
         simulation rather than the entry call itself being wrong.
    Anything that clears both checks defaults to "market_opposite": the
    setup fired exactly as designed and simply predicted the wrong
    direction this time -- normal strategy variance, not a mistake."""
    consistency_issue = check_trigger_consistency(setup_type, trigger_context)
    if consistency_issue:
        return {"category": "bot_mistake", "detail": f"logic inconsistency -- {consistency_issue}"}

    if exit_reason == "stop_hit" and entry is not None and stop is not None:
        intended_risk = abs(entry - stop)
        actual_loss = abs(pnl_per_unit)
        if intended_risk > 0 and actual_loss > intended_risk * overshoot_multiple:
            ratio = actual_loss / intended_risk
            return {
                "category": "stop_overshoot",
                "detail": f"intended risk {intended_risk:,.4g}/unit, actual loss {actual_loss:,.4g}/unit ({ratio:.1f}x) -- price moved past the stop faster than the bot's bar-close check could exit; a violent move against the position, amplified by simulation lag rather than a bad entry call",
            }

    return {
        "category": "market_opposite",
        "detail": "no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)",
    }


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
    that change have no "surfaced" field and default to counted. If
    market has an entry in STRATEGY_LAUNCHED_AT, entries fired before
    that cutoff are excluded too -- otherwise a strategy that changed
    mid-day would have its numbers diluted by a superseded strategy's
    results on the very day it shipped."""
    day_ist = day_ist or (datetime.now(timezone.utc) + IST_OFFSET).strftime("%Y-%m-%d")
    log = [e for e in state.get(log_key, []) if to_ist_date(e["fired_at"]) == day_ist and e.get("surfaced", True)]
    if market:
        log = [e for e in log if market_of(e["symbol"]) == market]
        launched_at = STRATEGY_LAUNCHED_AT.get(market)
        if launched_at:
            log = [e for e in log if e["fired_at"] >= launched_at]

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


WHY_REPORT_FILE = os.path.join(os.path.dirname(__file__), "Trade Why Report.md")
BOT_MISTAKES_FILE = os.path.join(os.path.dirname(__file__), "BOT_MISTAKES.md")


def find_bot_mistakes(state):
    """Self-learning groundwork, step 4 (the closing-the-loop step): scan
    every resolved loss in the ENTIRE setup_log -- not just today -- for
    diagnose_loss() category == "bot_mistake". Unlike market_opposite
    (the setup fired correctly, the market just went the other way) or
    stop_overshoot (a real but structural bar-close-vs-tick-data
    limitation), bot_mistake means the logged trigger_context itself
    contradicts the condition the setup claims to have fired on -- an
    unambiguous logic bug, by construction (see check_trigger_
    consistency()'s docstring for why this should essentially never
    legitimately happen).

    The intent: whenever this list is non-empty, that specific bug gets
    investigated and fixed immediately (the exact setup_type + logged
    trigger_context pinpoints which check_*() function and which
    condition is wrong) -- not queued, not batched, not left for a
    future "someday" cleanup. market_opposite/stop_overshoot losses are
    NOT touched by this process; changing entry/exit logic to reduce
    those needs the same walk-forward backtest discipline every other
    live change in this bot has required (the confidence-gating
    backtest is the standing example of why: a plausible-sounding
    filter that measurably hurt performance once actually tested)."""
    mistakes = []
    for e in state.get("setup_log", []):
        if not e.get("resolved") or not e.get("outcome"):
            continue
        pnl = e["outcome"]["pnl_per_unit"]
        if pnl > 0:
            continue
        d = diagnose_loss(e["type"], e.get("entry"), e.get("stop"), pnl, e["outcome"]["exit_reason"], e.get("trigger_context"))
        if d["category"] == "bot_mistake":
            mistakes.append({
                "symbol": e["symbol"], "type": e["type"], "direction": e["direction"],
                "fired_at": e["fired_at"], "detail": d["detail"], "trigger_context": e.get("trigger_context"),
            })
    return mistakes


def write_bot_mistakes_file(mistakes):
    """Overwritten each run (not appended) -- this file's whole purpose
    is "is there something to fix right now", so it should only ever
    reflect the CURRENT state of the log, not accumulate stale entries
    a past run already got fixed. Kept as its own small file (rather
    than folded into Trade Why Report.md's daily wall of text) so it's
    impossible to miss: empty/absent means clean, present with content
    means stop and look."""
    if not mistakes:
        if os.path.exists(BOT_MISTAKES_FILE):
            os.remove(BOT_MISTAKES_FILE)
        return
    lines = [
        "# Bot Mistakes Detected",
        "",
        f"{len(mistakes)} logic inconsistency/inconsistencies found -- the logged trigger_context "
        "contradicts the condition the setup claims to have fired on. This is a real bug, not "
        "normal strategy variance. Investigate and fix immediately; see check_trigger_consistency() "
        "in report.py for the exact check that flagged each one.",
        "",
    ]
    for m in mistakes:
        lines.append(f"## {m['symbol']} {m['type']} ({m['direction']}) -- fired {m['fired_at']}")
        lines.append(f"- {m['detail']}")
        lines.append(f"- trigger_context: {m['trigger_context']}")
        lines.append("")
    with open(BOT_MISTAKES_FILE, "w") as f:
        f.write("\n".join(lines))


def build_why_report(state, label, day_ist, market=None):
    """Self-learning groundwork, step 2 (see explain_trigger()/
    explain_outcome() above): for every setup that fired on this IST
    calendar day, why did it fire, and why did it win or lose? Separate
    report from build_daily_report()'s "would I be up or down" number --
    this one is file-only (see append_why_report_to_file()), never sent
    to Telegram, since it's meant to be read/reviewed at leisure, not
    pushed as an alert.

    Deliberately NOT filtered to surfaced==True the way
    build_daily_report() is -- build_daily_report() answers "what did
    the user actually see suggested", but this report is about the
    bot's underlying signal logic itself, so every setup that fired
    (surfaced or shadow-only) is in scope."""
    log = [e for e in state.get("setup_log", []) if to_ist_date(e["fired_at"]) == day_ist]
    if market:
        log = [e for e in log if market_of(e["symbol"]) == market]

    if not log:
        return f"**{label}** ({day_ist})\nNo setups fired."

    resolved = [e for e in log if e["resolved"]]
    pending = [e for e in log if not e["resolved"]]
    lines = [f"**{label}** ({day_ist})",
              f"- Fired: {len(log)} | Resolved: {len(resolved)} | Still open: {len(pending)}"]

    for e in resolved:
        pnl = e["outcome"]["pnl_per_unit"]
        mark = "WIN" if pnl > 0 else "LOSS"
        pnl_suffix = f" ({e['outcome']['pnl_total']:+,.4g})" if e["outcome"].get("pnl_total") is not None else ""
        lines.append(f"\n[{mark}] {e['symbol']} {e['type']} ({e['direction']}){pnl_suffix}")
        lines.append(f"  Triggered: {explain_trigger(e['type'], e.get('trigger_context'))}")
        lines.append(f"  Outcome:   {explain_outcome(e['outcome']['exit_reason'], pnl)}")
        if pnl <= 0:
            diagnosis = diagnose_loss(e["type"], e.get("entry"), e.get("stop"), pnl, e["outcome"]["exit_reason"], e.get("trigger_context"))
            label_map = {"bot_mistake": "BOT MISTAKE", "stop_overshoot": "STOP OVERSHOOT", "market_opposite": "market read wrong"}
            lines.append(f"  Diagnosis: [{label_map[diagnosis['category']]}] {diagnosis['detail']}")

    if pending:
        lines.append("\nStill open (too soon to say why it worked or not):")
        for e in pending:
            lines.append(f"  {e['symbol']} {e['type']} ({e['direction']}) -- triggered: {explain_trigger(e['type'], e.get('trigger_context'))}")

    return "\n".join(lines)


def append_why_report_to_file(report_text):
    ist_now = datetime.now(timezone.utc) + IST_OFFSET
    header = f"## {ist_now.strftime('%Y-%m-%d %H:%M')} IST\n\n"
    entry = header + report_text + "\n\n---\n\n"

    if not os.path.exists(WHY_REPORT_FILE):
        with open(WHY_REPORT_FILE, "w") as f:
            f.write(
                "# Trade Why Report\n\n"
                "Per-setup breakdown of why each fired setup fired (trigger_context: the "
                "specific indicator values behind that entry) and why it won or lost "
                "(outcome: trail-locked win vs real stop-loss vs clean target/manual exit). "
                "File-only, never sent to Telegram -- appended nightly at 12:00 AM IST "
                "alongside Trade Results.md. Entries fired before trigger_context tracking "
                "started show no trigger detail.\n\n---\n\n"
            )

    with open(WHY_REPORT_FILE, "a") as f:
        f.write(entry)


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
    ist_now = datetime.now(timezone.utc) + IST_OFFSET

    # The nightly cron fires right at 00:00 IST -- at that instant "today"
    # (IST calendar day) has existed for seconds, so scoping to "today"
    # always produces an empty report ("No setups fired today", every
    # single night). What the nightly run actually means to summarize is
    # the day that JUST ENDED. Heuristic: before 6 AM IST, this is either
    # the scheduled midnight run or someone manually checking in that dead
    # window -- either way "yesterday" is the day with anything to show.
    # From 6 AM onward, a manual on-demand check should keep showing the
    # current in-progress day, same as it always has during the day.
    if ist_now.hour < 6:
        day_ist = (ist_now - timedelta(days=1)).strftime("%Y-%m-%d")
    else:
        day_ist = ist_now.strftime("%Y-%m-%d")

    sections = [
        build_daily_report(state, label="INDIA -- SIGNAL QUALITY", market="india", day_ist=day_ist),
        build_daily_report(state, label="CRYPTO -- SIGNAL QUALITY", market="crypto", day_ist=day_ist),
        build_daily_report(state, label="US -- SIGNAL QUALITY", market="us", day_ist=day_ist),
    ]
    # India futures (NIFTY/SENSEX) aren't scanned by the automated pipeline
    # -- no scriptable intraday data source exists, so they're tracked
    # manually (TradingView, checked by hand) and logged into the same
    # setup_log. Only shown when there's actually something logged today,
    # unlike the always-on markets above, since most days will have none.
    futures_today = [e for e in state.get("setup_log", [])
                      if market_of(e["symbol"]) == "india_futures" and to_ist_date(e["fired_at"]) == day_ist]
    if futures_today:
        sections.append(build_daily_report(state, label="INDIA FUTURES (MANUAL) -- SIGNAL QUALITY", market="india_futures", day_ist=day_ist))

    report_text = "\n\n".join(sections)
    append_to_file(report_text)
    monitor.send_telegram("TRADE PERFORMANCE REPORT\n\n" + report_text)

    # File-only companion report (see build_why_report()'s docstring) --
    # never sent to Telegram, deliberately.
    why_sections = [
        build_why_report(state, "INDIA -- WHY", day_ist, market="india"),
        build_why_report(state, "CRYPTO -- WHY", day_ist, market="crypto"),
        build_why_report(state, "US -- WHY", day_ist, market="us"),
    ]
    if futures_today:
        why_sections.append(build_why_report(state, "INDIA FUTURES (MANUAL) -- WHY", day_ist, market="india_futures"))
    append_why_report_to_file("\n\n".join(why_sections))

    # Self-learning groundwork, step 4 -- see find_bot_mistakes()'s
    # docstring. Checked against the WHOLE log every run (not just
    # today) so a bug never goes unnoticed just because the run that
    # would have caught it got skipped. Loud stdout print too, not just
    # the file -- surfaces in the GitHub Actions run log immediately,
    # before anyone has to think to go open BOT_MISTAKES.md.
    mistakes = find_bot_mistakes(state)
    write_bot_mistakes_file(mistakes)
    if mistakes:
        print(f"!!! {len(mistakes)} BOT MISTAKE(S) DETECTED -- see BOT_MISTAKES.md -- fix immediately, this is a real logic bug !!!")


if __name__ == "__main__":
    sys.exit(main())
