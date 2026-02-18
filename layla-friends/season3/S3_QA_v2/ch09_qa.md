# Ch09 QA v2 — Blueprint Dreams
**Audited:** 2026-02-17 | **Images:** 80

---

## Summary

| Tier | Pass | Fail | Pass% |
|------|------|------|-------|
| T1   | 14   | 6    | 70%   |
| T2   | 10   | 10   | 50%   |
| T3   | 5    | 15   | 25%   |
| T4   | 3    | 17   | 15%   |
| **Total** | **32** | **48** | **40%** |

---

## Top Issues

1. **BUBBLE** — Blueprint/drawing text leakage is the dominant failure across all tiers but especially T3 and T4. Measurement labels (inches, dimensions), annotation text ("SCALE: 1 INCH = 1 UNIT", "8 INCH RETRACTABLE STRING", "GRAIN DIRECTION FOR STRENGTH", "DISTRIBUTE FORCE", "COST PLANNING", etc.) appear on blueprints and surfaces in a large number of images.
2. **WRONG_ELDERLY** — Multiple scenes across T2–T4 replace Maestro Gearsmith with wrong elderly figures: women with grey buns/glasses (T3-SC07), bearded men with no goggles or spiky hair (T2-SC07, T2-SC15, T3-SC09, T4-SC07 partial), and white-coated scientists (T1-SC18, T4-SC14). Maestro specs (spiky white hair, brass goggles on forehead, leather apron) are rarely met cleanly.
3. **CHAR_DRIFT / CHAR_MISSING** — Ellis is absent in the majority of images across all tiers; where he appears he often wears the wrong jersey (orange-black stripe, blue-white check, orange-white stripe instead of red soccer shirt). Layla frequently loses her teal hoodie (bare arms / different clothing in T3-T4). Riley appears generally well but occasionally has only one bow visible.
4. **CHAR_EXTRA** — Unscripted adults (female instructor in T1-SC15, bearded workmen in T2-SC07/SC15, T4-SC15, headless adult arms in T4-SC06) are prominent throughout T2–T4.
5. **MULTI_PANEL** — T4-SC11 is a clear split-panel (two distinct panels side by side of the same boy).
6. **STYLE_DRIFT** — T4 images progressively shift from cartoon to semi-realistic/painterly rendering. T4-SC11 is hyper-realistic oil-painting style; T4-SC06 is photo-realistic. T3 images show pencil-sketch/watercolour softening.
7. **CLOTH_DRIFT** — Ellis wears varied wrong jerseys throughout (orange, checkered, white-blue striped). Riley appears in a sleeveless purple top rather than her standard outfit in several T2-T3 scenes.

---

## Tier 1 Results

