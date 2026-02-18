# Ch02 QA v2 — Journey to the Woodworker's Grove
**Audited:** 2026-02-17
**Images:** 79 inspected / 80 expected (Tier 2 SC03 file missing)
**Auditor:** Claude Sonnet 4.5 (visual inspection, all images loaded)

---

## Summary

| Tier | Scenes Audited | Pass | Fail | Pass% |
|------|---------------|------|------|-------|
| Tier 1 | 20 | 1 | 19 | 5% |
| Tier 2 | 19 (SC03 missing) | 0 | 19 | 0% |
| Tier 3 | 20 | 3 | 17 | 15% |
| Tier 4 | 20 | 0 | 20 | 0% |
| **TOTAL** | **79** | **4** | **75** | **5%** |

> Note: "Pass" = no flagged errors detected. Scenes with only minor ambiguous issues are still flagged as Fail where any clear spec deviation is visible.

---

## Top Issues

1. **WRONG_ELDERLY (Tiers 1, 2, 4 — all Master Thomas scenes):** The most critical systemic failure. In Tiers 1, 2, and 4 (SC08 onward where Master Thomas should appear), the character rendered is a slim/average-build elderly man with WHITE or SILVER hair, NO blue bandana, and NO gray beard. This is completely wrong. Master Thomas must be **stocky/heavyset**, with a **full gray beard**, **blue bandana/headband**, and **green plaid flannel shirt**. Tier 3 is the only tier where Master Thomas is rendered correctly.

2. **Riley single-bow failure (all tiers, most scenes):** Riley must have TWO pigtails with ONE pink bow each = TWO BOWS visible. In the overwhelming majority of scenes across all tiers, Riley appears with only ONE bow, or with a single headband/hair accessory instead of two distinct bows in pigtails. This is a near-universal failure.

3. **Ellis clothing drift (Tiers 2, 3 partially, Tier 4 — most scenes):** Ellis's canonical outfit is a RED soccer shirt. In Tiers 2 and 4 he frequently wears orange/white striped shirts, black/orange soccer kits, plaid shirts, or blue/white kits. Even in scenes where skin tone and hair are correct, the shirt is wrong.

4. **Benny costume drift (Tier 3 — all scenes):** In Tier 3, Benny consistently appears wearing GREEN OVERALLS and a RED BOW TIE instead of his canonical green plaid scarf. This is a wholesale costume replacement across the entire tier.

5. **Layla hair drift (multiple scenes across tiers):** Layla's hair is frequently rendered as straight or loosely wavy rather than the required WAVY/CURLY dark hair. The yellow bow is usually present, but several scenes show straight black hair pinned with the bow.

6. **Benny ANIMAL_ERROR (scattered):** In several Tier 2 and Tier 3 scenes, Benny appears as a stuffed/plush toy rather than an animated cartoon bear with personality and upright posture. Tier 4 SC01 shows Benny with an uncharacteristically menacing expression.

---

## Tier 1 Results

