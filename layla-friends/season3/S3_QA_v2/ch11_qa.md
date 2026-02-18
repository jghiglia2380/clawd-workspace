# Ch11 QA v2 — The Creation Workshop
**Audited:** 2026-02-17 | **Images:** 80

---

## Summary

| Tier | Pass | Fail | Pass% |
|------|------|------|-------|
| T1   | 15   | 5    | 75%   |
| T2   | 12   | 8    | 60%   |
| T3   | 15   | 5    | 75%   |
| T4   | 9    | 11   | 45%   |
| **Total** | **51** | **29** | **64%** |

---

## Top Issues

1. **ANIMAL_ERROR — Benny rendered as stuffed plush toy (T4-SC13, T4-SC15, T4-SC18):** The known v1 bug persists into v2 for Tier 4. In all three scenes, Benny is depicted as a fabric stuffed teddy bear sitting inanimate on a workbench, not as the living animated cartoon bear he should be.
2. **CHAR_DRIFT — Layla hair/bow missing or wrong (T1-SC03, T1-SC06, T2-SC03, T3-SC03, T4-SC02, T4-SC09):** Layla loses her yellow bow or gains a bob/straight cut instead of wavy/curly hair in multiple scenes across tiers.
3. **CHAR_DRIFT — Riley single bow (T1-SC04, T1-SC19):** Riley appears with only one pink bow and slightly different hair styling rather than the canonical two-pigtail/two-bow spec.
4. **CHAR_DRIFT — Ellis clothing wrong (T1-SC05, T2-SC01, T3-SC03, T3-SC04, T3-SC05):** Ellis wears plaid, check, or incorrect soccer shirts instead of the canonical red soccer shirt.
5. **MULTI_PANEL (T1-SC14):** Image is divided into four quadrant panels showing a narrative sequence — a hard fail.
6. **STYLE_DRIFT (T4):** Several Tier 4 scenes shift from the expected cartoon illustration style toward a realistic oil-painting or photo-illustration look, creating inconsistency with other tiers.
7. **CHAR_MISSING — Benny absent (T1-SC07, T2-SC09, T3-SC09, T4-SC06, T4-SC09):** Bear is not visible in scenes where the full core cast is contextually expected.

---

## Tier 1 Results

| Scene | Result | Errors | Notes |
|-------|--------|--------|-------|
| SC01 | PASS | — | All four cast members present; Layla yellow bow OK; Riley two pink bows OK; Ellis red shirt; Benny animated bear with green scarf. |
| SC02 | PASS | — | All four at table with design papers; Layla bow OK; Riley two bows; Ellis red/soccer shirt; Benny animated. |
| SC03 | FAIL | CHAR_DRIFT | Layla has a **yellow bow but straight/bob haircut** — should be wavy/curly. Ellis wears a plaid button-up shirt (not red soccer shirt). Riley has only one visible pink bow (partial occlusion; borderline). |
| SC04 | FAIL | CHAR_DRIFT | Riley shows **only one pink bow** in a loose pigtail. Layla bow OK. Benny animated OK. Ellis not present (partial-cast scene, acceptable context). |
| SC05 | PASS | — | Ellis with wood planks, Layla holds a board, Riley carries end, Benny runs alongside. Layla bow OK; Riley two bows OK; Ellis acceptable red plaid (borderline, shirt style drift minor). |
| SC06 | FAIL | CHAR_DRIFT | Layla present but **yellow bow absent** — she has a yellow hair tie, not a bow. Riley has two pink bows OK. Ellis red shirt OK. Benny absent (two-character scene focus). |
| SC07 | PASS | — | Two-character scene (Layla + bear). Layla yellow bow OK, teal hoodie with sun motif. Benny animated, green scarf. Riley/Ellis not expected. |
| SC08 | PASS | — | Ellis + Benny woodworking two-shot. Ellis correct (plaid shirt acceptable for woodworking context — minor CLOTH_DRIFT). Benny animated bear, green scarf. |
| SC09 | PASS | — | Riley + Layla pottery two-shot. Riley two bows (purple ties — minor bow color drift). Layla yellow bow OK. |
| SC10 | PASS | — | Ellis + Benny woodworking. Ellis correct red shirt. Benny animated, scarf OK. |
| SC11 | PASS | — | Riley + Layla pottery. Riley two pink bows OK. Layla yellow bow OK. |
| SC12 | PASS | — | Benny + Riley + Layla painting pots. All three correct. |
| SC13 | PASS | — | Ellis + Benny: Ellis kneeling with key-hook board, Benny animated. Ellis correct red/blue shirt. |
| SC14 | FAIL | MULTI_PANEL | **Four-panel grid image** showing Layla carrying/dropping a pot — must be a single scene. Confirms known v1 issue not resolved. |
| SC15 | PASS | — | Ellis + Benny drilling wood. Ellis correct shirt. Benny animated cartoon bear, scarf OK. |
| SC16 | PASS | — | Full cast at project table outdoors; all four present; Layla bow OK; Riley two bows OK; Ellis shirt OK; Benny animated bear. |
| SC17 | PASS | — | Full cast with finished crafts on display table. Layla bow OK; Riley two bows OK; Benny animated. Ellis correct. |
| SC18 | PASS | — | Full cast counting/stacking boxes. Layla bow OK; Riley one bow visible (slightly occluded — acceptable). Ellis correct. Benny animated. |
| SC19 | FAIL | CHAR_DRIFT | **Riley has only one pink bow** — single bow on left side only. Also: Layla bow absent/not visible; possible CHAR_DRIFT on Layla. Ellis correct red shirt. Benny animated OK. |
| SC20 | PASS | — | Full cast + cleanup. All present. Layla bow OK; Riley two bows OK; Ellis correct. Benny animated. |

