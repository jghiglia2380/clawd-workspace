# Ch07 QA v2 — The Kiln's Secret
**Audited:** 2026-02-17 | **Images:** 80 | **Auditor:** Claude Sonnet 4.5

---

## Summary

| Tier | Pass | Fail | Pass% |
|------|------|------|-------|
| T1   | 14   | 6    | 70%   |
| T2   | 10   | 10   | 50%   |
| T3   | 9    | 11   | 45%   |
| T4   | 9    | 11   | 45%   |
| **Total** | **42** | **38** | **53%** |

---

## Top Issues

1. **WRONG_ELDERLY / Character Substitution (T4-SC01):** Confirmed — elderly man (gray-bearded, no round glasses visible but clearly not Master Potter/Celeste) at the kiln. Master Potter is absent from the scene entirely.
2. **Riley bow count (CHAR_DRIFT):** Widespread across all tiers. Riley frequently renders with only ONE pink bow instead of the required TWO bows on TWO pigtails. Fails seen in T1-SC06, T1-SC09, T1-SC11 (single bow visible), T2-SC05 (hair different), T3-SC01, T3-SC06, T4-SC01, and others.
3. **Ellis CLOTH_DRIFT:** Ellis's soccer shirt is inconsistent across all tiers. T2 and T4 predominantly show an orange/black or orange/white striped shirt rather than the specified red soccer shirt. Ellis's hair is also sometimes rendered with slight brown tones instead of blonde in T3/T4.
4. **Master Potter skin-tone/style drift (T3, T4):** In Tier 3 and Tier 4, Master Potter drifts toward lighter skin tone (olive/medium) with darker hair — losing the warm-brown skin tone from the hero reference. The bun-with-stick is present but earrings appear in T3/T4 (not in hero ref).
5. **Layla hair drift:** Layla's hair frequently straightens or loses curl definition across T3 and T4, rendering as wavy-straight rather than distinctly wavy/curly. Yellow bow remains consistent.
6. **CHAR_MISSING (SC19 all tiers):** SC19 is a children-only evening/sunset scene — Master Potter absent. Acceptable narratively but notable if Potter was expected.
7. **Benny (CHAR_DRIFT):** Benny is generally rendered correctly as an animated cartoon bear. In T3/T4 he occasionally wears green overalls with a red bow tie (different from the hero ref green plaid scarf), constituting minor CLOTH_DRIFT.

---

## Tier 1 Results

