# S3 QA v2 — Master Summary Report
**Compiled:** 2026-02-17 | **Auditor:** Claude Sonnet 4.5 (12 parallel agents)
**Scope:** All 12 chapters × 80 images (4 tiers × 20 scenes) = 960 images (959 audited; CH02-SC03-T2 missing)

---

## Overall Pass Rate

| Chapter | Guest Character | Pass | Total | Pass% | T1% | T2% | T3% | T4% |
|---------|----------------|------|-------|-------|-----|-----|-----|-----|
| Ch01 — The Invitation Arrives | None | 27 | 80 | **34%** | 45% | 30% | 25% | 35% |
| Ch02 — Journey to the Woodworker's Grove | Master Thomas | 1 | 79 | **1%** | 0% | 0% | 5% | 0% |
| Ch03 — The Sawdust Challenge | Master Thomas | 11 | 80 | **14%** | 20% | 10% | 15% | 10% |
| Ch04 — Building Boxes | Master Thomas | 1 | 80 | **1%** | 0% | 0% | 5% | 0% |
| Ch05 — The Potter's Valley | Master Potter | 44 | 80 | **55%** | 60% | 45% | 55% | 60% |
| Ch06 — Throwing and Turning | Master Potter | 42 | 80 | **53%** | 50% | 55% | 50% | 55% |
| Ch07 — The Kiln's Secret | Master Potter | 42 | 80 | **53%** | 70% | 50% | 45% | 45% |
| Ch08 — The Inventor's Tower | Maestro Gearsmith | 45 | 80 | **56%** | 70% | 50% | 55% | 50% |
| Ch09 — Blueprint Dreams | Maestro Gearsmith | 32 | 80 | **40%** | 70% | 50% | 25% | 15% |
| Ch10 — Maker's Market Research | None | 41 | 80 | **51%** | 60% | 55% | 50% | 40% |
| Ch11 — The Creation Workshop | None | 51 | 80 | **64%** | 75% | 60% | 75% | 45% |
| Ch12 — The Makers' Faire | None | 22 | 80 | **28%** | 70% | 25% | 15% | 0% |
| **TOTAL** | | **359** | **959** | **37%** | | | | |

### Pass Rate by Tier (across all 12 chapters)

| Tier | Pass | Audited | Pass% | Primary failure mode |
|------|------|---------|-------|---------------------|
| Tier 1 | ~119 | 240 | **50%** | Riley single bow, Ellis shirt, WRONG_ELDERLY in Ch02-04 |
| Tier 2 | ~86 | 238 | **36%** | Ellis orange/black shirt (batch-wide), WRONG_ELDERLY, Layla straight hair |
| Tier 3 | ~86 | 240 | **36%** | Benny overalls+bowtie (ALL chapters), WRONG_ELDERLY, BUBBLE (Ch09) |
| Tier 4 | ~71 | 240 | **30%** | Riley loses pigtails (Ch12), Ellis orange/white shirt, ANIMAL_ERROR, STYLE_DRIFT |

### Pass Rate by Chapter Type

| Category | Chapters | Avg Pass% | Primary issue |
|----------|---------|-----------|---------------|
| Master Thomas chapters | Ch02–Ch04 | **5%** | WRONG_ELDERLY across T1/T2; no bandana T1/T2 |
| Master Potter chapters | Ch05–Ch07 | **54%** | WRONG_ELDERLY scattered, skin-tone drift T3, CHAR_DUPLICATE SC13 |
| Maestro Gearsmith chapters | Ch08–Ch09 | **48%** | 0 clean Maestro passes in Ch09, BUBBLE (blueprint text) T3/T4 |
| No-guest chapters | Ch01, Ch10–Ch12 | **44%** | Riley bow, Ellis shirt, Benny T3 costume, Ch12 T4 complete failure |

---

## Systemic Issues — Cross-Chapter Analysis

### Issue 1: Riley Two-Bow Failure (UNIVERSAL)
**Severity: CRITICAL | Chapters affected: All 12 | Est. images: ~380/959**

Riley must have TWO pink bows, one in each pigtail. In approximately 40–60% of all scenes across all tiers and chapters, Riley renders with only ONE bow (headband-style) or a single bow on one side. In Tier 4 of Ch12, Riley loses her pigtails entirely (18/20 scenes show straight hair with single pink headband).

