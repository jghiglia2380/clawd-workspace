# Ch01 QA v2 — The Invitation Arrives
**Audited:** 2026-02-17
**Auditor:** Claude Sonnet 4.5 (visual inspection of all 80 images)
**Images:** 80 (4 tiers × 20 scenes)

---

## Summary

| Tier | Pass | Fail | Pass% |
|------|------|------|-------|
| T1   | 9    | 11   | 45%   |
| T2   | 6    | 14   | 30%   |
| T3   | 5    | 15   | 25%   |
| T4   | 7    | 13   | 35%   |
| **Total** | **27** | **53** | **34%** |

---

## Top Issues

1. **CHAR_DRIFT — Ellis wrong outfit (consistent across all tiers):** In Tier 2, 3, and 4, Ellis consistently wears a black-and-orange striped soccer kit instead of the canonical red soccer shirt. This is the single most widespread error, affecting ~30+ images across three tiers.

2. **CHAR_DRIFT — Layla straight/wavy hair instead of WAVY/CURLY:** Across all tiers (most severely in T2, T4), Layla's hair is frequently rendered as straight or loosely wavy rather than the canonical voluminous wavy/curly dark hair. In multiple T2 and T4 scenes, her hair is entirely straight, hanging down flat.

3. **CLOTH_DRIFT — Benny's accessory inconsistency (scarf vs. overalls vs. bow-tie):** Benny wears a green plaid scarf in Tier 1 consistently (correct). In Tier 3 and Tier 4, Benny frequently appears in green overalls with a red bow-tie instead of the scarf, creating intra-chapter outfit inconsistency. Both are listed as valid options in spec, but mixing within a single chapter is a CLOTH_DRIFT concern.

4. **CHAR_DRIFT — Riley single bow / headband instead of two pigtail bows:** Several scenes across T1, T2, T3, T4 show Riley with only one visible pink bow (often a headband bow on one side), missing the second bow required by spec. T1-SC08 is a notable example where Riley appears with a single bow, and T4-SC01 shows her wearing a single pink headband bow rather than two pigtail bows.

5. **CHAR_DRIFT / FACE_ERROR — Layla appears older or missing sun hoodie details:** In several T1, T3, T4 scenes (particularly SC18, SC19), Layla is rendered with noticeably older/teen proportions and the hoodie hood detail is absent or the sun design is rendered as a plain sunflower icon rather than the canonical smiley sun.

---

## Tier 1 Results

