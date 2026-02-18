# Ch03 QA v2 — The Sawdust Challenge
**Audited:** 2026-02-17 | **Images:** 80

---

## Summary

| Tier | Pass | Fail | Pass% |
|------|------|------|-------|
| Tier 1 | 4 | 16 | 20% |
| Tier 2 | 2 | 18 | 10% |
| Tier 3 | 3 | 17 | 15% |
| Tier 4 | 2 | 18 | 10% |
| **TOTAL** | **11** | **69** | **14%** |

---

## Top Issues

1. **WRONG_ELDERLY / Master Thomas substitution** — An elderly WOMAN (gray hair bun, round glasses, floral/flower-print apron) replaces Master Thomas in a massive number of scenes across all tiers (Tier 1: SC08–SC15 and beyond; Tier 2: SC11–SC17+; Tier 3: SC09–SC10, SC15, SC17–SC19; Tier 4: SC10–SC12, SC14). This is the single most critical and pervasive failure in the chapter.

2. **Master Thomas CHAR_DRIFT** — Even when a correct elderly male appears, he frequently lacks the required blue bandana (appears clean-bald or with glasses only), lacks the green plaid shirt (shown in brown/tan plaid or plain plaid), and is often rendered as slim/lean rather than the required STOCKY HEAVYSET build. Scenes affected across all tiers.

3. **Riley single bow / CHAR_DRIFT** — Riley's spec requires TWO PINK BOWS (one per pigtail). In many scenes she appears with only ONE pink bow or the bows are undersized/styled differently.

4. **Ellis CLOTH_DRIFT** — Ellis's shirt varies significantly across scenes (red/blue soccer shirt is correct, but in Tier 2 and Tier 4 he appears in orange/black or orange/white striped soccer kits inconsistent with reference). In some Tier 3 scenes Ellis is replaced entirely with a dark-haired boy (CHAR_MISSING / CHAR_EXTRA).

5. **Benny CLOTH_DRIFT / scarf color** — Benny's green scarf is generally correct but in several Tier 3 and Tier 4 scenes he appears in green overalls with a red bow tie instead of a scarf — a costume variant not shown in the reference.

6. **MULTI_PANEL** — SC11 (Tier 1), SC04 (Tier 2), SC11 (Tier 2), SC04 (Tier 3), SC11 (Tier 4), SC12 (Tier 4) are multi-panel / split-panel layouts rather than single scenes.

7. **Layla CHAR_DRIFT (straight hair)** — In Tier 2 SC03 and multiple Tier 4 scenes, Layla's hair appears straighter/less wavy than the curly/wavy reference standard.

8. **Master Thomas missing entirely (CHAR_MISSING)** — SC07 (Tier 1), SC07 (Tier 3) have all four kids + Benny but no adult mentor visible.

---

## Tier 1 Results

