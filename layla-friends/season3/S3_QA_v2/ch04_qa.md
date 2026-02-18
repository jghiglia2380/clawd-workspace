# Ch04 QA v2 — Building Boxes
**Audited:** 2026-02-17 | **Images:** 80 | **Auditor:** Claude Sonnet 4.5

---

## Summary

| Tier | Pass | Fail | Pass% |
|------|------|------|-------|
| Tier 1 | 0 | 20 | 0% |
| Tier 2 | 0 | 20 | 0% |
| Tier 3 | 1 | 19 | 5% |
| Tier 4 | 0 | 20 | 0% |
| **TOTAL** | **1** | **79** | **1.25%** |

> v1 pass rate was 19%. v2 is 1.25% — this chapter requires a full regeneration pass across all tiers.

---

## Top Issues

1. **CHAR_DRIFT — Master Thomas (Tiers 1 & 2):** Blue bandana is completely absent across ALL 40 Tier 1 and Tier 2 scenes. The elder woodworker is rendered as a generic grandfather with glasses and no head covering. Tiers 3 & 4 correctly include the bandana. This is the single most pervasive failure mode in the chapter.

2. **Riley — Single Bow (all tiers):** Riley should always have TWO pink bows in TWO pigtails. In the vast majority of scenes across all tiers she appears with only ONE bow (single pigtail or single bow in hair). Confirmed multi-bow correct rendering in only a small minority of scenes. This is a systemic prompt failure.

3. **Ellis — Wrong Shirt Color (Tiers 2, 3, 4):** Ellis's red soccer shirt drifts to orange in Tier 2 and orange/white striped in Tiers 3–4. The red shirt is correct only in Tier 1 (partially) and a few T3/T4 frames.

4. **ANIMAL_ERROR — Benny (Tier 4):** Benny is rendered as a photorealistic grizzly bear in SC01 and SC17. SC18 renders Benny as a stuffed teddy at miniature scale. Only the animated cartoon bear at child height is correct.

5. **CHAR_MISSING — Cast dropouts (all tiers):** Multiple scenes with only 2–3 of the expected 5 characters. Frequent missing characters: Benny dropped from crowd shots, Ellis drops out in Tiers 2–3, Master Thomas absent in SC20 closing scene across T1/T2/T3.

6. **Layla — Straight Hair / Missing Bow (Tiers 1–4):** In approximately 20% of scenes, Layla's wavy/curly dark hair is rendered straight. In several scenes, the yellow bow is absent or replaced with a yellow headband only.

7. **MULTI_PANEL — SC04-T4:** Scene contains embedded thumbnail insets (3 small panels in upper corner), making this a multi-panel composite rather than a single scene illustration.

---

## Tier 1 Results