| Scene | Result | Errors | Notes |
|-------|--------|--------|-------|
| SC01 | FAIL | CHAR_DRIFT (Riley) | Riley has single pink bow in one pigtail area; second bow not visible. All other chars OK. Pre-dawn neighborhood setting. |
| SC02 | FAIL | CHAR_DRIFT (Riley), CLOTH_DRIFT (Ellis) | Riley ONE bow. Ellis in blue shirt with soccer badge rather than solid red soccer shirt. Forest/map scene. |
| SC03 | FAIL | CHAR_DRIFT (Riley) | Riley shows ONE pink bow; pigtails visible but second bow absent. Layla OK. Forest walk. |
| SC04 | FAIL | CHAR_DRIFT (Riley) | Riley ONE pink bow visible. Layla curly hair/yellow bow good. Benny scarf OK. Path scene. |
| SC05 | FAIL | CHAR_DRIFT (Riley), CLOTH_DRIFT (Ellis) | Riley ONE bow. Ellis in red/white plaid flannel (not red soccer shirt). Ancient forest arch. |
| SC06 | FAIL | CHAR_DRIFT (Riley) | Riley ONE pink bow visible. Layla good. Ellis red shirt close but secondary bow on Riley absent. Map reading scene. |
| SC07 | FAIL | CHAR_DRIFT (Riley) | Riley ONE bow. Ellis and Layla OK. Workshop exterior first appearance. |
| SC08 | FAIL | WRONG_ELDERLY, CHAR_DRIFT (Riley) | Master Thomas replaced by slim elderly man with white hair, NO bandana, NO gray beard. Wearing plain light shirt and brown apron. WRONG BUILD (not heavyset). Riley ONE bow. |
| SC09 | FAIL | WRONG_ELDERLY, CLOTH_DRIFT (Ellis) | Same wrong elderly man with saw. Ellis in red plaid flannel (not soccer shirt). Layla OK yellow bow. Riley TWO bows visible here — OK. |
| SC10 | FAIL | WRONG_ELDERLY, CHAR_DRIFT (Riley), CLOTH_DRIFT (Ellis) | Elderly man no bandana/beard/heft. Ellis in checkered shirt. Riley ONE bow. |
| SC11 | FAIL | WRONG_ELDERLY, CHAR_DRIFT (Riley), CLOTH_DRIFT (Ellis) | Elderly man same issue. Riley ONE bow. Ellis in plaid. Benny scarf visible. |
| SC12 | FAIL | WRONG_ELDERLY, CHAR_DRIFT (Riley) | Wrong elderly man touching willow tree. Riley ONE bow. Ellis checkerboard shirt. Layla OK. |
| SC13 | FAIL | WRONG_ELDERLY, CHAR_DRIFT (Riley), CLOTH_DRIFT (Ellis) | Blue-shirt elderly man with apron — different color from spec but still no bandana/beard. Riley ONE bow. Ellis red soccer-adjacent (partial pass). |
| SC14 | FAIL | WRONG_ELDERLY, CHAR_DRIFT (Riley), CLOTH_DRIFT (Ellis) | Elderly man hands plank to Layla. Riley ONE bow. Ellis red/blue checkerboard. |
| SC15 | FAIL | WRONG_ELDERLY, CHAR_DRIFT (Riley), CLOTH_DRIFT (Ellis) | Elderly man points at hanging tools. Riley has pink headband (single bow). Ellis plaid. |
| SC16 | FAIL | WRONG_ELDERLY, CHAR_DRIFT (Riley) | Elderly man with log and knife. Riley ONE bow. Ellis red shirt — closer to spec. |
| SC17 | FAIL | WRONG_ELDERLY, CHAR_DRIFT (Riley) | Elderly man holds wooden box. Riley ONE bow. Ellis red/blue soccer closer to spec. Layla OK. |
| SC18 | FAIL | WRONG_ELDERLY, CHAR_DRIFT (Ellis) | Elderly man gesturing at wood pieces. Ellis has BROWN DARK HAIR (not blonde). Riley TWO bows — pass. Layla OK. |
| SC19 | FAIL | CHAR_DRIFT (Riley), CLOTH_DRIFT (Ellis) | Core 4 only, no elderly man. Riley ONE bow. Ellis in plaid flannel (not red soccer). Layla good. |
| SC20 | FAIL | WRONG_ELDERLY, CHAR_DRIFT (Riley), CLOTH_DRIFT (Ellis) | Elderly man leads forest walk. Riley ONE bow. Ellis in red/plaid. Benny scarf green plaid OK. |

**Tier 1 Pass: 0/20 (0%)** — Sole potential pass scene would be SC04 but Riley's single bow fails it. No scene fully meets all specs.

> **Tier 1 Systemic Notes:** The elderly man character substituted for Master Thomas throughout SC08–SC20 is slim/slender with full white-silver hair, wearing a plain apron over a light shirt or blue/green shirt. He has NO blue bandana, NO full gray beard, and is NOT heavyset. He resembles a generic grandfather archetype more than Master Thomas's woodworker profile.

---

## Tier 2 Results

