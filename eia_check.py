#!/usr/bin/env python3
"""Fetches the real EIA weekly natural gas storage report (free bulk
download, no API key -- confirmed working directly) and computes this
week's storage "surprise" vs. the seasonal norm (same ISO week, prior
5 years) -- the exact methodology validated in the commodity strategy
review (real 2012-2026 backtest: correlation near zero on small
surprises, but a genuine out-of-sample-holding edge when combined with
seasonality and required as a confirmation gate, not an optional one).

Runs weekly, gated by wall-clock time in the workflow (the report only
updates Thursdays ~10:30am ET) -- same reasoning as the opening-range
scans: no point re-downloading a 4.4MB file that hasn't changed.

Saves into state["eia_ng_surprise"] = {"date", "surprise_bcf",
"fetched_at"} -- consumed by check_watching_commodity() as a REQUIRED
gate for NG=F's seasonal setup (fails closed if this is missing or
stale, not optional)."""
import io
import subprocess
import sys
import zipfile
from datetime import datetime, timezone

import monitor

SERIES_ID = "NG.NW2_EPG0_SWO_R48_BCF.W"  # Weekly Lower 48 States Natural Gas Working Underground Storage
BULK_URL = "https://api.eia.gov/bulk/NG.zip"
SEASONAL_LOOKBACK_YEARS = 5
# Staleness is enforced on the READ side, in monitor.py's
# check_watching_commodity() (EIA_STALE_DAYS) -- not here, since this
# script only ever writes a fresh fetch when it runs at all.


def fetch_bulk_zip():
    raw = subprocess.run(["curl", "-sL", "--max-time", "60", BULK_URL], capture_output=True, check=True).stdout
    with zipfile.ZipFile(io.BytesIO(raw)) as zf:
        with zf.open("NG.txt") as f:
            for line in f:
                if SERIES_ID.encode() in line:
                    import json
                    return json.loads(line)
    return None


def compute_surprise(series_json):
    import json
    data = series_json["data"]  # [["20260821", 3184], ...], newest first
    parsed = [(datetime.strptime(d, "%Y%m%d"), v) for d, v in data]
    parsed.sort(key=lambda x: x[0])

    latest_date, latest_val = parsed[-1]
    prev_val = parsed[-2][1] if len(parsed) >= 2 else None
    if prev_val is None:
        return None
    change_bcf = latest_val - prev_val

    latest_week = latest_date.isocalendar()[1]
    window_start = latest_date.replace(year=latest_date.year - SEASONAL_LOOKBACK_YEARS)
    same_week_changes = []
    for i in range(1, len(parsed)):
        d, v = parsed[i]
        if d >= latest_date or d < window_start:
            continue
        if d.isocalendar()[1] == latest_week:
            same_week_changes.append(v - parsed[i - 1][1])
    if len(same_week_changes) < 2:
        return None
    seasonal_expected = sum(same_week_changes) / len(same_week_changes)
    surprise = change_bcf - seasonal_expected
    return {
        "date": latest_date.date().isoformat(),
        "change_bcf": change_bcf,
        "seasonal_expected_bcf": round(seasonal_expected, 1),
        "surprise_bcf": round(surprise, 1),
    }


def main():
    try:
        series = fetch_bulk_zip()
    except Exception as e:
        print(f"EIA bulk fetch failed: {e}")
        return 1
    if series is None:
        print("Series not found in EIA bulk file.")
        return 1

    result = compute_surprise(series)
    if result is None:
        print("Not enough history to compute a seasonal surprise.")
        return 1

    state = monitor.load_state()
    result["fetched_at"] = datetime.now(timezone.utc).isoformat()
    state["eia_ng_surprise"] = result
    monitor.save_state(state)
    print(f"EIA NG storage: {result['date']} change={result['change_bcf']:+.0f} Bcf "
          f"seasonal_expected={result['seasonal_expected_bcf']:+.1f} Bcf "
          f"surprise={result['surprise_bcf']:+.1f} Bcf")
    return 0


if __name__ == "__main__":
    sys.exit(main())