| Scene | Result | Errors | Notes |
|-------|--------|--------|-------|
| SC01 | FAIL | CHAR_DRIFT, CLOTH_DRIFT | MT: no blue bandana (generic grandpa). Riley: single pink bow only, pigtail on one side only. Ellis: very dark hair borderline. |
| SC02 | FAIL | CHAR_DRIFT, CHAR_MISSING | MT: no bandana, wearing glasses, gray hair only. CHAR_MISSING: Riley, Ellis, Benny absent — 2-character close-up scene. |
| SC03 | FAIL | CHAR_DRIFT | MT: no bandana. Riley: 1 pink bow. All 5 characters present otherwise. |
| SC04 | FAIL | CHAR_DRIFT | MT: no bandana. Riley: 2 bows present (PASS on Riley). Benny animated bear at bench. |
| SC05 | FAIL | CHAR_DRIFT | MT: no bandana. Riley: 1 bow only. All 5 characters present. |
| SC06 | FAIL | CHAR_DRIFT, CHAR_DRIFT (Layla) | MT: no bandana. Layla: hair is dark and straight — not wavy/curly per spec. No yellow bow visible. Riley: 2 bows (PASS). |
| SC07 | FAIL | CHAR_DRIFT | MT: no bandana. Riley: 2 bows (PASS). All 5 present. Benny animated. |
| SC08 | FAIL | CHAR_DRIFT | MT: no bandana and wearing glasses not in spec. Riley: 1 bow only. |
| SC09 | FAIL | CHAR_DRIFT | MT: no bandana. Layla: teal hoodie but yellow bow absent from head. Riley: 1 bow. Benny at worktable (animated OK). |
| SC10 | FAIL | CHAR_DRIFT | MT: no bandana. Riley: 1 bow only. All 5 present. |
| SC11 | FAIL | CHAR_DRIFT | MT: no bandana. Riley: 2 bows (PASS). Benny appears as tiny stature bear-child at table. |
| SC12 | FAIL | CHAR_DRIFT | MT: no bandana. Riley: 1 bow only. |
| SC13 | FAIL | CHAR_MISSING | Solo Riley scene — only Riley present. CHAR_MISSING: Layla, Ellis, Master Thomas, Benny absent. Riley: 2 bows (PASS). |
| SC14 | FAIL | CHAR_DRIFT | MT: no bandana. Riley: 1 bow. All 5 present. |
| SC15 | FAIL | CHAR_DRIFT | MT: no bandana. Riley: 1 bow. Benny green plaid scarf (OK). |
| SC16 | FAIL | CHAR_DRIFT, CHAR_MISSING | MT: no bandana. Riley not visible in scene. CHAR_MISSING: Riley. Only Layla, Ellis, MT, Benny shown. |
| SC17 | FAIL | CHAR_DRIFT, ANIMAL_ERROR | MT: no bandana. Benny has ANTLER-like protrusions from head — ANIMAL_ERROR / prop corruption. Riley: 2 bows (PASS). |
| SC18 | FAIL | CHAR_DRIFT | MT: no bandana. Riley: 1 bow. All 5 present. |
| SC19 | FAIL | CHAR_DRIFT, CHAR_DRIFT (Ellis) | MT: no bandana. Ellis: has BROWN/dark hair — not blonde per spec. Riley: 1 bow. |
| SC20 | FAIL | CHAR_MISSING | CHAR_MISSING: Master Thomas absent from closing scene. Riley: 1 bow. Only 4 kids + bear carrying boxes. |

**Tier 1 Pass: 0/20 (0%)**

---

## Tier 2 Results