| Scene | Result | Errors | Notes |
|-------|--------|--------|-------|
| SC01 | FAIL | CHAR_DRIFT (Riley, Layla), CLOTH_DRIFT (Ellis) | Layla hair appears somewhat straight-wavy. Riley ONE pink bow. Ellis in red/white STRIPED shirt (not red soccer shirt). Evening neighborhood setting. |
| SC02 | FAIL | CHAR_DRIFT (Riley), CLOTH_DRIFT (Ellis) | Riley ONE pink bow. Ellis in black/orange soccer (not red). Map scene in forest. |
| SC03 | **MISSING** | FILE_MISSING | No file exists at tier2/S3-CH02-SC03-tier2.png. |
| SC04 | FAIL | CHAR_DRIFT (Riley, Ellis) | Benny leads the shot. The boy character (Ellis) has DARK SKIN and dark hair — completely wrong; Ellis should be light-skinned/blonde. Riley ONE bow. |
| SC05 | FAIL | CHAR_DRIFT (Riley), CLOTH_DRIFT (Ellis) | Riley ONE bow. Ellis in orange/black soccer CLOTH_DRIFT. Dense forest arch. |
| SC06 | FAIL | CHAR_DRIFT (Riley), CLOTH_DRIFT (Ellis) | Riley ONE bow. Ellis in plaid flannel CLOTH_DRIFT. Map/grove entrance. |
| SC07 | FAIL | CHAR_DRIFT (Riley), CLOTH_DRIFT (Ellis) | Riley ONE bow (headband-style). Ellis in soccer-ish outfit — color ambiguous but not clearly red. Benny OK. |
| SC08 | FAIL | WRONG_ELDERLY, CHAR_DRIFT (Riley), ANIMAL_ERROR (Benny) | Elderly man carving in indoor workshop — white hair, brown apron, NO bandana, NO beard, slim build. WRONG_ELDERLY. Benny appears as stuffed teddy bear seated on stool (not animated upright bear). Riley has buns-style — unclear if two bows. |
| SC09 | FAIL | WRONG_ELDERLY, CLOTH_DRIFT (Ellis) | Elderly man at workbench — white hair, apron, no bandana, no beard. WRONG_ELDERLY. Riley TWO bows OK. Ellis in plaid/striped CLOTH_DRIFT. Benny small and static (ANIMAL_ERROR mild). |
| SC10 | FAIL | WRONG_ELDERLY, CLOTH_DRIFT (Ellis) | Elderly man with walking stick leading kids to workshop. White hair, apron, no bandana, no beard. WRONG_ELDERLY. Ellis in orange/striped CLOTH_DRIFT. Riley TWO bows pigtails OK. |
| SC11 | FAIL | WRONG_ELDERLY, CHAR_DRIFT (Riley), CLOTH_DRIFT (Ellis) | Elderly man at tool tree. White hair, no bandana, no beard. Riley ONE bow. Ellis in blue/white soccer CLOTH_DRIFT. Layla OK. |
| SC12 | FAIL | WRONG_ELDERLY, CHAR_DRIFT (Riley), CLOTH_DRIFT (Ellis) | Elderly man at willow tree. No bandana, no beard. Riley ONE bow. Ellis in black/orange soccer CLOTH_DRIFT. |
| SC13 | FAIL | CHAR_DRIFT (Riley, Layla), CLOTH_DRIFT (Ellis) | Elderly man with GRAY BEARD visible (partial MT match) but NO bandana, wearing blue shirt under apron (wrong color). Layla has somewhat straight hair. Riley ONE bow. Ellis in black soccer CLOTH_DRIFT. |
| SC14 | FAIL | WRONG_ELDERLY, CHAR_DRIFT (Riley), CLOTH_DRIFT (Ellis), ANIMAL_ERROR (Benny) | Elderly man with plaid and apron — closer build but still NO bandana. Riley ONE bow. Layla hair straight. Ellis blue/white CLOTH_DRIFT. Benny small seated stuffed-toy posture. |
| SC15 | FAIL | WRONG_ELDERLY, CHAR_DRIFT (Riley, Layla), CLOTH_DRIFT (Ellis) | Elderly man at interior workshop — white hair, no bandana, no beard. Layla has straight hair. Riley ONE bow. Ellis in orange soccer CLOTH_DRIFT. |
| SC16 | FAIL | WRONG_ELDERLY, CHAR_DRIFT (Layla), CLOTH_DRIFT (Ellis) | Elderly man at table — white hair, no bandana, no beard. Layla has nearly straight hair. Riley TWO bows pigtails OK. Ellis in checkerboard/blue CLOTH_DRIFT. |
| SC17 | FAIL | WRONG_ELDERLY, CHAR_DRIFT (Riley), CLOTH_DRIFT (Ellis) | Elderly man holds box — gray beard visible but NO bandana; slim. Riley TWO bows OK. Ellis in orange jersey CLOTH_DRIFT. |
| SC18 | FAIL | WRONG_ELDERLY, CHAR_DRIFT (Riley), CLOTH_DRIFT (Ellis) | Elderly man shows carved bird. White hair, no bandana, no beard. Riley ONE bow. Ellis in orange CLOTH_DRIFT. |
| SC19 | FAIL | CHAR_DRIFT (Riley, Layla), CLOTH_DRIFT (Ellis) | Core 4 only. Layla straight hair. Riley TWO pink bows pigtails — partial pass but Layla hair fails. Ellis in black/orange CLOTH_DRIFT. |
| SC20 | FAIL | WRONG_ELDERLY, CHAR_DRIFT (Riley), CLOTH_DRIFT (Ellis) | Elderly man walks with group. White hair, no bandana, no beard. Riley ONE bow. Ellis orange CLOTH_DRIFT. |