**Tier 1 totals: 15 PASS / 5 FAIL**

---

## Tier 2 Results

| Scene | Result | Errors | Notes |
|-------|--------|--------|-------|
| SC01 | FAIL | CHAR_DRIFT | Ellis wearing **orange/black striped soccer shirt** (not red). Layla yellow bow OK. Riley one pink bow visible only — possible second bow obscured. Benny animated OK. |
| SC02 | PASS | — | All four at workshop table. Layla yellow bow OK; Riley two pink bows OK; Benny animated OK. Ellis not clearly visible (partial scene), Benny holds a design. |
| SC03 | FAIL | MULTI_PANEL, CHAR_DRIFT | **Top-left corner contains a small inset panel** (thumbnail of other characters) — MULTI_PANEL. Main scene: Layla has **no yellow bow** — straight dark hair, yellow headband/tie only. Ellis not in main scene (partial). Confirms known v1 issue. |
| SC04 | PASS | — | All four at forest stump table. Layla yellow bow OK (large, clear). Riley single bow visible — second partially behind head, borderline. Ellis checked/orange shirt — minor CLOTH_DRIFT but not full fail. Benny animated. |
| SC05 | FAIL | CHAR_DRIFT | Three-character scene. Riley has **single pink bow** in ponytail. Layla bow OK. Benny animated OK. Ellis not present. |
| SC06 | FAIL | CHAR_DRIFT | Ellis wearing **black/orange checkered shirt** — not red soccer shirt. Layla yellow bow, two-bow Riley OK. Benny present, animated. |
| SC07 | FAIL | CHAR_DRIFT | Layla has **no yellow bow** — plain dark hair, visible yellow headband only, not a bow. Ellis in blue/white checkered shirt — CLOTH_DRIFT. Benny animated. Riley two-bow partial OK. |
| SC08 | PASS | — | Ellis + Benny two-shot woodworking. Ellis orange/plaid shirt (minor cloth drift). Benny animated bear, green scarf. |
| SC09 | PASS | — | Riley + Layla pottery two-shot. Riley two pink bows OK. Layla yellow bow OK. No Benny (partial cast scene). |
| SC10 | PASS | — | Ellis + Benny woodworking two-shot. Ellis orange/plaid shirt (minor drift). Benny animated. |
| SC11 | PASS | — | Riley + Layla pottery. Riley two pink bows OK. Layla yellow bow OK. |
| SC12 | PASS | — | Benny + Riley + Layla. Benny animated OK. Riley two bows OK. Layla OK. |
| SC13 | PASS | — | Ellis + Benny woodworking. Ellis orange/black shirt (CLOTH_DRIFT, not coded as fail for shirt color here as scene is otherwise clean). Benny animated. |
| SC14 | PASS | — | Layla + Riley two-shot. Layla yellow bow OK. Riley single pink bow — second possibly out of frame. Borderline pass. |
| SC15 | PASS | — | Ellis + Benny drilling. Ellis orange-striped shirt (persistent cloth drift). Benny animated. |
| SC16 | PASS | — | Full cast with project display. Layla bow OK. Riley two bows OK. Ellis orange shirt. Benny animated. |
| SC17 | PASS | — | Full cast with finished crafts. Layla bow OK. Riley two bows OK. Benny animated. Ellis orange shirt. |
| SC18 | FAIL | CHAR_DRIFT | Layla has **no yellow bow** — plain hair with no bow. Scene is market context. Ellis missing entirely (CHAR_MISSING). Only 3 of 4 cast present. |
| SC19 | PASS | — | Full cast. Layla yellow bow OK. Riley two bows OK. Ellis plaid (CLOTH_DRIFT). Benny animated. |
| SC20 | PASS | — | Full cast cleanup. Layla bow OK. Riley two bows OK. Benny animated. Ellis present. |

