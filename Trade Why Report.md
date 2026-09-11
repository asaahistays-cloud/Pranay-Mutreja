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

## 2026-09-03 00:11 IST

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

## 2026-09-04 00:00 IST

**INDIA -- WHY** (2026-09-03)
- Fired: 37 | Resolved: 35 | Still open: 2

[LOSS] RPOWER.NS triple_ma_long (long) (-3,009)
  Triggered: EMA(8/16/25) = 22.1389/22.105/22.0979, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] HUDCO.NS triple_ma_long (long) (-3,608)
  Triggered: EMA(8/16/25) = 179.952/178.661/178.192, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] COALINDIA.NS triple_ma_long (long) (-2,793)
  Triggered: EMA(8/16/25) = 420.191/418.171/416.38, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] BANKINDIA.NS triple_ma_long (long) (+320.6)
  Triggered: EMA(8/16/25) = 143.453/142.798/142.563, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] TATAPOWER.NS triple_ma_long (long) (-1,421)
  Triggered: EMA(8/16/25) = 364.284/362.091/360.315, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] UNIONBANK.NS triple_ma_long (long) (-962.8)
  Triggered: EMA(8/16/25) = 187.115/186.191/185.722, freshly aligned
  Outcome:   session ended before stop or target hit -- settled at the day's close (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via eod_settlement; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] INDIANB.NS triple_ma_long (long) (+2,420)
  Triggered: EMA(8/16/25) = 881.719/877.934/876.834, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] NMDC.NS triple_ma_long (long) (-2,375)
  Triggered: EMA(8/16/25) = 85.5671/85.2649/85.2106, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] IRCON.NS triple_ma_long (long) (-417.5)
  Triggered: EMA(8/16/25) = 118.815/118.446/118.389, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] SAIL.NS triple_ma_long (long) (-3,176)
  Triggered: EMA(8/16/25) = 196.824/195.822/195.311, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] NHPC.NS triple_ma_long (long) (-417.9)
  Triggered: EMA(8/16/25) = 76.1488/76.0683/76.02, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] IRFC.NS triple_ma_long (long) (+1,564)
  Triggered: EMA(8/16/25) = 82.6638/82.4965/82.4718, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] HUDCO.NS triple_ma_long (long) (-3,791)
  Triggered: EMA(8/16/25) = 180.746/179.232/178.602, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] RVNL.NS triple_ma_long (long) (-1,995)
  Triggered: EMA(8/16/25) = 207.961/206.986/206.822, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] BANKINDIA.NS triple_ma_long (long) (+481.1)
  Triggered: EMA(8/16/25) = 143.908/143.115/142.786, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] TATAPOWER.NS triple_ma_long (long) (-2,627)
  Triggered: EMA(8/16/25) = 365.468/362.977/361.022, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] UNIONBANK.NS triple_ma_long (long) (+659.9)
  Triggered: EMA(8/16/25) = 187.626/186.568/186.007, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] INDIANB.NS triple_ma_long (long) (+2,264)
  Triggered: EMA(8/16/25) = 884.364/879.781/878.115, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] COALINDIA.NS triple_ma_long (long) (+344.8)
  Triggered: EMA(8/16/25) = 421.125/418.903/416.992, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] IRCON.NS triple_ma_long (long) (-2,318)
  Triggered: EMA(8/16/25) = 119.181/118.682/118.547, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] YESBANK.NS triple_ma_long (long) (+0)
  Triggered: EMA(8/16/25) = 22.2339/22.135/22.0912, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] NMDC.NS triple_ma_long (long) (-3,828)
  Triggered: EMA(8/16/25) = 85.7095/85.3764/85.2868, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] RPOWER.NS triple_ma_long (long) (-3,424)
  Triggered: EMA(8/16/25) = 22.2081/22.1509/22.1292, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] SAIL.NS triple_ma_long (long) (-2,956)
  Triggered: EMA(8/16/25) = 197.199/196.138/195.552, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] NHPC.NS triple_ma_long (long) (-845.9)
  Triggered: EMA(8/16/25) = 76.302/76.1592/76.0831, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] IRFC.NS triple_ma_long (long) (-4,465)
  Triggered: EMA(8/16/25) = 82.8769/82.6288/82.5594, freshly aligned
  Outcome:   session ended before stop or target hit -- settled at the day's close (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via eod_settlement; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] SUZLON.NS triple_ma_long (long) (-1,931)
  Triggered: EMA(8/16/25) = 46.0058/45.8921/45.8777, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] NMDC.NS triple_ma_short (short) (+667.6)
  Triggered: EMA(8/16/25) = 85.0868/85.2195/85.24, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] COALINDIA.NS triple_ma_long (long) (-175.6)
  Triggered: EMA(8/16/25) = 420.194/420.19/419.191, freshly aligned
  Outcome:   session ended before stop or target hit -- settled at the day's close (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via eod_settlement; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] RPOWER.NS triple_ma_short (short) (+452.3)
  Triggered: EMA(8/16/25) = 22.1221/22.1298/22.13, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] SAIL.NS triple_ma_short (short) (-1,875)
  Triggered: EMA(8/16/25) = 195.187/195.494/195.524, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] IRFC.NS triple_ma_long (long) (-543.6)
  Triggered: EMA(8/16/25) = 82.8925/82.8903/82.8397, freshly aligned
  Outcome:   session ended before stop or target hit -- settled at the day's close (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via eod_settlement; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] SAIL.NS triple_ma_long (long) (-382.1)
  Triggered: EMA(8/16/25) = 195.749/195.706/195.64, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] NHPC.NS triple_ma_short (short) (-65.79)
  Triggered: EMA(8/16/25) = 76.2812/76.4006/76.4074, freshly aligned
  Outcome:   session ended before stop or target hit -- settled at the day's close (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via eod_settlement; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] IRCON.NS triple_ma_short (short) (-421.3)
  Triggered: EMA(8/16/25) = 118.839/118.972/118.976, freshly aligned
  Outcome:   session ended before stop or target hit -- settled at the day's close (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via eod_settlement; the market simply moved the other way this time (normal strategy variance, not a bug)

Still open (too soon to say why it worked or not):
  HINDCOPPER.NS triple_ma_long (long) -- triggered: EMA(8/16/25) = 523.02/522.054/521.86, freshly aligned
  GMRAIRPORT.NS triple_ma_long (long) -- triggered: EMA(8/16/25) = 94.398/94.1762/94.1019, freshly aligned

**CRYPTO -- WHY** (2026-09-03)
- Fired: 14 | Resolved: 13 | Still open: 1

[LOSS] NEAR-USD triple_ma_short (short) (-36.08)
  Triggered: EMA(8/16/25) = 1.84971/1.84992/1.85055, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] ETH-USD triple_ma_short (short) (-33)
  Triggered: EMA(8/16/25) = 2,389.87/2,390.13/2,390.42, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] SOL-USD dmi_dpo_short (short) (-13.41)
  Triggered: +DI 19.06 vs -DI 21.73, ADX 23.01, DPO -0.0278 (period 50)
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] ETH-USD triple_ma_long (long) (-20.82)
  Triggered: EMA(8/16/25) = 2,391.64/2,391.15/2,391.09, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] ETH-USD triple_ma_short (short) (+8.456)
  Triggered: EMA(8/16/25) = 2,389.62/2,390.14/2,390.45, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] FET-USD triple_ma_short (short) (-27.43)
  Triggered: EMA(8/16/25) = 0.15172/0.151756/0.15177, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] BTC-USD triple_ma_short (short) (-70.26)
  Triggered: EMA(8/16/25) = 77,143.3/77,197.8/77,204.6, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] AVAX-USD triple_ma_long (long) (+41.66)
  Triggered: EMA(8/16/25) = 7.17239/7.16848/7.16589, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] BTC-USD triple_ma_long (long) (+58.75)
  Triggered: EMA(8/16/25) = 77,216.4/77,199.9/77,197.6, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] NEAR-USD triple_ma_short (short) (+10.4)
  Triggered: EMA(8/16/25) = 1.88419/1.88714/1.88731, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] ETH-USD triple_ma_short (short) (-64.94)
  Triggered: EMA(8/16/25) = 2,397.28/2,399.52/2,399.6, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] SOL-USD triple_ma_short (short) (-75.1)
  Triggered: EMA(8/16/25) = 100.341/100.46/100.464, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] FET-USD triple_ma_short (short) (-41)
  Triggered: EMA(8/16/25) = 0.153796/0.15404/0.154053, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

Still open (too soon to say why it worked or not):
  FET-USD triple_ma_long (long) -- triggered: EMA(8/16/25) = 0.154215/0.154172/0.154135, freshly aligned

**US -- WHY** (2026-09-03)
- Fired: 41 | Resolved: 29 | Still open: 12

[WIN] CCL triple_ma_long (long) (+635.2)
  Triggered: EMA(8/16/25) = 23.5647/23.5404/23.5389, freshly aligned
  Outcome:   session ended before stop or target hit -- settled at the day's close (win)

[LOSS] NEM triple_ma_long (long) (+0)
  Triggered: EMA(8/16/25) = 124.552/124.456/124.451, freshly aligned
  Outcome:   session ended before stop or target hit -- settled at the day's close (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via eod_settlement; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] NEM triple_ma_long (long) (+110.8)
  Triggered: EMA(8/16/25) = 125.324/124.877/124.727, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] CLF triple_ma_long (long) (-1,108)
  Triggered: EMA(8/16/25) = 12.4498/12.3501/12.2604, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] CCL triple_ma_long (long) (-985.5)
  Triggered: EMA(8/16/25) = 23.6624/23.6/23.5777, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] HOOD triple_ma_long (long) (+908.7)
  Triggered: EMA(8/16/25) = 108.571/107.311/106.675, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] SNAP triple_ma_long (long) (+1,153)
  Triggered: EMA(8/16/25) = 5.65705/5.63445/5.60472, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] UBER triple_ma_long (long) (+594.4)
  Triggered: EMA(8/16/25) = 76.8091/76.7082/76.5654, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] KO triple_ma_long (long) (-174.1)
  Triggered: EMA(8/16/25) = 88.6333/88.6281/88.5861, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] SNAP triple_threat_long (long) (+65.65)
  Triggered: RSI 50->77 crossed 50, broke 5.7, trend EMA 5.602
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] UBER triple_threat_long (long) (-866.9)
  Triggered: RSI 28->72 crossed 50, broke 77.24, trend EMA 76.54
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] HOOD triple_ma_long (long) (+901.9)
  Triggered: EMA(8/16/25) = 113.58/110.486/108.916, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] PLTR triple_ma_long (long) (+344)
  Triggered: EMA(8/16/25) = 176.118/173.585/173.371, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] SNAP triple_ma_long (long) (-489.4)
  Triggered: EMA(8/16/25) = 5.80398/5.72566/5.67149, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] MARA triple_ma_long (long) (+3,752)
  Triggered: EMA(8/16/25) = 10.6028/10.4961/10.4371, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] LYFT triple_ma_long (long) (-1,176)
  Triggered: EMA(8/16/25) = 17.5745/17.4383/17.339, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] PINS triple_ma_long (long) (-1,002)
  Triggered: EMA(8/16/25) = 21.481/21.3713/21.3408, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] NEM triple_ma_long (long) (+314.7)
  Triggered: EMA(8/16/25) = 126.29/125.52/125.181, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] C triple_ma_long (long) (-373.7)
  Triggered: EMA(8/16/25) = 135.286/134.694/134.363, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] UBER triple_ma_long (long) (-1,037)
  Triggered: EMA(8/16/25) = 77.4304/77.0924/76.8486, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] RIVN triple_ma_long (long) (-239.6)
  Triggered: EMA(8/16/25) = 15.7045/15.6352/15.6094, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] HOOD triple_ma_long (long) (+768.6)
  Triggered: EMA(8/16/25) = 113.633/110.514/108.935, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] SNAP triple_ma_long (long) (-1,144)
  Triggered: EMA(8/16/25) = 5.79509/5.72095/5.66841, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] MARA triple_ma_long (long) (+1,908)
  Triggered: EMA(8/16/25) = 10.6262/10.5084/10.4452, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] NEM triple_ma_long (long) (+246.8)
  Triggered: EMA(8/16/25) = 126.299/125.525/125.184, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] LYFT triple_ma_long (long) (-1,271)
  Triggered: EMA(8/16/25) = 17.5656/17.4336/17.3359, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] PINS triple_ma_long (long) (-1,415)
  Triggered: EMA(8/16/25) = 21.4666/21.3637/21.3358, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] RIVN triple_ma_long (long) (-335.1)
  Triggered: EMA(8/16/25) = 15.7112/15.6387/15.6117, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] UBER triple_ma_long (long) (-1,641)
  Triggered: EMA(8/16/25) = 77.3971/77.0747/76.8371, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [STOP OVERSHOOT] intended risk 0.8046/unit, actual loss 1.32/unit (1.6x) -- price moved past the stop faster than the bot's bar-close check could exit; a violent move against the position, amplified by simulation lag rather than a bad entry call

Still open (too soon to say why it worked or not):
  F triple_ma_long (long) -- triggered: EMA(8/16/25) = 14.1066/14.0416/14, freshly aligned
  DKNG triple_ma_long (long) -- triggered: EMA(8/16/25) = 24.4638/24.4623/24.3971, freshly aligned
  PYPL triple_ma_long (long) -- triggered: EMA(8/16/25) = 54.4684/54.2836/54.0917, freshly aligned
  RIOT triple_ma_long (long) -- triggered: EMA(8/16/25) = 18.6545/18.5164/18.4052, freshly aligned
  RIVN triple_ma_long (long) -- triggered: EMA(8/16/25) = 15.6218/15.5802/15.5714, freshly aligned
  SOFI triple_ma_long (long) -- triggered: EMA(8/16/25) = 18.1527/18.0088/17.9033, freshly aligned
  PLTR triple_ma_long (long) -- triggered: EMA(8/16/25) = 176.343/173.704/173.449, freshly aligned
  RIOT triple_ma_long (long) -- triggered: EMA(8/16/25) = 18.8088/18.6366/18.5025, freshly aligned
  C triple_ma_long (long) -- triggered: EMA(8/16/25) = 135.503/134.877/134.509, freshly aligned
  LYFT triple_ma_long (long) -- triggered: EMA(8/16/25) = 17.3952/17.3939/17.3691, freshly aligned
  SNAP triple_ma_long (long) -- triggered: EMA(8/16/25) = 5.73741/5.73512/5.71957, freshly aligned
  PFE triple_ma_long (long) -- triggered: EMA(8/16/25) = 28.7942/28.7737/28.7735, freshly aligned

**INDIA FUTURES (MANUAL) -- WHY** (2026-09-03)
- Fired: 5 | Resolved: 5 | Still open: 0

[LOSS] BANKNIFTY-FUT triple_ma_long (long) (-917)
  Triggered: EMA(8/16/25) = 57,317.8/57,222.2/57,203.8, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] NIFTY-FUT triple_ma_long (long) (-797.4)
  Triggered: EMA(8/16/25) = 23,950.1/23,920.6/23,916.2, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] SENSEX-FUT triple_ma_long (long) (-887.5)
  Triggered: EMA(8/16/25) = 76,620.8/76,547.6/76,544.8, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] SENSEX-FUT triple_ma_long (long) (+33.28)
  Triggered: EMA(8/16/25) = 76,661.6/76,660.1/76,645.5, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (win)

[LOSS] SENSEX-FUT triple_ma_long (long) (-482.2)
  Triggered: EMA(8/16/25) = 76,662.6/76,660.5/76,649.7, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

---

## 2026-09-04 00:13 IST

**INDIA -- WHY** (2026-09-03)
- Fired: 37 | Resolved: 35 | Still open: 2

[LOSS] RPOWER.NS triple_ma_long (long) (-3,009)
  Triggered: EMA(8/16/25) = 22.1389/22.105/22.0979, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] HUDCO.NS triple_ma_long (long) (-3,608)
  Triggered: EMA(8/16/25) = 179.952/178.661/178.192, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] COALINDIA.NS triple_ma_long (long) (-2,793)
  Triggered: EMA(8/16/25) = 420.191/418.171/416.38, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] BANKINDIA.NS triple_ma_long (long) (+320.6)
  Triggered: EMA(8/16/25) = 143.453/142.798/142.563, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] TATAPOWER.NS triple_ma_long (long) (-1,421)
  Triggered: EMA(8/16/25) = 364.284/362.091/360.315, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] UNIONBANK.NS triple_ma_long (long) (-962.8)
  Triggered: EMA(8/16/25) = 187.115/186.191/185.722, freshly aligned
  Outcome:   session ended before stop or target hit -- settled at the day's close (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via eod_settlement; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] INDIANB.NS triple_ma_long (long) (+2,420)
  Triggered: EMA(8/16/25) = 881.719/877.934/876.834, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] NMDC.NS triple_ma_long (long) (-2,375)
  Triggered: EMA(8/16/25) = 85.5671/85.2649/85.2106, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] IRCON.NS triple_ma_long (long) (-417.5)
  Triggered: EMA(8/16/25) = 118.815/118.446/118.389, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] SAIL.NS triple_ma_long (long) (-3,176)
  Triggered: EMA(8/16/25) = 196.824/195.822/195.311, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] NHPC.NS triple_ma_long (long) (-417.9)
  Triggered: EMA(8/16/25) = 76.1488/76.0683/76.02, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] IRFC.NS triple_ma_long (long) (+1,564)
  Triggered: EMA(8/16/25) = 82.6638/82.4965/82.4718, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] HUDCO.NS triple_ma_long (long) (-3,791)
  Triggered: EMA(8/16/25) = 180.746/179.232/178.602, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] RVNL.NS triple_ma_long (long) (-1,995)
  Triggered: EMA(8/16/25) = 207.961/206.986/206.822, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] BANKINDIA.NS triple_ma_long (long) (+481.1)
  Triggered: EMA(8/16/25) = 143.908/143.115/142.786, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] TATAPOWER.NS triple_ma_long (long) (-2,627)
  Triggered: EMA(8/16/25) = 365.468/362.977/361.022, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] UNIONBANK.NS triple_ma_long (long) (+659.9)
  Triggered: EMA(8/16/25) = 187.626/186.568/186.007, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] INDIANB.NS triple_ma_long (long) (+2,264)
  Triggered: EMA(8/16/25) = 884.364/879.781/878.115, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] COALINDIA.NS triple_ma_long (long) (+344.8)
  Triggered: EMA(8/16/25) = 421.125/418.903/416.992, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] IRCON.NS triple_ma_long (long) (-2,318)
  Triggered: EMA(8/16/25) = 119.181/118.682/118.547, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] YESBANK.NS triple_ma_long (long) (+0)
  Triggered: EMA(8/16/25) = 22.2339/22.135/22.0912, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] NMDC.NS triple_ma_long (long) (-3,828)
  Triggered: EMA(8/16/25) = 85.7095/85.3764/85.2868, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] RPOWER.NS triple_ma_long (long) (-3,424)
  Triggered: EMA(8/16/25) = 22.2081/22.1509/22.1292, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] SAIL.NS triple_ma_long (long) (-2,956)
  Triggered: EMA(8/16/25) = 197.199/196.138/195.552, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] NHPC.NS triple_ma_long (long) (-845.9)
  Triggered: EMA(8/16/25) = 76.302/76.1592/76.0831, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] IRFC.NS triple_ma_long (long) (-4,465)
  Triggered: EMA(8/16/25) = 82.8769/82.6288/82.5594, freshly aligned
  Outcome:   session ended before stop or target hit -- settled at the day's close (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via eod_settlement; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] SUZLON.NS triple_ma_long (long) (-1,931)
  Triggered: EMA(8/16/25) = 46.0058/45.8921/45.8777, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] NMDC.NS triple_ma_short (short) (+667.6)
  Triggered: EMA(8/16/25) = 85.0868/85.2195/85.24, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] COALINDIA.NS triple_ma_long (long) (-175.6)
  Triggered: EMA(8/16/25) = 420.194/420.19/419.191, freshly aligned
  Outcome:   session ended before stop or target hit -- settled at the day's close (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via eod_settlement; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] RPOWER.NS triple_ma_short (short) (+452.3)
  Triggered: EMA(8/16/25) = 22.1221/22.1298/22.13, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] SAIL.NS triple_ma_short (short) (-1,875)
  Triggered: EMA(8/16/25) = 195.187/195.494/195.524, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] IRFC.NS triple_ma_long (long) (-543.6)
  Triggered: EMA(8/16/25) = 82.8925/82.8903/82.8397, freshly aligned
  Outcome:   session ended before stop or target hit -- settled at the day's close (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via eod_settlement; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] SAIL.NS triple_ma_long (long) (-382.1)
  Triggered: EMA(8/16/25) = 195.749/195.706/195.64, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] NHPC.NS triple_ma_short (short) (-65.79)
  Triggered: EMA(8/16/25) = 76.2812/76.4006/76.4074, freshly aligned
  Outcome:   session ended before stop or target hit -- settled at the day's close (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via eod_settlement; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] IRCON.NS triple_ma_short (short) (-421.3)
  Triggered: EMA(8/16/25) = 118.839/118.972/118.976, freshly aligned
  Outcome:   session ended before stop or target hit -- settled at the day's close (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via eod_settlement; the market simply moved the other way this time (normal strategy variance, not a bug)

Still open (too soon to say why it worked or not):
  HINDCOPPER.NS triple_ma_long (long) -- triggered: EMA(8/16/25) = 523.02/522.054/521.86, freshly aligned
  GMRAIRPORT.NS triple_ma_long (long) -- triggered: EMA(8/16/25) = 94.398/94.1762/94.1019, freshly aligned

**CRYPTO -- WHY** (2026-09-03)
- Fired: 14 | Resolved: 13 | Still open: 1

[LOSS] NEAR-USD triple_ma_short (short) (-36.08)
  Triggered: EMA(8/16/25) = 1.84971/1.84992/1.85055, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] ETH-USD triple_ma_short (short) (-33)
  Triggered: EMA(8/16/25) = 2,389.87/2,390.13/2,390.42, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] SOL-USD dmi_dpo_short (short) (-13.41)
  Triggered: +DI 19.06 vs -DI 21.73, ADX 23.01, DPO -0.0278 (period 50)
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] ETH-USD triple_ma_long (long) (-20.82)
  Triggered: EMA(8/16/25) = 2,391.64/2,391.15/2,391.09, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] ETH-USD triple_ma_short (short) (+8.456)
  Triggered: EMA(8/16/25) = 2,389.62/2,390.14/2,390.45, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] FET-USD triple_ma_short (short) (-27.43)
  Triggered: EMA(8/16/25) = 0.15172/0.151756/0.15177, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] BTC-USD triple_ma_short (short) (-70.26)
  Triggered: EMA(8/16/25) = 77,143.3/77,197.8/77,204.6, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] AVAX-USD triple_ma_long (long) (+41.66)
  Triggered: EMA(8/16/25) = 7.17239/7.16848/7.16589, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] BTC-USD triple_ma_long (long) (+58.75)
  Triggered: EMA(8/16/25) = 77,216.4/77,199.9/77,197.6, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] NEAR-USD triple_ma_short (short) (+10.4)
  Triggered: EMA(8/16/25) = 1.88419/1.88714/1.88731, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] ETH-USD triple_ma_short (short) (-64.94)
  Triggered: EMA(8/16/25) = 2,397.28/2,399.52/2,399.6, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] SOL-USD triple_ma_short (short) (-75.1)
  Triggered: EMA(8/16/25) = 100.341/100.46/100.464, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] FET-USD triple_ma_short (short) (-41)
  Triggered: EMA(8/16/25) = 0.153796/0.15404/0.154053, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

Still open (too soon to say why it worked or not):
  FET-USD triple_ma_long (long) -- triggered: EMA(8/16/25) = 0.154215/0.154172/0.154135, freshly aligned

**US -- WHY** (2026-09-03)
- Fired: 41 | Resolved: 31 | Still open: 10

[WIN] CCL triple_ma_long (long) (+635.2)
  Triggered: EMA(8/16/25) = 23.5647/23.5404/23.5389, freshly aligned
  Outcome:   session ended before stop or target hit -- settled at the day's close (win)

[LOSS] NEM triple_ma_long (long) (+0)
  Triggered: EMA(8/16/25) = 124.552/124.456/124.451, freshly aligned
  Outcome:   session ended before stop or target hit -- settled at the day's close (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via eod_settlement; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] NEM triple_ma_long (long) (+110.8)
  Triggered: EMA(8/16/25) = 125.324/124.877/124.727, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] CLF triple_ma_long (long) (-1,108)
  Triggered: EMA(8/16/25) = 12.4498/12.3501/12.2604, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] CCL triple_ma_long (long) (-985.5)
  Triggered: EMA(8/16/25) = 23.6624/23.6/23.5777, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] HOOD triple_ma_long (long) (+908.7)
  Triggered: EMA(8/16/25) = 108.571/107.311/106.675, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] SNAP triple_ma_long (long) (+1,153)
  Triggered: EMA(8/16/25) = 5.65705/5.63445/5.60472, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] UBER triple_ma_long (long) (+594.4)
  Triggered: EMA(8/16/25) = 76.8091/76.7082/76.5654, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] KO triple_ma_long (long) (-174.1)
  Triggered: EMA(8/16/25) = 88.6333/88.6281/88.5861, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] SNAP triple_threat_long (long) (+65.65)
  Triggered: RSI 50->77 crossed 50, broke 5.7, trend EMA 5.602
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] UBER triple_threat_long (long) (-866.9)
  Triggered: RSI 28->72 crossed 50, broke 77.24, trend EMA 76.54
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] HOOD triple_ma_long (long) (+901.9)
  Triggered: EMA(8/16/25) = 113.58/110.486/108.916, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] PLTR triple_ma_long (long) (+344)
  Triggered: EMA(8/16/25) = 176.118/173.585/173.371, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] SNAP triple_ma_long (long) (-489.4)
  Triggered: EMA(8/16/25) = 5.80398/5.72566/5.67149, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] MARA triple_ma_long (long) (+3,752)
  Triggered: EMA(8/16/25) = 10.6028/10.4961/10.4371, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] LYFT triple_ma_long (long) (-1,176)
  Triggered: EMA(8/16/25) = 17.5745/17.4383/17.339, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] PINS triple_ma_long (long) (-1,002)
  Triggered: EMA(8/16/25) = 21.481/21.3713/21.3408, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] NEM triple_ma_long (long) (+314.7)
  Triggered: EMA(8/16/25) = 126.29/125.52/125.181, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] C triple_ma_long (long) (-373.7)
  Triggered: EMA(8/16/25) = 135.286/134.694/134.363, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] UBER triple_ma_long (long) (-1,037)
  Triggered: EMA(8/16/25) = 77.4304/77.0924/76.8486, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] RIVN triple_ma_long (long) (-239.6)
  Triggered: EMA(8/16/25) = 15.7045/15.6352/15.6094, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] HOOD triple_ma_long (long) (+768.6)
  Triggered: EMA(8/16/25) = 113.633/110.514/108.935, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] SNAP triple_ma_long (long) (-1,144)
  Triggered: EMA(8/16/25) = 5.79509/5.72095/5.66841, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] MARA triple_ma_long (long) (+1,908)
  Triggered: EMA(8/16/25) = 10.6262/10.5084/10.4452, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] NEM triple_ma_long (long) (+246.8)
  Triggered: EMA(8/16/25) = 126.299/125.525/125.184, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] LYFT triple_ma_long (long) (-1,271)
  Triggered: EMA(8/16/25) = 17.5656/17.4336/17.3359, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] PINS triple_ma_long (long) (-1,415)
  Triggered: EMA(8/16/25) = 21.4666/21.3637/21.3358, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] RIVN triple_ma_long (long) (-335.1)
  Triggered: EMA(8/16/25) = 15.7112/15.6387/15.6117, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] UBER triple_ma_long (long) (-1,641)
  Triggered: EMA(8/16/25) = 77.3971/77.0747/76.8371, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [STOP OVERSHOOT] intended risk 0.8046/unit, actual loss 1.32/unit (1.6x) -- price moved past the stop faster than the bot's bar-close check could exit; a violent move against the position, amplified by simulation lag rather than a bad entry call

[LOSS] LYFT triple_ma_long (long) (-182.3)
  Triggered: EMA(8/16/25) = 17.3952/17.3939/17.3691, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] PFE triple_ma_long (long) (-52.01)
  Triggered: EMA(8/16/25) = 28.7942/28.7737/28.7735, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

Still open (too soon to say why it worked or not):
  F triple_ma_long (long) -- triggered: EMA(8/16/25) = 14.1066/14.0416/14, freshly aligned
  DKNG triple_ma_long (long) -- triggered: EMA(8/16/25) = 24.4638/24.4623/24.3971, freshly aligned
  PYPL triple_ma_long (long) -- triggered: EMA(8/16/25) = 54.4684/54.2836/54.0917, freshly aligned
  RIOT triple_ma_long (long) -- triggered: EMA(8/16/25) = 18.6545/18.5164/18.4052, freshly aligned
  RIVN triple_ma_long (long) -- triggered: EMA(8/16/25) = 15.6218/15.5802/15.5714, freshly aligned
  SOFI triple_ma_long (long) -- triggered: EMA(8/16/25) = 18.1527/18.0088/17.9033, freshly aligned
  PLTR triple_ma_long (long) -- triggered: EMA(8/16/25) = 176.343/173.704/173.449, freshly aligned
  RIOT triple_ma_long (long) -- triggered: EMA(8/16/25) = 18.8088/18.6366/18.5025, freshly aligned
  C triple_ma_long (long) -- triggered: EMA(8/16/25) = 135.503/134.877/134.509, freshly aligned
  SNAP triple_ma_long (long) -- triggered: EMA(8/16/25) = 5.73741/5.73512/5.71957, freshly aligned

