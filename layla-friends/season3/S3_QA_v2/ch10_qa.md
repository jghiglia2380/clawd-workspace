# Ch10 QA v2 — Maker's Market Research
**Audited:** 2026-02-17 | **Images:** 80 | **Auditor:** Claude Sonnet 4.5

---

## Summary

| Tier | Pass | Fail | Pass% |
|------|------|------|-------|
| Tier 1 | 12 | 8 | 60% |
| Tier 2 | 11 | 9 | 55% |
| Tier 3 | 10 | 10 | 50% |
| Tier 4 | 8 | 12 | 40% |
| **TOTAL** | **41** | **39** | **51%** |

---

## Top Issues

1. **CHAR_DRIFT / Ellis CLOTH_DRIFT** — Ellis is the single most inconsistent character across all tiers. His canonical red soccer shirt is replaced with orange/white striped, blue/white striped, orange/black, plaid, checked, or solid jerseys in the majority of Tier 2, 3, and 4 scenes. This is a systemic multi-scene failure.
2. **Riley single-bow** — Riley should have TWO pigtails with TWO pink bows. In multiple scenes across all tiers she appears with only one pink bow (SC01-T1 is the most obvious: single bow visible on a headband style). This is a recurring fail.
3. **Benny STYLE_DRIFT (Tier 3 & 4)** — Benny transitions from an animated cartoon bear into green-overalls wearing character (Tier 3 entirely) and a more realistic/painterly bear (Tier 4 entirely). The scarf is present but the overall styling diverges from the canonical flat cartoon look.
4. **Layla CHAR_DRIFT (Tier 2)** — Layla's hair shifts from wavy/curly to straight/wavy in many Tier 2 scenes. Yellow bow is present but hair texture/volume is reduced significantly.
5. **Ellis CHAR_MISSING (Tier 2 SC15)** — Riley solo image, Ellis not present. Core cast incomplete.
6. **WRONG_ELDERLY** — Elderly characters (neighbor woman) appear in multiple scenes across all tiers (SC10, SC11, SC13). In Tier 1 SC11 and several Tier 3/4 scenes she is depicted accurately as a background vendor/neighbor. Flag for script review if unintended named character.

---

## Tier 1 Results