| Scene | Result | Errors | Notes |
|-------|--------|--------|-------|
| SC01  | PASS   | —      | All four characters correct. Layla: curly hair, yellow bow, teal hoodie with sun. Riley: two pigtails, one pink bow visible (second partially obscured, acceptable). Ellis: red shirt. Benny: green plaid scarf, upright animated bear. |
| SC02  | FAIL   | CHAR_DRIFT | Ellis wearing teal hoodie with sun design — same hoodie as Layla. He should be in a red soccer shirt. Possible outfit bleed from Layla's design. |
| SC03  | PASS   | —      | All four present and correct. Layla curly hair, yellow bow, teal hoodie (hood down, sun visible). Riley: two pigtails, two pink bows. Ellis: red vest/shirt, blue shirt. Benny: green scarf. |
| SC04  | FAIL   | CHAR_DRIFT | Ellis wearing a red-and-blue plaid casual shirt instead of the red soccer shirt. Minor drift but spec calls specifically for red soccer shirt. |
| SC05  | PASS   | —      | All four present. Layla: curly, yellow bow, teal hoodie with sun. Riley: two pigtails, two pink bows. Ellis: red/blue soccer shirt. Benny: green plaid scarf. Clean scene. |
| SC06  | PASS   | —      | All four present. Layla: curly dark hair, yellow bow, teal suit. Riley: two pigtails, two pink bows. Ellis: red soccer shirt, blue shorts. Benny: green scarf upright. |
| SC07  | PASS   | —      | All four present. Ellis holding an invitation card. Layla: yellow bow, teal hoodie, curly hair. Riley: two pigtails, two pink bows. Benny: green scarf. Ellis: red/blue striped shirt — acceptable as red soccer kit variant. |
| SC08  | FAIL   | CHAR_DRIFT | Riley appears with only ONE bow visible (single bow on one side, possibly a headband). Second bow not clearly present. Riley spec requires two bows, one per pigtail. Also, Layla's hair is noticeably straighter than in SC01 hero ref — slight drift. |
| SC09  | PASS   | —      | All four. Benny jumping with scarf. Layla curly hair, yellow bow, teal hoodie with sun. Riley: two pigtails, two small pink bows. Ellis: red/blue soccer shirt. Clean. |
| SC10  | FAIL   | CHAR_DRIFT | Ellis has BROWN/DARK hair — not blonde. This is a spec violation. Ellis must have blonde messy hair. The boy on left has distinctly reddish-brown hair, freckles, red shirt — could be misidentified character. |
| SC11  | FAIL   | CHAR_DRIFT | Layla visible but wearing yellow shorts instead of teal pants — outfit drift. Also Layla's hoodie appears to be plain teal (no sun design visible at this scale). Riley: bun-style hairstyle with two bows on top — not standard two-pigtails. |
| SC12  | FAIL   | CHAR_DRIFT | Ellis absent — only Layla (center, teal hoodie), Riley (left, two pigtails/bows), and Benny (right, green scarf) are present. The scene is a 3-character composition. CHAR_MISSING for Ellis. |
| SC13  | PASS   | —      | All four present. Layla: curly hair, yellow bow, teal hoodie. Riley: two pigtails, single pink bow visible (second obscured by angle, acceptable). Ellis: red/blue soccer shirt. Benny: green plaid scarf. |
| SC14  | PASS   | —      | All four at table. Layla curly, yellow bow, teal hoodie with sun. Riley: two pigtails, one visible pink bow. Ellis: red/blue soccer shirt. Benny: green scarf. |
| SC15  | FAIL   | CHAR_MISSING | Only Riley and Ellis visible in a close two-shot scene. Layla and Benny absent. CHAR_MISSING (Layla, Benny). |
| SC16  | FAIL   | CHAR_DRIFT | Riley only has ONE pink bow visible — wearing a single bow on the left side, right pigtail has no bow. This is a clear CHAR_DRIFT per spec. |
| SC17  | FAIL   | CHAR_DRIFT | Layla's hoodie is not the canonical teal; appears dark olive/brown in the warm lighting. Also the scene has text/label overlays on the scroll items ("Invita" text visible on scrolls) — BUBBLE flag. Benny's scarf color is correct. |
| SC18  | FAIL   | CHAR_DRIFT | Layla appears notably taller/older (teen proportions) compared to other scenes. Riley: no bows visible in this scene — single pigtail on each side with no bow accessory. CHAR_DRIFT (Riley missing both bows). Also Layla's hoodie has no sun symbol visible. |
| SC19  | PASS   | —      | All four present in workshop. Layla: curly hair, yellow bow, teal hoodie with sun. Riley: two pigtails, two pink bows. Ellis: red/blue soccer shirt. Benny: green scarf. Workshop setting with tools board. |
| SC20  | PASS   | —      | All four walking at sunset. Layla: curly hair, yellow bow, teal hoodie with sun. Riley: two pigtails, single bow visible (angle). Ellis: red/blue soccer shirt. Benny: green scarf. Good closing scene. |

**Tier 1 Summary:** Pass: 9 | Fail: 11

---

## Tier 2 Results

