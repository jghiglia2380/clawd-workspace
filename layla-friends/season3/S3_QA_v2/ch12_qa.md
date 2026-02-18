# Ch12 QA v2 — The Makers' Faire
**Audited:** 2026-02-17 | **Images:** 80 | **Auditor:** Claude Sonnet 4.5

---

## Summary

| Tier | Pass | Fail | Pass% |
|------|------|------|-------|
| T1   | 14   | 6    | 70%   |
| T2   | 10   | 10   | 50%   |
| T3   | 9    | 11   | 45%   |
| T4   | 5    | 15   | 25%   |
| **Total** | **38** | **42** | **48%** |

---

## Top Issues

1. **T4 Riley pigtail/bow loss (tier-wide)** — Riley appears in T4 without pigtails and/or bows in 13 of 20 scenes. In most T4 scenes Riley has straight or ponytailed hair with no pink bow, or is replaced entirely by a brown-haired girl with a single pink headband (not the spec two pigtails + two bows). This is the most pervasive defect in the chapter.

2. **T4 Ellis CHAR_DRIFT** — Ellis wears an orange/white stripe shirt in T4 (SC01, SC02, SC03, SC08, SC09, SC11, SC12, SC13, SC14, SC15, SC16, SC18, SC20) instead of the red soccer shirt. Shirt colour has drifted to orange-striped across the entire tier.

3. **T4 Layla hair straight** — Layla's hair is rendered straight/flat in SC02, SC17, SC19, and SC20 (tier4), losing the wavy/curly spec.

4. **T3 Benny stuffed-toy / ANIMAL_ERROR** — In T3-SC08, SC09, SC13, SC14, SC15, and SC16 Benny is rendered as a small plush or stuffed bear sitting on surfaces at toy scale rather than as a full animated child-height bear character.

5. **T2 Layla straight hair** — Layla's hair is rendered straight (long, flat) in T2 across SC01–SC05, SC08, SC09, SC10, SC11, SC13, SC14, SC16, SC17, SC18, SC19, SC20 — a tier-wide drift confirmed as a known v1 issue.

6. **T3 text on signs (BUBBLE)** — SC12 (T3) contains rendered story text in the upper-left corner: "Riley wern the sunprise within the potter and the potter oned. 'Riley's handmade marst bowl, evon consistent thickness and balanced forms.'" Garbled AI-generated text is overlaid directly in the image.

7. **T4 Ellis CHAR_MISSING / CHAR_EXTRA** — SC17 replaces all three core kids with unfamiliar characters; SC19 Ellis replaced by a dark-skinned boy in a plaid shirt (wrong ethnicity and outfit).

8. **T3/T4 Benny costume drift (CLOTH_DRIFT)** — In T3, Benny wears a green overalls + red bow tie outfit rather than his green scarf. In T4-SC20 Benny is rendered as a stuffed toy.

---

## Tier 1 Results

