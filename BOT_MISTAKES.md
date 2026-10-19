# Bot Mistakes Detected

1 logic inconsistency/inconsistencies found -- the logged trigger_context contradicts the condition the setup claims to have fired on. This is a real bug, not normal strategy variance. Investigate and fix immediately; see check_trigger_consistency() in report.py for the exact check that flagged each one.

## FET-USD triple_ma_long (long) -- fired 2026-10-19T16:31:09.503106+00:00
- logic inconsistency -- fired as triple_ma_long but logged EMAs (0.18984/0.189609/0.189609) aren't fast>med>slow
- trigger_context: {'fast_ema': 0.18984, 'med_ema': 0.189609, 'slow_ema': 0.189609, 'periods': {'fast': 8, 'med': 16, 'slow': 25}}