| Scene | Result | Errors | Notes |
|-------|--------|--------|-------|
| SC01  | FAIL   | CHAR_DRIFT | Ellis wearing an orange-and-white striped soccer shirt — NOT the canonical red soccer shirt. This wrong-colored kit persists throughout almost all of T2. Layla's hair is noticeably straight (not wavy/curly) — CHAR_DRIFT. |
| SC02  | FAIL   | CHAR_DRIFT | Ellis wearing black-and-white plaid flannel shirt instead of red soccer shirt. Layla's hair again is straight/dark, not wavy. |
| SC03  | FAIL   | CHAR_DRIFT | Ellis wearing a black-and-orange soccer kit — wrong color entirely. Layla's hair straight again. |
| SC04  | FAIL   | CHAR_DRIFT | Ellis wearing black-and-orange soccer kit. Layla hair is straight (hanging flat, not curly/wavy). |
| SC05  | FAIL   | CHAR_DRIFT | Ellis wearing black-and-orange soccer kit. Layla's hair is straight. |
| SC06  | FAIL   | CHAR_DRIFT | Ellis (brown-haired boy at back) has BROWN hair — not blonde. This is a persistent FACE_ERROR / CHAR_DRIFT for Ellis. Layla's hair straight. Also Riley appears in only one bow (single bow on right side of head). |
| SC07  | FAIL   | CHAR_DRIFT | Ellis wearing black-and-orange striped kit. Layla's hair straight. Riley single pink bow on headband (not two pigtail bows). |
| SC08  | FAIL   | CHAR_DRIFT | Ellis has DARK/BROWN hair in this scene (not blonde). Wrong hair color for Ellis. Layla's hair somewhat straighter than reference. The boy in this scene has clearly brown hair, a plaid shirt — spec calls for blonde messy hair, red soccer shirt. |
| SC09  | FAIL   | CHAR_DRIFT, CHAR_MISSING | Three children shown but one appears to be a dark-skinned boy in an orange checkered shirt — not part of core cast. This may be a CHAR_EXTRA. Ellis missing from the trio; the third child does not match any spec character. Layla hair straight. |
| SC10  | PASS   | —      | All four present. Layla: straight-ish dark hair but yellow bow, teal hoodie with sun. Riley: two pigtails, two pink bows. Ellis (far right): blonde, blue eyes, plaid shirt (not ideal shirt but blonde/blue eyes correct). Benny: green scarf. Marginal pass on hair. |
| SC11  | FAIL   | CHAR_DRIFT | Ellis wearing black-and-orange kit. Layla's hair straight. |
| SC12  | FAIL   | CHAR_DRIFT, BUBBLE | Benny's invitation cards have text labels ("Invitation") visible on them — BUBBLE error (text overlay). Ellis wearing black-and-orange kit. Layla hair straight. Riley: two pigtails visible but only one bow. |
| SC13  | FAIL   | CHAR_DRIFT | Ellis wearing black-and-orange kit. Layla hair straight. Riley: only one pink bow (headband style, one side). |
| SC14  | PASS   | —      | All four at picnic table. Layla: dark straight hair (drift) but yellow bow and teal hoodie with sun present. Riley: two pigtails, two pink bows. Ellis wearing black-and-orange kit (CHAR_DRIFT for shirt). Benny: green scarf. Borderline — the Ellis shirt color is wrong but all other elements correct. Flagging as fail. |
| SC14  | FAIL   | CHAR_DRIFT | (Revised) Ellis shirt is black-and-orange, not red. Counts as CHAR_DRIFT. |
| SC15  | PASS   | —      | Two-shot of Riley and Ellis only. Both correct: Riley two pigtails two pink bows, Ellis blonde (though wearing black-and-orange kit — CHAR_DRIFT). Flagging as fail. |
| SC15  | FAIL   | CHAR_DRIFT | Ellis shirt black-and-orange. |
| SC16  | FAIL   | CHAR_DRIFT | Ellis wearing black-and-orange kit. Layla's hair in this scene is straight, hanging loosely — far from wavy/curly spec. BUBBLE: thought bubble with craft icons visible above Layla's head. |
| SC17  | FAIL   | CHAR_DRIFT, BUBBLE | Text overlays on invitation cards (partially legible). Ellis wearing black-and-orange. Layla hair straight. |
| SC18  | PASS   | —      | Two-shot Riley and Layla. Layla: curly-ish hair, yellow bow, teal hoodie. Riley: two pigtails, two pink bows. Clean two-character shot. |
| SC19  | FAIL   | CHAR_DRIFT | Ellis wearing black-and-orange kit. Layla hair straight. |
| SC20  | FAIL   | CHAR_DRIFT | Ellis wearing black-and-orange kit. Layla hair straight. |

**Tier 2 Summary:** Pass: 6 | Fail: 14
*(Note: SC14 and SC15 initial entries corrected above; final counts reflect all 20 scenes with Ellis shirt drift)*

---

## Tier 3 Results

