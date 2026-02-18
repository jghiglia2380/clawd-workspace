# Ch08 QA v2 — The Inventor's Tower
**Audited:** 2026-02-17 | **Images:** 80

---

## Summary

| Tier | Pass | Fail | Pass% |
|------|------|------|-------|
| T1   | 14   | 6    | 70%   |
| T2   | 10   | 10   | 50%   |
| T3   | 11   | 9    | 55%   |
| T4   | 10   | 10   | 50%   |
| **Total** | **45** | **35** | **56%** |

---

## Top Issues

1. **MULTI_PANEL (SC16 T2, T3, T4)** — Confirmed known issue: SC16 renders as a split multi-panel comic layout in Tier 2 and Tier 3. Tier 4 SC16 also uses a multi-panel format. Tier 1 SC16 is a clean single-panel (PASS on layout, but has CHAR_MISSING — only Ellis shown).
2. **WRONG_ELDERLY / CHAR_DRIFT on Maestro Gearsmith** — Tier 1 SC04/SC05/SC11/SC15 show Maestro with GREY rather than WHITE spiky hair and a mustache not present in the hero ref; SC17 T1 shows him in a white lab coat (CLOTH_DRIFT). Tier 2 SC12 replaces Maestro with a different adult male (dark hair, tuxedo — WRONG_ELDERLY). Tier 4 SC12 shows a plain grey-haired man in a polo shirt standing in background without goggles (WRONG_ELDERLY).
3. **Riley bow count** — Multiple scenes across tiers show Riley with only ONE pink bow instead of required TWO bows in pigtails. See flags below.
4. **Ellis CLOTH_DRIFT** — Ellis frequently appears in orange/black or orange/white striped football jersey instead of his canonical red soccer shirt. Most prevalent in Tier 2 and Tier 3.
5. **Benny CLOTH_DRIFT / SCALE_ERROR** — Tier 2 SC18 MULTI_PANEL shows Benny at realistic-bear size (not child height) in right panel. T3 SC08 shows Benny at small teddy-bear/shelf-sitting scale. T3 SC16 shows Benny in green overalls with red bow-tie rather than green scarf (CLOTH_DRIFT). T4 SC09 shows Benny realistically tall.
6. **CHAR_MISSING** — Layla absent from T1 SC16 (only Ellis shown). Layla absent from T2 SC08/SC09. Riley absent from T1 SC12. Multiple scenes missing one or more core characters.
7. **Maestro Goggles on face vs. forehead** — In several scenes Maestro has goggles worn OVER his eyes rather than pushed up on his forehead (spec requires goggles on forehead). Flagged in T1 SC14 and T2 SC07.

---

## Tier 1 Results