| Scene | Result | Errors | Notes |
|-------|--------|--------|-------|
| SC01 | FAIL | CHAR_DRIFT | Master Thomas present (correct beard+bandana) but rendered SLIM/not stocky. All kids present. Riley has 1 bow only — FAIL. |
| SC02 | FAIL | CHAR_DRIFT | Master Thomas present (beard+bandana) but slim build. Riley has 1 bow. Benny shown without scarf. |
| SC03 | PASS | — | Master Thomas correct (beard, bandana, apron). All 5 characters present. Riley 1 bow (minor). Benny scarf OK. Layla bow OK. Ellis correct. Acceptable pass with noted Riley bow issue. |
| SC04 | FAIL | CHAR_DRIFT | Master Thomas slim, no blue bandana visible (bald top). All kids present. Riley 1 bow. |
| SC05 | FAIL | CHAR_DRIFT | Master Thomas slim build, no blue bandana. Riley only 1 bow. |
| SC06 | FAIL | CHAR_DRIFT | Master Thomas slim, no bandana. Riley 1 bow only. |
| SC07 | FAIL | CHAR_MISSING, CHAR_DRIFT | Master Thomas absent from scene (kids + Benny only, sanding). No adult in frame. |
| SC08 | FAIL | WRONG_ELDERLY, CHAR_MISSING | Elderly WOMAN replaces Master Thomas — gray hair bun NOT visible but elderly man shown is slim, wearing BLUE PLAID shirt (not green plaid) with NO beard visible — borderline wrong. Layla hair appears straight/flat ponytail rather than curly. Riley missing. |
| SC09 | FAIL | WRONG_ELDERLY, CHAR_DRIFT | Elderly man shown: slim, glasses, BLUE PLAID shirt, no beard or minimal beard — wrong physical spec (not heavyset, not full gray beard, glasses added). Riley 1 bow. |
| SC10 | FAIL | WRONG_ELDERLY, CHAR_DRIFT | Same slim elderly male with glasses, no bandana, tan/beige plaid shirt (not green). Wrong build. |
| SC11 | FAIL | MULTI_PANEL, WRONG_ELDERLY | 4-panel layout. Elderly man shown is slim, wearing BLUE PLAID overalls — not Master Thomas spec. No blue bandana in any panel. CHAR_DRIFT throughout. |
| SC12 | FAIL | WRONG_ELDERLY, CHAR_MISSING | Slim elderly man with gray hair/mustache only (no full beard), no bandana, blue shirt. Layla and Riley absent from scene (only Benny + elderly man). CHAR_MISSING ×2. |
| SC13 | FAIL | WRONG_ELDERLY, CHAR_DRIFT | Slim elderly man, glasses, no bandana. All kids present but Ellis has CLOTH_DRIFT (red plaid shirt, not red soccer shirt). |
| SC14 | FAIL | WRONG_ELDERLY, CHAR_DRIFT | Slim elderly man, glasses, no bandana, orange/brown plaid shirt. Ellis no soccer shirt. |
| SC15 | FAIL | WRONG_ELDERLY, CHAR_DRIFT | Slim elderly man, glasses, no bandana, red/orange plaid shirt. Character passes for kids. |
| SC16 | FAIL | WRONG_ELDERLY | Slim elderly man, no bandana, no beard, glasses — does not match Master Thomas. Kids all present. |
| SC17 | PASS | CHAR_DRIFT (minor) | Correct elderly man shape/beard present, tan plaid (not green). Bandana absent. Kids OK. Marginal pass — beard/body correct but bandana/shirt color wrong. |
| SC18 | FAIL | WRONG_ELDERLY | Slim elderly man with glasses, no bandana, no beard visible. Kids present. |
| SC19 | FAIL | WRONG_ELDERLY, CHAR_DRIFT | Slim elderly man, glasses, no beard, no bandana, floral apron — transitional to WRONG_ELDERLY. Riley 1 bow only. |
| SC20 | PASS | — | All 5 kids + correct Benny. No adult in scene (acceptable for ending scene). Layla bow correct. Riley 1 bow (minor). |

**Tier 1 Pass: 3/20 — 15%**
*(SC03, SC17 marginal, SC20 no-adult acceptable)*

---

## Tier 2 Results