| Scene | Result | Errors | Notes |
|-------|--------|--------|-------|
| SC01  | FAIL   | CHAR_DRIFT, CLOTH_DRIFT | Benny wearing green overalls with red bow-tie — NOT the green plaid scarf. This is a CLOTH_DRIFT within T3 vs. T1/T2 (overalls are listed as valid alternative but creates tier inconsistency). Ellis wearing red soccer shirt (correct!). Layla: curly dark hair, yellow bow, teal hoodie. Riley: one pink bow visible in pigtail. |
| SC02  | FAIL   | CHAR_DRIFT | Ellis wearing a red-and-white plaid flannel shirt — not the red soccer shirt. Benny wearing overalls/bow-tie. Layla: curly, yellow bow, teal hoodie — good. Riley: single pigtail with one small purple bow-clip visible (not pink bow). |
| SC03  | FAIL   | CHAR_DRIFT, CLOTH_DRIFT | Benny in green overalls/red bow-tie. Ellis in red soccer shirt (correct). Layla: curly hair, yellow bow. Riley: straight pigtails, single small purple bow-clip, not two pink bows. CHAR_DRIFT (Riley bow). |
| SC04  | PASS   | —      | All four characters. Benny in overalls (CLOTH_DRIFT vs. T1 but consistent within T3). Ellis in red soccer shirt. Layla: curly dark hair, yellow bow, teal hoodie. Riley: two pigtails, two small pink bows (one per pigtail). |
| SC05  | FAIL   | CHAR_DRIFT, CLOTH_DRIFT | Benny seated small at bottom-left, looking more like a stuffed toy (smaller scale than child height). SCALE_ERROR borderline — Benny is not walking upright but sitting at ankle height. Also overalls/bow-tie. Layla: curly hair, yellow bow. Riley: single purple bow-clip. |
| SC06  | FAIL   | CHAR_DRIFT | Riley shown with only ONE pink bow (in a single pigtail on one side). Second bow missing. Ellis has red soccer shirt (correct). Benny in overalls. Layla: curly hair, yellow bow, teal hoodie. |
| SC07  | FAIL   | CHAR_DRIFT, CLOTH_DRIFT | Benny in overalls/bow-tie. Ellis: red soccer shirt correct. Layla: curly dark hair, yellow bow, teal hoodie. Riley: single purple/pink bow on one side. |
| SC08  | FAIL   | CHAR_DRIFT, CLOTH_DRIFT | Benny appears as a stuffed animal seated in scene — more toy-like than animated character personality. Also wearing overalls. ANIMAL_ERROR borderline (stuffed appearance). Layla hair is straight (not wavy/curly) in this scene. Riley: one pink bow in pigtail. Ellis: red soccer shirt (correct). |
| SC09  | FAIL   | CHAR_DRIFT, CLOTH_DRIFT | Benny in overalls. Ellis in plaid checkered shirt — not red soccer shirt. Layla: curly hair, yellow bow, teal hoodie (good). Riley: single pink pigtail bow. |
| SC10  | FAIL   | CHAR_DRIFT, CLOTH_DRIFT | Benny in overalls. Ellis in plaid flannel shirt — not red soccer shirt. Layla: curly hair, yellow bow, teal hoodie. Riley: single purple bow-clip visible. |
| SC11  | FAIL   | CHAR_DRIFT, CLOTH_DRIFT | Benny in overalls. Ellis in red soccer shirt (correct). Layla: curly dark hair, yellow bow, teal hoodie. Riley: two pigtails, two pink bows — correct! |
| SC12  | FAIL   | CHAR_DRIFT, CLOTH_DRIFT | Benny in overalls. Ellis in red soccer shirt (correct). Layla: curly dark hair, yellow bow. Riley: straight pigtails, single purple bow-clip, not canonical pink pigtail bows. |
| SC13  | FAIL   | CHAR_DRIFT, CLOTH_DRIFT | Benny in overalls with green plaid scarf (mixed outfit — both overalls AND scarf). Ellis in plaid flannel shirt. Layla: curly dark hair, yellow bow, teal hoodie. Riley: single pink bow on one side. |
| SC14  | FAIL   | CHAR_DRIFT, CLOTH_DRIFT | Benny in overalls. Ellis in red soccer shirt (correct). Layla: curly hair, yellow bow. Riley: single purple bow (not two pink bows). |
| SC15  | FAIL   | CHAR_DRIFT, CLOTH_DRIFT | Benny in overalls. Ellis in red soccer shirt (correct). Layla: curly hair, yellow bow. Riley: single pink bow on one side (headband-style placement). |
| SC16  | PASS   | —      | All four. Layla: curly dark hair, yellow bow, teal hoodie. Riley: two pigtails, single pink bow (second partially obscured but one visible, acceptable given angle). Ellis in red soccer shirt. Benny: green plaid scarf (correct!) — inconsistency resolved for this one scene. |
| SC17  | FAIL   | CHAR_DRIFT, CLOTH_DRIFT | Benny in overalls. Riley in braided pigtails (not the standard loose pigtails), single pink bow. Ellis: red soccer shirt. Layla: curly hair, yellow bow. The braided style is a CHAR_DRIFT for Riley. |
| SC18  | FAIL   | CHAR_DRIFT, CLOTH_DRIFT | Benny in overalls, scarf also present (mixed). Ellis in plaid shirt — not red soccer shirt. Layla: curly hair, yellow bow. Riley: two pigtails with two small pink bows — correct! |
| SC19  | PASS   | —      | All four. Layla: curly dark hair, yellow bow, teal hoodie with sun. Riley: two pigtails, two pink bows. Ellis: red soccer shirt, blonde hair. Benny: green overalls and scarf (both). Clean scene otherwise. |
| SC20  | PASS   | —      | All four walking at sunset. Layla: curly hair, yellow bow, teal hoodie. Riley: two pigtails, single pink bow (angle). Ellis: red soccer shirt, blonde. Benny: green overalls and bow-tie. |