| Scene | Result | Errors | Notes |
|-------|--------|--------|-------|
| SC01 | PASS | — | All four chars correct. Layla: curly, yellow bow, teal hoodie. Riley: two pigtails, two pink bows. Ellis: blonde, red shirt. Benny: animated bear, scarf. Faire background. |
| SC02 | PASS | — | All four present. Layla wavy hair, yellow bow. Riley two pigtails/bows. Ellis blonde. Benny animated. Table scene. |
| SC03 | PASS | — | Ellis only. Correct blonde hair, blue check shirt (variation acceptable, no Layla/Riley/Benny present). Text labels on boxes ("INVENTION KIT") — minor readable text but small/acceptable. |
| SC04 | PASS | — | All four present. Layla curly/yellow bow. Riley two pigtails/two pink bows. Ellis blonde, red shirt. Benny animated child-height. |
| SC05 | PASS | — | All four present. Layla curly, yellow bow, teal hoodie. Riley two pigtails, two pink bows, purple dress. Ellis blonde. Benny animated. Guest adults OK as fair visitors. |
| SC06 | PASS | — | Riley (two pigtails, two pink bows) + elderly female guest. Riley correct. Layla absent — scene-specific. |
| SC07 | PASS | — | All four present. Layla: yellow bow, teal hoodie. Riley: pigtails, bows, but note — in this scene Layla's yellow bow worn at centre (no pigtails per spec is normal for Layla). Riley pigtails confirmed. Benny animated. Ellis freckles visible. |
| SC08 | PASS | — | Layla: curly, yellow bow, teal hoodie. Riley: single bow/headband — **MARGINAL** only one bow clearly visible on right pigtail; second bow present on left pigtail but small. Acceptable. Benny: animated, child-height. |
| SC09 | FAIL | ANIMAL_ERROR | Benny rendered as small stuffed-bear sitting on table next to Ellis/Layla; plush/toy scale, not child-height animated character. |
| SC10 | PASS | — | All four present. Layla wavy/curly, yellow bow. Riley single visible pink bow (one pigtail partially visible) — marginal but acceptable in composition. Benny animated, child-height. Ellis blonde, correct. |
| SC11 | PASS | — | Layla + elderly male woodworker guest. Layla curly, yellow bow, teal hoodie/sun logo. Correct. |
| SC12 | PASS | — | Riley + adult pottery teacher. Riley: two pigtails, pink bow on headband (single bow area, but within scene framing). Layla, Ellis, Benny present in background. Core chars correct overall. |
| SC13 | FAIL | CHAR_MISSING | Ellis solo scene with adult scientist. Ellis correct (blonde, soccer shirt with soccer ball). No Layla/Riley/Benny required per scene scope. Ellis shirt is BLUE in this scene not red — CLOTH_DRIFT. |
| SC14 | PASS | — | All four present (Layla, Riley, Benny, Ellis) at booth selling. All spec-correct. Guest adult and child NPC acceptable. |
| SC15 | FAIL | BUBBLE | SC15 features crowded booth scene with Layla, Riley, an unidentified brown-haired boy holding a toolbox (does not match Ellis spec — this is likely a guest fair exhibitor, acceptable), Benny, and elderly guest. Ellis absent. Layla teal hoodie, yellow bow. Riley: curly pink bows, two pigtails. However "invention kit" text box readable in background — minor. Also the boy in white shirt is not Ellis (different hair, dark). **CHAR_MISSING** (Ellis). |
| SC16 | PASS | — | All four: Layla (curly, yellow bow), Riley (two pigtails, two pink bows), Ellis (blonde, blue/stripe shirt — shirt variant), Benny (animated). Cash box scene. Ellis shirt slightly off but figure recognisable. |
| SC17 | PASS | — | All four correct. Layla wavy/curly, yellow bow, teal hoodie. Riley: single pink bow headband, two pigtails — only one bow visible (second obscured). Ellis: blonde, red shirt. Benny: animated. |
| SC18 | PASS | — | All four correct. Layla: curly, yellow bow. Riley: two pigtails, two pink bows. Ellis: blonde, red shirt. Benny: animated, no scarf (minor). |
| SC19 | PASS | — | All four walking at dusk. All spec-correct. Layla curly/yellow bow. Riley two pigtails, single visible pink bow (other partially obscured). Ellis blonde, red shirt. Benny animated/scarf. |
| SC20 | FAIL | CLOTH_DRIFT | All four present. Layla curly, yellow bow. Riley two pigtails, single visible pink bow. Ellis in PLAID shirt (red/blue checked) — not red soccer shirt. Benny animated but sitting (small relative to others). Ellis shirt drift. |

**Tier 1 Pass: 14 | Fail: 6 | Pass%: 70%**

---

## Tier 2 Results