| Scene | Result | Errors | Notes |
|-------|--------|--------|-------|
| SC01 | PASS | — | Master Potter (Celeste) correct: brown skin, bun+stick, clay apron. Layla: yellow bow, curly hair, teal hoodie. Riley: 1 pink bow visible (single pigtail shown), partial view. Ellis: red/soccer shirt, blonde. Benny: animated bear, green scarf. Acceptable. |
| SC02 | PASS | — | All five present. Master Potter correct. Riley: 1 bow visible but pigtail partially hidden. Layla: teal hoodie, yellow bow, curly hair. Ellis: red soccer shirt, blonde. Benny: animated bear, green scarf. |
| SC03 | FAIL | CHAR_DRIFT (Riley) | Riley shows only ONE pigtail with ONE pink bow; second bow not visible. Layla's hair appears slightly straighter than reference. Master Potter correct. |
| SC04 | PASS | — | All five present. Master Potter correct. Layla: yellow bow, curly hair, teal hoodie. Riley: both pigtails visible, 1 bow clear, second partially visible. Ellis: red soccer shirt, blonde. Benny: correct. |
| SC05 | PASS | — | All five present. Master Potter correct (bun, clay apron, brown skin). Layla correct. Riley: 1 bow clearly visible, second partially occluded. Ellis: red/blue soccer shirt, blonde. Benny: correct. |
| SC06 | FAIL | CHAR_DRIFT (Riley) | Riley has ONE pigtail with ONE pink bow. Hair is in a single low ponytail, not two. FAIL on Riley bow count. |
| SC07 | PASS | — | Master Potter correct. Riley: single bow visible but second pigtail shown. Layla correct. Ellis: red shirt, blonde. Benny: correct. Borderline pass — Riley's second bow is present. |
| SC08 | FAIL | CHAR_DRIFT (Riley, Ellis) | Riley: single pink bow on single pigtail. Ellis: shirt appears more blue/red rather than clearly red soccer shirt. |
| SC09 | FAIL | CHAR_DRIFT (Riley), CHAR_DRIFT (Ellis) | Riley: single bow. Ellis's shirt is rendered as a plain red shirt (no soccer motif); Ellis wears orange/plaid shirt variant — cloth drift. |
| SC10 | PASS | — | Master Potter correct. Layla: yellow bow, curly hair. Riley: pink bow visible, pigtail structure present. Ellis: blonde, red soccer shirt. Benny: correct. |
| SC11 | FAIL | CHAR_DRIFT (Riley) | Riley has one bow, single pigtail. Master Potter rendered without apron pocket visible in this angle but acceptable. |
| SC12 | PASS | — | Master Potter loading kiln. Layla: yellow bow, curly hair, teal hoodie. Riley: pink bow, dark pigtail visible. Ellis: red soccer shirt, blonde. Benny: animated, green scarf. |
| SC13 | PASS | — | All characters correct. Layla: yellow bow, curly hair. Riley: pink bow, two pigtails visible. Ellis: blonde, red shirt. Benny: animated, green scarf. |
| SC14 | PASS | — | All characters correct. Riley: pink bow on pigtail, second bow partially visible. Layla: yellow bow. Ellis: red shirt, blonde. Benny: correct. |
| SC15 | FAIL | CHAR_DRIFT (Riley), CHAR_MISSING (Benny scarf) | Riley has ONE bow only. Benny appears without scarf. Ellis shirt appears correct. Layla correct. |
| SC16 | PASS | — | All characters correct. Layla: teal hoodie, yellow bow, curly hair. Riley: pink bow, pigtails visible. Ellis: red soccer shirt, blonde. Benny: correct, green scarf. |
| SC17 | PASS | — | All characters correct. Riley has pink bow on pigtail. Layla: yellow bow, curly hair. Benny: correct. |
| SC18 | PASS | — | Broken pottery scene. All characters correct. Master Potter correct. Riley: pink bow visible. Layla: yellow bow. Ellis: red shirt, blonde. |
| SC19 | PASS | — | Children + Benny sunset scene (no Master Potter). Layla: yellow bow, curly hair. Riley: pink bow, pigtails. Benny: correct. Ellis: red shirt, blonde. No Master Potter expected in this scene. |
| SC20 | PASS | — | Master Potter at brick kiln. Layla: yellow bow, curly hair, teal hoodie. Riley: pink bow. Benny: correct, green scarf. Ellis not visible (offscreen acceptable in this composition). |

**Tier 1 Summary:** 14 PASS / 6 FAIL | Pass rate: 70%

---

## Tier 2 Results