**Worst chapters:** Ch12-T4 (0/20 correct), Ch01-T3 (~15/20 fail), Ch02 (~60/79 fail)
**Root cause:** Prompt-level failure to enforce two-pigtail two-bow constraint

---

### Issue 2: Ellis Shirt Drift (CLOTH_DRIFT — Tier-wide)
**Severity: HIGH | Chapters affected: All 12 | Est. images: ~250/959**

Ellis's canonical red soccer shirt is replaced by:
- **Tier 2:** Orange/black striped soccer kit (batch-wide across most chapters)
- **Tier 4:** Orange/white striped jersey (batch-wide across most chapters)
- **Tier 3:** Plaid, checkered, or flannel shirts in scattered scenes

Tier 1 generally has the best Ellis compliance (~70–80% correct).

**Worst chapters:** Ch07-T2 (all 20 scenes wrong), Ch12-T4 (17/20 wrong), Ch04-T2 (all 20 wrong)

---

### Issue 3: Benny Tier 3 Costume (CLOTH_DRIFT — T3 Universal)
**Severity: HIGH | Chapters affected: All 12 | Est. images: ~130/240 T3 scenes**

In Tier 3, Benny consistently wears GREEN OVERALLS with a RED BOW TIE instead of his canonical green plaid scarf. This is a full-tier costume substitution present in every chapter (some T3 scenes partially revert to scarf). The character is still animated (not ANIMAL_ERROR) but the outfit is wrong throughout the tier.

**Note:** Overalls appear in T4 of some chapters and scattered in T1/T2 as well, but T3 is universal.

---

### Issue 4: WRONG_ELDERLY — Guest Character Substitution
**Severity: CATASTROPHIC (Ch02–04), HIGH (Ch05–09)**

The most destructive issue in the season. Three distinct manifestations:

#### Master Thomas chapters (Ch02–Ch04):
- **Ch02:** Slim elderly man (white hair, no bandana, no beard) substitutes for Master Thomas in ALL T1/T2 scenes SC08–SC20. Tier 3 is the ONLY tier with correct Master Thomas. T4 mostly correct except SC17. Only 1 passing image exists in T1 (none in T2).
- **Ch03:** Elderly WOMAN (gray bun, round glasses, floral apron) substitutes in ~17 scenes across all tiers. Also multi-panel corruption and CHAR_MISSING.
- **Ch04:** Master Thomas missing blue bandana in ALL 40 T1/T2 scenes. T3/T4 have bandana correct. One PASS total in entire chapter (T3-SC19).

#### Master Potter chapters (Ch05–Ch07):
- Robed adult male at kiln (SC02 all 4 tiers, all 3 chapters)
- Pale-skinned woman with head-covering (T2-SC06 Ch05/Ch06)
- Skin tone drift toward olive/lighter in T3 (all Master Potter chapters)
- CHAR_DUPLICATE: Master Potter appears 2–3× in SC13 (Ch06-T1, Ch06-T4, Ch07-T3)

#### Maestro Gearsmith chapters (Ch08–Ch09):
- **Ch08:** Wrong adult in SC12 (black tuxedo man T2; polo-shirt grey man T4)
- **Ch09:** ZERO clean Maestro Gearsmith passes across all 80 images. Maestro replaced by: young bearded men, elderly women with grey buns, white-lab-coat scientists, Mr. Mason look-alikes

---

### Issue 5: BUBBLE — Text Leakage
**Severity: HIGH (Ch09 T3/T4), MODERATE (Ch12, Ch01)**

Blueprint and sign text appears as rendered readable text in images:
- **Ch09-T4-SC13 (MOST SEVERE):** "DISTRIBUTE FORCE", "COST PLANNING", "BUY: 4+1 SPARE=5 CLIPS", "6 INCHES APART", "COST ESTIMATE"
- **Ch09-T4-SC11:** "BASE: 10"×12"", "SUPPORT BEAMS (4)", "GRAIN DIRECTION FOR STRENGTH"
- **Ch09-T3-SC05:** "SCALE: 1 INCH = 1 UNIT", "8 INCH RETRACTABLE STRING"
- **Ch12-T3-SC12 (CRITICAL):** Garbled story text overlay: "Riley wern the sunprise within the potter and the potter oned. 'Riley's handmade marst bowl, evon consistent thickness and balanced forms.'"
- **Ch09-T1-SC15:** Blueprint reads "PLANNING", "LESS WASTE."
- **Ch12-T4 (multiple scenes):** "Summer's End Faire", "Handmade Toys" readable on signs