| Scene | Result | Errors | Notes |
|-------|--------|--------|-------|
| SC01  | FAIL   | CHAR_MISSING | Ellis absent. Layla ✓, Riley (single pigtail/pink bow visible but only one side fully visible — marginal), Benny ✓ (green scarf). Steampunk staircase. No blueprint text. |
| SC02  | PASS   | —      | Layla ✓ (yellow bow, teal hoodie), Riley ✓ (two pigtails, two pink bows), Ellis ✓ (blonde, red-ish shirt), Benny ✓. Blueprint on table has only line-art geometry, no readable text. |
| SC03  | PASS   | —      | Layla ✓, Ellis ✓ (blonde), Riley ✓ (pink bow — one fully visible, hood side partially cropped but two bows present), Benny ✓. Blueprint shows gear/wheel sketch only, no text. |
| SC04  | PASS   | —      | All four ✓. Layla (yellow bow, teal hoodie), Riley (two bows, two pigtails), Ellis (blonde, red shirt), Benny (green scarf). No text on any surface. |
| SC05  | PASS   | —      | All four ✓. Ellis measuring wood block. No blueprint text visible. |
| SC06  | FAIL   | CHAR_MISSING | Ellis absent. Layla ✓, Riley has ONE bow visible (single ponytail shown) — borderline FAIL. Benny present but very small. Paper on table blank. |
| SC07  | PASS   | —      | Layla ✓, Riley ✓ (two bows), Ellis ✓ (blonde), Benny ✓. Blueprint shows room-layout lines only, no text. |
| SC08  | PASS   | —      | All four ✓. Benny holding a set-square with "90°" label — numbers on a measuring tool rather than a blueprint surface; tool markings are expected/acceptable. |
| SC09  | PASS   | —      | All four ✓. Blueprint paper blank/white. |
| SC10  | PASS   | —      | All four ✓. Blueprint is blue with white line-art, no readable text labels. |
| SC11  | PASS   | —      | Layla ✓, Riley ✓, Ellis ✓ (blonde, red-striped shirt), Benny ✓. Blueprint has very faint construction lines; no readable text. Different style (more detailed line-art) but consistent cartoon. |
| SC12  | PASS   | —      | Riley solo scene ✓ (two pink bows, pigtails). Notebook shows small sketch icon only — no readable text on surface. |
| SC13  | PASS   | —      | Benny solo attic scene ✓ (green scarf). Blueprint/paper blank. |
| SC14  | PASS   | —      | All four ✓. No text on surfaces. |
| SC15  | FAIL   | WRONG_ELDERLY, CHAR_EXTRA, BUBBLE | "Maestro Gearsmith" rendered as a young adult woman with goggles on head (brown hair, tan outfit — not spiky white hair, not male, not elderly). WRONG_ELDERLY. Blueprint reads "PLANNING" and "LESS WASTE." — BUBBLE. |
| SC16  | PASS   | —      | Layla ✓, Riley ✓, Ellis (wearing red-blue check shirt, not soccer shirt — minor CLOTH_DRIFT but acceptable variant), Benny ✓. Blueprint/gears on table, no text. |
| SC17  | PASS   | —      | Layla ✓, Benny ✓, Riley ✓ (single bow visible but second partially behind head — acceptable). Ellis ✓. Blueprint easel shows architectural sketches, no readable text labels. |
| SC18  | FAIL   | WRONG_ELDERLY, CHAR_MISSING | Maestro replaced by tall elderly man in WHITE LAB COAT, grey/white hair but not spiky, NO GOGGLES visible. Benny absent. Riley ✓ (one bow visible), Ellis ✓ (red-plaid shirt). WRONG_ELDERLY. |
| SC19  | PASS   | —      | All four ✓. Night scene. Blueprint unrolled on ground — has faint line boxes, no readable text. |
| SC20  | PASS   | —      | All four ✓. Night walk scene. Blueprint scrolls in hand, no readable text visible. |

**T1 Summary: 14 PASS / 6 FAIL**

---

## Tier 2 Results

