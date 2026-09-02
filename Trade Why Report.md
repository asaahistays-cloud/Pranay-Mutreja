# Trade Why Report

Per-setup breakdown of why each fired setup fired (trigger_context: the specific indicator values behind that entry) and why it won or lost (outcome: trail-locked win vs real stop-loss vs clean target/manual exit). File-only, never sent to Telegram -- appended nightly at 12:00 AM IST alongside Trade Results.md. Entries fired before trigger_context tracking started show no trigger detail.

---

## 2026-09-01 08:38 IST

**INDIA -- WHY** (2026-09-01)
No setups fired.

**CRYPTO -- WHY** (2026-09-01)
- Fired: 9 | Resolved: 5 | Still open: 4

[LOSS] AVAX-USD triple_threat_long (long) (-59.77)
  Triggered: no trigger detail logged (fired before trigger_context tracking started)
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] FET-USD triple_threat_long (long) (+40.59)
  Triggered: no trigger detail logged (fired before trigger_context tracking started)
  Outcome:   trend_reversed

[LOSS] FET-USD triple_ma_short (short) (-100.7)
  Triggered: no trigger detail logged (fired before trigger_context tracking started)
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] AVAX-USD triple_threat_long (long) (-59.77)
  Triggered: no trigger detail logged (fired before trigger_context tracking started)
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] FET-USD triple_ma_long (long) (+44.54)
  Triggered: no trigger detail logged (fired before trigger_context tracking started)
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

Still open (too soon to say why it worked or not):
  BTC-USD triple_ma_short (short) -- triggered: EMA(8/16/25) = 7.84e+04/7.85e+04/7.857e+04, freshly aligned
  ETH-USD triple_ma_short (short) -- triggered: EMA(8/16/25) = 2,463/2,466/2,467, freshly aligned
  SOL-USD triple_ma_short (short) -- triggered: EMA(8/16/25) = 103.1/103.2/103.2, freshly aligned
  XRP-USD triple_ma_short (short) -- triggered: EMA(8/16/25) = 1.376/1.378/1.38, freshly aligned

**US -- WHY** (2026-09-01)
- Fired: 3 | Resolved: 2 | Still open: 1

[LOSS] HOOD triple_ma_long (long) (-65.49)
  Triggered: no trigger detail logged (fired before trigger_context tracking started)
  Outcome:   eod_settlement
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] AAL triple_ma_short (short) (+61.3)
  Triggered: no trigger detail logged (fired before trigger_context tracking started)
  Outcome:   eod_settlement

Still open (too soon to say why it worked or not):
  GC=F seasonal_short (short) -- triggered: month 9 seasonal edge

---

## 2026-09-02 00:00 IST

**INDIA -- WHY** (2026-09-01)
- Fired: 79 | Resolved: 71 | Still open: 8

[WIN] JSWENERGY.NS triple_ma_short (short) (+2,309)
  Triggered: EMA(8/16/25) = 527.2/528.5/529.5, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] VEDL.NS triple_ma_short (short) (+0)
  Triggered: EMA(8/16/25) = 279.2/279.2/279.6, freshly aligned
  Outcome:   trend_reversed
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] JPPOWER.NS triple_ma_long (long) (-1,880)
  Triggered: EMA(8/16/25) = 16.68/16.65/16.65, freshly aligned
  Outcome:   trend_reversed
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] IOC.NS triple_ma_long (long) (-527.9)
  Triggered: EMA(8/16/25) = 135.8/135.4/135.4, freshly aligned
  Outcome:   trend_reversed
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] JSWENERGY.NS triple_ma_short (short) (+1,391)
  Triggered: EMA(8/16/25) = 524.4/526.8/528.3, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] IDEA.NS triple_ma_short (short) (+1,005)
  Triggered: EMA(8/16/25) = 14.59/14.65/14.68, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] GMRAIRPORT.NS triple_ma_short (short) (-1,514)
  Triggered: EMA(8/16/25) = 94.88/95.44/95.9, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] NHPC.NS triple_ma_long (long) (+702.1)
  Triggered: EMA(8/16/25) = 75.42/75.14/75.04, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] UNIONBANK.NS triple_ma_long (long) (+1,361)
  Triggered: EMA(8/16/25) = 184.7/184.2/184, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] POWERGRID.NS triple_ma_short (short) (-1,611)
  Triggered: EMA(8/16/25) = 263.7/264.2/264.4, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] INDIANB.NS triple_ma_long (long) (-2,620)
  Triggered: EMA(8/16/25) = 880.8/877.2/875.9, freshly aligned
  Outcome:   trend_reversed
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] SUZLON.NS triple_ma_long (long) (+1,141)
  Triggered: EMA(8/16/25) = 46.58/46.42/46.38, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] PFC.NS triple_ma_short (short) (-1,304)
  Triggered: EMA(8/16/25) = 345.1/346.3/347.2, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] ETERNAL.NS triple_ma_short (short) (-158.2)
  Triggered: EMA(8/16/25) = 324.6/324.8/325.2, freshly aligned
  Outcome:   trend_reversed
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] JSWENERGY.NS triple_ma_short (short) (-2,034)
  Triggered: EMA(8/16/25) = 522.3/525.4/527.3, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] IDEA.NS triple_ma_short (short) (+875)
  Triggered: EMA(8/16/25) = 14.56/14.63/14.67, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] NHPC.NS triple_ma_long (long) (+864.9)
  Triggered: EMA(8/16/25) = 75.47/75.2/75.09, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] GMRAIRPORT.NS triple_ma_short (short) (-2,310)
  Triggered: EMA(8/16/25) = 94.69/95.27/95.76, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] INDIANB.NS triple_ma_long (long) (-2,644)
  Triggered: EMA(8/16/25) = 881.5/878/876.5, freshly aligned
  Outcome:   trend_reversed
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] POWERGRID.NS triple_ma_short (short) (+761.4)
  Triggered: EMA(8/16/25) = 263.5/264/264.3, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] IOC.NS triple_ma_long (long) (+782.5)
  Triggered: EMA(8/16/25) = 135.9/135.5/135.5, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] PFC.NS triple_ma_short (short) (-1,992)
  Triggered: EMA(8/16/25) = 344.8/346/347, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] UNIONBANK.NS triple_ma_long (long) (+1,037)
  Triggered: EMA(8/16/25) = 184.9/184.3/184.1, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] SUZLON.NS triple_ma_long (long) (+992.3)
  Triggered: EMA(8/16/25) = 46.6/46.45/46.41, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] BANKINDIA.NS triple_ma_short (short) (+563.9)
  Triggered: EMA(8/16/25) = 142.2/142.3/142.4, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] TATAPOWER.NS triple_ma_short (short) (-2,085)
  Triggered: EMA(8/16/25) = 348.3/348.5/348.8, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] JSWENERGY.NS triple_ma_short (short) (-1,830)
  Triggered: EMA(8/16/25) = 522.4/525.5/527.3, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] IDEA.NS triple_ma_short (short) (+1,144)
  Triggered: EMA(8/16/25) = 14.56/14.63/14.67, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] GMRAIRPORT.NS triple_ma_short (short) (-2,313)
  Triggered: EMA(8/16/25) = 94.68/95.27/95.75, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] NHPC.NS triple_ma_long (long) (+764.2)
  Triggered: EMA(8/16/25) = 75.47/75.2/75.09, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] JPPOWER.NS triple_ma_long (long) (-557.8)
  Triggered: EMA(8/16/25) = 16.66/16.64/16.64, freshly aligned
  Outcome:   trend_reversed
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] POWERGRID.NS triple_ma_short (short) (+951.3)
  Triggered: EMA(8/16/25) = 263.5/264/264.3, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] INDIANB.NS triple_ma_long (long) (+1,297)
  Triggered: EMA(8/16/25) = 881.2/877.8/876.4, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] BANKINDIA.NS triple_ma_short (short) (-1,446)
  Triggered: EMA(8/16/25) = 142.2/142.3/142.4, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] PFC.NS triple_ma_short (short) (-1,822)
  Triggered: EMA(8/16/25) = 344.9/346/347, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] SUZLON.NS triple_ma_long (long) (+992.3)
  Triggered: EMA(8/16/25) = 46.6/46.45/46.41, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] IOC.NS triple_ma_long (long) (+747.9)
  Triggered: EMA(8/16/25) = 135.9/135.5/135.5, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] UNIONBANK.NS triple_ma_long (long) (+1,548)
  Triggered: EMA(8/16/25) = 184.8/184.3/184.1, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] JSWENERGY.NS triple_ma_short (short) (-1,658)
  Triggered: EMA(8/16/25) = 522.5/525.5/527.4, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] IDEA.NS triple_ma_short (short) (+0)
  Triggered: EMA(8/16/25) = 14.55/14.62/14.66, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] GMRAIRPORT.NS triple_ma_short (short) (-2,661)
  Triggered: EMA(8/16/25) = 94.63/95.24/95.74, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] NHPC.NS triple_ma_long (long) (+868.2)
  Triggered: EMA(8/16/25) = 75.46/75.19/75.08, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] POWERGRID.NS triple_ma_short (short) (-2,234)
  Triggered: EMA(8/16/25) = 263.4/263.9/264.2, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] INDIANB.NS triple_ma_long (long) (-2,203)
  Triggered: EMA(8/16/25) = 881.2/877.8/876.4, freshly aligned
  Outcome:   trend_reversed
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] PFC.NS triple_ma_short (short) (-1,937)
  Triggered: EMA(8/16/25) = 344.8/346/346.9, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] BANKINDIA.NS triple_ma_short (short) (-1,977)
  Triggered: EMA(8/16/25) = 142.1/142.3/142.4, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] IOC.NS triple_ma_long (long) (+922.7)
  Triggered: EMA(8/16/25) = 135.9/135.5/135.5, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] BHEL.NS triple_ma_long (long) (+1,136)
  Triggered: EMA(8/16/25) = 431.6/431/430.4, freshly aligned
  Outcome:   trend_reversed