---

### Issue 6: ANIMAL_ERROR — Benny Not Animated Bear
**Severity: HIGH | Chapters affected: Ch01, Ch04, Ch11, Ch12**

| File | Description |
|------|-------------|
| CH04-SC01-T4 | Benny = photorealistic grizzly bear |
| CH04-SC17-T4 | Full scene photorealistic, Benny = real bear |
| CH04-SC18-T4 | Benny = miniature stuffed teddy at toy scale |
| CH04-SC17-T1 | Benny has deer antlers (prop corruption) |
| CH11-SC13-T4 | Benny = stuffed plush teddy on workbench (v1 bug unresolved) |
| CH11-SC15-T4 | Benny = stuffed plush teddy on workbench (v1 bug unresolved) |
| CH11-SC18-T4 | Benny = stuffed plush teddy (NEW — not in v1 list) |
| CH12-SC02-T4 | Benny = stuffed bear on table |
| CH12-SC20-T4 | Benny = stuffed bear on porch |
| CH01-SC08-T3 | Benny appears stuffed/inanimate |
| CH12-SC09-T1 | Benny = stuffed toy at table scale |

---

### Issue 7: MULTI_PANEL — Split Layout Renders
**Severity: HIGH | Chapters affected: Ch03, Ch04, Ch08, Ch09, Ch11**

| File | Description |
|------|-------------|
| CH08-SC16-T2 | 2-panel side-by-side with character reference inset |
| CH08-SC16-T3 | 4-quadrant 2×2 grid with non-canonical children |
| CH08-SC16-T4 | 3-panel strip; Ellis duplicated 3× across panels |
| CH08-SC18-T2 | 2-panel; Benny at realistic-bear scale |
| CH09-SC11-T4 | 2-panel hyper-realistic oil painting of same blonde boy |
| CH03-SC11-T1 | 4-panel comic layout |
| CH03-SC11-T2 | 2-panel; WRONG_ELDERLY woman in both panels |
| CH03-SC11-T4 | 3-panel; WRONG_ELDERLY woman in all panels |
| CH03-SC12-T4 | 2-panel; WRONG_ELDERLY in both |
| CH03-SC04-T2 | 2-panel; Layla/Riley/Ellis absent |
| CH03-SC04-T3 | 3-panel; Layla/Riley/Ellis absent |
| CH04-SC04-T4 | Embedded thumbnail insets in upper corner |
| CH11-SC14-T1 | 4-panel grid (v1 known, unresolved) |
| CH11-SC03-T2 | Inset panel in corner (v1 known, unresolved) |

---

### Issue 8: Layla Hair/Bow Issues
**Severity: MODERATE | Spread across all chapters**

- **Straight hair** (should be wavy/curly): Tier 2 in most chapters (Ch12-T2 is tier-wide), Tier 4 scattered
- **Hood UP** (should be DOWN): Ch07-T4-SC01, Ch10-T4-SC02, various scattered scenes
- **Yellow bow missing:** Scattered scenes across Ch06, Ch11 T2

---

## Character Failure Rate Summary

| Character | Most Common Issue | Approx. Failure Rate | Worst Chapter |
|-----------|------------------|---------------------|---------------|
| Riley | Single bow / missing pigtails | ~45% of all scenes | Ch12-T4 (100% fail on this) |
| Ellis | Wrong shirt color | ~35% of all scenes | Ch07-T2 (100%), Ch12-T4 (85%) |
| Benny | T3 overalls costume | ~55% of T3 scenes | All chapters T3 |
| Layla | Straight hair | ~20% of all scenes | Ch12-T2 (tier-wide) |
| Master Thomas | WRONG_ELDERLY / no bandana | ~80% of scenes in Ch02-04 | Ch02-T1/T2 (100%) |
| Master Potter | Skin-tone drift / WRONG_ELDERLY | ~20% of Potter scenes | Ch06-T1 (~30%) |
| Maestro Gearsmith | WRONG_ELDERLY / never correct | ~60% of Maestro scenes | Ch09 (0% pass rate for character) |