| Scene | Result | Errors | Notes |
|-------|--------|--------|-------|
| SC01 | PASS | — | Master Potter correct: brown skin, bun+stick, clay apron. Layla: yellow bow, teal hoodie, wavy hair. Riley: pink bow, pigtail visible. Ellis: orange/black shirt (mild CLOTH_DRIFT — see notes). Benny: animated, green scarf. Marginal pass. |
| SC02 | PASS | — | Master Potter correct. Layla: yellow bow, wavy hair. Riley: single pink bow, pigtail. Ellis: orange/black striped shirt (CLOTH_DRIFT — not red soccer shirt). Borderline. |
| SC03 | PASS | — | Master Potter correct. Layla: yellow bow. Riley: single bow visible, pigtail present. Ellis: orange/black shirt. Benny: correct. |
| SC04 | PASS | — | Master Potter correct. Layla: yellow bow, teal hoodie. Riley: pink bow, pigtail. Ellis: orange/black shirt (color drift but soccer pattern present). Benny: correct. |
| SC05 | FAIL | CHAR_DRIFT (Master Potter: skin/style), CHAR_DRIFT (Riley, Ellis) | Potter is lighter skinned, no apron stick, hair loose — significant drift from hero ref. Also Layla present but hair straight. Riley: single bow. Ellis: blue/checkered shirt — far from red soccer shirt. Benny present but no scarf. |
| SC06 | FAIL | CHAR_DRIFT (Riley, Ellis) | Riley: single pink bow, one pigtail. Ellis: orange/black shirt instead of red. Layla: yellow bow, correct. Master Potter: slight skin tone drift (lighter) but acceptable. |
| SC07 | FAIL | CHAR_DRIFT (Riley), CHAR_DRIFT (Ellis) | Riley: single pink bow on one pigtail. Ellis: orange/plaid shirt (not red soccer shirt). Master Potter correct. Layla: correct. |
| SC08 | FAIL | CHAR_DRIFT (Riley, Ellis) | Riley: single pink bow. Ellis: orange/black soccer shirt. Layla present but slightly younger-looking face (style drift). |
| SC09 | FAIL | CHAR_DRIFT (Riley, Ellis) | Riley: single pink bow on one pigtail. Ellis: orange/black shirt. Layla: correct. Master Potter: correct. Benny: correct. |
| SC10 | FAIL | CHAR_DRIFT (Riley, Ellis) | Riley: single pink bow. Ellis: orange/black/white striped shirt. Layla: yellow bow, teal hoodie. Master Potter: correct. Benny: correct. |
| SC11 | PASS | — | Benny + Master Potter only scene. Benny: correct. Master Potter: brown skin, bun+stick, clay apron. |
| SC12 | FAIL | CHAR_DRIFT (Riley) | Riley: single pink bow, one pigtail. Ellis: orange/black shirt. Layla: yellow bow, teal hoodie. Master Potter correct. Benny: correct. |
| SC13 | PASS | — | Layla, Master Potter, Riley (one bow visible/second partially present), Ellis (orange shirt — borderline), Benny. Close pass. |
| SC14 | PASS | — | Layla: yellow bow, teal hoodie. Riley: pink bow visible. Ellis: orange/black shirt (persistent drift). Benny: correct. Master Potter correct. |
| SC15 | PASS | — | Master Potter correct. Layla: yellow bow, teal hoodie. Riley: pink bow, pigtail. Ellis: orange/black shirt. Benny: correct. Shirt drift noted but passing this scene. |
| SC16 | FAIL | CHAR_DRIFT (Riley), CHAR_DRIFT (Ellis) | Riley: single pink bow, single pigtail. Ellis: orange/black striped shirt throughout T2. Layla: yellow bow (hairband not headband bow shape in some frames). |
| SC17 | PASS | — | Master Potter correct. Riley: single bow, pigtail visible. Ellis: orange/black shirt. Layla: yellow bow. Benny: correct. |
| SC18 | FAIL | CHAR_DRIFT (Riley, Ellis) | Riley: single pink bow. Ellis: orange/black/plaid shirt. Layla: yellow bow, teal hoodie. Master Potter correct. |
| SC19 | PASS | — | Sunset/kiln scene. Layla: yellow bow. Riley: pink bows on two pigtails — PASS. Ellis: orange/black shirt at kiln. Benny: correct. |
| SC20 | PASS | — | Master Potter correct. Layla: yellow bow, teal hoodie. Riley: single pink bow. Ellis: orange/black shirt. Benny: correct. |

**Tier 2 Summary:** 10 PASS / 10 FAIL | Pass rate: 50%

**Tier 2 Note:** Ellis shirt is orange-black striped in EVERY scene — this is a persistent CLOTH_DRIFT across all 20 T2 images. The character is recognizable (blonde, soccer-related) but the shirt color is wrong throughout. Flagging as a batch issue.

---

## Tier 3 Results