**INDIA FUTURES (MANUAL) -- WHY** (2026-09-03)
- Fired: 5 | Resolved: 5 | Still open: 0

[LOSS] BANKNIFTY-FUT triple_ma_long (long) (-917)
  Triggered: EMA(8/16/25) = 57,317.8/57,222.2/57,203.8, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] NIFTY-FUT triple_ma_long (long) (-797.4)
  Triggered: EMA(8/16/25) = 23,950.1/23,920.6/23,916.2, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] SENSEX-FUT triple_ma_long (long) (-887.5)
  Triggered: EMA(8/16/25) = 76,620.8/76,547.6/76,544.8, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] SENSEX-FUT triple_ma_long (long) (+33.28)
  Triggered: EMA(8/16/25) = 76,661.6/76,660.1/76,645.5, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (win)

[LOSS] SENSEX-FUT triple_ma_long (long) (-482.2)
  Triggered: EMA(8/16/25) = 76,662.6/76,660.5/76,649.7, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

---

## 2026-09-05 00:00 IST

**INDIA -- WHY** (2026-09-04)
- Fired: 20 | Resolved: 20 | Still open: 0

[WIN] IOB.NS triple_ma_long (long) (+2,438)
  Triggered: EMA(8/16/25) = 33.1635/33.1586/33.0997, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] UNIONBANK.NS triple_ma_short (short) (-1,840)
  Triggered: EMA(8/16/25) = 187.798/188.118/188.123, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] VEDL.NS triple_ma_long (long) (-2,139)
  Triggered: EMA(8/16/25) = 270.232/269.919/269.887, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] GAIL.NS triple_ma_short (short) (+115.9)
  Triggered: EMA(8/16/25) = 173.063/173.275/173.296, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] PNB.NS triple_ma_long (long) (+1,705)
  Triggered: EMA(8/16/25) = 117.099/117.067/117.065, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] UNIONBANK.NS triple_ma_long (long) (+688.8)
  Triggered: EMA(8/16/25) = 188.385/188.355/188.287, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] GAIL.NS breakdown_short (short) (+522.4)
  Triggered: broke range low 172.4 on vol 184,102 vs avg 141,938, trend EMA 172.9; India gate: RSI 36.34 / VWAP 173.2 (rsi<40 and close<=vwap)
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] INDIANB.NS triple_ma_long (long) (-2,075)
  Triggered: EMA(8/16/25) = 888.305/887.523/887.431, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] INDIANB.NS triple_ma_long (long) (+816.2)
  Triggered: EMA(8/16/25) = 887.697/887.247/887.226, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] BEL.NS triple_ma_short (short) (-122.6)
  Triggered: EMA(8/16/25) = 408.569/409.033/409.051, freshly aligned
  Outcome:   session ended before stop or target hit -- settled at the day's close (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via eod_settlement; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] BEL.NS triple_ma_short (short) (-122.6)
  Triggered: EMA(8/16/25) = 408.524/408.963/409.011, freshly aligned
  Outcome:   session ended before stop or target hit -- settled at the day's close (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via eod_settlement; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] ONGC.NS triple_ma_short (short) (+149.1)
  Triggered: EMA(8/16/25) = 234.775/234.78/234.903, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] PAYTM.NS triple_ma_long (long) (-855.8)
  Triggered: EMA(8/16/25) = 1,667.93/1,667.7/1,663.78, freshly aligned
  Outcome:   session ended before stop or target hit -- settled at the day's close (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via eod_settlement; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] BHEL.NS triple_ma_long (long) (-806.6)
  Triggered: EMA(8/16/25) = 433.139/433.029/432.624, freshly aligned
  Outcome:   session ended before stop or target hit -- settled at the day's close (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via eod_settlement; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] INDIANB.NS triple_ma_short (short) (+500.8)
  Triggered: EMA(8/16/25) = 886.944/887.393/887.402, freshly aligned
  Outcome:   session ended before stop or target hit -- settled at the day's close (win)

[LOSS] ETERNAL.NS breakdown_short (short) (-1,166)
  Triggered: broke range low 322.1 on vol 981,877 vs avg 530,336, trend EMA 322.8; India gate: RSI 29.27 / VWAP 324.3 (rsi<40 and close<=vwap)
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] PAYTM.NS triple_ma_long (long) (-617.1)
  Triggered: EMA(8/16/25) = 1,667.47/1,667.45/1,663.87, freshly aligned
  Outcome:   session ended before stop or target hit -- settled at the day's close (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via eod_settlement; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] UNIONBANK.NS triple_ma_short (short) (+453)
  Triggered: EMA(8/16/25) = 188.236/188.455/188.467, freshly aligned
  Outcome:   session ended before stop or target hit -- settled at the day's close (win)

[LOSS] GAIL.NS triple_ma_long (long) (-57.61)
  Triggered: EMA(8/16/25) = 173.194/173.06/173.053, freshly aligned
  Outcome:   session ended before stop or target hit -- settled at the day's close (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via eod_settlement; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] BEL.NS breakdown_short (short) (-1,167)
  Triggered: broke range low 407.2 on vol 1,076,849 vs avg 192,950, trend EMA 408; India gate: RSI 30.0 / VWAP 409.6 (rsi<40 and close<=vwap)
  Outcome:   session ended before stop or target hit -- settled at the day's close (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via eod_settlement; the market simply moved the other way this time (normal strategy variance, not a bug)

**CRYPTO -- WHY** (2026-09-04)
- Fired: 44 | Resolved: 40 | Still open: 4

[LOSS] XRP-USD oi_divergence_long (long) (+0)
  Triggered: price_chg_1h=-0.007829, oi_chg_1h=-0.027991, oi_at_entry=122844456.7893
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] XRP-USD oi_divergence_long (long) (+0)
  Triggered: price_chg_1h=-0.011801, oi_chg_1h=-0.01217, oi_at_entry=123669212.6097
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] NEAR-USD oi_divergence_long (long) (-102.7)
  Triggered: price_chg_1h=-0.009067, oi_chg_1h=-0.010398, oi_at_entry=26682518.902
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] SOL-USD oi_divergence_long (long) (+12.74)
  Triggered: price_chg_1h=-0.008764, oi_chg_1h=-0.012349, oi_at_entry=342612704.2511
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (win)

[LOSS] FET-USD triple_ma_short (short) (-126.8)
  Triggered: EMA(8/16/25) = 0.157838/0.158405/0.158457, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] NEAR-USD triple_ma_short (short) (+3.975)
  Triggered: EMA(8/16/25) = 1.96265/1.96946/1.96948, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] SOL-USD triple_ma_short (short) (+7.787)
  Triggered: EMA(8/16/25) = 104.121/104.369/104.374, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] XRP-USD triple_ma_short (short) (-54.65)
  Triggered: EMA(8/16/25) = 1.44823/1.4522/1.45254, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] FET-USD triple_ma_short (short) (-46.73)
  Triggered: EMA(8/16/25) = 0.157984/0.15799/0.158029, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] BTC-USD triple_ma_short (short) (-42.16)
  Triggered: EMA(8/16/25) = 80,904.7/81,026/81,035.4, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] NEAR-USD triple_ma_short (short) (+13.06)
  Triggered: EMA(8/16/25) = 1.94989/1.95011/1.95171, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] SOL-USD triple_ma_short (short) (+12.17)
  Triggered: EMA(8/16/25) = 103.863/103.865/103.908, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] AVAX-USD triple_ma_short (short) (+38.22)
  Triggered: EMA(8/16/25) = 7.49774/7.50026/7.50067, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] NEAR-USD oi_divergence_long (long) (-105.2)
  Triggered: price_chg_1h=-0.011588, oi_chg_1h=-0.013151, oi_at_entry=26317687.152
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] FET-USD triple_ma_short (short) (+28.85)
  Triggered: EMA(8/16/25) = 0.158057/0.158198/0.158219, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] NEAR-USD oi_divergence_long (long) (-14.86)
  Triggered: price_chg_1h=-0.010633, oi_chg_1h=-0.011927, oi_at_entry=26114966.874
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] BTC-USD triple_ma_short (short) (-30.06)
  Triggered: EMA(8/16/25) = 80,932.8/80,960/80,974.1, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] XRP-USD triple_ma_short (short) (+0)
  Triggered: EMA(8/16/25) = 1.44739/1.44792/1.44829, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] NEAR-USD oi_divergence_long (long) (+129.4)
  Triggered: price_chg_1h=-0.010022, oi_chg_1h=-0.012088, oi_at_entry=26718173.817
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (win)

[LOSS] BTC-USD triple_ma_long (long) (-232.2)
  Triggered: EMA(8/16/25) = 81,023/80,974.6/80,968.3, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] XRP-USD oi_divergence_long (long) (+0.9629)
  Triggered: price_chg_1h=-0.005566, oi_chg_1h=-0.010473, oi_at_entry=123187505.1812
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (win)

[LOSS] FET-USD triple_ma_short (short) (-53.21)
  Triggered: EMA(8/16/25) = 0.157022/0.157052/0.157153, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] XRP-USD triple_ma_short (short) (-33.14)
  Triggered: EMA(8/16/25) = 1.44901/1.4492/1.44924, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] NEAR-USD oi_divergence_long (long) (+21.8)
  Triggered: price_chg_1h=-0.00584, oi_chg_1h=-0.01715, oi_at_entry=27139768.746
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (win)

[LOSS] XRP-USD triple_ma_long (long) (-202.6)
  Triggered: EMA(8/16/25) = 1.44964/1.44944/1.44939, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] SOL-USD oi_divergence_long (long) (+6.696)
  Triggered: price_chg_1h=-0.027882, oi_chg_1h=-0.066226, oi_at_entry=314264125.3695
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (win)

[WIN] BTC-USD triple_ma_short (short) (+12.52)
  Triggered: EMA(8/16/25) = 80,880.6/80,972.9/80,990, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] SOL-USD triple_ma_short (short) (+15.91)
  Triggered: EMA(8/16/25) = 103.569/103.783/103.847, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] XRP-USD oi_divergence_long (long) (-7.89)
  Triggered: price_chg_1h=-0.028021, oi_chg_1h=-0.068621, oi_at_entry=115593782.3832
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] AVAX-USD oi_divergence_long (long) (-0.7322)
  Triggered: price_chg_1h=-0.017726, oi_chg_1h=-0.018786, oi_at_entry=11542937.2204
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] NEAR-USD oi_divergence_long (long) (-23.89)
  Triggered: price_chg_1h=-0.035748, oi_chg_1h=-0.057961, oi_at_entry=25881868.444
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] XRP-USD triple_ma_short (short) (+48.87)
  Triggered: EMA(8/16/25) = 1.4356/1.44197/1.44453, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] AVAX-USD oi_divergence_long (long) (+48.19)
  Triggered: price_chg_1h=-0.018417, oi_chg_1h=-0.011054, oi_at_entry=11634108.1344
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] NEAR-USD triple_ma_short (short) (+31.77)
  Triggered: EMA(8/16/25) = 1.97109/1.97899/1.97981, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] NEAR-USD oi_divergence_long (long) (+15.22)
  Triggered: price_chg_1h=-0.010245, oi_chg_1h=-0.013743, oi_at_entry=25796498.035
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (win)

[WIN] AVAX-USD oi_divergence_long (long) (+65.23)
  Triggered: price_chg_1h=-0.005153, oi_chg_1h=-0.011272, oi_at_entry=11468599.2995
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (win)

[WIN] SOL-USD oi_divergence_long (long) (+4.348)
  Triggered: price_chg_1h=-0.009927, oi_chg_1h=-0.014382, oi_at_entry=315803491.8433
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (win)

[WIN] XRP-USD oi_divergence_long (long) (+11.73)
  Triggered: price_chg_1h=-0.012194, oi_chg_1h=-0.012026, oi_at_entry=114080035.7917
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (win)

[LOSS] AVAX-USD oi_divergence_long (long) (-5.501)
  Triggered: price_chg_1h=-0.006494, oi_chg_1h=-0.023091, oi_at_entry=11276355.7047
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] SOL-USD oi_divergence_long (long) (-20.59)
  Triggered: price_chg_1h=-0.005982, oi_chg_1h=-0.010749, oi_at_entry=323593098.5743
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

Still open (too soon to say why it worked or not):
  ETH-USD triple_ma_short (short) -- triggered: EMA(8/16/25) = 2,508.79/2,514.52/2,515.19, freshly aligned
  FET-USD triple_ma_short (short) -- triggered: EMA(8/16/25) = 0.156971/0.157135/0.157191, freshly aligned
  AVAX-USD triple_ma_short (short) -- triggered: EMA(8/16/25) = 7.44825/7.4697/7.47841, freshly aligned
  XRP-USD oi_divergence_long (long) -- triggered: price_chg_1h=-0.008324, oi_chg_1h=-0.016124, oi_at_entry=115156707.0114

**US -- WHY** (2026-09-04)
- Fired: 28 | Resolved: 25 | Still open: 3

[LOSS] PFE triple_ma_long (long) (-346.8)
  Triggered: EMA(8/16/25) = 28.8007/28.7795/28.7781, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] NCLH triple_ma_long (long) (+128.6)
  Triggered: EMA(8/16/25) = 15.514/15.4925/15.4917, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (win)

[WIN] PFE triple_ma_long (long) (+278.4)
  Triggered: EMA(8/16/25) = 28.7831/28.7804/28.7789, freshly aligned
  Outcome:   session ended before stop or target hit -- settled at the day's close (win)

[LOSS] NCLH triple_ma_long (long) (+0)
  Triggered: EMA(8/16/25) = 15.5217/15.4966/15.4944, freshly aligned
  Outcome:   session ended before stop or target hit -- settled at the day's close (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via eod_settlement; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] RIOT triple_ma_long (long) (+242.7)
  Triggered: EMA(8/16/25) = 20.9796/20.7726/20.488, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] SOFI triple_ma_long (long) (-437.6)
  Triggered: EMA(8/16/25) = 18.4949/18.4716/18.3886, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] MARA triple_ma_long (long) (-309)
  Triggered: EMA(8/16/25) = 11.5767/11.5169/11.4003, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] INTC triple_ma_long (long) (+553.2)
  Triggered: EMA(8/16/25) = 91.8037/91.4268/91.0872, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] SIRI triple_ma_long (long) (-747.2)
  Triggered: EMA(8/16/25) = 29.8806/29.8608/29.7955, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] WFC triple_ma_long (long) (-266.5)
  Triggered: EMA(8/16/25) = 89.1699/89.1571/89.1485, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] GOLD triple_ma_long (long) (+664)
  Triggered: EMA(8/16/25) = 42.0252/41.4495/41.3518, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] GOLD triple_ma_long (long) (+225)
  Triggered: EMA(8/16/25) = 42.8302/41.9585/41.695, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] INTC triple_ma_long (long) (+44.78)
  Triggered: EMA(8/16/25) = 93.0039/92.1832/91.6454, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] MARA triple_ma_long (long) (-466.8)
  Triggered: EMA(8/16/25) = 11.4948/11.4824/11.3953, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] RIOT triple_ma_long (long) (-65.58)
  Triggered: EMA(8/16/25) = 21.134/20.9038/20.6189, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] GOLD triple_ma_long (long) (+574.9)
  Triggered: EMA(8/16/25) = 42.7913/41.9379/41.6815, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] INTC triple_ma_long (long) (+204.5)
  Triggered: EMA(8/16/25) = 92.9594/92.1597/91.63, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] MARA triple_ma_long (long) (-342.3)
  Triggered: EMA(8/16/25) = 11.4904/11.48/11.3937, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] RIOT triple_ma_long (long) (-221.3)
  Triggered: EMA(8/16/25) = 21.1562/20.9156/20.6265, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] GOLD triple_ma_long (long) (+262)
  Triggered: EMA(8/16/25) = 42.8136/41.9496/41.6892, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] INTC triple_ma_long (long) (+27.71)
  Triggered: EMA(8/16/25) = 93.0072/92.185/91.6466, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] MARA triple_ma_long (long) (-356.8)
  Triggered: EMA(8/16/25) = 11.4926/11.4812/11.3945, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] RIOT triple_ma_long (long) (-472.1)
  Triggered: EMA(8/16/25) = 21.1784/20.9273/20.6342, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] DAL triple_ma_long (long) (+88.98)
  Triggered: EMA(8/16/25) = 79.2837/78.967/78.7605, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] C triple_ma_long (long) (+163.8)
  Triggered: EMA(8/16/25) = 136.956/136.897/136.885, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

Still open (too soon to say why it worked or not):
  HOOD triple_ma_long (long) -- triggered: EMA(8/16/25) = 123.468/122.822/121.281, freshly aligned
  NCLH triple_ma_long (long) -- triggered: EMA(8/16/25) = 15.5324/15.505/15.4994, freshly aligned
  NKE triple_ma_long (long) -- triggered: EMA(8/16/25) = 38.4369/38.4154/38.4145, freshly aligned

**INDIA FUTURES (MANUAL) -- WHY** (2026-09-04)
- Fired: 5 | Resolved: 5 | Still open: 0

[WIN] NIFTY-FUT triple_ma_long (long) (+220.3)
  Triggered: EMA(8/16/25) = 23,926.2/23,922.2/23,921.7, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] SENSEX-FUT triple_ma_long (long) (-397.1)
  Triggered: EMA(8/16/25) = 76,637.3/76,616.7/76,612.8, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] BANKNIFTY-FUT triple_ma_long (long) (-302)
  Triggered: EMA(8/16/25) = 57,467.2/57,466.5/57,460.8, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] NIFTY-FUT triple_ma_long (long) (-78.31)
  Triggered: EMA(8/16/25) = 23,946.4/23,945.9/23,941.5, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] NIFTY-FUT triple_ma_long (long) (-228.6)
  Triggered: EMA(8/16/25) = 23,945.5/23,945.5/23,942.1, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

---

## 2026-09-05 00:08 IST

**INDIA -- WHY** (2026-09-04)
- Fired: 20 | Resolved: 20 | Still open: 0

[WIN] IOB.NS triple_ma_long (long) (+2,438)
  Triggered: EMA(8/16/25) = 33.1635/33.1586/33.0997, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] UNIONBANK.NS triple_ma_short (short) (-1,840)
  Triggered: EMA(8/16/25) = 187.798/188.118/188.123, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] VEDL.NS triple_ma_long (long) (-2,139)
  Triggered: EMA(8/16/25) = 270.232/269.919/269.887, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] GAIL.NS triple_ma_short (short) (+115.9)
  Triggered: EMA(8/16/25) = 173.063/173.275/173.296, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] PNB.NS triple_ma_long (long) (+1,705)
  Triggered: EMA(8/16/25) = 117.099/117.067/117.065, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] UNIONBANK.NS triple_ma_long (long) (+688.8)
  Triggered: EMA(8/16/25) = 188.385/188.355/188.287, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] GAIL.NS breakdown_short (short) (+522.4)
  Triggered: broke range low 172.4 on vol 184,102 vs avg 141,938, trend EMA 172.9; India gate: RSI 36.34 / VWAP 173.2 (rsi<40 and close<=vwap)
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] INDIANB.NS triple_ma_long (long) (-2,075)
  Triggered: EMA(8/16/25) = 888.305/887.523/887.431, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] INDIANB.NS triple_ma_long (long) (+816.2)
  Triggered: EMA(8/16/25) = 887.697/887.247/887.226, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] BEL.NS triple_ma_short (short) (-122.6)
  Triggered: EMA(8/16/25) = 408.569/409.033/409.051, freshly aligned
  Outcome:   session ended before stop or target hit -- settled at the day's close (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via eod_settlement; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] BEL.NS triple_ma_short (short) (-122.6)
  Triggered: EMA(8/16/25) = 408.524/408.963/409.011, freshly aligned
  Outcome:   session ended before stop or target hit -- settled at the day's close (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via eod_settlement; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] ONGC.NS triple_ma_short (short) (+149.1)
  Triggered: EMA(8/16/25) = 234.775/234.78/234.903, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] PAYTM.NS triple_ma_long (long) (-855.8)
  Triggered: EMA(8/16/25) = 1,667.93/1,667.7/1,663.78, freshly aligned
  Outcome:   session ended before stop or target hit -- settled at the day's close (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via eod_settlement; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] BHEL.NS triple_ma_long (long) (-806.6)
  Triggered: EMA(8/16/25) = 433.139/433.029/432.624, freshly aligned
  Outcome:   session ended before stop or target hit -- settled at the day's close (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via eod_settlement; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] INDIANB.NS triple_ma_short (short) (+500.8)
  Triggered: EMA(8/16/25) = 886.944/887.393/887.402, freshly aligned
  Outcome:   session ended before stop or target hit -- settled at the day's close (win)

[LOSS] ETERNAL.NS breakdown_short (short) (-1,166)
  Triggered: broke range low 322.1 on vol 981,877 vs avg 530,336, trend EMA 322.8; India gate: RSI 29.27 / VWAP 324.3 (rsi<40 and close<=vwap)
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] PAYTM.NS triple_ma_long (long) (-617.1)
  Triggered: EMA(8/16/25) = 1,667.47/1,667.45/1,663.87, freshly aligned
  Outcome:   session ended before stop or target hit -- settled at the day's close (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via eod_settlement; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] UNIONBANK.NS triple_ma_short (short) (+453)
  Triggered: EMA(8/16/25) = 188.236/188.455/188.467, freshly aligned
  Outcome:   session ended before stop or target hit -- settled at the day's close (win)

[LOSS] GAIL.NS triple_ma_long (long) (-57.61)
  Triggered: EMA(8/16/25) = 173.194/173.06/173.053, freshly aligned
  Outcome:   session ended before stop or target hit -- settled at the day's close (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via eod_settlement; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] BEL.NS breakdown_short (short) (-1,167)
  Triggered: broke range low 407.2 on vol 1,076,849 vs avg 192,950, trend EMA 408; India gate: RSI 30.0 / VWAP 409.6 (rsi<40 and close<=vwap)
  Outcome:   session ended before stop or target hit -- settled at the day's close (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via eod_settlement; the market simply moved the other way this time (normal strategy variance, not a bug)

**CRYPTO -- WHY** (2026-09-04)
- Fired: 44 | Resolved: 40 | Still open: 4

[LOSS] XRP-USD oi_divergence_long (long) (+0)
  Triggered: price_chg_1h=-0.007829, oi_chg_1h=-0.027991, oi_at_entry=122844456.7893
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] XRP-USD oi_divergence_long (long) (+0)
  Triggered: price_chg_1h=-0.011801, oi_chg_1h=-0.01217, oi_at_entry=123669212.6097
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] NEAR-USD oi_divergence_long (long) (-102.7)
  Triggered: price_chg_1h=-0.009067, oi_chg_1h=-0.010398, oi_at_entry=26682518.902
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] SOL-USD oi_divergence_long (long) (+12.74)
  Triggered: price_chg_1h=-0.008764, oi_chg_1h=-0.012349, oi_at_entry=342612704.2511
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (win)

[LOSS] FET-USD triple_ma_short (short) (-126.8)
  Triggered: EMA(8/16/25) = 0.157838/0.158405/0.158457, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] NEAR-USD triple_ma_short (short) (+3.975)
  Triggered: EMA(8/16/25) = 1.96265/1.96946/1.96948, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] SOL-USD triple_ma_short (short) (+7.787)
  Triggered: EMA(8/16/25) = 104.121/104.369/104.374, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] XRP-USD triple_ma_short (short) (-54.65)
  Triggered: EMA(8/16/25) = 1.44823/1.4522/1.45254, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] FET-USD triple_ma_short (short) (-46.73)
  Triggered: EMA(8/16/25) = 0.157984/0.15799/0.158029, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] BTC-USD triple_ma_short (short) (-42.16)
  Triggered: EMA(8/16/25) = 80,904.7/81,026/81,035.4, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] NEAR-USD triple_ma_short (short) (+13.06)
  Triggered: EMA(8/16/25) = 1.94989/1.95011/1.95171, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] SOL-USD triple_ma_short (short) (+12.17)
  Triggered: EMA(8/16/25) = 103.863/103.865/103.908, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] AVAX-USD triple_ma_short (short) (+38.22)
  Triggered: EMA(8/16/25) = 7.49774/7.50026/7.50067, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] NEAR-USD oi_divergence_long (long) (-105.2)
  Triggered: price_chg_1h=-0.011588, oi_chg_1h=-0.013151, oi_at_entry=26317687.152
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] FET-USD triple_ma_short (short) (+28.85)
  Triggered: EMA(8/16/25) = 0.158057/0.158198/0.158219, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] NEAR-USD oi_divergence_long (long) (-14.86)
  Triggered: price_chg_1h=-0.010633, oi_chg_1h=-0.011927, oi_at_entry=26114966.874
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] BTC-USD triple_ma_short (short) (-30.06)
  Triggered: EMA(8/16/25) = 80,932.8/80,960/80,974.1, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] XRP-USD triple_ma_short (short) (+0)
  Triggered: EMA(8/16/25) = 1.44739/1.44792/1.44829, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] NEAR-USD oi_divergence_long (long) (+129.4)
  Triggered: price_chg_1h=-0.010022, oi_chg_1h=-0.012088, oi_at_entry=26718173.817
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (win)

[LOSS] BTC-USD triple_ma_long (long) (-232.2)
  Triggered: EMA(8/16/25) = 81,023/80,974.6/80,968.3, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] XRP-USD oi_divergence_long (long) (+0.9629)
  Triggered: price_chg_1h=-0.005566, oi_chg_1h=-0.010473, oi_at_entry=123187505.1812
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (win)

[LOSS] FET-USD triple_ma_short (short) (-53.21)
  Triggered: EMA(8/16/25) = 0.157022/0.157052/0.157153, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] XRP-USD triple_ma_short (short) (-33.14)
  Triggered: EMA(8/16/25) = 1.44901/1.4492/1.44924, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] NEAR-USD oi_divergence_long (long) (+21.8)
  Triggered: price_chg_1h=-0.00584, oi_chg_1h=-0.01715, oi_at_entry=27139768.746
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (win)

[LOSS] XRP-USD triple_ma_long (long) (-202.6)
  Triggered: EMA(8/16/25) = 1.44964/1.44944/1.44939, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] SOL-USD oi_divergence_long (long) (+6.696)
  Triggered: price_chg_1h=-0.027882, oi_chg_1h=-0.066226, oi_at_entry=314264125.3695
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (win)

[WIN] BTC-USD triple_ma_short (short) (+12.52)
  Triggered: EMA(8/16/25) = 80,880.6/80,972.9/80,990, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] SOL-USD triple_ma_short (short) (+15.91)
  Triggered: EMA(8/16/25) = 103.569/103.783/103.847, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] XRP-USD oi_divergence_long (long) (-7.89)
  Triggered: price_chg_1h=-0.028021, oi_chg_1h=-0.068621, oi_at_entry=115593782.3832
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] AVAX-USD oi_divergence_long (long) (-0.7322)
  Triggered: price_chg_1h=-0.017726, oi_chg_1h=-0.018786, oi_at_entry=11542937.2204
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] NEAR-USD oi_divergence_long (long) (-23.89)
  Triggered: price_chg_1h=-0.035748, oi_chg_1h=-0.057961, oi_at_entry=25881868.444
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] XRP-USD triple_ma_short (short) (+48.87)
  Triggered: EMA(8/16/25) = 1.4356/1.44197/1.44453, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] AVAX-USD oi_divergence_long (long) (+48.19)
  Triggered: price_chg_1h=-0.018417, oi_chg_1h=-0.011054, oi_at_entry=11634108.1344
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] NEAR-USD triple_ma_short (short) (+31.77)
  Triggered: EMA(8/16/25) = 1.97109/1.97899/1.97981, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] NEAR-USD oi_divergence_long (long) (+15.22)
  Triggered: price_chg_1h=-0.010245, oi_chg_1h=-0.013743, oi_at_entry=25796498.035
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (win)

[WIN] AVAX-USD oi_divergence_long (long) (+65.23)
  Triggered: price_chg_1h=-0.005153, oi_chg_1h=-0.011272, oi_at_entry=11468599.2995
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (win)

[WIN] SOL-USD oi_divergence_long (long) (+4.348)
  Triggered: price_chg_1h=-0.009927, oi_chg_1h=-0.014382, oi_at_entry=315803491.8433
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (win)

[WIN] XRP-USD oi_divergence_long (long) (+11.73)
  Triggered: price_chg_1h=-0.012194, oi_chg_1h=-0.012026, oi_at_entry=114080035.7917
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (win)

[LOSS] AVAX-USD oi_divergence_long (long) (-5.501)
  Triggered: price_chg_1h=-0.006494, oi_chg_1h=-0.023091, oi_at_entry=11276355.7047
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] SOL-USD oi_divergence_long (long) (-20.59)
  Triggered: price_chg_1h=-0.005982, oi_chg_1h=-0.010749, oi_at_entry=323593098.5743
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

Still open (too soon to say why it worked or not):
  ETH-USD triple_ma_short (short) -- triggered: EMA(8/16/25) = 2,508.79/2,514.52/2,515.19, freshly aligned
  FET-USD triple_ma_short (short) -- triggered: EMA(8/16/25) = 0.156971/0.157135/0.157191, freshly aligned
  AVAX-USD triple_ma_short (short) -- triggered: EMA(8/16/25) = 7.44825/7.4697/7.47841, freshly aligned
  XRP-USD oi_divergence_long (long) -- triggered: price_chg_1h=-0.008324, oi_chg_1h=-0.016124, oi_at_entry=115156707.0114

**US -- WHY** (2026-09-04)
- Fired: 28 | Resolved: 26 | Still open: 2

[LOSS] PFE triple_ma_long (long) (-346.8)
  Triggered: EMA(8/16/25) = 28.8007/28.7795/28.7781, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] NCLH triple_ma_long (long) (+128.6)
  Triggered: EMA(8/16/25) = 15.514/15.4925/15.4917, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (win)