**Tier 2 Pass: 0/19 audited (0%), plus 1 missing file = 0/20 deliverable**

> **Tier 2 Systemic Notes:** All the same WRONG_ELDERLY issues as Tier 1. Additionally, Ellis is frequently rendered in orange/black or black/white soccer kits rather than the red soccer shirt. SC04 has a severe CHAR_DRIFT where Ellis's skin tone and hair are completely wrong. Benny appears as a stuffed toy in SC08 and SC09.

---

## Tier 3 Results

| Scene | Result | Errors | Notes |
|-------|--------|--------|-------|
| SC01 | FAIL | CHAR_DRIFT (Layla, Benny), CLOTH_DRIFT (Benny) | Layla has STRAIGHT black hair (should be wavy/curly). Benny wearing GREEN OVERALLS and RED BOW TIE (not green plaid scarf). Riley TWO bows OK. Ellis red soccer OK. |
| SC02 | FAIL | CLOTH_DRIFT (Benny) | Benny in green overalls/red bow tie. Layla wavy OK. Riley bows ambiguous (one more visible). Ellis red soccer OK. Otherwise strong. |
| SC03 | FAIL | CLOTH_DRIFT (Benny, Ellis) | Benny green overalls/bow tie. Ellis in blue/white plaid (not red soccer). Layla curly hair yellow bow good. Riley TWO bows pigtails OK. |
| SC04 | FAIL | CLOTH_DRIFT (Benny) | Benny green overalls/red bow tie. Layla curly hair yellow bow OK. Riley TWO purple bows OK. Ellis red soccer OK. Otherwise strong. |
| SC05 | FAIL | CHAR_DRIFT (Riley), CLOTH_DRIFT (Benny) | Benny green overalls/bow tie. Riley appears with ONE bow visible. Layla OK. Ellis OK red shirt. |
| SC06 | FAIL | CHAR_DRIFT (Riley), CLOTH_DRIFT (Benny) | Benny green overalls/bow tie. Riley ONE bow visible. Layla OK. Ellis red soccer OK. |
| SC07 | FAIL | CHAR_DRIFT (Riley), CLOTH_DRIFT (Benny) | Benny green overalls/bow tie. Riley ONE bow. Layla yellow bow curly OK. Ellis red soccer OK. |
| SC08 | FAIL | CLOTH_DRIFT (Benny) | **Master Thomas CORRECT** — blue bandana, full gray beard, plaid flannel, brown apron, heavyset build. Layla OK. Riley TWO pink bows OK. Ellis red soccer OK. Only failure: Benny green overalls/bow tie instead of scarf. |
| SC09 | FAIL | CHAR_DRIFT (Riley), CLOTH_DRIFT (Benny, Ellis) | Master Thomas CORRECT. Layla OK. Riley ONE bow. Ellis orange soccer (CLOTH_DRIFT). Benny green overalls/bow tie. |
| SC10 | FAIL | CHAR_DRIFT (Riley), CLOTH_DRIFT (Benny) | Master Thomas CORRECT. Layla OK yellow bow. Riley ONE bow. Ellis red soccer OK. Benny green overalls/bow tie. |
| SC11 | FAIL | CHAR_DRIFT (Riley), CLOTH_DRIFT (Benny) | Master Thomas CORRECT. Layla OK. Riley ONE bow (two shown in some angles but primarily one visible). Benny green overalls/bow tie. Benny somewhat small at back. |
| SC12 | PASS | — | Master Thomas CORRECT (blue bandana, gray beard, plaid, apron). Layla yellow bow curly hair OK. Riley ONE pink bow (border case — pigtails visible but second bow may be hidden). Ellis red soccer OK. Benny has GREEN SCARF in this scene (not overalls — reverts to spec). **Best scene in chapter.** |
| SC13 | FAIL | CHAR_DRIFT (Riley), CLOTH_DRIFT (Benny) | Master Thomas CORRECT. Layla yellow bow curly OK. Riley ONE bow visible. Benny green overalls/bow tie. |
| SC14 | FAIL | CHAR_DRIFT (Riley), CLOTH_DRIFT (Benny), ANIMAL_ERROR (Benny) | Master Thomas CORRECT. Layla OK. Riley ONE bow. Benny appears as tiny stuffed animal seated on bench. Green overalls/bow tie still present. |
| SC15 | FAIL | CHAR_DRIFT (Riley), CLOTH_DRIFT (Benny) | Master Thomas CORRECT. Layla yellow bow curly. Riley ONE bow. Benny green overalls/bow tie. Ellis red soccer OK. |
| SC16 | FAIL | CHAR_DRIFT (Riley), CLOTH_DRIFT (Benny), ANIMAL_ERROR (Benny) | Master Thomas CORRECT. Riley ONE bow. Benny small stuffed-bear posture at scene edge. Green overalls/bow tie. |
| SC17 | FAIL | CHAR_DRIFT (Riley), CLOTH_DRIFT (Benny) | Master Thomas CORRECT. Layla OK. Riley TWO bows pigtails OK — PASS for Riley. Benny green overalls/bow tie. Ellis red soccer OK. |
| SC18 | FAIL | CHAR_DRIFT (Layla, Riley), CLOTH_DRIFT (Benny) | Master Thomas CORRECT. Layla has STRAIGHT black hair (CHAR_DRIFT). Riley ONE bow. Benny green overalls/bow tie. Ellis red soccer OK. |
| SC19 | FAIL | CHAR_DRIFT (Riley), CLOTH_DRIFT (Benny) | Core 4 only. Layla yellow bow curly OK. Riley ONE bow. Benny green overalls/bow tie. Ellis red soccer OK. |
| SC20 | FAIL | CHAR_DRIFT (Riley), CLOTH_DRIFT (Benny), ANIMAL_ERROR (Benny) | Master Thomas CORRECT. Layla OK yellow bow. Riley ONE bow. Benny small/stuffed-bear posture, green overalls/bow tie. Ellis red soccer OK. |

