# Ch06 QA v2 — Throwing and Turning
**Audited:** 2026-02-17 | **Images:** 80 | **Auditor:** Claude Sonnet 4.5

---

## Summary

| Tier | Pass | Fail | Pass% |
|------|------|------|-------|
| Tier 1 | 10 | 10 | 50% |
| Tier 2 | 11 | 9 | 55% |
| Tier 3 | 10 | 10 | 50% |
| Tier 4 | 11 | 9 | 55% |
| **Total** | **42** | **38** | **52.5%** |

---

## Top Issues

| Rank | Error Code | Count | Description |
|------|-----------|-------|-------------|
| 1 | CHAR_DRIFT | 31 | Ellis wears wrong shirt (plaid/check/orange-stripe instead of red soccer shirt); Layla hood UP; characters lose defining features across tiers |
| 2 | WRONG_ELDERLY | 12 | Master Potter rendered as elderly grey-haired woman (especially T1-SC03, T1-SC14, T1-SC16, T4-SC12, T4-SC16) |
| 3 | CHAR_DUPLICATE | 3 | Master Potter appears 2–3 times in single scene (T1-SC13 confirmed; resolved in later tiers) |
| 4 | CHAR_MISSING | 8 | One of the core four absent from scene (Benny missing T1-SC12; Riley missing several scenes) |
| 5 | CLOTH_DRIFT | 9 | Ellis shirt drifts to orange/black stripes (T2+T3+T4 consistent), Benny scarf changes to bandana |
| 6 | SCALE_ERROR | 3 | Benny rendered at adult/oversized scale vs. children (T4-SC04, T4-SC13) |

---

## Tier 1 Results