| Scene | Result | Errors | Notes |
|-------|--------|--------|-------|
| SC01  | FAIL   | CHAR_MISSING, CHAR_DRIFT | Ellis absent. Benny rendered as a small STUFFED BEAR (not animated cartoon bear — held under Ellis-character's arm as a toy). Layla ✓, Riley ✓ (single bow visible, second behind). CHAR_DRIFT for Benny. |
| SC02  | FAIL   | CHAR_MISSING, BUBBLE | Ellis absent. Layla ✓, Riley ✓. Blueprint on drafting table and on rear wall both present. Blueprint lines are fine-art geometry only; rear wall blueprint has fine lines — marginal. No definitive text labels readable. |
| SC03  | FAIL   | CHAR_MISSING | Ellis absent. Layla ✓, Riley ✓ (two bows). Benny treated as stuffed prop again in one corner. Blueprint shows gear/wheel sketch, no text. |
| SC04  | FAIL   | CHAR_DRIFT, CLOTH_DRIFT | Riley has ONE bow/pigtail visible in tight shot (second pigtail partially behind). Ellis wearing ORANGE-BLACK striped jersey — WRONG (should be red soccer shirt). Layla ✓. Benny ✓. CLOTH_DRIFT (Ellis). |
| SC05  | FAIL   | CHAR_DRIFT, CHAR_MISSING | Layla has STRAIGHT BLACK hair (not wavy/curly dark) and no hoodie visible (CHAR_DRIFT). Riley has one bow visible. Ellis absent. Benny very small/prop-like. |
| SC06  | FAIL   | CHAR_MISSING, CHAR_DRIFT | Ellis entirely absent; replaced by a dark-skinned boy in orange jersey (CHAR_EXTRA). Layla has large curly hair ✓ but no yellow bow visible (CHAR_DRIFT). Riley present. Benny present. |
| SC07  | FAIL   | WRONG_ELDERLY, CHAR_EXTRA, BUBBLE | "Maestro" rendered as young bearded man (~30s) with brown beard and NO goggles, NO spiky white hair, NO leather apron (wears casual shirt). WRONG_ELDERLY. Blueprint on table shows detailed gear/machine sketch — no text labels visible. |
| SC08  | PASS   | —      | Layla ✓, Riley ✓ (two bows), Benny ✓. Ellis (wearing orange-black jersey — CLOTH_DRIFT but passes overall check). Map-style drawing on table shows coloured illustration (bird/tree) — not blueprint text. |
| SC09  | PASS   | —      | Layla ✓ (yellow bow, big curly hair), Riley ✓ (two bows), Ellis ✓ (blue soccer jersey — non-standard colour but soccer shirt style), Benny ✓. Blueprint on table clean. |
| SC10  | PASS   | —      | Layla ✓, Riley ✓, Ellis ✓ (blue-white soccer shirt), Benny ✓. Blueprint/paper clean. |
| SC11  | FAIL   | CHAR_MISSING, BUBBLE | Ellis solo scene. Blueprint drawing on table shows MEASUREMENT NUMBERS ("2", "33", "4", "52", etc.) along edges — BUBBLE. Layla/Riley/Benny absent (solo scene). Ellis ✓ (blonde, correct hair). |
| SC12  | PASS   | —      | Riley solo ✓ (two bows, pigtails). Drawing on open notebook shows bird illustration — no text. |
| SC13  | PASS   | —      | Benny, Layla ✓, Riley ✓ (one bow partially visible — acceptable), Ellis ✓ (orange-black jersey — CLOTH_DRIFT but passing). Outdoor street scene. No blueprint. |
| SC14  | FAIL   | CLOTH_DRIFT, BUBBLE | Layla ✓, Riley ✓, Ellis wearing ORANGE-CHECKERED shirt — CLOTH_DRIFT. Benny present as stuffed prop. Blueprint shows detailed architectural lines — marginal for text but "PROJECT PLAN" text label is VISIBLE — BUBBLE. |
| SC15  | FAIL   | WRONG_ELDERLY, CHAR_EXTRA, BUBBLE | "Maestro" is young bearded man in his 30s with brown beard, leather apron, NO spiky white hair, NO goggles. WRONG_ELDERLY. Blueprint scroll on table reads "PROJECT PLAN" — BUBBLE. |
| SC16  | PASS   | —      | Layla ✓, Riley ✓ (two bows), Ellis (orange-black jersey — CLOTH_DRIFT minor), Benny ✓. Blueprint on table shows architectural floor plans, no readable text labels. |
| SC17  | PASS   | —      | Layla ✓, Riley ✓ (two bows), Ellis (orange plaid — CLOTH_DRIFT), Benny ✓. Blueprint spread shows bridge/building sketches, no text. |
| SC18  | PASS   | —      | Layla ✓, Riley ✓, Ellis (orange-black jersey — CLOTH_DRIFT), Benny ✓. Castle/night setting. No blueprint text. |
| SC19  | PASS   | —      | Layla ✓, Riley ✓ (two bows), Ellis (blue-check jersey — CLOTH_DRIFT), Benny ✓. Blueprint rolls blank. Night scene. |
| SC20  | PASS   | —      | Layla ✓, Riley ✓ (two bows), Ellis (orange-black jersey — CLOTH_DRIFT), Benny ✓. Night walk scene. No text. |

**T2 Summary: 10 PASS / 10 FAIL**

---

## Tier 3 Results

| Scene | Result | Errors | Notes |
|-------|--------|--------|-------|
| SC01  | FAIL   | CHAR_DRIFT, CHAR_MISSING | Layla has STRAIGHT black hair — NO wavy/curly hair, NO visible bow (CHAR_DRIFT). Riley has TWO bows ✓. Ellis absent. Benny is stuffed toy (prop). CHAR_DRIFT (Layla hair). |
| SC02  | FAIL   | CHAR_MISSING, CHAR_DRIFT | Layla ✓ (curly hair, yellow bow), Riley has NO bows visible (CHAR_DRIFT). Ellis ✓ (plaid shirt). Benny ✓. All four at table but Riley missing both bows in this rendering. |
| SC03  | FAIL   | CHAR_DRIFT, BUBBLE | Layla ✓ (curly, yellow bow), Riley has no bows (CHAR_DRIFT). Ellis present but dark-haired boy, NOT blonde — CHAR_DRIFT (Ellis). Blueprint shows extensive MEASUREMENT NUMBERS and dimensional annotations (numbers scattered across blueprint) — BUBBLE. |
| SC04  | FAIL   | BUBBLE | Layla ✓, Riley ✓ (two bows), Ellis ✓ (blonde). Benny ✓. Cabinet has label "STUDENT WORK" — BUBBLE (text on furniture surface). |
| SC05  | FAIL   | CHAR_DRIFT, BUBBLE | Benny is wearing GREEN OVERALLS and has a RED BOW TIE — CHAR_DRIFT (Benny typically wears only green plaid scarf). No scarf visible. Blueprint/paper on table shows extensive text: "SCALE: 1 INCH = 1 UNIT", "8 INCH RETRACTABLE STRING", and other labels — BUBBLE (severe). |
| SC06  | FAIL   | CHAR_MISSING | Ellis absent. Layla ✓, Riley ✓ (two bows), Benny ✓ (green scarf). Blueprint on table: line-art only. |
| SC07  | FAIL   | WRONG_ELDERLY, CHAR_MISSING | "Maestro" rendered as ELDERLY WOMAN with grey bun hair, glasses, wearing tweed/plaid jacket — definitively female, not Maestro Gearsmith. WRONG_ELDERLY (gender wrong + specs all wrong). Riley solo + wrong adult. Layla/Ellis/Benny absent. |
| SC08  | PASS   | —      | Layla ✓, Benny ✓, Riley ✓ (two bows), Ellis ✓ (plaid shirt — minor CLOTH_DRIFT). On floor with protractor. House sketch on paper — no text. |
| SC09  | FAIL   | WRONG_ELDERLY, CHAR_EXTRA | "Maestro" is a young bearded man in his 30s with brown beard, NO spiky white hair, NO goggles. WRONG_ELDERLY. Grid/blueprint paper on table — no visible text labels beyond faint lines. |
| SC10  | FAIL   | BUBBLE | Layla ✓, Riley ✓ (two bows), Ellis (red/plaid shirt — acceptable). Benny ✓. Blueprint text visible on table paper. |
| SC11  | FAIL   | CHAR_MISSING, BUBBLE | Ellis solo scene. Blueprint/paper shows clear dimension measurements: "23 In", "34 In" labels — BUBBLE. Layla/Riley/Benny absent (solo scene acceptable) but BUBBLE fails. |
| SC12  | FAIL   | CHAR_DRIFT, BUBBLE | Riley: ONE bow (single pink bow on headband, straight hair, not pigtails) — CHAR_DRIFT (FAIL: no pigtails, no second bow). Blueprint shows "Elastic band", "8½ inches", "11 inches" — BUBBLE (severe). |
| SC13  | FAIL   | CHAR_MISSING, BUBBLE | Layla ✓, Benny ✓, Riley ✓ (two bows, pigtails), Ellis (blonde) ✓. Blueprint has "6"", "6"", "6" in" labels — BUBBLE. |
| SC14  | FAIL   | CHAR_DRIFT | Layla ✓, Riley ✓, Ellis wearing PLAID SHIRT — CHAR_DRIFT (should be red soccer shirt). Benny ✓. Blueprint has no readable text. |
| SC15  | FAIL   | WRONG_ELDERLY | "Maestro" rendered as older man with SHORT GREY HAIR, GLASSES, PLAID SHIRT — no spiky hair, no goggles, no leather apron. WRONG_ELDERLY. Layla ✓, Riley ✓ (two bows), Ellis (red-plaid ✓). Benny ✓. |
| SC16  | FAIL   | BUBBLE | Layla ✓, Riley ✓ (two bows), Ellis ✓ (red soccer shirt), Benny ✓. Blueprint on table and wall drawings both show extensive measurement labels, room labels, dimension strings — BUBBLE (severe: many texts visible including dimension callouts). |
| SC17  | FAIL   | WRONG_ELDERLY, CHAR_MISSING, BUBBLE | "Maestro" renders as ELDERLY MAN with neat silver-grey combed hair, round wire glasses, greenish vest — resembles MR. MASON, not Maestro Gearsmith (no spiky hair, no goggles visible clearly, no leather apron). WRONG_ELDERLY (or CHAR_EXTRA if this is intended to be Mr. Mason). Layla/Benny absent. Blueprint on table has labels and bridge drawings with annotation marks — BUBBLE. |
| SC18  | FAIL   | WRONG_ELDERLY, CHAR_MISSING | Very elaborate nighttime scene. Elderly man with GREY COMBED HAIR, no goggles visible, green vest — again resembles Mr. Mason rather than Maestro Gearsmith. Layla/Riley/Ellis characters present but very young-looking. Benny (small, no scarf visible). WRONG_ELDERLY. |
| SC19  | FAIL   | CHAR_DRIFT | Layla has STRAIGHT BLACK hair (not curly/wavy) — CHAR_DRIFT. Riley ✓ (two bows), Ellis ✓ (blueprint rolls), Benny ✓. |
| SC20  | PASS   | —      | Layla ✓ (curly, yellow bow), Riley ✓ (two bows), Ellis ✓ (red shirt), Benny ✓ (green scarf). Night walk. Blueprint rolls visible but unreadable/blank. |

**T3 Summary: 5 PASS / 15 FAIL**

---

## Tier 4 Results

| Scene | Result | Errors | Notes |
|-------|--------|--------|-------|
| SC01  | FAIL   | CHAR_MISSING, CHAR_DRIFT | Ellis absent. Benny rendered as a small stuffed prop held by Layla. Layla has STRAIGHT BLACK hair (not wavy/curly) — CHAR_DRIFT. Riley has SINGLE bow/pigtail visible — CHAR_DRIFT. Style is semi-realistic digital painting. |
| SC02  | FAIL   | CHAR_DRIFT | Layla has STRAIGHT BLACK hair (not wavy/curly) — CHAR_DRIFT. Riley ✓ (two bows visible). Ellis wearing PLAID SHIRT — CLOTH_DRIFT. Benny ✓. Blueprint mostly blank. |
| SC03  | FAIL   | CHAR_DRIFT, BUBBLE | Layla ✓ (curly, yellow bow). Riley has STRAIGHT black hair, ONE PINK BOW — CHAR_DRIFT (no pigtails, hair completely straight). Ellis wearing blue-red sports shirt (acceptable). Benny ✓. Blueprint shows extensive measurement labels, dimension callouts, text annotations — BUBBLE (severe). |
| SC04  | FAIL   | CHAR_DRIFT | Layla ✓ (curly, yellow bow). Riley has two BUNS (not pigtails, two pink bows on buns) — CHAR_DRIFT. Ellis (plaid — CLOTH_DRIFT). Benny ✓. No blueprint text. |
| SC05  | FAIL   | CHAR_DRIFT | Ellis wearing blue-orange jersey (CLOTH_DRIFT). Layla has straight hair (CHAR_DRIFT). Riley (straight-ish black hair, two bows — marginal). Benny ✓. No text. |
| SC06  | FAIL   | CHAR_EXTRA, CHAR_MISSING, STYLE_DRIFT | Scene shows only adult HANDS reaching into frame (headless adult) — CHAR_EXTRA (unidentified adult). Layla ✓, Riley ✓, Ellis (no bow, not matching character fully). Benny = stuffed toy prop. Style is photo-realistic painting. Blueprint on table has faint line boxes, barely legible. |
| SC07  | FAIL   | WRONG_ELDERLY, CHAR_MISSING | Scene shows elderly man with neat GREY COMBED HAIR, DARK BEARD, no spiky hair, no goggles, wearing apron — wrong identity for Maestro Gearsmith. Riley alone with this wrong adult. Layla/Ellis/Benny absent. Blueprint reads "SCALE DRAWING — 1:10 RATIO" — BUBBLE. |
| SC08  | FAIL   | CHAR_DRIFT | Riley has STRAIGHT black hair with NO BOWS — CHAR_DRIFT (FAIL: missing both bows and pigtails). Layla ✓ (curly, yellow bow). Ellis wearing red-white striped shirt — CLOTH_DRIFT. Benny ✓. No blueprint text. |
| SC09  | FAIL   | CHAR_DRIFT, BUBBLE | Layla ✓, Riley ✓ (two bows, pigtails), Ellis wearing blue-red jersey (acceptable). Benny ✓. Blueprint being handed over — paper has grid lines. Scene is fine except CHAR_DRIFT: Ellis in non-standard jersey. Disembodied hand passing paper adds to CHAR_EXTRA flag. |
| SC10  | FAIL   | BUBBLE | Layla solo. Yellow bow ✓, curly hair ✓, teal hoodie ✓. Blueprint on table shows "String", "Spring", "Housing" labels and dimension measurements — BUBBLE (severe). |
| SC11  | FAIL   | MULTI_PANEL, STYLE_DRIFT, BUBBLE | TWO-PANEL split image of the same blonde boy at two angles — MULTI_PANEL. Style is photo-realistic oil painting (not cartoon). Layla/Riley/Benny all absent. Blueprint/paper shows text: "BASE: 10" x 12"", "SUPPORT BEAMS (4)", "GRAIN DIRECTION FOR STRENGTH", "1" x 10"" — BUBBLE (severe). STYLE_DRIFT (hyper-realistic). |
| SC12  | FAIL   | CHAR_DRIFT, BUBBLE | Riley has STRAIGHT BLACK hair, ONE PINK BOW on headband — CHAR_DRIFT (no pigtails). Blueprint shows "11 IN", "8.5 IN" measurement labels — BUBBLE. |
| SC13  | FAIL   | BUBBLE | Benny solo. Benny ✓ (correct green plaid scarf). Blueprint on table shows extensive text: "DISTRIBUTE FORCE", "FOUR CLIPS = STRONGER", "BUY: 4 + 1 SPARE = 5 CLIPS", "COST PLANNING", "6 INCHES APART", "1 INCH FROM SIDE" — BUBBLE (very severe). Separate document reads "COST ESTIMATE". |
| SC14  | FAIL   | WRONG_ELDERLY | "Maestro" rendered as elderly man in WHITE LAB COAT, no spiky hair, no goggles, no leather apron — WRONG_ELDERLY. Layla ✓ (yellow bow, teal hoodie), Riley ✓ (two bows), Ellis (plaid shirt — CLOTH_DRIFT). Benny ✓. No blueprint text visible. |
| SC15  | FAIL   | WRONG_ELDERLY, CHAR_EXTRA | "Maestro" rendered as young adult WOMAN with dark upswept hair, tan apron — wrong gender, wrong age, wrong specs. WRONG_ELDERLY + CHAR_EXTRA. Layla ✓ (yellow bow, teal hoodie), Riley ✓ (single bow on pigtail — marginal). Ellis present (plaid — CLOTH_DRIFT). Benny ✓. |
| SC16  | FAIL   | CHAR_DRIFT, CHAR_MISSING | Riley has STRAIGHT BLACK hair, ONE PINK BOW on headband (no pigtails) — CHAR_DRIFT. Layla absent. Ellis ✓. Benny absent. Scene is just Riley + Ellis at drafting table. Blueprint has architectural floor plans visible, no readable text labels. |
| SC17  | FAIL   | WRONG_ELDERLY, CHAR_MISSING, CHAR_EXTRA | Scene shows older man with NEAT GREY HAIR, ROUND GLASSES, NO GOGGLES, NO SPIKY HAIR, NO LEATHER APRON — matches MR. MASON description more than Maestro Gearsmith. Two children present with BROWN/DARK HAIR (neither Layla nor Riley identifiable). CHAR_EXTRA/CHAR_MISSING. Benny present. Blueprint table with detailed architectural drawings — no legible text. |
| SC18  | FAIL   | WRONG_ELDERLY, CHAR_DRIFT | "Maestro" renders as elderly man with white/grey MESSY (but not truly spiky) hair, wearing vest/waistcoat — goggles visible being lifted to head but placement/style differs from reference. Layla has STRAIGHT dark hair (CHAR_DRIFT). Riley visible. Ellis is brown-haired boy in blue soccer kit — CHAR_DRIFT. Benny ✓. |
| SC19  | FAIL   | CHAR_DRIFT, CHAR_MISSING | Riley has STRAIGHT BLACK hair, ONE bow — CHAR_DRIFT. Layla absent. Ellis ✓ (blue-red jersey). Benny ✓. Night scene. Blueprint rolls visible but blank. |
| SC20  | PASS   | —      | Layla ✓ (curly, yellow bow, teal hoodie), Riley ✓ (two bows, pigtails), Ellis (red-white striped — CLOTH_DRIFT minor but recognisable), Benny ✓ (green scarf). Night walk. Blueprint rolls visible, no text. Best T4 image. |

**T4 Summary: 3 PASS / 17 FAIL**

---

## Priority Flags

Ranked by severity. Immediate re-generation required.

| File | Errors | Issue |
|------|--------|-------|
| S3-CH09-SC11-tier4.png | MULTI_PANEL, STYLE_DRIFT, BUBBLE | Split two-panel hyper-realistic painting of same boy. Blueprint has full engineering text annotations. Complete rebuild required. |
| S3-CH09-SC13-tier4.png | BUBBLE | Benny-only scene. Blueprint covered in engineering text: "DISTRIBUTE FORCE", "COST PLANNING", "6 INCHES APART", "BUY: 4+1 SPARE=5 CLIPS", "COST ESTIMATE" — most severe text leakage in chapter. |
| S3-CH09-SC10-tier4.png | BUBBLE | Layla solo. Blueprint shows "String", "Spring", "Housing" labels with dimension measurements. |
| S3-CH09-SC07-tier4.png | WRONG_ELDERLY, BUBBLE | Wrong adult (grey-haired bearded man, no goggles). Blueprint reads "SCALE DRAWING — 1:10 RATIO". |
| S3-CH09-SC05-tier3.png | CHAR_DRIFT, BUBBLE | Benny in green overalls/red bow tie (wrong costume). Blueprint shows "SCALE: 1 INCH = 1 UNIT" and "8 INCH RETRACTABLE STRING" in full text. |
| S3-CH09-SC12-tier3.png | CHAR_DRIFT, BUBBLE | Riley has single bow on headband, straight hair (not pigtails). Blueprint shows "Elastic band", "8½ inches", "11 inches". |
| S3-CH09-SC12-tier4.png | CHAR_DRIFT, BUBBLE | Riley single bow, straight hair. Blueprint shows "11 IN", "8.5 IN" measurements. |
| S3-CH09-SC16-tier3.png | BUBBLE | All four characters otherwise correct. Blueprints on table and wall show extensive dimensional callout text — most saturated text scene in T3. |
| S3-CH09-SC17-tier3.png | WRONG_ELDERLY, BUBBLE | Elderly man resembles Mr. Mason (grey combed hair, glasses, green vest). Bridge blueprint with annotation marks. |
| S3-CH09-SC11-tier3.png | BUBBLE | Ellis solo. Blueprint shows "23 In", "34 In" measurement labels. |
| S3-CH09-SC03-tier4.png | CHAR_DRIFT, BUBBLE | Riley straight hair / single bow. Blueprint saturated with measurement annotations. |
| S3-CH09-SC07-tier3.png | WRONG_ELDERLY | Maestro replaced by elderly WOMAN in tweed jacket with grey bun and glasses. Complete character swap. |
| S3-CH09-SC15-tier1.png | WRONG_ELDERLY, BUBBLE | Maestro replaced by young adult woman with goggles. "PLANNING" / "LESS WASTE." text on blueprint. |
| S3-CH09-SC17-tier4.png | WRONG_ELDERLY, CHAR_MISSING, CHAR_EXTRA | Two unidentified dark-haired children + Mr. Mason-like figure. Layla/Ellis not present. |
| S3-CH09-SC18-tier1.png | WRONG_ELDERLY | Maestro in white lab coat (no spiky hair, no goggles). |
| S3-CH09-SC15-tier4.png | WRONG_ELDERLY, CHAR_EXTRA | Maestro replaced by young adult woman in apron. |
| S3-CH09-SC14-tier4.png | WRONG_ELDERLY | Maestro in white lab coat again. No spiky hair, no goggles. |
| S3-CH09-SC15-tier2.png | WRONG_ELDERLY, BUBBLE | Young bearded man (no goggles). Blueprint reads "PROJECT PLAN". |
| S3-CH09-SC07-tier2.png | WRONG_ELDERLY | Young bearded man in ~30s replaces Maestro. |
| S3-CH09-SC18-tier4.png | WRONG_ELDERLY | Partial goggles visible but hair not truly spiky; Layla and Ellis show CHAR_DRIFT. |

---

## Character-Specific Failure Summary

### Layla
- T1: Generally good. Hair and bow consistent.
- T2: Loses bow in SC06; straight hair in SC05.
- T3: Straight hair in SC01, SC19 (FAIL); curly/bow correct in SC06, SC13, SC20.
- T4: Straight hair in SC01, SC02, SC05 (FAIL across multiple). Mostly absent in later T4 scenes.

### Riley
- T1: Very good. Two bows/pigtails consistent across most scenes.
- T2: SC04 — single bow visible (marginal). Generally passes.
- T3: SC02 no bows (FAIL); SC07/SC12 single bow (FAIL); SC01 two bows ✓.
- T4: Straight hair with single bow in SC01, SC03, SC08, SC12, SC16, SC19 (FAIL). Two bows in SC04, SC14 only.

### Ellis
- T1: Absent in SC01. Correct in most other scenes where present. Soccer shirt ✓.
- T2: Absent in SC01-SC06. Where present wears orange-black jersey (CLOTH_DRIFT). Never fully correct jersey in T2.
- T3: Appears more but dark-haired in SC03 (FAIL). Plaid shirt common (CLOTH_DRIFT).
- T4: Plaid or sports-stripe shirts throughout (CLOTH_DRIFT). Absent in many scenes.

### Benny
- T1: Correct animated cartoon bear throughout. Green plaid scarf ✓.
- T2: Often rendered as stuffed toy/prop rather than animated bear (CHAR_DRIFT in SC01, SC03, SC05).
- T3: SC05 has green overalls + red bow tie (CHAR_DRIFT). Mostly ✓ otherwise.
- T4: Stuffed toy prop in SC01, SC06. Otherwise ✓.

### Maestro Gearsmith
- Correct appearance: Appears in SC15-T1 (female — FAIL), SC18-T1 (lab coat — FAIL), SC07-T2 (bearded young man — FAIL), SC15-T2 (bearded young man — FAIL), SC07-T3 (elderly woman — FAIL), SC09-T3 (bearded man — FAIL), SC17-T3 (Mr. Mason-like — FAIL), SC07-T4 (bearded grey man — FAIL), SC14-T4 (lab coat — FAIL), SC15-T4 (young woman — FAIL), SC17-T4 (Mr. Mason-like — FAIL), SC18-T4 (partial/marginal — FAIL).
- **0 clean Maestro Gearsmith passes** across all 80 images. Every Maestro scene fails the character spec.

---

## Notes on Maestro Gearsmith Absence
Maestro Gearsmith should appear in scenes where an adult instructor/inventor is depicted. In ALL such scenes across all tiers, the character fails: the model is consistently generating wrong elderly figures (women with buns, bearded men in their 30s, lab-coat scientists, or Mr. Mason look-alikes). The spiky white hair + brass goggles on forehead + leather apron combination is never achieved. This is the single most critical systemic failure in Ch09.

---

*Report generated by visual QA audit of 80 images across 4 tiers × 20 scenes.*