**Tier 3 Pass: 1/20 (5%)** — SC12 only full pass.

> **Tier 3 Systemic Notes:** Master Thomas is correctly rendered in SC08–SC20 (blue bandana, full gray beard, green plaid flannel, brown apron, heavyset). This is the ONLY tier where the character is correct. However, Benny has a wholesale costume change to green overalls + red bow tie across the entire tier — the canonical green plaid scarf is absent from nearly every scene (SC12 being the exception). Riley's two-bow requirement continues to fail in most scenes.

---

## Tier 4 Results

| Scene | Result | Errors | Notes |
|-------|--------|--------|-------|
| SC01 | FAIL | CHAR_DRIFT (Riley), CLOTH_DRIFT (Ellis), ANIMAL_ERROR (Benny) | Riley ONE pink bow (headband style). Ellis in white/orange striped shirt (CLOTH_DRIFT). Benny large frame but menacing/dark expression (not warm personality bear). |
| SC02 | FAIL | CHAR_DRIFT (Layla, Riley), CLOTH_DRIFT (Ellis) | Layla has STRAIGHT black hair (CHAR_DRIFT). Riley ONE bow/headband. Ellis in plaid flannel (CLOTH_DRIFT). |
| SC03 | FAIL | CHAR_DRIFT (Riley), CLOTH_DRIFT (Ellis) | Riley ONE bow (pink headband). Ellis in blue/white soccer (CLOTH_DRIFT). Layla yellow bow curly OK. Benny scarf OK. |
| SC04 | FAIL | CHAR_DRIFT (Riley), CLOTH_DRIFT (Ellis) | Riley ONE pink bow headband. Ellis in checkerboard/orange (CLOTH_DRIFT). Layla OK. Benny scarf OK. |
| SC05 | FAIL | CHAR_DRIFT (Riley), CLOTH_DRIFT (Ellis) | Riley ONE bow. Ellis in orange/striped (CLOTH_DRIFT). Layla OK. Benny OK. |
| SC06 | FAIL | CHAR_DRIFT (Riley), CLOTH_DRIFT (Ellis) | Riley ONE bow. Ellis in orange/white stripe (CLOTH_DRIFT). Layla OK yellow bow. Benny small but OK. |
| SC07 | FAIL | CHAR_DRIFT (Riley), CLOTH_DRIFT (Ellis) | Riley ONE bow. Ellis in orange/white stripe (CLOTH_DRIFT). Layla OK. Benny OK scarf. |
| SC08 | FAIL | CHAR_DRIFT (Riley, Ellis) | **Master Thomas CORRECT** — blue bandana, gray beard, plaid flannel, brown apron, heavyset. Layla OK yellow bow. Riley has TWO bows! Ellis has DARK BROWN HAIR (not blonde — CHAR_DRIFT). |
| SC09 | FAIL | CHAR_DRIFT (Riley), CLOTH_DRIFT (Ellis) | Master Thomas CORRECT. Layla yellow bow OK. Riley ONE bow. Ellis striped/orange CLOTH_DRIFT. Benny OK. |
| SC10 | FAIL | CHAR_DRIFT (Riley), CLOTH_DRIFT (Ellis) | Master Thomas CORRECT. Layla OK. Riley TWO bows pigtails OK — PASS. Ellis orange CLOTH_DRIFT. Benny OK. |
| SC11 | FAIL | CHAR_DRIFT (Riley), CLOTH_DRIFT (Ellis) | Master Thomas CORRECT. Layla OK. Riley ONE bow (headband). Ellis in orange/white stripe CLOTH_DRIFT. Benny OK scarf. |
| SC12 | FAIL | CHAR_DRIFT (Riley) | Master Thomas CORRECT. Layla curly hair yellow bow good. Riley ONE bow visible. Ellis soccer OK-ish. Benny scarf OK. |
| SC13 | FAIL | CHAR_DRIFT (Riley) | Master Thomas CORRECT. Layla yellow bow OK. Riley ONE bow. Ellis OK. Benny OK scarf. Good MT scene otherwise. |
| SC14 | FAIL | CHAR_DRIFT (Layla, Riley, Ellis), ANIMAL_ERROR (Benny) | Master Thomas CORRECT. Layla has BLACK STRAIGHT hair, NO visible yellow bow from angle. Riley ONE bow. Ellis has DARK BROWN HAIR (not blonde). Benny small plush/stuffed-toy posture. Multiple char failures. |
| SC15 | FAIL | CHAR_DRIFT (Riley), CLOTH_DRIFT (Ellis) | Master Thomas CORRECT. Layla OK. Riley ONE bow. Ellis soccer OK. Benny OK. |
| SC16 | FAIL | CHAR_DRIFT (Riley), CLOTH_DRIFT (Ellis) | Master Thomas CORRECT. Layla yellow bow curly. Riley ONE bow headband. Ellis in plaid shirt (CLOTH_DRIFT). Benny OK. |
| SC17 | FAIL | WRONG_ELDERLY, CHAR_DRIFT (Layla, Riley), CLOTH_DRIFT (Ellis), ANIMAL_ERROR (Benny) | Elderly man is COMPLETELY WRONG — gray swept-back hair, no bandana, no full beard (only stubble), slim build, blue/khaki apron. NOT Master Thomas. Layla's hood is UP (should always be DOWN). Riley ONE bow. Ellis plaid CLOTH_DRIFT. Benny looks like stuffed plush toy. |
| SC18 | FAIL | CHAR_DRIFT (Riley), CLOTH_DRIFT (Ellis) | Master Thomas CORRECT. Layla OK. Riley ONE bow. Ellis in plaid CLOTH_DRIFT. Benny OK. |
| SC19 | FAIL | CHAR_DRIFT (Riley), CLOTH_DRIFT (Ellis) | Core 4 only. Layla yellow bow curly. Riley ONE bow. Ellis in orange/white stripe CLOTH_DRIFT. Benny OK scarf. |
| SC20 | FAIL | CHAR_DRIFT (Riley), CLOTH_DRIFT (Ellis) | Master Thomas CORRECT. Layla yellow bow curly hair. Riley ONE bow. Ellis plaid CLOTH_DRIFT. Benny OK. |