| Scene | Result | Errors | Notes |
|-------|--------|--------|-------|
| SC01 | FAIL | CHAR_DRIFT (Layla), CHAR_DRIFT (MT), CLOTH_DRIFT (Ellis) | MT: no bandana. Layla: straight dark hair, not curly. Ellis: orange jersey not red. Riley: 2 bows (PASS). Benny tiny in fg. |
| SC02 | FAIL | CHAR_DRIFT, CHAR_MISSING | MT: no bandana. CHAR_MISSING: Riley, Ellis, Benny — 2-character scene. |
| SC03 | FAIL | CHAR_DRIFT | MT: no bandana (gray beard present). Riley: 1 bow only. Ellis orange stripe shirt. |
| SC04 | FAIL | CHAR_DRIFT, CLOTH_DRIFT | MT: no bandana. Riley: 2 bows (PASS). Ellis: orange/black jersey (not red soccer shirt). |
| SC05 | FAIL | CHAR_DRIFT, CHAR_MISSING | MT: no bandana. CHAR_MISSING: Riley, Ellis, Benny — 2-character scene (Layla + MT only). |
| SC06 | FAIL | CHAR_DRIFT, CLOTH_DRIFT | MT: no bandana. Riley: 2 bows (PASS). Ellis: orange/black jersey. |
| SC07 | FAIL | CHAR_DRIFT, CHAR_MISSING | MT: no bandana. CHAR_MISSING: Ellis absent. Layla, Riley (1 bow), MT, Benny present. |
| SC08 | FAIL | CHAR_DRIFT, CHAR_MISSING, FACE_ERROR | MT: no bandana. Only MT + Ellis visible (2-char close-up). CHAR_MISSING: Layla, Riley, Benny. MT has only a grey moustache — full gray beard missing from face. |
| SC09 | FAIL | CHAR_DRIFT, CHAR_MISSING | MT: no bandana. Benny carving (animated OK). Riley: 1 bow. CHAR_MISSING: Ellis absent. |
| SC10 | FAIL | CHAR_DRIFT, CHAR_MISSING | MT: no bandana. CHAR_MISSING: Ellis absent. Riley: 1 bow. |
| SC11 | FAIL | CHAR_DRIFT, CLOTH_DRIFT | MT: no bandana. Riley: 2 bows (PASS). Ellis: orange/black jersey. |
| SC12 | FAIL | CHAR_DRIFT, CLOTH_DRIFT | MT: no bandana. Riley: 2 bows (PASS). Ellis: orange/black jersey. |
| SC13 | FAIL | CHAR_DUPLICATE, CHAR_DRIFT | Riley: 2 bows (PASS). Two identical blond boys in matching orange/black jerseys visible — CHAR_DUPLICATE (Ellis doubled). MT: no bandana. |
| SC14 | FAIL | CHAR_DRIFT, CLOTH_DRIFT | MT: no bandana. Riley: 1 bow. Ellis: orange/black jersey. |
| SC15 | FAIL | CHAR_DRIFT, CLOTH_DRIFT | MT: no bandana (full beard present). Riley: 1 bow. Ellis: orange/black jersey. |
| SC16 | FAIL | CHAR_DRIFT, CLOTH_DRIFT | MT: no bandana. Riley: 1 bow. Ellis: orange/black jersey. |
| SC17 | FAIL | CHAR_DRIFT, CLOTH_DRIFT | MT: no bandana. Riley: 2 bows (PASS). Ellis: orange/black jersey. |
| SC18 | FAIL | CHAR_DRIFT, CLOTH_DRIFT | MT: no bandana. Riley: 1 bow. Ellis: orange/black jersey. |
| SC19 | FAIL | CHAR_DRIFT, CHAR_MISSING | MT: no bandana. CHAR_MISSING: Ellis absent. Layla + Riley (1 bow) + Benny + MT only. |
| SC20 | FAIL | CHAR_DRIFT, CHAR_MISSING | CHAR_MISSING: Master Thomas absent from final scene — only 4 children + bear. Riley: 1 bow only. |

**Tier 2 Pass: 0/20 (0%)**

---

## Tier 3 Results

*Note: Master Thomas Tier 3 reference correctly shows blue bandana + orange/brown plaid shirt. Benny in Tier 3 often rendered in green overalls — treated as STYLE_DRIFT (acceptable if still animated cartoon bear at child height).*