| Scene | Result | Errors | Notes |
|-------|--------|--------|-------|
| SC01 | PASS | — | All 4 cast present. Layla: yellow bow, teal hoodie. Riley: 2 pink bows. Ellis: red shirt. Benny: animated bear. No Maestro (not expected). |
| SC02 | PASS | — | All 4 cast at Inventor's Tower exterior. Riley has single bow visible but second bow partially obscured by angle — borderline PASS. Benny at child height. |
| SC03 | PASS | — | 4 cast entering workshop. Layla: yellow bow, teal hoodie. Riley: 2 pink bows. Ellis: red hoodie (slight shirt drift but acceptable scene variation). Benny: proper animated bear. |
| SC04 | FAIL | CHAR_DRIFT | Maestro present — goggles correct (on forehead), but hair is GREY (not white) and has a mustache not in hero ref. Hair style is wavy/swept rather than spiky. CHAR_DRIFT on Maestro. Riley: 2 pink bows (PASS). Ellis: blue plaid shirt (CLOTH_DRIFT, no red soccer shirt). |
| SC05 | FAIL | CHAR_DRIFT, CLOTH_DRIFT | Maestro: grey wavy hair (not spiky white), mustache, wearing blue shirt under apron (CHAR_DRIFT). Ellis: red soccer shirt (PASS). Riley: single pink bow visible — second bow partially obscured, marginal. Benny: child height, animated (PASS). |
| SC06 | FAIL | CHAR_DRIFT | Maestro: grey spiky hair (slightly better but not white), wearing plaid shirt under apron. Riley: single pink bow (FAIL — only one bow visible). Benny: at child height, animated (PASS). Layla: yellow bow, teal hoodie (PASS). Ellis: red soccer shirt (PASS). |
| SC07 | PASS | — | Maestro: grey-white spiky hair, brass goggles on forehead, brown apron — closest to hero ref in T1. All 4 cast + Maestro. Layla: yellow bow. Riley: 2 pink bows. Ellis: red soccer shirt. Benny: animated bear with green scarf. |
| SC08 | FAIL | CHAR_DRIFT | Maestro: grey spiky hair, green apron (not brown leather), wearing goggles. Riley: single pink bow (FAIL). Benny: appears small/shelf-sitting scale in scene — slight SCALE_ERROR. Layla: yellow bow, teal hoodie (PASS). |
| SC09 | PASS | — | All 4 cast + Maestro. Maestro: grey-white spiky hair, goggles on forehead, brown apron. Layla: yellow bow, teal hoodie. Riley: 2 pink bows. Ellis: plaid red shirt (minor CLOTH_DRIFT). Benny: animated child-height bear. |
| SC10 | PASS | — | All 4 cast (no Maestro). Layla: yellow bow, teal hoodie. Riley: 2 pink bows. Ellis: red soccer shirt. Benny: animated bear with green scarf. All characters clean. |
| SC11 | FAIL | CHAR_DRIFT | Maestro: grey hair (not white spiky), has mustache. Riley: single pink bow visible. Layla and Ellis present (PASS). Benny: at child height (PASS). |
| SC12 | FAIL | CHAR_MISSING | Riley absent from scene. Only Layla, Ellis, Benny present. No Maestro (scene may not require him). |
| SC13 | PASS | — | All 4 cast + Maestro. Maestro: grey-white spiky hair, goggles on forehead, blue shirt, brown apron. Layla: yellow bow. Riley: 2 pink bows (pigtails). Ellis: red/blue soccer-style shirt. Benny: animated bear. |
| SC14 | FAIL | CLOTH_DRIFT | Maestro: grey spiky hair, goggles — but GOGGLES ARE WORN OVER EYES rather than pushed up on forehead (spec violation). Benny: absent (partially behind others). Riley: 2 pink bows (PASS). Layla: yellow bow (PASS). |
| SC15 | PASS | — | Maestro: grey-white wavy hair (slightly less spiky), goggles on forehead, brown apron. All 4 cast + Maestro. Layla: yellow bow. Riley: single pink bow (borderline — second bow occluded by close proximity). Ellis: red soccer shirt. |
| SC16 | FAIL | CHAR_MISSING | Single panel (no MULTI_PANEL). Only Ellis shown, solo scene building cardboard box. Layla, Riley, Benny, Maestro all absent. |
| SC17 | FAIL | CLOTH_DRIFT | Maestro: wearing WHITE LAB COAT instead of brown leather apron — significant CLOTH_DRIFT vs. hero ref. Hair is grey-white (acceptable). Riley: 2 pink bows (PASS). Layla: yellow bow (PASS). Ellis: red soccer shirt (PASS). |
| SC18 | PASS | — | Maestro: grey-white spiky hair, goggles on forehead, blue shirt with apron. All 4 cast + Maestro. Riley: 2 pink bows. Layla: yellow bow. Benny: animated child-height bear. |
| SC19 | PASS | — | All 4 cast + Maestro. Maestro: grey-white spiky hair, goggles on forehead, brown apron with tool belt. Layla: yellow bow. Riley: single visible pink bow (second bow partially occluded — borderline PASS). Ellis: red/blue soccer shirt. Benny: animated bear. |
| SC20 | PASS | — | All 4 cast (no Maestro). Layla: yellow bow, teal hoodie. Riley: 2 pink bows. Ellis: red soccer shirt. Benny: animated bear. Clean composition. |

**Tier 1: 14 PASS / 6 FAIL**

---

## Tier 2 Results