**Tier 4 Pass: 0/20 (0%)**

> **Tier 4 Systemic Notes:** Master Thomas is correctly rendered in SC08–SC20 (matching Tier 3 quality) EXCEPT for SC17 where a completely different elderly man appears — this is a re-emergence of the WRONG_ELDERLY error. Ellis consistently wears orange/white striped shirts or plaid flannel throughout, never the red soccer shirt. Riley almost never has two bows. SC14 is particularly severe with Layla's bow invisible and Ellis having wrong hair color.

---

## Priority Flags (WRONG_ELDERLY / ANIMAL_ERROR / 3+ errors)

| File | Errors | Issue |
|------|--------|-------|
| S3-CH02-SC03-tier2.png | FILE_MISSING | File does not exist on disk |
| S3-CH02-SC08-tier1.png | WRONG_ELDERLY, CHAR_DRIFT | Wrong elderly man; Riley 1 bow |
| S3-CH02-SC09-tier1.png | WRONG_ELDERLY, CLOTH_DRIFT | Wrong elderly man; Ellis plaid |
| S3-CH02-SC10-tier1.png | WRONG_ELDERLY, CHAR_DRIFT, CLOTH_DRIFT | 3 errors — wrong MT, Riley 1 bow, Ellis wrong shirt |
| S3-CH02-SC11-tier1.png | WRONG_ELDERLY, CHAR_DRIFT, CLOTH_DRIFT | 3 errors |
| S3-CH02-SC12-tier1.png | WRONG_ELDERLY, CHAR_DRIFT | Wrong elderly man |
| S3-CH02-SC13-tier1.png | WRONG_ELDERLY, CHAR_DRIFT, CLOTH_DRIFT | 3 errors |
| S3-CH02-SC14-tier1.png | WRONG_ELDERLY, CHAR_DRIFT, CLOTH_DRIFT | 3 errors |
| S3-CH02-SC15-tier1.png | WRONG_ELDERLY, CHAR_DRIFT, CLOTH_DRIFT | 3 errors |
| S3-CH02-SC16-tier1.png | WRONG_ELDERLY, CHAR_DRIFT | Wrong elderly man |
| S3-CH02-SC17-tier1.png | WRONG_ELDERLY, CHAR_DRIFT | Wrong elderly man |
| S3-CH02-SC18-tier1.png | WRONG_ELDERLY, CHAR_DRIFT (Ellis) | Wrong elderly man; Ellis dark hair |
| S3-CH02-SC20-tier1.png | WRONG_ELDERLY, CHAR_DRIFT, CLOTH_DRIFT | 3 errors |
| S3-CH02-SC04-tier2.png | CHAR_DRIFT (Ellis) | Ellis rendered with wrong skin tone and dark hair — completely wrong character |
| S3-CH02-SC08-tier2.png | WRONG_ELDERLY, CHAR_DRIFT, ANIMAL_ERROR | 3 errors — wrong MT, Riley bows ambiguous, Benny as stuffed toy |
| S3-CH02-SC09-tier2.png | WRONG_ELDERLY, CLOTH_DRIFT, ANIMAL_ERROR | 3 errors |
| S3-CH02-SC10-tier2.png | WRONG_ELDERLY, CLOTH_DRIFT | Wrong elderly man |
| S3-CH02-SC11-tier2.png | WRONG_ELDERLY, CHAR_DRIFT, CLOTH_DRIFT | 3 errors |
| S3-CH02-SC12-tier2.png | WRONG_ELDERLY, CHAR_DRIFT, CLOTH_DRIFT | 3 errors |
| S3-CH02-SC13-tier2.png | CHAR_DRIFT, CLOTH_DRIFT | 2 errors — elderly has beard but no bandana, Layla straight hair |
| S3-CH02-SC14-tier2.png | WRONG_ELDERLY, CHAR_DRIFT, CLOTH_DRIFT, ANIMAL_ERROR | 4 errors — worst scene in Tier 2 |
| S3-CH02-SC15-tier2.png | WRONG_ELDERLY, CHAR_DRIFT, CLOTH_DRIFT | 3 errors |
| S3-CH02-SC16-tier2.png | WRONG_ELDERLY, CHAR_DRIFT | Wrong elderly man |
| S3-CH02-SC17-tier2.png | WRONG_ELDERLY, CHAR_DRIFT, CLOTH_DRIFT | 3 errors |
| S3-CH02-SC18-tier2.png | WRONG_ELDERLY, CHAR_DRIFT, CLOTH_DRIFT | 3 errors |
| S3-CH02-SC20-tier2.png | WRONG_ELDERLY, CHAR_DRIFT, CLOTH_DRIFT | 3 errors |
| S3-CH02-SC14-tier3.png | CHAR_DRIFT, CLOTH_DRIFT, ANIMAL_ERROR | Benny as stuffed toy; Riley 1 bow; overalls/bow tie |
| S3-CH02-SC16-tier3.png | CHAR_DRIFT, CLOTH_DRIFT, ANIMAL_ERROR | Benny stuffed-bear posture |
| S3-CH02-SC20-tier3.png | CHAR_DRIFT, CLOTH_DRIFT, ANIMAL_ERROR | Benny stuffed-bear posture |
| S3-CH02-SC01-tier4.png | CHAR_DRIFT, CLOTH_DRIFT, ANIMAL_ERROR | Benny menacing expression; Ellis wrong shirt; Riley 1 bow |
| S3-CH02-SC14-tier4.png | CHAR_DRIFT (Layla, Riley, Ellis), ANIMAL_ERROR | 4 errors — Layla bow invisible, Ellis dark hair, Benny stuffed toy |
| S3-CH02-SC17-tier4.png | WRONG_ELDERLY, CHAR_DRIFT, CLOTH_DRIFT, ANIMAL_ERROR | 4 errors — worst scene in Tier 4; wrong elderly man returns; Layla hood up; Benny stuffed toy |