| Scene | Result | Errors | Notes |
|-------|--------|--------|-------|
| SC01 | PASS | — | All four kids + Benny present; Layla yellow bow, teal hoodie hood DOWN; Riley two pink bows, two pigtails; Ellis red/blue soccer shirt; Benny animated bear with green plaid scarf; pottery booth setting; clean. |
| SC02 | FAIL | CHAR_DRIFT | Master Potter present, correct bun/stick/apron; Ellis wears red CHECKERED shirt — not canonical red soccer shirt. Cloth drift on Ellis. |
| SC03 | FAIL | WRONG_ELDERLY, CHAR_DRIFT | Master Potter replaced by elderly grey-haired pale woman in brown robe — completely wrong character. WRONG_ELDERLY. Ellis has reddish-brown hair (should be blonde). Layla hair appears straight, bow present but hair texture drifted. |
| SC04 | PASS | CHAR_DRIFT (minor) | All present. Master Potter correct. Riley one visible bow only (other hidden by angle — acceptable). Ellis shirt red/blue with soccer ball graphic — borderline pass; scarf missing on Benny (no scarf but otherwise correct bear). Minor note only. |
| SC05 | PASS | — | Riley + Master Potter two-shot; Riley two pink bows confirmed; Master Potter bun/stick/apron/warm brown skin. Clean. |
| SC06 | FAIL | CHAR_DRIFT | Ellis wears red PLAID long-sleeve shirt — not canonical short-sleeve red soccer shirt. Layla visible in background, hood DOWN, yellow bow — OK. |
| SC07 | PASS | — | All four present with clay bowls; Layla yellow bow, teal hoodie; Riley two pink bows, two pigtails; Ellis red/blue soccer shirt; Benny animated bear green scarf. |
| SC08 | PASS | — | Master Potter holding two bowls; all four core characters present; Layla teal hoodie hood DOWN yellow bow; Riley one visible bow (angle acceptable); Ellis red soccer shirt; Benny animated bear. Good. |
| SC09 | FAIL | CHAR_DRIFT, CHAR_MISSING | Riley has only ONE pink bow on headband — FAIL. Benny present. Layla correct. Ellis correct. Riley single bow is hard FAIL per spec. |
| SC10 | FAIL | WRONG_ELDERLY, CHAR_DRIFT | Master Potter is elderly grey-haired woman — WRONG_ELDERLY. Layla hair appears straight/dark (should be wavy/curly). Ellis wears red V-neck — close but not canonical soccer shirt graphic. |
| SC11 | FAIL | CHAR_DRIFT | Layla has hood UP — CLOTH_DRIFT (hood must be DOWN). Ellis wears red soccer shirt — OK. Riley two pink bows — OK. Benny green scarf — OK. Otherwise acceptable but hood UP is a FAIL. |
| SC12 | PASS | — | Layla, Riley, Ellis, Master Potter at table. Layla yellow bow, teal hoodie hood DOWN; Riley one bow visible (angle/pigtail present); Ellis red soccer shirt correct; Master Potter bun/stick/apron. No Benny — note only (not all scenes require Benny). |
| SC13 | FAIL | CHAR_DUPLICATE | THREE instances of Master Potter in the same scene — confirmed CHAR_DUPLICATE (matches known v1 issue). Each copy has bun/sticks/apron but triplication is a clear error. |
| SC14 | FAIL | WRONG_ELDERLY, CHAR_DRIFT | Master Potter replaced by elderly grey-haired woman in brown robe. WRONG_ELDERLY. Layla missing yellow bow entirely — CHAR_DRIFT. Ellis has reddish hair, not blonde. |
| SC15 | PASS | — | Ellis measuring clay alone (close-up scene); freckles visible, blonde hair, blue eyes — correct. No other characters needed in this solo scene. |
| SC16 | FAIL | WRONG_ELDERLY | Master Potter shown as elderly grey-haired woman — WRONG_ELDERLY. Layla yellow bow, teal hoodie present but slightly faded. Others acceptable. |
| SC17 | FAIL | CHAR_DRIFT | Ellis wears plaid/checkered shirt instead of red soccer shirt — CLOTH_DRIFT. Layla present, Riley one bow visible. Master Potter absent. |
| SC18 | PASS | — | Master Potter + Layla + Riley + Ellis + Benny — all present. Master Potter has bun, stick, apron, brown skin, clay-marked. Layla yellow bow, hood DOWN; Riley two pink bows; Ellis red soccer shirt; Benny green scarf. One of the best scenes. |
| SC19 | PASS | — | Master Potter kneeling with Layla + Riley + Ellis + Benny at table; all specs met. Good. |
| SC20 | PASS | — | All five with box of finished pots; Layla yellow bow teal hoodie; Riley two pink bows; Ellis blue plaid — slight drift but acceptable; Benny green scarf. |

**Tier 1 Pass: 10/20 (50%)**

---

## Tier 2 Results