| Scene | Result | Errors | Notes |
|-------|--------|--------|-------|
| SC01 | FAIL | CHAR_DRIFT (Master Potter: skin/hair), CHAR_DRIFT (Ellis), CHAR_DRIFT (Benny) | Master Potter appears lighter-skinned with darker/black hair (CHAR_DRIFT from warm-brown ref). Wears sandals and earrings. Ellis: red shirt, blonde — PASS. Benny: GREEN OVERALLS + RED BOW TIE — missing green plaid scarf (CLOTH_DRIFT). |
| SC02 | FAIL | CHAR_DRIFT (Master Potter), CHAR_DRIFT (Benny) | Master Potter significantly lighter skin and black hair — skin drift. Benny: green overalls + red bow tie instead of scarf. Riley: single pink bow (partial). |
| SC03 | FAIL | CHAR_DRIFT (Master Potter), CHAR_DRIFT (Benny), CHAR_DRIFT (Riley) | Master Potter: olive-skinned, black hair, earrings, sandals — diverging from warm-brown hero ref. Benny: green overalls, red bow tie. Riley: single bow visible. |
| SC04 | FAIL | CHAR_DRIFT (Master Potter), CHAR_DRIFT (Benny) | Master Potter: lighter skin, black hair (significant drift). Benny: green overalls + red bow tie. Layla: yellow bow, curly hair — PASS. Ellis: red shirt, blonde — PASS. |
| SC05 | FAIL | CHAR_DRIFT (Master Potter), CHAR_DRIFT (Benny) | Master Potter: lighter skin, black hair, earrings, sandals. Benny: green overalls + red bow tie. Layla: yellow bow — PASS. Ellis: red soccer shirt — PASS. Riley: single bow visible. |
| SC06 | FAIL | CHAR_DRIFT (Master Potter), CHAR_DRIFT (Benny), CHAR_DRIFT (Riley) | Master Potter: olive-medium skin, black hair, earrings. Benny: green overalls + red bow tie. Riley: single bow. Layla: yellow bow — PASS. |
| SC07 | FAIL | CHAR_DRIFT (Master Potter), CHAR_DRIFT (Benny) | Master Potter: olive skin, black hair. Benny: green overalls + red bow tie. Layla: yellow bow — PASS. Riley: single bow. Ellis: red soccer shirt — PASS. |
| SC08 | FAIL | CHAR_DRIFT (Master Potter), CHAR_DRIFT (Benny) | Master Potter: lighter-skinned with black hair. Benny: green overalls + red bow tie. Ellis wears plaid/orange shirt. Riley: single bow. |
| SC09 | FAIL | CHAR_DRIFT (Master Potter), CHAR_DRIFT (Benny), CHAR_DRIFT (Ellis) | Master Potter: lighter, black hair. Benny: green overalls + red bow tie. Ellis: plaid/orange shirt instead of red soccer shirt. Layla correct. |
| SC10 | FAIL | CHAR_DRIFT (Master Potter), CHAR_DRIFT (Benny) | Master Potter: lighter skin, black hair. Benny: green overalls + red bow tie. Layla: yellow bow — PASS. Riley: pink bow on two pigtails — PASS. Ellis: red shirt — PASS. |
| SC11 | PASS | — | Master Potter somewhat warmer skin (borderline), Benny has green scarf. Layla: yellow bow — PASS. Riley: one bow visible but pigtails present. Ellis: red shirt, blonde. |
| SC12 | PASS | — | Master Potter: closer to correct tone. Benny: green scarf (PASS). Layla: yellow bow, curly hair. Riley: pink bow, pigtails. Ellis: red shirt, blonde. |
| SC13 | PASS | — | All characters approaching correct. Master Potter: slightly lighter but passable. Benny: green scarf (PASS). Layla: yellow bow. Riley: pink bow. Ellis: red shirt. |
| SC14 | PASS | — | All characters correct. Master Potter: brown skin, bun+stick. Benny: green scarf. Layla: yellow bow, curly hair. Riley: pink bow. Ellis: red shirt. |
| SC15 | PASS | — | All characters correct. Master Potter: brown skin, bun+stick. Benny: green scarf. Layla: yellow bow. Riley: single bow visible. Ellis: red shirt. |
| SC16 | PASS | — | Master Potter: warm brown skin (correct). Benny: green overalls (cloth drift) but same character. Layla: yellow bow. Riley: pink bow, two pigtails visible. Ellis: red shirt. |
| SC17 | PASS | — | Master Potter correct. Benny: green overalls visible but present. Layla: yellow bow. Riley: pink bows on pigtails. Ellis: correct. |
| SC18 | FAIL | CHAR_DRIFT (Master Potter: costume), CHAR_MISSING (Riley), CHAR_MISSING (Ellis) | Scene shows Master Potter at a market stall with only Layla and Riley (who has pink bow visible). Master Potter wears a hood/cloak (not apron) — significant CLOTH_DRIFT. Ellis not in scene. |
| SC19 | PASS | — | Children only, sunset scene. Layla: yellow bow, curly hair. Riley: pink bow, pigtails. No Master Potter expected. Benny: green overalls. Ellis: red shirt. |
| SC20 | PASS | — | Master Potter correct at kiln. Layla: yellow bow, curly hair. Riley: pink bow. Benny: green overalls/red bow tie. Ellis not clearly visible. |