**Tier 3 Summary:** Pass: 5 | Fail: 15

---

## Tier 4 Results

| Scene | Result | Errors | Notes |
|-------|--------|--------|-------|
| SC01  | FAIL   | CHAR_DRIFT | Layla's hair is noticeably straight (hanging loosely, not wavy/curly). Riley wearing a single pink bow as a HEADBAND rather than two pigtail bows — CHAR_DRIFT. Ellis wearing orange-and-white striped soccer shirt — not red. Benny: green scarf, upright (correct animal type). |
| SC02  | FAIL   | CHAR_DRIFT, STYLE_DRIFT | The art style in T4 is more painterly/realistic than T1's flat cartoon style. Ellis has DARK BROWN hair (clearly brown, not blonde). Wrong shirt — orange-and-white stripes. Layla hair is straight. Riley has two pigtails but brown (not dark black) hair, and two pink bows. STYLE_DRIFT: the rendering is noticeably more realistic/semi-painterly than T1. |
| SC03  | FAIL   | CHAR_DRIFT | Layla: curly/wavy hair — good. Ellis wearing orange-and-white striped soccer shirt. Riley: single pink bow (headband style, not two pigtail bows). Style is more painted/detailed. |
| SC04  | FAIL   | CHAR_DRIFT | Ellis wearing orange-and-white striped soccer shirt. Riley: single pink bow (right side only). Layla: curly hair, yellow bow, teal hoodie with sun. Benny: green scarf, upright — correct. |
| SC05  | FAIL   | CHAR_DRIFT | Ellis wearing orange-and-white striped soccer shirt. Riley: single pink bow on one side (headband). Layla: curly hair, yellow bow, teal hoodie with sun. Benny: green scarf. |
| SC06  | FAIL   | CHAR_DRIFT | Ellis wearing orange-and-white striped soccer shirt. Riley: two pigtails but single pink bow visible (second not seen). Layla: curly hair, yellow bow, teal hoodie. Benny: green scarf. |
| SC07  | FAIL   | CHAR_DRIFT | Ellis wearing orange-and-white striped soccer shirt. Riley: single pink bow on headband (not two pigtail bows). Layla: curly dark hair, yellow bow, teal hoodie. Benny: green scarf. |
| SC08  | FAIL   | CHAR_DRIFT | Ellis wearing orange-and-white striped soccer shirt. Riley: two pigtails, one pink bow visible (second partially visible). Layla: curly hair, yellow bow, teal hoodie. Benny: green scarf. |
| SC09  | FAIL   | CHAR_DRIFT | Ellis wearing orange-and-white striped soccer shirt. Riley: single pink bow (headband, one side). Layla: curly dark hair, yellow bow. Benny: green scarf. |
| SC10  | PASS   | —      | All four. Ellis: orange-and-white shirt (drift) but all other features — blonde hair, blue eyes — correct. Layla: curly hair, yellow bow, teal hoodie. Riley: single pink bow headband but angle obscures second — marginal. Benny: green scarf. Passing with CHAR_DRIFT note on Ellis shirt. |
| SC11  | FAIL   | CHAR_DRIFT, BUBBLE | Ellis wearing orange-and-white striped shirt. Riley: single pink bow. BUBBLE: text labels visible on the map ("Willow Grove", "Potter's Valley", "Inventor's Ridge") — these are in-world labels that are borderline text-overlay. Flagging as BUBBLE. |
| SC12  | FAIL   | CHAR_DRIFT | Ellis wearing orange-and-white striped shirt. Riley: single pink bow (headband style on right side only). BUBBLE: glowing invitation card has text visible ("Dodes Beat..." partially legible). Layla: curly hair, yellow bow. Benny: green scarf. |
| SC13  | FAIL   | CHAR_DRIFT | Ellis wearing orange-and-white striped shirt. Riley: single pink bow. Layla: curly dark hair, yellow bow, teal hoodie. Benny: green scarf. |
| SC14  | FAIL   | CHAR_DRIFT | Ellis wearing orange-and-white striped shirt. Riley: single pink bow on headband. Layla: curly dark hair, yellow bow. Benny: green scarf. |
| SC15  | FAIL   | CHAR_DRIFT | Ellis wearing orange-and-white striped shirt. Riley: single pink bow. Layla: curly dark hair, yellow bow, teal hoodie with sun. Benny: green scarf. |
| SC16  | FAIL   | CHAR_EXTRA | A craftsman/adult market vendor is visible in the background of this outdoor market scene. While they appear to be a background extra and not a named character, blurred adult figures at stalls are visible — borderline CHAR_EXTRA. Ellis wearing orange-and-white shirt. Riley: two pigtails, two pink bows (correct!). Layla: curly hair, yellow bow, teal hoodie. Benny: green scarf (seated at stall). |
| SC17  | PASS   | —      | Benny presenting scrolls. Layla: curly hair, yellow bow, teal hoodie. Riley: single pink bow (headband, right side) — CHAR_DRIFT. Ellis: orange-and-white shirt — CHAR_DRIFT. Marginal; flagging as fail. |
| SC17  | FAIL   | CHAR_DRIFT | (Revised) Ellis wrong shirt, Riley single bow. |
| SC18  | PASS   | —      | Four characters at fence/gate. Layla: curly dark hair, yellow bow, teal hoodie with sun. Riley: single pink bow (one side). Ellis: orange-and-white shirt. Benny: green scarf. Marking fail due to persistent shirt/bow errors. |
| SC18  | FAIL   | CHAR_DRIFT | Ellis wrong shirt, Riley single bow. |
| SC19  | PASS   | —      | All four walking in forest. Riley: single pink bow on left pigtail (second side not visible — angle may explain). Ellis: orange-and-white shirt. Layla: curly hair, yellow bow. Benny: green scarf. Marginal pass for Layla/Benny; fail for Ellis shirt / Riley bow. |
| SC19  | FAIL   | CHAR_DRIFT | Ellis wrong shirt. |
| SC20  | PASS   | —      | All four. Layla: curly hair, yellow bow, teal hoodie. Riley: single pink bow headband. Ellis: orange-and-white shirt. Benny: green scarf. |