[WIN] PFE triple_ma_long (long) (+278.4)
  Triggered: EMA(8/16/25) = 28.7831/28.7804/28.7789, freshly aligned
  Outcome:   session ended before stop or target hit -- settled at the day's close (win)

[LOSS] NCLH triple_ma_long (long) (+0)
  Triggered: EMA(8/16/25) = 15.5217/15.4966/15.4944, freshly aligned
  Outcome:   session ended before stop or target hit -- settled at the day's close (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via eod_settlement; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] RIOT triple_ma_long (long) (+242.7)
  Triggered: EMA(8/16/25) = 20.9796/20.7726/20.488, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] SOFI triple_ma_long (long) (-437.6)
  Triggered: EMA(8/16/25) = 18.4949/18.4716/18.3886, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] MARA triple_ma_long (long) (-309)
  Triggered: EMA(8/16/25) = 11.5767/11.5169/11.4003, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] INTC triple_ma_long (long) (+553.2)
  Triggered: EMA(8/16/25) = 91.8037/91.4268/91.0872, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] SIRI triple_ma_long (long) (-747.2)
  Triggered: EMA(8/16/25) = 29.8806/29.8608/29.7955, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] WFC triple_ma_long (long) (-266.5)
  Triggered: EMA(8/16/25) = 89.1699/89.1571/89.1485, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] GOLD triple_ma_long (long) (+664)
  Triggered: EMA(8/16/25) = 42.0252/41.4495/41.3518, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] GOLD triple_ma_long (long) (+225)
  Triggered: EMA(8/16/25) = 42.8302/41.9585/41.695, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] INTC triple_ma_long (long) (+44.78)
  Triggered: EMA(8/16/25) = 93.0039/92.1832/91.6454, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] MARA triple_ma_long (long) (-466.8)
  Triggered: EMA(8/16/25) = 11.4948/11.4824/11.3953, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] RIOT triple_ma_long (long) (-65.58)
  Triggered: EMA(8/16/25) = 21.134/20.9038/20.6189, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] GOLD triple_ma_long (long) (+574.9)
  Triggered: EMA(8/16/25) = 42.7913/41.9379/41.6815, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] INTC triple_ma_long (long) (+204.5)
  Triggered: EMA(8/16/25) = 92.9594/92.1597/91.63, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] MARA triple_ma_long (long) (-342.3)
  Triggered: EMA(8/16/25) = 11.4904/11.48/11.3937, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] RIOT triple_ma_long (long) (-221.3)
  Triggered: EMA(8/16/25) = 21.1562/20.9156/20.6265, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] GOLD triple_ma_long (long) (+262)
  Triggered: EMA(8/16/25) = 42.8136/41.9496/41.6892, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] INTC triple_ma_long (long) (+27.71)
  Triggered: EMA(8/16/25) = 93.0072/92.185/91.6466, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] MARA triple_ma_long (long) (-356.8)
  Triggered: EMA(8/16/25) = 11.4926/11.4812/11.3945, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] RIOT triple_ma_long (long) (-472.1)
  Triggered: EMA(8/16/25) = 21.1784/20.9273/20.6342, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] DAL triple_ma_long (long) (+88.98)
  Triggered: EMA(8/16/25) = 79.2837/78.967/78.7605, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] C triple_ma_long (long) (+163.8)
  Triggered: EMA(8/16/25) = 136.956/136.897/136.885, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] NKE triple_ma_long (long) (-376.7)
  Triggered: EMA(8/16/25) = 38.4369/38.4154/38.4145, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

Still open (too soon to say why it worked or not):
  HOOD triple_ma_long (long) -- triggered: EMA(8/16/25) = 123.468/122.822/121.281, freshly aligned
  NCLH triple_ma_long (long) -- triggered: EMA(8/16/25) = 15.5324/15.505/15.4994, freshly aligned

**INDIA FUTURES (MANUAL) -- WHY** (2026-09-04)
- Fired: 5 | Resolved: 5 | Still open: 0

[WIN] NIFTY-FUT triple_ma_long (long) (+220.3)
  Triggered: EMA(8/16/25) = 23,926.2/23,922.2/23,921.7, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] SENSEX-FUT triple_ma_long (long) (-397.1)
  Triggered: EMA(8/16/25) = 76,637.3/76,616.7/76,612.8, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] BANKNIFTY-FUT triple_ma_long (long) (-302)
  Triggered: EMA(8/16/25) = 57,467.2/57,466.5/57,460.8, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] NIFTY-FUT triple_ma_long (long) (-78.31)
  Triggered: EMA(8/16/25) = 23,946.4/23,945.9/23,941.5, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] NIFTY-FUT triple_ma_long (long) (-228.6)
  Triggered: EMA(8/16/25) = 23,945.5/23,945.5/23,942.1, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

---

## 2026-09-06 00:00 IST

**INDIA -- WHY** (2026-09-05)
No setups fired.

**CRYPTO -- WHY** (2026-09-05)
- Fired: 25 | Resolved: 25 | Still open: 0

[LOSS] SOL-USD triple_ma_short (short) (-25.82)
  Triggered: EMA(8/16/25) = 101.665/101.666/101.776, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] NEAR-USD oi_divergence_long (long) (+1.253)
  Triggered: price_chg_1h=-0.017888, oi_chg_1h=-0.016123, oi_at_entry=29627789.752
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (win)

[LOSS] ETH-USD triple_ma_short (short) (-9.623)
  Triggered: EMA(8/16/25) = 2,453.92/2,454.02/2,456.23, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] AVAX-USD triple_ma_short (short) (-7.795)
  Triggered: EMA(8/16/25) = 7.3742/7.37504/7.37848, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] FET-USD triple_ma_short (short) (-35.75)
  Triggered: EMA(8/16/25) = 0.154101/0.154125/0.154192, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] BTC-USD triple_ma_short (short) (+25.73)
  Triggered: EMA(8/16/25) = 79,706.6/79,708.9/79,725.9, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] NEAR-USD oi_divergence_long (long) (+15.02)
  Triggered: price_chg_1h=-0.005304, oi_chg_1h=-0.011507, oi_at_entry=31269571.48
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (win)

[WIN] ETH-USD triple_ma_short (short) (+27.74)
  Triggered: EMA(8/16/25) = 2,453.53/2,453.64/2,454.32, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] XRP-USD triple_ma_short (short) (-38.16)
  Triggered: EMA(8/16/25) = 1.39826/1.39832/1.39909, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] XRP-USD triple_ma_short (short) (-31.77)
  Triggered: EMA(8/16/25) = 1.39821/1.39834/1.39876, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] NEAR-USD oi_divergence_long (long) (-0.4804)
  Triggered: price_chg_1h=-0.010699, oi_chg_1h=-0.015961, oi_at_entry=30943256.02
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] SOL-USD triple_ma_short (short) (-43.75)
  Triggered: EMA(8/16/25) = 101.838/101.86/101.864, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] XRP-USD triple_ma_short (short) (-17.86)
  Triggered: EMA(8/16/25) = 1.39822/1.39824/1.39853, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] FET-USD oi_divergence_long (long) (+55.78)
  Triggered: price_chg_1h=-0.014646, oi_chg_1h=-0.028096, oi_at_entry=217531.363
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (win)

[LOSS] NEAR-USD oi_divergence_long (long) (-3.841)
  Triggered: price_chg_1h=-0.011137, oi_chg_1h=-0.015421, oi_at_entry=31503689.45
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] FET-USD oi_divergence_long (long) (+50.32)
  Triggered: price_chg_1h=-0.014936, oi_chg_1h=-0.038465, oi_at_entry=309193.416
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (win)

[WIN] FET-USD oi_divergence_long (long) (+35.38)
  Triggered: price_chg_1h=-0.005356, oi_chg_1h=-0.039729, oi_at_entry=308786.914
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (win)

[LOSS] BTC-USD triple_ma_short (short) (-11.35)
  Triggered: EMA(8/16/25) = 79,640/79,647.1/79,647.2, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] ETH-USD triple_ma_long (long) (-19.19)
  Triggered: EMA(8/16/25) = 2,455.89/2,455.69/2,455.42, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] NEAR-USD oi_divergence_long (long) (-111.1)
  Triggered: price_chg_1h=-0.005769, oi_chg_1h=-0.018266, oi_at_entry=31385469.804
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] FET-USD oi_divergence_long (long) (-108)
  Triggered: price_chg_1h=-0.008454, oi_chg_1h=-0.075368, oi_at_entry=490560.468
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] NEAR-USD triple_ma_short (short) (-3.991)
  Triggered: EMA(8/16/25) = 2.22371/2.23195/2.23269, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] NEAR-USD oi_divergence_long (long) (-35.3)
  Triggered: price_chg_1h=-0.007355, oi_chg_1h=-0.023217, oi_at_entry=30133014.926
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] FET-USD oi_divergence_long (long) (-20.37)
  Triggered: price_chg_1h=-0.006865, oi_chg_1h=-0.05319, oi_at_entry=445766.428
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] FET-USD triple_ma_short (short) (+5.635)
  Triggered: EMA(8/16/25) = 0.165396/0.165751/0.165783, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

**US -- WHY** (2026-09-05)
- Fired: 2 | Resolved: 2 | Still open: 0

[WIN] NKE triple_ma_long (long) (+87.05)
  Triggered: EMA(8/16/25) = 38.4349/38.4234/38.4199, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] MARA triple_ma_long (long) (-659.4)
  Triggered: EMA(8/16/25) = 11.3489/11.3462/11.3417, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

---

## 2026-09-07 00:00 IST

**INDIA -- WHY** (2026-09-06)
No setups fired.

**CRYPTO -- WHY** (2026-09-06)
- Fired: 43 | Resolved: 42 | Still open: 1

[WIN] XRP-USD oi_divergence_long (long) (+24.5)
  Triggered: price_chg_1h=-0.005958, oi_chg_1h=-0.013747, oi_at_entry=120554077.6971
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (win)

[WIN] NEAR-USD oi_divergence_long (long) (+16.67)
  Triggered: price_chg_1h=-0.01225, oi_chg_1h=-0.015392, oi_at_entry=31923563.682
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (win)

[WIN] NEAR-USD triple_ma_short (short) (+13.44)
  Triggered: EMA(8/16/25) = 2.21708/2.21781/2.21784, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] SOL-USD oi_divergence_long (long) (+0)
  Triggered: price_chg_1h=-0.005583, oi_chg_1h=-0.014164, oi_at_entry=333652470.1417
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] NEAR-USD oi_divergence_long (long) (-73.03)
  Triggered: price_chg_1h=-0.020669, oi_chg_1h=-0.023037, oi_at_entry=31715765.96
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] BTC-USD triple_ma_short (short) (-31.61)
  Triggered: EMA(8/16/25) = 79,799.7/79,837.5/79,838.2, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] BTC-USD triple_ma_short (short) (-46.04)
  Triggered: EMA(8/16/25) = 79,827.6/79,841.1/79,842.2, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] FET-USD triple_ma_short (short) (-61.51)
  Triggered: EMA(8/16/25) = 0.165012/0.165024/0.165078, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] XRP-USD triple_ma_short (short) (-41.78)
  Triggered: EMA(8/16/25) = 1.41487/1.41599/1.41613, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] SOL-USD triple_ma_short (short) (-52.9)
  Triggered: EMA(8/16/25) = 103.313/103.406/103.412, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] XRP-USD triple_ma_long (long) (+15.7)
  Triggered: EMA(8/16/25) = 1.41641/1.41608/1.41603, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] FET-USD oi_divergence_long (long) (-16.52)
  Triggered: price_chg_1h=-0.007474, oi_chg_1h=-0.029243, oi_at_entry=423690.825
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] NEAR-USD oi_divergence_long (long) (-2.901)
  Triggered: price_chg_1h=-0.011309, oi_chg_1h=-0.017453, oi_at_entry=31705765.892
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] FET-USD oi_divergence_long (long) (+0)
  Triggered: price_chg_1h=-0.007058, oi_chg_1h=-0.026833, oi_at_entry=417799.312
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] FET-USD triple_ma_short (short) (-43.75)
  Triggered: EMA(8/16/25) = 0.165316/0.165578/0.165603, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] SOL-USD oi_divergence_long (long) (-20.63)
  Triggered: price_chg_1h=-0.009197, oi_chg_1h=-0.016115, oi_at_entry=356770953.5342
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] BTC-USD triple_ma_short (short) (-69.42)
  Triggered: EMA(8/16/25) = 79,869.2/79,894.4/79,899.4, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] FET-USD oi_divergence_long (long) (+127.6)
  Triggered: price_chg_1h=-0.009601, oi_chg_1h=-0.032853, oi_at_entry=410221.54
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (win)

[WIN] SOL-USD oi_divergence_long (long) (+150.9)
  Triggered: price_chg_1h=-0.013277, oi_chg_1h=-0.029562, oi_at_entry=351105258.9162
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (win)

[WIN] XRP-USD oi_divergence_long (long) (+56.79)
  Triggered: price_chg_1h=-0.009755, oi_chg_1h=-0.012118, oi_at_entry=121819229.3894
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (win)

[LOSS] XRP-USD triple_ma_short (short) (-24.63)
  Triggered: EMA(8/16/25) = 1.4181/1.41925/1.41925, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] AVAX-USD triple_ma_short (short) (-46.05)
  Triggered: EMA(8/16/25) = 7.64798/7.65469/7.65521, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] ETH-USD triple_ma_short (short) (-40.12)
  Triggered: EMA(8/16/25) = 2,497.33/2,499.51/2,499.55, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] ETH-USD triple_ma_short (short) (-27.77)
  Triggered: EMA(8/16/25) = 2,498.27/2,499.44/2,499.49, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] ETH-USD triple_ma_short (short) (-18.91)
  Triggered: EMA(8/16/25) = 2,498.5/2,499.42/2,499.47, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] AVAX-USD triple_ma_long (long) (+25.54)
  Triggered: EMA(8/16/25) = 7.6585/7.657/7.65635, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] FET-USD breakout_long (long) (-101.4)
  Triggered: broke range high 0.171 on vol 801,640 vs avg 173,844, trend EMA 0.1691, 2-bar + retest
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] NEAR-USD oi_divergence_long (long) (-64.07)
  Triggered: price_chg_1h=-0.00503, oi_chg_1h=-0.022604, oi_at_entry=37075005.909
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] XRP-USD triple_ma_short (short) (+19.81)
  Triggered: EMA(8/16/25) = 1.41876/1.41937/1.4194, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] ETH-USD triple_ma_short (short) (+14.66)
  Triggered: EMA(8/16/25) = 2,498.38/2,499.51/2,499.75, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] AVAX-USD oi_divergence_long (long) (+41.58)
  Triggered: price_chg_1h=-0.006494, oi_chg_1h=-0.014763, oi_at_entry=12197913.985
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (win)

[LOSS] FET-USD oi_divergence_long (long) (+0)
  Triggered: price_chg_1h=-0.010722, oi_chg_1h=-0.016857, oi_at_entry=478674.78
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] BTC-USD triple_ma_short (short) (-16.16)
  Triggered: EMA(8/16/25) = 79,877.8/79,898.6/79,901.4, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] SOL-USD oi_divergence_long (long) (+60.52)
  Triggered: price_chg_1h=-0.005232, oi_chg_1h=-0.012007, oi_at_entry=354386821.5615
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (win)

[LOSS] AVAX-USD triple_ma_long (long) (-45.68)
  Triggered: EMA(8/16/25) = 7.67657/7.67644/7.67338, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] AVAX-USD oi_divergence_long (long) (+22.16)
  Triggered: price_chg_1h=-0.005622, oi_chg_1h=-0.017595, oi_at_entry=11975531.626
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (win)

[WIN] FET-USD oi_divergence_long (long) (+10.85)
  Triggered: price_chg_1h=-0.008185, oi_chg_1h=-0.049714, oi_at_entry=460074.096
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (win)

[WIN] SOL-USD oi_divergence_long (long) (+18.81)
  Triggered: price_chg_1h=-0.012514, oi_chg_1h=-0.025152, oi_at_entry=346056789.6066
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (win)

[LOSS] NEAR-USD oi_divergence_long (long) (-65.38)
  Triggered: price_chg_1h=-0.026518, oi_chg_1h=-0.041771, oi_at_entry=38905372.753
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] SOL-USD triple_ma_short (short) (-38.96)
  Triggered: EMA(8/16/25) = 105.945/106.111/106.118, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] NEAR-USD oi_divergence_long (long) (+0)
  Triggered: price_chg_1h=-0.025659, oi_chg_1h=-0.020916, oi_at_entry=38250618.807
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] FET-USD oi_divergence_long (long) (+19.56)
  Triggered: price_chg_1h=-0.006606, oi_chg_1h=-0.014821, oi_at_entry=484146.4
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (win)

Still open (too soon to say why it worked or not):
  AVAX-USD triple_ma_short (short) -- triggered: EMA(8/16/25) = 7.65587/7.66521/7.66632, freshly aligned

**US -- WHY** (2026-09-06)
No setups fired.

---

## 2026-09-07 00:07 IST

**INDIA -- WHY** (2026-09-06)
No setups fired.

**CRYPTO -- WHY** (2026-09-06)
- Fired: 43 | Resolved: 42 | Still open: 1

[WIN] XRP-USD oi_divergence_long (long) (+24.5)
  Triggered: price_chg_1h=-0.005958, oi_chg_1h=-0.013747, oi_at_entry=120554077.6971
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (win)

[WIN] NEAR-USD oi_divergence_long (long) (+16.67)
  Triggered: price_chg_1h=-0.01225, oi_chg_1h=-0.015392, oi_at_entry=31923563.682
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (win)

[WIN] NEAR-USD triple_ma_short (short) (+13.44)
  Triggered: EMA(8/16/25) = 2.21708/2.21781/2.21784, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] SOL-USD oi_divergence_long (long) (+0)
  Triggered: price_chg_1h=-0.005583, oi_chg_1h=-0.014164, oi_at_entry=333652470.1417
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] NEAR-USD oi_divergence_long (long) (-73.03)
  Triggered: price_chg_1h=-0.020669, oi_chg_1h=-0.023037, oi_at_entry=31715765.96
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] BTC-USD triple_ma_short (short) (-31.61)
  Triggered: EMA(8/16/25) = 79,799.7/79,837.5/79,838.2, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] BTC-USD triple_ma_short (short) (-46.04)
  Triggered: EMA(8/16/25) = 79,827.6/79,841.1/79,842.2, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] FET-USD triple_ma_short (short) (-61.51)
  Triggered: EMA(8/16/25) = 0.165012/0.165024/0.165078, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] XRP-USD triple_ma_short (short) (-41.78)
  Triggered: EMA(8/16/25) = 1.41487/1.41599/1.41613, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] SOL-USD triple_ma_short (short) (-52.9)
  Triggered: EMA(8/16/25) = 103.313/103.406/103.412, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] XRP-USD triple_ma_long (long) (+15.7)
  Triggered: EMA(8/16/25) = 1.41641/1.41608/1.41603, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] FET-USD oi_divergence_long (long) (-16.52)
  Triggered: price_chg_1h=-0.007474, oi_chg_1h=-0.029243, oi_at_entry=423690.825
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] NEAR-USD oi_divergence_long (long) (-2.901)
  Triggered: price_chg_1h=-0.011309, oi_chg_1h=-0.017453, oi_at_entry=31705765.892
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] FET-USD oi_divergence_long (long) (+0)
  Triggered: price_chg_1h=-0.007058, oi_chg_1h=-0.026833, oi_at_entry=417799.312
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] FET-USD triple_ma_short (short) (-43.75)
  Triggered: EMA(8/16/25) = 0.165316/0.165578/0.165603, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] SOL-USD oi_divergence_long (long) (-20.63)
  Triggered: price_chg_1h=-0.009197, oi_chg_1h=-0.016115, oi_at_entry=356770953.5342
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] BTC-USD triple_ma_short (short) (-69.42)
  Triggered: EMA(8/16/25) = 79,869.2/79,894.4/79,899.4, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] FET-USD oi_divergence_long (long) (+127.6)
  Triggered: price_chg_1h=-0.009601, oi_chg_1h=-0.032853, oi_at_entry=410221.54
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (win)

[WIN] SOL-USD oi_divergence_long (long) (+150.9)
  Triggered: price_chg_1h=-0.013277, oi_chg_1h=-0.029562, oi_at_entry=351105258.9162
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (win)

[WIN] XRP-USD oi_divergence_long (long) (+56.79)
  Triggered: price_chg_1h=-0.009755, oi_chg_1h=-0.012118, oi_at_entry=121819229.3894
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (win)

[LOSS] XRP-USD triple_ma_short (short) (-24.63)
  Triggered: EMA(8/16/25) = 1.4181/1.41925/1.41925, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] AVAX-USD triple_ma_short (short) (-46.05)
  Triggered: EMA(8/16/25) = 7.64798/7.65469/7.65521, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] ETH-USD triple_ma_short (short) (-40.12)
  Triggered: EMA(8/16/25) = 2,497.33/2,499.51/2,499.55, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] ETH-USD triple_ma_short (short) (-27.77)
  Triggered: EMA(8/16/25) = 2,498.27/2,499.44/2,499.49, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] ETH-USD triple_ma_short (short) (-18.91)
  Triggered: EMA(8/16/25) = 2,498.5/2,499.42/2,499.47, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] AVAX-USD triple_ma_long (long) (+25.54)
  Triggered: EMA(8/16/25) = 7.6585/7.657/7.65635, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] FET-USD breakout_long (long) (-101.4)
  Triggered: broke range high 0.171 on vol 801,640 vs avg 173,844, trend EMA 0.1691, 2-bar + retest
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] NEAR-USD oi_divergence_long (long) (-64.07)
  Triggered: price_chg_1h=-0.00503, oi_chg_1h=-0.022604, oi_at_entry=37075005.909
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] XRP-USD triple_ma_short (short) (+19.81)
  Triggered: EMA(8/16/25) = 1.41876/1.41937/1.4194, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] ETH-USD triple_ma_short (short) (+14.66)
  Triggered: EMA(8/16/25) = 2,498.38/2,499.51/2,499.75, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] AVAX-USD oi_divergence_long (long) (+41.58)
  Triggered: price_chg_1h=-0.006494, oi_chg_1h=-0.014763, oi_at_entry=12197913.985
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (win)

[LOSS] FET-USD oi_divergence_long (long) (+0)
  Triggered: price_chg_1h=-0.010722, oi_chg_1h=-0.016857, oi_at_entry=478674.78
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] BTC-USD triple_ma_short (short) (-16.16)
  Triggered: EMA(8/16/25) = 79,877.8/79,898.6/79,901.4, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] SOL-USD oi_divergence_long (long) (+60.52)
  Triggered: price_chg_1h=-0.005232, oi_chg_1h=-0.012007, oi_at_entry=354386821.5615
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (win)

[LOSS] AVAX-USD triple_ma_long (long) (-45.68)
  Triggered: EMA(8/16/25) = 7.67657/7.67644/7.67338, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] AVAX-USD oi_divergence_long (long) (+22.16)
  Triggered: price_chg_1h=-0.005622, oi_chg_1h=-0.017595, oi_at_entry=11975531.626
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (win)

[WIN] FET-USD oi_divergence_long (long) (+10.85)
  Triggered: price_chg_1h=-0.008185, oi_chg_1h=-0.049714, oi_at_entry=460074.096
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (win)

[WIN] SOL-USD oi_divergence_long (long) (+18.81)
  Triggered: price_chg_1h=-0.012514, oi_chg_1h=-0.025152, oi_at_entry=346056789.6066
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (win)

[LOSS] NEAR-USD oi_divergence_long (long) (-65.38)
  Triggered: price_chg_1h=-0.026518, oi_chg_1h=-0.041771, oi_at_entry=38905372.753
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] SOL-USD triple_ma_short (short) (-38.96)
  Triggered: EMA(8/16/25) = 105.945/106.111/106.118, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] NEAR-USD oi_divergence_long (long) (+0)
  Triggered: price_chg_1h=-0.025659, oi_chg_1h=-0.020916, oi_at_entry=38250618.807
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] FET-USD oi_divergence_long (long) (+19.56)
  Triggered: price_chg_1h=-0.006606, oi_chg_1h=-0.014821, oi_at_entry=484146.4
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (win)

Still open (too soon to say why it worked or not):
  AVAX-USD triple_ma_short (short) -- triggered: EMA(8/16/25) = 7.65587/7.66521/7.66632, freshly aligned

**US -- WHY** (2026-09-06)
No setups fired.

---

## 2026-09-08 00:00 IST

**INDIA -- WHY** (2026-09-07)
- Fired: 26 | Resolved: 25 | Still open: 1

[LOSS] COALINDIA.NS triple_threat_long (long) (-2,051)
  Triggered: RSI 48->70 crossed 50, broke 416.1, trend EMA 415.5
  Outcome:   session ended before stop or target hit -- settled at the day's close (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via eod_settlement; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] SAIL.NS triple_threat_short (short) (+2,779)
  Triggered: RSI 58->40 crossed 50, broke 194.4, trend EMA 196.8
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] SUZLON.NS breakdown_short (short) (-2,635)
  Triggered: broke range low 45.1 on vol 3,586,517 vs avg 2,995,278, trend EMA 45.3; India gate: RSI 32.52 / VWAP 45.15 (rsi<40 and close<=vwap)
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] BHEL.NS range_short_rejection (short) (+3,071)
  Triggered: wicked to 434.5 near range high [431.1, 434.5], closed back inside; India gate: RSI 31.43 / VWAP 432.4 (rsi<40 and close<=vwap)
  Outcome:   hit fixed target -- clean win

[WIN] BANKBARODA.NS range_short_rejection (short) (+1,443)
  Triggered: wicked to 240.9 near range high [239, 239.9], closed back inside; India gate: RSI 26.91 / VWAP 239.7 (rsi<40 and close<=vwap)
  Outcome:   hit fixed target -- clean win

[LOSS] INDIANB.NS breakdown_short (short) (-859.7)
  Triggered: broke range low 874.2 on vol 60,674 vs avg 40,508, trend EMA 882.8; India gate: RSI 20.79 / VWAP 875.4 (rsi<40 and close<=vwap)
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] UNIONBANK.NS breakdown_short (short) (-1,149)
  Triggered: broke range low 185.8 on vol 459,817 vs avg 406,830, trend EMA 187.5; India gate: RSI 18.45 / VWAP 186 (rsi<40 and close<=vwap)
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] BANKINDIA.NS breakdown_short (short) (+493.3)
  Triggered: broke range low 142.6 on vol 226,922 vs avg 192,570, trend EMA 143.6; India gate: RSI 11.02 / VWAP 143.1 (rsi<40 and close<=vwap)
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] BHEL.NS breakdown_short (short) (+4,084)
  Triggered: broke range low 426.2 on vol 223,798 vs avg 182,293, trend EMA 429.1; India gate: RSI 24.84 / VWAP 429.2 (rsi<40 and close<=vwap)
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] COALINDIA.NS triple_ma_short (short) (-1,692)
  Triggered: EMA(8/16/25) = 415.188/415.252/415.389, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] INDIANB.NS breakdown_short (short) (-575.7)
  Triggered: broke range low 869.3 on vol 41,014 vs avg 40,280, trend EMA 873.8; India gate: RSI 12.0 / VWAP 872.7 (rsi<40 and close<=vwap)
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] BANKINDIA.NS breakdown_short (short) (-353.2)
  Triggered: broke range low 141.6 on vol 245,606 vs avg 235,320, trend EMA 142.7; India gate: RSI 8.77 / VWAP 142.6 (rsi<40 and close<=vwap)
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] BHEL.NS breakdown_short (short) (-2,019)
  Triggered: broke range low 422.5 on vol 421,588 vs avg 189,546, trend EMA 427.7; India gate: RSI 20.86 / VWAP 427.3 (rsi<40 and close<=vwap)
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] RPOWER.NS triple_ma_short (short) (+562.7)
  Triggered: EMA(8/16/25) = 22.127/22.1365/22.1398, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] COALINDIA.NS triple_ma_short (short) (-2,771)
  Triggered: EMA(8/16/25) = 415.243/415.28/415.466, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] SAIL.NS breakdown_short (short) (-211.5)
  Triggered: broke range low 189.1 on vol 1,028,821 vs avg 906,959, trend EMA 190.6; India gate: RSI 2.06 / VWAP 190.7 (rsi<40 and close<=vwap)
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] COALINDIA.NS triple_ma_long (long) (+1,677)
  Triggered: EMA(8/16/25) = 416.19/415.824/415.786, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] NATIONALUM.NS breakdown_short (short) (-1,565)
  Triggered: broke range low 368.5 on vol 138,468 vs avg 71,723, trend EMA 369.7; India gate: RSI 38.97 / VWAP 370.1 (rsi<40 and close<=vwap)
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] SAIL.NS breakdown_short (short) (-2,029)
  Triggered: broke range low 187.7 on vol 908,181 vs avg 796,544, trend EMA 189; India gate: RSI 9.53 / VWAP 190.2 (rsi<40 and close<=vwap)
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] RVNL.NS triple_ma_short (short) (+23.67)
  Triggered: EMA(8/16/25) = 212.06/212.411/212.448, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] FEDERALBNK.NS triple_ma_short (short) (+513.2)
  Triggered: EMA(8/16/25) = 341.046/341.061/341.329, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] RVNL.NS breakdown_short (short) (-829)
  Triggered: broke range low 211.2 on vol 144,760 vs avg 132,201, trend EMA 211.8; India gate: RSI 22.51 / VWAP 213.7 (rsi<40 and close<=vwap)
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] VEDL.NS breakdown_short (short) (-2,243)
  Triggered: broke range low 268.1 on vol 673,059 vs avg 127,848, trend EMA 268.7; India gate: RSI 38.54 / VWAP 269.1 (rsi<40 and close<=vwap)
  Outcome:   session ended before stop or target hit -- settled at the day's close (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via eod_settlement; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] RVNL.NS breakdown_short (short) (-2,498)
  Triggered: broke range low 210.7 on vol 1,322,123 vs avg 209,785, trend EMA 211.5; India gate: RSI 6.53 / VWAP 213.1 (rsi<40 and close<=vwap)
  Outcome:   session ended before stop or target hit -- settled at the day's close (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via eod_settlement; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] VEDL.NS triple_threat_short (short) (-1,400)
  Triggered: RSI 53->43 crossed 50, broke 268.1, trend EMA 269.3
  Outcome:   session ended before stop or target hit -- settled at the day's close (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via eod_settlement; the market simply moved the other way this time (normal strategy variance, not a bug)