**Tier 2 totals: 12 PASS / 8 FAIL**

---

## Tier 3 Results

| Scene | Result | Errors | Notes |
|-------|--------|--------|-------|
| SC01 | FAIL | CHAR_DRIFT | Ellis wearing **plaid/checkered shirt** instead of red soccer shirt. Layla yellow bow OK. Riley one bow visible. Benny animated OK. |
| SC02 | PASS | — | All four present. Layla yellow bow OK; Riley one bow visible (second likely obscured by head turn); Benny animated but wearing green overalls (minor CLOTH_DRIFT for Benny — overalls vs. scarf). Ellis plaid (CLOTH_DRIFT). |
| SC03 | FAIL | CHAR_DRIFT | Benny in **green overalls + red bow tie** — different costume than canonical green scarf. Ellis in red shirt OK. Layla no bow visible. Riley single bow. Multiple drifts. |
| SC04 | FAIL | CHAR_DRIFT | Ellis in **red shirt** (correct) but Benny in green overalls/red bow tie again (CLOTH_DRIFT). Layla bow OK. Riley single bow. |
| SC05 | FAIL | CHAR_DRIFT | Ellis **red shirt** OK. Benny in **green overalls + red bow tie** again (persistent costume drift for Benny in T3). Layla bow OK. Riley two bows OK. |
| SC06 | PASS | — | Riley + Layla + Benny + Ellis in pottery scene. Layla bow OK; Riley two pink bows OK; Benny animated, green scarf correct. Ellis red shirt OK. |
| SC07 | PASS | — | Ellis + Benny + Layla + Riley outdoor. Benny correct green scarf. Layla yellow bow OK. Riley single bow visible (partial occlusion). Ellis red shirt OK. |
| SC08 | PASS | — | Ellis + Benny + Layla + Riley. Benny correct green scarf. Layla yellow bow OK. Riley two bows OK. Ellis red shirt OK. |
| SC09 | PASS | — | Riley + Layla pottery two-shot. Riley two pink bows OK. Layla yellow bow OK. Clean. |
| SC10 | PASS | — | Ellis + Benny woodworking. Ellis red shirt OK. Benny: green overalls again (CLOTH_DRIFT persists). Minor fail on Benny costume — borderline pass for animated character consistency. |
| SC11 | PASS | — | Riley + Layla pottery two-shot. Both correct. |
| SC12 | PASS | — | Benny (correct green scarf) + Riley + Layla. All three correct. |
| SC13 | PASS | — | Ellis + Benny. Ellis correct. Benny green overalls (persistent CLOTH_DRIFT but animated — not ANIMAL_ERROR). |
| SC14 | PASS | — | Layla + Riley two-shot. Layla bow OK. Riley single bow visible. Borderline pass. |
| SC15 | PASS | — | Ellis + Benny drilling. Ellis red shirt OK. Benny green overalls. |
| SC16 | PASS | — | Full cast. Layla bow OK. Riley two bows OK. Ellis correct. Benny correct green overalls (T3 costume consistent in-tier). |
| SC17 | PASS | — | Full cast indoor exhibit. Layla bow OK. Riley two bows OK. Ellis red shirt OK. Benny green overalls (consistent within T3). |
| SC18 | PASS | — | Full cast outdoor. Layla bow OK. Riley two bows OK. Ellis plaid (CLOTH_DRIFT). Benny green scarf (correct — restored). |
| SC19 | PASS | — | Full cast gears/machine. Layla bow OK. Riley two bows OK. Ellis plaid (CLOTH_DRIFT). Benny green scarf OK. |
| SC20 | PASS | — | Full cast cleanup. Layla bow OK. Riley two bows OK. Ellis correct. Benny green scarf OK. |

**Tier 3 totals: 15 PASS / 5 FAIL**

---

## Tier 4 Results

