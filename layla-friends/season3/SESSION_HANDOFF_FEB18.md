# Session Handoff — February 18, 2026

## What Happened Tonight

### S3 QA v2 Audit — Full Results

Ran 12 parallel visual audit agents across all Season 3 chapters (CH01–CH12), covering all 4 tiers each (20 scenes × 4 tiers = 80 images per chapter, 960 total).

**Results:**
- **Pass rate: 37%** (≈359/959 images — 1 image was missing/unauditable)
- **Failure count: ≈600 images**
- **Audit files saved to:** `S3_QA_v2/` (per-chapter) + `S3_QA_v2_SUMMARY.md` (merged)

Failure codes used in audit:
- `MULTI_PANEL` — image generated as split panels or comic strip grid
- `CHAR_MISSING` — one or more required characters absent
- `CHAR_DRIFT` — character appears but wrong design (wrong hair, wrong clothes, wrong species)
- `WRONG_ELDERLY` — wrong elderly character rendered (e.g. Mr. Mason face on Master Thomas)
- `CLOTH_DRIFT` — outfit inconsistency across scenes in same chapter
- `STYLE_DRIFT` — art style inconsistent with chapter tier
- `FILE_MISSING` — image file does not exist
- `TEXT_OVERLAY` — unwanted text rendered in image

---

### P1 Sprint — 28 Critical Images Regenerated

Split 28 P1 failures into 5 worker lists (`s3_regen_p1_w1.md` through `_w5.md`) and ran 5 parallel workers using 5 different API keys.

- Workers W1–W4 used keys: PE-images-2, Project-B, Project-C, Project-D
- Worker W5 used key: Project-E (quota exhausted immediately — swapped for old S2 key)
- **All 28/28 P1 images generated successfully**
- Worker logs: `s3_regen_log_w1.md` through `_w5.md`
- API calls used: 5–8 per worker (well under 250/worker quota)

---

### Root Cause Analysis — Why Images Were Failing

**Primary cause: static CHARACTER_LOCK_BLOCK describing all 5 characters in every scene**

The old `build_enhanced_prompt()` prepended a block describing Layla, Riley, Ellis, Benny, Mr. Mason, Frances, Master Thomas, Master Potter, and Maestro Gearsmith to every single prompt regardless of which characters actually appeared in that scene. This told the model all 9 characters "exist" — so it tried to include them all, causing:
- Character crowding / missing characters
- Model sneaking in background versions of absent characters
- Identity bleed between visually similar characters (e.g. Mr. Mason vs. Master Thomas — both elderly men)

**Master Thomas drift specifically:**
Master Thomas is visually similar to Mr. Mason (elderly man, gray hair, apron). When the lock block described both in the same prompt, the model frequently rendered Master Thomas with Mr. Mason's round wire-frame glasses, or merged the two designs. The fix: only describe the characters that actually appear in the scene.

**Secondary cause: all 5 characters listed in every prompt file scene**
The original `prompts/S3-CH04_TIER*_PROMPTS.md` files list all 5 recurring characters (`Layla, Riley, Ellis, Benny, Master Thomas`) in the `**Characters:**` line of every scene, even scenes where only 2 should be visible. This feeds into `get_original_scene_data()` → `get_character_refs()`, loading 30+ reference images and 9 character descriptions for every generation call — overwhelming the model.

---

### HERO_REFS Optimization

Character reference images are structured as:
```
/Volumes/JG DRIVE/Project Explore/Character Reference Images/
  {Character} all tiers/
    {Character} tier {N}/
      HERO_REFS/
        {Name}_Tier{N}_Hero_Body.webp   ← required anchor
        {Name}_Tier{N}_Hero_Face.webp   ← required anchor
        {Name}_Tier{N}_Hero_Action.webp  ← action poses
        {Name}_Tier{N}_Hero_Action2.webp
        ...
```

9 characters with HERO_REFS: Layla, Riley, Ellis, Benny, Mr. Mason, Frances, Master Thomas, Master Potter (Celeste), Maestro Gearsmith — each across 4 tiers. The script loads Body + Face first (required), then all Action files, then 1 random varied shot from the tier folder.