Still open (too soon to say why it worked or not):
  CANBK.NS breakdown_short (short) -- triggered: broke range low 125 on vol 1,151,767 vs avg 543,989, trend EMA 126; India gate: RSI 12.93 / VWAP 125.1 (rsi<40 and close<=vwap)

**CRYPTO -- WHY** (2026-09-07)
- Fired: 50 | Resolved: 50 | Still open: 0

[LOSS] BTC-USD triple_ma_long (long) (-52.87)
  Triggered: EMA(8/16/25) = 79,840.4/79,793.7/79,789.7, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] SOL-USD triple_ma_short (short) (+12.67)
  Triggered: EMA(8/16/25) = 106.076/106.103/106.109, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] FET-USD breakout_long (long) (-139.3)
  Triggered: broke range high 0.1749 on vol 348,928 vs avg 287,296, trend EMA 0.1736, 2-bar + retest
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] SOL-USD triple_ma_short (short) (-60.94)
  Triggered: EMA(8/16/25) = 105.771/105.832/105.89, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] XRP-USD oi_divergence_long (long) (+40.91)
  Triggered: price_chg_1h=-0.006885, oi_chg_1h=-0.010491, oi_at_entry=119606820.6861
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (win)

[LOSS] AVAX-USD oi_divergence_long (long) (+0)
  Triggered: price_chg_1h=-0.006538, oi_chg_1h=-0.016108, oi_at_entry=12157523.3079
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] NEAR-USD range_short_rejection (short) (+70.59)
  Triggered: wicked to 2.499 near range high [1.781, 2.492], closed back inside, ADX 22.5 confirmed ranging
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] FET-USD oi_divergence_long (long) (-0.4731)
  Triggered: price_chg_1h=-0.015535, oi_chg_1h=-0.016885, oi_at_entry=492887.729
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] NEAR-USD oi_divergence_long (long) (+31.42)
  Triggered: price_chg_1h=-0.020329, oi_chg_1h=-0.016957, oi_at_entry=38856275.156
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (win)

[LOSS] NEAR-USD oi_divergence_long (long) (-146.7)
  Triggered: price_chg_1h=-0.013928, oi_chg_1h=-0.011894, oi_at_entry=38617435.985
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] NEAR-USD oi_divergence_long (long) (-116.6)
  Triggered: price_chg_1h=-0.011037, oi_chg_1h=-0.01088, oi_at_entry=38349696.724
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] SOL-USD triple_ma_short (short) (+15.8)
  Triggered: EMA(8/16/25) = 105.937/105.99/105.992, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] NEAR-USD triple_ma_short (short) (+13.26)
  Triggered: EMA(8/16/25) = 2.407/2.41871/2.42005, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] FET-USD oi_divergence_long (long) (-108.9)
  Triggered: price_chg_1h=-0.016336, oi_chg_1h=-0.025581, oi_at_entry=498432.795
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] XRP-USD triple_ma_short (short) (-104)
  Triggered: EMA(8/16/25) = 1.41346/1.41599/1.41642, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] AVAX-USD oi_divergence_long (long) (+37.7)
  Triggered: price_chg_1h=-0.016139, oi_chg_1h=-0.01407, oi_at_entry=12256262.6456
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (win)

[LOSS] FET-USD triple_ma_short (short) (-113.6)
  Triggered: EMA(8/16/25) = 0.173283/0.17401/0.174069, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] SOL-USD triple_ma_short (short) (+26.86)
  Triggered: EMA(8/16/25) = 105.869/105.873/105.897, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] FET-USD triple_ma_short (short) (-0.8805)
  Triggered: EMA(8/16/25) = 0.173684/0.174089/0.174115, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] BTC-USD triple_ma_short (short) (+5.874)
  Triggered: EMA(8/16/25) = 79,896.3/79,951.8/79,961.2, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] SOL-USD oi_divergence_long (long) (+0)
  Triggered: price_chg_1h=-0.006706, oi_chg_1h=-0.01642, oi_at_entry=344178140.9114
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] AVAX-USD oi_divergence_long (long) (+133.2)
  Triggered: price_chg_1h=-0.005745, oi_chg_1h=-0.01827, oi_at_entry=12090752.5536
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (win)

[WIN] XRP-USD oi_divergence_long (long) (+24.56)
  Triggered: price_chg_1h=-0.013839, oi_chg_1h=-0.01434, oi_at_entry=121648437.9063
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (win)

[WIN] FET-USD oi_divergence_long (long) (+58.48)
  Triggered: price_chg_1h=-0.021604, oi_chg_1h=-0.023437, oi_at_entry=469295.112
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (win)

[LOSS] ETH-USD triple_ma_short (short) (-68.05)
  Triggered: EMA(8/16/25) = 2,501.54/2,504.2/2,504.53, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] NEAR-USD oi_divergence_long (long) (+41.01)
  Triggered: price_chg_1h=-0.017334, oi_chg_1h=-0.014743, oi_at_entry=36898214.32
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (win)

[LOSS] FET-USD oi_divergence_long (long) (-17.98)
  Triggered: price_chg_1h=-0.006143, oi_chg_1h=-0.024045, oi_at_entry=495576.354
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] ETH-USD triple_ma_short (short) (+46.26)
  Triggered: EMA(8/16/25) = 2,503.99/2,504.39/2,504.49, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] AVAX-USD oi_divergence_long (long) (-102.7)
  Triggered: price_chg_1h=-0.006566, oi_chg_1h=-0.010481, oi_at_entry=12186144.8716
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] NEAR-USD oi_divergence_long (long) (-207.7)
  Triggered: price_chg_1h=-0.019337, oi_chg_1h=-0.018896, oi_at_entry=36682757.032
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [STOP OVERSHOOT] intended risk 0.02975/unit, actual loss 0.0618/unit (2.1x) -- price moved past the stop faster than the bot's bar-close check could exit; a violent move against the position, amplified by simulation lag rather than a bad entry call

[LOSS] FET-USD oi_divergence_long (long) (-7.13)
  Triggered: price_chg_1h=-0.01148, oi_chg_1h=-0.034843, oi_at_entry=479201.74
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] NEAR-USD triple_ma_short (short) (+49.93)
  Triggered: EMA(8/16/25) = 2.40297/2.40699/2.40824, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] FET-USD triple_ma_short (short) (-65.6)
  Triggered: EMA(8/16/25) = 0.173722/0.173884/0.17391, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] XRP-USD oi_divergence_long (long) (+12.82)
  Triggered: price_chg_1h=-0.006045, oi_chg_1h=-0.01007, oi_at_entry=122681479.8255
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (win)

[WIN] SOL-USD oi_divergence_long (long) (+7.795)
  Triggered: price_chg_1h=-0.0059, oi_chg_1h=-0.015208, oi_at_entry=341270328.9058
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (win)

[WIN] FET-USD triple_ma_long (long) (+53.07)
  Triggered: EMA(8/16/25) = 0.174164/0.174007/0.173961, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] AVAX-USD oi_divergence_long (long) (-11.85)
  Triggered: price_chg_1h=-0.008923, oi_chg_1h=-0.010911, oi_at_entry=12428161.6225
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] AVAX-USD oi_divergence_long (long) (+20.1)
  Triggered: price_chg_1h=-0.005068, oi_chg_1h=-0.014266, oi_at_entry=12334266.6392
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (win)

[LOSS] XRP-USD triple_ma_long (long) (-159.3)
  Triggered: EMA(8/16/25) = 1.40699/1.40492/1.40475, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] BTC-USD triple_ma_short (short) (+52.49)
  Triggered: EMA(8/16/25) = 79,463.4/79,467.8/79,489.3, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] SOL-USD oi_divergence_long (long) (-100.8)
  Triggered: price_chg_1h=-0.005959, oi_chg_1h=-0.010594, oi_at_entry=343238532.2076
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] XRP-USD triple_ma_short (short) (+40.66)
  Triggered: EMA(8/16/25) = 1.40365/1.40369/1.40396, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] NEAR-USD oi_divergence_long (long) (-103.5)
  Triggered: price_chg_1h=-0.009451, oi_chg_1h=-0.014325, oi_at_entry=33473996.61
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] FET-USD oi_divergence_long (long) (+39.39)
  Triggered: price_chg_1h=-0.016747, oi_chg_1h=-0.01596, oi_at_entry=608994.107
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (win)

[WIN] ETH-USD triple_ma_short (short) (+38)
  Triggered: EMA(8/16/25) = 2,493.56/2,494.38/2,494.69, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] SOL-USD triple_ma_short (short) (+62.08)
  Triggered: EMA(8/16/25) = 104.93/105.022/105.044, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] NEAR-USD oi_divergence_long (long) (-141.3)
  Triggered: price_chg_1h=-0.011936, oi_chg_1h=-0.01019, oi_at_entry=33261686.57
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] NEAR-USD triple_ma_short (short) (+53.28)
  Triggered: EMA(8/16/25) = 2.35949/2.36116/2.36286, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] XRP-USD oi_divergence_long (long) (+20.45)
  Triggered: price_chg_1h=-0.009393, oi_chg_1h=-0.026151, oi_at_entry=120494421.1264
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (win)

[WIN] AVAX-USD oi_divergence_long (long) (+81.77)
  Triggered: price_chg_1h=-0.006699, oi_chg_1h=-0.0165, oi_at_entry=12457537.7056
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (win)

**US -- WHY** (2026-09-07)
No setups fired.

---

## 2026-09-08 00:13 IST

**INDIA -- WHY** (2026-09-07)
- Fired: 26 | Resolved: 25 | Still open: 1

[LOSS] COALINDIA.NS triple_threat_long (long) (-2,051)
  Triggered: RSI 48->70 crossed 50, broke 416.1, trend EMA 415.5
  Outcome:   session ended before stop or target hit -- settled at the day's close (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via eod_settlement; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] SAIL.NS triple_threat_short (short) (+2,779)
  Triggered: RSI 58->40 crossed 50, broke 194.4, trend EMA 196.8
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] SUZLON.NS breakdown_short (short) (-2,635)
  Triggered: broke range low 45.1 on vol 3,586,517 vs avg 2,995,278, trend EMA 45.3; India gate: RSI 32.52 / VWAP 45.15 (rsi<40 and close<=vwap)
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] BHEL.NS range_short_rejection (short) (+3,071)
  Triggered: wicked to 434.5 near range high [431.1, 434.5], closed back inside; India gate: RSI 31.43 / VWAP 432.4 (rsi<40 and close<=vwap)
  Outcome:   hit fixed target -- clean win

[WIN] BANKBARODA.NS range_short_rejection (short) (+1,443)
  Triggered: wicked to 240.9 near range high [239, 239.9], closed back inside; India gate: RSI 26.91 / VWAP 239.7 (rsi<40 and close<=vwap)
  Outcome:   hit fixed target -- clean win

[LOSS] INDIANB.NS breakdown_short (short) (-859.7)
  Triggered: broke range low 874.2 on vol 60,674 vs avg 40,508, trend EMA 882.8; India gate: RSI 20.79 / VWAP 875.4 (rsi<40 and close<=vwap)
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] UNIONBANK.NS breakdown_short (short) (-1,149)
  Triggered: broke range low 185.8 on vol 459,817 vs avg 406,830, trend EMA 187.5; India gate: RSI 18.45 / VWAP 186 (rsi<40 and close<=vwap)
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] BANKINDIA.NS breakdown_short (short) (+493.3)
  Triggered: broke range low 142.6 on vol 226,922 vs avg 192,570, trend EMA 143.6; India gate: RSI 11.02 / VWAP 143.1 (rsi<40 and close<=vwap)
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] BHEL.NS breakdown_short (short) (+4,084)
  Triggered: broke range low 426.2 on vol 223,798 vs avg 182,293, trend EMA 429.1; India gate: RSI 24.84 / VWAP 429.2 (rsi<40 and close<=vwap)
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] COALINDIA.NS triple_ma_short (short) (-1,692)
  Triggered: EMA(8/16/25) = 415.188/415.252/415.389, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] INDIANB.NS breakdown_short (short) (-575.7)
  Triggered: broke range low 869.3 on vol 41,014 vs avg 40,280, trend EMA 873.8; India gate: RSI 12.0 / VWAP 872.7 (rsi<40 and close<=vwap)
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] BANKINDIA.NS breakdown_short (short) (-353.2)
  Triggered: broke range low 141.6 on vol 245,606 vs avg 235,320, trend EMA 142.7; India gate: RSI 8.77 / VWAP 142.6 (rsi<40 and close<=vwap)
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] BHEL.NS breakdown_short (short) (-2,019)
  Triggered: broke range low 422.5 on vol 421,588 vs avg 189,546, trend EMA 427.7; India gate: RSI 20.86 / VWAP 427.3 (rsi<40 and close<=vwap)
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] RPOWER.NS triple_ma_short (short) (+562.7)
  Triggered: EMA(8/16/25) = 22.127/22.1365/22.1398, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] COALINDIA.NS triple_ma_short (short) (-2,771)
  Triggered: EMA(8/16/25) = 415.243/415.28/415.466, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] SAIL.NS breakdown_short (short) (-211.5)
  Triggered: broke range low 189.1 on vol 1,028,821 vs avg 906,959, trend EMA 190.6; India gate: RSI 2.06 / VWAP 190.7 (rsi<40 and close<=vwap)
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] COALINDIA.NS triple_ma_long (long) (+1,677)
  Triggered: EMA(8/16/25) = 416.19/415.824/415.786, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] NATIONALUM.NS breakdown_short (short) (-1,565)
  Triggered: broke range low 368.5 on vol 138,468 vs avg 71,723, trend EMA 369.7; India gate: RSI 38.97 / VWAP 370.1 (rsi<40 and close<=vwap)
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] SAIL.NS breakdown_short (short) (-2,029)
  Triggered: broke range low 187.7 on vol 908,181 vs avg 796,544, trend EMA 189; India gate: RSI 9.53 / VWAP 190.2 (rsi<40 and close<=vwap)
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] RVNL.NS triple_ma_short (short) (+23.67)
  Triggered: EMA(8/16/25) = 212.06/212.411/212.448, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] FEDERALBNK.NS triple_ma_short (short) (+513.2)
  Triggered: EMA(8/16/25) = 341.046/341.061/341.329, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] RVNL.NS breakdown_short (short) (-829)
  Triggered: broke range low 211.2 on vol 144,760 vs avg 132,201, trend EMA 211.8; India gate: RSI 22.51 / VWAP 213.7 (rsi<40 and close<=vwap)
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] VEDL.NS breakdown_short (short) (-2,243)
  Triggered: broke range low 268.1 on vol 673,059 vs avg 127,848, trend EMA 268.7; India gate: RSI 38.54 / VWAP 269.1 (rsi<40 and close<=vwap)
  Outcome:   session ended before stop or target hit -- settled at the day's close (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via eod_settlement; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] RVNL.NS breakdown_short (short) (-2,498)
  Triggered: broke range low 210.7 on vol 1,322,123 vs avg 209,785, trend EMA 211.5; India gate: RSI 6.53 / VWAP 213.1 (rsi<40 and close<=vwap)
  Outcome:   session ended before stop or target hit -- settled at the day's close (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via eod_settlement; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] VEDL.NS triple_threat_short (short) (-1,400)
  Triggered: RSI 53->43 crossed 50, broke 268.1, trend EMA 269.3
  Outcome:   session ended before stop or target hit -- settled at the day's close (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via eod_settlement; the market simply moved the other way this time (normal strategy variance, not a bug)

Still open (too soon to say why it worked or not):
  CANBK.NS breakdown_short (short) -- triggered: broke range low 125 on vol 1,151,767 vs avg 543,989, trend EMA 126; India gate: RSI 12.93 / VWAP 125.1 (rsi<40 and close<=vwap)

**CRYPTO -- WHY** (2026-09-07)
- Fired: 50 | Resolved: 50 | Still open: 0

[LOSS] BTC-USD triple_ma_long (long) (-52.87)
  Triggered: EMA(8/16/25) = 79,840.4/79,793.7/79,789.7, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] SOL-USD triple_ma_short (short) (+12.67)
  Triggered: EMA(8/16/25) = 106.076/106.103/106.109, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] FET-USD breakout_long (long) (-139.3)
  Triggered: broke range high 0.1749 on vol 348,928 vs avg 287,296, trend EMA 0.1736, 2-bar + retest
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] SOL-USD triple_ma_short (short) (-60.94)
  Triggered: EMA(8/16/25) = 105.771/105.832/105.89, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] XRP-USD oi_divergence_long (long) (+40.91)
  Triggered: price_chg_1h=-0.006885, oi_chg_1h=-0.010491, oi_at_entry=119606820.6861
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (win)

[LOSS] AVAX-USD oi_divergence_long (long) (+0)
  Triggered: price_chg_1h=-0.006538, oi_chg_1h=-0.016108, oi_at_entry=12157523.3079
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] NEAR-USD range_short_rejection (short) (+70.59)
  Triggered: wicked to 2.499 near range high [1.781, 2.492], closed back inside, ADX 22.5 confirmed ranging
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] FET-USD oi_divergence_long (long) (-0.4731)
  Triggered: price_chg_1h=-0.015535, oi_chg_1h=-0.016885, oi_at_entry=492887.729
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] NEAR-USD oi_divergence_long (long) (+31.42)
  Triggered: price_chg_1h=-0.020329, oi_chg_1h=-0.016957, oi_at_entry=38856275.156
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (win)

[LOSS] NEAR-USD oi_divergence_long (long) (-146.7)
  Triggered: price_chg_1h=-0.013928, oi_chg_1h=-0.011894, oi_at_entry=38617435.985
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] NEAR-USD oi_divergence_long (long) (-116.6)
  Triggered: price_chg_1h=-0.011037, oi_chg_1h=-0.01088, oi_at_entry=38349696.724
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] SOL-USD triple_ma_short (short) (+15.8)
  Triggered: EMA(8/16/25) = 105.937/105.99/105.992, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] NEAR-USD triple_ma_short (short) (+13.26)
  Triggered: EMA(8/16/25) = 2.407/2.41871/2.42005, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] FET-USD oi_divergence_long (long) (-108.9)
  Triggered: price_chg_1h=-0.016336, oi_chg_1h=-0.025581, oi_at_entry=498432.795
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] XRP-USD triple_ma_short (short) (-104)
  Triggered: EMA(8/16/25) = 1.41346/1.41599/1.41642, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] AVAX-USD oi_divergence_long (long) (+37.7)
  Triggered: price_chg_1h=-0.016139, oi_chg_1h=-0.01407, oi_at_entry=12256262.6456
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (win)

[LOSS] FET-USD triple_ma_short (short) (-113.6)
  Triggered: EMA(8/16/25) = 0.173283/0.17401/0.174069, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] SOL-USD triple_ma_short (short) (+26.86)
  Triggered: EMA(8/16/25) = 105.869/105.873/105.897, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] FET-USD triple_ma_short (short) (-0.8805)
  Triggered: EMA(8/16/25) = 0.173684/0.174089/0.174115, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] BTC-USD triple_ma_short (short) (+5.874)
  Triggered: EMA(8/16/25) = 79,896.3/79,951.8/79,961.2, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] SOL-USD oi_divergence_long (long) (+0)
  Triggered: price_chg_1h=-0.006706, oi_chg_1h=-0.01642, oi_at_entry=344178140.9114
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] AVAX-USD oi_divergence_long (long) (+133.2)
  Triggered: price_chg_1h=-0.005745, oi_chg_1h=-0.01827, oi_at_entry=12090752.5536
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (win)

[WIN] XRP-USD oi_divergence_long (long) (+24.56)
  Triggered: price_chg_1h=-0.013839, oi_chg_1h=-0.01434, oi_at_entry=121648437.9063
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (win)

[WIN] FET-USD oi_divergence_long (long) (+58.48)
  Triggered: price_chg_1h=-0.021604, oi_chg_1h=-0.023437, oi_at_entry=469295.112
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (win)

[LOSS] ETH-USD triple_ma_short (short) (-68.05)
  Triggered: EMA(8/16/25) = 2,501.54/2,504.2/2,504.53, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] NEAR-USD oi_divergence_long (long) (+41.01)
  Triggered: price_chg_1h=-0.017334, oi_chg_1h=-0.014743, oi_at_entry=36898214.32
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (win)

[LOSS] FET-USD oi_divergence_long (long) (-17.98)
  Triggered: price_chg_1h=-0.006143, oi_chg_1h=-0.024045, oi_at_entry=495576.354
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] ETH-USD triple_ma_short (short) (+46.26)
  Triggered: EMA(8/16/25) = 2,503.99/2,504.39/2,504.49, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] AVAX-USD oi_divergence_long (long) (-102.7)
  Triggered: price_chg_1h=-0.006566, oi_chg_1h=-0.010481, oi_at_entry=12186144.8716
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] NEAR-USD oi_divergence_long (long) (-207.7)
  Triggered: price_chg_1h=-0.019337, oi_chg_1h=-0.018896, oi_at_entry=36682757.032
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [STOP OVERSHOOT] intended risk 0.02975/unit, actual loss 0.0618/unit (2.1x) -- price moved past the stop faster than the bot's bar-close check could exit; a violent move against the position, amplified by simulation lag rather than a bad entry call

[LOSS] FET-USD oi_divergence_long (long) (-7.13)
  Triggered: price_chg_1h=-0.01148, oi_chg_1h=-0.034843, oi_at_entry=479201.74
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] NEAR-USD triple_ma_short (short) (+49.93)
  Triggered: EMA(8/16/25) = 2.40297/2.40699/2.40824, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] FET-USD triple_ma_short (short) (-65.6)
  Triggered: EMA(8/16/25) = 0.173722/0.173884/0.17391, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] XRP-USD oi_divergence_long (long) (+12.82)
  Triggered: price_chg_1h=-0.006045, oi_chg_1h=-0.01007, oi_at_entry=122681479.8255
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (win)

[WIN] SOL-USD oi_divergence_long (long) (+7.795)
  Triggered: price_chg_1h=-0.0059, oi_chg_1h=-0.015208, oi_at_entry=341270328.9058
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (win)

[WIN] FET-USD triple_ma_long (long) (+53.07)
  Triggered: EMA(8/16/25) = 0.174164/0.174007/0.173961, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] AVAX-USD oi_divergence_long (long) (-11.85)
  Triggered: price_chg_1h=-0.008923, oi_chg_1h=-0.010911, oi_at_entry=12428161.6225
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] AVAX-USD oi_divergence_long (long) (+20.1)
  Triggered: price_chg_1h=-0.005068, oi_chg_1h=-0.014266, oi_at_entry=12334266.6392
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (win)

[LOSS] XRP-USD triple_ma_long (long) (-159.3)
  Triggered: EMA(8/16/25) = 1.40699/1.40492/1.40475, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] BTC-USD triple_ma_short (short) (+52.49)
  Triggered: EMA(8/16/25) = 79,463.4/79,467.8/79,489.3, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] SOL-USD oi_divergence_long (long) (-100.8)
  Triggered: price_chg_1h=-0.005959, oi_chg_1h=-0.010594, oi_at_entry=343238532.2076
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] XRP-USD triple_ma_short (short) (+40.66)
  Triggered: EMA(8/16/25) = 1.40365/1.40369/1.40396, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] NEAR-USD oi_divergence_long (long) (-103.5)
  Triggered: price_chg_1h=-0.009451, oi_chg_1h=-0.014325, oi_at_entry=33473996.61
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] FET-USD oi_divergence_long (long) (+39.39)
  Triggered: price_chg_1h=-0.016747, oi_chg_1h=-0.01596, oi_at_entry=608994.107
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (win)

[WIN] ETH-USD triple_ma_short (short) (+38)
  Triggered: EMA(8/16/25) = 2,493.56/2,494.38/2,494.69, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] SOL-USD triple_ma_short (short) (+62.08)
  Triggered: EMA(8/16/25) = 104.93/105.022/105.044, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] NEAR-USD oi_divergence_long (long) (-141.3)
  Triggered: price_chg_1h=-0.011936, oi_chg_1h=-0.01019, oi_at_entry=33261686.57
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] NEAR-USD triple_ma_short (short) (+53.28)
  Triggered: EMA(8/16/25) = 2.35949/2.36116/2.36286, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] XRP-USD oi_divergence_long (long) (+20.45)
  Triggered: price_chg_1h=-0.009393, oi_chg_1h=-0.026151, oi_at_entry=120494421.1264
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (win)

[WIN] AVAX-USD oi_divergence_long (long) (+81.77)
  Triggered: price_chg_1h=-0.006699, oi_chg_1h=-0.0165, oi_at_entry=12457537.7056
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (win)

**US -- WHY** (2026-09-07)
No setups fired.

---

## 2026-09-09 00:00 IST

**INDIA -- WHY** (2026-09-08)
- Fired: 23 | Resolved: 22 | Still open: 1

[WIN] VEDL.NS triple_threat_long (long) (+357.1)
  Triggered: RSI 35->67 crossed 50, broke 269.5, trend EMA 269.4
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] NATIONALUM.NS triple_threat_long (long) (+332.8)
  Triggered: RSI 25->63 crossed 50, broke 370.9, trend EMA 370.3
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] BANKINDIA.NS triple_threat_short (short) (-1,425)
  Triggered: RSI 52->35 crossed 50, broke 141.5, trend EMA 142.5
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] IRFC.NS breakdown_short (short) (-909.3)
  Triggered: broke range low 82.49 on vol 222,375 vs avg 221,592, trend EMA 82.88; India gate: RSI 11.83 / VWAP 82.67 (rsi<40 and close<=vwap)
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] JPPOWER.NS triple_ma_short (short) (+564.5)
  Triggered: EMA(8/16/25) = 16.5675/16.6104/16.6122, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] NHPC.NS breakdown_short (short) (-599.5)
  Triggered: broke range low 75.1 on vol 735,435 vs avg 186,351, trend EMA 75.35; India gate: RSI 30.84 / VWAP 75.31 (rsi<40 and close<=vwap)
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] JPPOWER.NS triple_ma_short (short) (+801.5)
  Triggered: EMA(8/16/25) = 16.5787/16.6048/16.6078, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] IRFC.NS breakdown_short (short) (+1,096)
  Triggered: broke range low 82.3 on vol 305,428 vs avg 175,872, trend EMA 82.47; India gate: RSI 14.68 / VWAP 82.53 (rsi<40 and close<=vwap)
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] IDEA.NS triple_ma_long (long) (-2,468)
  Triggered: EMA(8/16/25) = 15.4767/15.4758/15.4632, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] IDEA.NS triple_ma_long (long) (+645.6)
  Triggered: EMA(8/16/25) = 15.4779/15.4764/15.4651, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] VEDL.NS triple_ma_long (long) (-1,756)
  Triggered: EMA(8/16/25) = 270.625/270.61/270.487, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] POWERGRID.NS triple_ma_short (short) (+752.1)
  Triggered: EMA(8/16/25) = 265.38/265.388/265.62, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] NATIONALUM.NS triple_ma_short (short) (+472.7)
  Triggered: EMA(8/16/25) = 371.594/372.241/372.294, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] RPOWER.NS breakdown_short (short) (-1,848)
  Triggered: broke range low 21.7 on vol 793,361 vs avg 261,344, trend EMA 21.74; India gate: RSI 31.71 / VWAP 21.79 (rsi<40 and close<=vwap)
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] IOC.NS breakdown_short (short) (-2,252)
  Triggered: broke range low 134.2 on vol 1,121,987 vs avg 131,485, trend EMA 134.2; India gate: RSI 7.73 / VWAP 134.4 (rsi<40 and close<=vwap)
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] POWERGRID.NS triple_ma_short (short) (-1,887)
  Triggered: EMA(8/16/25) = 265.318/265.36/265.555, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] VEDL.NS triple_ma_short (short) (-1,762)
  Triggered: EMA(8/16/25) = 270.034/270.253/270.27, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] BEL.NS triple_ma_long (long) (+546.9)
  Triggered: EMA(8/16/25) = 411.914/411.909/411.366, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] VEDL.NS triple_ma_short (short) (-1,203)
  Triggered: EMA(8/16/25) = 270.158/270.298/270.299, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] BEL.NS triple_ma_long (long) (-849.4)
  Triggered: EMA(8/16/25) = 411.96/411.929/411.451, freshly aligned
  Outcome:   session ended before stop or target hit -- settled at the day's close (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via eod_settlement; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] VEDL.NS triple_ma_long (long) (-92.31)
  Triggered: EMA(8/16/25) = 270.428/270.399/270.373, freshly aligned
  Outcome:   session ended before stop or target hit -- settled at the day's close (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via eod_settlement; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] HUDCO.NS triple_threat_long (long) (-754.5)
  Triggered: RSI 48->58 crossed 50, broke 178.8, trend EMA 178.4
  Outcome:   session ended before stop or target hit -- settled at the day's close (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via eod_settlement; the market simply moved the other way this time (normal strategy variance, not a bug)