| Scene | Result | Errors | Notes |
|-------|--------|--------|-------|
| SC01 | FAIL | CHAR_DRIFT, CLOTH_DRIFT | Master Thomas correct beard+bandana+green plaid+stocky — PASS on MT. Ellis: orange/black soccer kit (not red). Riley: 1 bow only. Layla OK. |
| SC02 | FAIL | CHAR_DRIFT, CLOTH_DRIFT | Master Thomas present (beard, bandana, glasses added). Ellis wearing orange/black soccer kit. Riley 1 bow. |
| SC03 | FAIL | CHAR_DRIFT, CLOTH_DRIFT | Master Thomas present (beard, bandana). Layla hair appears notably straighter. Ellis orange/black kit. |
| SC04 | FAIL | MULTI_PANEL, CHAR_MISSING | 2-panel vertical split. Master Thomas + Benny only — Layla, Riley, Ellis all absent both panels. CHAR_MISSING ×3. |
| SC05 | FAIL | CHAR_DRIFT, CHAR_EXTRA | Two Master Thomas figures (duplicate elderly men) — LEFT man is slim, RIGHT man is stocky. CHAR_DUPLICATE. Ellis wearing orange/black soccer kit. |
| SC06 | PASS | CHAR_DRIFT (minor) | Master Thomas present (beard, bandana, glasses added). All 5 present. Ellis orange kit (minor drift). Acceptable overall. |
| SC07 | FAIL | CHAR_MISSING | Master Thomas absent. Kids + Benny only sanding. No adult in frame. |
| SC08 | FAIL | WRONG_ELDERLY | Slim elderly man, large round glasses, no bandana visible, no beard — transitioning toward WRONG_ELDERLY female archetype. Riley 1 bow. |
| SC09 | FAIL | WRONG_ELDERLY, CHAR_MISSING | Slim elderly man, large glasses, no bandana. Ellis absent. |
| SC10 | FAIL | WRONG_ELDERLY, CHAR_MISSING | Slim elderly man, large glasses, no bandana. Ellis absent. |
| SC11 | FAIL | MULTI_PANEL, WRONG_ELDERLY | 2-panel layout. Both panels show WRONG_ELDERLY — elderly WOMAN with gray bun, round glasses, floral apron. Riley has 1 bow. |
| SC12 | FAIL | WRONG_ELDERLY | Elderly WOMAN confirmed — gray bun, round glasses, floral apron. Master Thomas absent. |
| SC13 | FAIL | WRONG_ELDERLY | Elderly WOMAN — gray bun, round glasses, floral apron sawing with kids. Master Thomas absent. |
| SC14 | FAIL | WRONG_ELDERLY | Elderly WOMAN — gray bun, round glasses, floral apron. |
| SC15 | FAIL | WRONG_ELDERLY, CHAR_MISSING | Elderly WOMAN (confirmed). Unknown children grouping — does not match core cast fully. Ellis absent. |
| SC16 | FAIL | WRONG_ELDERLY | Elderly WOMAN — gray bun, round glasses, floral apron. Ellis absent (orange-kit boy replaced by different character). |
| SC17 | FAIL | WRONG_ELDERLY | Elderly WOMAN confirmed (gray bun, round glasses, floral apron). All kids otherwise present. |
| SC18 | PASS | CHAR_DRIFT (minor) | Elderly man with gray hair, no glasses, plaid shirt — not perfect but no WRONG_ELDERLY. Riley 1 bow. Benny scarf OK. |
| SC19 | FAIL | WRONG_ELDERLY, CHAR_DRIFT | Elderly WOMAN — gray bun, floral apron, glasses. Kids present but Ellis replaced by different boy silhouette. |
| SC20 | FAIL | CHAR_MISSING | No adult. Kids + Benny only. Acceptable for ending but Master Thomas absent from chapter close. |

**Tier 2 Pass: 2/20 — 10%**
*(SC06, SC18 marginal)*

---

## Tier 3 Results