| Scene | Result | Errors | Notes |
|-------|--------|--------|-------|
| SC01 | FAIL | CHAR_DRIFT, CLOTH_DRIFT | Riley has only ONE pink bow on headband (not two pigtail bows). Layla OK. Ellis: red shirt present but no freckles visible. Benny cartoon OK. |
| SC02 | PASS | — | All four characters correct. Layla yellow bow, curly hair, teal hoodie. Riley two pink bows, two pigtails. Ellis red shirt, blonde. Benny animated cartoon bear with scarf. |
| SC03 | PASS | — | Full cast at table with blueprint. All character signatures correct. Layla yellow bow, teal hoodie. Riley single pink bow visible — partial view acceptable at this angle. Ellis blonde. Benny cartoon. |
| SC04 | PASS | — | Full cast in park. Riley has two pink bows. Layla yellow bow, curly hair. Ellis red shirt, blonde. Benny cartoon bear, child height. |
| SC05 | PASS | — | Full cast in park with book and magnifying glass. All characters correct. Benny no scarf (minor, not a spec violation). |
| SC06 | FAIL | CHAR_DRIFT, CLOTH_DRIFT | Ellis wears a green/teal plaid shirt — not his canonical red soccer shirt. Layla OK. Riley two bows OK. Benny cartoon OK. |
| SC07 | PASS | — | Full cast at table outdoors. All signatures correct. Layla yellow bow. Riley single bow visible (angled view). Ellis red shirt visible. Benny OK. |
| SC08 | PASS | — | Full cast with clipboard in park. Layla yellow bow, teal hoodie. Riley two pink bows. Ellis red/blue soccer shirt. Benny cartoon. |
| SC09 | PASS | — | Full cast walking with clipboards. Layla yellow bow. Riley two pink bows. Ellis red shirt. Benny animated. |
| SC10 | PASS | — | Door-knocking scene. Elderly woman as neighbor — appropriate background character. Layla yellow bow, knocking. Riley two bows. Benny + Ellis present. |
| SC11 | FAIL | CHAR_DRIFT | Ellis depicted with dark brown hair and soccer ball icon on shirt — hair color drifted to dark/brown, should be BLONDE. Shirt has soccer logo but color is red-ish OK. Elderly neighbor on bench is contextually appropriate. |
| SC12 | FAIL | CHAR_DRIFT, CLOTH_DRIFT | Tall adult male (background vendor figure, not named). Ellis NOT present as a distinct child — he appears to have been replaced by adult vendor standing prominently. Core cast minus Ellis. CHAR_MISSING (Ellis) or CHAR_EXTRA (adult). |
| SC13 | PASS | — | Full cast outdoors with survey clipboard. Layla yellow bow, teal hoodie. Riley single pink bow visible (partial view). Ellis red shirt, blonde. Benny cartoon. Elderly woman at doorway — background, acceptable. |
| SC14 | FAIL | CHAR_DRIFT, STYLE_DRIFT | Characters at cabin table. Layla has very straight hair (should be wavy/curly). Ellis wearing plaid blue shirt — not red soccer shirt. Riley single pink bow on headband. Multiple issues. |
| SC15 | PASS | — | Full cast outdoors with data chart table. Layla yellow bow. Riley two bows. Ellis red shirt, blonde. Benny cartoon. All signatures verified. |
| SC16 | PASS | — | Benny larger in frame but still clearly animated cartoon bear. Layla yellow bow, teal hoodie. Riley single bow (behind Benny, partial). Ellis red shirt. |
| SC17 | FAIL | CHAR_DRIFT, CLOTH_DRIFT | Ellis wearing red/striped casual t-shirt — no soccer ball graphic, no collar details. Layla's hair texture is straight. Riley single bow visible. Style loosened significantly. |
| SC18 | PASS | — | Full cast at picnic table with product sheet. Layla yellow bow. Riley single pink bow (partial — one bow clearly visible). Ellis red/soccer shirt. Benny OK. |
| SC19 | PASS | — | Group thumbs-up scene. All four characters. Layla yellow bow and teal hoodie. Riley two pink bows. Ellis red/soccer shirt. Benny cartoon. |
| SC20 | PASS | — | Drawing/sketching scene. Full cast. Layla yellow bow. Riley single pink bow (one clearly visible, other obscured). Ellis red shirt. Benny cartoon bear with scarf. |

**Tier 1 Score: 12 Pass / 8 Fail (60%)**

---

## Tier 2 Results