Still open (too soon to say why it worked or not):
  ETERNAL.NS triple_threat_long (long) -- triggered: RSI 49->57 crossed 50, broke 323.4, trend EMA 322.3

**CRYPTO -- WHY** (2026-09-08)
- Fired: 60 | Resolved: 59 | Still open: 1

[LOSS] NEAR-USD oi_divergence_long (long) (-17.23)
  Triggered: price_chg_1h=-0.012904, oi_chg_1h=-0.013816, oi_at_entry=32216594.82
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] FET-USD oi_divergence_long (long) (+3.598)
  Triggered: price_chg_1h=-0.011964, oi_chg_1h=-0.024888, oi_at_entry=644720.243
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (win)

[WIN] AVAX-USD oi_divergence_long (long) (+35.21)
  Triggered: price_chg_1h=-0.010304, oi_chg_1h=-0.022467, oi_at_entry=12688950.2074
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (win)

[LOSS] XRP-USD triple_ma_short (short) (-40.47)
  Triggered: EMA(8/16/25) = 1.39587/1.39592/1.39674, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] SOL-USD triple_ma_short (short) (+67.49)
  Triggered: EMA(8/16/25) = 104.046/104.056/104.138, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] AVAX-USD oi_divergence_long (long) (+43)
  Triggered: price_chg_1h=-0.009091, oi_chg_1h=-0.010343, oi_at_entry=12639557.9309
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (win)

[LOSS] FET-USD oi_divergence_long (long) (+0)
  Triggered: price_chg_1h=-0.017654, oi_chg_1h=-0.025812, oi_at_entry=655024.528
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] NEAR-USD oi_divergence_long (long) (+0)
  Triggered: price_chg_1h=-0.006288, oi_chg_1h=-0.010699, oi_at_entry=32096482.393
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] AVAX-USD oi_divergence_long (long) (-2.226)
  Triggered: price_chg_1h=-0.010059, oi_chg_1h=-0.017128, oi_at_entry=12625714.6623
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] NEAR-USD triple_ma_short (short) (-70.46)
  Triggered: EMA(8/16/25) = 2.31689/2.31771/2.32093, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] BTC-USD triple_ma_short (short) (+79.21)
  Triggered: EMA(8/16/25) = 79,179.8/79,183.2/79,187.3, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] XRP-USD triple_ma_short (short) (+50.51)
  Triggered: EMA(8/16/25) = 1.39699/1.39719/1.3973, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] FET-USD oi_divergence_long (long) (-107.9)
  Triggered: price_chg_1h=-0.027942, oi_chg_1h=-0.010114, oi_at_entry=678846.87
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] NEAR-USD oi_divergence_long (long) (+19.51)
  Triggered: price_chg_1h=-0.012583, oi_chg_1h=-0.010229, oi_at_entry=32031249.484
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (win)

[LOSS] ETH-USD triple_ma_short (short) (-52.12)
  Triggered: EMA(8/16/25) = 2,487.59/2,489.04/2,489.31, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] SOL-USD oi_divergence_long (long) (+39.06)
  Triggered: price_chg_1h=-0.005677, oi_chg_1h=-0.011673, oi_at_entry=340833334.6761
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (win)

[WIN] FET-USD triple_ma_long (long) (+46.45)
  Triggered: EMA(8/16/25) = 0.183073/0.183024/0.182802, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] BTC-USD triple_ma_long (long) (-53.07)
  Triggered: EMA(8/16/25) = 79,209/79,161.4/79,153.7, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] FET-USD breakout_long (long) (-79.95)
  Triggered: broke range high 0.1871 on vol 770,032 vs avg 428,211, trend EMA 0.1856, 2-bar + retest
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] SOL-USD triple_ma_long (long) (-65.85)
  Triggered: EMA(8/16/25) = 104.082/103.979/103.97, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] NEAR-USD oi_divergence_long (long) (+0)
  Triggered: price_chg_1h=-0.011828, oi_chg_1h=-0.012849, oi_at_entry=32400089.566
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] AVAX-USD oi_divergence_long (long) (+4.722)
  Triggered: price_chg_1h=-0.011788, oi_chg_1h=-0.030977, oi_at_entry=12489684.8888
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (win)

[LOSS] NEAR-USD oi_divergence_long (long) (-166.1)
  Triggered: price_chg_1h=-0.009885, oi_chg_1h=-0.01031, oi_at_entry=32190952.499
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [STOP OVERSHOOT] intended risk 0.02528/unit, actual loss 0.042/unit (1.7x) -- price moved past the stop faster than the bot's bar-close check could exit; a violent move against the position, amplified by simulation lag rather than a bad entry call

[LOSS] SOL-USD triple_ma_short (short) (-2.405)
  Triggered: EMA(8/16/25) = 103.841/103.888/103.914, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] BTC-USD triple_ma_short (short) (-7.371)
  Triggered: EMA(8/16/25) = 79,103.4/79,139.7/79,148, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] AVAX-USD triple_ma_short (short) (-52.72)
  Triggered: EMA(8/16/25) = 8.07253/8.08331/8.08465, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] ETH-USD triple_ma_short (short) (+33.92)
  Triggered: EMA(8/16/25) = 2,488.38/2,490.18/2,490.43, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] FET-USD oi_divergence_long (long) (+7.016)
  Triggered: price_chg_1h=-0.008798, oi_chg_1h=-0.01356, oi_at_entry=722374.33
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (win)

[LOSS] XRP-USD triple_ma_short (short) (-42.4)
  Triggered: EMA(8/16/25) = 1.39571/1.39688/1.39708, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] NEAR-USD triple_ma_short (short) (-47.23)
  Triggered: EMA(8/16/25) = 2.31397/2.31974/2.32075, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] NEAR-USD oi_divergence_long (long) (+0)
  Triggered: price_chg_1h=-0.01799, oi_chg_1h=-0.010602, oi_at_entry=31732737.979
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] FET-USD oi_divergence_long (long) (+0)
  Triggered: price_chg_1h=-0.019294, oi_chg_1h=-0.076949, oi_at_entry=671413.444
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] FET-USD triple_ma_short (short) (-44.86)
  Triggered: EMA(8/16/25) = 0.184229/0.184929/0.184971, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] SOL-USD oi_divergence_long (long) (+0)
  Triggered: price_chg_1h=-0.005045, oi_chg_1h=-0.011893, oi_at_entry=337657174.8343
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] FET-USD oi_divergence_long (long) (+25.08)
  Triggered: price_chg_1h=-0.007871, oi_chg_1h=-0.025369, oi_at_entry=679391.02
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (win)

[LOSS] FET-USD triple_ma_short (short) (-50.4)
  Triggered: EMA(8/16/25) = 0.184762/0.185019/0.185061, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] NEAR-USD oi_divergence_long (long) (-124.4)
  Triggered: price_chg_1h=-0.011181, oi_chg_1h=-0.010998, oi_at_entry=32513190.657
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] FET-USD oi_divergence_long (long) (-137.7)
  Triggered: price_chg_1h=-0.010057, oi_chg_1h=-0.042539, oi_at_entry=692858.033
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] BTC-USD triple_ma_short (short) (-9.864)
  Triggered: EMA(8/16/25) = 78,545.2/78,559/78,595.7, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] SOL-USD oi_divergence_long (long) (+28.57)
  Triggered: price_chg_1h=-0.008201, oi_chg_1h=-0.013528, oi_at_entry=337783718.88
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (win)

[WIN] XRP-USD oi_divergence_long (long) (+59.7)
  Triggered: price_chg_1h=-0.00508, oi_chg_1h=-0.010327, oi_at_entry=122800823.8044
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (win)

[LOSS] ETH-USD triple_ma_short (short) (-4.375)
  Triggered: EMA(8/16/25) = 2,479.89/2,480.47/2,480.67, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] SOL-USD triple_ma_short (short) (+4.473)
  Triggered: EMA(8/16/25) = 103.191/103.193/103.2, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] AVAX-USD oi_divergence_long (long) (-9.915)
  Triggered: price_chg_1h=-0.014102, oi_chg_1h=-0.018709, oi_at_entry=12734835.6482
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] SOL-USD oi_divergence_long (long) (-15.27)
  Triggered: price_chg_1h=-0.005028, oi_chg_1h=-0.011218, oi_at_entry=337991163.644
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] AVAX-USD triple_ma_short (short) (+172.9)
  Triggered: EMA(8/16/25) = 8.06059/8.0675/8.06853, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] NEAR-USD triple_ma_short (short) (-44.48)
  Triggered: EMA(8/16/25) = 2.29857/2.30319/2.3037, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] XRP-USD triple_ma_long (long) (+32.98)
  Triggered: EMA(8/16/25) = 1.39336/1.39334/1.39306, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] FET-USD oi_divergence_long (long) (-84.94)
  Triggered: price_chg_1h=-0.013536, oi_chg_1h=-0.063463, oi_at_entry=595857.561
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] SOL-USD oi_divergence_long (long) (+82.12)
  Triggered: price_chg_1h=-0.009608, oi_chg_1h=-0.0121, oi_at_entry=335978920.3601
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (win)

[WIN] AVAX-USD oi_divergence_long (long) (+37.01)
  Triggered: price_chg_1h=-0.019291, oi_chg_1h=-0.029266, oi_at_entry=12394384.3075
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (win)

[LOSS] NEAR-USD oi_divergence_long (long) (-4.392)
  Triggered: price_chg_1h=-0.010794, oi_chg_1h=-0.023645, oi_at_entry=32957666.42
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] FET-USD oi_divergence_long (long) (+5.871)
  Triggered: price_chg_1h=-0.015437, oi_chg_1h=-0.021352, oi_at_entry=606776.508
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (win)

[LOSS] NEAR-USD oi_divergence_long (long) (-9.18)
  Triggered: price_chg_1h=-0.011992, oi_chg_1h=-0.014165, oi_at_entry=33103488.249
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] AVAX-USD oi_divergence_long (long) (+0)
  Triggered: price_chg_1h=-0.005467, oi_chg_1h=-0.019975, oi_at_entry=12390356.1046
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] NEAR-USD oi_divergence_long (long) (+0)
  Triggered: price_chg_1h=-0.019545, oi_chg_1h=-0.01556, oi_at_entry=32671323.966
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] XRP-USD oi_divergence_long (long) (+85.95)
  Triggered: price_chg_1h=-0.00599, oi_chg_1h=-0.011349, oi_at_entry=124946519.4056
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (win)

[LOSS] AVAX-USD triple_ma_short (short) (-33.45)
  Triggered: EMA(8/16/25) = 8.02115/8.02261/8.02534, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] FET-USD oi_divergence_long (long) (+28.46)
  Triggered: price_chg_1h=-0.017191, oi_chg_1h=-0.012322, oi_at_entry=599773.083
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (win)

Still open (too soon to say why it worked or not):
  FET-USD triple_ma_short (short) -- triggered: EMA(8/16/25) = 0.181835/0.181988/0.182122, freshly aligned

**US -- WHY** (2026-09-08)
- Fired: 20 | Resolved: 17 | Still open: 3

[WIN] INTC triple_ma_long (long) (+1,180)
  Triggered: EMA(8/16/25) = 96.4601/95.5866/94.9769, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] RIOT triple_ma_long (long) (+369.1)
  Triggered: EMA(8/16/25) = 21.6983/21.5976/21.4613, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] CLF triple_ma_long (long) (-711.6)
  Triggered: EMA(8/16/25) = 12.4739/12.4406/12.4187, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] NKE triple_ma_long (long) (-368.7)
  Triggered: EMA(8/16/25) = 38.455/38.4512/38.4418, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] NKE triple_threat_long (long) (-624.3)
  Triggered: RSI 45->58 crossed 50, broke 38.65, trend EMA 38.46
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] INTC triple_ma_long (long) (+1,954)
  Triggered: EMA(8/16/25) = 98.1442/96.7081/95.8131, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] RIOT triple_ma_long (long) (+118.1)
  Triggered: EMA(8/16/25) = 21.9569/21.768/21.5962, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] OXY triple_ma_long (long) (-1,134)
  Triggered: EMA(8/16/25) = 60.7973/60.525/60.4472, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] CLF triple_ma_long (long) (-904.4)
  Triggered: EMA(8/16/25) = 12.5484/12.4904/12.4566, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] MARA triple_ma_long (long) (+859.3)
  Triggered: EMA(8/16/25) = 11.4314/11.3918/11.3725, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] INTC triple_ma_long (long) (+1,789)
  Triggered: EMA(8/16/25) = 98.1315/96.7014/95.8087, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] RIOT triple_ma_long (long) (-32.54)
  Triggered: EMA(8/16/25) = 21.9303/21.7538/21.587, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] MARA triple_ma_long (long) (+1,108)
  Triggered: EMA(8/16/25) = 11.417/11.3841/11.3675, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] OXY triple_ma_long (long) (-330.1)
  Triggered: EMA(8/16/25) = 60.8273/60.5409/60.4576, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] CLF triple_ma_long (long) (-1,186)
  Triggered: EMA(8/16/25) = 12.5339/12.4828/12.4516, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] DAL triple_ma_long (long) (-334)
  Triggered: EMA(8/16/25) = 79.6025/79.6003/79.5825, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] DAL triple_ma_long (long) (-75.21)
  Triggered: EMA(8/16/25) = 79.7201/79.7142/79.6907, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

Still open (too soon to say why it worked or not):
  GOLD triple_ma_long (long) -- triggered: EMA(8/16/25) = 45.7866/45.435/44.9771, freshly aligned
  RIVN triple_ma_long (long) -- triggered: EMA(8/16/25) = 15.7711/15.7509/15.746, freshly aligned
  DAL triple_ma_long (long) -- triggered: EMA(8/16/25) = 79.7273/79.7183/79.6948, freshly aligned

---

## 2026-09-10 00:01 IST

**INDIA -- WHY** (2026-09-09)
- Fired: 12 | Resolved: 12 | Still open: 0

[LOSS] JPPOWER.NS range_long_rejection (long) (-4,630)
  Triggered: wicked to 16.41 near range low [16.45, 16.92], closed back inside; India gate: RSI 62.5 / VWAP 16.56 (rsi>60 and close>=vwap)
  Outcome:   session ended before stop or target hit -- settled at the day's close (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via eod_settlement; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] IDEA.NS breakdown_short (short) (-1,650)
  Triggered: broke range low 15.31 on vol 35,334,948 vs avg 11,281,417, trend EMA 15.41; India gate: RSI 29.31 / VWAP 15.28 (rsi<40 and close<=vwap)
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] JPPOWER.NS triple_threat_long (long) (-3,307)
  Triggered: RSI 33->65 crossed 50, broke 16.62, trend EMA 16.56
  Outcome:   session ended before stop or target hit -- settled at the day's close (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via eod_settlement; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] IDEA.NS triple_ma_long (long) (+5,833)
  Triggered: EMA(8/16/25) = 15.4648/15.45/15.4495, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] POWERGRID.NS triple_ma_short (short) (-3,588)
  Triggered: EMA(8/16/25) = 265.758/266.055/266.091, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] JPPOWER.NS triple_ma_short (short) (+443)
  Triggered: EMA(8/16/25) = 16.5643/16.5748/16.581, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] POWERGRID.NS triple_ma_long (long) (+1,164)
  Triggered: EMA(8/16/25) = 266.312/266.309/266.274, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] IRCON.NS breakdown_short (short) (+432.7)
  Triggered: broke range low 115.6 on vol 55,251 vs avg 34,111, trend EMA 116; India gate: RSI 31.35 / VWAP 116.3 (rsi<40 and close<=vwap)
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] ETERNAL.NS breakdown_short (short) (-1,335)
  Triggered: broke range low 318.5 on vol 1,225,675 vs avg 773,293, trend EMA 319.5; India gate: RSI 39.42 / VWAP 319.8 (rsi<40 and close<=vwap)
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] RPOWER.NS triple_ma_short (short) (-864.2)
  Triggered: EMA(8/16/25) = 22.0119/22.0641/22.0676, freshly aligned
  Outcome:   session ended before stop or target hit -- settled at the day's close (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via eod_settlement; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] SUZLON.NS triple_ma_short (short) (+439.7)
  Triggered: EMA(8/16/25) = 45.6432/45.7164/45.7224, freshly aligned
  Outcome:   session ended before stop or target hit -- settled at the day's close (win)

[LOSS] NHPC.NS triple_ma_long (long) (-4,157)
  Triggered: EMA(8/16/25) = 76.6797/76.6445/76.5652, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

**CRYPTO -- WHY** (2026-09-09)
- Fired: 59 | Resolved: 54 | Still open: 5

[LOSS] AVAX-USD triple_ma_short (short) (-52.39)
  Triggered: EMA(8/16/25) = 8.0163/8.02023/8.02321, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] SOL-USD oi_divergence_long (long) (+36.46)
  Triggered: price_chg_1h=-0.006821, oi_chg_1h=-0.012919, oi_at_entry=333498365.6588
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] XRP-USD oi_divergence_long (long) (+0)
  Triggered: price_chg_1h=-0.008541, oi_chg_1h=-0.011754, oi_at_entry=123950678.5737
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] NEAR-USD oi_divergence_long (long) (-88.59)
  Triggered: price_chg_1h=-0.005996, oi_chg_1h=-0.010634, oi_at_entry=32533717.022
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] BTC-USD triple_ma_short (short) (-37.31)
  Triggered: EMA(8/16/25) = 78,490.9/78,519.8/78,522.5, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] NEAR-USD oi_divergence_long (long) (-100.4)
  Triggered: price_chg_1h=-0.006498, oi_chg_1h=-0.014134, oi_at_entry=32259145.277
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] XRP-USD oi_divergence_long (long) (-20.51)
  Triggered: price_chg_1h=-0.005743, oi_chg_1h=-0.025915, oi_at_entry=120738502.8462
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] NEAR-USD triple_ma_short (short) (-31.24)
  Triggered: EMA(8/16/25) = 2.33343/2.34414/2.34539, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] SOL-USD triple_ma_short (short) (-59.25)
  Triggered: EMA(8/16/25) = 103.375/103.479/103.487, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] XRP-USD oi_divergence_long (long) (+52.83)
  Triggered: price_chg_1h=-0.005902, oi_chg_1h=-0.012615, oi_at_entry=121599209.0778
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (win)

[LOSS] ETH-USD triple_ma_short (short) (-71.08)
  Triggered: EMA(8/16/25) = 2,484.18/2,485.52/2,485.59, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] BTC-USD triple_ma_short (short) (-46.98)
  Triggered: EMA(8/16/25) = 78,509.9/78,520.7/78,522.1, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] XRP-USD triple_ma_short (short) (-41.78)
  Triggered: EMA(8/16/25) = 1.41902/1.42043/1.42045, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] BTC-USD triple_ma_long (long) (+14.7)
  Triggered: EMA(8/16/25) = 78,528.9/78,518.5/78,517.6, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] ETH-USD triple_ma_long (long) (-36.45)
  Triggered: EMA(8/16/25) = 2,487.15/2,486.34/2,486.04, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] AVAX-USD triple_ma_short (short) (+8.113)
  Triggered: EMA(8/16/25) = 7.9899/7.99243/7.99562, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] FET-USD triple_ma_short (short) (+41.7)
  Triggered: EMA(8/16/25) = 0.179277/0.17942/0.179589, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] NEAR-USD oi_divergence_long (long) (+0)
  Triggered: price_chg_1h=-0.01073, oi_chg_1h=-0.014186, oi_at_entry=32355289.892
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] FET-USD oi_divergence_long (long) (-154.6)
  Triggered: price_chg_1h=-0.010941, oi_chg_1h=-0.014918, oi_at_entry=632705.851
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [STOP OVERSHOOT] intended risk 0.001675/unit, actual loss 0.00259/unit (1.5x) -- price moved past the stop faster than the bot's bar-close check could exit; a violent move against the position, amplified by simulation lag rather than a bad entry call

[LOSS] NEAR-USD oi_divergence_long (long) (-40.57)
  Triggered: price_chg_1h=-0.014464, oi_chg_1h=-0.016866, oi_at_entry=31775546.438
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] NEAR-USD triple_ma_short (short) (+44.52)
  Triggered: EMA(8/16/25) = 2.32321/2.32518/2.32683, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] FET-USD oi_divergence_long (long) (-9.765)
  Triggered: price_chg_1h=-0.01099, oi_chg_1h=-0.049669, oi_at_entry=587105.883
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] SOL-USD triple_ma_short (short) (-75.2)
  Triggered: EMA(8/16/25) = 103.402/103.473/103.478, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] BTC-USD triple_ma_long (long) (+61.9)
  Triggered: EMA(8/16/25) = 78,699.2/78,686.2/78,662.2, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] ETH-USD triple_ma_long (long) (+58.1)
  Triggered: EMA(8/16/25) = 2,492.13/2,491.84/2,491.04, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] AVAX-USD oi_divergence_long (long) (+28.93)
  Triggered: price_chg_1h=-0.009566, oi_chg_1h=-0.010447, oi_at_entry=12695023.0555
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (win)

[LOSS] FET-USD oi_divergence_long (long) (-15.96)
  Triggered: price_chg_1h=-0.010425, oi_chg_1h=-0.012998, oi_at_entry=621490.751
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] FET-USD oi_divergence_long (long) (+0)
  Triggered: price_chg_1h=-0.005908, oi_chg_1h=-0.010008, oi_at_entry=617247.484
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] FET-USD oi_divergence_long (long) (-142.5)
  Triggered: price_chg_1h=-0.005635, oi_chg_1h=-0.01014, oi_at_entry=615297.482
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] SOL-USD oi_divergence_long (long) (-203)
  Triggered: price_chg_1h=-0.006763, oi_chg_1h=-0.012041, oi_at_entry=330937570.3073
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [STOP OVERSHOOT] intended risk 0.335/unit, actual loss 0.68/unit (2.0x) -- price moved past the stop faster than the bot's bar-close check could exit; a violent move against the position, amplified by simulation lag rather than a bad entry call

[LOSS] XRP-USD oi_divergence_long (long) (-118.1)
  Triggered: price_chg_1h=-0.008466, oi_chg_1h=-0.02117, oi_at_entry=126086149.1663
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] AVAX-USD oi_divergence_long (long) (-132.8)
  Triggered: price_chg_1h=-0.011456, oi_chg_1h=-0.014949, oi_at_entry=12662655.0534
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] FET-USD triple_ma_short (short) (-20.71)
  Triggered: EMA(8/16/25) = 0.177735/0.17813/0.178243, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] AVAX-USD triple_ma_short (short) (-28.81)
  Triggered: EMA(8/16/25) = 7.9773/7.99488/7.99888, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] NEAR-USD oi_divergence_long (long) (+0)
  Triggered: price_chg_1h=-0.016156, oi_chg_1h=-0.018497, oi_at_entry=35314089.21
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] XRP-USD triple_ma_short (short) (-119.5)
  Triggered: EMA(8/16/25) = 1.42667/1.42946/1.42956, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] ETH-USD triple_ma_short (short) (-56.09)
  Triggered: EMA(8/16/25) = 2,497.34/2,501.17/2,501.5, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] SOL-USD triple_ma_short (short) (-45.2)
  Triggered: EMA(8/16/25) = 103.987/104.143/104.149, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] BTC-USD triple_ma_short (short) (-58.86)
  Triggered: EMA(8/16/25) = 79,022.7/79,092.7/79,094, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] NEAR-USD breakout_long (long) (+5.123)
  Triggered: broke range high 2.555 on vol 231,652 vs avg 166,625, trend EMA 2.526, 2-bar + retest
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] SOL-USD triple_ma_long (long) (-85.32)
  Triggered: EMA(8/16/25) = 104.223/104.158/104.14, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] FET-USD triple_ma_long (long) (-36.81)
  Triggered: EMA(8/16/25) = 0.178228/0.177956/0.177937, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] SOL-USD oi_divergence_long (long) (+48.44)
  Triggered: price_chg_1h=-0.007935, oi_chg_1h=-0.011426, oi_at_entry=327478473.7942
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (win)

[WIN] XRP-USD oi_divergence_long (long) (+11.81)
  Triggered: price_chg_1h=-0.006821, oi_chg_1h=-0.012385, oi_at_entry=126045920.8571
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (win)

[WIN] NEAR-USD oi_divergence_long (long) (+5.604)
  Triggered: price_chg_1h=-0.009618, oi_chg_1h=-0.011164, oi_at_entry=38193117.285
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (win)

[WIN] AVAX-USD triple_ma_short (short) (+51.4)
  Triggered: EMA(8/16/25) = 7.96789/7.9679/7.97145, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] FET-USD triple_ma_short (short) (-35.78)
  Triggered: EMA(8/16/25) = 0.17794/0.177974/0.177978, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] FET-USD triple_ma_short (short) (-21.47)
  Triggered: EMA(8/16/25) = 0.17794/0.177978/0.177988, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] XRP-USD triple_ma_short (short) (+38.73)
  Triggered: EMA(8/16/25) = 1.42839/1.42891/1.42893, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] FET-USD triple_ma_long (long) (-83.14)
  Triggered: EMA(8/16/25) = 0.178015/0.17801/0.178008, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] FET-USD triple_ma_short (short) (-36.37)
  Triggered: EMA(8/16/25) = 0.177149/0.177554/0.177711, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] XRP-USD oi_divergence_long (long) (-33.19)
  Triggered: price_chg_1h=-0.008472, oi_chg_1h=-0.01296, oi_at_entry=125875165.9316
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] AVAX-USD oi_divergence_long (long) (-27.83)
  Triggered: price_chg_1h=-0.008427, oi_chg_1h=-0.010644, oi_at_entry=12760611.038
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] NEAR-USD oi_divergence_long (long) (+12.26)
  Triggered: price_chg_1h=-0.030061, oi_chg_1h=-0.022809, oi_at_entry=37570190.53
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (win)

Still open (too soon to say why it worked or not):
  SOL-USD triple_ma_short (short) -- triggered: EMA(8/16/25) = 104.058/104.118/104.127, freshly aligned
  BTC-USD triple_ma_short (short) -- triggered: EMA(8/16/25) = 78,987.4/79,105.6/79,134.9, freshly aligned
  ETH-USD triple_ma_short (short) -- triggered: EMA(8/16/25) = 2,499.36/2,501.05/2,501.27, freshly aligned
  AVAX-USD triple_ma_short (short) -- triggered: EMA(8/16/25) = 7.93604/7.93651/7.94198, freshly aligned
  NEAR-USD oi_divergence_long (long) -- triggered: price_chg_1h=-0.019477, oi_chg_1h=-0.0216, oi_at_entry=37815019.437

**US -- WHY** (2026-09-09)
- Fired: 13 | Resolved: 8 | Still open: 5

[LOSS] OXY triple_ma_long (long) (-205.6)
  Triggered: EMA(8/16/25) = 60.7093/60.7039/60.6785, freshly aligned
  Outcome:   session ended before stop or target hit -- settled at the day's close (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via eod_settlement; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] AAL triple_ma_long (long) (-496.6)
  Triggered: EMA(8/16/25) = 13.078/13.0695/13.0685, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] CLF triple_ma_long (long) (-491.2)
  Triggered: EMA(8/16/25) = 12.4743/12.4727/12.4674, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] DKNG triple_ma_long (long) (-64.46)
  Triggered: EMA(8/16/25) = 23.8444/23.8055/23.8025, freshly aligned
  Outcome:   session ended before stop or target hit -- settled at the day's close (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via eod_settlement; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] RIOT triple_ma_long (long) (-841.4)
  Triggered: EMA(8/16/25) = 22.4283/22.4248/22.3476, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] GOLD triple_ma_long (long) (-381)
  Triggered: EMA(8/16/25) = 48.1029/47.5589/47.1461, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] OXY triple_ma_long (long) (+40.41)
  Triggered: EMA(8/16/25) = 61.3795/61.1231/60.9821, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] OXY triple_ma_long (long) (-28.19)
  Triggered: EMA(8/16/25) = 61.3895/61.1284/60.9856, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

Still open (too soon to say why it worked or not):
  MARA triple_ma_long (long) -- triggered: EMA(8/16/25) = 11.9383/11.8879/11.8231, freshly aligned
  GOLD triple_ma_long (long) -- triggered: EMA(8/16/25) = 47.7049/47.3038/46.9508, freshly aligned
  INTC triple_ma_long (long) -- triggered: EMA(8/16/25) = 104.618/104.396/103.501, freshly aligned
  MARA triple_ma_long (long) -- triggered: EMA(8/16/25) = 11.8874/11.8675/11.8194, freshly aligned
  GOLD triple_ma_long (long) -- triggered: EMA(8/16/25) = 48.3945/47.7766/47.3254, freshly aligned

---

## 2026-09-10 00:14 IST

**INDIA -- WHY** (2026-09-09)
- Fired: 12 | Resolved: 12 | Still open: 0