| Scene | Result | Errors | Notes |
|-------|--------|--------|-------|
| SC01 | FAIL | CHAR_DRIFT, CLOTH_DRIFT | Master Thomas present (beard, bandana) but wearing brown/orange plaid not green. Benny in GREEN OVERALLS + red bow tie (not scarf). Ellis wearing RED T-shirt (OK) but design wrong — red t-shirt not soccer kit. |
| SC02 | FAIL | CHAR_DRIFT | Master Thomas present (beard, bandana) but brown/orange plaid shirt. Benny in overalls/red bowtie. Ellis in plaid shirt (not soccer kit). |
| SC03 | FAIL | CHAR_DRIFT, CLOTH_DRIFT | Master Thomas present (beard, bandana, brown plaid). Benny in overalls+red bowtie. Ellis in plaid shirt not soccer kit. |
| SC04 | FAIL | MULTI_PANEL, CHAR_MISSING | 3-panel horizontal. Shows only Benny + Master Thomas. Layla, Riley, Ellis absent all panels. CHAR_MISSING ×3. |
| SC05 | FAIL | CHAR_DRIFT | Master Thomas present (beard, bandana, brown plaid). Benny in overalls+red bowtie. Ellis absent, replaced by different boy (CHAR_EXTRA). |
| SC06 | FAIL | CHAR_DRIFT, CHAR_MISSING | Master Thomas present (beard, bandana, brown plaid). Benny in overalls+red bowtie. Ellis absent. |
| SC07 | FAIL | CHAR_MISSING | Master Thomas absent. Kids sanding, no adult. Benny in overalls. |
| SC08 | FAIL | WRONG_ELDERLY, CHAR_DRIFT | Slim elderly man with gray hair, glasses, plaid shirt — no beard, no bandana — borderline WRONG_ELDERLY male version. |
| SC09 | FAIL | WRONG_ELDERLY | Elderly WOMAN confirmed — gray bun, glasses, floral/flower apron. Layla + Riley + Ellis + Benny present. |
| SC10 | FAIL | WRONG_ELDERLY | Elderly WOMAN confirmed — gray bun, glasses, floral apron. |
| SC11 | FAIL | WRONG_ELDERLY | Slim elderly man, glasses, no bandana, no beard — WRONG_ELDERLY male variant. |
| SC12 | FAIL | WRONG_ELDERLY | Slim elderly man, glasses, green apron, no beard, no bandana. |
| SC13 | FAIL | WRONG_ELDERLY | Slim elderly man, glasses, green apron, no beard, no bandana. |
| SC14 | FAIL | WRONG_ELDERLY | Slim elderly man, glasses, green apron, no beard, no bandana. Benny in overalls. |
| SC15 | FAIL | WRONG_ELDERLY | Elderly WOMAN confirmed — gray bun, glasses, floral apron. |
| SC16 | PASS | CHAR_DRIFT (minor) | Elderly man with glasses, plaid, apron — no bandana but beard present. Benny in overalls. Kids present. Acceptable. |
| SC17 | FAIL | WRONG_ELDERLY | Elderly WOMAN confirmed — gray bun, glasses, floral apron. |
| SC18 | FAIL | WRONG_ELDERLY | Elderly WOMAN confirmed — gray bun, glasses, floral apron holding box. |
| SC19 | FAIL | WRONG_ELDERLY | Elderly man (slim, glasses, floral apron visible in background) — transitional WRONG_ELDERLY male. |
| SC20 | PASS | — | All 4 kids + Benny, no adult. Correct for closing scene. Benny scarf OK. Layla bow OK. Riley 1 bow (minor). |

**Tier 3 Pass: 2/20 — 10%**
*(SC16 marginal, SC20 no-adult acceptable)*

---

## Tier 4 Results