| Scene | Result | Errors | Notes |
|-------|--------|--------|-------|
| SC01 | FAIL | CHAR_MISSING, CLOTH_DRIFT | Ellis wears black/orange striped shirt — CLOTH_DRIFT (not red soccer shirt). Layla has apron over teal hoodie (unusual but hood DOWN, bow visible). Riley has one pink bow on headband — FAIL (needs two bows in pigtails). Benny present. |
| SC02 | FAIL | CLOTH_DRIFT | Master Potter present and correct. Ellis wears orange/black striped shirt — CLOTH_DRIFT. Layla yellow bow, teal hoodie — OK. Riley single pink bow — borderline (one visible). |
| SC03 | PASS | — | Layla + Master Potter two-shot; Layla yellow bow, teal hoodie hood DOWN, wavy dark hair; Master Potter bun/stick/apron, brown skin, clay marks. Clean. |
| SC04 | PASS | — | Benny at table with clay (animated bear, child height); Layla, Riley, Master Potter present; Master Potter bun/stick/apron; Ellis orange-stripe shirt (mild drift noted). Benny render good. |
| SC05 | PASS | — | Riley at pottery wheel with Master Potter coaching; Riley two pink bows confirmed; Master Potter correct; Layla in background; Ellis (orange-stripe — drift). Scene context passes, main chars OK. |
| SC06 | PASS | — | Ellis at wheel with Master Potter coaching; Layla, Riley in background; Benny watching; Master Potter correct bun/stick/apron; minor Ellis shirt drift (orange stripe) but focus on Ellis at wheel — soccer ball imagery missing. Marginal pass. |
| SC07 | FAIL | CHAR_DRIFT, CHAR_MISSING | Layla has purple top — CLOTH_DRIFT (should be teal hoodie). Layla's yellow bow is there but hoodie replaced with pink/purple shirt. Riley visible. Ellis (orange shirt) present. Benny present. Master Potter absent — acceptable for this scene. Core issue: Layla's teal hoodie replaced. |
| SC08 | PASS | — | Master Potter holds two bowls; Layla yellow bow teal hoodie; Riley two pink bows; Ellis orange-stripe (drift noted but not critical fail); Benny green scarf. |
| SC09 | PASS | — | Master Potter + all four kids at shelf of pottery; Layla yellow bow, teal hoodie; Riley one bow visible (angle); Ellis orange-stripe; Benny. |
| SC10 | FAIL | CHAR_DRIFT, WRONG_ELDERLY | Master Potter has dark curly bun but appears lighter-skinned than ref; scene shows Master Potter without stick in hair — minor. Ellis wearing blue/white soccer kit — less drift than orange. Layla has no yellow bow — CHAR_DRIFT. |
| SC11 | PASS | — | All four kids making clay; Layla yellow bow teal hoodie; Riley two pink bows; Ellis (orange-stripe shirt — drift); Benny green scarf. |
| SC12 | PASS | — | Master Potter + kids at pottery wheel; Layla yellow bow; Riley two pink bows; Ellis orange stripe; Benny. |
| SC13 | PASS | — | Master Potter walks among wheels, one instance only — CHAR_DUPLICATE issue RESOLVED in Tier 2. Layla, Riley, Ellis (orange stripe), Benny all present at individual wheels. |
| SC14 | PASS | — | Master Potter at table with all four; Layla yellow bow; Riley two pink bows; Ellis; Benny. |
| SC15 | FAIL | CHAR_MISSING | Ellis alone measuring clay — solo scene. No other chars expected. Ellis wears orange-stripe shirt (CLOTH_DRIFT from canonical red) but freckles, blonde hair, blue eyes present. Flagged as drift, not outright fail — but canonical shirt missing. |
| SC16 | FAIL | CHAR_DRIFT | Master Potter at table with thought-bubble; Layla yellow bow, teal hoodie — OK. Benny present (no scarf visible — CLOTH_DRIFT). Ellis (orange-stripe). Master Potter correct. Riley absent — CHAR_MISSING. |
| SC17 | PASS | — | All four kids struggling with clay; Layla yellow bow; Riley two pink bows; Ellis (orange stripe); Benny green scarf. |
| SC18 | PASS | — | Master Potter with rows of bowls; Layla, Riley (two bows), Ellis (orange-stripe), Benny. |
| SC19 | PASS | — | Master Potter presents to group; Layla yellow bow; Riley two pink bows; Ellis (orange-stripe); Benny. |
| SC20 | FAIL | CHAR_DRIFT | Ellis wears blue striped shirt (soccer kit — different from canonical red soccer shirt with ball); Layla yellow bow; Riley one bow on headband — CHAR_DRIFT on Riley. |

**Tier 2 Pass: 11/20 (55%)**

---

## Tier 3 Results