| Scene | Result | Errors | Notes |
|-------|--------|--------|-------|
| SC01 | FAIL | CLOTH_DRIFT (Riley) | MT: blue bandana present (PASS). Layla: curly yellow bow OK. Ellis: red shirt OK. Riley: 1 bow only (single purple/red hair tie). Benny: overalls (minor STYLE_DRIFT). |
| SC02 | FAIL | CHAR_DRIFT (Layla), CLOTH_DRIFT (Riley) | MT: blue bandana OK. Layla: straight dark hair — CHAR_DRIFT (not curly/wavy). Riley: 1 pink bow. Ellis: red shirt OK. |
| SC03 | FAIL | CLOTH_DRIFT (Riley) | MT: blue bandana OK. Layla: curly OK. Riley: 1 pink bow. Ellis: red shirt OK. Benny: overalls (STYLE_DRIFT minor). |
| SC04 | FAIL | CLOTH_DRIFT (Riley) | MT: blue bandana OK. Layla: yellow bow OK. Riley: 1 purple bow. Benny: overalls. All 5 present. |
| SC05 | FAIL | CLOTH_DRIFT (Riley) | MT: blue bandana OK. Layla: curly yellow bow OK. Riley: 1 pink bow. Ellis: red shirt OK. Benny: overalls. |
| SC06 | FAIL | CHAR_MISSING, CLOTH_DRIFT (Riley) | MT: blue bandana OK. CHAR_MISSING: Layla not visible in scene. Riley: 1 bow. Benny: overalls. |
| SC07 | FAIL | CLOTH_DRIFT (Riley) | MT: blue bandana OK. Layla: curly yellow bow OK. Riley: 1 purple bow (pigtails). Ellis: red/orange shirt. Benny: overalls. |
| SC08 | FAIL | CLOTH_DRIFT (Riley) | MT: blue bandana OK. Layla: curly yellow bow OK. Riley: 1 bow (purple/pink pigtail). Ellis: red shirt OK. |
| SC09 | FAIL | CLOTH_DRIFT (Riley) | MT: blue bandana OK. Layla: curly teal hoodie OK. Riley: 1 bow. Benny: overalls (sitting, background). |
| SC10 | FAIL | CLOTH_DRIFT (Riley) | MT: blue bandana OK. Layla: curly yellow bow OK. Riley: 1 bow (purple/pink). Ellis: red shirt OK. Benny: overalls. |
| SC11 | FAIL | CLOTH_DRIFT (Riley) | MT: blue bandana OK. Layla: teal hoodie yellow bow OK. Riley: 1 purple bow. Ellis: red shirt OK. Benny: overalls. |
| SC12 | FAIL | CHAR_DRIFT (Layla) | MT: blue bandana OK. Layla: dark STRAIGHT hair — CHAR_DRIFT. Riley: 2 pink bows (PASS). Ellis: red shirt. Benny: overalls. |
| SC13 | FAIL | CHAR_MISSING | MT: blue bandana OK. Scene shows only Riley + MT (2-char comparison shot). CHAR_MISSING: Layla, Ellis, Benny. Riley: 2 bows (PASS). |
| SC14 | FAIL | CHAR_DRIFT (MT build), CLOTH_DRIFT (Riley) | MT: blue bandana OK, but rendered notably slimmer/younger than heavyset spec. Riley: 1 bow. |
| SC15 | FAIL | CLOTH_DRIFT (Riley) | MT: blue bandana OK. Layla: curly, bow hard to see. Riley: 1 purple bow. Benny: overalls. |
| SC16 | FAIL | CHAR_DRIFT (Layla), CLOTH_DRIFT (Riley) | MT: blue bandana OK. Layla: straight dark hair — CHAR_DRIFT. Riley: 1 bow. Benny: overalls. |
| SC17 | FAIL | CLOTH_DRIFT (Riley) | MT: blue bandana OK. Layla: curly yellow bow OK. Riley: 1 purple bow (pigtail). Ellis: red shirt OK. Benny: overalls. |
| SC18 | FAIL | CLOTH_DRIFT (Riley) | MT: blue bandana OK. Layla: curly yellow bow OK, teal hoodie. Riley: 1 purple bow. Benny: overalls. |
| SC19 | PASS | — | MT: blue bandana OK. Layla: curly, yellow bow OK, teal hoodie. Riley: 2 pink bows (PASS). Ellis: red shirt OK. Benny: overalls (STYLE_DRIFT minor, animated bear at child height). All 5 present. |
| SC20 | FAIL | CHAR_MISSING, CLOTH_DRIFT (Riley) | CHAR_MISSING: Master Thomas absent from closing scene. Layla: curly yellow bow OK. Riley: 1 bow. Ellis: red shirt OK. Benny: overalls. |

**Tier 3 Pass: 1/20 (5%)** — SC19 only.

---

## Tier 4 Results

*Note: Tier 4 style is semi-realistic painted illustration. Master Thomas reference shows blue bandana + orange/brown plaid shirt. Expected characters at this style level.*