[LOSS] JPPOWER.NS range_long_rejection (long) (-4,630)
  Triggered: wicked to 16.41 near range low [16.45, 16.92], closed back inside; India gate: RSI 62.5 / VWAP 16.56 (rsi>60 and close>=vwap)
  Outcome:   session ended before stop or target hit -- settled at the day's close (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via eod_settlement; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] IDEA.NS breakdown_short (short) (-1,650)
  Triggered: broke range low 15.31 on vol 35,334,948 vs avg 11,281,417, trend EMA 15.41; India gate: RSI 29.31 / VWAP 15.28 (rsi<40 and close<=vwap)
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] JPPOWER.NS triple_threat_long (long) (-3,307)
  Triggered: RSI 33->65 crossed 50, broke 16.62, trend EMA 16.56
  Outcome:   session ended before stop or target hit -- settled at the day's close (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via eod_settlement; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] IDEA.NS triple_ma_long (long) (+5,833)
  Triggered: EMA(8/16/25) = 15.4648/15.45/15.4495, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] POWERGRID.NS triple_ma_short (short) (-3,588)
  Triggered: EMA(8/16/25) = 265.758/266.055/266.091, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] JPPOWER.NS triple_ma_short (short) (+443)
  Triggered: EMA(8/16/25) = 16.5643/16.5748/16.581, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] POWERGRID.NS triple_ma_long (long) (+1,164)
  Triggered: EMA(8/16/25) = 266.312/266.309/266.274, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] IRCON.NS breakdown_short (short) (+432.7)
  Triggered: broke range low 115.6 on vol 55,251 vs avg 34,111, trend EMA 116; India gate: RSI 31.35 / VWAP 116.3 (rsi<40 and close<=vwap)
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] ETERNAL.NS breakdown_short (short) (-1,335)
  Triggered: broke range low 318.5 on vol 1,225,675 vs avg 773,293, trend EMA 319.5; India gate: RSI 39.42 / VWAP 319.8 (rsi<40 and close<=vwap)
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] RPOWER.NS triple_ma_short (short) (-864.2)
  Triggered: EMA(8/16/25) = 22.0119/22.0641/22.0676, freshly aligned
  Outcome:   session ended before stop or target hit -- settled at the day's close (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via eod_settlement; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] SUZLON.NS triple_ma_short (short) (+439.7)
  Triggered: EMA(8/16/25) = 45.6432/45.7164/45.7224, freshly aligned
  Outcome:   session ended before stop or target hit -- settled at the day's close (win)

[LOSS] NHPC.NS triple_ma_long (long) (-4,157)
  Triggered: EMA(8/16/25) = 76.6797/76.6445/76.5652, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

**CRYPTO -- WHY** (2026-09-09)
- Fired: 59 | Resolved: 54 | Still open: 5

[LOSS] AVAX-USD triple_ma_short (short) (-52.39)
  Triggered: EMA(8/16/25) = 8.0163/8.02023/8.02321, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] SOL-USD oi_divergence_long (long) (+36.46)
  Triggered: price_chg_1h=-0.006821, oi_chg_1h=-0.012919, oi_at_entry=333498365.6588
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] XRP-USD oi_divergence_long (long) (+0)
  Triggered: price_chg_1h=-0.008541, oi_chg_1h=-0.011754, oi_at_entry=123950678.5737
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] NEAR-USD oi_divergence_long (long) (-88.59)
  Triggered: price_chg_1h=-0.005996, oi_chg_1h=-0.010634, oi_at_entry=32533717.022
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] BTC-USD triple_ma_short (short) (-37.31)
  Triggered: EMA(8/16/25) = 78,490.9/78,519.8/78,522.5, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] NEAR-USD oi_divergence_long (long) (-100.4)
  Triggered: price_chg_1h=-0.006498, oi_chg_1h=-0.014134, oi_at_entry=32259145.277
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] XRP-USD oi_divergence_long (long) (-20.51)
  Triggered: price_chg_1h=-0.005743, oi_chg_1h=-0.025915, oi_at_entry=120738502.8462
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] NEAR-USD triple_ma_short (short) (-31.24)
  Triggered: EMA(8/16/25) = 2.33343/2.34414/2.34539, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] SOL-USD triple_ma_short (short) (-59.25)
  Triggered: EMA(8/16/25) = 103.375/103.479/103.487, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] XRP-USD oi_divergence_long (long) (+52.83)
  Triggered: price_chg_1h=-0.005902, oi_chg_1h=-0.012615, oi_at_entry=121599209.0778
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (win)

[LOSS] ETH-USD triple_ma_short (short) (-71.08)
  Triggered: EMA(8/16/25) = 2,484.18/2,485.52/2,485.59, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] BTC-USD triple_ma_short (short) (-46.98)
  Triggered: EMA(8/16/25) = 78,509.9/78,520.7/78,522.1, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] XRP-USD triple_ma_short (short) (-41.78)
  Triggered: EMA(8/16/25) = 1.41902/1.42043/1.42045, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] BTC-USD triple_ma_long (long) (+14.7)
  Triggered: EMA(8/16/25) = 78,528.9/78,518.5/78,517.6, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] ETH-USD triple_ma_long (long) (-36.45)
  Triggered: EMA(8/16/25) = 2,487.15/2,486.34/2,486.04, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] AVAX-USD triple_ma_short (short) (+8.113)
  Triggered: EMA(8/16/25) = 7.9899/7.99243/7.99562, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] FET-USD triple_ma_short (short) (+41.7)
  Triggered: EMA(8/16/25) = 0.179277/0.17942/0.179589, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] NEAR-USD oi_divergence_long (long) (+0)
  Triggered: price_chg_1h=-0.01073, oi_chg_1h=-0.014186, oi_at_entry=32355289.892
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] FET-USD oi_divergence_long (long) (-154.6)
  Triggered: price_chg_1h=-0.010941, oi_chg_1h=-0.014918, oi_at_entry=632705.851
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [STOP OVERSHOOT] intended risk 0.001675/unit, actual loss 0.00259/unit (1.5x) -- price moved past the stop faster than the bot's bar-close check could exit; a violent move against the position, amplified by simulation lag rather than a bad entry call

[LOSS] NEAR-USD oi_divergence_long (long) (-40.57)
  Triggered: price_chg_1h=-0.014464, oi_chg_1h=-0.016866, oi_at_entry=31775546.438
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] NEAR-USD triple_ma_short (short) (+44.52)
  Triggered: EMA(8/16/25) = 2.32321/2.32518/2.32683, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] FET-USD oi_divergence_long (long) (-9.765)
  Triggered: price_chg_1h=-0.01099, oi_chg_1h=-0.049669, oi_at_entry=587105.883
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] SOL-USD triple_ma_short (short) (-75.2)
  Triggered: EMA(8/16/25) = 103.402/103.473/103.478, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] BTC-USD triple_ma_long (long) (+61.9)
  Triggered: EMA(8/16/25) = 78,699.2/78,686.2/78,662.2, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] ETH-USD triple_ma_long (long) (+58.1)
  Triggered: EMA(8/16/25) = 2,492.13/2,491.84/2,491.04, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] AVAX-USD oi_divergence_long (long) (+28.93)
  Triggered: price_chg_1h=-0.009566, oi_chg_1h=-0.010447, oi_at_entry=12695023.0555
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (win)

[LOSS] FET-USD oi_divergence_long (long) (-15.96)
  Triggered: price_chg_1h=-0.010425, oi_chg_1h=-0.012998, oi_at_entry=621490.751
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] FET-USD oi_divergence_long (long) (+0)
  Triggered: price_chg_1h=-0.005908, oi_chg_1h=-0.010008, oi_at_entry=617247.484
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] FET-USD oi_divergence_long (long) (-142.5)
  Triggered: price_chg_1h=-0.005635, oi_chg_1h=-0.01014, oi_at_entry=615297.482
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] SOL-USD oi_divergence_long (long) (-203)
  Triggered: price_chg_1h=-0.006763, oi_chg_1h=-0.012041, oi_at_entry=330937570.3073
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [STOP OVERSHOOT] intended risk 0.335/unit, actual loss 0.68/unit (2.0x) -- price moved past the stop faster than the bot's bar-close check could exit; a violent move against the position, amplified by simulation lag rather than a bad entry call

[LOSS] XRP-USD oi_divergence_long (long) (-118.1)
  Triggered: price_chg_1h=-0.008466, oi_chg_1h=-0.02117, oi_at_entry=126086149.1663
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] AVAX-USD oi_divergence_long (long) (-132.8)
  Triggered: price_chg_1h=-0.011456, oi_chg_1h=-0.014949, oi_at_entry=12662655.0534
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] FET-USD triple_ma_short (short) (-20.71)
  Triggered: EMA(8/16/25) = 0.177735/0.17813/0.178243, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] AVAX-USD triple_ma_short (short) (-28.81)
  Triggered: EMA(8/16/25) = 7.9773/7.99488/7.99888, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] NEAR-USD oi_divergence_long (long) (+0)
  Triggered: price_chg_1h=-0.016156, oi_chg_1h=-0.018497, oi_at_entry=35314089.21
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] XRP-USD triple_ma_short (short) (-119.5)
  Triggered: EMA(8/16/25) = 1.42667/1.42946/1.42956, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] ETH-USD triple_ma_short (short) (-56.09)
  Triggered: EMA(8/16/25) = 2,497.34/2,501.17/2,501.5, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] SOL-USD triple_ma_short (short) (-45.2)
  Triggered: EMA(8/16/25) = 103.987/104.143/104.149, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] BTC-USD triple_ma_short (short) (-58.86)
  Triggered: EMA(8/16/25) = 79,022.7/79,092.7/79,094, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] NEAR-USD breakout_long (long) (+5.123)
  Triggered: broke range high 2.555 on vol 231,652 vs avg 166,625, trend EMA 2.526, 2-bar + retest
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] SOL-USD triple_ma_long (long) (-85.32)
  Triggered: EMA(8/16/25) = 104.223/104.158/104.14, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] FET-USD triple_ma_long (long) (-36.81)
  Triggered: EMA(8/16/25) = 0.178228/0.177956/0.177937, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] SOL-USD oi_divergence_long (long) (+48.44)
  Triggered: price_chg_1h=-0.007935, oi_chg_1h=-0.011426, oi_at_entry=327478473.7942
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (win)

[WIN] XRP-USD oi_divergence_long (long) (+11.81)
  Triggered: price_chg_1h=-0.006821, oi_chg_1h=-0.012385, oi_at_entry=126045920.8571
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (win)

[WIN] NEAR-USD oi_divergence_long (long) (+5.604)
  Triggered: price_chg_1h=-0.009618, oi_chg_1h=-0.011164, oi_at_entry=38193117.285
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (win)

[WIN] AVAX-USD triple_ma_short (short) (+51.4)
  Triggered: EMA(8/16/25) = 7.96789/7.9679/7.97145, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] FET-USD triple_ma_short (short) (-35.78)
  Triggered: EMA(8/16/25) = 0.17794/0.177974/0.177978, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] FET-USD triple_ma_short (short) (-21.47)
  Triggered: EMA(8/16/25) = 0.17794/0.177978/0.177988, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] XRP-USD triple_ma_short (short) (+38.73)
  Triggered: EMA(8/16/25) = 1.42839/1.42891/1.42893, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] FET-USD triple_ma_long (long) (-83.14)
  Triggered: EMA(8/16/25) = 0.178015/0.17801/0.178008, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] FET-USD triple_ma_short (short) (-36.37)
  Triggered: EMA(8/16/25) = 0.177149/0.177554/0.177711, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] XRP-USD oi_divergence_long (long) (-33.19)
  Triggered: price_chg_1h=-0.008472, oi_chg_1h=-0.01296, oi_at_entry=125875165.9316
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] AVAX-USD oi_divergence_long (long) (-27.83)
  Triggered: price_chg_1h=-0.008427, oi_chg_1h=-0.010644, oi_at_entry=12760611.038
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] NEAR-USD oi_divergence_long (long) (+12.26)
  Triggered: price_chg_1h=-0.030061, oi_chg_1h=-0.022809, oi_at_entry=37570190.53
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (win)

Still open (too soon to say why it worked or not):
  SOL-USD triple_ma_short (short) -- triggered: EMA(8/16/25) = 104.058/104.118/104.127, freshly aligned
  BTC-USD triple_ma_short (short) -- triggered: EMA(8/16/25) = 78,987.4/79,105.6/79,134.9, freshly aligned
  ETH-USD triple_ma_short (short) -- triggered: EMA(8/16/25) = 2,499.36/2,501.05/2,501.27, freshly aligned
  AVAX-USD triple_ma_short (short) -- triggered: EMA(8/16/25) = 7.93604/7.93651/7.94198, freshly aligned
  NEAR-USD oi_divergence_long (long) -- triggered: price_chg_1h=-0.019477, oi_chg_1h=-0.0216, oi_at_entry=37815019.437

**US -- WHY** (2026-09-09)
- Fired: 13 | Resolved: 8 | Still open: 5

[LOSS] OXY triple_ma_long (long) (-205.6)
  Triggered: EMA(8/16/25) = 60.7093/60.7039/60.6785, freshly aligned
  Outcome:   session ended before stop or target hit -- settled at the day's close (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via eod_settlement; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] AAL triple_ma_long (long) (-496.6)
  Triggered: EMA(8/16/25) = 13.078/13.0695/13.0685, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] CLF triple_ma_long (long) (-491.2)
  Triggered: EMA(8/16/25) = 12.4743/12.4727/12.4674, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] DKNG triple_ma_long (long) (-64.46)
  Triggered: EMA(8/16/25) = 23.8444/23.8055/23.8025, freshly aligned
  Outcome:   session ended before stop or target hit -- settled at the day's close (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via eod_settlement; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] RIOT triple_ma_long (long) (-841.4)
  Triggered: EMA(8/16/25) = 22.4283/22.4248/22.3476, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] GOLD triple_ma_long (long) (-381)
  Triggered: EMA(8/16/25) = 48.1029/47.5589/47.1461, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] OXY triple_ma_long (long) (+40.41)
  Triggered: EMA(8/16/25) = 61.3795/61.1231/60.9821, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] OXY triple_ma_long (long) (-28.19)
  Triggered: EMA(8/16/25) = 61.3895/61.1284/60.9856, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

Still open (too soon to say why it worked or not):
  MARA triple_ma_long (long) -- triggered: EMA(8/16/25) = 11.9383/11.8879/11.8231, freshly aligned
  GOLD triple_ma_long (long) -- triggered: EMA(8/16/25) = 47.7049/47.3038/46.9508, freshly aligned
  INTC triple_ma_long (long) -- triggered: EMA(8/16/25) = 104.618/104.396/103.501, freshly aligned
  MARA triple_ma_long (long) -- triggered: EMA(8/16/25) = 11.8874/11.8675/11.8194, freshly aligned
  GOLD triple_ma_long (long) -- triggered: EMA(8/16/25) = 48.3945/47.7766/47.3254, freshly aligned

---

## 2026-09-11 00:01 IST

**INDIA -- WHY** (2026-09-10)
- Fired: 31 | Resolved: 31 | Still open: 0

[LOSS] IRCON.NS triple_threat_long (long) (-3,662)
  Triggered: RSI 35->67 crossed 50, broke 116.9, trend EMA 116
  Outcome:   session ended before stop or target hit -- settled at the day's close (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via eod_settlement; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] IRFC.NS triple_ma_short (short) (+2,633)
  Triggered: EMA(8/16/25) = 81.7427/81.7433/81.7843, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] RVNL.NS triple_ma_short (short) (+756.6)
  Triggered: EMA(8/16/25) = 207.779/207.782/207.825, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] IDEA.NS breakdown_short (short) (-2,027)
  Triggered: broke range low 15.18 on vol 76,439,755 vs avg 43,235,031, trend EMA 15.34; India gate: RSI 8.33 / VWAP 15.37 (rsi<40 and close<=vwap)
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] IRFC.NS triple_ma_short (short) (+3,977)
  Triggered: EMA(8/16/25) = 81.7446/81.7456/81.7803, freshly aligned
  Outcome:   session ended before stop or target hit -- settled at the day's close (win)

[WIN] IRFC.NS triple_ma_short (short) (+2,450)
  Triggered: EMA(8/16/25) = 81.7502/81.7529/81.778, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] INDIANB.NS triple_ma_short (short) (+2,477)
  Triggered: EMA(8/16/25) = 859.249/859.467/859.479, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] IRCON.NS triple_ma_long (long) (-1,808)
  Triggered: EMA(8/16/25) = 116.136/116.081/116.075, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] HINDCOPPER.NS triple_ma_short (short) (+5,869)
  Triggered: EMA(8/16/25) = 535.439/535.756/535.777, freshly aligned
  Outcome:   session ended before stop or target hit -- settled at the day's close (win)

[LOSS] IRCON.NS triple_ma_long (long) (-2,286)
  Triggered: EMA(8/16/25) = 116.102/116.066/116.065, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] IRFC.NS breakdown_short (short) (-739.6)
  Triggered: broke range low 81.2 on vol 242,690 vs avg 238,179, trend EMA 81.43; India gate: RSI 23.9 / VWAP 81.77 (rsi<40 and close<=vwap)
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] BANKINDIA.NS triple_ma_short (short) (-1,244)
  Triggered: EMA(8/16/25) = 141.154/141.307/141.332, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] ONGC.NS triple_ma_short (short) (-1,970)
  Triggered: EMA(8/16/25) = 236.236/236.462/236.469, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] IRCON.NS triple_ma_long (long) (-2,153)
  Triggered: EMA(8/16/25) = 116.092/116.071/116.07, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] GAIL.NS triple_ma_short (short) (+459.8)
  Triggered: EMA(8/16/25) = 174.698/174.879/174.9, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] HINDCOPPER.NS breakdown_short (short) (+1,836)
  Triggered: broke range low 531 on vol 185,585 vs avg 176,049, trend EMA 533.5; India gate: RSI 23.67 / VWAP 537.4 (rsi<40 and close<=vwap)
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] RVNL.NS breakdown_short (short) (+557.6)
  Triggered: broke range low 206.4 on vol 93,305 vs avg 78,482, trend EMA 206.8; India gate: RSI 37.5 / VWAP 208.4 (rsi<40 and close<=vwap)
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] CANBK.NS triple_ma_short (short) (+1,766)
  Triggered: EMA(8/16/25) = 125.004/125.208/125.232, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] IRCON.NS triple_ma_short (short) (+2,848)
  Triggered: EMA(8/16/25) = 116.017/116.032/116.042, freshly aligned
  Outcome:   session ended before stop or target hit -- settled at the day's close (win)

[LOSS] IDFCFIRSTB.NS triple_ma_long (long) (-1,615)
  Triggered: EMA(8/16/25) = 86.6349/86.6345/86.6255, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] RVNL.NS breakdown_short (short) (-1,482)
  Triggered: broke range low 206.1 on vol 99,284 vs avg 73,907, trend EMA 206.5; India gate: RSI 25.0 / VWAP 208.2 (rsi<40 and close<=vwap)
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] GAIL.NS breakdown_short (short) (-144)
  Triggered: broke range low 173.6 on vol 81,884 vs avg 75,912, trend EMA 174.3; India gate: RSI 26.9 / VWAP 175.1 (rsi<40 and close<=vwap)
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] PNB.NS triple_ma_short (short) (-85.81)
  Triggered: EMA(8/16/25) = 116.717/116.889/116.906, freshly aligned
  Outcome:   session ended before stop or target hit -- settled at the day's close (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via eod_settlement; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] IDFCFIRSTB.NS triple_ma_long (long) (-1,095)
  Triggered: EMA(8/16/25) = 86.6407/86.6358/86.6267, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] JSWENERGY.NS triple_threat_long (long) (+46.91)
  Triggered: RSI 48->69 crossed 50, broke 531.9, trend EMA 531.2
  Outcome:   session ended before stop or target hit -- settled at the day's close (win)

[LOSS] ONGC.NS triple_ma_long (long) (-548.7)
  Triggered: EMA(8/16/25) = 236.54/236.536/236.515, freshly aligned
  Outcome:   session ended before stop or target hit -- settled at the day's close (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via eod_settlement; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] IDFCFIRSTB.NS triple_ma_short (short) (-346.6)
  Triggered: EMA(8/16/25) = 86.5972/86.6109/86.613, freshly aligned
  Outcome:   session ended before stop or target hit -- settled at the day's close (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via eod_settlement; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] ONGC.NS triple_ma_long (long) (-21.12)
  Triggered: EMA(8/16/25) = 236.531/236.52/236.51, freshly aligned
  Outcome:   session ended before stop or target hit -- settled at the day's close (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via eod_settlement; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] RVNL.NS breakdown_short (short) (-1,631)
  Triggered: broke range low 205.7 on vol 382,138 vs avg 111,590, trend EMA 206.2; India gate: RSI 30.06 / VWAP 207.8 (rsi<40 and close<=vwap)
  Outcome:   session ended before stop or target hit -- settled at the day's close (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via eod_settlement; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] JSWENERGY.NS triple_ma_short (short) (-2,594)
  Triggered: EMA(8/16/25) = 530.794/530.836/531, freshly aligned
  Outcome:   session ended before stop or target hit -- settled at the day's close (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via eod_settlement; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] IRFC.NS breakdown_short (short) (-493.8)
  Triggered: broke range low 81.05 on vol 1,091,657 vs avg 196,866, trend EMA 81.17; India gate: RSI 7.46 / VWAP 81.57 (rsi<40 and close<=vwap)
  Outcome:   session ended before stop or target hit -- settled at the day's close (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via eod_settlement; the market simply moved the other way this time (normal strategy variance, not a bug)

**CRYPTO -- WHY** (2026-09-10)
- Fired: 47 | Resolved: 45 | Still open: 2

[WIN] SOL-USD triple_ma_short (short) (+67.99)
  Triggered: EMA(8/16/25) = 103.458/103.476/103.548, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] NEAR-USD oi_divergence_long (long) (-212.4)
  Triggered: price_chg_1h=-0.014136, oi_chg_1h=-0.014548, oi_at_entry=37668208.702
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [STOP OVERSHOOT] intended risk 0.03419/unit, actual loss 0.0726/unit (2.1x) -- price moved past the stop faster than the bot's bar-close check could exit; a violent move against the position, amplified by simulation lag rather than a bad entry call

[LOSS] SOL-USD oi_divergence_long (long) (-133.2)
  Triggered: price_chg_1h=-0.00839, oi_chg_1h=-0.012024, oi_at_entry=319586550.9406
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] AVAX-USD oi_divergence_long (long) (-105.7)
  Triggered: price_chg_1h=-0.00693, oi_chg_1h=-0.010775, oi_at_entry=12854248.8109
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] FET-USD oi_divergence_long (long) (-134.2)
  Triggered: price_chg_1h=-0.012189, oi_chg_1h=-0.044007, oi_at_entry=640203.921
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] XRP-USD oi_divergence_long (long) (-94.28)
  Triggered: price_chg_1h=-0.011526, oi_chg_1h=-0.018462, oi_at_entry=123504124.9471
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] NEAR-USD triple_ma_short (short) (+56.01)
  Triggered: EMA(8/16/25) = 2.54833/2.56846/2.57011, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] FET-USD oi_divergence_long (long) (-135.2)
  Triggered: price_chg_1h=-0.012195, oi_chg_1h=-0.032636, oi_at_entry=635846.096
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] FET-USD oi_divergence_long (long) (+0)
  Triggered: price_chg_1h=-0.010923, oi_chg_1h=-0.016818, oi_at_entry=626713.474
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] NEAR-USD oi_divergence_long (long) (-2.922)
  Triggered: price_chg_1h=-0.019393, oi_chg_1h=-0.016179, oi_at_entry=35465967.549
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] XRP-USD oi_divergence_long (long) (-76.8)
  Triggered: price_chg_1h=-0.005131, oi_chg_1h=-0.019663, oi_at_entry=121490104.3581
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] AVAX-USD oi_divergence_long (long) (-113.2)
  Triggered: price_chg_1h=-0.006607, oi_chg_1h=-0.011577, oi_at_entry=12550660.2516
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] FET-USD oi_divergence_long (long) (-124.4)
  Triggered: price_chg_1h=-0.009915, oi_chg_1h=-0.076035, oi_at_entry=577656.099
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] SOL-USD oi_divergence_long (long) (+44.17)
  Triggered: price_chg_1h=-0.012206, oi_chg_1h=-0.010203, oi_at_entry=317495428.2302
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] AVAX-USD oi_divergence_long (long) (-70.52)
  Triggered: price_chg_1h=-0.012005, oi_chg_1h=-0.010477, oi_at_entry=12452360.325
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] NEAR-USD oi_divergence_long (long) (-4.648)
  Triggered: price_chg_1h=-0.005791, oi_chg_1h=-0.010966, oi_at_entry=35094922.1
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] FET-USD oi_divergence_long (long) (+0)
  Triggered: price_chg_1h=-0.007325, oi_chg_1h=-0.013974, oi_at_entry=606315.336
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] XRP-USD triple_ma_short (short) (-14.3)
  Triggered: EMA(8/16/25) = 1.39007/1.39009/1.39167, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] NEAR-USD oi_divergence_long (long) (-133.1)
  Triggered: price_chg_1h=-0.005934, oi_chg_1h=-0.012271, oi_at_entry=36075370.149
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] SOL-USD triple_ma_long (long) (-41.47)
  Triggered: EMA(8/16/25) = 101.92/101.781/101.779, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] NEAR-USD oi_divergence_long (long) (-118)
  Triggered: price_chg_1h=-0.008215, oi_chg_1h=-0.010893, oi_at_entry=35883719.706
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] XRP-USD triple_ma_short (short) (+14.47)
  Triggered: EMA(8/16/25) = 1.38922/1.38964/1.39079, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] NEAR-USD oi_divergence_long (long) (+4.528)
  Triggered: price_chg_1h=-0.021121, oi_chg_1h=-0.023766, oi_at_entry=35186324.512
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (win)

[WIN] NEAR-USD triple_ma_short (short) (+81.95)
  Triggered: EMA(8/16/25) = 2.48493/2.49082/2.49276, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] FET-USD triple_ma_short (short) (-47.33)
  Triggered: EMA(8/16/25) = 0.169948/0.169993/0.170097, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] BTC-USD triple_ma_long (long) (-37.54)
  Triggered: EMA(8/16/25) = 78,319.6/78,312.1/78,304.3, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] SOL-USD triple_ma_short (short) (+29.59)
  Triggered: EMA(8/16/25) = 101.781/101.786/101.792, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] BTC-USD triple_ma_short (short) (+19.43)
  Triggered: EMA(8/16/25) = 78,225.7/78,262.1/78,273.2, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] AVAX-USD oi_divergence_long (long) (-79.25)
  Triggered: price_chg_1h=-0.007921, oi_chg_1h=-0.01347, oi_at_entry=12451701.3456
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] FET-USD oi_divergence_long (long) (+0)
  Triggered: price_chg_1h=-0.012015, oi_chg_1h=-0.01268, oi_at_entry=616812.789
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] AVAX-USD triple_ma_short (short) (-42.11)
  Triggered: EMA(8/16/25) = 7.79739/7.80732/7.80937, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] NEAR-USD oi_divergence_long (long) (+34.84)
  Triggered: price_chg_1h=-0.027109, oi_chg_1h=-0.022072, oi_at_entry=34857430.837
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (win)

[LOSS] ETH-USD triple_ma_short (short) (-38.28)
  Triggered: EMA(8/16/25) = 2,471.91/2,472.7/2,472.7, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] NEAR-USD oi_divergence_long (long) (-80.61)
  Triggered: price_chg_1h=-0.008383, oi_chg_1h=-0.011915, oi_at_entry=34656845.127
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] FET-USD oi_divergence_long (long) (-161.9)
  Triggered: price_chg_1h=-0.008352, oi_chg_1h=-0.036036, oi_at_entry=599213.827
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [STOP OVERSHOOT] intended risk 0.00113/unit, actual loss 0.00183/unit (1.6x) -- price moved past the stop faster than the bot's bar-close check could exit; a violent move against the position, amplified by simulation lag rather than a bad entry call

[WIN] ETH-USD triple_ma_short (short) (+2.06)
  Triggered: EMA(8/16/25) = 2,471.66/2,472.28/2,472.4, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] AVAX-USD oi_divergence_long (long) (+8.502)
  Triggered: price_chg_1h=-0.005791, oi_chg_1h=-0.011954, oi_at_entry=12319637.2032
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (win)

[LOSS] FET-USD oi_divergence_long (long) (+0)
  Triggered: price_chg_1h=-0.008026, oi_chg_1h=-0.012591, oi_at_entry=590636.111
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] SOL-USD oi_divergence_long (long) (-96.41)
  Triggered: price_chg_1h=-0.012632, oi_chg_1h=-0.036499, oi_at_entry=302981689.2709
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] XRP-USD oi_divergence_long (long) (-79.89)
  Triggered: price_chg_1h=-0.00819, oi_chg_1h=-0.041026, oi_at_entry=118727844.986
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] AVAX-USD oi_divergence_long (long) (-113)
  Triggered: price_chg_1h=-0.012252, oi_chg_1h=-0.011603, oi_at_entry=12228730.8065
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] NEAR-USD oi_divergence_long (long) (-2.847)
  Triggered: price_chg_1h=-0.006651, oi_chg_1h=-0.01327, oi_at_entry=35021453.355
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] FET-USD oi_divergence_long (long) (+0)
  Triggered: price_chg_1h=-0.010712, oi_chg_1h=-0.05467, oi_at_entry=637519.036
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] NEAR-USD triple_ma_short (short) (-63.91)
  Triggered: EMA(8/16/25) = 2.41559/2.41651/2.42034, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] FET-USD oi_divergence_long (long) (+69.49)
  Triggered: price_chg_1h=-0.011538, oi_chg_1h=-0.041651, oi_at_entry=633370.18
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (win)

Still open (too soon to say why it worked or not):
  SOL-USD oi_divergence_long (long) -- triggered: price_chg_1h=-0.00531, oi_chg_1h=-0.014326, oi_at_entry=302570840.3004
  AVAX-USD oi_divergence_long (long) -- triggered: price_chg_1h=-0.007098, oi_chg_1h=-0.025115, oi_at_entry=11854025.2564

**US -- WHY** (2026-09-10)
- Fired: 17 | Resolved: 10 | Still open: 7