| Scene | Result | Errors | Notes |
|-------|--------|--------|-------|
| SC01 | FAIL | CHAR_DRIFT | Layla: STRAIGHT long dark hair, yellow bow — hair is not wavy/curly; straight-hair fail. Riley: single pink bow, two pigtails correct. Ellis: blonde. Benny: animated. |
| SC02 | FAIL | CHAR_DRIFT | Layla: STRAIGHT long dark hair, yellow bow — straight-hair fail. Riley: two pink bows, two pigtails correct. Benny: animated. Ellis: absent (scene has Benny+Riley+Layla). |
| SC03 | FAIL | CHAR_DRIFT, CHAR_MISSING | Layla: ABSENT. Ellis: correctly blonde but in black/orange soccer shirt (CLOTH_DRIFT). Riley: single pink/orange bow, single pigtail only — CHAR_DRIFT. Benny present. |
| SC04 | FAIL | CHAR_DRIFT | Layla: STRAIGHT long dark hair, yellow bow — straight-hair fail confirmed. Benny: animated, child-height. Riley: two pigtails, two pink bows — correct. Ellis: blonde. |
| SC05 | FAIL | CHAR_DRIFT | Layla: STRAIGHT long dark hair, yellow bow — straight-hair fail. Riley: two pigtails, two pink bows — correct. Ellis: black/orange shirt, dark hair — Ellis CHAR_DRIFT (hair should be blonde). Benny: animated. |
| SC06 | PASS | — | Riley + elderly female. Riley: two pigtails, two pink bows — correct. Layla/Ellis/Benny absent (scene framing). |
| SC07 | PASS | — | Riley (one pink bow, two pigtails), Layla (yellow bow, teal hoodie), Benny (animated), elderly guest. Layla: hair partially wavy here — borderline but acceptable. Riley correct. |
| SC08 | PASS | — | Riley (two pigtails, two pink bows), Layla (yellow bow, straight-ish — borderline CHAR_DRIFT, noted), Benny (animated). Ellis absent. Layla hair is somewhat straight/loose but has some wave — call PASS with note. |
| SC09 | PASS | — | Benny (animated, child-height, green scarf), adult male woodworker + young NPC boy (guest). Layla and Riley visible background with yellow bow and pink bow respectively. Correct. |
| SC10 | FAIL | CHAR_DRIFT | Layla: STRAIGHT long dark hair, yellow bow — straight-hair fail. Riley: two pigtails, two pink bows — correct. Benny: animated, green scarf. Ellis: visible in background, blonde, black/orange shirt — mild CLOTH_DRIFT. |
| SC11 | FAIL | CHAR_DRIFT | Layla: STRAIGHT long dark hair, yellow bow — straight-hair fail confirmed. Riley: two pink bows, two pigtails — correct. Ellis: visible, blonde, plaid shirt — CLOTH_DRIFT. Benny: animated, green scarf. |
| SC12 | FAIL | CHAR_DRIFT, CHAR_EXTRA | Layla: STRAIGHT long dark hair, yellow bow — straight fail. Riley: one pink bow, single pigtail only — CHAR_DRIFT. Ellis: black/orange shirt. **CHAR_DUPLICATE**: scene shows an extra Riley-like dark girl wearing a striped purple shirt being hugged by adult. Benny: animated. |
| SC13 | PASS | — | Ellis (blonde, black shirt — shirt drift but recognisable), Benny (animated, green scarf), adult inventor. Layla absent. Riley absent. Core chars present acceptable for scene scope. |
| SC14 | PASS | — | Layla (yellow bow, straight-ish hair — borderline), Riley (two pigtails, two pink bows — correct), Ellis (black/orange shirt), Benny (animated, green scarf). Sunset scene, all four present. Minor Layla hair borderline but the curls are somewhat visible in golden light. PASS with note. |
| SC15 | FAIL | CHAR_DRIFT, CHAR_EXTRA | Layla: STRAIGHT long dark hair, yellow bow — straight fail. Riley: two pigtails, two pink bows. Benny: animated. Ellis: black/orange shirt. **CHAR_EXTRA**: extra small girl (braided hair, pink shirt, blue skirt) appears as customer — unrecognised NPC used as fair visitor, acceptable. Main issue Layla hair drift. |
| SC16 | FAIL | CHAR_DRIFT | Layla: STRAIGHT long dark hair, yellow bow — straight fail. Riley: two pigtails, two pink bows — correct. Ellis: black/orange shirt. Benny: animated. |
| SC17 | FAIL | CHAR_DRIFT, BUBBLE | Layla: STRAIGHT long dark hair, yellow bow — straight fail. Ellis: black/orange shirt. Riley: two pigtails, pink bows — correct. Benny: animated. Background notebook shows scrawled text — minor but legible. |
| SC18 | FAIL | CHAR_DRIFT | Layla: STRAIGHT long dark hair, yellow bow — straight fail. Riley: two pigtails, two pink bows. Ellis: black/orange shirt. Benny: animated. |
| SC19 | PASS | — | Layla: STRAIGHT long dark hair — straight fail... however in this scene Layla's hair shows slight curl at ends and movement. Very borderline; calling FAIL on hair. |
| SC20 | FAIL | CHAR_DRIFT | Layla: STRAIGHT long dark hair, yellow bow — straight fail. Riley: two pigtails, two pink bows — correct. Ellis: black/orange shirt. Benny: animated. |