| Scene | Result | Errors | Notes |
|-------|--------|--------|-------|
| SC01 | FAIL | ANIMAL_ERROR, CHAR_DRIFT (Layla), CHAR_MISSING | Benny rendered as PHOTOREALISTIC GRIZZLY BEAR (real-world animal proportions). Layla: straight dark hair, not curly. MT: blue bandana (PASS). CHAR_MISSING: Riley not in scene. |
| SC02 | FAIL | CHAR_MISSING, CLOTH_DRIFT (Riley) | MT: blue bandana OK. Layla: curly yellow bow OK. Riley: 1 pink bow (pigtails with 1 bow only). CHAR_MISSING: Ellis not in scene. Benny in background. |
| SC03 | FAIL | CLOTH_DRIFT (Riley), CLOTH_DRIFT (Ellis) | MT: blue bandana OK. Layla: curly yellow bow OK. Ellis: orange/blue jersey (not red). Riley: 1 bow. |
| SC04 | FAIL | MULTI_PANEL | Scene has 3 embedded thumbnail insets in upper-left corner (composite multi-panel). MT: blue bandana OK. Riley: 2 bows in main panel (PASS). Character portraits appear unfinished/in-draft state. |
| SC05 | FAIL | CLOTH_DRIFT (Ellis), CLOTH_DRIFT (Riley) | MT: blue bandana OK. Layla: curly yellow bow OK. Riley: 2 bows (PASS). Ellis: orange/checkered jersey (not red soccer shirt). Benny animated (OK). |
| SC06 | FAIL | CLOTH_DRIFT (Riley), CLOTH_DRIFT (Ellis) | MT: blue bandana OK. Layla: curly yellow bow OK. Riley: 1 bow only. Ellis: orange/white soccer jersey. Benny animated. |
| SC07 | FAIL | CHAR_MISSING, CLOTH_DRIFT (Ellis) | MT: blue bandana OK. Layla: curly yellow bow OK. CHAR_MISSING: Riley not identifiable in scene. Ellis: orange/red-white jersey. Benny: large semi-realistic but animated. |
| SC08 | FAIL | CLOTH_DRIFT (Riley), CLOTH_DRIFT (Ellis) | MT: blue bandana OK. Layla: curly yellow bow OK. Riley: 1 bow. Ellis: orange/red stripe jersey. Benny animated (green scarf OK). |
| SC09 | FAIL | CHAR_DUPLICATE, CLOTH_DRIFT (Ellis) | MT: blue bandana OK. CHAR_DUPLICATE: Two girls with yellow bows visible — Layla (curly) + a second girl in purple dress with yellow bow (Riley wearing wrong bow color — pink bows replaced with yellow). Riley character identification ambiguous. Ellis: orange jersey. |
| SC10 | FAIL | CHAR_MISSING, CLOTH_DRIFT (Ellis) | MT: blue bandana OK. Layla: curly yellow bow OK. Benny: large animated. CHAR_MISSING: Ellis replaced by dark-haired boy (CHAR_DRIFT). Riley: 1 pink bow. |
| SC11 | FAIL | CLOTH_DRIFT (Ellis), ANIMAL_ERROR | MT: blue bandana OK. Layla: curly yellow bow OK. Riley: 2 pink bows (PASS). Ellis: white/multistripe jersey (not red). Benny: semi-realistic furry proportions (borderline ANIMAL_ERROR). |
| SC12 | FAIL | CLOTH_DRIFT (Riley), CLOTH_DRIFT (Ellis) | MT: blue bandana OK. Layla: curly yellow bow OK. Riley: 1 bow. Ellis: orange/white striped jersey. Benny animated. |
| SC13 | FAIL | CLOTH_DRIFT (Riley), CLOTH_DRIFT (Ellis) | MT: blue bandana OK. Layla: curly yellow bow OK. Riley: 1 purple bow. Ellis: orange/white stripe. Benny animated. |
| SC14 | FAIL | CLOTH_DRIFT (Ellis), CLOTH_DRIFT (Riley) | MT: blue bandana OK. Layla: curly OK. Riley: 2 pink bows (PASS). Ellis: orange/white jersey (not red). All 5 present. |
| SC15 | FAIL | CHAR_DRIFT (Riley), CLOTH_DRIFT (Ellis) | MT: blue bandana OK. Layla: curly OK. "Riley" has long straight dark hair + 1 pink bow — CHAR_DRIFT (should be shorter pigtails). Ellis: white striped shirt. Benny animated. |
| SC16 | FAIL | CLOTH_DRIFT (Riley) | MT: blue bandana OK. Layla: curly curly OK. Riley: 1 pink bow only. Ellis: orange/white jersey. Benny animated. |
| SC17 | FAIL | ANIMAL_ERROR | MT: blue bandana OK (photorealistic render). Benny rendered as PHOTOREALISTIC REAL BEAR in real-world workshop setting. All characters photorealistic (style renders as real-world photography aesthetic). |
| SC18 | FAIL | ANIMAL_ERROR, CLOTH_DRIFT (Riley) | MT: blue bandana OK. Layla: curly OK. Riley: 1 bow. Benny rendered as STUFFED TEDDY BEAR at miniature scale — ANIMAL_ERROR (must be animated bear at child height). |
| SC19 | FAIL | CLOTH_DRIFT (Riley), CLOTH_DRIFT (Ellis) | MT: blue bandana OK. Layla: curly yellow bow OK. Riley: 1 bow (pink headband). Ellis: orange/white soccer jersey (not red). Benny animated. |
| SC20 | FAIL | CLOTH_DRIFT (Riley), CLOTH_DRIFT (Ellis) | MT: blue bandana OK. Layla: curly yellow bow OK. Riley: 1 pink bow. Ellis: orange/blue soccer jersey. Benny: large semi-realistic proportions (borderline). |