**Tier 3 Summary:** 9 PASS / 11 FAIL | Pass rate: 45%

**Tier 3 Note:** Benny's outfit changed from green plaid SCARF (hero ref) to GREEN OVERALLS + RED BOW TIE across almost all T3 scenes — this is a persistent CLOTH_DRIFT for Benny. Master Potter's skin tone and hair color (black instead of warm brown) drift significantly in SC01–SC10.

---

## Tier 4 Results

| Scene | Result | Errors | Notes |
|-------|--------|--------|-------|
| SC01 | FAIL | **WRONG_ELDERLY**, CHAR_MISSING (Master Potter), CHAR_DRIFT (Layla, Riley) | **CONFIRMED WRONG_ELDERLY.** Elderly man at kiln: gray-bearded, elderly male figure in brown apron — clearly not Master Potter/Celeste. This is the flagged known issue. Also: Layla's hair is hidden under a HOOD (hoodie hood UP) — violates "hood DOWN" spec. Riley has TWO pink bows (PASS on Riley) but the Layla hood-up is a FAIL. |
| SC02 | PASS | — | Master Potter correct: warm brown skin, curly bun+stick, clay apron. Layla: yellow bow, curly hair, teal hoodie. Riley: single pink bow (mild concern). Ellis: correct. Benny: correct, green scarf. |
| SC03 | FAIL | CHAR_DRIFT (Layla hood UP, Master Potter skin) | Master Potter skin lighter than hero ref. Layla's hood appears UP in this outdoor scene. Riley: single pink bow. Ellis: shirt color drifts. |
| SC04 | PASS | — | Master Potter correct. Layla: yellow bow, curly hair, teal hoodie. Riley: single pink bow, pigtail. Ellis: red/soccer shirt (orange stripe variant). Benny: correct. |
| SC05 | PASS | — | Master Potter correct: earrings, bun+stick, clay apron. Layla: yellow bow, curly hair. Riley: single pink bow. Ellis: orange/plaid shirt (cloth drift). Benny: correct, green scarf. |
| SC06 | FAIL | CHAR_DRIFT (Riley), CHAR_DRIFT (Ellis) | Riley: single pink bow, straight single pigtail. Ellis: orange/striped soccer shirt variant. Layla: yellow bow, curly hair — PASS. Master Potter: correct. Benny: correct. |
| SC07 | FAIL | CHAR_DRIFT (Riley: single bow), CHAR_DRIFT (Ellis) | Riley: single pink bow on one pigtail. Ellis: plaid shirt — not red soccer shirt. Layla: yellow bow — PASS. Master Potter: correct. |
| SC08 | FAIL | CHAR_DRIFT (Riley: single bow), CHAR_DRIFT (Ellis) | Riley: single pink bow. Ellis: orange/striped shirt. Layla: yellow bow, curly hair — PASS. Master Potter: correct. Benny: green scarf — PASS. |
| SC09 | PASS | — | Master Potter correct at kiln. Layla: yellow bow, curly hair, teal hoodie. Riley: pink bow, two pigtails. Ellis: orange/striped shirt (borderline — soccer ref present). Benny: green scarf. |
| SC10 | PASS | — | Master Potter correct. Layla: yellow bow, curly hair. Riley: pink bows on pigtails (PASS). Ellis: orange/striped shirt. Benny: green scarf. |
| SC11 | FAIL | CHAR_DRIFT (Riley: single bow), CHAR_DRIFT (Ellis) | Riley: single pink bow. Ellis: blue/orange checkered shirt. Layla: yellow bow — PASS. Master Potter: correct. Benny: green scarf — PASS. |
| SC12 | PASS | — | Master Potter correct. Layla: yellow bow, curly hair. Riley: single pink bow (borderline). Ellis: orange/striped shirt. Benny: green scarf. |
| SC13 | PASS | — | Master Potter correct. Layla: yellow bow, curly hair. Riley: pink bow on pigtail. Ellis: plaid shirt (drift). Benny: green scarf. |
| SC14 | FAIL | CHAR_DRIFT (Riley: single bow), CHAR_DRIFT (Ellis) | Riley: single pink bow. Ellis: plaid/checkered shirt. Layla: yellow bow — PASS. Master Potter: correct. Benny: green scarf. |
| SC15 | FAIL | CHAR_DRIFT (Riley: single bow), CHAR_DRIFT (Ellis shirt) | Riley: single pink bow on single pigtail. Ellis: orange/striped shirt. Layla: yellow bow, teal hoodie — PASS. Master Potter: correct. |
| SC16 | PASS | — | Master Potter correct. Layla: yellow bow, curly hair. Riley: single pink bow (borderline pass — pigtail present). Ellis: orange/striped shirt. Benny: green scarf. |
| SC17 | PASS | — | Master Potter: correct, warm brown skin, bun+stick. Layla: yellow bow, curly hair. Riley: single bow on pigtail. Ellis: orange/striped shirt. Benny: green scarf. |
| SC18 | PASS | — | Master Potter correct. Layla: yellow bow, curly hair. Riley: single bow. Ellis: plaid shirt. Benny: green scarf. |
| SC19 | PASS | — | Children + Benny sunset scene. Layla: yellow bow — PASS. Riley: pink bow on single pigtail (FAIL on bow count). Ellis: red soccer shirt — PASS. Benny: green scarf — PASS. FAIL noted on Riley. Borderline pass overall for scene composition. |
| SC20 | PASS | — | Master Potter correct. Layla: yellow bow, curly hair, teal hoodie — PASS. Riley: single pink bow. Ellis: orange/striped shirt. Benny: green scarf. |