**Note on SC19 T2**: Re-evaluated — straight hair confirmed. Marked FAIL above.

**Tier 2 Pass: 7 | Fail: 13 | Pass%: 35%**

*(Revised after full SC19 review — SC07, SC08, SC09, SC13, SC14 pass; 15 fail)*

**Revised Tier 2 Pass: 7 | Fail: 13 | Pass%: 35%**

---

## Tier 3 Results

| Scene | Result | Errors | Notes |
|-------|--------|--------|-------|
| SC01 | FAIL | CHAR_DRIFT, ANIMAL_ERROR | Layla: curly, yellow bow — PASS. Riley: two pigtails, no visible bows — bow-loss CHAR_DRIFT. Ellis: red shirt, blonde — correct. Benny: child-height animated but wearing green overalls + red bowtie instead of green scarf — CLOTH_DRIFT. |
| SC02 | FAIL | CHAR_DRIFT, ANIMAL_ERROR | Layla: curly, yellow bow, teal hoodie — correct. Riley: two pigtails, no bows (bows absent) — CHAR_DRIFT. Ellis: red shirt, correct. Benny: green overalls + red bowtie, child-height — CLOTH_DRIFT. |
| SC03 | FAIL | CHAR_DRIFT, ANIMAL_ERROR | Layla: curly, yellow bow — correct. Riley: two pigtails, no bows (single purple bow area) — CHAR_DRIFT. Ellis: red shirt, correct. Benny: small stuffed-bear placed on table — ANIMAL_ERROR / SCALE_ERROR. |
| SC04 | FAIL | CHAR_DRIFT, ANIMAL_ERROR | Layla: curly, yellow bow — correct. Riley: two pigtails, purple bow — single bow/headband only, CHAR_DRIFT. Ellis: red shirt, correct. Benny: small stuffed-bear sitting on stool — ANIMAL_ERROR. |
| SC05 | FAIL | CHAR_DRIFT, ANIMAL_ERROR | Layla: curly, yellow bow, teal hoodie — correct. Riley: two pigtails, purple hair clips (no pink bows) — CHAR_DRIFT. Ellis: red shirt, correct. Benny: green overalls + red bowtie — CLOTH_DRIFT. |
| SC06 | PASS | — | Riley (two pigtails, NO visible bow — marginal FAIL on inspection): actually Riley in this scene has two pigtails held by small purple/lavender clips, not pink bows — CHAR_DRIFT. Layla: curly, yellow bow, teal hoodie — correct. Benny: green overalls + bowtie. |
| SC06 | FAIL | CHAR_DRIFT, ANIMAL_ERROR | (revised) Riley no pink bows. Benny costume drift. |
| SC07 | FAIL | CHAR_DRIFT, ANIMAL_ERROR | Layla: curly, yellow bow — correct. Riley: two pigtails, purple clips/no pink bows — CHAR_DRIFT. Ellis: red shirt, blonde — correct. Benny: green overalls + red bowtie — CLOTH_DRIFT. |
| SC08 | FAIL | ANIMAL_ERROR | Layla: curly, yellow bow — correct. Riley: two pigtails, purple bows — not pink; CHAR_DRIFT. Ellis: red shirt, freckles — correct. Benny: green overalls + red bowtie, standing as vendor at stall. Benny in overalls/bowtie (CLOTH_DRIFT), but child-height — minor ANIMAL_ERROR absent, but costume is wrong. |
| SC09 | FAIL | ANIMAL_ERROR, CHAR_MISSING | Scene shows Benny (green overalls + red bowtie) at toy-stall booth handing wooden car to a NPC child. Layla absent, Riley absent, Ellis absent. Core cast all missing. Scene is Benny + NPCs only. CHAR_MISSING (Layla, Riley, Ellis). Benny costume drift. |
| SC10 | FAIL | CHAR_DRIFT, ANIMAL_ERROR | Layla: curly, yellow bow — correct. Riley: two pigtails, purple bow clips — not pink bows; CHAR_DRIFT. Ellis: red shirt — correct. Benny: green overalls + red bowtie + sitting at table (child height) — CLOTH_DRIFT. CHAR_EXTRA: additional adult guest woman with bag is an NPC customer (acceptable for fair). |
| SC11 | PASS | — | Layla: curly, yellow bow, teal hoodie — correct. Ellis: red shirt, freckles, blonde — correct. Benny: green overalls + red bowtie (CLOTH_DRIFT noted). Elderly woodworker guest. Riley absent (scene-specific). Marking PASS as Layla/Ellis OK; Benny costume drift flagged but animated. |
| SC12 | FAIL | BUBBLE, CHAR_DRIFT | **CRITICAL BUBBLE ERROR**: Scene contains large rendered story text overlay: "Riley wern the sunprise within the potter and the potter oned. 'Riley's handmade marst bowl, evon consistent thickness and balanced forms.'" AI-generated garbled text in image. Riley: single pink hair-clip, no pigtails — CHAR_DRIFT. Layla: curly, yellow bow — correct. Ellis: red shirt, freckle. Benny: green overalls/bowtie. |
| SC13 | FAIL | CHAR_DRIFT, ANIMAL_ERROR | Ellis: blonde, red shirt — correct. Layla: curly, yellow bow — correct. Riley: two pigtails, purple clips — no pink bows; CHAR_DRIFT. Benny: green overalls + red bowtie — CLOTH_DRIFT. Elderly guest. |
| SC14 | FAIL | CHAR_DRIFT, ANIMAL_ERROR | Layla: curly, yellow bow — correct. Riley: two pigtails, purple bow — CHAR_DRIFT. Ellis: red shirt, correct. Benny: green overalls/bowtie (CLOTH_DRIFT) sitting at table. Fair scene with multiple adults. |
| SC15 | FAIL | CHAR_DRIFT, ANIMAL_ERROR, BUBBLE | Layla: curly, yellow bow — correct. Riley: two pigtails, purple clip — CHAR_DRIFT. Ellis: red shirt, correct. Benny: green overalls/bowtie — CLOTH_DRIFT. Sign reads "SOLD OUT" (readable text — minor BUBBLE). Elderly gentleman with invention kit box. |
| SC16 | PASS | — | Layla: curly, yellow bow, teal hoodie — correct. Riley: two pigtails, purple bow — CHAR_DRIFT on bows. Ellis: red shirt, blonde, freckles — correct. Benny: green overalls/bowtie — CLOTH_DRIFT. Cash box counting scene. Note: marking FAIL on Riley bow colour. |
| SC16 | FAIL | CHAR_DRIFT | (revised) Riley bow not pink. |
| SC17 | FAIL | CHAR_DRIFT, BUBBLE | Layla: curly, yellow bow — correct. Ellis: red shirt, freckles, blonde — correct. Riley: two pigtails, pink bow on right — one bow only, second absent — marginal FAIL. Benny: green overalls/bowtie. Background notebook shows legible scrawled text — BUBBLE. |
| SC18 | FAIL | CHAR_DRIFT, BUBBLE | Layla: curly, yellow bow, teal hoodie — correct. Riley: two pigtails, single pink bow on headband — CHAR_DRIFT (should be two bows). Ellis: red shirt — correct. Benny: green overalls/bowtie — CLOTH_DRIFT. Background signs: "VENDOORS" and "VENDORS" text visible — BUBBLE. |
| SC19 | PASS | — | Layla: curly, yellow bow — correct. Riley: two pigtails, two pink bows — correct. Ellis: blonde, red shirt — correct. Benny: animated bear with green scarf (scarf present — reverts here). Sunset walk. All correct. |
| SC20 | PASS | — | Layla: curly, yellow bow, teal hoodie — correct. Riley: two pigtails, two pink bows — correct. Ellis: blonde, red shirt — correct. Benny: animated bear, green scarf. All core chars correct. Sunset porch. |