[WIN] UNIONBANK.NS triple_ma_long (long) (+1,634)
  Triggered: EMA(8/16/25) = 184.8/184.3/184.1, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] TATAPOWER.NS triple_ma_short (short) (-2,374)
  Triggered: EMA(8/16/25) = 348.2/348.5/348.8, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] SUZLON.NS triple_ma_long (long) (+923.5)
  Triggered: EMA(8/16/25) = 46.59/46.44/46.4, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] JPPOWER.NS triple_ma_long (long) (-1,346)
  Triggered: EMA(8/16/25) = 16.67/16.65/16.65, freshly aligned
  Outcome:   trend_reversed
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] ETERNAL.NS triple_ma_long (long) (+795.5)
  Triggered: EMA(8/16/25) = 326.3/325.8/325.7, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] BHEL.NS triple_ma_long (long) (-769.2)
  Triggered: EMA(8/16/25) = 430.8/430.7/430.4, freshly aligned
  Outcome:   trend_reversed
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] TATAPOWER.NS triple_ma_long (long) (+0)
  Triggered: EMA(8/16/25) = 350/349.5/349.4, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] BANKINDIA.NS triple_ma_long (long) (-1,604)
  Triggered: EMA(8/16/25) = 142.7/142.5/142.5, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] ETERNAL.NS breakout_long (long) (-456.6)
  Triggered: broke range high 328.5 on vol 826,929 vs avg 657,565, trend EMA 327; India gate: RSI 61.32 / VWAP 326.6 (rsi>60 and close>=vwap)
  Outcome:   trend_reversed
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] JPPOWER.NS triple_ma_short (short) (+1,957)
  Triggered: EMA(8/16/25) = 16.64/16.64/16.64, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] BHEL.NS triple_ma_short (short) (+877)
  Triggered: EMA(8/16/25) = 429.5/430/430, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] BHEL.NS breakdown_short (short) (+1,114)
  Triggered: broke range low 427.4 on vol 233,413 vs avg 198,881, trend EMA 429.5; India gate: RSI 23.77 / VWAP 430.5 (rsi<40 and close<=vwap)
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] IDEA.NS breakdown_short (short) (+3,876)
  Triggered: broke range low 14.24 on vol 13,885,330 vs avg 6,050,337, trend EMA 14.31; India gate: RSI 28.26 / VWAP 14.4 (rsi<40 and close<=vwap)
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] IDEA.NS breakdown_short (short) (+1,767)
  Triggered: broke range low 14.17 on vol 10,100,000 vs avg 7,054,972, trend EMA 14.28; India gate: RSI 29.55 / VWAP 14.39 (rsi<40 and close<=vwap)
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] BHEL.NS breakdown_short (short) (-822.8)
  Triggered: broke range low 425.6 on vol 236,615 vs avg 168,048, trend EMA 428; India gate: RSI 23.03 / VWAP 430 (rsi<40 and close<=vwap)
  Outcome:   trend_reversed
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] BANKINDIA.NS triple_ma_short (short) (-1,411)
  Triggered: EMA(8/16/25) = 142.4/142.5/142.5, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] IDEA.NS breakdown_short (short) (-2,498)
  Triggered: broke range low 14.06 on vol 21,549,128 vs avg 7,805,167, trend EMA 14.21; India gate: RSI 14.0 / VWAP 14.33 (rsi<40 and close<=vwap)
  Outcome:   trend_reversed
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] UNIONBANK.NS triple_ma_short (short) (-2,671)
  Triggered: EMA(8/16/25) = 184.3/184.6/184.7, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] TATAPOWER.NS triple_ma_long (long) (-285.6)
  Triggered: EMA(8/16/25) = 350.3/350.3/350.2, freshly aligned
  Outcome:   trend_reversed
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] SUZLON.NS triple_ma_short (short) (+0)
  Triggered: EMA(8/16/25) = 46.52/46.56/46.56, freshly aligned
  Outcome:   eod_settlement
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] ETERNAL.NS triple_ma_long (long) (-1,376)
  Triggered: EMA(8/16/25) = 326.6/326.6/326.5, freshly aligned
  Outcome:   trend_reversed
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] PFC.NS triple_ma_short (short) (-72.58)
  Triggered: EMA(8/16/25) = 345.3/345.5/345.7, freshly aligned
  Outcome:   eod_settlement
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] INDIANB.NS triple_ma_short (short) (-1,428)
  Triggered: EMA(8/16/25) = 878.5/879.9/879.9, freshly aligned
  Outcome:   eod_settlement
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

Still open (too soon to say why it worked or not):
  NMDC.NS triple_ma_long (long) -- triggered: EMA(8/16/25) = 86.62/86.29/86.18, freshly aligned
  HINDCOPPER.NS triple_threat_long (long) -- triggered: RSI 48->75 crossed 50, broke 528.8, trend EMA 528
  RPOWER.NS triple_threat_long (long) -- triggered: RSI 41->75 crossed 50, broke 22.2, trend EMA 22.2
  PNB.NS triple_ma_long (long) -- triggered: EMA(8/16/25) = 114.6/114.5/114.5, freshly aligned
  SAIL.NS triple_ma_short (short) -- triggered: EMA(8/16/25) = 197.3/197.4/197.4, freshly aligned
  IRCON.NS triple_ma_short (short) -- triggered: EMA(8/16/25) = 119.8/120.2/120.5, freshly aligned
  COALINDIA.NS triple_ma_long (long) -- triggered: EMA(8/16/25) = 402.9/402.2/401.9, freshly aligned
  PAYTM.NS triple_ma_long (long) -- triggered: EMA(8/16/25) = 1,674/1,671/1,669, freshly aligned

**CRYPTO -- WHY** (2026-09-01)
- Fired: 30 | Resolved: 27 | Still open: 3

[LOSS] AVAX-USD triple_threat_long (long) (-59.77)
  Triggered: no trigger detail logged (fired before trigger_context tracking started)
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] FET-USD triple_threat_long (long) (+40.59)
  Triggered: no trigger detail logged (fired before trigger_context tracking started)
  Outcome:   trend_reversed

[LOSS] FET-USD triple_ma_short (short) (-100.7)
  Triggered: no trigger detail logged (fired before trigger_context tracking started)
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] AVAX-USD triple_threat_long (long) (-59.77)
  Triggered: no trigger detail logged (fired before trigger_context tracking started)
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] FET-USD triple_ma_long (long) (+44.54)
  Triggered: no trigger detail logged (fired before trigger_context tracking started)
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] BTC-USD triple_ma_short (short) (-106.2)
  Triggered: EMA(8/16/25) = 7.84e+04/7.85e+04/7.857e+04, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] ETH-USD triple_ma_short (short) (-93.95)
  Triggered: EMA(8/16/25) = 2,463/2,466/2,467, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] SOL-USD triple_ma_short (short) (-43.81)
  Triggered: EMA(8/16/25) = 103.1/103.2/103.2, freshly aligned
  Outcome:   trend_reversed
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] XRP-USD triple_ma_short (short) (-52.66)
  Triggered: EMA(8/16/25) = 1.376/1.378/1.38, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] ETH-USD triple_ma_long (long) (+21.43)
  Triggered: EMA(8/16/25) = 2,470/2,469/2,469, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] BTC-USD triple_ma_long (long) (+33.28)
  Triggered: EMA(8/16/25) = 7.869e+04/7.863e+04/7.862e+04, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] NEAR-USD dmi_dpo_long (long) (-72.27)
  Triggered: +DI 29.11 vs -DI 14.99, ADX 23.53, DPO 0.000416 (period 50)
  Outcome:   trend_reversed
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] NEAR-USD dmi_dpo_long (long) (-52.39)
  Triggered: +DI 27.68 vs -DI 17.94, ADX 24.42, DPO 0.00012 (period 50)
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] SOL-USD triple_ma_short (short) (+117.9)
  Triggered: EMA(8/16/25) = 103.4/103.5/103.5, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] BTC-USD triple_ma_short (short) (+35.44)
  Triggered: EMA(8/16/25) = 7.863e+04/7.869e+04/7.87e+04, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] XRP-USD triple_ma_short (short) (+35.42)
  Triggered: EMA(8/16/25) = 1.381/1.383/1.383, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] AVAX-USD triple_threat_short (short) (-45.74)
  Triggered: RSI 51->41 crossed 50, broke 7.25, trend EMA 7.278
  Outcome:   trend_reversed
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] ETH-USD triple_ma_short (short) (-11.12)
  Triggered: EMA(8/16/25) = 2,466/2,469/2,470, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] NEAR-USD triple_ma_short (short) (+21.54)
  Triggered: EMA(8/16/25) = 1.938/1.945/1.946, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] FET-USD triple_ma_short (short) (+50.92)
  Triggered: EMA(8/16/25) = 0.155/0.1557/0.1558, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] AVAX-USD triple_ma_short (short) (-92.41)
  Triggered: EMA(8/16/25) = 7.259/7.272/7.273, freshly aligned
  Outcome:   trend_reversed
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] NEAR-USD dmi_dpo_long (long) (-6.022)
  Triggered: +DI 23.02 vs -DI 21.54, ADX 23.79, DPO 0.02187 (period 50)
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] XRP-USD triple_ma_short (short) (-42.69)
  Triggered: EMA(8/16/25) = 1.376/1.376/1.376, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] ETH-USD community_idea (short) (-134.9)
  Triggered: no trigger detail logged (fired before trigger_context tracking started)
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] BTC-USD triple_ma_short (short) (+42.94)
  Triggered: EMA(8/16/25) = 7.8e+04/7.803e+04/7.807e+04, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] XRP-USD triple_ma_short (short) (-47.16)
  Triggered: EMA(8/16/25) = 1.374/1.374/1.375, freshly aligned
  Outcome:   trend_reversed
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] FET-USD triple_ma_short (short) (+25.9)
  Triggered: EMA(8/16/25) = 0.1539/0.1539/0.154, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

Still open (too soon to say why it worked or not):
  XRP-USD triple_ma_short (short) -- triggered: EMA(8/16/25) = 1.375/1.375/1.375, freshly aligned
  AVAX-USD triple_ma_short (short) -- triggered: EMA(8/16/25) = 7.27/7.277/7.278, freshly aligned
  NEAR-USD triple_ma_short (short) -- triggered: EMA(8/16/25) = 1.969/1.979/1.979, freshly aligned

**US -- WHY** (2026-09-01)
- Fired: 10 | Resolved: 9 | Still open: 1

[LOSS] HOOD triple_ma_long (long) (-65.49)
  Triggered: no trigger detail logged (fired before trigger_context tracking started)
  Outcome:   eod_settlement
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] AAL triple_ma_short (short) (+61.3)
  Triggered: no trigger detail logged (fired before trigger_context tracking started)
  Outcome:   eod_settlement

[WIN] GC=F seasonal_short (short) (+0.01103)
  Triggered: month 9 seasonal edge
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] MO community_idea (long) (-114.4)
  Triggered: no trigger detail logged (fired before trigger_context tracking started)
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] MO triple_ma_long (long) (-94.47)
  Triggered: EMA(8/16/25) = 69.33/69.07/68.91, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] MO triple_ma_long (long) (-6.484)
  Triggered: EMA(8/16/25) = 69.32/69.06/68.9, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] CLF triple_ma_long (long) (-178.3)
  Triggered: EMA(8/16/25) = 11.62/11.6/11.6, freshly aligned
  Outcome:   trend_reversed
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] CLF triple_ma_long (long) (+183.5)
  Triggered: EMA(8/16/25) = 11.63/11.61/11.6, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] CLF triple_ma_long (long) (-163.6)
  Triggered: EMA(8/16/25) = 11.64/11.64/11.63, freshly aligned
  Outcome:   trend_reversed
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