[LOSS] OXY triple_ma_long (long) (-8.145)
  Triggered: EMA(8/16/25) = 61.4042/61.4038/61.3391, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] OXY triple_ma_long (long) (+89.56)
  Triggered: EMA(8/16/25) = 61.4073/61.4057/61.3447, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] DKNG triple_ma_long (long) (-360.6)
  Triggered: EMA(8/16/25) = 23.6065/23.5514/23.5512, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] DKNG triple_ma_long (long) (-125.7)
  Triggered: EMA(8/16/25) = 23.6039/23.555/23.5537, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] T triple_ma_long (long) (-223.4)
  Triggered: EMA(8/16/25) = 25.3825/25.2928/25.2842, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] T triple_ma_long (long) (-437.6)
  Triggered: EMA(8/16/25) = 25.445/25.3361/25.3131, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] T triple_ma_long (long) (-461.2)
  Triggered: EMA(8/16/25) = 25.4406/25.3337/25.3115, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] T triple_ma_long (long) (-675.9)
  Triggered: EMA(8/16/25) = 25.4383/25.3326/25.3107, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] OXY triple_ma_long (long) (-122.2)
  Triggered: EMA(8/16/25) = 61.2318/61.1727/61.1705, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] OXY triple_ma_long (long) (-358.5)
  Triggered: EMA(8/16/25) = 61.2422/61.1839/61.1756, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

Still open (too soon to say why it worked or not):
  DKNG triple_ma_long (long) -- triggered: EMA(8/16/25) = 23.6322/23.5754/23.5679, freshly aligned
  VZ triple_ma_long (long) -- triggered: EMA(8/16/25) = 50.125/49.9352/49.8769, freshly aligned
  MO triple_ma_long (long) -- triggered: EMA(8/16/25) = 68.4601/68.1964/68.0943, freshly aligned
  MO triple_ma_long (long) -- triggered: EMA(8/16/25) = 68.4468/68.1893/68.0896, freshly aligned
  VZ triple_ma_long (long) -- triggered: EMA(8/16/25) = 50.1172/49.9311/49.8742, freshly aligned
  MO triple_ma_long (long) -- triggered: EMA(8/16/25) = 68.4734/68.2034/68.0989, freshly aligned
  F triple_ma_long (long) -- triggered: EMA(8/16/25) = 13.8721/13.8383/13.8378, freshly aligned

---

## 2026-09-11 00:11 IST

**INDIA -- WHY** (2026-09-10)
- Fired: 31 | Resolved: 31 | Still open: 0

[LOSS] IRCON.NS triple_threat_long (long) (-3,662)
  Triggered: RSI 35->67 crossed 50, broke 116.9, trend EMA 116
  Outcome:   session ended before stop or target hit -- settled at the day's close (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via eod_settlement; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] IRFC.NS triple_ma_short (short) (+2,633)
  Triggered: EMA(8/16/25) = 81.7427/81.7433/81.7843, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] RVNL.NS triple_ma_short (short) (+756.6)
  Triggered: EMA(8/16/25) = 207.779/207.782/207.825, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] IDEA.NS breakdown_short (short) (-2,027)
  Triggered: broke range low 15.18 on vol 76,439,755 vs avg 43,235,031, trend EMA 15.34; India gate: RSI 8.33 / VWAP 15.37 (rsi<40 and close<=vwap)
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] IRFC.NS triple_ma_short (short) (+3,977)
  Triggered: EMA(8/16/25) = 81.7446/81.7456/81.7803, freshly aligned
  Outcome:   session ended before stop or target hit -- settled at the day's close (win)

[WIN] IRFC.NS triple_ma_short (short) (+2,450)
  Triggered: EMA(8/16/25) = 81.7502/81.7529/81.778, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] INDIANB.NS triple_ma_short (short) (+2,477)
  Triggered: EMA(8/16/25) = 859.249/859.467/859.479, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] IRCON.NS triple_ma_long (long) (-1,808)
  Triggered: EMA(8/16/25) = 116.136/116.081/116.075, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] HINDCOPPER.NS triple_ma_short (short) (+5,869)
  Triggered: EMA(8/16/25) = 535.439/535.756/535.777, freshly aligned
  Outcome:   session ended before stop or target hit -- settled at the day's close (win)

[LOSS] IRCON.NS triple_ma_long (long) (-2,286)
  Triggered: EMA(8/16/25) = 116.102/116.066/116.065, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] IRFC.NS breakdown_short (short) (-739.6)
  Triggered: broke range low 81.2 on vol 242,690 vs avg 238,179, trend EMA 81.43; India gate: RSI 23.9 / VWAP 81.77 (rsi<40 and close<=vwap)
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] BANKINDIA.NS triple_ma_short (short) (-1,244)
  Triggered: EMA(8/16/25) = 141.154/141.307/141.332, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] ONGC.NS triple_ma_short (short) (-1,970)
  Triggered: EMA(8/16/25) = 236.236/236.462/236.469, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] IRCON.NS triple_ma_long (long) (-2,153)
  Triggered: EMA(8/16/25) = 116.092/116.071/116.07, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] GAIL.NS triple_ma_short (short) (+459.8)
  Triggered: EMA(8/16/25) = 174.698/174.879/174.9, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] HINDCOPPER.NS breakdown_short (short) (+1,836)
  Triggered: broke range low 531 on vol 185,585 vs avg 176,049, trend EMA 533.5; India gate: RSI 23.67 / VWAP 537.4 (rsi<40 and close<=vwap)
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] RVNL.NS breakdown_short (short) (+557.6)
  Triggered: broke range low 206.4 on vol 93,305 vs avg 78,482, trend EMA 206.8; India gate: RSI 37.5 / VWAP 208.4 (rsi<40 and close<=vwap)
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] CANBK.NS triple_ma_short (short) (+1,766)
  Triggered: EMA(8/16/25) = 125.004/125.208/125.232, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] IRCON.NS triple_ma_short (short) (+2,848)
  Triggered: EMA(8/16/25) = 116.017/116.032/116.042, freshly aligned
  Outcome:   session ended before stop or target hit -- settled at the day's close (win)

[LOSS] IDFCFIRSTB.NS triple_ma_long (long) (-1,615)
  Triggered: EMA(8/16/25) = 86.6349/86.6345/86.6255, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] RVNL.NS breakdown_short (short) (-1,482)
  Triggered: broke range low 206.1 on vol 99,284 vs avg 73,907, trend EMA 206.5; India gate: RSI 25.0 / VWAP 208.2 (rsi<40 and close<=vwap)
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] GAIL.NS breakdown_short (short) (-144)
  Triggered: broke range low 173.6 on vol 81,884 vs avg 75,912, trend EMA 174.3; India gate: RSI 26.9 / VWAP 175.1 (rsi<40 and close<=vwap)
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] PNB.NS triple_ma_short (short) (-85.81)
  Triggered: EMA(8/16/25) = 116.717/116.889/116.906, freshly aligned
  Outcome:   session ended before stop or target hit -- settled at the day's close (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via eod_settlement; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] IDFCFIRSTB.NS triple_ma_long (long) (-1,095)
  Triggered: EMA(8/16/25) = 86.6407/86.6358/86.6267, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] JSWENERGY.NS triple_threat_long (long) (+46.91)
  Triggered: RSI 48->69 crossed 50, broke 531.9, trend EMA 531.2
  Outcome:   session ended before stop or target hit -- settled at the day's close (win)

[LOSS] ONGC.NS triple_ma_long (long) (-548.7)
  Triggered: EMA(8/16/25) = 236.54/236.536/236.515, freshly aligned
  Outcome:   session ended before stop or target hit -- settled at the day's close (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via eod_settlement; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] IDFCFIRSTB.NS triple_ma_short (short) (-346.6)
  Triggered: EMA(8/16/25) = 86.5972/86.6109/86.613, freshly aligned
  Outcome:   session ended before stop or target hit -- settled at the day's close (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via eod_settlement; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] ONGC.NS triple_ma_long (long) (-21.12)
  Triggered: EMA(8/16/25) = 236.531/236.52/236.51, freshly aligned
  Outcome:   session ended before stop or target hit -- settled at the day's close (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via eod_settlement; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] RVNL.NS breakdown_short (short) (-1,631)
  Triggered: broke range low 205.7 on vol 382,138 vs avg 111,590, trend EMA 206.2; India gate: RSI 30.06 / VWAP 207.8 (rsi<40 and close<=vwap)
  Outcome:   session ended before stop or target hit -- settled at the day's close (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via eod_settlement; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] JSWENERGY.NS triple_ma_short (short) (-2,594)
  Triggered: EMA(8/16/25) = 530.794/530.836/531, freshly aligned
  Outcome:   session ended before stop or target hit -- settled at the day's close (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via eod_settlement; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] IRFC.NS breakdown_short (short) (-493.8)
  Triggered: broke range low 81.05 on vol 1,091,657 vs avg 196,866, trend EMA 81.17; India gate: RSI 7.46 / VWAP 81.57 (rsi<40 and close<=vwap)
  Outcome:   session ended before stop or target hit -- settled at the day's close (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via eod_settlement; the market simply moved the other way this time (normal strategy variance, not a bug)

**CRYPTO -- WHY** (2026-09-10)
- Fired: 47 | Resolved: 45 | Still open: 2

[WIN] SOL-USD triple_ma_short (short) (+67.99)
  Triggered: EMA(8/16/25) = 103.458/103.476/103.548, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] NEAR-USD oi_divergence_long (long) (-212.4)
  Triggered: price_chg_1h=-0.014136, oi_chg_1h=-0.014548, oi_at_entry=37668208.702
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [STOP OVERSHOOT] intended risk 0.03419/unit, actual loss 0.0726/unit (2.1x) -- price moved past the stop faster than the bot's bar-close check could exit; a violent move against the position, amplified by simulation lag rather than a bad entry call

[LOSS] SOL-USD oi_divergence_long (long) (-133.2)
  Triggered: price_chg_1h=-0.00839, oi_chg_1h=-0.012024, oi_at_entry=319586550.9406
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] AVAX-USD oi_divergence_long (long) (-105.7)
  Triggered: price_chg_1h=-0.00693, oi_chg_1h=-0.010775, oi_at_entry=12854248.8109
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] FET-USD oi_divergence_long (long) (-134.2)
  Triggered: price_chg_1h=-0.012189, oi_chg_1h=-0.044007, oi_at_entry=640203.921
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] XRP-USD oi_divergence_long (long) (-94.28)
  Triggered: price_chg_1h=-0.011526, oi_chg_1h=-0.018462, oi_at_entry=123504124.9471
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] NEAR-USD triple_ma_short (short) (+56.01)
  Triggered: EMA(8/16/25) = 2.54833/2.56846/2.57011, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] FET-USD oi_divergence_long (long) (-135.2)
  Triggered: price_chg_1h=-0.012195, oi_chg_1h=-0.032636, oi_at_entry=635846.096
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] FET-USD oi_divergence_long (long) (+0)
  Triggered: price_chg_1h=-0.010923, oi_chg_1h=-0.016818, oi_at_entry=626713.474
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] NEAR-USD oi_divergence_long (long) (-2.922)
  Triggered: price_chg_1h=-0.019393, oi_chg_1h=-0.016179, oi_at_entry=35465967.549
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] XRP-USD oi_divergence_long (long) (-76.8)
  Triggered: price_chg_1h=-0.005131, oi_chg_1h=-0.019663, oi_at_entry=121490104.3581
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] AVAX-USD oi_divergence_long (long) (-113.2)
  Triggered: price_chg_1h=-0.006607, oi_chg_1h=-0.011577, oi_at_entry=12550660.2516
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] FET-USD oi_divergence_long (long) (-124.4)
  Triggered: price_chg_1h=-0.009915, oi_chg_1h=-0.076035, oi_at_entry=577656.099
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] SOL-USD oi_divergence_long (long) (+44.17)
  Triggered: price_chg_1h=-0.012206, oi_chg_1h=-0.010203, oi_at_entry=317495428.2302
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] AVAX-USD oi_divergence_long (long) (-70.52)
  Triggered: price_chg_1h=-0.012005, oi_chg_1h=-0.010477, oi_at_entry=12452360.325
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] NEAR-USD oi_divergence_long (long) (-4.648)
  Triggered: price_chg_1h=-0.005791, oi_chg_1h=-0.010966, oi_at_entry=35094922.1
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] FET-USD oi_divergence_long (long) (+0)
  Triggered: price_chg_1h=-0.007325, oi_chg_1h=-0.013974, oi_at_entry=606315.336
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] XRP-USD triple_ma_short (short) (-14.3)
  Triggered: EMA(8/16/25) = 1.39007/1.39009/1.39167, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] NEAR-USD oi_divergence_long (long) (-133.1)
  Triggered: price_chg_1h=-0.005934, oi_chg_1h=-0.012271, oi_at_entry=36075370.149
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] SOL-USD triple_ma_long (long) (-41.47)
  Triggered: EMA(8/16/25) = 101.92/101.781/101.779, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] NEAR-USD oi_divergence_long (long) (-118)
  Triggered: price_chg_1h=-0.008215, oi_chg_1h=-0.010893, oi_at_entry=35883719.706
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] XRP-USD triple_ma_short (short) (+14.47)
  Triggered: EMA(8/16/25) = 1.38922/1.38964/1.39079, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] NEAR-USD oi_divergence_long (long) (+4.528)
  Triggered: price_chg_1h=-0.021121, oi_chg_1h=-0.023766, oi_at_entry=35186324.512
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (win)

[WIN] NEAR-USD triple_ma_short (short) (+81.95)
  Triggered: EMA(8/16/25) = 2.48493/2.49082/2.49276, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] FET-USD triple_ma_short (short) (-47.33)
  Triggered: EMA(8/16/25) = 0.169948/0.169993/0.170097, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] BTC-USD triple_ma_long (long) (-37.54)
  Triggered: EMA(8/16/25) = 78,319.6/78,312.1/78,304.3, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] SOL-USD triple_ma_short (short) (+29.59)
  Triggered: EMA(8/16/25) = 101.781/101.786/101.792, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] BTC-USD triple_ma_short (short) (+19.43)
  Triggered: EMA(8/16/25) = 78,225.7/78,262.1/78,273.2, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] AVAX-USD oi_divergence_long (long) (-79.25)
  Triggered: price_chg_1h=-0.007921, oi_chg_1h=-0.01347, oi_at_entry=12451701.3456
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] FET-USD oi_divergence_long (long) (+0)
  Triggered: price_chg_1h=-0.012015, oi_chg_1h=-0.01268, oi_at_entry=616812.789
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] AVAX-USD triple_ma_short (short) (-42.11)
  Triggered: EMA(8/16/25) = 7.79739/7.80732/7.80937, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] NEAR-USD oi_divergence_long (long) (+34.84)
  Triggered: price_chg_1h=-0.027109, oi_chg_1h=-0.022072, oi_at_entry=34857430.837
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (win)

[LOSS] ETH-USD triple_ma_short (short) (-38.28)
  Triggered: EMA(8/16/25) = 2,471.91/2,472.7/2,472.7, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] NEAR-USD oi_divergence_long (long) (-80.61)
  Triggered: price_chg_1h=-0.008383, oi_chg_1h=-0.011915, oi_at_entry=34656845.127
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] FET-USD oi_divergence_long (long) (-161.9)
  Triggered: price_chg_1h=-0.008352, oi_chg_1h=-0.036036, oi_at_entry=599213.827
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [STOP OVERSHOOT] intended risk 0.00113/unit, actual loss 0.00183/unit (1.6x) -- price moved past the stop faster than the bot's bar-close check could exit; a violent move against the position, amplified by simulation lag rather than a bad entry call

[WIN] ETH-USD triple_ma_short (short) (+2.06)
  Triggered: EMA(8/16/25) = 2,471.66/2,472.28/2,472.4, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] AVAX-USD oi_divergence_long (long) (+8.502)
  Triggered: price_chg_1h=-0.005791, oi_chg_1h=-0.011954, oi_at_entry=12319637.2032
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (win)

[LOSS] FET-USD oi_divergence_long (long) (+0)
  Triggered: price_chg_1h=-0.008026, oi_chg_1h=-0.012591, oi_at_entry=590636.111
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] SOL-USD oi_divergence_long (long) (-96.41)
  Triggered: price_chg_1h=-0.012632, oi_chg_1h=-0.036499, oi_at_entry=302981689.2709
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] XRP-USD oi_divergence_long (long) (-79.89)
  Triggered: price_chg_1h=-0.00819, oi_chg_1h=-0.041026, oi_at_entry=118727844.986
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] AVAX-USD oi_divergence_long (long) (-113)
  Triggered: price_chg_1h=-0.012252, oi_chg_1h=-0.011603, oi_at_entry=12228730.8065
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] NEAR-USD oi_divergence_long (long) (-2.847)
  Triggered: price_chg_1h=-0.006651, oi_chg_1h=-0.01327, oi_at_entry=35021453.355
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] FET-USD oi_divergence_long (long) (+0)
  Triggered: price_chg_1h=-0.010712, oi_chg_1h=-0.05467, oi_at_entry=637519.036
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] NEAR-USD triple_ma_short (short) (-63.91)
  Triggered: EMA(8/16/25) = 2.41559/2.41651/2.42034, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] FET-USD oi_divergence_long (long) (+69.49)
  Triggered: price_chg_1h=-0.011538, oi_chg_1h=-0.041651, oi_at_entry=633370.18
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (win)

Still open (too soon to say why it worked or not):
  SOL-USD oi_divergence_long (long) -- triggered: price_chg_1h=-0.00531, oi_chg_1h=-0.014326, oi_at_entry=302570840.3004
  AVAX-USD oi_divergence_long (long) -- triggered: price_chg_1h=-0.007098, oi_chg_1h=-0.025115, oi_at_entry=11854025.2564

**US -- WHY** (2026-09-10)
- Fired: 17 | Resolved: 10 | Still open: 7

[LOSS] OXY triple_ma_long (long) (-8.145)
  Triggered: EMA(8/16/25) = 61.4042/61.4038/61.3391, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] OXY triple_ma_long (long) (+89.56)
  Triggered: EMA(8/16/25) = 61.4073/61.4057/61.3447, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] DKNG triple_ma_long (long) (-360.6)
  Triggered: EMA(8/16/25) = 23.6065/23.5514/23.5512, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] DKNG triple_ma_long (long) (-125.7)
  Triggered: EMA(8/16/25) = 23.6039/23.555/23.5537, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] T triple_ma_long (long) (-223.4)
  Triggered: EMA(8/16/25) = 25.3825/25.2928/25.2842, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] T triple_ma_long (long) (-437.6)
  Triggered: EMA(8/16/25) = 25.445/25.3361/25.3131, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] T triple_ma_long (long) (-461.2)
  Triggered: EMA(8/16/25) = 25.4406/25.3337/25.3115, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] T triple_ma_long (long) (-675.9)
  Triggered: EMA(8/16/25) = 25.4383/25.3326/25.3107, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] OXY triple_ma_long (long) (-122.2)
  Triggered: EMA(8/16/25) = 61.2318/61.1727/61.1705, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] OXY triple_ma_long (long) (-358.5)
  Triggered: EMA(8/16/25) = 61.2422/61.1839/61.1756, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

Still open (too soon to say why it worked or not):
  DKNG triple_ma_long (long) -- triggered: EMA(8/16/25) = 23.6322/23.5754/23.5679, freshly aligned
  VZ triple_ma_long (long) -- triggered: EMA(8/16/25) = 50.125/49.9352/49.8769, freshly aligned
  MO triple_ma_long (long) -- triggered: EMA(8/16/25) = 68.4601/68.1964/68.0943, freshly aligned
  MO triple_ma_long (long) -- triggered: EMA(8/16/25) = 68.4468/68.1893/68.0896, freshly aligned
  VZ triple_ma_long (long) -- triggered: EMA(8/16/25) = 50.1172/49.9311/49.8742, freshly aligned
  MO triple_ma_long (long) -- triggered: EMA(8/16/25) = 68.4734/68.2034/68.0989, freshly aligned
  F triple_ma_long (long) -- triggered: EMA(8/16/25) = 13.8721/13.8383/13.8378, freshly aligned

---

## 2026-09-12 00:00 IST

**INDIA -- WHY** (2026-09-11)
- Fired: 12 | Resolved: 12 | Still open: 0

[LOSS] IRCON.NS breakdown_short (short) (-104.4)
  Triggered: broke range low 115 on vol 79,916 vs avg 57,241, trend EMA 115.1; India gate: RSI 9.62 / VWAP 113.7 (rsi<40 and close<=vwap)
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] HINDCOPPER.NS breakdown_short (short) (-5,393)
  Triggered: broke range low 526 on vol 757,856 vs avg 257,271, trend EMA 525.7; India gate: RSI 8.8 / VWAP 508.9 (rsi<40 and close<=vwap)
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] IDFCFIRSTB.NS breakdown_short (short) (-1,517)
  Triggered: broke range low 85.9 on vol 576,314 vs avg 555,988, trend EMA 86.46; India gate: RSI 27.53 / VWAP 85.76 (rsi<40 and close<=vwap)
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] BANKINDIA.NS breakdown_short (short) (-4,698)
  Triggered: broke range low 140.3 on vol 408,452 vs avg 185,132, trend EMA 140.4; India gate: RSI 18.34 / VWAP 138.5 (rsi<40 and close<=vwap)
  Outcome:   session ended before stop or target hit -- settled at the day's close (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via eod_settlement; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] IDEA.NS triple_ma_short (short) (-1,806)
  Triggered: EMA(8/16/25) = 15.0258/15.0262/15.0464, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] IDEA.NS triple_ma_short (short) (-2,305)
  Triggered: EMA(8/16/25) = 15.0295/15.0296/15.0446, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] BHEL.NS triple_ma_long (long) (+977.9)
  Triggered: EMA(8/16/25) = 428.736/428.086/428.081, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] IDEA.NS triple_ma_short (short) (-333.3)
  Triggered: EMA(8/16/25) = 15.032/15.0335/15.0441, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] NATIONALUM.NS triple_ma_short (short) (-689.7)
  Triggered: EMA(8/16/25) = 361.559/361.569/362.909, freshly aligned
  Outcome:   session ended before stop or target hit -- settled at the day's close (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via eod_settlement; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] HUDCO.NS triple_ma_short (short) (-1,014)
  Triggered: EMA(8/16/25) = 172.613/172.615/172.813, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] JSWENERGY.NS triple_ma_short (short) (-1,286)
  Triggered: EMA(8/16/25) = 525.067/525.078/525.65, freshly aligned
  Outcome:   session ended before stop or target hit -- settled at the day's close (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via eod_settlement; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] HUDCO.NS triple_ma_short (short) (+0)
  Triggered: EMA(8/16/25) = 172.566/172.588/172.78, freshly aligned
  Outcome:   session ended before stop or target hit -- settled at the day's close (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via eod_settlement; the market simply moved the other way this time (normal strategy variance, not a bug)

**CRYPTO -- WHY** (2026-09-11)
- Fired: 54 | Resolved: 52 | Still open: 2

[WIN] XRP-USD oi_divergence_long (long) (+52.97)
  Triggered: price_chg_1h=-0.006255, oi_chg_1h=-0.011394, oi_at_entry=119885317.547
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (win)

[LOSS] SOL-USD triple_ma_short (short) (-34.72)
  Triggered: EMA(8/16/25) = 99.7578/99.7599/99.8493, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] AVAX-USD triple_ma_short (short) (-20.41)
  Triggered: EMA(8/16/25) = 7.60339/7.60384/7.6129, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] FET-USD oi_divergence_long (long) (+0)
  Triggered: price_chg_1h=-0.005509, oi_chg_1h=-0.011033, oi_at_entry=594854.177
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] AVAX-USD triple_ma_short (short) (+32.26)
  Triggered: EMA(8/16/25) = 7.60535/7.60542/7.6112, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] BTC-USD triple_ma_short (short) (+23.69)
  Triggered: EMA(8/16/25) = 77,182.6/77,189.2/77,214.5, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] SOL-USD oi_divergence_long (long) (-145.9)
  Triggered: price_chg_1h=-0.005408, oi_chg_1h=-0.0103, oi_at_entry=302649956.1323
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] FET-USD oi_divergence_long (long) (+0)
  Triggered: price_chg_1h=-0.006695, oi_chg_1h=-0.018807, oi_at_entry=598243.772
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] SOL-USD triple_ma_short (short) (+26.7)
  Triggered: EMA(8/16/25) = 99.7664/99.8158/99.8571, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] XRP-USD oi_divergence_long (long) (-248.1)
  Triggered: price_chg_1h=-0.005175, oi_chg_1h=-0.010404, oi_at_entry=120903082.5617
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [STOP OVERSHOOT] intended risk 0.005886/unit, actual loss 0.0146/unit (2.5x) -- price moved past the stop faster than the bot's bar-close check could exit; a violent move against the position, amplified by simulation lag rather than a bad entry call

[WIN] ETH-USD triple_ma_short (short) (+8.954)
  Triggered: EMA(8/16/25) = 2,453.3/2,455.93/2,456.03, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] AVAX-USD oi_divergence_long (long) (-299.5)
  Triggered: price_chg_1h=-0.007267, oi_chg_1h=-0.013176, oi_at_entry=11676642.6512
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [STOP OVERSHOOT] intended risk 0.02871/unit, actual loss 0.086/unit (3.0x) -- price moved past the stop faster than the bot's bar-close check could exit; a violent move against the position, amplified by simulation lag rather than a bad entry call

[LOSS] NEAR-USD oi_divergence_long (long) (-64.33)
  Triggered: price_chg_1h=-0.012415, oi_chg_1h=-0.01011, oi_at_entry=37237220.692
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] FET-USD triple_ma_short (short) (+22.69)
  Triggered: EMA(8/16/25) = 0.164448/0.164632/0.164635, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] XRP-USD oi_divergence_long (long) (+127.4)
  Triggered: price_chg_1h=-0.006109, oi_chg_1h=-0.012891, oi_at_entry=117693188.7851
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (win)

[LOSS] NEAR-USD triple_ma_short (short) (-31.42)
  Triggered: EMA(8/16/25) = 2.47847/2.48461/2.48477, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] NEAR-USD oi_divergence_long (long) (-132.8)
  Triggered: price_chg_1h=-0.014324, oi_chg_1h=-0.015246, oi_at_entry=36616886.21
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] NEAR-USD triple_ma_short (short) (+17.88)
  Triggered: EMA(8/16/25) = 2.47656/2.48243/2.48347, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] ETH-USD triple_ma_short (short) (-64.25)
  Triggered: EMA(8/16/25) = 2,450.39/2,450.7/2,451.36, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] NEAR-USD oi_divergence_long (long) (-12.39)
  Triggered: price_chg_1h=-0.008715, oi_chg_1h=-0.015755, oi_at_entry=35885630.407
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] BTC-USD triple_ma_long (long) (+45.47)
  Triggered: EMA(8/16/25) = 76,987.4/76,937.2/76,935.1, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] ETH-USD triple_ma_long (long) (-2.349)
  Triggered: EMA(8/16/25) = 2,453.14/2,451.48/2,451.22, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] XRP-USD triple_ma_long (long) (+12.71)
  Triggered: EMA(8/16/25) = 1.34699/1.34559/1.34544, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] FET-USD oi_divergence_long (long) (-11.08)
  Triggered: price_chg_1h=-0.009541, oi_chg_1h=-0.020561, oi_at_entry=593696.388
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] NEAR-USD oi_divergence_long (long) (-13.74)
  Triggered: price_chg_1h=-0.011138, oi_chg_1h=-0.017224, oi_at_entry=36357572.108
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] AVAX-USD triple_ma_short (short) (-49.06)
  Triggered: EMA(8/16/25) = 7.49902/7.50129/7.50131, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] FET-USD triple_ma_short (short) (+50.42)
  Triggered: EMA(8/16/25) = 0.165261/0.165613/0.165639, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] NEAR-USD oi_divergence_long (long) (+23.92)
  Triggered: price_chg_1h=-0.005099, oi_chg_1h=-0.010666, oi_at_entry=36527203.793
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (win)

[LOSS] FET-USD oi_divergence_long (long) (-111.3)
  Triggered: price_chg_1h=-0.005751, oi_chg_1h=-0.016006, oi_at_entry=610465.134
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] AVAX-USD oi_divergence_long (long) (+0)
  Triggered: price_chg_1h=-0.0152, oi_chg_1h=-0.032992, oi_at_entry=11406204.4218
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] XRP-USD triple_ma_short (short) (+144)
  Triggered: EMA(8/16/25) = 1.34683/1.34839/1.3484, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] SOL-USD triple_ma_short (short) (+70.6)
  Triggered: EMA(8/16/25) = 99.5434/99.6082/99.6085, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] BTC-USD triple_ma_short (short) (+44.16)
  Triggered: EMA(8/16/25) = 77,046.9/77,096.8/77,103.4, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] XRP-USD oi_divergence_long (long) (-200.6)
  Triggered: price_chg_1h=-0.006488, oi_chg_1h=-0.012559, oi_at_entry=118131808.2433
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [STOP OVERSHOOT] intended risk 0.004586/unit, actual loss 0.0092/unit (2.0x) -- price moved past the stop faster than the bot's bar-close check could exit; a violent move against the position, amplified by simulation lag rather than a bad entry call

[LOSS] AVAX-USD oi_divergence_long (long) (-158.4)
  Triggered: price_chg_1h=-0.006215, oi_chg_1h=-0.021247, oi_at_entry=11457188.4768
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] NEAR-USD oi_divergence_long (long) (+28.4)
  Triggered: price_chg_1h=-0.021443, oi_chg_1h=-0.016329, oi_at_entry=36521723.291
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (win)