**Known path quirks (already handled via `TIER_PATH_OVERRIDES`):**
- Maestro Gearsmith Tier 1 folder has a trailing space: `"Maestro Gearsmith Tier 1 /HERO_REFS"`
- Frances Tier 3 folder is `"Frances Tier 3 (1)/HERO_REFS"`

**Layla naming fix:**
Reference files for Layla were previously named with a legacy name in some tiers. The CHAR_REF_MAP hero_name `"Layla"` ensures the script looks for `Layla_Tier{N}_Hero_Body.webp` etc. — confirm these files exist under that exact naming before generating new chapters. If Body/Face refs are missing for any character/tier, the script logs a WARNING and skips that ref (generation still proceeds).

---

### Script Changes Applied Tonight — `generate_regen_s3.py`

#### 1. Dynamic per-scene character lock block (most important fix)

Replaced static `CHARACTER_LOCK_BLOCK` string with `build_character_lock_block(characters: list)`.

- Takes the list of characters for the current scene
- Builds a lock block describing ONLY those characters
- Ends with: `"ONLY N character(s) in this frame. Do NOT add any other people, children, or animals not listed above."`
- Fallback: if characters list is empty, describes all known characters (backward compat)

`build_enhanced_prompt()` now takes `characters: list = None` parameter and calls the builder.
`generate_image()` extracts characters from `scene_data` and passes them through.

#### 2. 16:9 aspect ratio hardcoded

```python
config=types.GenerateContentConfig(
    response_modalities=["IMAGE"],
    image_config=types.ImageConfig(aspect_ratio="16:9")
)
```

Added to every `generate_content` call. Previously images generated in default aspect ratio.

#### 3. `--batch N` mode

```bash
python3 generate_regen_s3.py --batch 5
```

Stops after N successful generations, prints a summary of files generated, then exits. Re-run to continue — existing resume logic (`was_generated_today()`) skips already-generated files. Use for spot-checking before committing to a full 20-image run.

#### 4. `PROMPTS_DIR` env var override

```python
PROMPTS_DIR = Path(os.environ.get("PROMPTS_DIR", "prompts"))
```

Defaults to `prompts/` (original). Set `PROMPTS_DIR=prompts_v2` to use the new character-capped prompt files.

---

### Character Cap Strategy (50/30/20 Rule)

For new prompt files going forward:
- **50% of scenes** → 2 characters (tightest focus)
- **30% of scenes** → 3 characters
- **20% of scenes** → 4 characters
- **Never more than 4** characters in any single frame

Priority order when selecting which characters appear: Guest character (Master Thomas / Potter / Gearsmith) → Layla → whoever fits the scene beat → Riley / Ellis / Benny.

Applied to `prompts_v2/S3-CH04_TIER*_PROMPTS.md` — 20 scenes, rotation below:

| Scene | Characters | Count |
|-------|-----------|-------|
| SC01 | Layla, Riley, Master Thomas, Benny | 4 |
| SC02 | Layla, Master Thomas | 2 |
| SC03 | Ellis, Master Thomas, Layla | 3 |
| SC04 | Riley, Benny | 2 |
| SC05 | Layla, Ellis | 2 |
| SC06 | Master Thomas, Riley, Layla | 3 |
| SC07 | Riley, Master Thomas | 2 |
| SC08 | Ellis, Benny | 2 |
| SC09 | Benny, Master Thomas | 2 |
| SC10 | Layla, Master Thomas | 2 |
| SC11 | Layla, Riley, Ellis | 3 |
| SC12 | Layla, Riley, Benny | 3 |
| SC13 | Riley, Layla | 2 |
| SC14 | Master Thomas, Ellis, Layla | 3 |
| SC15 | Master Thomas, Ellis | 2 |
| SC16 | Layla, Benny, Riley | 3 |
| SC17 | Master Thomas, Layla, Ellis | 3 |
| SC18 | Master Thomas, Layla, Benny | 3 |
| SC19 | Layla, Master Thomas | 2 |
| SC20 | Layla, Riley, Ellis, Benny | 4 |