Still open (too soon to say why it worked or not):
  GC=F community_idea (short) -- triggered: no trigger detail logged (fired before trigger_context tracking started)

**INDIA FUTURES (MANUAL) -- WHY** (2026-09-01)
- Fired: 6 | Resolved: 6 | Still open: 0

[LOSS] BANKNIFTY-FUT triple_ma_long (long) (-561.6)
  Triggered: EMA(8/16/25) = 5.756e+04/5.755e+04/5.752e+04, freshly aligned
  Outcome:   trend_reversed
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] SENSEX-FUT triple_ma_long (long) (-844.8)
  Triggered: EMA(8/16/25) = 7.712e+04/7.708e+04/7.705e+04, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] NIFTY-FUT triple_ma_long (long) (+74.88)
  Triggered: EMA(8/16/25) = 2.408e+04/2.408e+04/2.408e+04, freshly aligned
  Outcome:   trend_reversed

[LOSS] NIFTY-FUT triple_ma_short (short) (-710.8)
  Triggered: EMA(8/16/25) = 2.406e+04/2.407e+04/2.407e+04, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] BANKNIFTY-FUT triple_ma_short (short) (-1,986)
  Triggered: EMA(8/16/25) = 5.739e+04/5.745e+04/5.746e+04, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] SENSEX-FUT triple_ma_short (short) (+82.41)
  Triggered: EMA(8/16/25) = 7.693e+04/7.698e+04/7.698e+04, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

---

## 2026-09-02 00:12 IST

**INDIA -- WHY** (2026-09-01)
- Fired: 79 | Resolved: 71 | Still open: 8

[WIN] JSWENERGY.NS triple_ma_short (short) (+2,309)
  Triggered: EMA(8/16/25) = 527.2/528.5/529.5, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] VEDL.NS triple_ma_short (short) (+0)
  Triggered: EMA(8/16/25) = 279.2/279.2/279.6, freshly aligned
  Outcome:   trend_reversed
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] JPPOWER.NS triple_ma_long (long) (-1,880)
  Triggered: EMA(8/16/25) = 16.68/16.65/16.65, freshly aligned
  Outcome:   trend_reversed
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] IOC.NS triple_ma_long (long) (-527.9)
  Triggered: EMA(8/16/25) = 135.8/135.4/135.4, freshly aligned
  Outcome:   trend_reversed
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] JSWENERGY.NS triple_ma_short (short) (+1,391)
  Triggered: EMA(8/16/25) = 524.4/526.8/528.3, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] IDEA.NS triple_ma_short (short) (+1,005)
  Triggered: EMA(8/16/25) = 14.59/14.65/14.68, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] GMRAIRPORT.NS triple_ma_short (short) (-1,514)
  Triggered: EMA(8/16/25) = 94.88/95.44/95.9, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] NHPC.NS triple_ma_long (long) (+702.1)
  Triggered: EMA(8/16/25) = 75.42/75.14/75.04, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] UNIONBANK.NS triple_ma_long (long) (+1,361)
  Triggered: EMA(8/16/25) = 184.7/184.2/184, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] POWERGRID.NS triple_ma_short (short) (-1,611)
  Triggered: EMA(8/16/25) = 263.7/264.2/264.4, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] INDIANB.NS triple_ma_long (long) (-2,620)
  Triggered: EMA(8/16/25) = 880.8/877.2/875.9, freshly aligned
  Outcome:   trend_reversed
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] SUZLON.NS triple_ma_long (long) (+1,141)
  Triggered: EMA(8/16/25) = 46.58/46.42/46.38, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] PFC.NS triple_ma_short (short) (-1,304)
  Triggered: EMA(8/16/25) = 345.1/346.3/347.2, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] ETERNAL.NS triple_ma_short (short) (-158.2)
  Triggered: EMA(8/16/25) = 324.6/324.8/325.2, freshly aligned
  Outcome:   trend_reversed
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] JSWENERGY.NS triple_ma_short (short) (-2,034)
  Triggered: EMA(8/16/25) = 522.3/525.4/527.3, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] IDEA.NS triple_ma_short (short) (+875)
  Triggered: EMA(8/16/25) = 14.56/14.63/14.67, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] NHPC.NS triple_ma_long (long) (+864.9)
  Triggered: EMA(8/16/25) = 75.47/75.2/75.09, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] GMRAIRPORT.NS triple_ma_short (short) (-2,310)
  Triggered: EMA(8/16/25) = 94.69/95.27/95.76, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] INDIANB.NS triple_ma_long (long) (-2,644)
  Triggered: EMA(8/16/25) = 881.5/878/876.5, freshly aligned
  Outcome:   trend_reversed
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] POWERGRID.NS triple_ma_short (short) (+761.4)
  Triggered: EMA(8/16/25) = 263.5/264/264.3, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] IOC.NS triple_ma_long (long) (+782.5)
  Triggered: EMA(8/16/25) = 135.9/135.5/135.5, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] PFC.NS triple_ma_short (short) (-1,992)
  Triggered: EMA(8/16/25) = 344.8/346/347, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] UNIONBANK.NS triple_ma_long (long) (+1,037)
  Triggered: EMA(8/16/25) = 184.9/184.3/184.1, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] SUZLON.NS triple_ma_long (long) (+992.3)
  Triggered: EMA(8/16/25) = 46.6/46.45/46.41, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] BANKINDIA.NS triple_ma_short (short) (+563.9)
  Triggered: EMA(8/16/25) = 142.2/142.3/142.4, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] TATAPOWER.NS triple_ma_short (short) (-2,085)
  Triggered: EMA(8/16/25) = 348.3/348.5/348.8, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] JSWENERGY.NS triple_ma_short (short) (-1,830)
  Triggered: EMA(8/16/25) = 522.4/525.5/527.3, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] IDEA.NS triple_ma_short (short) (+1,144)
  Triggered: EMA(8/16/25) = 14.56/14.63/14.67, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] GMRAIRPORT.NS triple_ma_short (short) (-2,313)
  Triggered: EMA(8/16/25) = 94.68/95.27/95.75, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] NHPC.NS triple_ma_long (long) (+764.2)
  Triggered: EMA(8/16/25) = 75.47/75.2/75.09, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] JPPOWER.NS triple_ma_long (long) (-557.8)
  Triggered: EMA(8/16/25) = 16.66/16.64/16.64, freshly aligned
  Outcome:   trend_reversed
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] POWERGRID.NS triple_ma_short (short) (+951.3)
  Triggered: EMA(8/16/25) = 263.5/264/264.3, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] INDIANB.NS triple_ma_long (long) (+1,297)
  Triggered: EMA(8/16/25) = 881.2/877.8/876.4, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] BANKINDIA.NS triple_ma_short (short) (-1,446)
  Triggered: EMA(8/16/25) = 142.2/142.3/142.4, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] PFC.NS triple_ma_short (short) (-1,822)
  Triggered: EMA(8/16/25) = 344.9/346/347, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] SUZLON.NS triple_ma_long (long) (+992.3)
  Triggered: EMA(8/16/25) = 46.6/46.45/46.41, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] IOC.NS triple_ma_long (long) (+747.9)
  Triggered: EMA(8/16/25) = 135.9/135.5/135.5, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] UNIONBANK.NS triple_ma_long (long) (+1,548)
  Triggered: EMA(8/16/25) = 184.8/184.3/184.1, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] JSWENERGY.NS triple_ma_short (short) (-1,658)
  Triggered: EMA(8/16/25) = 522.5/525.5/527.4, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] IDEA.NS triple_ma_short (short) (+0)
  Triggered: EMA(8/16/25) = 14.55/14.62/14.66, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] GMRAIRPORT.NS triple_ma_short (short) (-2,661)
  Triggered: EMA(8/16/25) = 94.63/95.24/95.74, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] NHPC.NS triple_ma_long (long) (+868.2)
  Triggered: EMA(8/16/25) = 75.46/75.19/75.08, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] POWERGRID.NS triple_ma_short (short) (-2,234)
  Triggered: EMA(8/16/25) = 263.4/263.9/264.2, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] INDIANB.NS triple_ma_long (long) (-2,203)
  Triggered: EMA(8/16/25) = 881.2/877.8/876.4, freshly aligned
  Outcome:   trend_reversed
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] PFC.NS triple_ma_short (short) (-1,937)
  Triggered: EMA(8/16/25) = 344.8/346/346.9, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] BANKINDIA.NS triple_ma_short (short) (-1,977)
  Triggered: EMA(8/16/25) = 142.1/142.3/142.4, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] IOC.NS triple_ma_long (long) (+922.7)
  Triggered: EMA(8/16/25) = 135.9/135.5/135.5, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] BHEL.NS triple_ma_long (long) (+1,136)
  Triggered: EMA(8/16/25) = 431.6/431/430.4, freshly aligned
  Outcome:   trend_reversed