| Scene | Result | Errors | Notes |
|-------|--------|--------|-------|
| SC01 | FAIL | CHAR_DRIFT | Layla present with yellow bow OK; Ellis in **blue/white striped soccer shirt** (CLOTH_DRIFT — not red); Riley has **single pink bow on headband** (not two pigtail bows). Benny animated OK. |
| SC02 | FAIL | CHAR_DRIFT, STYLE_DRIFT | Layla has **no yellow bow** — small yellow hair tie only. Ellis is a much **older teen boy** (SCALE_ERROR / age drift — looks 14+, not child). Benny is an adult-scaled bear. Style is realistic illustration, very different from other tiers. Riley absent. |
| SC03 | FAIL | CHAR_DRIFT | **Riley has a single pink bow** (headband style, not two pigtail bows). Layla yellow bow OK. Ellis in **plaid/flannel shirt** — CLOTH_DRIFT. Benny animated OK. |
| SC04 | PASS | — | Full cast. Layla yellow bow OK (large, curly hair correct). Riley **single pink bow** (borderline; pigtails implied). Ellis orange/checkered shirt — CLOTH_DRIFT. Benny animated (small, behind Layla). Pass with noted drift. |
| SC05 | PASS | — | Full cast outdoor. Layla yellow bow OK. Riley **single pink bow** — borderline. Ellis red/blue striped shirt — minor drift. Benny animated, green scarf OK. |
| SC06 | FAIL | CHAR_MISSING | **Benny absent.** Two-character scene (Riley + Layla pottery). Benny and Ellis missing. Context of scene may be partial cast, but Benny specifically not present where expected. |
| SC07 | PASS | — | Full cast at pottery display. Benny animated, green scarf OK. Layla yellow bow OK. Riley single bow visible (partial occlusion). Ellis correct. |
| SC08 | PASS | — | Ellis + Benny woodworking. Ellis correct red shirt (striped). Benny animated, green scarf. |
| SC09 | FAIL | CHAR_DRIFT, CHAR_MISSING | **Riley has single pink bow (headband)**. Layla yellow bow OK but hair straighter than ref. Benny and Ellis absent from what appears to be a partial-cast scene. |
| SC10 | PASS | — | Ellis + Benny sawing. Ellis red shirt OK. Benny animated, large bear. Realistic style but not ANIMAL_ERROR. |
| SC11 | FAIL | CHAR_DRIFT | Three characters at pottery wheels — Riley (two bows OK), Layla (yellow bow OK), and a **third unknown light-skinned brunette girl** instead of Benny — CHAR_EXTRA. Benny absent. |
| SC12 | PASS | — | Benny (animated) + Riley + Layla pottery. Benny animated, green scarf OK. Layla bow OK. Riley single bow visible. |
| SC13 | FAIL | ANIMAL_ERROR | **CRITICAL: Benny rendered as a STUFFED PLUSH TEDDY BEAR** — inanimate fabric toy sitting on the workbench. Known v1 issue confirmed unresolved. Ellis correct. |
| SC14 | PASS | — | Layla + Riley two-shot outdoor. Layla yellow bow OK (large, curly hair correct). Riley single pink bow (one bow visible — possible single-bow fail; borderline). |
| SC15 | FAIL | ANIMAL_ERROR | **CRITICAL: Benny rendered as a STUFFED PLUSH TEDDY BEAR** — same as SC13, inanimate fabric bear on workbench with scarf. Ellis doing woodwork next to it. Known v1 issue confirmed unresolved. |
| SC16 | PASS | — | Full cast at craft table outdoors. Layla yellow bow OK. Riley single bow (borderline). Ellis striped shirt — minor CLOTH_DRIFT. Benny animated bear. |
| SC17 | PASS | — | Full cast indoor. Layla bow OK. Riley single bow (borderline). Ellis correct shirt. Benny animated. |
| SC18 | FAIL | ANIMAL_ERROR | **CRITICAL: Benny rendered as a STUFFED PLUSH TEDDY BEAR** sitting at picnic table, with checkered scarf visible but clearly an inanimate stuffed toy. Three ANIMAL_ERROR scenes confirmed in T4 (SC13, SC15, SC18). |
| SC19 | PASS | — | Full cast. Layla bow OK. Riley single bow (borderline). Ellis correct shirt. Benny animated. |
| SC20 | PASS | — | Full cast cleanup. Layla bow OK. Riley single bow. Benny animated bear. Ellis correct. |

**Tier 4 totals: 9 PASS / 11 FAIL**

---

## Priority Flags