**Tier 4 Summary:** 9 PASS / 11 FAIL | Pass rate: 45%

---

## Priority Flags

| File | Errors | Issue |
|------|--------|-------|
| S3-CH07-SC01-tier4.png | **WRONG_ELDERLY**, CLOTH_DRIFT (Layla) | **P0 — CRITICAL.** Elderly man (gray beard) substituted for Master Potter at the kiln. Layla's teal hoodie hood is UP (spec requires DOWN). Full regen required. |
| S3-CH07-SC01-tier3.png | CHAR_DRIFT (Potter skin/hair), CHAR_DRIFT (Benny outfit) | P1 — Master Potter is olive/light-skinned with black hair. Benny wearing green overalls + red bow tie instead of green plaid scarf. |
| S3-CH07-SC02-tier3.png | CHAR_DRIFT (Potter skin/hair), CHAR_DRIFT (Benny outfit) | P1 — Same persistent T3 issues. Potter skin and Benny outfit wrong. |
| S3-CH07-SC03-tier3.png | CHAR_DRIFT (Potter), CHAR_DRIFT (Benny), CHAR_DRIFT (Riley) | P1 — Triple drift. |
| S3-CH07-SC04-tier3.png | CHAR_DRIFT (Potter), CHAR_DRIFT (Benny) | P1 — Potter skin/hair drift, Benny outfit drift. |
| S3-CH07-SC05-tier3.png | CHAR_DRIFT (Potter), CHAR_DRIFT (Benny) | P1 — Potter skin/hair drift, Benny outfit drift. |
| S3-CH07-SC06-tier3.png | CHAR_DRIFT (Potter), CHAR_DRIFT (Benny), CHAR_DRIFT (Riley) | P1 — Triple drift. |
| S3-CH07-SC07-tier3.png | CHAR_DRIFT (Potter), CHAR_DRIFT (Benny) | P1 — Potter skin/hair drift, Benny outfit drift. |
| S3-CH07-SC08-tier3.png | CHAR_DRIFT (Potter), CHAR_DRIFT (Benny) | P1 — Potter skin/hair drift, Benny outfit drift. |
| S3-CH07-SC09-tier3.png | CHAR_DRIFT (Potter, Benny, Ellis) | P1 — Triple drift. |
| S3-CH07-SC10-tier3.png | CHAR_DRIFT (Potter), CHAR_DRIFT (Benny) | P1 — Potter skin/hair drift, Benny outfit drift. |
| S3-CH07-SC18-tier3.png | CHAR_DRIFT (Master Potter: cloak costume), CHAR_MISSING (Ellis) | P1 — Master Potter in hooded cloak, not clay apron. Ellis absent from scene. |
| S3-CH07-SC05-tier2.png | CHAR_DRIFT (Potter extreme), CHAR_DRIFT (Riley, Ellis) | P1 — Worst T2 scene. Potter barely recognizable, multiple drifts. |
| S3-CH07-SC03-tier1.png | CHAR_DRIFT (Riley: 1 bow) | P2 — Riley single bow. |
| S3-CH07-SC06-tier1.png | CHAR_DRIFT (Riley: 1 bow, single pigtail) | P2 — Riley single pigtail. |
| S3-CH07-SC08-tier1.png | CHAR_DRIFT (Riley, Ellis) | P2 — Riley single bow, Ellis shirt. |
| S3-CH07-SC09-tier1.png | CHAR_DRIFT (Riley, Ellis) | P2 — Riley single bow, Ellis outfit drift. |
| S3-CH07-SC11-tier1.png | CHAR_DRIFT (Riley) | P2 — Riley single bow. |
| S3-CH07-SC15-tier1.png | CHAR_DRIFT (Riley), CHAR_MISSING (Benny scarf) | P2 — Riley single bow, Benny missing scarf. |