[WIN] UNIONBANK.NS triple_ma_long (long) (+1,634)
  Triggered: EMA(8/16/25) = 184.8/184.3/184.1, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] TATAPOWER.NS triple_ma_short (short) (-2,374)
  Triggered: EMA(8/16/25) = 348.2/348.5/348.8, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] SUZLON.NS triple_ma_long (long) (+923.5)
  Triggered: EMA(8/16/25) = 46.59/46.44/46.4, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] JPPOWER.NS triple_ma_long (long) (-1,346)
  Triggered: EMA(8/16/25) = 16.67/16.65/16.65, freshly aligned
  Outcome:   trend_reversed
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] ETERNAL.NS triple_ma_long (long) (+795.5)
  Triggered: EMA(8/16/25) = 326.3/325.8/325.7, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] BHEL.NS triple_ma_long (long) (-769.2)
  Triggered: EMA(8/16/25) = 430.8/430.7/430.4, freshly aligned
  Outcome:   trend_reversed
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] TATAPOWER.NS triple_ma_long (long) (+0)
  Triggered: EMA(8/16/25) = 350/349.5/349.4, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] BANKINDIA.NS triple_ma_long (long) (-1,604)
  Triggered: EMA(8/16/25) = 142.7/142.5/142.5, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] ETERNAL.NS breakout_long (long) (-456.6)
  Triggered: broke range high 328.5 on vol 826,929 vs avg 657,565, trend EMA 327; India gate: RSI 61.32 / VWAP 326.6 (rsi>60 and close>=vwap)
  Outcome:   trend_reversed
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] JPPOWER.NS triple_ma_short (short) (+1,957)
  Triggered: EMA(8/16/25) = 16.64/16.64/16.64, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] BHEL.NS triple_ma_short (short) (+877)
  Triggered: EMA(8/16/25) = 429.5/430/430, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] BHEL.NS breakdown_short (short) (+1,114)
  Triggered: broke range low 427.4 on vol 233,413 vs avg 198,881, trend EMA 429.5; India gate: RSI 23.77 / VWAP 430.5 (rsi<40 and close<=vwap)
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] IDEA.NS breakdown_short (short) (+3,876)
  Triggered: broke range low 14.24 on vol 13,885,330 vs avg 6,050,337, trend EMA 14.31; India gate: RSI 28.26 / VWAP 14.4 (rsi<40 and close<=vwap)
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] IDEA.NS breakdown_short (short) (+1,767)
  Triggered: broke range low 14.17 on vol 10,100,000 vs avg 7,054,972, trend EMA 14.28; India gate: RSI 29.55 / VWAP 14.39 (rsi<40 and close<=vwap)
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] BHEL.NS breakdown_short (short) (-822.8)
  Triggered: broke range low 425.6 on vol 236,615 vs avg 168,048, trend EMA 428; India gate: RSI 23.03 / VWAP 430 (rsi<40 and close<=vwap)
  Outcome:   trend_reversed
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] BANKINDIA.NS triple_ma_short (short) (-1,411)
  Triggered: EMA(8/16/25) = 142.4/142.5/142.5, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] IDEA.NS breakdown_short (short) (-2,498)
  Triggered: broke range low 14.06 on vol 21,549,128 vs avg 7,805,167, trend EMA 14.21; India gate: RSI 14.0 / VWAP 14.33 (rsi<40 and close<=vwap)
  Outcome:   trend_reversed
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] UNIONBANK.NS triple_ma_short (short) (-2,671)
  Triggered: EMA(8/16/25) = 184.3/184.6/184.7, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] TATAPOWER.NS triple_ma_long (long) (-285.6)
  Triggered: EMA(8/16/25) = 350.3/350.3/350.2, freshly aligned
  Outcome:   trend_reversed
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] SUZLON.NS triple_ma_short (short) (+0)
  Triggered: EMA(8/16/25) = 46.52/46.56/46.56, freshly aligned
  Outcome:   eod_settlement
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] ETERNAL.NS triple_ma_long (long) (-1,376)
  Triggered: EMA(8/16/25) = 326.6/326.6/326.5, freshly aligned
  Outcome:   trend_reversed
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] PFC.NS triple_ma_short (short) (-72.58)
  Triggered: EMA(8/16/25) = 345.3/345.5/345.7, freshly aligned
  Outcome:   eod_settlement
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] INDIANB.NS triple_ma_short (short) (-1,428)
  Triggered: EMA(8/16/25) = 878.5/879.9/879.9, freshly aligned
  Outcome:   eod_settlement
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

Still open (too soon to say why it worked or not):
  NMDC.NS triple_ma_long (long) -- triggered: EMA(8/16/25) = 86.62/86.29/86.18, freshly aligned
  HINDCOPPER.NS triple_threat_long (long) -- triggered: RSI 48->75 crossed 50, broke 528.8, trend EMA 528
  RPOWER.NS triple_threat_long (long) -- triggered: RSI 41->75 crossed 50, broke 22.2, trend EMA 22.2
  PNB.NS triple_ma_long (long) -- triggered: EMA(8/16/25) = 114.6/114.5/114.5, freshly aligned
  SAIL.NS triple_ma_short (short) -- triggered: EMA(8/16/25) = 197.3/197.4/197.4, freshly aligned
  IRCON.NS triple_ma_short (short) -- triggered: EMA(8/16/25) = 119.8/120.2/120.5, freshly aligned
  COALINDIA.NS triple_ma_long (long) -- triggered: EMA(8/16/25) = 402.9/402.2/401.9, freshly aligned
  PAYTM.NS triple_ma_long (long) -- triggered: EMA(8/16/25) = 1,674/1,671/1,669, freshly aligned

**CRYPTO -- WHY** (2026-09-01)
- Fired: 30 | Resolved: 27 | Still open: 3

[LOSS] AVAX-USD triple_threat_long (long) (-59.77)
  Triggered: no trigger detail logged (fired before trigger_context tracking started)
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] FET-USD triple_threat_long (long) (+40.59)
  Triggered: no trigger detail logged (fired before trigger_context tracking started)
  Outcome:   trend_reversed

[LOSS] FET-USD triple_ma_short (short) (-100.7)
  Triggered: no trigger detail logged (fired before trigger_context tracking started)
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] AVAX-USD triple_threat_long (long) (-59.77)
  Triggered: no trigger detail logged (fired before trigger_context tracking started)
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] FET-USD triple_ma_long (long) (+44.54)
  Triggered: no trigger detail logged (fired before trigger_context tracking started)
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] BTC-USD triple_ma_short (short) (-106.2)
  Triggered: EMA(8/16/25) = 7.84e+04/7.85e+04/7.857e+04, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] ETH-USD triple_ma_short (short) (-93.95)
  Triggered: EMA(8/16/25) = 2,463/2,466/2,467, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] SOL-USD triple_ma_short (short) (-43.81)
  Triggered: EMA(8/16/25) = 103.1/103.2/103.2, freshly aligned
  Outcome:   trend_reversed
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] XRP-USD triple_ma_short (short) (-52.66)
  Triggered: EMA(8/16/25) = 1.376/1.378/1.38, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] ETH-USD triple_ma_long (long) (+21.43)
  Triggered: EMA(8/16/25) = 2,470/2,469/2,469, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] BTC-USD triple_ma_long (long) (+33.28)
  Triggered: EMA(8/16/25) = 7.869e+04/7.863e+04/7.862e+04, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] NEAR-USD dmi_dpo_long (long) (-72.27)
  Triggered: +DI 29.11 vs -DI 14.99, ADX 23.53, DPO 0.000416 (period 50)
  Outcome:   trend_reversed
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] NEAR-USD dmi_dpo_long (long) (-52.39)
  Triggered: +DI 27.68 vs -DI 17.94, ADX 24.42, DPO 0.00012 (period 50)
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] SOL-USD triple_ma_short (short) (+117.9)
  Triggered: EMA(8/16/25) = 103.4/103.5/103.5, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] BTC-USD triple_ma_short (short) (+35.44)
  Triggered: EMA(8/16/25) = 7.863e+04/7.869e+04/7.87e+04, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] XRP-USD triple_ma_short (short) (+35.42)
  Triggered: EMA(8/16/25) = 1.381/1.383/1.383, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] AVAX-USD triple_threat_short (short) (-45.74)
  Triggered: RSI 51->41 crossed 50, broke 7.25, trend EMA 7.278
  Outcome:   trend_reversed
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] ETH-USD triple_ma_short (short) (-11.12)
  Triggered: EMA(8/16/25) = 2,466/2,469/2,470, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] NEAR-USD triple_ma_short (short) (+21.54)
  Triggered: EMA(8/16/25) = 1.938/1.945/1.946, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] FET-USD triple_ma_short (short) (+50.92)
  Triggered: EMA(8/16/25) = 0.155/0.1557/0.1558, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] AVAX-USD triple_ma_short (short) (-92.41)
  Triggered: EMA(8/16/25) = 7.259/7.272/7.273, freshly aligned
  Outcome:   trend_reversed
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] NEAR-USD dmi_dpo_long (long) (-6.022)
  Triggered: +DI 23.02 vs -DI 21.54, ADX 23.79, DPO 0.02187 (period 50)
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] XRP-USD triple_ma_short (short) (-42.69)
  Triggered: EMA(8/16/25) = 1.376/1.376/1.376, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] ETH-USD community_idea (short) (-134.9)
  Triggered: no trigger detail logged (fired before trigger_context tracking started)
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] BTC-USD triple_ma_short (short) (+42.94)
  Triggered: EMA(8/16/25) = 7.8e+04/7.803e+04/7.807e+04, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] XRP-USD triple_ma_short (short) (-47.16)
  Triggered: EMA(8/16/25) = 1.374/1.374/1.375, freshly aligned
  Outcome:   trend_reversed
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] FET-USD triple_ma_short (short) (+25.9)
  Triggered: EMA(8/16/25) = 0.1539/0.1539/0.154, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

Still open (too soon to say why it worked or not):
  XRP-USD triple_ma_short (short) -- triggered: EMA(8/16/25) = 1.375/1.375/1.375, freshly aligned
  AVAX-USD triple_ma_short (short) -- triggered: EMA(8/16/25) = 7.27/7.277/7.278, freshly aligned
  NEAR-USD triple_ma_short (short) -- triggered: EMA(8/16/25) = 1.969/1.979/1.979, freshly aligned

**US -- WHY** (2026-09-01)
- Fired: 10 | Resolved: 10 | Still open: 0

[LOSS] HOOD triple_ma_long (long) (-65.49)
  Triggered: no trigger detail logged (fired before trigger_context tracking started)
  Outcome:   eod_settlement
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] AAL triple_ma_short (short) (+61.3)
  Triggered: no trigger detail logged (fired before trigger_context tracking started)
  Outcome:   eod_settlement

[WIN] GC=F seasonal_short (short) (+0.01103)
  Triggered: month 9 seasonal edge
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] MO community_idea (long) (-114.4)
  Triggered: no trigger detail logged (fired before trigger_context tracking started)
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] MO triple_ma_long (long) (-94.47)
  Triggered: EMA(8/16/25) = 69.33/69.07/68.91, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] MO triple_ma_long (long) (-6.484)
  Triggered: EMA(8/16/25) = 69.32/69.06/68.9, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] CLF triple_ma_long (long) (-178.3)
  Triggered: EMA(8/16/25) = 11.62/11.6/11.6, freshly aligned
  Outcome:   trend_reversed
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] CLF triple_ma_long (long) (+183.5)
  Triggered: EMA(8/16/25) = 11.63/11.61/11.6, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] GC=F community_idea (short) (+0.1365)
  Triggered: no trigger detail logged (fired before trigger_context tracking started)
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] CLF triple_ma_long (long) (-163.6)
  Triggered: EMA(8/16/25) = 11.64/11.64/11.63, freshly aligned
  Outcome:   trend_reversed
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

**INDIA FUTURES (MANUAL) -- WHY** (2026-09-01)
- Fired: 6 | Resolved: 6 | Still open: 0

[LOSS] BANKNIFTY-FUT triple_ma_long (long) (-561.6)
  Triggered: EMA(8/16/25) = 5.756e+04/5.755e+04/5.752e+04, freshly aligned
  Outcome:   trend_reversed
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] SENSEX-FUT triple_ma_long (long) (-844.8)
  Triggered: EMA(8/16/25) = 7.712e+04/7.708e+04/7.705e+04, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] NIFTY-FUT triple_ma_long (long) (+74.88)
  Triggered: EMA(8/16/25) = 2.408e+04/2.408e+04/2.408e+04, freshly aligned
  Outcome:   trend_reversed