**Tier 4 Pass: 0/20 (0%)**

---

## Priority Flags

*Highest-severity issues requiring immediate regeneration attention, ordered by severity.*

| File | Errors | Issue |
|------|--------|-------|
| S3-CH04-SC01-tier4.png | ANIMAL_ERROR, CHAR_MISSING | Benny is a photorealistic grizzly bear; Riley missing from scene |
| S3-CH04-SC17-tier4.png | ANIMAL_ERROR | Full scene rendered photorealistic; Benny is a real bear |
| S3-CH04-SC18-tier4.png | ANIMAL_ERROR | Benny rendered as a miniature stuffed teddy, not animated bear |
| S3-CH04-SC04-tier4.png | MULTI_PANEL | Composite multi-panel with embedded inset thumbnails |
| S3-CH04-SC17-tier1.png | ANIMAL_ERROR | Benny has deer antlers on head — prop corruption |
| S3-CH04-SC13-tier2.png | CHAR_DUPLICATE | Two identical Ellis boys (blond, orange/black jersey) in same scene |
| S3-CH04-SC09-tier4.png | CHAR_DUPLICATE | Two yellow-bow girls (Layla + Riley with wrong bow color) |
| S3-CH04-SC02-tier1.png | CHAR_MISSING | Only Layla + MT; Riley, Ellis, Benny absent |
| S3-CH04-SC05-tier2.png | CHAR_MISSING | Only Layla + MT; Riley, Ellis, Benny absent |
| S3-CH04-SC13-tier1.png | CHAR_MISSING | Solo Riley scene; Layla, Ellis, MT, Benny absent |
| S3-CH04-SC08-tier2.png | CHAR_MISSING, FACE_ERROR | Only MT + Ellis; MT missing full gray beard |
| S3-CH04-SC20-tier1.png | CHAR_MISSING | Master Thomas absent from closing scene |
| S3-CH04-SC20-tier2.png | CHAR_MISSING | Master Thomas absent from closing scene |
| S3-CH04-SC20-tier3.png | CHAR_MISSING | Master Thomas absent from closing scene |
| S3-CH04-SC19-tier1.png | CHAR_DRIFT (Ellis) | Ellis has dark/brown hair — must be blonde |
| S3-CH04-SC06-tier1.png | CHAR_DRIFT (Layla) | Layla has straight dark hair, not wavy/curly; yellow bow missing |
| S3-CH04-SC02-tier3.png | CHAR_DRIFT (Layla) | Layla has straight dark hair |
| S3-CH04-SC12-tier3.png | CHAR_DRIFT (Layla) | Layla has straight dark hair |
| S3-CH04-SC16-tier3.png | CHAR_DRIFT (Layla) | Layla has straight dark hair |
| S3-CH04-SC15-tier4.png | CHAR_DRIFT (Riley) | Riley has long straight dark hair instead of pigtails |