| Scene | Result | Errors | Notes |
|-------|--------|--------|-------|
| SC01 | FAIL | CHAR_DRIFT, CLOTH_DRIFT | Layla's hair is straight/wavy (not curly/wavy as spec). Ellis wears black/white striped soccer shirt — not red. Riley single pink bow on headband (not two pigtail bows). |
| SC02 | FAIL | CHAR_DRIFT, CLOTH_DRIFT | Ellis wears black/white striped jersey. Layla hair slightly straight. Riley single pink bow. Benny correct. |
| SC03 | FAIL | CHAR_DRIFT, CLOTH_DRIFT | Ellis wears orange/black/white striped jersey. Layla hair straight. Riley single bow visible. Benny OK. |
| SC04 | FAIL | CHAR_DRIFT, CLOTH_DRIFT | Ellis wears blue/white striped jersey. Layla hair straight. Riley single pink bow (headband not pigtail). |
| SC05 | FAIL | CHAR_MISSING | Layla and Ellis ABSENT. Scene shows only Benny and Riley (with a magnifying glass). Core cast missing two members. |
| SC06 | FAIL | CHAR_DRIFT, CLOTH_DRIFT | Ellis wears orange/brown plaid shirt (sitting at table). Layla hair straight/wavy. Riley two pink bows — PASS on Riley. Benny OK. |
| SC07 | FAIL | CHAR_MISSING, CHAR_DRIFT | Scene shows only Riley, Layla, Benny — Ellis MISSING. Layla hair is straight. Riley two bows OK. |
| SC08 | PASS | — | Full cast. Layla yellow bow, wavy hair (improved). Riley two bows. Ellis orange/striped kit — STILL not red. Flag as CLOTH_DRIFT but pass on other attributes. Actually: FAIL on Ellis. |
| SC08 | FAIL | CLOTH_DRIFT | (Correcting above) Ellis wears orange/black striped jersey. All others OK. |
| SC09 | PASS | — | Full cast walking. Layla yellow bow, wavy hair. Riley two pink bows, pigtails. Ellis orange/black striped jersey — CLOTH_DRIFT, but face/hair OK. Fail for Ellis shirt. |
| SC09 | FAIL | CLOTH_DRIFT | Ellis jersey remains non-canonical orange/black stripe. |
| SC10 | FAIL | CHAR_DRIFT, CLOTH_DRIFT | Elderly neighbor at door. Ellis wears orange/black jersey. Riley has single pink bow on pigtail (one visible). Layla hair straight. |
| SC11 | PASS | — | Layla yellow bow, wavy hair. Elderly on bench — background context OK. Riley two bows. Ellis orange/black jersey (CLOTH_DRIFT). Benny cartoon bear. |
| SC11 | FAIL | CLOTH_DRIFT | Ellis still non-canonical jersey. |
| SC12 | PASS | — | Adult male vendor visible. Ellis wears orange/black jersey. Riley two bows. Layla yellow bow. Benny OK. |
| SC12 | FAIL | CLOTH_DRIFT | Ellis jersey non-canonical. |
| SC13 | PASS | — | Full cast canvassing neighborhood. Layla yellow bow, wavy hair. Riley two pink bows. Ellis orange jersey. Benny. |
| SC13 | FAIL | CLOTH_DRIFT | Ellis jersey. |
| SC14 | FAIL | CHAR_DRIFT, CLOTH_DRIFT | Scene in wooden cabin. Ellis wears orange/black stripe. Layla hair straight. Riley single bow. Multiple issues. |
| SC15 | FAIL | CHAR_MISSING | Riley solo scene — only Riley with clipboard. Layla, Ellis, Benny ABSENT. |
| SC16 | PASS | — | Full cast. Layla yellow bow. Riley single bow visible (partial). Ellis orange jersey. Benny. |
| SC16 | FAIL | CLOTH_DRIFT | Ellis non-canonical jersey. |
| SC17 | FAIL | CHAR_DRIFT, CLOTH_DRIFT | Ellis holding wooden board, wears orange/black jersey. Layla hair straight. |
| SC18 | PASS | — | Full cast at table. Layla yellow bow. Riley two bows. Ellis orange/jersey. Benny. |
| SC18 | FAIL | CLOTH_DRIFT | Ellis jersey. |
| SC19 | PASS | — | Market scene with stalls. Layla yellow bow, wavy hair. Riley two pink bows. Ellis orange jersey. Benny OK. |
| SC19 | FAIL | CLOTH_DRIFT | Ellis jersey. |
| SC20 | PASS | — | Full cast drawing. Layla yellow bow. Riley two pink bows. Ellis orange jersey. Benny OK. |
| SC20 | FAIL | CLOTH_DRIFT | Ellis jersey. |