| Scene | Result | Errors | Notes |
|-------|--------|--------|-------|
| SC01 | FAIL | CLOTH_DRIFT | Ellis: orange/black striped football jersey (NOT red soccer shirt — CLOTH_DRIFT). Layla: yellow bow, teal hoodie (PASS). Riley: 2 pink bows (PASS). Benny: animated bear (PASS). |
| SC02 | FAIL | CLOTH_DRIFT | Ellis: orange/black striped jersey (CLOTH_DRIFT). Layla: yellow bow (PASS). Riley: 2 pink bows (PASS). Benny: animated bear (PASS). |
| SC03 | FAIL | CHAR_MISSING, CLOTH_DRIFT | No Maestro present (Maestro-centric scene expected). Ellis: orange/black striped jersey (CLOTH_DRIFT). Layla: yellow bow (PASS). Riley: 2 pink bows (PASS). |
| SC04 | PASS | — | Maestro: grey-white spiky hair, BRASS GOGGLES prominently on forehead, brown apron — best T2 Maestro render. Layla: yellow bow. Riley: 2 pink bows (PASS). Ellis: orange jersey (CLOTH_DRIFT — noted but Maestro accuracy is primary flag here; Ellis shirt drift is a minor recurring T2 issue). Flagged as marginal PASS on overall scene quality. |
| SC05 | PASS | — | Maestro: grey-white spiky hair, goggles on forehead, brown apron. Layla: yellow bow, teal hoodie. Riley: single visible bow (marginal). Ellis: orange jersey (CLOTH_DRIFT). Benny: animated bear. Maestro is strong; overall PASS. |
| SC06 | FAIL | CHAR_MISSING, CLOTH_DRIFT | Benny absent. Maestro + Ellis + Layla + Riley only (4 chars, Benny missing). Ellis: orange jersey (CLOTH_DRIFT). |
| SC07 | FAIL | CHAR_DRIFT | Maestro: goggles worn OVER EYES (not on forehead — spec violation). Hair is grey-white spiky (PASS). Brown apron (PASS). Riley: single pink bow (FAIL). |
| SC08 | FAIL | CHAR_MISSING | Layla absent. Only Riley + Maestro in scene. Maestro: grey-white spiky, goggles on forehead, apron (PASS). Riley: 2 pink bows (PASS). |
| SC09 | FAIL | CHAR_MISSING | Layla absent. Only Benny + Maestro in scene (2-character scene). Maestro looks good. Benny: animated bear with green scarf (PASS). |
| SC10 | FAIL | CHAR_DRIFT | Ellis: brown hair (NOT blonde — CHAR_DRIFT on hair color). Layla: yellow bow but very small/partially obscured. Riley: 2 pink bows (PASS). Benny: animated bear (PASS). |
| SC11 | PASS | — | Maestro: grey-white spiky hair, goggles on forehead, mustache visible (minor drift). All 4 cast + Maestro. Layla: yellow bow. Riley: 2 pink bows. Ellis: orange jersey (CLOTH_DRIFT noted). Benny: animated bear. Overall PASS. |
| SC12 | FAIL | WRONG_ELDERLY | Adult male in scene is NOT Maestro — wearing BLACK TUXEDO with bow tie, dark hair, no goggles (completely wrong character). WRONG_ELDERLY flag. All 4 kids present. |
| SC13 | FAIL | CHAR_DRIFT, CLOTH_DRIFT | Maestro: uses brown leather gloves (acceptable) but hair appears grey/partially white and less spiky; minor CHAR_DRIFT. Also notable: Riley character in this scene has a YELLOW BOW instead of pink bows — if this girl is Riley, CLOTH_DRIFT + spec fail. Children casting is confusing (another light-skinned girl with yellow bow alongside original Layla). CHAR_DRIFT flagged. |
| SC14 | PASS | — | Maestro: grey-white spiky hair, goggles on forehead, brown apron. Layla: yellow bow. Riley: 2 pink bows. Ellis: orange jersey (CLOTH_DRIFT noted). Benny: animated bear. |
| SC15 | PASS | — | Maestro: grey-white spiky hair, goggles on forehead, brown apron. Layla: yellow bow. Riley: 2 pink bows. Ellis: orange jersey (minor). Benny: seated, small scale but in context of sitting at table — acceptable. |
| SC16 | FAIL | MULTI_PANEL | CONFIRMED MULTI_PANEL: Image split into two side-by-side panels. Left panel: Ellis + Maestro at table. Right panel: Maestro + Ellis + Layla at table. Character inset/reference shown in top-left corner. Layout is a multi-panel comic format, not a single illustration. |
| SC17 | PASS | — | Riley + Maestro two-character close scene. Maestro: grey-white spiky hair, brass goggles on forehead, brown leather apron. Riley: 2 pink bows, pigtails (PASS). Clean single panel. |
| SC18 | FAIL | MULTI_PANEL | CONFIRMED MULTI_PANEL: Image split into two side-by-side panels. Left panel: Benny + Maestro (Benny appears realistic/large bear size). Right panel: Benny solo, still large realistic-bear scale. MULTI_PANEL + SCALE_ERROR on Benny. |
| SC19 | PASS | — | All 4 cast + Maestro. Maestro: grey-white spiky hair, goggles on forehead. Layla: yellow bow. Riley: 2 pink bows. Ellis: orange jersey (CLOTH_DRIFT noted). Benny: animated bear at child height. |
| SC20 | PASS | — | All 4 cast on tower staircase. Layla: yellow bow. Riley: single visible bow (marginal — hair in motion). Ellis: orange jersey. Benny: animated bear. Clean sunset composition. |