---

## Top 20 Priority Regenerations (Immediate Action Required)

Ranked by severity. All are P0/P1 critical.

| Rank | File | Error Codes | Issue |
|------|------|------------|-------|
| 1 | CH12-SC12-T3 | BUBBLE | Garbled story text rendered in image — unacceptable for publication |
| 2 | CH09-SC13-T4 | BUBBLE | Engineering annotations covering blueprint: "DISTRIBUTE FORCE", "COST PLANNING", "BUY: 4+1 SPARE=5 CLIPS" |
| 3 | CH09-SC11-T4 | MULTI_PANEL + STYLE_DRIFT + BUBBLE | Split hyper-realistic oil painting; blueprint text; 2-panel |
| 4 | CH04-SC01-T4 | ANIMAL_ERROR + CHAR_MISSING | Benny = photorealistic grizzly; Riley absent |
| 5 | CH04-SC17-T4 | ANIMAL_ERROR | Full scene photorealistic real-world; Benny = real bear |
| 6 | CH06-SC13-T1 | CHAR_DUPLICATE | Master Potter appears 3× in single frame |
| 7 | CH06-SC13-T4 | CHAR_DUPLICATE | Master Potter appears 2× in single frame |
| 8 | CH08-SC12-T2 | WRONG_ELDERLY | Adult in black tuxedo replaces Maestro entirely |
| 9 | CH08-SC12-T4 | WRONG_ELDERLY | Grey-haired man in polo shirt replaces Maestro |
| 10 | CH07-SC01-T4 | WRONG_ELDERLY + CLOTH_DRIFT | Elderly man at kiln instead of Celeste; Layla hood UP |
| 11 | CH02-SC17-T4 | WRONG_ELDERLY + CHAR_DRIFT + ANIMAL_ERROR | Wrong elderly man + Layla hood UP + Benny stuffed toy |
| 12 | CH02-SC14-T2 | WRONG_ELDERLY + CHAR_DRIFT + CLOTH_DRIFT + ANIMAL_ERROR | 4 simultaneous errors — worst single T2 scene |
| 13 | CH11-SC13-T4 | ANIMAL_ERROR | Benny = inanimate stuffed plush on workbench (v1 unresolved) |
| 14 | CH11-SC15-T4 | ANIMAL_ERROR | Benny = inanimate stuffed plush (v1 unresolved) |
| 15 | CH11-SC18-T4 | ANIMAL_ERROR | Benny = inanimate stuffed plush (NEW — not in v1 list) |
| 16 | CH09-SC07-T3 | WRONG_ELDERLY | Maestro replaced by elderly WOMAN with grey bun and glasses |
| 17 | CH03-SC11-T2 | MULTI_PANEL + WRONG_ELDERLY | 2-panel; elderly woman in both panels |
| 18 | CH08-SC16-T4 | MULTI_PANEL + CHAR_DUPLICATE | 3-panel strip; Ellis duplicated 3× |
| 19 | CH12-SC17-T4 | CHAR_DRIFT + CHAR_MISSING + CHAR_EXTRA | All three core children replaced by unrecognisable characters |
| 20 | CH04-SC18-T4 | ANIMAL_ERROR | Benny = miniature stuffed teddy at toy scale |

---

## Batch Regeneration Priority Queue

### BATCH 1 — WRONG_ELDERLY Master Thomas (Ch02–Ch04)
**~60 images requiring full regeneration of guest character**
- Ch02: All T1 and T2 scenes SC08–SC20 (26 images) — wrong elderly man throughout
- Ch03: All WRONG_ELDERLY WOMAN scenes (confirm from ch03_qa.md flags — ~17 images)
- Ch04: All T1 and T2 scenes SC01–SC20 (40 images) — missing blue bandana

*Fix: Add blue bandana to Master Thomas prompt; enforce stocky/heavyset build; full gray beard*

### BATCH 2 — Ellis Red Shirt (Tier 2 All Chapters)
**~140 images with wrong shirt color**
- Every Tier 2 chapter has a batch-wide orange/black shirt substitution for Ellis
- Every Tier 4 chapter has orange/white stripe substitution