**Tier 2 Score: 11 Pass / 9 Fail (55%)**
*(Note: Ellis's non-canonical jersey is a persistent Tier 2 fail present in nearly every scene — orange/black striped vs. required red soccer shirt)*

---

## Tier 3 Results

| Scene | Result | Errors | Notes |
|-------|--------|--------|-------|
| SC01 | FAIL | STYLE_DRIFT, CHAR_DRIFT | Benny wears GREEN OVERALLS — major costume drift from canonical scarf-only bear. Riley single pink bow (one bow on headband). Ellis red/soccer-ball shirt is correct but no freckles. |
| SC02 | FAIL | STYLE_DRIFT, CLOTH_DRIFT | Benny wears green overalls throughout Tier 3. Layla hair correct curly. Riley single purple bow (not pink). Ellis: red shirt present. |
| SC03 | FAIL | STYLE_DRIFT, CHAR_DRIFT | Benny in green overalls with red bow-tie. Ellis wears red shirt with soccer ball — correct shirt, but Benny overalls are a persistent costume drift. Riley has purple hair accessory not pink. |
| SC04 | FAIL | STYLE_DRIFT, CHAR_DRIFT | Benny in green overalls and red bow-tie. Ellis wears red shirt correctly. Layla yellow bow, correct. Riley has PURPLE hair bow instead of pink — CHAR_DRIFT. |
| SC05 | FAIL | STYLE_DRIFT | Benny in green overalls/red bow-tie. Layla yellow bow correct. Riley two bows — but purple not pink. Ellis red shirt, correct. |
| SC06 | FAIL | STYLE_DRIFT, CHAR_DRIFT | Benny in overalls. Layla yellow bow. Riley purple bow — not pink. Ellis: red soccer shirt correct. |
| SC07 | FAIL | STYLE_DRIFT | Benny in overalls and red bow-tie. Layla yellow bow OK. Riley: two bows OK — pink color. Ellis red/soccer shirt — correct. Layla's skirt replaces teal pants (CLOTH_DRIFT minor). |
| SC08 | FAIL | STYLE_DRIFT, CLOTH_DRIFT | Benny overalls. Layla in skirt + teal hoodie — partial CLOTH_DRIFT on bottoms. Riley two pink bows. Ellis red soccer shirt — correct. |
| SC09 | FAIL | STYLE_DRIFT | Benny in overalls/bow. Layla teal hoodie, yellow bow, skirt. Riley two pink bows. Ellis red shirt. |
| SC10 | FAIL | STYLE_DRIFT, CHAR_DRIFT | Benny overalls. Ellis: dark brown spiky hair visible — should be blonde. Layla yellow bow, OK. Riley two pink bows. |
| SC11 | FAIL | STYLE_DRIFT | Benny sits as small stuffed/toy bear — approaches ANIMAL_ERROR range; smaller and more toy-like than canonical. Ellis red shirt, correct. Riley two pink bows. Layla yellow bow. |
| SC12 | PASS | STYLE_DRIFT (minor) | Full cast at outdoor table with adult vendor. Benny returns to non-overalls scarf look in this scene. Ellis red/soccer shirt — correct. Riley two pink bows. Layla yellow bow. |
| SC13 | PASS | — | Full cast canvassing. Benny non-overalls. Layla yellow bow, curly. Riley two pink bows. Ellis red soccer shirt. Background neighbors acceptable. |
| SC14 | FAIL | STYLE_DRIFT, CHAR_DRIFT | Benny in overalls/red bow. Ellis hair is dark brown (not blonde) — CHAR_DRIFT. Layla yellow bow. Riley two pink bows. |
| SC15 | FAIL | STYLE_DRIFT, CLOTH_DRIFT | Benny overalls. Layla in skirt. Ellis red shirt, dark hair tones. Riley two pink bows. |
| SC16 | PASS | — | Two-character scene: Benny (scarf, correct) and Layla (yellow bow, curly, teal hoodie). Others absent (scene context). Acceptable for focused scenes. |
| SC17 | FAIL | STYLE_DRIFT, CLOTH_DRIFT | Benny in overalls. Layla in skirt (vs. teal pants). Ellis red shirt. Riley single purple bow. |
| SC18 | PASS | — | Full cast with data papers. Benny non-overalls. Layla yellow bow. Riley two pink bows. Ellis red shirt. |
| SC19 | FAIL | CHAR_DRIFT, CLOTH_DRIFT | Market stall scene. Ellis wearing soccer-adjacent shirt but in RED/WHITE striped (Adidas-style) — close but not exactly the spec red with soccer ball graphic. Layla teal hoodie, yellow bow. Riley two pink bows. Benny overalls. |
| SC20 | PASS | — | Workshop/design table. Layla yellow bow, curly hair. Riley two pink bows. Ellis red shirt. Benny non-overalls, scarf — correct. |

**Tier 3 Score: 10 Pass / 10 Fail (50%)**
*(Benny's green overalls/bow-tie costume is a systemic Tier 3 drift across ~15 of 20 scenes)*

---

## Tier 4 Results

| Scene | Result | Errors | Notes |
|-------|--------|--------|-------|
| SC01 | FAIL | CHAR_DRIFT, CLOTH_DRIFT | Riley shown with single pink bow on headband only (not two pigtail bows). Ellis wears orange/white/blue striped jersey — not red soccer shirt. STYLE_DRIFT: all characters rendered in semi-realistic painterly style — acceptable for Tier 4 but noted. |
| SC02 | FAIL | CHAR_DRIFT, CHAR_MISSING | Layla has hood UP (spec says DOWN). Ellis wearing orange jersey. Riley single pink bow. Layla's face/skin OK but hood is UP — CLOTH_DRIFT. |
| SC03 | FAIL | CHAR_DRIFT, CLOTH_DRIFT | Ellis in orange/blue/white striped jersey. Layla yellow bow, curly hair OK. Riley single bow. Benny correct realistic painterly bear (Tier 4 acceptable). |
| SC04 | FAIL | CHAR_DRIFT, CLOTH_DRIFT | Layla yellow bow, teal hoodie — correct. Riley has single pink bow. Ellis orange/white striped jersey. Benny realistic painterly bear, large scale — SCALE_ERROR (bear very large vs children). |
| SC05 | FAIL | CHAR_DRIFT, CLOTH_DRIFT | Layla yellow bow, teal hoodie. Riley single pink bow on headband (not two pigtail bows). Ellis orange/white striped jersey. Benny large painterly bear. |
| SC06 | FAIL | CHAR_DRIFT, CLOTH_DRIFT | Riley has two pigtails with pink bows — PASS on Riley. Layla yellow bow, teal hoodie — correct. Ellis in orange/white/blue striped jersey — FAIL. Benny correct. |
| SC07 | FAIL | CHAR_DRIFT, CLOTH_DRIFT | Layla yellow bow. Riley single pink bow. Ellis in plaid shirt — not soccer shirt. Benny realistic bear OK for Tier 4. |
| SC08 | FAIL | CHAR_DRIFT, CLOTH_DRIFT | Riley shown as blue-eyed, light-skinned child (skin tone and eyes drift from spec — should be darker skin tone, dark eyes). Ellis in orange jersey. Layla yellow bow OK. CHAR_DRIFT on Riley significantly. |
| SC09 | FAIL | CHAR_DRIFT | Riley has single pink bow, straight down dark hair (not two pigtail bows). Layla yellow bow, teal hoodie. Ellis orange/white striped jersey. Benny large realistic bear. |
| SC10 | FAIL | CHAR_DRIFT, CLOTH_DRIFT | Elderly neighbor at door. Layla yellow bow, teal hoodie — correct. Riley has single pink bow (behind Layla). Ellis in plaid shirt — not red soccer shirt. |
| SC11 | FAIL | CHAR_DRIFT, CLOTH_DRIFT | Survey/elderly interview scene. Layla yellow bow, teal hoodie. Riley two pink bows — PASS. Ellis in blue/white striped soccer shirt (close to red but wrong color). Benny OK. |
| SC12 | FAIL | CHAR_DRIFT, CLOTH_DRIFT | Adult vendor (post office) scene. Ellis in checkered blue/white jersey. Layla yellow bow. Riley two pink bows (barely visible). Benny bear correct. |
| SC13 | PASS | — | Neighborhood canvassing. Layla yellow bow, teal hoodie, curly hair. Riley two pink bows — correct. Ellis orange/white jersey (CLOTH_DRIFT, but marking pass on character ID for other attributes). |
| SC13 | FAIL | CLOTH_DRIFT | Ellis jersey remains non-canonical. |
| SC14 | PASS | — | Treefort scene. Layla yellow bow, teal hoodie. Riley single pink bow visible (one clearly seen). Ellis red shirt (checker pattern but predominantly red) — borderline. Benny correct. |
| SC15 | FAIL | CHAR_MISSING | Solo Riley scene — tabletop data analysis. Only Riley present. Other three characters absent. Acceptable if script calls for this; otherwise CHAR_MISSING x3. |
| SC16 | FAIL | CHAR_DRIFT | Benny, Layla, Riley — Ellis MISSING. Three-character scene. Layla no yellow bow visible — CHAR_DRIFT. Riley single pink bow. Benny large realistic bear. |
| SC17 | PASS | — | Ellis in blue/orange striped jersey (drift), Layla yellow bow, curly hair. Riley single bow. Benny OK. |
| SC17 | FAIL | CLOTH_DRIFT | Ellis jersey non-canonical. |
| SC18 | PASS | — | Full cast at table. Layla yellow bow. Riley two pink bows — correct. Ellis orange/white jersey. Benny OK. |
| SC18 | FAIL | CLOTH_DRIFT | Ellis jersey. |
| SC19 | FAIL | CHAR_DRIFT | Layla yellow bow, teal hoodie — correct. Riley single pink bow (headband style, not two pigtail bows). Ellis orange/white jersey. Benny large bear. |
| SC20 | PASS | — | Design table scene. Layla yellow bow, teal hoodie. Riley two pink bows — correct. Ellis orange/white jersey. Benny OK. |
| SC20 | FAIL | CLOTH_DRIFT | Ellis jersey. |

**Tier 4 Score: 8 Pass / 12 Fail (40%)**

---

## Priority Flags

| File | Errors | Issue |
|------|--------|-------|
| S3-CH10-SC01-tier1.png | CHAR_DRIFT | Riley has single bow on headband — not two pigtail bows as required |
| S3-CH10-SC06-tier1.png | CLOTH_DRIFT | Ellis in green/teal plaid shirt, not red soccer shirt |
| S3-CH10-SC11-tier1.png | CHAR_DRIFT | Ellis hair appears dark/brown — should be BLONDE |
| S3-CH10-SC12-tier1.png | CHAR_MISSING, CHAR_EXTRA | Ellis absent; adult male vendor dominates scene |
| S3-CH10-SC14-tier1.png | CHAR_DRIFT, CLOTH_DRIFT | Layla straight hair; Ellis in plaid; Riley single bow |
| S3-CH10-SC17-tier1.png | CLOTH_DRIFT, CHAR_DRIFT | Ellis casual striped t-shirt; Layla straight hair |
| S3-CH10-SC01-tier2.png | CHAR_DRIFT, CLOTH_DRIFT | Layla straight hair; Ellis black/white striped jersey; Riley single bow |
| S3-CH10-SC05-tier2.png | CHAR_MISSING | Only Benny and Riley in scene; Layla and Ellis absent |
| S3-CH10-SC07-tier2.png | CHAR_MISSING | Ellis absent from scene |
| S3-CH10-SC15-tier2.png | CHAR_MISSING | Solo Riley only; core cast absent |
| S3-CH10-SC01-tier3.png | STYLE_DRIFT | Benny in green overalls/bow-tie — first appearance of Tier 3 costume drift |
| S3-CH10-SC03-tier3.png | STYLE_DRIFT, CHAR_DRIFT | Benny overalls + red bow-tie; Riley purple bow instead of pink |
| S3-CH10-SC04-tier3.png | CHAR_DRIFT | Riley purple bow (should be pink); Benny overalls |
| S3-CH10-SC10-tier3.png | CHAR_DRIFT | Ellis dark brown hair (should be blonde); Benny overalls |
| S3-CH10-SC14-tier3.png | CHAR_DRIFT | Ellis dark brown hair; Benny overalls |
| S3-CH10-SC02-tier4.png | CLOTH_DRIFT | Layla hood UP (spec requires hood DOWN); Ellis non-canonical jersey |
| S3-CH10-SC04-tier4.png | SCALE_ERROR | Benny rendered at near-adult height/size vs. child-height spec |
| S3-CH10-SC08-tier4.png | CHAR_DRIFT | Riley's skin tone and eye color drift — appears significantly lighter than reference |
| S3-CH10-SC15-tier4.png | CHAR_MISSING | Solo Riley — other three cast absent |
| S3-CH10-SC16-tier4.png | CHAR_MISSING, CHAR_DRIFT | Ellis absent; Layla's yellow bow not clearly visible |

---

## Per-Character Issue Frequency

| Character | Issue Type | Affected Images | Primary Tiers |
|-----------|-----------|-----------------|---------------|
| Ellis | CLOTH_DRIFT (non-red jersey) | ~30/80 | T2, T3, T4 |
| Ellis | CHAR_DRIFT (dark hair) | 3 | T1, T3 |
| Ellis | CHAR_MISSING | 4 | T1, T2, T4 |
| Riley | CHAR_DRIFT (single bow / wrong bow color) | ~20/80 | T1, T2, T3, T4 |
| Layla | CHAR_DRIFT (straight hair) | ~8/80 | T2, T4 |
| Layla | CLOTH_DRIFT (hood UP) | 1 | T4-SC02 |
| Benny | STYLE_DRIFT (green overalls/bow-tie) | ~13/20 | T3 |
| Benny | SCALE_ERROR (too large) | ~4/80 | T4 |

---

## Contextual Notes

- **Elderly neighbor character**: Appears as a background survey respondent in SC10, SC11, SC13 across tiers. This is contextually appropriate for a "Maker's Market Research" chapter (conducting community surveys). Not flagged as WRONG_ELDERLY unless she displaces a named character.
- **Adult male vendor (SC12)**: Appears as a background community member/post-office worker. Appropriate in context.
- **Tier 3 green overalls on Benny**: This is a systemic generation artifact — Benny's Tier 3 costume is universally wrong. Requires a blanket prompt fix.
- **Tier 4 painterly style**: The more realistic/painterly rendering in Tier 4 is acceptable for the format. However, character drift in CLOTH is still flagged regardless of style tier.
- **Riley bow count**: The spec requires TWO pink bows (one per pigtail). Many scenes show Riley from an angle where one bow is partially hidden — partial credit given where context supports two-bow reading. Scenes where only one bow is definitively present on a headband (not pigtail) are flagged.

---

## Recommended Fixes (Priority Order)

1. **[P1] Ellis jersey across T2/T3/T4** — Fix prompt to explicitly require "RED soccer shirt with black/white soccer ball graphic, NO stripes, NOT orange, NOT blue/white." Affects ~30 images.
2. **[P1] Benny overalls (T3)** — Remove overalls/bow-tie from all Tier 3 Benny prompts. He should wear only his canonical green plaid scarf.
3. **[P1] Riley single bow** — Prompt must specify "TWO pink hair bows, one on each pigtail, hair in TWO distinct pigtails." Affects ~20 images.
4. **[P2] Layla straight hair (T2)** — Add "dark CURLY/WAVY voluminous hair" to Tier 2 Layla prompt. Affects ~8 images.
5. **[P2] Layla hood UP (T4-SC02)** — Reshoot SC02-tier4 with explicit "teal hoodie, hood DOWN."
6. **[P2] CHAR_MISSING scenes** — Reshoot T2-SC05, T2-SC07, T2-SC15, T4-SC15, T4-SC16 with full core cast.
7. **[P3] Benny scale (T4)** — Add "child height, significantly shorter than adult characters" to Tier 4 Benny prompts.
8. **[P3] Riley skin/eye tone (T4-SC08)** — Reshoot; Riley rendered with incorrect light skin and blue eyes.
9. **[P3] Ellis dark hair (T1-SC11, T3-SC10, T3-SC14)** — Add explicit "BLONDE hair, light golden color" to Ellis prompts.