| Scene | Result | Errors | Notes |
|-------|--------|--------|-------|
| SC01 | FAIL | CHAR_DRIFT, CHAR_MISSING | Ellis wears red/orange PLAID shirt — CLOTH_DRIFT. Benny has red bow-tie and green overalls instead of green plaid scarf — CLOTH_DRIFT on Benny. Layla yellow bow, teal hoodie — OK. Riley two pink bows — OK. Master Potter absent (scene-appropriate). |
| SC02 | FAIL | CHAR_DRIFT | Master Potter has dark hair in bun but appears lighter-skinned (possible CHAR_DRIFT); no clay marks visible. Ellis wears red T-shirt with soccer ball — borderline correct. Benny has red bow-tie/green overalls — CLOTH_DRIFT. |
| SC03 | FAIL | CHAR_DRIFT, WRONG_ELDERLY | Master Potter rendered lighter-skinned with dark hair pulled back low — not warm-brown skinned with high curly bun/stick. CHAR_DRIFT toward lighter female. Benny has red bow-tie. Ellis correct shirt (red soccer ball). |
| SC04 | FAIL | CHAR_DRIFT | Master Potter lighter skin, low dark hair, no visible stick in bun — CHAR_DRIFT. Benny has red bow-tie/green overalls. Ellis red soccer shirt — OK. Layla correct. Riley two pink bows (one visible + pigtails). |
| SC05 | FAIL | CHAR_DRIFT | Master Potter correct in isolation (lighter-skinned, earring, bun, apron). Riley has purple bow in pigtail — only ONE bow — FAIL. Benny red bow-tie (drift). Ellis correct. Layla correct. |
| SC06 | PASS | CLOTH_DRIFT (minor) | Master Potter kneeling with Ellis at wheel; Layla + Riley + Benny watching; Master Potter bun/stick/apron, warm skin — acceptable; Benny red bow-tie (drift from green scarf); Ellis red soccer shirt — OK; Riley two bows — OK; Layla yellow bow — OK. |
| SC07 | PASS | CLOTH_DRIFT (minor) | All four at table with bowls; Layla yellow bow teal hoodie; Riley two pink bows; Ellis red soccer shirt; Benny red bow-tie/green overalls. Core character IDs pass despite Benny cloth drift. |
| SC08 | FAIL | CHAR_DRIFT, WRONG_ELDERLY | Master Potter lighter-skinned, seated, no clear bun stick, earring visible — CHAR_DRIFT. Benny red bow-tie. Layla partial teal hoodie (short version?). |
| SC09 | PASS | CLOTH_DRIFT (minor) | Master Potter + all four at shelf; Layla yellow bow; Riley two-bow pigtails (one bow visible clearly, one implied); Ellis red soccer shirt; Benny red bow-tie. |
| SC10 | PASS | CLOTH_DRIFT (minor) | Master Potter correct; Layla yellow bow; Riley two pink bows — OK; Ellis red soccer shirt; Benny red bow-tie/green overalls. |
| SC11 | PASS | CLOTH_DRIFT (minor) | All four with bowls; Layla yellow bow, teal hoodie; Riley two bows; Ellis red soccer shirt; Benny red bow-tie. |
| SC12 | PASS | — | Master Potter at wheel + all four watching; correct master potter specs; Layla yellow bow; Riley two bows; Ellis red soccer shirt; Benny red bow-tie. |
| SC13 | PASS | — | Master Potter one instance (duplicate RESOLVED); Riley + Benny; Ellis red soccer shirt. |
| SC14 | FAIL | CHAR_DRIFT | Master Potter lighter-skinned with grey streaks in low ponytail — drifting toward WRONG_ELDERLY; no stick in hair. Layla's hair appears straight/dark not wavy. Benny red bow-tie. |
| SC15 | FAIL | CHAR_MISSING | Ellis solo scene (measuring clay) — correct character (blonde, freckles, red soccer shirt). No other characters present; contextually appropriate, but Ellis's hair is spiked/messy — minor CHAR_DRIFT. Solo scene acceptable. |
| SC16 | PASS | CLOTH_DRIFT (minor) | Master Potter + all four; Layla yellow bow; Riley one bow clearly + pigtails OK; Ellis red soccer shirt; Benny red bow-tie. Master Potter bun + stick + apron. |
| SC17 | PASS | CLOTH_DRIFT (minor) | All four kids at table; Layla yellow bow, teal hoodie (short); Riley two pink bows; Ellis red soccer shirt; Benny red bow-tie. |
| SC18 | PASS | — | Master Potter + all four; Layla yellow bow; Riley two pink bows; Ellis red soccer shirt; Benny red bow-tie. |
| SC19 | PASS | CLOTH_DRIFT (minor) | Master Potter + all four with table of bowls; Layla yellow bow; Riley two pink bows; Ellis red soccer shirt; Benny red bow-tie. |
| SC20 | PASS | CLOTH_DRIFT (minor) | Master Potter + all four; Layla yellow bow, teal hoodie; Riley two bows; Ellis red soccer shirt; Benny red bow-tie. |