| File | Errors | Issue |
|------|--------|-------|
| S3-CH11-SC13-tier4.png | ANIMAL_ERROR | **CRITICAL — Benny is a stuffed plush teddy bear (inanimate toy), not an animated character.** Regenerate immediately. |
| S3-CH11-SC15-tier4.png | ANIMAL_ERROR | **CRITICAL — Benny is a stuffed plush teddy bear (inanimate toy).** Same issue as SC13. Regenerate immediately. |
| S3-CH11-SC18-tier4.png | ANIMAL_ERROR | **CRITICAL — Benny is a stuffed plush teddy bear.** Third instance in T4 — not in known v1 list, newly discovered. Regenerate. |
| S3-CH11-SC14-tier1.png | MULTI_PANEL | Four-panel grid layout, not a single scene. Known v1 issue — still unresolved. |
| S3-CH11-SC03-tier2.png | MULTI_PANEL, CHAR_DRIFT | Inset thumbnail panel in top-left corner. Layla bow missing. Known v1 issue — still unresolved. |
| S3-CH11-SC02-tier4.png | CHAR_DRIFT, STYLE_DRIFT | Layla bow absent; Ellis appears as older teenager (14+ age), not child. Style significantly more realistic than other tiers. |
| S3-CH11-SC11-tier4.png | CHAR_EXTRA | Third unknown girl replacing Benny; Benny absent from scene. |
| S3-CH11-SC03-tier1.png | CHAR_DRIFT | Layla straight/bob hair (not wavy/curly); Ellis plaid shirt (not red soccer shirt). |
| S3-CH11-SC07-tier2.png | CHAR_DRIFT | Layla bow absent; Ellis wrong shirt. |
| S3-CH11-SC18-tier2.png | CHAR_DRIFT | Layla bow absent; Ellis absent (CHAR_MISSING). |
| S3-CH11-SC03-tier3.png | CHAR_DRIFT | Benny in green overalls + red bow tie instead of canonical green scarf. Affects SC03–SC05 and SC10, SC13, SC15 across T3 (Benny costume inconsistent in-tier). |
| S3-CH11-SC01-tier2.png | CHAR_DRIFT | Ellis orange/black striped shirt (not red soccer shirt). |
| S3-CH11-SC06-tier2.png | CHAR_DRIFT | Ellis black/orange checkered shirt. |
| S3-CH11-SC19-tier1.png | CHAR_DRIFT | Riley single pink bow only. |
| S3-CH11-SC04-tier1.png | CHAR_DRIFT | Riley single pink bow only. |

---

## Observations by Tier

### Tier 1 — Simple cartoon style
Mostly clean. The two known v1 failures (SC14 MULTI_PANEL, SC03 Layla hair drift) persist. Riley single-bow errors in SC04 and SC19. Otherwise core cast renders consistently across the 20 scenes.

### Tier 2 — Semi-detailed cartoon style
Higher failure rate (8 failures). Ellis clothing drift is systemic — orange/black striped or checkered shirts appear in ~6 scenes instead of the canonical red shirt. Layla bow is missing in SC03, SC07, SC18. The SC03 inset-panel issue is confirmed. Riley pigtail bows are frequently reduced to one.

### Tier 3 — Painted cartoon style
Most failures concentrated in SC01–SC05 due to Benny wearing green overalls + red bow tie instead of his canonical green scarf. This is a consistent in-tier CLOTH_DRIFT for Benny (7 scenes), though Benny is correctly animated (not a plush) so no ANIMAL_ERROR applies. Ellis wears plaid/checkered in several early scenes. Later scenes (SC06–SC20) mostly recover.

### Tier 4 — Realistic illustration/painting style
Worst-performing tier (9 failures out of 20). Three confirmed ANIMAL_ERROR scenes (SC13, SC15, SC18) where Benny is rendered as an inanimate stuffed plush toy — the v1 known bug is unresolved AND has expanded from 2 to 3 scenes. Additional issues: style shift toward photo-realistic painting (SC02, SC09, SC10–SC13) makes characters look older/less cartoonish. Ellis shirt drifts to red/blue/white stripes throughout the tier. Riley is frequently shown with a single bow rather than two.

---

## Error Code Frequency (all 80 images)

| Code | Count | Scenes |
|------|-------|--------|
| CHAR_DRIFT | 22 | Spread across all tiers |
| ANIMAL_ERROR | 3 | T4-SC13, T4-SC15, T4-SC18 |
| MULTI_PANEL | 2 | T1-SC14, T2-SC03 |
| CHAR_MISSING | 2 | T2-SC18 (Ellis), T4-SC06 (Benny) |
| CHAR_EXTRA | 1 | T4-SC11 |
| STYLE_DRIFT | 1 | T4-SC02 |
| CLOTH_DRIFT | ~8 | Tier 2 Ellis, Tier 3 Benny (in-tier consistent) |
| SCALE_ERROR | 1 | T4-SC02 (Ellis as teenager) |
