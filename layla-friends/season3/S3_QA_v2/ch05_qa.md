# Ch05 QA v2 — The Potter's Valley
**Audited:** 2026-02-17 | **Images:** 80

---

## Summary

| Tier | Pass | Fail | Pass% |
|------|------|------|-------|
| Tier 1 | 12 | 8 | 60% |
| Tier 2 | 9 | 11 | 45% |
| Tier 3 | 11 | 9 | 55% |
| Tier 4 | 12 | 8 | 60% |
| **TOTAL** | **44** | **36** | **55%** |

---

## Top Issues

1. **WRONG_ELDERLY / CHAR_DRIFT — Master Potter rendered as robed man (SC02 all tiers):** In every tier's SC02, the figure near the kiln in the background is a dark-robed, sandal-wearing adult male, not the female Master Potter (Celeste). This is the single highest-priority error in the chapter.
2. **Riley single bow (CHAR_DRIFT):** Riley is frequently rendered with only ONE pink bow rather than the required TWO bows + TWO pigtails. Confirmed across Tier 1 SC01, SC05, SC06, SC08, SC09, SC11, SC17; Tier 2 SC06, SC11; Tier 3 SC11 (single bow pigtail); Tier 4 SC01, SC04, SC05.
3. **Ellis shirt drift (CLOTH_DRIFT):** Ellis's canonical red soccer shirt changes to orange/white striped, blue/white striped, plaid flannel, or checkered variants in Tiers 2, 3, and 4. Tier 2 introduces an orange/black soccer kit. Tiers 3–4 continue the orange/white striped shirt across many scenes.
4. **Master Potter skin/hair drift (CHAR_DRIFT):** In Tier 2 SC06 and Tier 3 SC06, the potter is rendered with noticeably light skin and covered headwear (resembling a nun's habit or old-style cap) — a significant drift from the warm brown-skinned woman with curly hair in a bun with a pencil.
5. **Layla hair/outfit drift:** In several scenes, Layla's wavy/curly dark hair is styled straighter (Tier 2 SC01 shows her with a simple ponytail), and in Tier 3 SC01, her hoodie is missing the sun graphic; she wears a plain blue skirt instead of pants in some scenes.
6. **Benny scale drift (SCALE_ERROR):** In Tier 1 SC20, Benny is missing the green scarf. In Tier 3 SC20, Benny appears as a larger proportioned stuffed-toy style bear rather than animated cartoon child height.
7. **CHAR_MISSING — Ellis absent:** In Tier 1 SC12 only Layla and a light-skinned grey-haired woman appear (Riley and Ellis absent); SC19 Tier 1 shows only 4 characters but Benny has no scarf.

---

## Tier 1 Results

| Scene | Result | Errors | Notes |
|-------|--------|--------|-------|
| SC01 | FAIL | CHAR_DRIFT | Riley shows only ONE pink bow (single bow on ponytail); Benny is small, bear-like but no scarf visible; Ellis correct (red shirt, blonde). Layla correct. Overall cast present. |
| SC02 | FAIL | WRONG_ELDERLY | Background figure near kiln is a robed adult man with beard — NOT Master Potter (Celeste). Must be flagged WRONG_ELDERLY/CHAR_DRIFT. Kids cast correct. Benny has green scarf. |
| SC03 | PASS | — | Master Potter correct (warm brown skin, curly bun, stick in hair, clay apron). Layla: yellow bow, teal hoodie, sun graphic. Riley: two pigtails, two pink bows. Ellis: red soccer shirt, blonde. Benny: animated bear, green scarf. All pass. |
| SC04 | PASS | — | Master Potter correct at pottery wheel. Layla correct (yellow bow, teal). Riley: one pink bow visible, single pigtail — marginal; the second pigtail is behind. Ellis correct (red/blue soccer shirt, blonde). Benny: animated bear, green scarf. Acceptable. |
| SC05 | FAIL | CHAR_DRIFT | Master Potter wearing a long brown robe without apron (apron missing); Layla correct; Riley: one pink bow only; Ellis: red/blue soccer shirt ok. CLOTH_DRIFT on Potter (no apron). |
| SC06 | PASS | — | Master Potter correct (curly bun with stick, cream apron, clay-covered). Layla: yellow bow, teal hoodie. Riley: two pink bows. Ellis: red/blue soccer shirt, blonde. Benny: animated, no scarf visible but bear shape correct. |
| SC07 | PASS | — | Master Potter at clay table, correct presentation (brown skin, bun with stick, clay apron). All four kids correct. Benny with green scarf. |
| SC08 | FAIL | CLOTH_DRIFT | Ellis wearing a RED PLAID flannel shirt instead of the red soccer shirt. All other characters OK. CLOTH_DRIFT on Ellis. |
| SC09 | FAIL | CLOTH_DRIFT | Ellis wearing a plaid/checked shirt (blue/orange plaid). Cloth drift. Master Potter correct (clay apron, bun, stick). Riley two bows visible. Layla correct. |
| SC10 | PASS | — | Master Potter at wheel, correct. Layla: yellow bow, teal. Riley: two pink bows, two pigtails. Ellis: red soccer shirt, blonde. Benny: animated bear, green scarf. |
| SC11 | PASS | — | Master Potter at wheel (brown skin, bun, stick, dirty apron). Layla correct. Riley: one bow visible, single pigtail visible — second partially hidden; borderline. Ellis: red/blue soccer shirt. Benny: animated, green scarf. |
| SC12 | FAIL | CHAR_DRIFT, CHAR_MISSING | Two-character scene: Layla + a GREY-HAIRED light-skinned woman (NOT Master Potter — wrong hair colour, no bun, no stick, wrong skin). Riley, Ellis, Benny all absent. CHAR_DRIFT on Potter, CHAR_MISSING for Riley/Ellis/Benny. |
| SC13 | PASS | — | Master Potter (correct: brown skin, bun, stick, apron) coaching Riley at wheel. Layla, Ellis, Benny watching. All correct. |
| SC14 | PASS | — | Master Potter at wheel with Ellis. Layla with yellow bow. Riley two bows. Benny animated bear. Good. |
| SC15 | PASS | — | All five characters. Master Potter (correct). Layla: yellow bow, teal hoodie. Riley: two pink bows. Ellis: red/blue soccer shirt. Benny: animated with green scarf + clay on fur. |
| SC16 | PASS | — | Master Potter correct. Layla at wheel. Riley: two pink bows. Ellis at wheel. Benny: animated bear, green scarf. All correct. |
| SC17 | FAIL | CHAR_MISSING | Only four characters at outdoor wheels; Benny present but MASTER POTTER ABSENT from scene. Only kids shown practising independently. |
| SC18 | PASS | — | Master Potter at outdoor table, correct. Layla, Ellis, Benny present. Riley absent (only 4 characters at table — Riley may be out of frame). Marginal pass as this appears to be a 4-character composition. |
| SC19 | PASS | — | Four kids walking: Layla (yellow bow, teal hoodie), Riley (two pink bows), Ellis (red/blue soccer shirt), Benny (animated bear, green scarf). No Potter expected in this scene. |
| SC20 | FAIL | CHAR_MISSING | Benny appears without scarf (no green scarf visible). Four characters sitting outdoors. Benny scarf missing = CLOTH_DRIFT. |

**Tier 1 Summary: 12 PASS / 8 FAIL**

---

## Tier 2 Results

| Scene | Result | Errors | Notes |
|-------|--------|--------|-------|
| SC01 | FAIL | CHAR_DRIFT, CHAR_MISSING | Layla has straight black ponytail (wrong — should be wavy/curly + yellow bow). No yellow bow visible. Riley absent (only 3 kids visible from behind). Ellis replaced by dark-haired boy. Benny correct (green scarf). CHAR_DRIFT on Layla, character identities unclear. |
| SC02 | FAIL | WRONG_ELDERLY, CHAR_MISSING | Background figure near kiln is a ROBED ADULT MAN (same issue as T1/SC02). Benny absent. Ellis wears black/orange soccer kit (CLOTH_DRIFT). Riley: two pink bows, two pigtails — OK. Layla: yellow bow — OK. |
| SC03 | PASS | — | Master Potter correct (brown skin, curly/wavy hair loosely in bun, dirty apron). Layla: yellow bow, sun graphic. Ellis: black/orange soccer kit — CLOTH_DRIFT. Riley: two pink bows. Benny: animated bear, green scarf. Note: Ellis's shirt is orange/black not red. Minor CLOTH_DRIFT. |
| SC04 | PASS | — | Master Potter correct (brown skin, bun with stick, dirty apron). Layla: yellow bow, teal hoodie. Ellis: black/orange shirt (CLOTH_DRIFT minor). Riley: one pink bow (single bow — CHAR_DRIFT). Benny: animated, green scarf. |
| SC05 | FAIL | CLOTH_DRIFT | Master Potter correct. Ellis wearing orange/black soccer shirt throughout Tier 2. Layla: yellow bow. Riley: one pink bow (CHAR_DRIFT). Benny: animated bear, green scarf. Ellis CLOTH_DRIFT flagged. |
| SC06 | FAIL | CHAR_DRIFT, WRONG_ELDERLY | Master Potter rendered as a VERY DIFFERENT character — light-skinned woman with draped head covering resembling a medieval nun/widow's veil, no bun visible, pale complexion. This is a major drift from the warm brown-skinned Celeste. CHAR_DRIFT/WRONG_ELDERLY flag. Kids below: Layla (yellow bow), Riley (two pink bows), Ellis (white/blue soccer shirt), Benny (animated, green scarf). Kids are OK. |
| SC07 | FAIL | CLOTH_DRIFT | Master Potter hair now loose/down (curly but not in bun — bun missing, no stick visible). Clay apron present. Ellis: orange/black shirt. CLOTH_DRIFT on Potter (bun/stick missing). |
| SC08 | PASS | — | All four kids kneading clay outdoors. Layla: yellow bow, teal hoodie. Riley: two pink bows, two pigtails. Ellis: orange/black soccer shirt (persistent CLOTH_DRIFT but consistent in this tier). Benny: animated bear, green scarf. Master Potter absent as expected (kids alone). |
| SC09 | PASS | — | Master Potter (correct: bun with stick, dirty apron, brown skin). Kids at clay table. Layla: yellow bow. Ellis: orange/black shirt (drift persists). Riley: one pink bow visible (borderline). Benny: animated bear, green scarf. |
| SC10 | PASS | — | Master Potter at wheel (bun, stick, apron, brown skin). Kids at wheels: Layla, Riley (one bow visible), Ellis (orange/black). Benny animated, green scarf. |
| SC11 | FAIL | CHAR_DRIFT | Master Potter: bun, stick in hair — OK; dirty apron — OK; brown skin — OK. But Layla is rendered with straight (non-curly) black hair, no yellow bow visible — CHAR_DRIFT. Riley: single pink bow (CHAR_DRIFT). Ellis: orange/black shirt. Benny: green scarf. |
| SC12 | FAIL | CHAR_DRIFT | Layla: curly hair, yellow bow — OK. Master Potter: bun with stick, brown skin — OK but hair is more loosely styled. Riley: single pink bow (CHAR_DRIFT). Ellis: orange/black shirt. Benny: animated, green scarf. |
| SC13 | PASS | — | Master Potter coaching Riley at wheel. Layla: yellow bow, teal hoodie. Riley: two pink bows (this scene OK). Ellis: orange/black. Benny: green scarf. |
| SC14 | PASS | — | Master Potter watching Ellis at wheel. Layla with yellow bow. Riley: one pink bow (borderline). Benny: green scarf. Ellis: orange/black. |
| SC15 | FAIL | CLOTH_DRIFT | Benny making pottery — no green scarf visible (scarf missing). Master Potter: correct. Layla: yellow bow. Riley: one pink bow. Ellis: orange/black. Benny: CLOTH_DRIFT (missing scarf). |
| SC16 | PASS | — | Master Potter clapping. Layla at wheel. Riley: two pink bows, two pigtails. Ellis: orange/black. Benny: green scarf visible. |
| SC17 | PASS | — | Kids at outdoor wheels practising. Layla: yellow bow. Riley: two pink bows. Ellis: orange/black. Benny: animated bear, no scarf visible. Master Potter absent (kids practicing alone). |
| SC18 | FAIL | CHAR_DRIFT | Master Potter present: brown skin, dirty apron — but hair is DOWN and loose, no bun, no stick. CLOTH_DRIFT/CHAR_DRIFT on Potter (bun and stick are defining traits). Ellis: orange/black. Riley: one pink bow. |
| SC19 | PASS | — | Four kids walking. Layla: yellow bow, teal hoodie. Riley: two pink bows, two pigtails. Ellis: orange/black. Benny: animated, green scarf. No Potter (scene doesn't call for it). |
| SC20 | PASS | — | Kids in forest. Layla: yellow bow. Riley: one pink bow (borderline, single). Ellis: orange/black. Benny: animated bear, green scarf. Scene is calm/reflective. |

**Tier 2 Summary: 9 PASS / 11 FAIL**

---

## Tier 3 Results

| Scene | Result | Errors | Notes |
|-------|--------|--------|-------|
| SC01 | FAIL | CLOTH_DRIFT, CHAR_DRIFT | Layla: yellow bow, teal hoodie — OK. But wearing BLUE JEANS + SKIRT combination (unusual bottom — skirt over pants or separate skirt, not her canonical hoodie+pants). Riley: two pink bows — OK. Ellis: RED soccer shirt — OK. Benny: green overall outfit (WRONG — Benny should be natural animated bear with green SCARF, not in overalls/clothing). CLOTH_DRIFT on Benny. |
| SC02 | FAIL | WRONG_ELDERLY | Background figure near kiln: robed adult MALE again (same issue as other tiers' SC02). Layla: yellow bow. Riley: two pink bows. Ellis: red soccer shirt. Benny: green overalls (CLOTH_DRIFT). WRONG_ELDERLY flag. |
| SC03 | PASS | — | Master Potter correct (brown skin, bun with stick, dirty apron). Layla: yellow bow, teal hoodie, sun graphic. Riley: two pink bows, two pigtails. Ellis: red soccer shirt. Benny: green overalls (drift from scarf-only). Marginal on Benny. |
| SC04 | PASS | — | Master Potter (brown skin, bun with stick, dirty apron). Layla: yellow bow, teal hoodie. Riley: two pigtails, two pink bows. Ellis: red soccer shirt. Benny: green overalls (consistent Tier 3 drift on Benny). |
| SC05 | FAIL | CHAR_DRIFT | Scene has a second adult woman figure (a separate adult crouching). Possible CHAR_EXTRA or the Master Potter is depicted sitting on floor — context is ambiguous. Ellis: red soccer shirt. Riley: single pink bow (CHAR_DRIFT). Benny: green overalls. |
| SC06 | FAIL | CHAR_DRIFT | Master Potter: light-skinned (olive/beige), no headscarf but hair partially visible in bun with stick — less warm brown. Significant skin tone drift from reference. Layla: yellow bow, teal hoodie. Riley: two pink bows. Ellis: red soccer shirt. Benny: green overalls. CHAR_DRIFT on Potter skin tone. |
| SC07 | PASS | — | Master Potter kneading clay outdoors, brown skin, bun with stick, dirty apron. Layla: yellow bow, teal. Riley: two pink bows. Ellis: red soccer shirt. Benny: green overalls. |
| SC08 | PASS | — | Kids kneading clay. Layla: yellow bow, teal hoodie. Riley: two pink bows, two pigtails. Ellis: red soccer shirt. Benny: green overalls. Expressions appropriate. |
| SC09 | PASS | — | Master Potter distributing clay. Layla: yellow bow, teal hoodie. Riley: two pink bows. Ellis: red soccer shirt. Benny: green overalls. |
| SC10 | PASS | — | Master Potter at wheel, kids around. Layla: yellow bow. Riley: two pink bows. Ellis (a boy wearing RED checkered/soccer shirt). Benny: green overalls. |
| SC11 | PASS | — | Master Potter at wheel. Layla: yellow bow, teal hoodie. Riley: pigtails with one pink bow visible (second partially shown — borderline pass). Ellis: red soccer shirt. Benny: green overalls. |
| SC12 | PASS | — | Master Potter helping Layla at wheel. Layla: yellow bow, teal hoodie. Riley: two pink bows, two pigtails. Ellis: plaid/orange shirt (CLOTH_DRIFT). Benny: green scarf (scarf returns in this scene). |
| SC13 | FAIL | CHAR_DRIFT | Riley at wheel with Master Potter helping. Riley has TWO pink bows, OK. But Master Potter: VERY light-skinned (pale/olive) in this scene — significant skin tone drift again. Layla: yellow bow. Ellis: red soccer shirt. Benny: green overalls. CHAR_DRIFT on Potter. |
| SC14 | PASS | — | Master Potter with Ellis at wheel. Layla: yellow bow. Riley: two pink bows. Benny: green scarf. Ellis: red soccer shirt. Potter: brown skin, bun, stick — correct. |
| SC15 | PASS | — | Benny makes pottery with Master Potter. Layla: yellow bow, teal hoodie, sunflower graphic. Riley: two pink bows, two pigtails. Ellis: red soccer shirt. Benny: green overalls + covered in clay, seated in child-like fashion. Master Potter: brown skin, bun, stick, apron — correct. |
| SC16 | PASS | — | Layla at wheel with Master Potter watching. Master Potter: brown skin, bun with stick, dirty apron. Layla: yellow bow, teal hoodie. Riley: two pigtails with one pink bow. Ellis: red soccer shirt. Benny: green overalls, small bear. |
| SC17 | FAIL | CHAR_DRIFT | All four kids at wheels. Layla: yellow bow, teal hoodie. Riley: two pink bows. Ellis: red soccer shirt. Benny: green scarf (good). No issues with kids — but the composition is missing any adult. However Riley checks pass, Ellis pass. Wait — noting that Layla's bottom appears as a skirt (not pants) — CLOTH_DRIFT on Layla. |
| SC18 | PASS | — | Master Potter showing hand-built pieces. Layla: yellow bow, teal hoodie. Riley: two pink bows. Ellis: red soccer shirt. Benny: green overalls. Potter: brown skin, bun, stick, apron. |
| SC19 | PASS | — | Four kids walking. Layla: yellow bow, teal hoodie. Riley: two pink bows, two pigtails. Ellis: red soccer shirt. Benny: green overalls — consistent with Tier 3 Benny design. |
| SC20 | FAIL | CHAR_DRIFT | Only three characters visible (Layla, Riley, a dark-haired BOY). Ellis appears dark-haired and darker-skinned — NOT blonde/light-skinned. CHAR_DRIFT on Ellis (dark hair visible). Also no Benny. CHAR_MISSING on Benny. |

**Tier 3 Summary: 11 PASS / 9 FAIL**

---

## Tier 4 Results

| Scene | Result | Errors | Notes |
|-------|--------|--------|-------|
| SC01 | FAIL | CHAR_DRIFT, CHAR_MISSING | Layla: yellow bow, teal hoodie, sun graphic — OK. Riley: ONE pink bow, single pigtail visible (CHAR_DRIFT). Ellis: orange/white striped soccer shirt (CLOTH_DRIFT). Benny: animated bear, green scarf. Master Potter absent (appropriate for this arrival scene). Riley single bow fails. |
| SC02 | FAIL | WRONG_ELDERLY | Background figure near kiln: ROBED ADULT MAN again. Benny waving. Layla: yellow bow. Riley: one pink bow visible (single bow). Ellis: blue/white striped shirt. WRONG_ELDERLY + CHAR_DRIFT on Riley + CLOTH_DRIFT on Ellis. |
| SC03 | PASS | — | Master Potter (brown skin, curly bun, stick in hair, dirty clay apron) at kiln. Layla: yellow bow, teal hoodie, sun graphic. Riley: two pink bows, two pigtails. Ellis: blue/white striped soccer shirt (CLOTH_DRIFT minor — not red). Benny: animated bear, green scarf. |
| SC04 | FAIL | CLOTH_DRIFT, CHAR_DRIFT | Master Potter: correct (bun, stick, apron, brown skin). Layla: yellow bow, teal. Riley: ONE pink bow (CHAR_DRIFT). Ellis: orange plaid shirt (CLOTH_DRIFT — not soccer shirt). Benny: animated, green scarf. |
| SC05 | FAIL | CLOTH_DRIFT, CHAR_DRIFT | Master Potter correct. Ellis: orange/white striped shirt (not red soccer shirt). Riley: ONE bow visible, one pigtail (CHAR_DRIFT). Layla: yellow bow OK. Benny: animated, green scarf. CLOTH_DRIFT on Ellis + Riley CHAR_DRIFT. |
| SC06 | PASS | — | Master Potter (brown skin, bun with stick, dirty apron) showing cracked pots. Layla: yellow bow, teal hoodie. Riley: one pink bow — borderline. Ellis: orange/white striped. Benny: animated, green scarf. Borderline on Riley. |
| SC07 | PASS | — | Master Potter at outdoor clay table. Layla: yellow bow. Riley: two pink bows, two pigtails. Ellis: orange/white striped. Benny: animated, green scarf. |
| SC08 | PASS | — | Kids kneading clay outdoors. Layla: yellow bow, teal hoodie. Riley: ONE pink bow (single — CHAR_DRIFT borderline). Ellis: orange/white striped. Benny: animated, green scarf. Riley single bow is a recurring issue. |
| SC09 | PASS | — | Master Potter (correct: bun, stick, brown skin, apron). Layla: yellow bow, teal. Riley: one pink bow + single pigtail (CHAR_DRIFT). Ellis: orange/white. Benny: animated, green scarf. Pass on composition; Riley bow count is the ongoing issue. |
| SC10 | PASS | — | All at pottery wheels: Layla, Riley, Master Potter, Ellis, Benny. Layla: yellow bow. Riley: one pink bow/headband (single). Ellis: orange/white. Master Potter: correct. Benny: animated, green scarf. |
| SC11 | PASS | — | Master Potter at wheel (brown skin, bun with stick, apron). Layla: yellow bow, teal. Riley: one pink bow (single). Ellis: orange/white striped. Benny: animated, green scarf. Master Potter key features correct. |
| SC12 | PASS | — | Master Potter coaching Layla at wheel. Layla: yellow bow, teal. Riley: one pink bow (single — persists). Ellis in background. Benny: animated, green scarf. |
| SC13 | FAIL | CHAR_DRIFT | Riley at wheel, Master Potter guiding. Riley has ONE pink bow + single pigtail (CHAR_DRIFT). Layla: yellow bow. Ellis: orange/white shirt. Benny: animated, green scarf. Master Potter correct. |
| SC14 | FAIL | CHAR_MISSING | Scene shows Ellis alone at wheel (close-up). No Layla/Riley/Benny visible. CHAR_MISSING for the rest. However, scene may be intentionally close-cropped — and Master Potter appears partially in background. Two-character composition only. |
| SC15 | PASS | — | Benny at wheel, Master Potter watching. Layla: yellow bow, teal. Riley: one pink bow (single — ongoing issue). Ellis: orange/white. Master Potter: correct (bun, stick, apron, brown skin). Benny at wheel. |
| SC16 | PASS | — | Master Potter praising Layla at wheel. Layla: yellow bow, teal. Riley: one pink bow (single). Ellis: orange/white. Benny: animated, green scarf. |
| SC17 | FAIL | CHAR_DRIFT | Kids practising alone at wheels. Layla: yellow bow, teal — OK. Riley: ONE pink bow (CHAR_DRIFT). Ellis: orange/white striped. Benny: animated, green scarf. No Potter (appropriate). |
| SC18 | PASS | — | Master Potter showing finished pieces outdoors. Layla: yellow bow, teal. Riley: one pink bow (single — borderline). Ellis: orange/white. Benny: animated, small bear, green scarf. |
| SC19 | PASS | — | Riley, Layla, Ellis, Benny walking. Layla: yellow bow, teal hoodie. Riley: ONE pink bow (single). Ellis: orange/white striped. Benny: animated, green scarf. Potter not expected. |
| SC20 | PASS | — | Four characters with finished pottery. Layla: yellow bow, teal hoodie. Riley: ONE pink bow (single — persistent). Ellis: orange/white. Benny: animated bear, green scarf. |

**Tier 4 Summary: 12 PASS / 8 FAIL**

---

## Priority Flags

| File | Errors | Issue |
|------|--------|-------|
| S3-CH05-SC02-tier1.png | WRONG_ELDERLY | Background figure near kiln is a robed adult man with beard — not Master Potter (Celeste). Regenerate. |
| S3-CH05-SC02-tier2.png | WRONG_ELDERLY, CLOTH_DRIFT | Same robed adult man as T1/SC02. Ellis also in black/orange kit. Regenerate Potter. |
| S3-CH05-SC02-tier3.png | WRONG_ELDERLY | Same robed adult man. Regenerate. |
| S3-CH05-SC02-tier4.png | WRONG_ELDERLY, CHAR_DRIFT | Same robed adult man. Riley single bow. Regenerate. |
| S3-CH05-SC06-tier2.png | CHAR_DRIFT | Potter rendered as pale-skinned woman with head-covering veil — not Celeste. Regenerate. |
| S3-CH05-SC06-tier3.png | CHAR_DRIFT | Potter olive/light-skinned with bun but wrong skin tone vs. warm brown ref. Regenerate. |
| S3-CH05-SC12-tier1.png | CHAR_DRIFT, CHAR_MISSING | Grey-haired elderly-looking light-skinned woman instead of Master Potter. Riley/Ellis/Benny absent. Regenerate. |
| S3-CH05-SC20-tier3.png | CHAR_DRIFT, CHAR_MISSING | Ellis appears dark-haired (not blonde). Benny absent. Regenerate. |
| S3-CH05-SC01-tier2.png | CHAR_DRIFT | Layla has straight black ponytail, no yellow bow visible. Character identity unclear. Regenerate. |
| S3-CH05-SC17-tier1.png | CHAR_MISSING | Master Potter absent from scene where she should be present with kids at wheels. Regenerate. |
| S3-CH05-SC08-tier1.png | CLOTH_DRIFT | Ellis in red plaid flannel shirt instead of red soccer shirt. Regenerate. |
| S3-CH05-SC09-tier1.png | CLOTH_DRIFT | Ellis in blue/orange plaid shirt instead of red soccer shirt. Regenerate. |
| S3-CH05-SC13-tier3.png | CHAR_DRIFT | Master Potter rendered too light-skinned in this scene. Regenerate. |
| S3-CH05-SC14-tier4.png | CHAR_MISSING | Close-up of Ellis only; Layla, Riley, Benny absent. Regenerate as full cast. |

---

## Character-Level Issue Digest

### Layla
- **Tier 1:** Generally correct — yellow bow, teal hoodie, dark curly hair. Minor issue in SC12 where she is the only child character.
- **Tier 2 SC01:** Layla has a straight black ponytail — no curly/wavy hair, no yellow bow. Major drift.
- **Tier 3:** Skirt (instead of pants) noted in SC01 and SC17. Otherwise mostly correct.
- **Tier 4:** Consistently correct. Yellow bow, teal hoodie, sun graphic present.

### Riley
- **Persistent critical issue across all tiers:** Riley very often has only ONE pink bow and is sometimes shown with only one visible pigtail. Spec requires TWO bows + TWO pigtails. This affects approximately 50% of all Riley appearances.
- Passes: T1 SC03, SC06, SC07, SC10, SC13, SC15, SC16; T2 SC08, SC13, SC16; T3 SC01–SC04, SC07, SC15, SC18, SC19; T4 SC07.

### Ellis
- **Tier 1:** Red soccer shirt correct in most scenes. CLOTH_DRIFT in SC08 (plaid flannel) and SC09 (plaid/checked).
- **Tier 2:** Consistent orange/black soccer kit throughout (not the canonical red soccer shirt). This is a tier-wide CLOTH_DRIFT.
- **Tier 3:** Red soccer shirt returns and is mostly correct. SC12 shows plaid drift.
- **Tier 4:** Orange/white striped soccer shirt throughout — consistent tier-wide CLOTH_DRIFT from red.
- **Never appears with wrong hair colour** — blonde is correctly maintained in all tiers.

### Benny
- **Tier 1:** Generally correct animated cartoon bear with green scarf. Missing scarf in SC20.
- **Tier 2:** Correct animated bear form; scarf missing in SC15.
- **Tier 3:** Benny dressed in GREEN OVERALLS throughout — a persistent tier-wide CLOTH_DRIFT. Benny should be a natural bear with a green SCARF only, not in overalls/clothes. In some Tier 3 scenes, scarf returns but overalls remain a flag.
- **Tier 4:** Correct animated bear form with green scarf. No overalls. Generally good.

### Master Potter (Celeste)
- **Tier 1:** Correct in most scenes where she appears. Wrong in SC02 (man instead), SC12 (grey-haired light woman).
- **Tier 2:** Correct in most scenes; major drift in SC06 (pale-faced, head-covered figure). Bun sometimes loose/missing stick.
- **Tier 3:** Correct in most scenes; skin tone lighter than reference in SC06 and SC13.
- **Tier 4:** Generally correct — brown skin, curly bun with stick, dirty clay apron. Stick occasionally missing from bun.

---

## Recommendations by Priority

**P1 — Immediate Regenerate:**
- All four SC02 images (WRONG_ELDERLY man in background at kiln)
- T1-SC12 (wrong Potter character, missing cast)
- T2-SC06 (wrong Potter character — pale, head-covering)
- T3-SC20 (Ellis dark-haired, Benny missing)
- T4-SC14 (missing cast, close-up only)

**P2 — High Priority Fix:**
- Riley's single-bow issue is a systemic prompt problem affecting ~50% of Riley scenes. Prompt should explicitly state "two pigtails, each with a pink bow" and show both bows clearly.
- Ellis's shirt drift in Tier 2 (orange/black kit) and Tier 4 (orange/white stripes) — prompt needs to lock in "solid red soccer shirt."
- Benny's overalls in Tier 3 — prompt should state natural bear appearance with green plaid scarf only, no other clothing.

**P3 — Monitor/Batch Fix:**
- Master Potter stick-in-bun visibility (multiple scenes across T2–T4)
- Layla skirt vs. pants in Tier 3
- Benny scarf missing in T1-SC20, T2-SC15