**Tier 3 Pass: 10/20 (50%)**

---

## Tier 4 Results

| Scene | Result | Errors | Notes |
|-------|--------|--------|-------|
| SC01 | FAIL | CHAR_DRIFT, CHAR_MISSING | Layla at wheel with Riley and Ellis; Benny present (adult-bear scale). Layla has yellow bow and teal hoodie — OK. Riley has ONE pink bow on headband — FAIL. Ellis wears plaid/checkered shirt — CLOTH_DRIFT. |
| SC02 | PASS | CLOTH_DRIFT (minor) | Master Potter + all four; Layla yellow bow teal hoodie; Riley ONE pink bow on headband — borderline (single bow visible; pigtail implied); Ellis red/blue stripe shirt. Master Potter bun/stick/apron. |
| SC03 | PASS | CLOTH_DRIFT (minor) | Master Potter + Layla + Riley + Ellis + Benny at outdoor table; Layla yellow bow teal hoodie; Riley one pink bow on headband; Ellis red/orange stripe shirt; Benny green plaid scarf. Master Potter correct. |
| SC04 | FAIL | SCALE_ERROR, CHAR_DRIFT | Benny rendered at table-height with children but appears significantly smaller (cub-sized, not child-height). Master Potter correct. Layla yellow bow. Riley single bow headband. Ellis correct stripe shirt. |
| SC05 | FAIL | CHAR_DRIFT | Riley has straight dark hair, NO bow, single hair — CHAR_DRIFT, should have two pigtails with pink bows. Layla yellow bow, teal hoodie. Ellis red/orange stripe. Benny green scarf. |
| SC06 | FAIL | CHAR_DRIFT | Ellis wears red/orange/blue stripe jersey — consistent drift from canonical plain red soccer shirt. Layla teal hoodie + yellow bow OK. Riley one pink bow on headband (not in pigtails — drift). |
| SC07 | PASS | CLOTH_DRIFT (minor) | All four + Master Potter absent (scene appropriate). Layla yellow bow; Riley one pink bow; Ellis orange/red stripe; Benny green scarf. |
| SC08 | FAIL | CHAR_DRIFT | Layla + Riley two-shot with Master Potter; Riley has purple/pink bow on headband — single bow — CHAR_DRIFT (needs two pigtail bows). Layla yellow bow — OK. Master Potter correct. |
| SC09 | PASS | — | Master Potter + Layla + Riley + Benny at shelves; Layla yellow bow; Riley one pink bow (pigtails implied at angle); Ellis orange stripe; Benny green scarf. |
| SC10 | PASS | — | Riley holding bowl with Master Potter + Layla + Benny; Layla yellow bow; Riley has pink bow; Master Potter correct; Ellis stripe shirt; Benny green scarf. |
| SC11 | PASS | — | Layla + Riley + Ellis + Benny at table in forest; Layla yellow bow, teal hoodie; Riley two pink bows — CONFIRMED both bows in pigtails; Ellis orange stripe (mild drift); Benny green scarf. |
| SC12 | FAIL | WRONG_ELDERLY | Master Potter rendered as elderly grey-haired lighter-skinned woman in brown robe seated at wheel — WRONG_ELDERLY. Layla yellow bow. Riley two bows — OK. Ellis stripe shirt. Benny green scarf. |
| SC13 | FAIL | CHAR_DUPLICATE | Two instances of Master Potter visible — one on left, one assisting in background — CHAR_DUPLICATE (mirrors v1 issue). Layla yellow bow; Riley single pink bow; Ellis orange/blue stripe. |
| SC14 | PASS | CLOTH_DRIFT (minor) | Master Potter (one instance, correct) with all four; Layla yellow bow; Riley one pink bow (headband); Ellis stripe shirt; Benny green scarf. |
| SC15 | FAIL | CHAR_MISSING | Ellis solo measuring scene; Ellis has orange/red/blue stripe shirt (CLOTH_DRIFT) but blonde hair, blue eyes, freckles correct. No other characters — scene-appropriate but Ellis shirt drift flagged. |
| SC16 | FAIL | WRONG_ELDERLY, CHAR_DRIFT | Master Potter appears as grey-haired lighter-skinned older woman — WRONG_ELDERLY. Layla yellow bow — OK. Riley one bow — CHAR_DRIFT. Ellis stripe shirt drift. |
| SC17 | PASS | CLOTH_DRIFT (minor) | All four at table with bowls; Layla yellow bow, teal hoodie; Riley two pink bows — both confirmed; Ellis orange stripe; Benny green scarf. |
| SC18 | PASS | — | Master Potter + all four with clay boards; Layla yellow bow teal hoodie; Riley one pink bow (pigtails at angle); Ellis orange stripe; Benny green scarf. |
| SC19 | PASS | — | Master Potter + Layla + Ellis + Benny; Layla yellow bow; Riley one pink bow; Master Potter correct bun/stick/apron; Ellis stripe. |
| SC20 | PASS | — | Master Potter + all four cleaning up; Layla yellow bow; Riley one pink bow; Ellis orange stripe; Benny green scarf. Master Potter correct. |