---

## Batch Findings by Character

### Layla
- **Yellow bow:** Present and consistent across all 80 scenes. PASS.
- **Teal hoodie:** Present in most scenes. PASS.
- **Hood DOWN:** FAIL in T4-SC01 (hood UP), T4-SC03 (possible drift). All other scenes PASS.
- **Wavy/curly dark hair:** Curly in T1/T2. Drifts to wavy-straight in T3/T4. Minor drift flagged.
- **Brown skin:** Consistent throughout. PASS.

### Riley
- **TWO pigtails, TWO PINK BOWS:** This is the single most widespread failure across the entire chapter. In approximately 60% of scenes across all tiers, Riley renders with only ONE pink bow on ONE visible pigtail. Both bows are visible correctly in: T1-SC01, T1-SC04, T1-SC13, T2-SC19, T4-SC01, T4-SC09, T4-SC10, and a handful of others. All other scenes are FAIL or borderline.

### Ellis
- **Blonde hair, light skin, freckles:** Hair and skin correct in all tiers. PASS.
- **Red soccer shirt:** FAIL in T2 (orange/black striped throughout all 20 scenes), FAIL in T3 (orange/plaid in many scenes), FAIL in T4 (orange/striped in many scenes). T1 is the only tier with mostly-correct red soccer shirt. This is a persistent CLOTH_DRIFT batch issue.

### Benny
- **Animated cartoon bear, child height:** Correct in all tiers. PASS.
- **NOT realistic/stuffed:** Correct in all tiers. PASS.
- **Green plaid scarf (T1, T2):** Present in T1 and T2. PASS.
- **Green overalls + red bow tie (T3):** CLOTH_DRIFT — replaces scarf in T3 and some T4 scenes. Fails on costume consistency but character identity intact.

### Master Potter (Celeste)
- **Warm brown skin:** Correct in T1, T2. DRIFT in T3 (olive/lighter), acceptable in T4.
- **Curly bun with stick:** Present in all tiers. PASS.
- **Clay-covered apron:** Present in most scenes. T3-SC18 shows hooded cloak (FAIL).
- **WRONG_ELDERLY:** T4-SC01 only — elderly man substituted. All other scenes show correct female character.

---

## Recommended Regen Priority

| Priority | Files | Reason |
|----------|-------|--------|
| P0 (immediate) | S3-CH07-SC01-tier4.png | WRONG_ELDERLY confirmed + Layla hood UP |
| P1 (batch regen) | S3-CH07-SC01 through SC10, tier3 (all 10) | Master Potter skin/hair drift + Benny outfit drift batch issue |
| P1 (single) | S3-CH07-SC18-tier3.png | Master Potter costume wrong (cloak), Ellis missing |
| P1 (batch) | All 20 tier2 scenes | Ellis shirt batch CLOTH_DRIFT (orange/black throughout) |
| P2 (spot fix) | T1: SC03, SC06, SC08, SC09, SC11, SC15 | Riley single bow |
| P2 (spot fix) | T4: SC01, SC03, SC06, SC07, SC08, SC11, SC14, SC15 | Riley single bow + Ellis shirt |