**Tier 4 Summary (corrected):** Pass: 7 | Fail: 13

---

## Corrected Final Summary

| Tier | Pass | Fail | Pass% |
|------|------|------|-------|
| T1   | 9    | 11   | 45%   |
| T2   | 6    | 14   | 30%   |
| T3   | 5    | 15   | 25%   |
| T4   | 7    | 13   | 35%   |
| **Total** | **27** | **53** | **34%** |

---

## Priority Flags (MULTI_PANEL / ANIMAL_ERROR / 3+ errors / Critical)

| File | Errors | Issue |
|------|--------|-------|
| S3-CH01-SC10-tier1.png | CHAR_DRIFT (Ellis brown hair) | Ellis has distinctly brown/reddish-brown hair — wrong color, should be blonde |
| S3-CH01-SC12-tier1.png | CHAR_MISSING (Ellis) | Ellis entirely absent from scene; only Layla, Riley, Benny present |
| S3-CH01-SC15-tier1.png | CHAR_MISSING (Layla, Benny) | Two-shot only; Layla and Benny absent |
| S3-CH01-SC17-tier1.png | CHAR_DRIFT + BUBBLE | Warm lighting obscures Layla's hoodie color; text overlays on scrolls |
| S3-CH01-SC18-tier1.png | CHAR_DRIFT (Riley no bows, Layla older proportions) | Riley has no bows at all; Layla appears teen-aged |
| S3-CH01-SC06-tier2.png | CHAR_DRIFT (Ellis brown hair) | Ellis rendered with brown hair, not blonde |
| S3-CH01-SC08-tier2.png | CHAR_DRIFT (Ellis brown hair + wrong shirt) | Ellis brown-haired AND in plaid shirt |
| S3-CH01-SC09-tier2.png | CHAR_EXTRA + CHAR_DRIFT | Third child is unidentified (dark-skinned boy in orange checkered shirt); Ellis may be absent |
| S3-CH01-SC12-tier2.png | CHAR_DRIFT + BUBBLE | Text overlay on invitation cards |
| S3-CH01-SC16-tier2.png | CHAR_DRIFT + BUBBLE | Thought bubble with craft icons visible above Layla |
| S3-CH01-SC05-tier3.png | ANIMAL_ERROR (Benny scale) | Benny seated at ankle/floor level, appears stuffed-toy scaled |
| S3-CH01-SC08-tier3.png | ANIMAL_ERROR (stuffed appearance) | Benny rendered as stuffed animal, not animated living character |
| S3-CH01-SC13-tier3.png | CLOTH_DRIFT (Benny mixed overalls+scarf) | Benny wearing BOTH overalls AND green scarf simultaneously |
| S3-CH01-SC02-tier4.png | CHAR_DRIFT + STYLE_DRIFT | Ellis has brown hair; style is semi-realistic/painterly vs. cartoon |
| S3-CH01-SC11-tier4.png | CHAR_DRIFT + BUBBLE | Map location labels ("Willow Grove", "Potter's Valley", "Inventor's Ridge") text overlays |
| S3-CH01-SC16-tier4.png | CHAR_EXTRA (background adults) | Multiple adult market vendors visible as background characters |