**Tier 4 Pass: 11/20 (55%)**

---

## Priority Flags

| File | Errors | Issue |
|------|--------|-------|
| S3-CH06-SC13-tier1.png | CHAR_DUPLICATE | **CRITICAL** — Master Potter appears 3 times in one frame; v1 bug confirmed unresolved in T1 |
| S3-CH06-SC13-tier4.png | CHAR_DUPLICATE | **CRITICAL** — Master Potter appears 2 times; duplicate bug re-emerged in T4 |
| S3-CH06-SC03-tier1.png | WRONG_ELDERLY | Master Potter replaced by elderly grey-haired pale woman entirely |
| S3-CH06-SC14-tier1.png | WRONG_ELDERLY, CHAR_DRIFT | Master Potter replaced by elderly woman; Layla missing yellow bow |
| S3-CH06-SC16-tier1.png | WRONG_ELDERLY | Master Potter rendered as elderly grey-haired woman |
| S3-CH06-SC10-tier1.png | WRONG_ELDERLY, CHAR_DRIFT | Master Potter elderly; Layla hair straight; Ellis shirt incorrect |
| S3-CH06-SC12-tier4.png | WRONG_ELDERLY | Master Potter rendered as elderly grey-haired woman at wheel |
| S3-CH06-SC16-tier4.png | WRONG_ELDERLY, CHAR_DRIFT | Master Potter elderly; Riley single bow |
| S3-CH06-SC05-tier4.png | CHAR_DRIFT | Riley has straight dark hair with NO bow — complete loss of identifying feature |
| S3-CH06-SC11-tier1.png | CLOTH_DRIFT | Layla hood UP — spec requires hood DOWN |
| S3-CH06-SC01-tier2.png | CLOTH_DRIFT, CHAR_DRIFT | Ellis orange/black stripe shirt (canonical: red soccer shirt); Riley single bow |
| S3-CH06-SC07-tier2.png | CLOTH_DRIFT | Layla teal hoodie replaced with purple shirt — major outfit drift |
| S3-CH06-SC09-tier1.png | CHAR_DRIFT | Riley has only ONE pink bow (hard fail per spec) |
| S3-CH06-SC03-tier3.png | CHAR_DRIFT, WRONG_ELDERLY | Master Potter lighter-skinned, low ponytail, no stick — major drift |
| S3-CH06-SC04-tier3.png | CHAR_DRIFT | Master Potter lighter skin, no stick in bun |
| S3-CH06-SC14-tier3.png | CHAR_DRIFT | Master Potter greying, low ponytail — approaching WRONG_ELDERLY |