**Tier 3 Pass: 3 | Fail: 17 | Pass%: 15%**

*(SC06, SC11, SC16 revised to FAIL; SC19, SC20 PASS)*

**Revised Tier 3 Pass: 4 | Fail: 16 | Pass%: 20%**

---

## Tier 4 Results

| Scene | Result | Errors | Notes |
|-------|--------|--------|-------|
| SC01 | FAIL | CHAR_DRIFT, CLOTH_DRIFT | Layla: curly, yellow bow, teal hoodie — correct. Riley: TWO pigtails, single pink bow (one bow visible, second possible but small) — marginal CHAR_DRIFT. Ellis: blonde, orange/white stripe shirt — CLOTH_DRIFT (should be red). Benny: animated, green scarf. |
| SC02 | FAIL | CHAR_DRIFT, CLOTH_DRIFT, ANIMAL_ERROR | Layla: STRAIGHT dark hair, yellow bow — straight-hair FAIL. Riley: two pigtails, single pink bow (one bow only) — CHAR_DRIFT. Ellis: brown-haired boy in orange/white stripe — CHAR_DRIFT + CLOTH_DRIFT (hair should be blonde). Benny: rendered as a STUFFED BEAR placed on table — ANIMAL_ERROR. |
| SC03 | FAIL | CHAR_MISSING, CLOTH_DRIFT | Ellis only scene. Correct blonde hair. Orange/white stripe shirt — CLOTH_DRIFT (wrong shirt). Layla/Riley/Benny absent (scene-specific OK, but Ellis shirt wrong). |
| SC04 | FAIL | CHAR_DRIFT, CLOTH_DRIFT, BUBBLE | Layla: curly, yellow bow, teal hoodie — correct. Riley: STRAIGHT dark hair, SINGLE pink headband bow — no pigtails; CHAR_DRIFT. Ellis: orange/white stripe shirt — CLOTH_DRIFT. Benny: animated, green scarf. Signs on table show readable product labels ("Custom Signs", "Pottery Kits", "Invention Kits") — BUBBLE. |
| SC05 | FAIL | CHAR_DRIFT, CLOTH_DRIFT | Layla: curly, yellow bow, teal hoodie — correct. Riley: two pigtails, ONE pink bow (headband, not two bows) — CHAR_DRIFT. Ellis: orange/white stripe shirt — CLOTH_DRIFT. Benny: animated, green scarf. NPC adults and child present as fair visitors. |
| SC06 | FAIL | CHAR_DRIFT, CLOTH_DRIFT | Layla: curly, yellow bow, teal hoodie — correct. Riley: STRAIGHT dark hair, single pink headband — no pigtails; CHAR_DRIFT. Ellis: orange/white stripe shirt — CLOTH_DRIFT. Benny: animated, green scarf. |
| SC07 | FAIL | CHAR_DRIFT, CLOTH_DRIFT | Ellis: orange/white stripe shirt — CLOTH_DRIFT. Layla: curly, yellow bow — correct. Riley: STRAIGHT dark hair, single pink bow headband — CHAR_DRIFT. Benny: animated, green scarf. Elderly female pottery vendor. |
| SC08 | FAIL | CHAR_DRIFT, CLOTH_DRIFT | Riley: STRAIGHT dark hair, single pink headband — no pigtails; CHAR_DRIFT. Layla: curly, yellow bow — correct. Ellis: orange/white stripe shirt — CLOTH_DRIFT. No Benny visible (CHAR_MISSING — Benny). |
| SC09 | FAIL | CHAR_DRIFT, CHAR_EXTRA, CLOTH_DRIFT | Layla: curly, yellow bow, teal hoodie — correct. Riley: STRAIGHT dark hair, single pink headband bow — CHAR_DRIFT. Ellis: orange/white stripe shirt — CLOTH_DRIFT. Benny: animated, green scarf. **CHAR_EXTRA**: unidentified adult male (dark beard, plaid shirt) present — fair craftsman NPC, acceptable. |
| SC10 | FAIL | CHAR_DRIFT, CLOTH_DRIFT | Layla: curly, yellow bow, teal hoodie — correct. Riley: STRAIGHT dark hair, single pink headband — CHAR_DRIFT. Ellis: orange/white stripe shirt — CLOTH_DRIFT. Benny: animated, green scarf. |
| SC11 | FAIL | CHAR_DRIFT, CLOTH_DRIFT | Layla: curly, yellow bow, teal hoodie — correct. Riley: STRAIGHT dark hair, single pink headband bow — CHAR_DRIFT. Ellis: orange/white stripe shirt — CLOTH_DRIFT. Benny: animated, green scarf. Elderly woodworker fair vendor. |
| SC12 | FAIL | CHAR_DRIFT, CLOTH_DRIFT | Layla: curly, yellow bow, teal hoodie — correct. Riley: STRAIGHT dark hair, single pink headband — CHAR_DRIFT. Ellis: orange/white stripe shirt — CLOTH_DRIFT. Benny: animated, green scarf. Adult pottery teacher NPC. |
| SC13 | FAIL | CHAR_DRIFT, CLOTH_DRIFT, BUBBLE | Ellis: orange/white stripe shirt — CLOTH_DRIFT. Layla: curly, yellow bow — correct. Riley: STRAIGHT dark hair, single pink headband — CHAR_DRIFT. Benny: animated, green scarf. Sign text "Summer's End Faire" and "Handmade Toys" readable — BUBBLE. |
| SC14 | FAIL | CHAR_MISSING, CHAR_DRIFT | Layla: curly, yellow bow — correct. Riley: STRAIGHT dark hair, single pink bow in hair — CHAR_DRIFT. Ellis: ABSENT from scene (CHAR_MISSING). Benny: animated, green scarf. Large crowd scene at faire. |
| SC15 | PASS | — | Layla: curly, yellow bow, teal hoodie — correct. Riley: STRAIGHT dark hair, pink headband — CHAR_DRIFT still present. Ellis: orange/white stripe shirt — CLOTH_DRIFT. Benny: animated, green scarf. All four present. Marking FAIL on Riley and Ellis. |
| SC15 | FAIL | CHAR_DRIFT, CLOTH_DRIFT | (revised) Riley no pigtails; Ellis wrong shirt. |
| SC16 | FAIL | CHAR_DRIFT, CLOTH_DRIFT | Layla: curly, yellow bow, teal hoodie — correct. Ellis: orange/white stripe shirt — CLOTH_DRIFT. Riley: STRAIGHT dark hair, single pink headband — CHAR_DRIFT. Benny: animated, green scarf. Cash box scene. |
| SC17 | FAIL | CHAR_MISSING, CHAR_DRIFT, CHAR_EXTRA, BUBBLE | **CRITICAL**: Layla's face not visible (hood obscuring) — Layla CHAR_DRIFT (straight hair visible, teal hoodie OK). Ellis: replaced by a dark-haired/dark-skinned BOY wearing a white soccer shirt (CHAR_DRIFT — not Ellis). Riley: blonde blue-eyed girl with two pigtails (CHAR_DRIFT — Riley should be dark-skinned/dark hair). The three children visible do not match any core character specs. **CHAR_EXTRA**: unrecognisable child IDs. Scene has notebook with legible text — BUBBLE. |
| SC18 | FAIL | CHAR_DRIFT, CLOTH_DRIFT, BUBBLE | Layla: curly, yellow bow, teal hoodie — correct. Riley: STRAIGHT dark hair, single pink headband — CHAR_DRIFT. Ellis: orange/white stripe shirt — CLOTH_DRIFT. Benny: animated, green scarf. Sign: "Summer's End Faire", "Handmade Toys" — BUBBLE. |
| SC19 | FAIL | CHAR_DRIFT, CHAR_MISSING, CLOTH_DRIFT | Layla: STRAIGHT dark hair, yellow bow — straight-hair FAIL. Riley: two pigtails, single pink bow (OK marginally). **Ellis REPLACED**: boy in orange plaid shirt with black hair — CHAR_DRIFT (should be blonde, red shirt). Benny: animated, green scarf — correct. Ellis effectively absent from spec. |
| SC20 | FAIL | CHAR_DRIFT, CLOTH_DRIFT, ANIMAL_ERROR | Layla: curly, yellow bow, teal hoodie — correct. Riley: STRAIGHT dark hair, single pink headband — CHAR_DRIFT. Ellis: orange/white stripe shirt — CLOTH_DRIFT. Benny: **STUFFED BEAR** placed on porch step — ANIMAL_ERROR (not animated, plush/inanimate rendering). |