*Fix: Explicitly enforce "SOLID RED soccer shirt, NOT orange, NOT striped, NOT plaid" at T2/T4 prompt level*

### BATCH 3 — Riley Two Bows (All Chapters, All Tiers)
**~380 images with single-bow or missing pigtail**
- Universal across all 12 chapters; worst in T4

*Fix: Enforce "TWO separate pigtails, each with ONE pink bow, BOTH bows clearly visible from front"*

### BATCH 4 — Benny T3 Costume (All Chapters, Tier 3)
**~130 images with overalls+bowtie instead of green plaid scarf**
- Every single chapter in Tier 3 shows this costume substitution

*Fix: Explicitly remove overalls from T3 Benny prompt; add "green plaid scarf ONLY, no overalls, no bow-tie"*

### BATCH 5 — Maestro Gearsmith Ch09 (All 80 Images)
**80 images with zero clean Maestro appearances**
- Every Maestro scene in Ch09 fails the character spec
- Wrong characters: elderly women, bearded men, lab-coat scientists, Mr. Mason look-alikes

*Fix: Maestro must have spiky WHITE hair, BRASS GOGGLES on forehead, BROWN LEATHER apron; no grey swept hair, no lab coat, no tuxedo*

### BATCH 6 — Blueprint Text Leakage Ch09 (Tier 3 + Tier 4)
**~12 images with readable engineering annotations on blueprints**
- Most severe: T4-SC13, T4-SC11, T4-SC10, T3-SC05, T3-SC12, T3-SC16

*Fix: Remove all text from blueprint surfaces; "blueprints show line drawings only, no readable text, no measurements, no annotations"*

### BATCH 7 — Layla Straight Hair Tier 2 (Ch12 + Others)
**~30 images with straight hair instead of wavy/curly**
- Ch12-T2: Tier-wide (all 20 scenes), known v1 unresolved
- Ch01-T2, Ch09-T4, Ch10-T2 scattered

*Fix: Enforce "dark wavy/curly voluminous hair" at T2 Layla prompt*

---

## File Status Note

**Missing file:** `S3-CH02-SC03-T2.png` — Does not exist on disk. Must be generated fresh.

---

## Chapter-by-Chapter Quick Reference

For detailed per-scene pass/fail tables, see individual chapter files:
- [Ch01 QA](./S3_QA_v2/ch01_qa.md) — 34% | Riley bow, Ellis shirt
- [Ch02 QA](./S3_QA_v2/ch02_qa.md) — 1% | WRONG_ELDERLY (all T1/T2), bandana missing
- [Ch03 QA](./S3_QA_v2/ch03_qa.md) — 14% | WRONG_ELDERLY woman, MULTI_PANEL
- [Ch04 QA](./S3_QA_v2/ch04_qa.md) — 1% | Bandana missing T1/T2, ANIMAL_ERROR T4
- [Ch05 QA](./S3_QA_v2/ch05_qa.md) — 55% | SC02 robed man, Potter skin drift T3
- [Ch06 QA](./S3_QA_v2/ch06_qa.md) — 53% | CHAR_DUPLICATE SC13, WRONG_ELDERLY scattered
- [Ch07 QA](./S3_QA_v2/ch07_qa.md) — 53% | WRONG_ELDERLY T4-SC01, T3 batch Potter/Benny drift
- [Ch08 QA](./S3_QA_v2/ch08_qa.md) — 56% | MULTI_PANEL SC16, WRONG_ELDERLY SC12
- [Ch09 QA](./S3_QA_v2/ch09_qa.md) — 40% | 0 clean Maestro passes, BUBBLE severe T3/T4
- [Ch10 QA](./S3_QA_v2/ch10_qa.md) — 51% | Ellis jersey drift, Benny T3, Riley bow
- [Ch11 QA](./S3_QA_v2/ch11_qa.md) — 64% | ANIMAL_ERROR T4 (×3), MULTI_PANEL T1/T2
- [Ch12 QA](./S3_QA_v2/ch12_qa.md) — 28% | T4 complete failure (0%), BUBBLE T3-SC12

---

*Master report compiled 2026-02-17. Based on 12 independent visual QA audits of 959 total images.*