[LOSS] NIFTY-FUT triple_ma_short (short) (-710.8)
  Triggered: EMA(8/16/25) = 2.406e+04/2.407e+04/2.407e+04, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] BANKNIFTY-FUT triple_ma_short (short) (-1,986)
  Triggered: EMA(8/16/25) = 5.739e+04/5.745e+04/5.746e+04, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] SENSEX-FUT triple_ma_short (short) (+82.41)
  Triggered: EMA(8/16/25) = 7.693e+04/7.698e+04/7.698e+04, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

---

## 2026-09-02 12:08 IST

**INDIA -- WHY** (2026-09-02)
- Fired: 72 | Resolved: 51 | Still open: 21

[WIN] ETERNAL.NS triple_ma_short (short) (+3,155)
  Triggered: EMA(8/16/25) = 326.272/326.406/326.41, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] BANKINDIA.NS breakdown_short (short) (-3,237)
  Triggered: broke range low 141.4 on vol 235,120 vs avg 106,724, trend EMA 141.9; India gate: RSI 22.6 / VWAP 140.7 (rsi<40 and close<=vwap)
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] TATAPOWER.NS triple_ma_long (long) (+7,569)
  Triggered: EMA(8/16/25) = 350.348/350.32/350.197, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] SUZLON.NS breakdown_short (short) (+705.5)
  Triggered: broke range low 45.95 on vol 1,993,915 vs avg 1,747,562, trend EMA 46.37; India gate: RSI 25.53 / VWAP 45.88 (rsi<40 and close<=vwap)
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] COALINDIA.NS triple_ma_long (long) (+1,254)
  Triggered: EMA(8/16/25) = 407.133/404.513/403.524, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] SUZLON.NS triple_ma_short (short) (-2,303)
  Triggered: EMA(8/16/25) = 46.1325/46.3247/46.4022, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] VEDL.NS triple_ma_short (short) (-2,426)
  Triggered: EMA(8/16/25) = 272.704/274.292/275.441, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] BEL.NS triple_ma_short (short) (+801.1)
  Triggered: EMA(8/16/25) = 408.374/409.709/410.261, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] BHEL.NS triple_ma_short (short) (-3,479)
  Triggered: EMA(8/16/25) = 423.714/425.655/426.804, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] PAYTM.NS triple_ma_short (short) (+1,917)
  Triggered: EMA(8/16/25) = 1,622.09/1,630.97/1,637.95, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] RPOWER.NS triple_ma_short (short) (-2,414)
  Triggered: EMA(8/16/25) = 22.1016/22.1331/22.1533, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] PNB.NS triple_ma_long (long) (+1,726)
  Triggered: EMA(8/16/25) = 115.393/115.367/115.299, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] COALINDIA.NS triple_ma_long (long) (+1,336)
  Triggered: EMA(8/16/25) = 409.212/405.929/404.525, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] SUZLON.NS triple_ma_short (short) (-3,076)
  Triggered: EMA(8/16/25) = 45.9965/46.2299/46.3345, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] VEDL.NS triple_ma_short (short) (-3,148)
  Triggered: EMA(8/16/25) = 271.992/273.727/274.979, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] BEL.NS triple_ma_short (short) (+556.3)
  Triggered: EMA(8/16/25) = 407.512/409.096/409.822, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] TATAPOWER.NS triple_ma_long (long) (+4,755)
  Triggered: EMA(8/16/25) = 351.541/350.984/350.65, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] RPOWER.NS triple_ma_short (short) (-2,059)
  Triggered: EMA(8/16/25) = 22.0836/22.1197/22.1431, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] BHEL.NS triple_ma_short (short) (-2,568)
  Triggered: EMA(8/16/25) = 422.956/425.022/426.302, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] PNB.NS triple_ma_long (long) (+2,071)
  Triggered: EMA(8/16/25) = 115.572/115.465/115.366, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] HINDCOPPER.NS triple_ma_short (short) (+732.4)
  Triggered: EMA(8/16/25) = 521.667/522.457/523.345, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] PAYTM.NS triple_ma_short (short) (+1,885)
  Triggered: EMA(8/16/25) = 1,618.79/1,628.17/1,635.55, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] IDEA.NS triple_ma_short (short) (-5,444)
  Triggered: EMA(8/16/25) = 14.1282/14.1678/14.2341, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] COALINDIA.NS triple_ma_long (long) (+1,280)
  Triggered: EMA(8/16/25) = 409.224/405.935/404.529, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] IDEA.NS triple_ma_short (short) (-7,568)
  Triggered: EMA(8/16/25) = 14.1749/14.1925/14.2503, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] TATAPOWER.NS breakout_long (long) (+978.7)
  Triggered: broke range high 356.5 on vol 1,046,607 vs avg 276,752, trend EMA 351.8; India gate: RSI 78.43 / VWAP 353.3 (rsi>60 and close>=vwap)
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] SUZLON.NS triple_ma_short (short) (-2,413)
  Triggered: EMA(8/16/25) = 46.0099/46.237/46.3391, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] JSWENERGY.NS triple_ma_short (short) (-5,796)
  Triggered: EMA(8/16/25) = 519.832/520.394/521.416, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] VEDL.NS triple_ma_short (short) (+1,110)
  Triggered: EMA(8/16/25) = 272.148/273.809/275.033, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] RPOWER.NS triple_ma_short (short) (-2,373)
  Triggered: EMA(8/16/25) = 22.0814/22.1185/22.1424, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] BEL.NS triple_ma_short (short) (+0)
  Triggered: EMA(8/16/25) = 407.579/409.132/409.845, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] HINDCOPPER.NS triple_ma_short (short) (+618.3)
  Triggered: EMA(8/16/25) = 521.656/522.451/523.342, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] PNB.NS triple_ma_long (long) (+1,599)
  Triggered: EMA(8/16/25) = 115.595/115.477/115.373, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] PAYTM.NS triple_ma_short (short) (+2,002)
  Triggered: EMA(8/16/25) = 1,618.88/1,628.22/1,635.58, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] COALINDIA.NS triple_ma_long (long) (+1,280)
  Triggered: EMA(8/16/25) = 409.224/405.935/404.529, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] IDEA.NS triple_ma_short (short) (-7,452)
  Triggered: EMA(8/16/25) = 14.1727/14.1913/14.2495, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] JSWENERGY.NS triple_ma_short (short) (-3,157)
  Triggered: EMA(8/16/25) = 520.376/520.682/521.604, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] TATAPOWER.NS triple_ma_long (long) (+929.9)
  Triggered: EMA(8/16/25) = 352.408/351.443/350.95, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] SUZLON.NS triple_ma_short (short) (-2,413)
  Triggered: EMA(8/16/25) = 46.0099/46.237/46.3391, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] PNB.NS triple_ma_long (long) (-1,885)
  Triggered: EMA(8/16/25) = 115.621/115.491/115.383, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] BEL.NS triple_ma_short (short) (+678.4)
  Triggered: EMA(8/16/25) = 407.701/409.196/409.887, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] VEDL.NS triple_ma_short (short) (+1,664)
  Triggered: EMA(8/16/25) = 272.215/273.845/275.056, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] HINDCOPPER.NS triple_ma_short (short) (+450)
  Triggered: EMA(8/16/25) = 521.544/522.392/523.303, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] PAYTM.NS triple_ma_short (short) (+2,396)
  Triggered: EMA(8/16/25) = 1,619.19/1,628.39/1,635.69, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] POWERGRID.NS triple_ma_long (long) (+502.4)
  Triggered: EMA(8/16/25) = 263.928/263.644/263.598, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] IDEA.NS triple_threat_long (long) (+886.1)
  Triggered: RSI 35->60 crossed 50, broke 14.4, trend EMA 14.29
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] JSWENERGY.NS breakout_long (long) (+707.6)
  Triggered: broke range high 530.8 on vol 292,979 vs avg 71,503, trend EMA 521.1; India gate: RSI 64.57 / VWAP 523.6 (rsi>60 and close>=vwap)
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] IDEA.NS breakout_long (long) (-3,037)
  Triggered: broke range high 14.51 on vol 46,994,859 vs avg 30,093,402, trend EMA 14.28; India gate: RSI 70.48 / VWAP 14.32 (rsi>60 and close>=vwap)
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] IDEA.NS triple_ma_long (long) (-1,887)
  Triggered: EMA(8/16/25) = 14.4281/14.3463/14.3421, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] TATAPOWER.NS breakout_long (long) (-1,804)
  Triggered: broke range high 359.4 on vol 616,104 vs avg 571,874, trend EMA 356; India gate: RSI 80.81 / VWAP 356.8 (rsi>60 and close>=vwap)
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] POWERGRID.NS breakout_long (long) (-2,062)
  Triggered: broke range high 266.1 on vol 766,490 vs avg 573,150, trend EMA 265; India gate: RSI 71.9 / VWAP 265.2 (rsi>60 and close>=vwap)
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

Still open (too soon to say why it worked or not):
  IOC.NS triple_threat_short (short) -- triggered: RSI 54->30 crossed 50, broke 136.2, trend EMA 136.3
  ETERNAL.NS triple_ma_short (short) -- triggered: EMA(8/16/25) = 325.137/325.765/325.982, freshly aligned
  RVNL.NS triple_ma_short (short) -- triggered: EMA(8/16/25) = 207.682/208.582/209.183, freshly aligned
  JPPOWER.NS triple_ma_short (short) -- triggered: EMA(8/16/25) = 16.4923/16.5303/16.5567, freshly aligned
  NTPC.NS triple_ma_short (short) -- triggered: EMA(8/16/25) = 325.449/326.036/326.272, freshly aligned
  IRCON.NS triple_ma_short (short) -- triggered: EMA(8/16/25) = 118.455/118.909/119.253, freshly aligned
  NMDC.NS triple_ma_short (short) -- triggered: EMA(8/16/25) = 85.2055/85.5027/85.6834, freshly aligned
  ONGC.NS triple_ma_long (long) -- triggered: EMA(8/16/25) = 236.533/235.915/235.399, freshly aligned
  RVNL.NS triple_ma_short (short) -- triggered: EMA(8/16/25) = 207.303/208.275/208.937, freshly aligned
  HUDCO.NS triple_ma_short (short) -- triggered: EMA(8/16/25) = 177.252/177.888/178.336, freshly aligned
  IRCON.NS triple_ma_short (short) -- triggered: EMA(8/16/25) = 118.297/118.771/119.135, freshly aligned
  NMDC.NS triple_ma_short (short) -- triggered: EMA(8/16/25) = 85.0668/85.3937/85.5979, freshly aligned
  RVNL.NS triple_ma_short (short) -- triggered: EMA(8/16/25) = 207.398/208.325/208.97, freshly aligned
  BHEL.NS triple_ma_short (short) -- triggered: EMA(8/16/25) = 423.356/425.234/426.441, freshly aligned
  HUDCO.NS triple_ma_short (short) -- triggered: EMA(8/16/25) = 177.323/177.926/178.361, freshly aligned
  IRCON.NS triple_ma_short (short) -- triggered: EMA(8/16/25) = 118.375/118.812/119.162, freshly aligned
  RPOWER.NS triple_ma_short (short) -- triggered: EMA(8/16/25) = 22.0947/22.1256/22.147, freshly aligned
  RVNL.NS triple_ma_short (short) -- triggered: EMA(8/16/25) = 207.421/208.337/208.977, freshly aligned
  BHEL.NS triple_ma_short (short) -- triggered: EMA(8/16/25) = 423.389/425.251/426.452, freshly aligned
  JPPOWER.NS triple_ma_short (short) -- triggered: EMA(8/16/25) = 16.4786/16.5184/16.5467, freshly aligned
  JSWENERGY.NS triple_ma_long (long) -- triggered: EMA(8/16/25) = 525.803/523.721/523.516, freshly aligned