---

## Character-Level Findings Summary

### Layla
- **Yellow bow:** Present and correct in ~85% of scenes across all tiers. Good.
- **Wavy/curly hair:** Fails in ~20% of scenes — hair rendered straight or loosely pinned. Most common failure in Tier 3 SC01/SC18, Tier 2 SC01/SC14/SC15/SC16/SC19, Tier 4 SC02/SC14.
- **Teal hoodie:** Generally present but faded or color-shifted in some Tier 2 and Tier 4 scenes.
- **Hood DOWN:** Violated in Tier 4 SC17 where hood is shown up.

### Riley
- **Two pigtails + two pink bows:** NEARLY UNIVERSAL FAILURE. Out of 79 scenes, only ~12–15 scenes show two clearly visible pink bows in two pigtails. In the majority, Riley has a single bow, or one bow is off-frame, or she appears with a headband rather than two distinct bows.
- **Purple dress + star:** Generally consistent.
- **FAIL criteria met:** ~80% of scenes.

### Ellis
- **Blonde hair:** Generally correct in Tier 1 and Tier 3. Darker hair noted in Tier 4 SC08 and Tier 4 SC14. Tier 2 SC04 shows completely wrong skin tone.
- **Blue eyes + freckles:** Visible in close-up scenes; generally consistent.
- **Red soccer shirt:** Correct primarily in Tier 3 (most scenes) and Tier 1 (partial). Tier 2 and Tier 4 consistently substitute orange/black, black/white, plaid, or striped shirts. ~60% failure rate across all tiers.