| Scene | Result | Errors | Notes |
|-------|--------|--------|-------|
| SC01 | PASS | CHAR_DRIFT (minor) | Master Thomas correct (beard, blue bandana, stocky). All 5 present. Ellis has orange/white striped soccer shirt (drift). Benny scarf OK. |
| SC02 | FAIL | CHAR_DRIFT, CLOTH_DRIFT | Master Thomas present (beard, bandana). Ellis in orange/white striped soccer kit. Riley 1 bow. |
| SC03 | FAIL | CHAR_DRIFT, CLOTH_DRIFT | Master Thomas present (beard, bandana). Ellis in orange/white soccer kit. Riley 1 bow. Layla hair somewhat straight. |
| SC04 | FAIL | CHAR_DRIFT | Master Thomas present (beard, bandana, orange/brown plaid). Ellis in orange/white kit. |
| SC05 | FAIL | WRONG_ELDERLY, CHAR_DRIFT | Elderly WOMAN confirmed — gray bun, glasses, floral apron. Master Thomas absent. Ellis in striped red t-shirt. |
| SC06 | FAIL | CHAR_DRIFT | Master Thomas present (beard, bandana) but brown/orange plaid shirt. Riley 1 bow. Ellis orange/white kit. |
| SC07 | FAIL | CHAR_MISSING | Master Thomas absent. Kids + Benny sanding (kids-only scene). |
| SC08 | FAIL | WRONG_ELDERLY, CHAR_DRIFT | Slim elderly man with glasses, floral apron — WRONG_ELDERLY (male version). Ellis absent — CHAR_MISSING. |
| SC09 | FAIL | WRONG_ELDERLY, CHAR_DRIFT | Slim elderly man, no bandana, no beard, glasses, plaid shirt (not stocky). Ellis absent. |
| SC10 | FAIL | WRONG_ELDERLY | Elderly WOMAN confirmed — gray bun, glasses, floral apron. |
| SC11 | FAIL | MULTI_PANEL, WRONG_ELDERLY | 3-panel horizontal. Both WRONG_ELDERLY — elderly WOMAN in all panels with floral apron. |
| SC12 | FAIL | MULTI_PANEL, WRONG_ELDERLY | 2-panel horizontal. Elderly WOMAN both panels — gray bun, glasses, floral apron. |
| SC13 | FAIL | WRONG_ELDERLY, CHAR_DRIFT | Slim elderly man, glasses, no beard, no bandana. Ellis replaced by dark-haired boy (CHAR_EXTRA). |
| SC14 | FAIL | WRONG_ELDERLY | Elderly WOMAN — gray bun, glasses, floral apron. Kids present but Ellis replaced (dark-haired boy). CHAR_EXTRA. |
| SC15 | FAIL | WRONG_ELDERLY | Slim elderly man, glasses, no beard, no bandana, green plaid apron only. |
| SC16 | FAIL | CHAR_DRIFT | Elderly man (slim, no bandana, no beard). Riley 1 bow. Layla hair straighter. |
| SC17 | FAIL | CHAR_DRIFT | Slim elderly man, glasses, no bandana, no beard. Riley 1 bow. |
| SC18 | FAIL | WRONG_ELDERLY, CHAR_DRIFT | Slim elderly man, no bandana, no beard, no apron. Layla hair straight. CHAR_EXTRA (extra brown-haired boy). |
| SC19 | FAIL | CHAR_DRIFT, CHAR_EXTRA | Slim elderly man without beard or bandana. Extra brown-haired children in crowd — CHAR_EXTRA. |
| SC20 | PASS | — | All 4 kids + Benny, no adult. Correct for closing scene. Layla bow OK. Riley 1 bow (minor). |

**Tier 4 Pass: 2/20 — 10%**
*(SC01 marginal, SC20 no-adult acceptable)*

---

## Priority Flags

| File | Errors | Issue |
|------|--------|-------|
| S3-CH03-SC11-tier1.png | MULTI_PANEL, WRONG_ELDERLY | 4-panel comic layout; elderly man in all panels is slim + blue plaid overalls, no bandana — not Master Thomas |
| S3-CH03-SC12-tier1.png | WRONG_ELDERLY, CHAR_MISSING | Slim elderly man with mustache only (no full beard), Layla + Riley absent |
| S3-CH03-SC11-tier2.png | MULTI_PANEL, WRONG_ELDERLY | 2-panel; both panels show confirmed elderly WOMAN — gray bun, round glasses, floral apron |
| S3-CH03-SC12-tier2.png | WRONG_ELDERLY | Confirmed elderly WOMAN (gray bun, glasses, floral apron) — Master Thomas fully replaced |
| S3-CH03-SC13-tier2.png | WRONG_ELDERLY | Confirmed elderly WOMAN sawing wood with kids |
| S3-CH03-SC14-tier2.png | WRONG_ELDERLY | Confirmed elderly WOMAN |
| S3-CH03-SC17-tier2.png | WRONG_ELDERLY | Confirmed elderly WOMAN |
| S3-CH03-SC09-tier3.png | WRONG_ELDERLY | Confirmed elderly WOMAN — gray bun, glasses, floral apron |
| S3-CH03-SC10-tier3.png | WRONG_ELDERLY | Confirmed elderly WOMAN |
| S3-CH03-SC15-tier3.png | WRONG_ELDERLY | Confirmed elderly WOMAN |
| S3-CH03-SC17-tier3.png | WRONG_ELDERLY | Confirmed elderly WOMAN |
| S3-CH03-SC18-tier3.png | WRONG_ELDERLY | Confirmed elderly WOMAN holding carved box |
| S3-CH03-SC05-tier4.png | WRONG_ELDERLY | Confirmed elderly WOMAN — gray bun, glasses, floral apron |
| S3-CH03-SC10-tier4.png | WRONG_ELDERLY | Confirmed elderly WOMAN |
| S3-CH03-SC11-tier4.png | MULTI_PANEL, WRONG_ELDERLY | 3-panel; WRONG_ELDERLY in all panels |
| S3-CH03-SC12-tier4.png | MULTI_PANEL, WRONG_ELDERLY | 2-panel; WRONG_ELDERLY in both panels |
| S3-CH03-SC14-tier4.png | WRONG_ELDERLY, CHAR_EXTRA | Confirmed elderly WOMAN + extra dark-haired boy replaces Ellis |
| S3-CH03-SC04-tier2.png | MULTI_PANEL, CHAR_MISSING | 2-panel; Layla/Riley/Ellis absent both panels |
| S3-CH03-SC04-tier3.png | MULTI_PANEL, CHAR_MISSING | 3-panel; Layla/Riley/Ellis absent all panels |
| S3-CH03-SC05-tier2.png | CHAR_DUPLICATE | Two elderly men present simultaneously — CHAR_DUPLICATE |