**CRYPTO -- WHY** (2026-09-02)
- Fired: 24 | Resolved: 22 | Still open: 2

[LOSS] FET-USD triple_ma_short (short) (-41.29)
  Triggered: EMA(8/16/25) = 0.153872/0.153883/0.153903, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] FET-USD triple_ma_long (long) (-49.08)
  Triggered: EMA(8/16/25) = 0.154079/0.153918/0.153909, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] FET-USD triple_threat_long (long) (-36.48)
  Triggered: RSI 48->57 crossed 50, broke 0.156, trend EMA 0.1539
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] FET-USD triple_ma_short (short) (+17.72)
  Triggered: EMA(8/16/25) = 0.153749/0.153816/0.153849, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] NEAR-USD triple_threat_short (short) (-31.69)
  Triggered: RSI 51->32 crossed 50, broke 1.882, trend EMA 1.921
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] BTC-USD dmi_dpo_short (short) (-33.84)
  Triggered: +DI 15.35 vs -DI 28.24, ADX 24.49, DPO -166.5 (period 50)
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] ETH-USD dmi_dpo_short (short) (-24.61)
  Triggered: +DI 14.01 vs -DI 29.51, ADX 26.67, DPO -2.549 (period 50)
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] SOL-USD dmi_dpo_short (short) (-24.02)
  Triggered: +DI 13.77 vs -DI 28.15, ADX 29.2, DPO -0.1116 (period 50)
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] BTC-USD dmi_dpo_short (short) (+51.14)
  Triggered: +DI 17.16 vs -DI 27.35, ADX 24.97, DPO -60.7 (period 50)
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] SOL-USD dmi_dpo_short (short) (+17.53)
  Triggered: +DI 14.83 vs -DI 27.42, ADX 30.02, DPO -0.04 (period 50)
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (win)

[WIN] ETH-USD dmi_dpo_short (short) (+74.36)
  Triggered: +DI 15.28 vs -DI 28.68, ADX 29.23, DPO -9.274 (period 50)
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] ETH-USD triple_ma_short (short) (+46.67)
  Triggered: EMA(8/16/25) = 2,414.77/2,415.19/2,417.5, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] SOL-USD dmi_dpo_short (short) (+18.57)
  Triggered: +DI 14.26 vs -DI 27.21, ADX 31.23, DPO -0.0776 (period 50)
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] SOL-USD triple_ma_short (short) (+11.27)
  Triggered: EMA(8/16/25) = 99.7947/99.8143/99.9579, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] BTC-USD triple_ma_short (short) (+46.82)
  Triggered: EMA(8/16/25) = 77,250.9/77,260/77,297.8, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] FET-USD triple_ma_short (short) (-72.34)
  Triggered: EMA(8/16/25) = 0.153123/0.153271/0.153336, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] XRP-USD breakdown_short (short) (-166)
  Triggered: broke range low 1.335 on vol 1,743,496 vs avg 1,097,415, trend EMA 1.341, 2-bar + retest
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [STOP OVERSHOOT] intended risk 0.0053/unit, actual loss 0.0088/unit (1.7x) -- price moved past the stop faster than the bot's bar-close check could exit; a violent move against the position, amplified by simulation lag rather than a bad entry call

[LOSS] SOL-USD triple_threat_long (long) (-38.92)
  Triggered: RSI 50->56 crossed 50, broke 100.2, trend EMA 99.84
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] BTC-USD dmi_dpo_short (short) (+22.27)
  Triggered: +DI 19.65 vs -DI 25.03, ADX 27.21, DPO -230.8 (period 50)
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] ETH-USD dmi_dpo_short (short) (+12.11)
  Triggered: +DI 16.98 vs -DI 26.7, ADX 32.6, DPO -9.118 (period 50)
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] ETH-USD dmi_dpo_short (short) (-41.08)
  Triggered: +DI 16.56 vs -DI 26.85, ADX 32.7, DPO -7.655 (period 50)
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] XRP-USD triple_ma_long (long) (-52.77)
  Triggered: EMA(8/16/25) = 1.34928/1.34792/1.34781, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

Still open (too soon to say why it worked or not):
  BTC-USD triple_threat_long (long) -- triggered: RSI 49->56 crossed 50, broke 7.76e+04, trend EMA 7.728e+04
  NEAR-USD triple_ma_short (short) -- triggered: EMA(8/16/25) = 1.86901/1.87054/1.87375, freshly aligned

**US -- WHY** (2026-09-02)
- Fired: 1 | Resolved: 1 | Still open: 0

[LOSS] CLF triple_ma_long (long) (-294.7)
  Triggered: EMA(8/16/25) = 11.6369/11.6364/11.6311, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

---

## 2026-09-03 00:00 IST

**INDIA -- WHY** (2026-09-02)
- Fired: 77 | Resolved: 66 | Still open: 11