---

## Tier-Level Summary Notes

### Tier 1 — Flat cartoon style
- Master Thomas: Zero bandana compliance across all 20 scenes. This is a systematic prompt failure — the elderly woodworker character is generated without his blue bandana headband in every single scene.
- Riley: Single bow in ~75% of scenes; two bows in ~25% (SC04, SC07, SC11, SC13).
- Ellis: Shirt color mostly red/correct in T1 — best tier for Ellis compliance.
- Benny: Animated cartoon bear throughout — no ANIMAL_ERROR except SC17 (antler anomaly).
- Layla: Curly hair and yellow bow mostly correct except SC06 (straight hair).

### Tier 2 — Enhanced cartoon / semi-painted cartoon style
- Master Thomas: Zero bandana compliance. Same failure as Tier 1.
- Ellis: Orange/black jersey drift is consistent across all T2 scenes — likely a prompt-level jersey color error in the T2 generation batch.
- Riley: Single bow in ~60% of scenes; two bows in ~40%.
- Frequent character dropouts — multiple 2-character close-up scenes missing 3 expected cast members.

### Tier 3 — Painted storybook style
- Master Thomas: Bandana is present and correct in all Tier 3 scenes (unlike T1/T2). This is the best-performing tier for MT.
- Riley: Single bow failure persists — only 3 of 20 scenes have correct two bows.
- Layla: Straight-hair CHAR_DRIFT appears in 3 scenes (SC02, SC12, SC16).
- Benny: Green overalls in all T3 scenes (STYLE_DRIFT vs. reference green plaid scarf). Acceptable as animated bear at child height.
- Only 1 PASS in the entire chapter (SC19-T3).

### Tier 4 — Semi-realistic painted / cinematic illustration style
- Master Thomas: Blue bandana present in all Tier 4 scenes — 100% bandana compliance.
- Benny: THREE scenes with ANIMAL_ERROR (SC01, SC17 photorealistic bear; SC18 stuffed teddy). This is the "known worst" failure cited in the brief and confirmed.
- Ellis: Red shirt absent in virtually all T4 scenes — consistent orange/stripe/checker drift.
- Riley: Single bow in ~70% of scenes.
- SC04 multi-panel composite must be regenerated as single scene.

---

## Regeneration Recommendations

**Priority 1 — Regenerate immediately (critical errors):**
- All 40 Tier 1 + Tier 2 scenes: Add blue bandana to Master Thomas prompt. Fix Riley two-pink-bows constraint.
- Tier 4 SC01, SC17, SC18: Fix Benny ANIMAL_ERROR (animated cartoon bear only).
- Tier 4 SC04: Regenerate as single scene — remove multi-panel layout.

**Priority 2 — High-priority fixes:**
- All tiers: Enforce "TWO pink bows, TWO pigtails" for Riley — current single-bow rate is ~70%.
- Tier 2–4: Restore Ellis red soccer shirt. T2 batch has a systematic orange jersey substitution.
- Tier 1 SC19: Fix Ellis to blonde hair.
- Tier 3 scenes with Layla straight-hair: SC02, SC12, SC16 — enforce curly/wavy hair.

**Priority 3 — Cast completeness:**
- Enforce 5-character minimum per scene prompt for all group shots.
- SC13 across all tiers (Riley solo) needs MT/Layla/Ellis/Benny added.
- Closing scene SC20 across T1/T2/T3 needs Master Thomas added back.