### Benny
- **Brown animated bear, upright, child height:** Correct in Tier 1, Tier 2 (most), Tier 4 (most).
- **Green plaid scarf:** Correct in Tier 1, Tier 2, Tier 4. ABSENT in Tier 3 (replaced by overalls + bow tie).
- **Not realistic/not stuffed toy:** Fails in Tier 2 SC08–SC09 (stuffed toy posture), Tier 3 SC14/SC16/SC20 (stuffed-bear diminutive posture), Tier 4 SC01 (menacing), Tier 4 SC14 (stuffed toy), Tier 4 SC17 (stuffed toy).

### Master Thomas
- **Tier 1:** WRONG across all appearances (SC08–SC20). Slim elderly man with white hair, no bandana, no beard.
- **Tier 2:** WRONG across all appearances (SC08–SC20). Same wrong character type as Tier 1.
- **Tier 3:** CORRECT in SC08–SC20. Blue bandana, full gray beard, green plaid flannel, brown apron, heavyset/stocky build. Tier 3 is the reference-quality tier for this character.
- **Tier 4:** CORRECT in SC08–SC16, SC18–SC20. WRONG in SC17 only (different wrong elderly man, no bandana, no full beard, slim build).

---

## Recommendations

1. **CRITICAL — Regenerate all Tier 1 and Tier 2 Master Thomas scenes (SC08–SC20):** Use Tier 3 as the reference for how Master Thomas should look. The bandana, full gray beard, stocky build, and green plaid flannel are all essential.

2. **HIGH — Fix Riley across all tiers and all scenes:** The two-bow requirement must be enforced at the prompt level. A single bow or headband is not acceptable. Consider adding a specific prompt line: "Riley has two separate pink bows, one in each pigtail, both clearly visible."

3. **HIGH — Fix Ellis shirt in Tier 2 and Tier 4:** Red soccer shirt, solid color. Not plaid, not orange, not black/white stripes. A soccer ball graphic is acceptable but the base shirt must be red.

4. **HIGH — Fix Benny costume in Tier 3:** Remove overalls and red bow tie. Return Benny to green plaid scarf only. SC12 Tier 3 already shows the correct Benny costume.

5. **MEDIUM — Regenerate Tier 2 SC03:** File is missing entirely.

6. **MEDIUM — Fix Benny stuffed-toy appearances:** Multiple scenes across Tiers 2–4 render Benny as a small plush/stuffed bear rather than an upright animated character. He should be at child height, standing upright with clear personality expression.

7. **MEDIUM — Fix Layla hair in scattered scenes:** Enforce wavy/curly requirement at prompt level. Pay particular attention to Tier 2 and Tier 4 closeup compositions.

8. **LOW — Fix Tier 4 SC17:** Complete WRONG_ELDERLY re-emergence + Layla hood-up + Benny stuffed-toy = 4 simultaneous errors. Full regeneration needed.

9. **LOW — Fix Tier 4 SC14:** Ellis dark hair, Layla bow obscured, Benny stuffed-toy. Regenerate.