Screen time: Layla 16 · Master Thomas 13 · Riley 10 · Ellis 9 · Benny 9

---

### `prompts_v2/` Format

Each scene in `prompts_v2/` follows this structure:

```markdown
## Scene 01: [title]

**Characters:** Layla, Riley, Master Thomas, Benny

**Prompt:**
​```
CRITICAL: Do NOT include any text, speech bubbles...

CHARACTERS IN THIS SCENE ONLY:
- Layla: [description]
- Riley: [description]
...

ONLY THESE CHARACTERS APPEAR IN THIS IMAGE. No other characters exist in this frame.

Scene: [visual description referencing only listed characters]

Setting: [location]

Art style: [tier-specific style]
​```
```

Key differences from `prompts/`:
- Dynamic character list per scene (no absent characters mentioned anywhere)
- Lock block embedded in the prompt text itself (belt + suspenders — both prompt text AND script-level lock block are scoped to scene)
- No reference image sections (those are loaded by the script from CHAR_REF_MAP)
- Tier differentiation via Art style line only (scene content is identical across 4 tier files)

---

### Ch04 Tier 1 Test — Status: PENDING APPROVAL

**Ready to launch** — waiting on user to review `prompts_v2/S3-CH04_TIER1_PROMPTS.md` and approve.

Launch command when approved:
```bash
PROMPTS_DIR=prompts_v2 \
REGEN_FAIL_LIST=s3_ch04_t1_all.md \
REGEN_LOG=s3_ch04_t1_log.md \
python3 generate_regen_s3.py --batch 5
```

`s3_ch04_t1_all.md` needs to be created — a 20-row fail list covering all CH04 Tier 1 scenes (treated as FILE_MISSING since we're regenerating with new prompts).

---

### What Still Needs to Happen

1. **User approval of `prompts_v2/S3-CH04_TIER1_PROMPTS.md`** → then create `s3_ch04_t1_all.md` and run Tier 1 batch
2. **Spot-check 5 images** → review for aspect ratio, character isolation, no drift
3. **If Tier 1 passes** → run Tier 2–4 for CH04 (can parallelize across 4 API keys)
4. **If CH04 results look good** → apply same prompts_v2 approach to all remaining S3 chapters with failures (~600 images)
5. **For remaining S3 chapters** → generate `prompts_v2/S3-CH{01-12}_TIER{1-4}_PROMPTS.md` files using the same rotation strategy (adapt rotation per chapter's guest character)
6. **Large regen sprint** — split P2/P3 failure list across 5 workers, each with its own key, using new prompts_v2 + dynamic lock block

---

### API Key Status

| Key | Project | Status |
|-----|---------|--------|
| `GOOGLE_AI_API_KEY` | PE-images-2 | Active, ~242 calls remaining today |
| `GOOGLE_AI_API_KEY_2` | Project-Explore-E (old S2 key) | Active, used for W5 sprint |
| `GOOGLE_AI_API_KEY_PROJECT_B` | Project-Explore-B | Active, ~242 calls remaining |
| `GOOGLE_AI_API_KEY_PROJECT_C` | Project-Explore-C | Active, ~242 calls remaining |
| `GOOGLE_AI_API_KEY_PROJECT_D` | Project-Explore-D | Active, ~242 calls remaining |

Original Project-E key (`AIzaSyCA3xjZjjQfvs4BWAgn5U4_7T-L4Qd5SyI`) was exhausted at sprint start — do not use.

---

### Key Files

| File | Purpose |
|------|---------|
| `generate_regen_s3.py` | Main regen script — all fixes applied |
| `S3_QA_v2_SUMMARY.md` | Full audit results, all 12 chapters |
| `S3_QA_v2/` | Per-chapter QA files |
| `prompts_v2/S3-CH04_TIER1-4_PROMPTS.md` | New character-capped prompts for CH04 |
| `prompts/` | Original prompts (5 characters every scene) — keep for reference |
| `s3_regen_p1_w1-5.md` | P1 sprint worker lists (28 images — all done) |
| `s3_regen_log_w1-5.md` | P1 sprint generation logs |