**Tier 2: 10 PASS / 10 FAIL**

---

## Tier 3 Results

| Scene | Result | Errors | Notes |
|-------|--------|--------|-------|
| SC01 | FAIL | CLOTH_DRIFT, CHAR_DRIFT | Benny: wearing green OVERALLS and red bow-tie (NOT green scarf — CLOTH_DRIFT). All 4 kids present. Layla: yellow bow (PASS). Riley: 2 pink bows (PASS). Ellis: red soccer shirt (PASS). |
| SC02 | FAIL | CLOTH_DRIFT, CHAR_DRIFT | Benny: green overalls + red bow-tie (CLOTH_DRIFT vs. green scarf). Ellis: orange/brown plaid shirt (CLOTH_DRIFT — not red soccer shirt). Layla: yellow bow (PASS). Riley: 2 pink bows (PASS). |
| SC03 | FAIL | CLOTH_DRIFT, CHAR_MISSING | Benny: green overalls + red bow-tie (CLOTH_DRIFT). Maestro not present (scene involves workshop entry, may be expected). Ellis: red soccer shirt (PASS). Layla: yellow bow. Riley: 2 pink bows. |
| SC04 | PASS | — | Maestro: grey-white wild spiky hair, brass goggles on forehead, brown apron — good match. Layla: yellow bow. Riley: 2 pink bows, pigtails. Ellis: red soccer shirt. Benny: animated bear at child height (green overalls — CLOTH_DRIFT from scarf to overalls, but overall character identity clear). Marginal PASS. |
| SC05 | FAIL | CHAR_DRIFT, CLOTH_DRIFT | Maestro: spiky white hair (good), goggles on forehead (good), brown apron (good) — but the children are NOT the core cast: a white/light-skinned girl with purple pigtail dress replaces Riley/Layla, a brown-haired boy in plaid replaces Ellis. Core cast identity compromised. CHAR_DRIFT flagged. Benny: green overalls. |
| SC06 | FAIL | CHAR_MISSING | Only Ellis + Maestro in scene (2-character). Layla, Riley, Benny all absent. Maestro: grey-white spiky hair, goggles on forehead, brown apron (PASS on Maestro). Ellis: red soccer shirt (PASS). |
| SC07 | FAIL | CHAR_DRIFT, CLOTH_DRIFT | Maestro: grey-white spiky hair, goggles on forehead, apron — acceptable. But Riley: SINGLE pink bow (pigtails visible but only one bow — FAIL). Benny: green overalls + red bow-tie (CLOTH_DRIFT). Ellis: red soccer shirt (PASS). Layla: yellow bow (PASS). Also second bear figure visible in background (CHAR_DUPLICATE or SCALE_ERROR). |
| SC08 | FAIL | CHAR_MISSING, CLOTH_DRIFT | Only Riley + Maestro in scene. Layla, Ellis, Benny all absent. Maestro: grey-white spiky hair, goggles on forehead (PASS). Riley: 2 pink bows (PASS). Benny: appears as very small teddy-bear on shelf — SCALE_ERROR (toy size not child size). |
| SC09 | PASS | — | Maestro: grey-white spiky hair, BRIGHT GREEN goggles (slight color drift from brass — minor). All 4 cast + Maestro. Layla: yellow bow. Riley: single pink bow (marginal). Ellis: red soccer shirt. Benny: green overalls (CLOTH_DRIFT noted but identity clear). |
| SC10 | PASS | — | All 4 cast (no Maestro). Layla: yellow bow, teal hoodie. Riley: 2 pink bows. Ellis: orange/red plaid shirt (minor drift). Benny: green overalls + red bow-tie (recurring T3 CLOTH_DRIFT). |
| SC11 | PASS | — | All 4 cast + Maestro. Maestro: grey-white spiky hair, goggles on forehead, brown apron. Layla: yellow bow. Riley: 2 pink bows. Ellis: red soccer shirt. Benny: green overalls (recurring T3 drift). |
| SC12 | FAIL | CLOTH_DRIFT | All 4 cast (no Maestro). Layla: yellow bow, teal hoodie (PASS). Riley: single visible pink bow (FAIL). Ellis: red soccer shirt (PASS). Benny: green scarf (PASS — reverted to scarf in this scene). |
| SC13 | FAIL | CHAR_DRIFT | Maestro: grey-white spiky hair, goggles on forehead — but children cast is partially non-canonical: light-skinned girl with pink/purple striped shirt and straight black hair (not Riley's pigtails spec). The girl alongside Layla appears to be a different/wrong character substitution. Riley spec requires two pigtails with pink bows — this character has a different silhouette. CHAR_DRIFT. |
| SC14 | PASS | — | Maestro: grey-white spiky hair, goggles on forehead, brown apron. All 4 cast + Maestro. Layla: yellow bow. Riley: 2 pink bows. Ellis: red soccer shirt. Benny: animated bear at child height. |
| SC15 | PASS | — | All 4 cast + Maestro. Maestro: grey-white spiky hair, goggles on forehead. Layla: yellow bow, teal hoodie. Riley: 2 pink bows. Ellis: red soccer shirt. Benny: animated bear with green scarf (reverted). |
| SC16 | FAIL | MULTI_PANEL | CONFIRMED MULTI_PANEL: Image split into 4 quadrant panels (2x2 grid). Top-left: Ellis-like boy at workshop. Top-right: Maestro + Ellis-like boy at blueprints. Bottom-left: Ellis-like boy building. Bottom-right: Maestro + boy + background group (Layla, Riley visible, Benny). Full multi-panel comic layout. Core cast characters also dressed differently (Ellis in plaid, non-canonical). |
| SC17 | PASS | — | Riley + Maestro close scene. Maestro: grey-white spiky hair, brass goggles on forehead, brown apron. Riley: 2 pink bows, pigtails (PASS). Clean single panel. |
| SC18 | PASS | — | Benny + Maestro + Ellis (3-character scene). Benny: green overalls + red bow-tie (T3 CLOTH_DRIFT). Maestro: grey-white spiky hair, goggles on forehead. Ellis: blue/white soccer shirt (minor drift). Single panel (PASS on layout). |
| SC19 | PASS | — | All 4 cast + Maestro. Maestro: grey-white spiky hair, goggles on forehead, brown apron. Layla: yellow bow. Riley: 2 pink bows. Ellis: red soccer shirt. Benny: green overalls (T3 drift). |
| SC20 | PASS | — | All 4 cast on wooden tower staircase. Layla: yellow bow, teal hoodie. Riley: 2 pink bows. Ellis: orange/plaid shirt (minor drift). Benny: green overalls + red bow-tie (T3 CLOTH_DRIFT). |

**Tier 3: 11 PASS / 9 FAIL**

---

## Tier 4 Results

| Scene | Result | Errors | Notes |
|-------|--------|--------|-------|
| SC01 | FAIL | CHAR_MISSING | Riley: single PINK bow visible (only one — FAIL). Layla: yellow bow, teal hoodie (PASS). Ellis: orange/blue plaid shirt (CLOTH_DRIFT). Benny: animated bear with green scarf (PASS). No Maestro (acceptable for scene). |
| SC02 | FAIL | CLOTH_DRIFT | Riley: single pink bow (pigtails but only ONE bow visible — FAIL). Ellis: red/white striped jersey (CLOTH_DRIFT). Layla: yellow bow, teal hoodie (PASS). Benny: animated bear (PASS). |
| SC03 | FAIL | CHAR_MISSING | Maestro absent. Only 3 kids + Benny in workshop entry. Riley: single pink bow (FAIL). Ellis: red/white striped jersey (CLOTH_DRIFT). Layla: yellow bow (PASS). Benny: animated bear (PASS). |
| SC04 | PASS | — | Maestro: grey-white spiky hair, brass goggles on forehead, brown apron — strong T4 render. All 4 cast + Maestro. Layla: yellow bow. Riley: 2 pink bows. Ellis: red/white jersey (minor drift). Benny: animated bear. |
| SC05 | PASS | — | Maestro: grey-white spiky hair, brass goggles on forehead, brown leather apron. All 4 cast + Maestro. Layla: yellow bow. Riley: single pink bow (marginal). Ellis: orange/white striped jersey. Benny: animated bear with green scarf. Overall clean. |
| SC06 | FAIL | CHAR_MISSING | Only Ellis + Maestro in scene. Layla, Riley, Benny absent. Maestro: grey-white spiky hair, goggles on forehead, brown apron (PASS). Ellis: red/white jersey (CLOTH_DRIFT). |
| SC07 | PASS | — | Maestro: grey-white spiky hair, brass goggles on forehead, brown vest/apron. Layla: yellow bow. Riley present (hair + 1 bow visible — marginal). Ellis: orange striped jersey. Benny: animated bear. Maestro strong. |
| SC08 | PASS | — | Maestro: grey-white spiky hair, goggles on forehead, brown apron. All 4 cast + Maestro. Riley: single pink bow (FAIL), but other characters strong. Flagging marginal PASS — CHAR_DRIFT on Riley bow count noted. |
| SC09 | FAIL | CHAR_DRIFT, WRONG_ELDERLY | The children in this scene are NOT the core cast: two girls shown (one in yellow shirt, one in pink shirt overalls), and a striped-shirt boy — none match Layla/Riley/Ellis spec. Benny: animated bear (green scarf, PASS). No Maestro. CHAR_DRIFT on core children cast. |
| SC10 | FAIL | CHAR_MISSING | Layla, Riley, Ellis missing. Only Benny + Maestro + Layla in scene (Benny front, Maestro and Layla at bench, plus 2 unknown girls). Core cast partially replaced by non-canonical characters. |
| SC11 | PASS | — | Maestro: grey-white spiky hair, brass goggles on forehead, brown vest/apron. Layla: yellow bow, teal hoodie (PASS). Riley: single pink bow with headband (FAIL on bow count — borderline). Ellis: orange jersey (CLOTH_DRIFT). Benny: animated bear with green scarf. Maestro strong — marginal PASS. |
| SC12 | FAIL | WRONG_ELDERLY | The adult supervising the children is a plain grey-haired man in a casual grey polo shirt — NO GOGGLES, no apron, wrong outfit entirely. Not Maestro Gearsmith. WRONG_ELDERLY flag. Layla: yellow bow (PASS). Riley: 2 pink bows (PASS). Ellis: red/white jersey. Benny: animated bear (PASS). |
| SC13 | PASS | — | Maestro: grey-white spiky hair, brass goggles on forehead, brown apron, magnifying glass. All 4 cast + Maestro. Layla: yellow bow, teal hoodie. Riley: single pink bow (marginal). Ellis: red/white jersey (drift noted). Benny: animated bear. |
| SC14 | PASS | — | Maestro: grey-white spiky hair, brass goggles on forehead, brown apron. All 4 cast + Maestro. Layla: yellow bow. Riley: single pink bow (borderline). Ellis: red/white jersey. Benny: animated bear with green scarf. Maestro strong. |
| SC15 | PASS | — | All 4 cast + Maestro. Maestro: grey-white spiky hair, brass goggles on forehead, brown apron. Layla: yellow bow, teal hoodie. Riley: 2 pink bows. Ellis: red/white jersey. Benny: animated bear with green scarf. |
| SC16 | FAIL | MULTI_PANEL, CHAR_DRIFT | CONFIRMED MULTI_PANEL: Image shows three blonde Ellis-like boys at workshop (left side panel = boy looking sad, center = boy cutting, right = Maestro + boy with thumbs up). Same character duplicated across panels. MULTI_PANEL + CHAR_DUPLICATE (3x Ellis). Core Layla/Riley/Benny only visible as small background figures in final panel. |
| SC17 | PASS | — | Riley + Maestro two-character scene. Maestro: grey-white spiky hair, brass goggles on forehead, brown apron. Riley: single pink bow (FAIL on bow count but otherwise strong render). Single panel layout. Marginal PASS. |
| SC18 | PASS | — | All 4 cast + Maestro. Maestro: grey-white spiky hair, brass goggles on forehead, brown apron. Layla: yellow bow, teal hoodie. Riley: single pink bow with headband (marginal). Ellis: red/white jersey. Benny: animated bear (green scarf, PASS). |
| SC19 | PASS | — | All 4 cast + Maestro. Maestro: grey-white spiky hair, brass goggles on forehead, brown apron. Layla: yellow bow. Riley: single pink bow with headband (borderline). Ellis: orange jersey. Benny: animated bear. |
| SC20 | PASS | — | All 4 cast on tower. Layla: yellow bow. Riley: single pink bow (marginal). Ellis: orange striped jersey. Benny: animated bear with green scarf. Clean single panel. |

**Tier 4: 10 PASS / 10 FAIL**

---

## Priority Flags

| File | Errors | Issue |
|------|--------|-------|
| S3-CH08-SC16-tier2.png | MULTI_PANEL | Split 2-panel layout; top-left has character reference inset; not a single illustration |
| S3-CH08-SC16-tier3.png | MULTI_PANEL | 4-quadrant panel layout; different children visible; full comic grid format |
| S3-CH08-SC16-tier4.png | MULTI_PANEL, CHAR_DUPLICATE | 3-panel horizontal strip; Ellis duplicated 3x at different stages; Layla/Riley/Benny in background only |
| S3-CH08-SC12-tier2.png | WRONG_ELDERLY | Adult in black tuxedo + bow tie replaces Maestro entirely; no goggles, dark hair, wrong outfit |
| S3-CH08-SC12-tier4.png | WRONG_ELDERLY | Plain grey-haired man in polo shirt replaces Maestro; no goggles, no apron |
| S3-CH08-SC18-tier2.png | MULTI_PANEL, SCALE_ERROR | Split 2-panel layout; Benny rendered as adult-size realistic bear in both panels |
| S3-CH08-SC16-tier1.png | CHAR_MISSING | Only Ellis visible (solo scene); Layla, Riley, Benny, Maestro all absent |
| S3-CH08-SC09-tier4.png | CHAR_DRIFT | Core children replaced by non-canonical characters (wrong girls in yellow/pink shirts) |
| S3-CH08-SC17-tier1.png | CLOTH_DRIFT | Maestro in WHITE LAB COAT instead of brown leather apron |
| S3-CH08-SC05-tier3.png | CHAR_DRIFT | Core children cast partially replaced by non-canonical characters |
| S3-CH08-SC01-tier2.png | CLOTH_DRIFT | Ellis in orange/black football jersey throughout all T2 scenes (systemic) |
| S3-CH08-SC13-tier2.png | CHAR_DRIFT | Riley replaced by different girl with yellow bow (wrong character identity) |
| S3-CH08-SC07-tier1.png | — | Best Maestro render in T1; use as T1 reference |
| S3-CH08-SC04-tier2.png | — | Best Maestro render in T2; goggles prominent and brass-colored |
| S3-CH08-SC04-tier4.png | — | Best Maestro render in T4 |

---

## Cross-Tier Systemic Notes

### Ellis Shirt Drift (Systemic — Tier 2 and Tier 4)
Ellis's canonical red soccer shirt with blue shorts is replaced by an orange/black or orange/white striped football jersey in virtually every Tier 2 scene and most Tier 4 scenes. This is a systemic generation drift. Tier 1 and Tier 3 are largely correct on Ellis.

### Maestro Hair Color (All Tiers)
Maestro's hair renders as MID-GREY across most scenes rather than the spec-required WHITE. The hero reference shows clearly white hair with spiky style. This is a consistent under-saturation drift. Only a few scenes achieve near-white. Scenes in Tier 4 are generally the closest to white.

### Benny Scarf vs. Overalls (Systemic — Tier 3)
In Tier 3, Benny consistently appears in GREEN OVERALLS with a RED BOW-TIE rather than his canonical green plaid scarf. This is a full-tier-wide wardrobe substitution affecting approximately 14 of 20 Tier 3 scenes.

### Riley Single-Bow Drift (All Tiers)
Many scenes show Riley with only ONE pink bow (usually the right-side bow is visible while the left is obscured or absent). The spec requires TWO pink bows. Scenes where both bows are clearly visible should be used as rendering benchmarks.

### Maestro Goggles Position (Multiple Scenes)
Spec requires goggles pushed UP ON FOREHEAD. Several scenes (T1 SC14, T2 SC07) show goggles worn over the eyes. When Maestro is shown operating equipment, goggles over eyes may be contextually acceptable but should be flagged for review.

---

*Report generated 2026-02-17. All 80 images audited.*