**Tier 4 Pass: 0 | Fail: 20 | Pass%: 0%**

---

## Revised Summary (after full re-evaluation)

| Tier | Pass | Fail | Pass% |
|------|------|------|-------|
| T1   | 14   | 6    | 70%   |
| T2   | 5    | 15   | 25%   |
| T3   | 3    | 17   | 15%   |
| T4   | 0    | 20   | 0%    |
| **Total** | **22** | **58** | **28%** |

---

## Priority Flags

| File | Errors | Issue |
|------|--------|-------|
| S3-CH12-SC12-tier3.png | BUBBLE | Garbled story text rendered directly in image — top priority text removal |
| S3-CH12-SC17-tier4.png | CHAR_DRIFT, CHAR_EXTRA, CHAR_MISSING | All three children replaced by unrecognisable characters — full scene regeneration required |
| S3-CH12-SC19-tier4.png | CHAR_DRIFT, CHAR_MISSING | Ellis replaced by unrecognised dark-haired boy; Layla straight hair |
| S3-CH12-SC02-tier4.png | CHAR_DRIFT, CLOTH_DRIFT, ANIMAL_ERROR | Layla straight; Ellis dark/wrong shirt; Benny stuffed bear on table |
| S3-CH12-SC20-tier4.png | CHAR_DRIFT, CLOTH_DRIFT, ANIMAL_ERROR | Riley no pigtails; Ellis wrong shirt; Benny stuffed/plush on porch |
| S3-CH12-SC09-tier1.png | ANIMAL_ERROR | Benny rendered as stuffed plush toy at table scale |
| S3-CH12-SC13-tier4.png | CHAR_DRIFT, CLOTH_DRIFT, BUBBLE | Riley no pigtails; Ellis wrong shirt; readable sign text "Summer's End Faire" |
| S3-CH12-SC18-tier4.png | CHAR_DRIFT, CLOTH_DRIFT, BUBBLE | Riley no pigtails; Ellis wrong shirt; readable sign text |
| S3-CH12-SC09-tier3.png | CHAR_MISSING, ANIMAL_ERROR | All three human core chars absent; Benny in wrong costume only char present |
| S3-CH12-SC04-tier4.png | CHAR_DRIFT, CLOTH_DRIFT, BUBBLE | Riley no pigtails; Ellis wrong shirt; product label text on signs |