[WIN] ETERNAL.NS triple_ma_short (short) (+3,155)
  Triggered: EMA(8/16/25) = 326.272/326.406/326.41, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] BANKINDIA.NS breakdown_short (short) (-3,237)
  Triggered: broke range low 141.4 on vol 235,120 vs avg 106,724, trend EMA 141.9; India gate: RSI 22.6 / VWAP 140.7 (rsi<40 and close<=vwap)
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] TATAPOWER.NS triple_ma_long (long) (+7,569)
  Triggered: EMA(8/16/25) = 350.348/350.32/350.197, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] SUZLON.NS breakdown_short (short) (+705.5)
  Triggered: broke range low 45.95 on vol 1,993,915 vs avg 1,747,562, trend EMA 46.37; India gate: RSI 25.53 / VWAP 45.88 (rsi<40 and close<=vwap)
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] COALINDIA.NS triple_ma_long (long) (+1,254)
  Triggered: EMA(8/16/25) = 407.133/404.513/403.524, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] SUZLON.NS triple_ma_short (short) (-2,303)
  Triggered: EMA(8/16/25) = 46.1325/46.3247/46.4022, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] VEDL.NS triple_ma_short (short) (-2,426)
  Triggered: EMA(8/16/25) = 272.704/274.292/275.441, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] BEL.NS triple_ma_short (short) (+801.1)
  Triggered: EMA(8/16/25) = 408.374/409.709/410.261, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] RVNL.NS triple_ma_short (short) (+3,081)
  Triggered: EMA(8/16/25) = 207.682/208.582/209.183, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] JPPOWER.NS triple_ma_short (short) (+1,219)
  Triggered: EMA(8/16/25) = 16.4923/16.5303/16.5567, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] BHEL.NS triple_ma_short (short) (-3,479)
  Triggered: EMA(8/16/25) = 423.714/425.655/426.804, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] PAYTM.NS triple_ma_short (short) (+1,917)
  Triggered: EMA(8/16/25) = 1,622.09/1,630.97/1,637.95, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] RPOWER.NS triple_ma_short (short) (-2,414)
  Triggered: EMA(8/16/25) = 22.1016/22.1331/22.1533, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] PNB.NS triple_ma_long (long) (+1,726)
  Triggered: EMA(8/16/25) = 115.393/115.367/115.299, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] COALINDIA.NS triple_ma_long (long) (+1,336)
  Triggered: EMA(8/16/25) = 409.212/405.929/404.525, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] SUZLON.NS triple_ma_short (short) (-3,076)
  Triggered: EMA(8/16/25) = 45.9965/46.2299/46.3345, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] VEDL.NS triple_ma_short (short) (-3,148)
  Triggered: EMA(8/16/25) = 271.992/273.727/274.979, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] BEL.NS triple_ma_short (short) (+556.3)
  Triggered: EMA(8/16/25) = 407.512/409.096/409.822, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] TATAPOWER.NS triple_ma_long (long) (+4,755)
  Triggered: EMA(8/16/25) = 351.541/350.984/350.65, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] RPOWER.NS triple_ma_short (short) (-2,059)
  Triggered: EMA(8/16/25) = 22.0836/22.1197/22.1431, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] RVNL.NS triple_ma_short (short) (+2,840)
  Triggered: EMA(8/16/25) = 207.303/208.275/208.937, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] BHEL.NS triple_ma_short (short) (-2,568)
  Triggered: EMA(8/16/25) = 422.956/425.022/426.302, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] PNB.NS triple_ma_long (long) (+2,071)
  Triggered: EMA(8/16/25) = 115.572/115.465/115.366, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] HINDCOPPER.NS triple_ma_short (short) (+732.4)
  Triggered: EMA(8/16/25) = 521.667/522.457/523.345, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] PAYTM.NS triple_ma_short (short) (+1,885)
  Triggered: EMA(8/16/25) = 1,618.79/1,628.17/1,635.55, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] IDEA.NS triple_ma_short (short) (-5,444)
  Triggered: EMA(8/16/25) = 14.1282/14.1678/14.2341, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] COALINDIA.NS triple_ma_long (long) (+1,280)
  Triggered: EMA(8/16/25) = 409.224/405.935/404.529, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] IDEA.NS triple_ma_short (short) (-7,568)
  Triggered: EMA(8/16/25) = 14.1749/14.1925/14.2503, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] TATAPOWER.NS breakout_long (long) (+978.7)
  Triggered: broke range high 356.5 on vol 1,046,607 vs avg 276,752, trend EMA 351.8; India gate: RSI 78.43 / VWAP 353.3 (rsi>60 and close>=vwap)
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] SUZLON.NS triple_ma_short (short) (-2,413)
  Triggered: EMA(8/16/25) = 46.0099/46.237/46.3391, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] JSWENERGY.NS triple_ma_short (short) (-5,796)
  Triggered: EMA(8/16/25) = 519.832/520.394/521.416, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] VEDL.NS triple_ma_short (short) (+1,110)
  Triggered: EMA(8/16/25) = 272.148/273.809/275.033, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] RPOWER.NS triple_ma_short (short) (-2,373)
  Triggered: EMA(8/16/25) = 22.0814/22.1185/22.1424, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] BEL.NS triple_ma_short (short) (+0)
  Triggered: EMA(8/16/25) = 407.579/409.132/409.845, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] HINDCOPPER.NS triple_ma_short (short) (+618.3)
  Triggered: EMA(8/16/25) = 521.656/522.451/523.342, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] RVNL.NS triple_ma_short (short) (+3,876)
  Triggered: EMA(8/16/25) = 207.398/208.325/208.97, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] PNB.NS triple_ma_long (long) (+1,599)
  Triggered: EMA(8/16/25) = 115.595/115.477/115.373, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] PAYTM.NS triple_ma_short (short) (+2,002)
  Triggered: EMA(8/16/25) = 1,618.88/1,628.22/1,635.58, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] BHEL.NS triple_ma_short (short) (-4,054)
  Triggered: EMA(8/16/25) = 423.356/425.234/426.441, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] COALINDIA.NS triple_ma_long (long) (+1,280)
  Triggered: EMA(8/16/25) = 409.224/405.935/404.529, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] IDEA.NS triple_ma_short (short) (-7,452)
  Triggered: EMA(8/16/25) = 14.1727/14.1913/14.2495, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] JSWENERGY.NS triple_ma_short (short) (-3,157)
  Triggered: EMA(8/16/25) = 520.376/520.682/521.604, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] TATAPOWER.NS triple_ma_long (long) (+929.9)
  Triggered: EMA(8/16/25) = 352.408/351.443/350.95, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] SUZLON.NS triple_ma_short (short) (-2,413)
  Triggered: EMA(8/16/25) = 46.0099/46.237/46.3391, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] PNB.NS triple_ma_long (long) (-1,885)
  Triggered: EMA(8/16/25) = 115.621/115.491/115.383, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] RPOWER.NS triple_ma_short (short) (+1,981)
  Triggered: EMA(8/16/25) = 22.0947/22.1256/22.147, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] BEL.NS triple_ma_short (short) (+678.4)
  Triggered: EMA(8/16/25) = 407.701/409.196/409.887, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] VEDL.NS triple_ma_short (short) (+1,664)
  Triggered: EMA(8/16/25) = 272.215/273.845/275.056, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] HINDCOPPER.NS triple_ma_short (short) (+450)
  Triggered: EMA(8/16/25) = 521.544/522.392/523.303, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] RVNL.NS triple_ma_short (short) (+4,116)
  Triggered: EMA(8/16/25) = 207.421/208.337/208.977, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] PAYTM.NS triple_ma_short (short) (+2,396)
  Triggered: EMA(8/16/25) = 1,619.19/1,628.39/1,635.69, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] BHEL.NS triple_ma_short (short) (-3,628)
  Triggered: EMA(8/16/25) = 423.389/425.251/426.452, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] POWERGRID.NS triple_ma_long (long) (+502.4)
  Triggered: EMA(8/16/25) = 263.928/263.644/263.598, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] JPPOWER.NS triple_ma_short (short) (+1,765)
  Triggered: EMA(8/16/25) = 16.4786/16.5184/16.5467, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] IDEA.NS triple_threat_long (long) (+886.1)
  Triggered: RSI 35->60 crossed 50, broke 14.4, trend EMA 14.29
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] JSWENERGY.NS breakout_long (long) (+707.6)
  Triggered: broke range high 530.8 on vol 292,979 vs avg 71,503, trend EMA 521.1; India gate: RSI 64.57 / VWAP 523.6 (rsi>60 and close>=vwap)
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] IDEA.NS breakout_long (long) (-3,037)
  Triggered: broke range high 14.51 on vol 46,994,859 vs avg 30,093,402, trend EMA 14.28; India gate: RSI 70.48 / VWAP 14.32 (rsi>60 and close>=vwap)
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] JSWENERGY.NS triple_ma_long (long) (+3,127)
  Triggered: EMA(8/16/25) = 525.803/523.721/523.516, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] IDEA.NS triple_ma_long (long) (-1,887)
  Triggered: EMA(8/16/25) = 14.4281/14.3463/14.3421, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] TATAPOWER.NS breakout_long (long) (-1,804)
  Triggered: broke range high 359.4 on vol 616,104 vs avg 571,874, trend EMA 356; India gate: RSI 80.81 / VWAP 356.8 (rsi>60 and close>=vwap)
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] POWERGRID.NS breakout_long (long) (-2,062)
  Triggered: broke range high 266.1 on vol 766,490 vs avg 573,150, trend EMA 265; India gate: RSI 71.9 / VWAP 265.2 (rsi>60 and close>=vwap)
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] POWERGRID.NS breakout_long (long) (-560)
  Triggered: broke range high 267.6 on vol 500,955 vs avg 395,754, trend EMA 266.4; India gate: RSI 67.37 / VWAP 265.8 (rsi>60 and close>=vwap)
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] JSWENERGY.NS breakout_long (long) (-1,991)
  Triggered: broke range high 538.4 on vol 203,445 vs avg 112,965, trend EMA 535.4; India gate: RSI 89.0 / VWAP 532.9 (rsi>60 and close>=vwap)
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] RPOWER.NS triple_ma_short (short) (-453.1)
  Triggered: EMA(8/16/25) = 22.0607/22.0609/22.0753, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] TATAPOWER.NS breakout_long (long) (-690.8)
  Triggered: broke range high 361.5 on vol 460,860 vs avg 323,330, trend EMA 360.5; India gate: RSI 76.5 / VWAP 358.4 (rsi>60 and close>=vwap)
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] RPOWER.NS triple_ma_short (short) (-2,041)
  Triggered: EMA(8/16/25) = 22.0627/22.0642/22.0722, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

Still open (too soon to say why it worked or not):
  IOC.NS triple_threat_short (short) -- triggered: RSI 54->30 crossed 50, broke 136.2, trend EMA 136.3
  ETERNAL.NS triple_ma_short (short) -- triggered: EMA(8/16/25) = 325.137/325.765/325.982, freshly aligned
  NTPC.NS triple_ma_short (short) -- triggered: EMA(8/16/25) = 325.449/326.036/326.272, freshly aligned
  IRCON.NS triple_ma_short (short) -- triggered: EMA(8/16/25) = 118.455/118.909/119.253, freshly aligned
  NMDC.NS triple_ma_short (short) -- triggered: EMA(8/16/25) = 85.2055/85.5027/85.6834, freshly aligned
  ONGC.NS triple_ma_long (long) -- triggered: EMA(8/16/25) = 236.533/235.915/235.399, freshly aligned
  HUDCO.NS triple_ma_short (short) -- triggered: EMA(8/16/25) = 177.252/177.888/178.336, freshly aligned
  IRCON.NS triple_ma_short (short) -- triggered: EMA(8/16/25) = 118.297/118.771/119.135, freshly aligned
  NMDC.NS triple_ma_short (short) -- triggered: EMA(8/16/25) = 85.0668/85.3937/85.5979, freshly aligned
  HUDCO.NS triple_ma_short (short) -- triggered: EMA(8/16/25) = 177.323/177.926/178.361, freshly aligned
  IRCON.NS triple_ma_short (short) -- triggered: EMA(8/16/25) = 118.375/118.812/119.162, freshly aligned

**CRYPTO -- WHY** (2026-09-02)
- Fired: 54 | Resolved: 51 | Still open: 3

[LOSS] FET-USD triple_ma_short (short) (-41.29)
  Triggered: EMA(8/16/25) = 0.153872/0.153883/0.153903, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] FET-USD triple_ma_long (long) (-49.08)
  Triggered: EMA(8/16/25) = 0.154079/0.153918/0.153909, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] FET-USD triple_threat_long (long) (-36.48)
  Triggered: RSI 48->57 crossed 50, broke 0.156, trend EMA 0.1539
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] FET-USD triple_ma_short (short) (+17.72)
  Triggered: EMA(8/16/25) = 0.153749/0.153816/0.153849, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] NEAR-USD triple_threat_short (short) (-31.69)
  Triggered: RSI 51->32 crossed 50, broke 1.882, trend EMA 1.921
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] BTC-USD dmi_dpo_short (short) (-33.84)
  Triggered: +DI 15.35 vs -DI 28.24, ADX 24.49, DPO -166.5 (period 50)
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] ETH-USD dmi_dpo_short (short) (-24.61)
  Triggered: +DI 14.01 vs -DI 29.51, ADX 26.67, DPO -2.549 (period 50)
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] SOL-USD dmi_dpo_short (short) (-24.02)
  Triggered: +DI 13.77 vs -DI 28.15, ADX 29.2, DPO -0.1116 (period 50)
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] BTC-USD dmi_dpo_short (short) (+51.14)
  Triggered: +DI 17.16 vs -DI 27.35, ADX 24.97, DPO -60.7 (period 50)
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] SOL-USD dmi_dpo_short (short) (+17.53)
  Triggered: +DI 14.83 vs -DI 27.42, ADX 30.02, DPO -0.04 (period 50)
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (win)

[WIN] ETH-USD dmi_dpo_short (short) (+74.36)
  Triggered: +DI 15.28 vs -DI 28.68, ADX 29.23, DPO -9.274 (period 50)
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] ETH-USD triple_ma_short (short) (+46.67)
  Triggered: EMA(8/16/25) = 2,414.77/2,415.19/2,417.5, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] SOL-USD dmi_dpo_short (short) (+18.57)
  Triggered: +DI 14.26 vs -DI 27.21, ADX 31.23, DPO -0.0776 (period 50)
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] SOL-USD triple_ma_short (short) (+11.27)
  Triggered: EMA(8/16/25) = 99.7947/99.8143/99.9579, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] BTC-USD triple_ma_short (short) (+46.82)
  Triggered: EMA(8/16/25) = 77,250.9/77,260/77,297.8, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] FET-USD triple_ma_short (short) (-72.34)
  Triggered: EMA(8/16/25) = 0.153123/0.153271/0.153336, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] XRP-USD breakdown_short (short) (-166)
  Triggered: broke range low 1.335 on vol 1,743,496 vs avg 1,097,415, trend EMA 1.341, 2-bar + retest
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [STOP OVERSHOOT] intended risk 0.0053/unit, actual loss 0.0088/unit (1.7x) -- price moved past the stop faster than the bot's bar-close check could exit; a violent move against the position, amplified by simulation lag rather than a bad entry call

