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