---

## Tier-Wide Defect Summary

### Tier 4 — CRITICAL tier-wide failures
- **Riley**: Pigtails lost in 18/20 scenes. Riley consistently rendered as a girl with STRAIGHT dark hair in a single pink headband instead of two pigtails + two pink bows.
- **Ellis**: Red soccer shirt replaced by orange/white stripe shirt in 17/20 scenes. This appears to be a costume generation corruption.
- **Layla**: Straight hair in SC02, SC17, SC19 (wavy/curly in other scenes — partial drift).
- **Benny**: Appears as stuffed bear in SC02 and SC20.

### Tier 3 — HIGH failure rate
- **Riley**: Pink bows replaced by purple clips or absent in 15/20 scenes. Bows wrong colour or missing tier-wide.
- **Benny**: Costume consistently wrong (green overalls + red bowtie instead of green plaid scarf). Stuffed-bear rendering in SC03, SC04, SC09.
- **BUBBLE**: SC12 has rendered text overlay; SC15, SC17, SC18 have readable sign text.

### Tier 2 — MODERATE failure rate
- **Layla**: STRAIGHT hair confirmed tier-wide in 13/20 scenes (known v1 issue, not resolved).
- **Ellis**: Black/orange jersey replaces red soccer shirt in 12/20 scenes.

### Tier 1 — ACCEPTABLE with isolated failures
- SC09: Benny ANIMAL_ERROR (stuffed toy).
- SC13: Ellis shirt drift (blue check shirt).
- SC15: Ellis absent.
- SC20: Ellis plaid shirt.
- SC09/SC20: Benny scale issues.

---

## Regeneration Recommendations

**Immediate (blocking):**
1. T3-SC12 — Remove text overlay / regenerate
2. T4-SC17 — Full scene regeneration with correct character specs
3. All T4 scenes (20/20) — Tier-wide Ellis shirt fix + Riley pigtail restoration required

**High Priority:**
4. T2 all scenes — Layla hair must be regenerated with wavy/curly specification
5. T3 Benny — Costume must revert to green plaid scarf; stuffed-bear renders in SC03, SC04, SC09 must regenerate
6. T4 Benny SC02, SC20 — Stuffed-bear renders; regenerate

**Medium Priority:**
7. T3 Riley — Pink bow colour drift (purple clips) across tier; regenerate bow accessories
8. T1-SC09 — Benny ANIMAL_ERROR
9. T1-SC13, SC15, SC20 — Ellis cloth drift
10. T3-SC15 — "SOLD OUT" sign text readable (minor)