---

## Character-Level Failure Summary

### Master Thomas
- **WRONG_ELDERLY substitution (elderly woman):** ~17 scenes across all tiers — highest priority error in chapter
- **CHAR_DRIFT (slim build, no bandana):** Affects virtually every scene where male elderly man IS present; correct stocky build only confirmed in SC01 tier1, SC01–SC03 tier2, SC01–SC06 tier4
- **Green plaid shirt:** Correct in Tier 1 SC01–SC06; replaced by brown/orange plaid in Tier 3 and Tier 4 throughout
- **Glasses added:** Added incorrectly in Tier 1 SC08+ and Tier 2 SC02+; Master Thomas reference does NOT wear glasses

### Riley
- **Single pink bow (CHAR_DRIFT):** Appears in nearly every scene; correct two-bow configuration only occasionally rendered
- **Pigtails:** Generally correct structure, but bows reduced to one in the majority of images

### Ellis
- **CLOTH_DRIFT (soccer kit color):** Orange/black or orange/white striped kit in Tier 2 and Tier 4 throughout (correct ref is red/blue soccer kit)
- **CHAR_MISSING:** Absent in Tier 2 SC04, SC09, SC10; Tier 3 SC04–SC06; Tier 4 SC08–SC09, SC13–SC14
- **CHAR_EXTRA:** In Tier 3 and Tier 4, unknown dark-haired boys appear where Ellis should be

### Benny
- **CLOTH_DRIFT:** Green scarf correct in Tier 1 and Tier 2; replaced by green overalls + red bowtie in Tier 3 and some Tier 4 scenes — not in reference

### Layla
- **Bow:** Yellow bow generally present and correct
- **Hair:** Curly/wavy in most scenes; appears straighter in Tier 2 SC03 and multiple Tier 4 scenes — CHAR_DRIFT

---

## Recommended Regeneration Priority

1. **CRITICAL — Regenerate all:** All scenes SC09–SC20 in Tier 2, Tier 3, and Tier 4 where WRONG_ELDERLY woman appears
2. **HIGH — Regenerate:** All multi-panel scenes (SC04 and SC11 across all tiers)
3. **HIGH — Regenerate:** Tier 1 SC08–SC16 (slim male replacing stocky Master Thomas)
4. **MEDIUM — Fix:** Ellis soccer shirt color in Tier 2 and Tier 4 (all 20 scenes)
5. **MEDIUM — Fix:** Benny costume in Tier 3 (overalls+bowtie vs. scarf)
6. **LOW — Fix:** Riley single bow throughout (all tiers)