[LOSS] NEAR-USD triple_ma_short (short) (-120.8)
  Triggered: EMA(8/16/25) = 2.45546/2.46017/2.46122, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] ETH-USD triple_ma_short (short) (-45.2)
  Triggered: EMA(8/16/25) = 2,460.39/2,462.8/2,462.88, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] AVAX-USD triple_ma_long (long) (+47.71)
  Triggered: EMA(8/16/25) = 7.48871/7.45847/7.45401, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] NEAR-USD breakout_long (long) (-111.3)
  Triggered: broke range high 2.649 on vol 379,896 vs avg 282,159, trend EMA 2.602, 2-bar + retest
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] XRP-USD oi_divergence_long (long) (-74.33)
  Triggered: price_chg_1h=-0.014554, oi_chg_1h=-0.034268, oi_at_entry=114886063.562
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] SOL-USD oi_divergence_long (long) (-28.12)
  Triggered: price_chg_1h=-0.015163, oi_chg_1h=-0.015589, oi_at_entry=315047050.0995
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] AVAX-USD oi_divergence_long (long) (-84.26)
  Triggered: price_chg_1h=-0.007592, oi_chg_1h=-0.010478, oi_at_entry=12796306.2032
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] SOL-USD oi_divergence_long (long) (+20.51)
  Triggered: price_chg_1h=-0.016365, oi_chg_1h=-0.025427, oi_at_entry=307036423.3397
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (win)

[WIN] XRP-USD oi_divergence_long (long) (+4.463)
  Triggered: price_chg_1h=-0.014841, oi_chg_1h=-0.015589, oi_at_entry=112656400.2687
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (win)

[WIN] AVAX-USD oi_divergence_long (long) (+0.6393)
  Triggered: price_chg_1h=-0.017894, oi_chg_1h=-0.018364, oi_at_entry=12561312.3244
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (win)

[WIN] FET-USD oi_divergence_long (long) (+11.34)
  Triggered: price_chg_1h=-0.019937, oi_chg_1h=-0.066024, oi_at_entry=568981.24
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (win)

[LOSS] NEAR-USD oi_divergence_long (long) (-89.1)
  Triggered: price_chg_1h=-0.011948, oi_chg_1h=-0.031882, oi_at_entry=38783709.452
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] AVAX-USD oi_divergence_long (long) (+23.37)
  Triggered: price_chg_1h=-0.017685, oi_chg_1h=-0.015433, oi_at_entry=12539435.5704
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (win)

[LOSS] XRP-USD oi_divergence_long (long) (-89.84)
  Triggered: price_chg_1h=-0.006611, oi_chg_1h=-0.017863, oi_at_entry=110565619.5305
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] AVAX-USD oi_divergence_long (long) (-101.8)
  Triggered: price_chg_1h=-0.007634, oi_chg_1h=-0.017299, oi_at_entry=12373569.5265
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] NEAR-USD oi_divergence_long (long) (-24.76)
  Triggered: price_chg_1h=-0.010117, oi_chg_1h=-0.024518, oi_at_entry=37153032.755
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

Still open (too soon to say why it worked or not):
  FET-USD oi_divergence_long (long) -- triggered: price_chg_1h=-0.010919, oi_chg_1h=-0.017316, oi_at_entry=580523.82
  SOL-USD oi_divergence_long (long) -- triggered: price_chg_1h=-0.010191, oi_chg_1h=-0.012203, oi_at_entry=304656465.7433

**US -- WHY** (2026-09-11)
- Fired: 40 | Resolved: 31 | Still open: 9

[LOSS] RF triple_ma_long (long) (-959)
  Triggered: EMA(8/16/25) = 29.9194/29.8528/29.8332, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [STOP OVERSHOOT] intended risk 0.1893/unit, actual loss 0.29/unit (1.5x) -- price moved past the stop faster than the bot's bar-close check could exit; a violent move against the position, amplified by simulation lag rather than a bad entry call

[WIN] MARA triple_threat_long (long) (+252.9)
  Triggered: RSI 43->65 crossed 50, broke 11.8, trend EMA 11.67
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] INTC triple_threat_long (long) (+76.36)
  Triggered: RSI 34->74 crossed 50, broke 102.2, trend EMA 102
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] CSCO triple_threat_long (long) (+382.1)
  Triggered: RSI 25->72 crossed 50, broke 109.1, trend EMA 108.6
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] NIO triple_threat_long (long) (+271.5)
  Triggered: RSI 13->71 crossed 50, broke 3.63, trend EMA 3.631
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] MARA triple_ma_long (long) (+238.6)
  Triggered: EMA(8/16/25) = 11.7143/11.6805/11.6797, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] RIVN triple_ma_long (long) (+564)
  Triggered: EMA(8/16/25) = 16.1948/16.1719/16.1642, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] RIVN triple_ma_long (long) (-1,067)
  Triggered: EMA(8/16/25) = 16.3918/16.2844/16.2392, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] SNAP triple_ma_long (long) (+281.3)
  Triggered: EMA(8/16/25) = 5.52798/5.47952/5.45236, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] CSCO triple_ma_long (long) (+1,071)
  Triggered: EMA(8/16/25) = 109.131/108.807/108.77, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] AAL triple_ma_long (long) (+243.6)
  Triggered: EMA(8/16/25) = 12.967/12.9178/12.903, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] T triple_ma_long (long) (+395.2)
  Triggered: EMA(8/16/25) = 25.7828/25.6813/25.615, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] NEM triple_ma_long (long) (-471.6)
  Triggered: EMA(8/16/25) = 127.444/127.099/127.09, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] DAL triple_ma_long (long) (+283.3)
  Triggered: EMA(8/16/25) = 78.8981/78.6198/78.5512, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] MARA triple_ma_long (long) (-557)
  Triggered: EMA(8/16/25) = 11.8955/11.7838/11.7487, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] RIVN triple_ma_long (long) (-1,140)
  Triggered: EMA(8/16/25) = 16.3707/16.2732/16.2319, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] CSCO triple_ma_long (long) (+1,127)
  Triggered: EMA(8/16/25) = 109.117/108.8/108.765, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] AAL triple_ma_long (long) (+502.7)
  Triggered: EMA(8/16/25) = 12.9581/12.9131/12.9, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] DAL triple_ma_long (long) (+238.6)
  Triggered: EMA(8/16/25) = 78.8992/78.6204/78.5516, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] SNAP triple_ma_long (long) (+466.5)
  Triggered: EMA(8/16/25) = 5.53955/5.49129/5.46204, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] T triple_ma_long (long) (+296.2)
  Triggered: EMA(8/16/25) = 25.7884/25.6843/25.6169, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] SIRI triple_ma_long (long) (+486.8)
  Triggered: EMA(8/16/25) = 29.044/28.9604/28.9155, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] NEM triple_ma_long (long) (-315.7)
  Triggered: EMA(8/16/25) = 127.413/127.083/127.079, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] GOLD triple_ma_long (long) (-394.3)
  Triggered: EMA(8/16/25) = 47.4189/46.7474/46.6598, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] CCL triple_ma_long (long) (+430.8)
  Triggered: EMA(8/16/25) = 22.6705/22.5881/22.5812, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] NEM triple_ma_long (long) (-564.4)
  Triggered: EMA(8/16/25) = 127.495/127.16/127.128, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] RIOT triple_ma_long (long) (-486.2)
  Triggered: EMA(8/16/25) = 21.5147/21.4131/21.4124, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] INTC triple_ma_long (long) (-991.2)
  Triggered: EMA(8/16/25) = 102.991/102.445/102.384, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] NCLH triple_ma_long (long) (+261)
  Triggered: EMA(8/16/25) = 14.7325/14.6719/14.6699, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] RIOT triple_ma_long (long) (+363.1)
  Triggered: EMA(8/16/25) = 21.5403/21.4472/21.4348, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] INTC triple_ma_long (long) (+202)
  Triggered: EMA(8/16/25) = 102.679/102.672/102.608, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

Still open (too soon to say why it worked or not):
  SNAP triple_ma_long (long) -- triggered: EMA(8/16/25) = 5.50922/5.46472/5.44093, freshly aligned
  HBAN triple_ma_long (long) -- triggered: EMA(8/16/25) = 16.7077/16.6605/16.6421, freshly aligned
  WFC triple_ma_long (long) -- triggered: EMA(8/16/25) = 89.4557/89.2323/89.1805, freshly aligned
  PYPL triple_ma_long (long) -- triggered: EMA(8/16/25) = 53.2392/53.1303/53.0506, freshly aligned
  MARA triple_ma_long (long) -- triggered: EMA(8/16/25) = 11.8778/11.7743/11.7425, freshly aligned
  NIO triple_ma_long (long) -- triggered: EMA(8/16/25) = 3.65845/3.63963/3.63938, freshly aligned
  WFC triple_ma_long (long) -- triggered: EMA(8/16/25) = 89.5466/89.3009/89.2258, freshly aligned
  C triple_ma_long (long) -- triggered: EMA(8/16/25) = 139.067/138.575/138.335, freshly aligned
  NIO triple_ma_long (long) -- triggered: EMA(8/16/25) = 3.66067/3.6408/3.64015, freshly aligned

**INDIA FUTURES (MANUAL) -- WHY** (2026-09-11)
- Fired: 4 | Resolved: 4 | Still open: 0

[WIN] BANKNIFTY-FUT triple_ma_long (long) (+672.8)
  Triggered: EMA(8/16/25) = 56,347.3/56,278/56,267.5, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] NIFTY-FUT triple_ma_long (long) (-94.91)
  Triggered: EMA(8/16/25) = 23,392.1/23,373.2/23,373, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] NIFTY-FUT triple_ma_long (long) (-526.2)
  Triggered: EMA(8/16/25) = 23,398.3/23,378.6/23,376.5, freshly aligned
  Outcome:   session ended before stop or target hit -- settled at the day's close (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via eod_settlement; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] SENSEX-FUT triple_ma_long (long) (-267.7)
  Triggered: EMA(8/16/25) = 74,694.7/74,628.9/74,622.4, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

---

## 2026-09-12 00:11 IST

**INDIA -- WHY** (2026-09-11)
- Fired: 12 | Resolved: 12 | Still open: 0

[LOSS] IRCON.NS breakdown_short (short) (-104.4)
  Triggered: broke range low 115 on vol 79,916 vs avg 57,241, trend EMA 115.1; India gate: RSI 9.62 / VWAP 113.7 (rsi<40 and close<=vwap)
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] HINDCOPPER.NS breakdown_short (short) (-5,393)
  Triggered: broke range low 526 on vol 757,856 vs avg 257,271, trend EMA 525.7; India gate: RSI 8.8 / VWAP 508.9 (rsi<40 and close<=vwap)
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] IDFCFIRSTB.NS breakdown_short (short) (-1,517)
  Triggered: broke range low 85.9 on vol 576,314 vs avg 555,988, trend EMA 86.46; India gate: RSI 27.53 / VWAP 85.76 (rsi<40 and close<=vwap)
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] BANKINDIA.NS breakdown_short (short) (-4,698)
  Triggered: broke range low 140.3 on vol 408,452 vs avg 185,132, trend EMA 140.4; India gate: RSI 18.34 / VWAP 138.5 (rsi<40 and close<=vwap)
  Outcome:   session ended before stop or target hit -- settled at the day's close (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via eod_settlement; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] IDEA.NS triple_ma_short (short) (-1,806)
  Triggered: EMA(8/16/25) = 15.0258/15.0262/15.0464, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] IDEA.NS triple_ma_short (short) (-2,305)
  Triggered: EMA(8/16/25) = 15.0295/15.0296/15.0446, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] BHEL.NS triple_ma_long (long) (+977.9)
  Triggered: EMA(8/16/25) = 428.736/428.086/428.081, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] IDEA.NS triple_ma_short (short) (-333.3)
  Triggered: EMA(8/16/25) = 15.032/15.0335/15.0441, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] NATIONALUM.NS triple_ma_short (short) (-689.7)
  Triggered: EMA(8/16/25) = 361.559/361.569/362.909, freshly aligned
  Outcome:   session ended before stop or target hit -- settled at the day's close (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via eod_settlement; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] HUDCO.NS triple_ma_short (short) (-1,014)
  Triggered: EMA(8/16/25) = 172.613/172.615/172.813, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] JSWENERGY.NS triple_ma_short (short) (-1,286)
  Triggered: EMA(8/16/25) = 525.067/525.078/525.65, freshly aligned
  Outcome:   session ended before stop or target hit -- settled at the day's close (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via eod_settlement; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] HUDCO.NS triple_ma_short (short) (+0)
  Triggered: EMA(8/16/25) = 172.566/172.588/172.78, freshly aligned
  Outcome:   session ended before stop or target hit -- settled at the day's close (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via eod_settlement; the market simply moved the other way this time (normal strategy variance, not a bug)

**CRYPTO -- WHY** (2026-09-11)
- Fired: 54 | Resolved: 52 | Still open: 2

[WIN] XRP-USD oi_divergence_long (long) (+52.97)
  Triggered: price_chg_1h=-0.006255, oi_chg_1h=-0.011394, oi_at_entry=119885317.547
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (win)

[LOSS] SOL-USD triple_ma_short (short) (-34.72)
  Triggered: EMA(8/16/25) = 99.7578/99.7599/99.8493, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] AVAX-USD triple_ma_short (short) (-20.41)
  Triggered: EMA(8/16/25) = 7.60339/7.60384/7.6129, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] FET-USD oi_divergence_long (long) (+0)
  Triggered: price_chg_1h=-0.005509, oi_chg_1h=-0.011033, oi_at_entry=594854.177
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] AVAX-USD triple_ma_short (short) (+32.26)
  Triggered: EMA(8/16/25) = 7.60535/7.60542/7.6112, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] BTC-USD triple_ma_short (short) (+23.69)
  Triggered: EMA(8/16/25) = 77,182.6/77,189.2/77,214.5, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] SOL-USD oi_divergence_long (long) (-145.9)
  Triggered: price_chg_1h=-0.005408, oi_chg_1h=-0.0103, oi_at_entry=302649956.1323
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] FET-USD oi_divergence_long (long) (+0)
  Triggered: price_chg_1h=-0.006695, oi_chg_1h=-0.018807, oi_at_entry=598243.772
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] SOL-USD triple_ma_short (short) (+26.7)
  Triggered: EMA(8/16/25) = 99.7664/99.8158/99.8571, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] XRP-USD oi_divergence_long (long) (-248.1)
  Triggered: price_chg_1h=-0.005175, oi_chg_1h=-0.010404, oi_at_entry=120903082.5617
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [STOP OVERSHOOT] intended risk 0.005886/unit, actual loss 0.0146/unit (2.5x) -- price moved past the stop faster than the bot's bar-close check could exit; a violent move against the position, amplified by simulation lag rather than a bad entry call

[WIN] ETH-USD triple_ma_short (short) (+8.954)
  Triggered: EMA(8/16/25) = 2,453.3/2,455.93/2,456.03, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] AVAX-USD oi_divergence_long (long) (-299.5)
  Triggered: price_chg_1h=-0.007267, oi_chg_1h=-0.013176, oi_at_entry=11676642.6512
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [STOP OVERSHOOT] intended risk 0.02871/unit, actual loss 0.086/unit (3.0x) -- price moved past the stop faster than the bot's bar-close check could exit; a violent move against the position, amplified by simulation lag rather than a bad entry call

[LOSS] NEAR-USD oi_divergence_long (long) (-64.33)
  Triggered: price_chg_1h=-0.012415, oi_chg_1h=-0.01011, oi_at_entry=37237220.692
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] FET-USD triple_ma_short (short) (+22.69)
  Triggered: EMA(8/16/25) = 0.164448/0.164632/0.164635, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] XRP-USD oi_divergence_long (long) (+127.4)
  Triggered: price_chg_1h=-0.006109, oi_chg_1h=-0.012891, oi_at_entry=117693188.7851
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (win)

[LOSS] NEAR-USD triple_ma_short (short) (-31.42)
  Triggered: EMA(8/16/25) = 2.47847/2.48461/2.48477, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] NEAR-USD oi_divergence_long (long) (-132.8)
  Triggered: price_chg_1h=-0.014324, oi_chg_1h=-0.015246, oi_at_entry=36616886.21
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] NEAR-USD triple_ma_short (short) (+17.88)
  Triggered: EMA(8/16/25) = 2.47656/2.48243/2.48347, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] ETH-USD triple_ma_short (short) (-64.25)
  Triggered: EMA(8/16/25) = 2,450.39/2,450.7/2,451.36, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] NEAR-USD oi_divergence_long (long) (-12.39)
  Triggered: price_chg_1h=-0.008715, oi_chg_1h=-0.015755, oi_at_entry=35885630.407
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] BTC-USD triple_ma_long (long) (+45.47)
  Triggered: EMA(8/16/25) = 76,987.4/76,937.2/76,935.1, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] ETH-USD triple_ma_long (long) (-2.349)
  Triggered: EMA(8/16/25) = 2,453.14/2,451.48/2,451.22, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] XRP-USD triple_ma_long (long) (+12.71)
  Triggered: EMA(8/16/25) = 1.34699/1.34559/1.34544, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] FET-USD oi_divergence_long (long) (-11.08)
  Triggered: price_chg_1h=-0.009541, oi_chg_1h=-0.020561, oi_at_entry=593696.388
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] NEAR-USD oi_divergence_long (long) (-13.74)
  Triggered: price_chg_1h=-0.011138, oi_chg_1h=-0.017224, oi_at_entry=36357572.108
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] AVAX-USD triple_ma_short (short) (-49.06)
  Triggered: EMA(8/16/25) = 7.49902/7.50129/7.50131, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] FET-USD triple_ma_short (short) (+50.42)
  Triggered: EMA(8/16/25) = 0.165261/0.165613/0.165639, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] NEAR-USD oi_divergence_long (long) (+23.92)
  Triggered: price_chg_1h=-0.005099, oi_chg_1h=-0.010666, oi_at_entry=36527203.793
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (win)

[LOSS] FET-USD oi_divergence_long (long) (-111.3)
  Triggered: price_chg_1h=-0.005751, oi_chg_1h=-0.016006, oi_at_entry=610465.134
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] AVAX-USD oi_divergence_long (long) (+0)
  Triggered: price_chg_1h=-0.0152, oi_chg_1h=-0.032992, oi_at_entry=11406204.4218
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] XRP-USD triple_ma_short (short) (+144)
  Triggered: EMA(8/16/25) = 1.34683/1.34839/1.3484, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] SOL-USD triple_ma_short (short) (+70.6)
  Triggered: EMA(8/16/25) = 99.5434/99.6082/99.6085, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] BTC-USD triple_ma_short (short) (+44.16)
  Triggered: EMA(8/16/25) = 77,046.9/77,096.8/77,103.4, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] XRP-USD oi_divergence_long (long) (-200.6)
  Triggered: price_chg_1h=-0.006488, oi_chg_1h=-0.012559, oi_at_entry=118131808.2433
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [STOP OVERSHOOT] intended risk 0.004586/unit, actual loss 0.0092/unit (2.0x) -- price moved past the stop faster than the bot's bar-close check could exit; a violent move against the position, amplified by simulation lag rather than a bad entry call

[LOSS] AVAX-USD oi_divergence_long (long) (-158.4)
  Triggered: price_chg_1h=-0.006215, oi_chg_1h=-0.021247, oi_at_entry=11457188.4768
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] NEAR-USD oi_divergence_long (long) (+28.4)
  Triggered: price_chg_1h=-0.021443, oi_chg_1h=-0.016329, oi_at_entry=36521723.291
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (win)

[LOSS] NEAR-USD triple_ma_short (short) (-120.8)
  Triggered: EMA(8/16/25) = 2.45546/2.46017/2.46122, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] ETH-USD triple_ma_short (short) (-45.2)
  Triggered: EMA(8/16/25) = 2,460.39/2,462.8/2,462.88, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] AVAX-USD triple_ma_long (long) (+47.71)
  Triggered: EMA(8/16/25) = 7.48871/7.45847/7.45401, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] NEAR-USD breakout_long (long) (-111.3)
  Triggered: broke range high 2.649 on vol 379,896 vs avg 282,159, trend EMA 2.602, 2-bar + retest
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] XRP-USD oi_divergence_long (long) (-74.33)
  Triggered: price_chg_1h=-0.014554, oi_chg_1h=-0.034268, oi_at_entry=114886063.562
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] SOL-USD oi_divergence_long (long) (-28.12)
  Triggered: price_chg_1h=-0.015163, oi_chg_1h=-0.015589, oi_at_entry=315047050.0995
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] AVAX-USD oi_divergence_long (long) (-84.26)
  Triggered: price_chg_1h=-0.007592, oi_chg_1h=-0.010478, oi_at_entry=12796306.2032
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] SOL-USD oi_divergence_long (long) (+20.51)
  Triggered: price_chg_1h=-0.016365, oi_chg_1h=-0.025427, oi_at_entry=307036423.3397
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (win)

[WIN] XRP-USD oi_divergence_long (long) (+4.463)
  Triggered: price_chg_1h=-0.014841, oi_chg_1h=-0.015589, oi_at_entry=112656400.2687
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (win)

[WIN] AVAX-USD oi_divergence_long (long) (+0.6393)
  Triggered: price_chg_1h=-0.017894, oi_chg_1h=-0.018364, oi_at_entry=12561312.3244
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (win)

[WIN] FET-USD oi_divergence_long (long) (+11.34)
  Triggered: price_chg_1h=-0.019937, oi_chg_1h=-0.066024, oi_at_entry=568981.24
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (win)

[LOSS] NEAR-USD oi_divergence_long (long) (-89.1)
  Triggered: price_chg_1h=-0.011948, oi_chg_1h=-0.031882, oi_at_entry=38783709.452
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] AVAX-USD oi_divergence_long (long) (+23.37)
  Triggered: price_chg_1h=-0.017685, oi_chg_1h=-0.015433, oi_at_entry=12539435.5704
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (win)

[LOSS] XRP-USD oi_divergence_long (long) (-89.84)
  Triggered: price_chg_1h=-0.006611, oi_chg_1h=-0.017863, oi_at_entry=110565619.5305
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] AVAX-USD oi_divergence_long (long) (-101.8)
  Triggered: price_chg_1h=-0.007634, oi_chg_1h=-0.017299, oi_at_entry=12373569.5265
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] NEAR-USD oi_divergence_long (long) (-24.76)
  Triggered: price_chg_1h=-0.010117, oi_chg_1h=-0.024518, oi_at_entry=37153032.755
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

Still open (too soon to say why it worked or not):
  FET-USD oi_divergence_long (long) -- triggered: price_chg_1h=-0.010919, oi_chg_1h=-0.017316, oi_at_entry=580523.82
  SOL-USD oi_divergence_long (long) -- triggered: price_chg_1h=-0.010191, oi_chg_1h=-0.012203, oi_at_entry=304656465.7433

**US -- WHY** (2026-09-11)
- Fired: 40 | Resolved: 31 | Still open: 9

[LOSS] RF triple_ma_long (long) (-959)
  Triggered: EMA(8/16/25) = 29.9194/29.8528/29.8332, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [STOP OVERSHOOT] intended risk 0.1893/unit, actual loss 0.29/unit (1.5x) -- price moved past the stop faster than the bot's bar-close check could exit; a violent move against the position, amplified by simulation lag rather than a bad entry call

[WIN] MARA triple_threat_long (long) (+252.9)
  Triggered: RSI 43->65 crossed 50, broke 11.8, trend EMA 11.67
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] INTC triple_threat_long (long) (+76.36)
  Triggered: RSI 34->74 crossed 50, broke 102.2, trend EMA 102
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] CSCO triple_threat_long (long) (+382.1)
  Triggered: RSI 25->72 crossed 50, broke 109.1, trend EMA 108.6
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] NIO triple_threat_long (long) (+271.5)
  Triggered: RSI 13->71 crossed 50, broke 3.63, trend EMA 3.631
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] MARA triple_ma_long (long) (+238.6)
  Triggered: EMA(8/16/25) = 11.7143/11.6805/11.6797, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] RIVN triple_ma_long (long) (+564)
  Triggered: EMA(8/16/25) = 16.1948/16.1719/16.1642, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] RIVN triple_ma_long (long) (-1,067)
  Triggered: EMA(8/16/25) = 16.3918/16.2844/16.2392, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] SNAP triple_ma_long (long) (+281.3)
  Triggered: EMA(8/16/25) = 5.52798/5.47952/5.45236, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] CSCO triple_ma_long (long) (+1,071)
  Triggered: EMA(8/16/25) = 109.131/108.807/108.77, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] AAL triple_ma_long (long) (+243.6)
  Triggered: EMA(8/16/25) = 12.967/12.9178/12.903, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] T triple_ma_long (long) (+395.2)
  Triggered: EMA(8/16/25) = 25.7828/25.6813/25.615, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] NEM triple_ma_long (long) (-471.6)
  Triggered: EMA(8/16/25) = 127.444/127.099/127.09, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] DAL triple_ma_long (long) (+283.3)
  Triggered: EMA(8/16/25) = 78.8981/78.6198/78.5512, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] MARA triple_ma_long (long) (-557)
  Triggered: EMA(8/16/25) = 11.8955/11.7838/11.7487, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] RIVN triple_ma_long (long) (-1,140)
  Triggered: EMA(8/16/25) = 16.3707/16.2732/16.2319, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] CSCO triple_ma_long (long) (+1,127)
  Triggered: EMA(8/16/25) = 109.117/108.8/108.765, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] AAL triple_ma_long (long) (+502.7)
  Triggered: EMA(8/16/25) = 12.9581/12.9131/12.9, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] DAL triple_ma_long (long) (+238.6)
  Triggered: EMA(8/16/25) = 78.8992/78.6204/78.5516, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] SNAP triple_ma_long (long) (+466.5)
  Triggered: EMA(8/16/25) = 5.53955/5.49129/5.46204, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] T triple_ma_long (long) (+296.2)
  Triggered: EMA(8/16/25) = 25.7884/25.6843/25.6169, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] SIRI triple_ma_long (long) (+486.8)
  Triggered: EMA(8/16/25) = 29.044/28.9604/28.9155, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] NEM triple_ma_long (long) (-315.7)
  Triggered: EMA(8/16/25) = 127.413/127.083/127.079, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] GOLD triple_ma_long (long) (-394.3)
  Triggered: EMA(8/16/25) = 47.4189/46.7474/46.6598, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] CCL triple_ma_long (long) (+430.8)
  Triggered: EMA(8/16/25) = 22.6705/22.5881/22.5812, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] NEM triple_ma_long (long) (-564.4)
  Triggered: EMA(8/16/25) = 127.495/127.16/127.128, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] RIOT triple_ma_long (long) (-486.2)
  Triggered: EMA(8/16/25) = 21.5147/21.4131/21.4124, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] INTC triple_ma_long (long) (-991.2)
  Triggered: EMA(8/16/25) = 102.991/102.445/102.384, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

[WIN] NCLH triple_ma_long (long) (+261)
  Triggered: EMA(8/16/25) = 14.7325/14.6719/14.6699, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] RIOT triple_ma_long (long) (+363.1)
  Triggered: EMA(8/16/25) = 21.5403/21.4472/21.4348, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[WIN] INTC triple_ma_long (long) (+202)
  Triggered: EMA(8/16/25) = 102.679/102.672/102.608, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

Still open (too soon to say why it worked or not):
  SNAP triple_ma_long (long) -- triggered: EMA(8/16/25) = 5.50922/5.46472/5.44093, freshly aligned
  HBAN triple_ma_long (long) -- triggered: EMA(8/16/25) = 16.7077/16.6605/16.6421, freshly aligned
  WFC triple_ma_long (long) -- triggered: EMA(8/16/25) = 89.4557/89.2323/89.1805, freshly aligned
  PYPL triple_ma_long (long) -- triggered: EMA(8/16/25) = 53.2392/53.1303/53.0506, freshly aligned
  MARA triple_ma_long (long) -- triggered: EMA(8/16/25) = 11.8778/11.7743/11.7425, freshly aligned
  NIO triple_ma_long (long) -- triggered: EMA(8/16/25) = 3.65845/3.63963/3.63938, freshly aligned
  WFC triple_ma_long (long) -- triggered: EMA(8/16/25) = 89.5466/89.3009/89.2258, freshly aligned
  C triple_ma_long (long) -- triggered: EMA(8/16/25) = 139.067/138.575/138.335, freshly aligned
  NIO triple_ma_long (long) -- triggered: EMA(8/16/25) = 3.66067/3.6408/3.64015, freshly aligned

**INDIA FUTURES (MANUAL) -- WHY** (2026-09-11)
- Fired: 4 | Resolved: 4 | Still open: 0

[WIN] BANKNIFTY-FUT triple_ma_long (long) (+672.8)
  Triggered: EMA(8/16/25) = 56,347.3/56,278/56,267.5, freshly aligned
  Outcome:   trail-locked win -- price moved favorably first, trailing stop locked in the gain (real follow-through)

[LOSS] NIFTY-FUT triple_ma_long (long) (-94.91)
  Triggered: EMA(8/16/25) = 23,392.1/23,373.2/23,373, freshly aligned
  Outcome:   early exit -- the setup's own signal flipped/faded before price reached stop or target, so the bot cut it rather than wait for the trailing stop (validated exit, see monitor.py's trend_reversed()) (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via trend_reversed; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] NIFTY-FUT triple_ma_long (long) (-526.2)
  Triggered: EMA(8/16/25) = 23,398.3/23,378.6/23,376.5, freshly aligned
  Outcome:   session ended before stop or target hit -- settled at the day's close (loss)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited via eod_settlement; the market simply moved the other way this time (normal strategy variance, not a bug)

[LOSS] SENSEX-FUT triple_ma_long (long) (-267.7)
  Triggered: EMA(8/16/25) = 74,694.7/74,628.9/74,622.4, freshly aligned
  Outcome:   real stop-loss -- no favorable move before the stop hit (no edge at entry)
  Diagnosis: [market read wrong] no anomaly found -- setup fired per its own rules and exited within its intended risk; the market simply moved the other way this time (normal strategy variance, not a bug)

---