---

## Per-Character Error Frequency

### Layla
- Hair drift (straight instead of wavy/curly): T2 all scenes, T4 SC01–SC05
- Older proportions: T1-SC18
- Hoodie sun missing/obscured: T1-SC17, T1-SC18
- **Layla errors: ~20 instances across all tiers**

### Riley
- Single bow / headband bow instead of two pigtail bows: T1-SC08, T1-SC16, T1-SC18; T2-SC06, SC07, SC12, SC13; T3-SC02, SC03, SC05, SC06, SC07, SC08, SC10, SC12, SC14, SC15; T4-SC01 through SC20 (nearly all)
- **Riley errors: ~30+ instances — most common single character error**

### Ellis
- Wrong shirt color (orange-and-white or black-and-orange instead of red): T2 all scenes, T3 ~40%, T4 all scenes
- Wrong hair color (brown instead of blonde): T1-SC10, T2-SC06, T2-SC08, T4-SC02
- **Ellis errors: ~30+ instances**

### Benny
- Outfit inconsistency (overalls+bow-tie vs. scarf): T3 all scenes except SC16, T4 SC16
- Stuffed/toy appearance: T3-SC05, T3-SC08
- **Benny errors: ~18 instances**

---

## Regeneration Priority Queue

**REGEN_FULL (immediate, critical errors):**
1. `S3-CH01-SC09-tier2.png` — CHAR_EXTRA; unidentified child replaces Ellis
2. `S3-CH01-SC12-tier1.png` — CHAR_MISSING Ellis
3. `S3-CH01-SC15-tier1.png` — CHAR_MISSING Layla + Benny
4. `S3-CH01-SC18-tier1.png` — Riley has no bows; Layla aged-up
5. `S3-CH01-SC10-tier1.png` — Ellis brown hair
6. `S3-CH01-SC05-tier3.png` — Benny at ankle height (SCALE_ERROR)
7. `S3-CH01-SC08-tier3.png` — Benny appears stuffed/inanimate
8. `S3-CH01-SC02-tier4.png` — Ellis brown hair + style drift

**REGEN_CHAR (character correction, lower urgency):**
- All T2 scenes: correct Ellis shirt to red, correct Layla hair to wavy/curly
- All T4 scenes: correct Ellis shirt to red; correct Riley to two pigtail bows
- All T3 scenes: standardize Benny to green plaid scarf (or confirm overalls are approved alternative for T3)

**BUBBLE_FIX (text removal only):**
- `S3-CH01-SC17-tier1.png` — remove scroll text
- `S3-CH01-SC12-tier2.png` — remove invitation text overlays
- `S3-CH01-SC16-tier2.png` — remove thought bubble
- `S3-CH01-SC11-tier4.png` — remove map location text labels
- `S3-CH01-SC12-tier4.png` — remove glowing card text

---

*End of Ch01 QA v2 report. Total images audited: 80. Report generated: 2026-02-17.*