[LOSS] SOL-USD triple_threat_long (long) (-38.92)
  Triggered: RSI 50->56 crossed 50, broke 100.2, trend EMA 99.84
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] BTC-USD triple_threat_long (long) (-27.16)
  Triggered: RSI 49->56 crossed 50, broke 7.76e+04, trend EMA 7.728e+04
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] BTC-USD dmi_dpo_short (short) (+22.27)
  Triggered: +DI 19.65 vs -DI 25.03, ADX 27.21, DPO -230.8 (period 50)
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] ETH-USD dmi_dpo_short (short) (+12.11)
  Triggered: +DI 16.98 vs -DI 26.7, ADX 32.6, DPO -9.118 (period 50)
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] ETH-USD dmi_dpo_short (short) (-41.08)
  Triggered: +DI 16.56 vs -DI 26.85, ADX 32.7, DPO -7.655 (period 50)
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] XRP-USD triple_ma_long (long) (-52.77)
  Triggered: EMA(8/16/25) = 1.34928/1.34792/1.34781, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] NEAR-USD triple_ma_short (short) (-37.64)
  Triggered: EMA(8/16/25) = 1.86901/1.87054/1.87375, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] BTC-USD dmi_dpo_short (short) (+211.6)
  Triggered: +DI 19.02 vs -DI 25.08, ADX 23.87, DPO -87.5 (period 50)
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] ETH-USD dmi_dpo_short (short) (+410.4)
  Triggered: +DI 17.25 vs -DI 25.73, ADX 31.02, DPO -1.825 (period 50)
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (win)

[WIN] SOL-USD dmi_dpo_short (short) (+147)
  Triggered: +DI 16.05 vs -DI 26.26, ADX 31.53, DPO -0.0686 (period 50)
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (win)

[LOSS] XRP-USD triple_ma_long (long) (-22.28)
  Triggered: EMA(8/16/25) = 1.34777/1.34746/1.34746, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] FET-USD triple_ma_long (long) (-35.27)
  Triggered: EMA(8/16/25) = 0.154425/0.154424/0.154333, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] XRP-USD triple_ma_short (short) (+84.97)
  Triggered: EMA(8/16/25) = 1.3469/1.34705/1.34718, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] SOL-USD triple_ma_short (short) (+62.96)
  Triggered: EMA(8/16/25) = 99.8889/99.938/99.9461, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] BTC-USD triple_ma_short (short) (+33.69)
  Triggered: EMA(8/16/25) = 77,321.8/77,401.2/77,410.2, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] ETH-USD triple_ma_short (short) (+59.57)
  Triggered: EMA(8/16/25) = 2,412.31/2,414.45/2,414.68, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] AVAX-USD triple_ma_short (short) (+33.62)
  Triggered: EMA(8/16/25) = 7.19763/7.20666/7.2084, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] FET-USD triple_ma_short (short) (+16.07)
  Triggered: EMA(8/16/25) = 0.153907/0.154142/0.15417, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] ETH-USD breakdown_short (short) (+76.96)
  Triggered: broke range low 2,382 on vol 885 vs avg 860, trend EMA 2,393, 2-bar + retest
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] NEAR-USD triple_ma_short (short) (+2.69)
  Triggered: EMA(8/16/25) = 1.8507/1.85107/1.85353, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] XRP-USD triple_threat_long (long) (-35.99)
  Triggered: RSI 48->69 crossed 50, broke 1.34, trend EMA 1.33
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] ETH-USD triple_ma_long (long) (-54.73)
  Triggered: EMA(8/16/25) = 2,397.83/2,393.07/2,392.82, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] NEAR-USD triple_ma_long (long) (-56.81)
  Triggered: EMA(8/16/25) = 1.85803/1.85501/1.85486, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] BTC-USD dmi_dpo_short (short) (-85.23)
  Triggered: +DI 16.6 vs -DI 24.67, ADX 20.04, DPO -217.4 (period 50)
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] ETH-USD dmi_dpo_short (short) (-50.33)
  Triggered: +DI 17.99 vs -DI 25.44, ADX 24.88, DPO -4.641 (period 50)
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] SOL-USD dmi_dpo_short (short) (-65.06)
  Triggered: +DI 16.21 vs -DI 25.1, ADX 27.69, DPO -0.343 (period 50)
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] NEAR-USD triple_ma_short (short) (-35.92)
  Triggered: EMA(8/16/25) = 1.8506/1.8516/1.85257, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] FET-USD triple_ma_short (short) (-38.46)
  Triggered: EMA(8/16/25) = 0.151848/0.151939/0.152106, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] BTC-USD dmi_dpo_short (short) (+11.91)
  Triggered: +DI 17.05 vs -DI 22.45, ADX 20.04, DPO -597.7 (period 50)
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (win)

[WIN] SOL-USD dmi_dpo_short (short) (+36.27)
  Triggered: +DI 16.92 vs -DI 22.94, ADX 27.57, DPO -0.7818 (period 50)
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] ETH-USD triple_ma_long (long) (-29.47)
  Triggered: EMA(8/16/25) = 2,393.67/2,392.57/2,392.45, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] NEAR-USD triple_ma_short (short) (-15.31)
  Triggered: EMA(8/16/25) = 1.85035/1.85079/1.8515, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] SOL-USD triple_ma_short (short) (-43.13)
  Triggered: EMA(8/16/25) = 98.8323/98.8742/98.878, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] AVAX-USD triple_ma_short (short) (-40.25)
  Triggered: EMA(8/16/25) = 7.13743/7.13896/7.14016, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

Still open (too soon to say why it worked or not):
  FET-USD triple_ma_short (short) -- triggered: EMA(8/16/25) = 0.151886/0.15191/0.152017, freshly aligned
  ETH-USD triple_ma_short (short) -- triggered: EMA(8/16/25) = 2,390.63/2,391.11/2,391.47, freshly aligned
  XRP-USD triple_ma_long (long) -- triggered: EMA(8/16/25) = 1.33327/1.33325/1.33308, freshly aligned

**US -- WHY** (2026-09-02)
- Fired: 33 | Resolved: 29 | Still open: 4

[LOSS] CLF triple_ma_long (long) (-294.7)
  Triggered: EMA(8/16/25) = 11.6369/11.6364/11.6311, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] CLF triple_ma_long (long) (+504.9)
  Triggered: EMA(8/16/25) = 11.7/11.6703/11.6558, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] WFC triple_ma_long (long) (+674.1)
  Triggered: EMA(8/16/25) = 87.154/86.9684/86.9034, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] SNAP triple_threat_long (long) (+705.5)
  Triggered: RSI 49->61 crossed 50, broke 5.4, trend EMA 5.367
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] NEM triple_threat_long (long) (-240.2)
  Triggered: RSI 33->66 crossed 50, broke 124.7, trend EMA 124.3
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] CLF triple_threat_long (long) (+414)
  Triggered: RSI 37->62 crossed 50, broke 11.77, trend EMA 11.65
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] SIRI triple_ma_long (long) (+580.8)
  Triggered: EMA(8/16/25) = 28.4946/28.192/28.0992, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] DKNG triple_ma_long (long) (+90.34)
  Triggered: EMA(8/16/25) = 24.0754/23.873/23.8517, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] CLF triple_ma_long (long) (+488.4)
  Triggered: EMA(8/16/25) = 11.8581/11.7657/11.7219, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] WFC triple_ma_long (long) (+642.6)
  Triggered: EMA(8/16/25) = 87.7527/87.3419/87.1631, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] PYPL triple_ma_long (long) (+652.7)
  Triggered: EMA(8/16/25) = 52.9564/52.8225/52.8096, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] SIRI triple_ma_long (long) (+435.1)
  Triggered: EMA(8/16/25) = 28.5091/28.1996/28.1042, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] SNAP triple_ma_long (long) (-198.3)
  Triggered: EMA(8/16/25) = 5.43398/5.3936/5.39017, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] DKNG triple_ma_long (long) (-782.4)
  Triggered: EMA(8/16/25) = 24.111/23.8919/23.864, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] CLF triple_ma_long (long) (+153.3)
  Triggered: EMA(8/16/25) = 11.8826/11.7787/11.7304, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] NEM triple_ma_long (long) (-323.7)
  Triggered: EMA(8/16/25) = 124.965/124.511/124.495, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] WFC triple_ma_long (long) (+717.4)
  Triggered: EMA(8/16/25) = 87.7416/87.3361/87.1592, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] PYPL triple_ma_long (long) (+578.5)
  Triggered: EMA(8/16/25) = 52.9652/52.8271/52.8126, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] SIRI triple_ma_long (long) (+492.9)
  Triggered: EMA(8/16/25) = 28.5035/28.1967/28.1023, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] SNAP triple_ma_long (long) (+183.4)
  Triggered: EMA(8/16/25) = 5.42622/5.3895/5.38749, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] CLF triple_ma_long (long) (-291.1)
  Triggered: EMA(8/16/25) = 11.9032/11.7896/11.7375, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] DKNG triple_ma_long (long) (-693.8)
  Triggered: EMA(8/16/25) = 24.0854/23.8783/23.8552, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] NEM triple_ma_long (long) (-419.1)
  Triggered: EMA(8/16/25) = 124.943/124.499/124.487, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] WFC triple_ma_long (long) (+391.6)
  Triggered: EMA(8/16/25) = 87.8092/87.3719/87.1827, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] PYPL triple_ma_long (long) (+595.2)
  Triggered: EMA(8/16/25) = 52.9629/52.8259/52.8118, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] DAL triple_ma_long (long) (-103.1)
  Triggered: EMA(8/16/25) = 77.4083/77.0398/77.0272, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] KEY triple_ma_long (long) (+581.5)
  Triggered: EMA(8/16/25) = 21.4573/21.3749/21.3715, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] SOFI triple_ma_long (long) (+77.5)
  Triggered: EMA(8/16/25) = 17.5058/17.3851/17.3766, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] NEM triple_ma_long (long) (-60.21)
  Triggered: EMA(8/16/25) = 124.698/124.684/124.64, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

Still open (too soon to say why it worked or not):
  T triple_ma_long (long) -- triggered: EMA(8/16/25) = 26.1363/26.1272/26.1175, freshly aligned
  T triple_threat_long (long) -- triggered: RSI 39->60 crossed 50, broke 26.23, trend EMA 26.11
  F community_idea (long) -- triggered: no trigger detail logged (fired before trigger_context tracking started)
  HOOD triple_ma_long (long) -- triggered: EMA(8/16/25) = 104.947/104.574/104.52, freshly aligned

**INDIA FUTURES (MANUAL) -- WHY** (2026-09-02)
- Fired: 4 | Resolved: 4 | Still open: 0

[WIN] NIFTY-FUT triple_ma_short (short) (+81.64)
  Triggered: EMA(8/16/25) = 23,876/23,876.7/23,892.6, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (win)

[LOSS] NIFTY-FUT triple_ma_short (short) (-216.8)
  Triggered: EMA(8/16/25) = 23,875.5/23,876.2/23,891, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] SENSEX-FUT triple_ma_short (short) (-128.1)
  Triggered: EMA(8/16/25) = 76,450.6/76,450.9/76,495.4, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] SENSEX-FUT triple_ma_short (short) (-289)
  Triggered: EMA(8/16/25) = 76,445.8/76,448/76,490.1, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

---