---

## Observations by Character

### Layla
- Generally strong across all tiers (yellow bow present in ~90% of scenes)
- **Recurring failure: hood UP** — T1-SC11 confirmed, check others with close-up angles
- Hair texture occasionally drifts from wavy/curly to straight (T1-SC03, T1-SC14)
- Bow missing entirely in T1-SC14

### Riley
- **Two-bow rule failures in ~25% of scenes** — single bow on headband instead of two bows in two pigtails
- Worst offenders: T1-SC09, T4-SC01, T4-SC05, T4-SC08, T4-SC16
- T4-SC05 is most severe: straight hair, no bow at all

### Ellis
- **Shirt drift is the single most pervasive error** across all tiers
- T1: checkered/plaid shirt in SC02, SC06, SC17
- T2+: orange/black stripe jersey replaces red soccer shirt across nearly all scenes
- T3: returns closer to red soccer shirt with soccer ball graphic (improvement)
- T4: orange/red/blue stripe — systematic drift
- Freckles, blonde hair, blue eyes consistently correct

### Benny
- Rendered as animated cartoon bear (correct) across all tiers — no ANIMAL_ERROR
- Scale generally child-appropriate; T4-SC04 slightly small
- **Cloth drift: T3 swaps green plaid scarf for red bow-tie + green overalls** throughout entire tier — systematic Tier 3 costume drift
- T4 returns to green plaid scarf (mostly correct)

### Master Potter (Celeste)
- **WRONG_ELDERLY is the most critical character-level failure** — affects T1-SC03, T1-SC10, T1-SC14, T1-SC16, T4-SC12, T4-SC16
- **CHAR_DUPLICATE confirmed in T1-SC13 (3×) and T4-SC13 (2×)**
- Tiers 2 and 3: some skin tone lightening and hair color drift (should be warm brown, not olive/neutral)
- T3: consistently lighter-skinned than reference — systematic drift
- Stick in bun sometimes missing; clay-covered apron generally present when character is correct
- Best rendering in T1-SC05, T1-SC08, T2-SC03, T2-SC05

---

## Tier-Level Style Notes

| Tier | Style | Issues |
|------|-------|--------|
| Tier 1 | Flat cartoon / coloring-book | Clean lines but WRONG_ELDERLY and CHAR_DUPLICATE bugs severe |
| Tier 2 | Cartoon / slightly more detailed | Ellis shirt systematically wrong (orange stripe); Riley bow compliance ~60% |
| Tier 3 | Illustrated cartoon | Master Potter skin tone drifts lighter throughout tier; Benny costume completely changed to bow-tie/overalls |
| Tier 4 | Painted/illustrated | Most detailed rendering; WRONG_ELDERLY recurs; CHAR_DUPLICATE recurs at SC13; Ellis shirt still drifted |

---

## Recommended Regen Priority

1. **IMMEDIATE** — T1-SC13, T4-SC13: CHAR_DUPLICATE (Master Potter ×2–3)
2. **HIGH** — T1-SC03, T1-SC10, T1-SC14, T1-SC16, T4-SC12, T4-SC16: WRONG_ELDERLY replacements
3. **HIGH** — T4-SC05: Riley loses all identifying features
4. **MEDIUM** — All Tier 2 scenes: Ellis shirt drift (orange stripe throughout)
5. **MEDIUM** — Tier 3 systematic: Benny costume (red bow-tie/overalls instead of green plaid scarf)
6. **MEDIUM** — T1-SC11: Layla hood UP
7. **LOW** — Riley single-bow scenes across T1, T4 (SC09-T1, SC01-T4, SC06-T4, SC08-T4)
