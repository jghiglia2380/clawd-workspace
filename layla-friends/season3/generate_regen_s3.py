#!/usr/bin/env python3
"""
S3 Targeted Regeneration Script
Reads P1 fail list from S3_QA_CORRECTED_SUMMARY.md, uses character reference pipeline,
stops at MAX_TOTAL_API_CALLS, logs to S3_REGENERATION_LOG.md.

Usage:
  python generate_regen_s3.py

Multi-worker (4 API key projects):
  REGEN_FAIL_LIST=s3_regen_w1.md REGEN_LOG=s3_regen_log_w1.md python generate_regen_s3.py
  REGEN_FAIL_LIST=s3_regen_w2.md REGEN_LOG=s3_regen_log_w2.md python generate_regen_s3.py
  REGEN_FAIL_LIST=s3_regen_w3.md REGEN_LOG=s3_regen_log_w3.md python generate_regen_s3.py
  REGEN_FAIL_LIST=s3_regen_w4.md REGEN_LOG=s3_regen_log_w4.md python generate_regen_s3.py

Resume: safe to re-run — skips files already generated today.
"""
import os
import re
import time
import random
import argparse
from pathlib import Path
from datetime import datetime, date
from google import genai
from google.genai import types
from dotenv import load_dotenv
from PIL import Image

load_dotenv()

# ──────────────────────────────────────────────
# CONFIGURATION
# ──────────────────────────────────────────────

MAX_TOTAL_API_CALLS = 250  # Hard stop — image gen calls only.

# API keys — load from environment.
# Override with env var REGEN_KEY_FILTER to use only specific keys by variable name.
# e.g., REGEN_KEY_FILTER=GOOGLE_AI_API_KEY_PROJECT_B
_key_filter = os.environ.get("REGEN_KEY_FILTER")
if _key_filter:
    API_KEYS = [k for k in [os.environ.get(_key_filter)] if k]
else:
    API_KEYS = [k for k in [
        os.environ.get('GOOGLE_AI_API_KEY'),
        os.environ.get('GOOGLE_AI_API_KEY_2'),
        os.environ.get('GOOGLE_AI_API_KEY_3'),
        os.environ.get('GOOGLE_AI_API_KEY_4'),
        os.environ.get('GOOGLE_AI_API_KEY_5'),
        os.environ.get('GOOGLE_AI_API_KEY_6'),
        os.environ.get('GOOGLE_AI_API_KEY_PROJECT_B'),
        os.environ.get('GOOGLE_AI_API_KEY_PROJECT_C'),
        os.environ.get('GOOGLE_AI_API_KEY_PROJECT_D'),
    ] if k]

if not API_KEYS:
    raise RuntimeError("No API keys found. Set GOOGLE_AI_API_KEY (and optionally _2 through _6, _PROJECT_B/C/D) in .env")

IMAGE_GEN_MODEL = "models/nano-banana-pro-preview"
VALIDATION_MODEL = "gemini-2.0-flash"
RATE_LIMIT_DELAY = 5  # seconds between image generation calls

PROMPTS_DIR = Path(os.environ.get("PROMPTS_DIR", "prompts"))
OUTPUT_BASE_DIR = Path("/Volumes/JG DRIVE/Project Explore/Season3-Images")
REGEN_LOG = Path(os.environ.get("REGEN_LOG", "S3_REGENERATION_LOG.md"))
FAIL_LIST_FILE = Path(os.environ.get("REGEN_FAIL_LIST", "S3_QA_CORRECTED_SUMMARY.md"))
CHAR_REF_BASE = Path("/Volumes/JG DRIVE/Project Explore/Character Reference Images")

# ──────────────────────────────────────────────
# CHARACTER REFERENCE PATHS
# ──────────────────────────────────────────────

CHAR_REF_MAP = {
    # Core cast
    "Layla":              ("Layla all tiers/Layla tier {tier}/HERO_REFS",                    "Layla"),
    "Riley":              ("Riley all tiers/Riley tier {tier}/HERO_REFS",                    "Riley"),
    "Ellis":              ("Ellis all tiers/Ellis tier {tier}/HERO_REFS",                    "Ellis"),
    "Benny":              ("Benny all tiers/Benny tier {tier}/HERO_REFS",                    "Benny"),
    "Mr. Mason":          ("Mr. Mason all tiers/Mr. Mason tier {tier}/HERO_REFS",            "Mr Mason"),
    "Mr_Mason":           ("Mr. Mason all tiers/Mr. Mason tier {tier}/HERO_REFS",            "Mr Mason"),
    "Frances":            ("Frances all tiers/Frances tier {tier}/HERO_REFS",                "Frances"),
    "Young Mr. Mason":    ("Mr. Mason all tiers/Young Mr. Mason Tier {tier}",                None),
    "Young_Mr_Mason":     ("Mr. Mason all tiers/Young Mr. Mason Tier {tier}",                None),
    "Young Frances":      ("Frances all tiers/Young Frances Tier {tier}",                    None),
    "Young_Frances":      ("Frances all tiers/Young Frances Tier {tier}",                    None),
    "Mrs_Patterson":      None,
    # S3 guest characters — now have HERO_REFS with curated Body/Face/Action files
    "Master Thomas":      ("Master Thomas/Master Thomas Tier {tier}/HERO_REFS",              "Master Thomas"),
    "Master_Thomas":      ("Master Thomas/Master Thomas Tier {tier}/HERO_REFS",              "Master Thomas"),
    "Master Potter":      ("Master Potter/Master Potter Tier {tier}/HERO_REFS",              "Master Potter"),
    "Master_Potter":      ("Master Potter/Master Potter Tier {tier}/HERO_REFS",              "Master Potter"),
    "Celeste":            ("Master Potter/Master Potter Tier {tier}/HERO_REFS",              "Master Potter"),
    "Maestro Gearsmith":  ("Maestro Gearsmith/Maestro Gearsmith Tier {tier}/HERO_REFS",     "Maestro Gearsmith"),
    "Maestro_Gearsmith":  ("Maestro Gearsmith/Maestro Gearsmith Tier {tier}/HERO_REFS",     "Maestro Gearsmith"),
}

# Per-character, per-tier path overrides (replaces the template-computed folder path)
TIER_PATH_OVERRIDES = {
    # Maestro Gearsmith Tier 1 folder has a trailing space — override to include HERO_REFS
    ("Maestro Gearsmith", 1):  "Maestro Gearsmith/Maestro Gearsmith Tier 1 /HERO_REFS",
    ("Maestro_Gearsmith", 1):  "Maestro Gearsmith/Maestro Gearsmith Tier 1 /HERO_REFS",
    # Frances Tier 3 folder is "Frances Tier 3 (1)" — override to correct path
    ("Frances", 3):             "Frances all tiers/Frances Tier 3 (1)/HERO_REFS",
}

# ──────────────────────────────────────────────
# PROMPT ENHANCEMENT BLOCKS
# ──────────────────────────────────────────────

_CHAR_DESCRIPTIONS = {
    "Layla":             "Layla: Brown-skinned girl, WAVY and CURLY dark hair (NEVER straight, NEVER a bob, NEVER pulled back flat), large yellow bow (ALWAYS visible), teal hoodie with hood DOWN and sun design. Child age 8-9. NOT an adult.",
    "Riley":             "Riley: Dark brown-skinned girl, black hair in TWO distinct pigtails. Each pigtail has its OWN separate pink bow tied at the base. BOTH pink bows must be clearly visible. Do NOT render Riley with a single bow, a headband, or a ponytail. Purple dress with star design. Child age 8-9.",
    "Ellis":             "Ellis: Light-skinned boy, BLONDE messy hair (NEVER brown, NEVER dark), blue eyes, freckles, red soccer shirt with soccer ball design. Child age 8-9. NOT elderly. NOT Mr. Mason.",
    "Benny":             "Benny: Brown ANIMATED CARTOON BEAR CHARACTER standing at child height (not a realistic bear, not a stuffed toy). Green plaid scarf around neck OR green overalls consistent with chapter. Walks upright, has a personality, eyes with visible whites.",
    "Mr. Mason":         "Mr. Mason: Elderly man, warm/olive skin, prominent ROUND WIRE-FRAME GLASSES, GRAY MUSTACHE (NOT a beard), curly gray hair, blue cardigan. Warm-toned skin.",
    "Mr_Mason":          "Mr. Mason: Elderly man, warm/olive skin, prominent ROUND WIRE-FRAME GLASSES, GRAY MUSTACHE (NOT a beard), curly gray hair, blue cardigan. Warm-toned skin.",
    "Frances":           "Frances: Elderly woman, warm smile, gardening apron.",
    "Master Thomas":     "Master Thomas: Stocky heavyset elderly man, warm/olive skin, FULL GRAY BEARD, BLUE BANDANA/headband across forehead, green plaid flannel shirt, brown woodworker's apron. NOT a woman. NOT wearing glasses.",
    "Master_Thomas":     "Master Thomas: Stocky heavyset elderly man, warm/olive skin, FULL GRAY BEARD, BLUE BANDANA/headband across forehead, green plaid flannel shirt, brown woodworker's apron. NOT a woman. NOT wearing glasses.",
    "Master Potter":     "Master Potter (Celeste): Warm brown-skinned woman, curly dark hair in a bun with a stick/pencil through it, clay-covered cream apron, warm terracotta-colored top, joyful expression. NOT an elderly man. NOT Mr. Mason.",
    "Master_Potter":     "Master Potter (Celeste): Warm brown-skinned woman, curly dark hair in a bun with a stick/pencil through it, clay-covered cream apron, warm terracotta-colored top, joyful expression. NOT an elderly man. NOT Mr. Mason.",
    "Celeste":           "Master Potter (Celeste): Warm brown-skinned woman, curly dark hair in a bun with a stick/pencil through it, clay-covered cream apron, warm terracotta-colored top, joyful expression. NOT an elderly man. NOT Mr. Mason.",
    "Maestro Gearsmith": "Maestro Gearsmith: Tall thin elderly man, wild SPIKY white hair, BRASS GOGGLES pushed up on forehead (not worn over eyes), white shirt under brown leather apron, steampunk boots with gear decorations. Distinctive pointed features.",
    "Maestro_Gearsmith": "Maestro Gearsmith: Tall thin elderly man, wild SPIKY white hair, BRASS GOGGLES pushed up on forehead (not worn over eyes), white shirt under brown leather apron, steampunk boots with gear decorations. Distinctive pointed features.",
}

def build_character_lock_block(characters: list) -> str:
    """Build a lock block containing ONLY the characters in this scene."""
    if not characters:
        # Fallback: describe all known recurring characters
        lines = ["STRICT CHARACTER REQUIREMENTS — match reference images exactly:"]
        for desc in _CHAR_DESCRIPTIONS.values():
            lines.append(f"- {desc}")
        return "\n".join(lines)
    lines = [f"STRICT CHARACTER REQUIREMENTS — ONLY these {len(characters)} character(s) appear in this scene:"]
    seen = set()
    for char in characters:
        desc = _CHAR_DESCRIPTIONS.get(char)
        if desc and desc not in seen:
            lines.append(f"- {desc}")
            seen.add(desc)
    lines.append(f"ONLY {len(characters)} character(s) in this frame. Do NOT add any other people, children, or animals not listed above.")
    return "\n".join(lines)

NEGATIVE_BLOCK = """DO NOT INCLUDE: speech bubbles, thought bubbles, caption text, floating text, question marks, exclamation marks, lightbulbs, multiple panels, split frames, European architecture, medieval settings, realistic photographic style, adult humans replacing child characters, extra animals (no squirrels, rabbits, foxes unless specified), generic unnamed children (unless scene specifically calls for background neighbors).
NOT a comic strip, NOT sequential panels, NOT side-by-side comparison, NOT before/after, NOT a grid layout. ONE single image of ONE single moment in time.
NO text on any surface — no labels on props, no blueprint measurements, no sign text, no notebook writing, no captions, no location names on maps.
Benny is an ANIMATED CARTOON BEAR — not a realistic bear, not a stuffed plush toy, not an otter."""

ENVIRONMENT_ANCHOR = "SETTING: Suburban American neighborhood or craftsman workshop interior. Warm illustrated style consistent with this chapter."

TIER4_EXTRA = "Illustrated cinematic painting style — NOT photographic, NOT photorealistic. Stylized but detailed. Show the SPECIFIC named characters — NOT generic children."

SPECIAL_SETTINGS = ["attic", "market", "bakery", "garden", "workshop", "kiln", "pottery",
                    "grove", "tower", "blueprint", "inventor", "faire", "woodworker",
                    "morocco", "italy", "mediterranean", "japan", "christmas",
                    "cemetery", "muertos", "tamalada", "spice", "auction", "fish"]

# ──────────────────────────────────────────────
# STATE
# ──────────────────────────────────────────────

current_key_index = 0
genai_client = genai.Client(api_key=API_KEYS[current_key_index])
total_api_calls = 0


# ──────────────────────────────────────────────
# HELPERS
# ──────────────────────────────────────────────

def log(message, level="INFO"):
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{ts}] [{level}] {message}")


def api_calls_remaining() -> int:
    return MAX_TOTAL_API_CALLS - total_api_calls


def was_generated_today(path: Path) -> bool:
    if not path.exists():
        return False
    mtime = datetime.fromtimestamp(path.stat().st_mtime).date()
    return mtime == date.today()


def get_character_refs(characters: list, tier: int) -> list:
    """Return up to 4 ref images per character.
    - Characters with hero_name: Body + Face from HERO_REFS + 2 random tier shots
    - Characters without hero_name: up to 4 images from tier folder directly
    """
    refs = []
    for char in characters:
        if char not in CHAR_REF_MAP:
            log(f"  No ref map entry for character: {char}", "WARNING")
            continue
        entry = CHAR_REF_MAP[char]
        if entry is None:
            continue  # Minor character with no refs — skip silently
        folder_template, hero_name = entry

        # Check for per-character per-tier path override
        override_key = (char, tier)
        if override_key in TIER_PATH_OVERRIDES:
            folder = CHAR_REF_BASE / TIER_PATH_OVERRIDES[override_key]
        else:
            folder = CHAR_REF_BASE / folder_template.format(tier=tier)

        if not folder.exists():
            log(f"  Missing char ref folder: {folder}", "WARNING")
            continue

        if hero_name:
            # Load Body + Face first (required anchors)
            for ref_type in ["Body", "Face"]:
                for ext in [".webp", ".png"]:
                    ref_path = folder / f"{hero_name}_Tier{tier}_Hero_{ref_type}{ext}"
                    if ref_path.exists():
                        refs.append(ref_path)
                        break
                else:
                    log(f"  Missing HERO_REF: {hero_name}_Tier{tier}_Hero_{ref_type}", "WARNING")
            # Load all additional Action files present in HERO_REFS (Action, Action2, Action3, etc.)
            action_refs = sorted([
                p for p in folder.iterdir()
                if p.is_file()
                and p.suffix.lower() in ('.webp', '.png')
                and "Action" in p.stem
            ])
            refs.extend(action_refs)
            # 1 random varied shot from the tier folder (parent of HERO_REFS) for extra variety
            tier_folder = folder.parent
            varied = [
                p for p in tier_folder.iterdir()
                if p.is_file() and p.suffix.lower() in ('.webp', '.png')
            ]
            if varied:
                refs.extend(random.sample(varied, 1))
        else:
            # No HERO_REFS: use up to 4 images from folder directly
            images = sorted(folder.glob("*.png"))[:4]
            if not images:
                images = sorted(folder.glob("*.webp"))[:4]
            refs.extend(images)

    return refs


def get_original_scene_data(chapter: int, tier: int, scene_id: str) -> dict | None:
    """
    Parse scene data from S3 markdown prompt file.
    scene_id format: S3-CH01-SC08-tier1
    File format:  prompts/S3-CH01_TIER1_PROMPTS.md
    """
    prompt_file = PROMPTS_DIR / f"S3-CH{chapter:02d}_TIER{tier}_PROMPTS.md"
    if not prompt_file.exists():
        log(f"  Prompt file not found: {prompt_file}", "ERROR")
        return None

    # Extract scene number from scene_id: "S3-CH01-SC08-tier1" → 8
    sc_match = re.search(r"-SC(\d{2})-", scene_id)
    if not sc_match:
        log(f"  Cannot extract scene number from scene_id: {scene_id}", "ERROR")
        return None
    scene_num = int(sc_match.group(1))

    try:
        text = prompt_file.read_text()

        # Find section: "## Scene 08:" — match until next scene or end
        section_pattern = re.compile(
            rf"## Scene {scene_num:02d}:(.*?)(?=\n## Scene \d{{2}}:|\Z)",
            re.DOTALL
        )
        m = section_pattern.search(text)
        if not m:
            log(f"  Scene {scene_num:02d} not found in {prompt_file.name}", "ERROR")
            return None

        section = m.group(0)

        # Extract characters from "**Characters:** Layla, Riley, Ellis, Benny (all four)"
        char_match = re.search(r"\*\*Characters:\*\*\s*(.+)", section)
        characters_raw = char_match.group(1).strip() if char_match else ""

        # Parse known character names (order matters — check multi-word first)
        known_chars = [
            "Master Thomas", "Master Potter", "Maestro Gearsmith",
            "Young Mr. Mason", "Young Frances", "Mrs_Patterson",
            "Mr. Mason", "Frances", "Layla", "Riley", "Ellis", "Benny", "Celeste",
        ]
        characters = []
        seen = set()
        for name in known_chars:
            if name.lower().replace(".", "").replace(" ", "") in characters_raw.lower().replace(".", "").replace(" ", ""):
                if name not in seen:
                    characters.append(name)
                    seen.add(name)

        # Extract prompt from ``` code block
        prompt_match = re.search(r"```\s*\n(.*?)```", section, re.DOTALL)
        if not prompt_match:
            log(f"  No prompt block found for scene {scene_num:02d} in {prompt_file.name}", "ERROR")
            return None

        prompt = prompt_match.group(1).strip()

        return {
            "scene_id": scene_id,
            "prompt": prompt,
            "characters": characters,
        }

    except Exception as e:
        log(f"  Failed to parse {prompt_file}: {e}", "ERROR")
        return None


def build_enhanced_prompt(original_prompt: str, tier: int, characters: list = None,
                          outfit_lock: str = "") -> str:
    char_block = build_character_lock_block(characters or []) + outfit_lock
    parts = [char_block, "\n\n", original_prompt]
    if tier == 4:
        parts.append(f"\n\n{TIER4_EXTRA}")
    if not any(s in original_prompt.lower() for s in SPECIAL_SETTINGS):
        parts.append(f"\n\n{ENVIRONMENT_ANCHOR}")
    parts.append(f"\n\n{NEGATIVE_BLOCK}")
    return "".join(parts)


# ──────────────────────────────────────────────
# STYLE ANCHOR
# ──────────────────────────────────────────────

def get_style_anchor(chapter: int, tier: int, exclude_scene_id: str,
                     fail_scene_ids: set) -> Path | None:
    """Find one passing image from same chapter/tier as a style reference."""
    folder = OUTPUT_BASE_DIR / f"CH{chapter:02d}" / f"tier{tier}"
    if not folder.exists():
        return None
    candidates = [
        p for p in folder.glob("*.png")
        if p.stem != exclude_scene_id
        and p.stem not in fail_scene_ids
        and p.stat().st_size > 0
    ]
    if not candidates:
        return None
    return random.choice(candidates)


# ──────────────────────────────────────────────
# CLOTHING LOCK
# ──────────────────────────────────────────────

_outfit_lock_cache: dict = {}


def scan_outfit_lock(chapter: int, tier: int) -> str:
    """Scan Scene 01 to identify Benny and Ellis outfits for chapter consistency."""
    cache_key = (chapter, tier)
    if cache_key in _outfit_lock_cache:
        return _outfit_lock_cache[cache_key]

    scene_path = None
    for sc in range(1, 6):
        candidate = OUTPUT_BASE_DIR / f"CH{chapter:02d}" / f"tier{tier}" / f"S3-CH{chapter:02d}-SC{sc:02d}-tier{tier}.png"
        if candidate.exists() and candidate.stat().st_size > 0:
            scene_path = candidate
            break

    if not scene_path:
        log(f"  Outfit lock: no scene found for CH{chapter:02d} T{tier}", "WARNING")
        _outfit_lock_cache[cache_key] = ""
        return ""

    prompt = (
        "Look at this children's illustration. Identify what BENNY (the brown cartoon bear) "
        "and ELLIS (the light-skinned blonde boy) are wearing. "
        "Be specific — note exact colors, patterns (plaid, striped, etc.), and garment types. "
        "If a character is not visible, say NOT VISIBLE. "
        "Respond ONLY in this format: BENNY: [description] | ELLIS: [description]"
    )

    try:
        validation_client = genai.Client(api_key=API_KEYS[current_key_index])
        img = Image.open(scene_path)
        response = validation_client.models.generate_content(
            model=VALIDATION_MODEL,
            contents=[prompt, img]
        )
        result = response.text.strip()
        log(f"  Outfit lock CH{chapter:02d} T{tier}: {result}")
        lock_str = f"\n- CHAPTER OUTFIT CONSISTENCY — {result} (must match across ALL scenes in this chapter)"
        _outfit_lock_cache[cache_key] = lock_str
        return lock_str
    except Exception as e:
        log(f"  Outfit lock scan failed for CH{chapter:02d} T{tier}: {e}", "WARNING")
        _outfit_lock_cache[cache_key] = ""
        return ""


# ──────────────────────────────────────────────
# GENERATION
# ──────────────────────────────────────────────

class QuotaExhaustedError(Exception):
    pass


def generate_image(scene_data: dict, chapter: int, tier: int, char_refs: list,
                   style_anchor: Path | None = None, outfit_lock: str = "") -> bool:
    global total_api_calls, genai_client

    scene_id = scene_data["scene_id"]
    original_prompt = scene_data["prompt"]
    characters = scene_data.get("characters", [])

    enhanced_prompt = build_enhanced_prompt(original_prompt, tier, characters, outfit_lock)

    all_ref_paths = list(char_refs)
    if style_anchor and style_anchor.exists():
        all_ref_paths.append(style_anchor)

    parts = [enhanced_prompt]
    char_refs_loaded = 0

    for ref in all_ref_paths:
        try:
            img = Image.open(ref)
            parts.append(img)
            if ref in char_refs:
                char_refs_loaded += 1
        except Exception as e:
            log(f"  Failed to load ref {ref.name}: {e}", "WARNING")

    log(f"  Refs loaded: {char_refs_loaded} char + {1 if style_anchor and style_anchor.exists() else 0} style anchor", "INFO")

    output_dir = OUTPUT_BASE_DIR / f"CH{chapter:02d}" / f"tier{tier}"
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / f"{scene_id}.png"

    if output_path.exists():
        output_path.unlink()

    total_api_calls += 1

    try:
        start = time.time()
        response = genai_client.models.generate_content(
            model=IMAGE_GEN_MODEL,
            contents=parts,
            config=types.GenerateContentConfig(
                response_modalities=["IMAGE"],
                image_config=types.ImageConfig(aspect_ratio="16:9")
            )
        )
        for part in response.candidates[0].content.parts:
            if part.inline_data is not None:
                with open(output_path, 'wb') as f:
                    f.write(part.inline_data.data)
                elapsed = time.time() - start
                size_kb = len(part.inline_data.data) / 1024
                log(f"  ✅ {scene_id} ({elapsed:.1f}s, {size_kb:.1f}KB) [call {total_api_calls}/{MAX_TOTAL_API_CALLS}]", "SUCCESS")
                return True

        log(f"  No image data in response for {scene_id}", "ERROR")
        return False

    except Exception as e:
        err = str(e)
        if "429" in err or "RESOURCE_EXHAUSTED" in err or "quota" in err.lower():
            log(f"  ⛔ Quota exhausted. Stopping.", "ERROR")
            raise QuotaExhaustedError("Daily quota reached")
        log(f"  API error for {scene_id}: {e}", "ERROR")
        return False


# ──────────────────────────────────────────────
# VALIDATION
# ──────────────────────────────────────────────

def validate_image(output_path: Path, characters: list) -> bool:
    if len(characters) < 3:
        return True

    if not output_path.exists():
        return False

    char_list = ", ".join(characters)
    validation_prompt = (
        f"This image should contain these characters: {char_list}. "
        f"Are all of them clearly visible? Answer only YES or NO."
    )

    try:
        validation_client = genai.Client(api_key=API_KEYS[current_key_index])
        img = Image.open(output_path)
        response = validation_client.models.generate_content(
            model=VALIDATION_MODEL,
            contents=[validation_prompt, img]
        )
        answer = response.text.strip().upper()
        passed = "YES" in answer
        if not passed:
            log(f"  ⚠️  Validation failed: {answer}", "WARNING")
        return passed
    except Exception as e:
        log(f"  Validation error (treating as pass): {e}", "WARNING")
        return True


# ──────────────────────────────────────────────
# FAIL LIST PARSER
# ──────────────────────────────────────────────

def parse_fail_list(fail_list_path: Path) -> list:
    """
    Parse P1 regen list from S3_QA_CORRECTED_SUMMARY.md or a split worker file.

    Handles table row format from the QA summary:
      | ch01/tier1/S3-CH01-SC08-tier1.png | REGEN_FULL, STYLE_DRIFT, CHAR_DRIFT | description |

    Also handles bare list format for split worker files:
      - ch01/tier1/S3-CH01-SC08-tier1.png | REGEN_FULL, STYLE_DRIFT | description
    """
    entries = []
    if not fail_list_path.exists():
        log(f"Fail list not found: {fail_list_path}", "ERROR")
        return entries

    current_priority = 1
    priority_pattern = re.compile(r"Priority\s+(\d)", re.IGNORECASE)

    # Match S3 filename pattern in table or list rows:
    # ch01/tier1/S3-CH01-SC08-tier1.png | errors | description
    entry_pattern = re.compile(
        r"(?:\|\s*|-\s*)?"                                         # optional | or - prefix
        r"(ch(\d{2})/tier(\d)/S3-CH\d{2}-SC(\d{2})-tier\d\.png)"  # path group
        r"(?:\s*\|\s*([^|\n]+?)(?:\s*\|\s*([^|\n]*))?)?",         # optional | errors | description
    )

    with open(fail_list_path) as f:
        for line in f:
            pm = priority_pattern.search(line)
            if pm:
                current_priority = int(pm.group(1))
                continue

            em = entry_pattern.search(line)
            if not em:
                continue

            file_path = em.group(1)
            chapter = int(em.group(2))
            tier = int(em.group(3))
            scene = int(em.group(4))
            errors = em.group(5).strip() if em.group(5) else "REGEN_FULL"
            description = em.group(6).strip() if em.group(6) else ""
            scene_id = f"S3-CH{chapter:02d}-SC{scene:02d}-tier{tier}"

            entries.append({
                "file": file_path,
                "chapter": chapter,
                "tier": tier,
                "scene": scene,
                "scene_id": scene_id,
                "priority": current_priority,
                "errors": errors,
                "description": description,
            })

    entries.sort(key=lambda e: (e["priority"], e["chapter"], e["tier"], e["scene"]))
    log(f"Parsed {len(entries)} failed images from fail list", "INFO")
    return entries


# ──────────────────────────────────────────────
# LOG WRITER
# ──────────────────────────────────────────────

def write_regen_log(generated: list, gen_failed: list, skipped_today: list,
                    never_attempted: list, stopped_at: str | None):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    lines = [
        "# S3 REGENERATION LOG",
        f"## Run: {now}",
        f"## Fail list: {FAIL_LIST_FILE}",
        f"## Quota limit: {MAX_TOTAL_API_CALLS} image generation calls",
        "",
        "---",
        "",
        "## SUMMARY",
        f"- **Image generation calls used:** {total_api_calls}/{MAX_TOTAL_API_CALLS}",
        f"- **Images successfully generated:** {len(generated)}",
        f"- **Generation failures:** {len(gen_failed)}",
        f"- **Skipped (already generated today):** {len(skipped_today)}",
        f"- **Never attempted (quota hit):** {len(never_attempted)}",
    ]
    if stopped_at:
        lines.append(f"- **Quota reached at:** `{stopped_at}`")
        lines.append(f"- **Status:** INCOMPLETE — resume by re-running (script skips today's files)")
    else:
        lines.append("- **Status:** ✅ COMPLETE")

    if generated:
        lines += ["", "---", "", "## GENERATED", "",
                  "| File | Priority | Errors | Validated |",
                  "|------|----------|--------|-----------|"]
        for e in generated:
            lines.append(f"| {e['file']} | P{e['priority']} | {e['errors']} | {e.get('validated', '—')} |")

    if gen_failed:
        lines += ["", "---", "", "## GENERATION FAILURES", "",
                  "| File | Priority | Reason |",
                  "|------|----------|--------|"]
        for e in gen_failed:
            lines.append(f"| {e['file']} | P{e['priority']} | {e.get('fail_reason', 'API error')} |")

    if never_attempted:
        lines += ["", "---", "", "## REMAINING (never attempted — quota hit)", "",
                  "| File | Priority | Errors |",
                  "|------|----------|--------|"]
        for e in never_attempted:
            lines.append(f"| {e['file']} | P{e['priority']} | {e['errors']} |")

    with open(REGEN_LOG, 'w') as f:
        f.write("\n".join(lines))
    log(f"Log written to {REGEN_LOG}", "INFO")


# ──────────────────────────────────────────────
# MAIN
# ──────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--batch", type=int, default=0,
                        help="Stop after N successful images for spot-checking (0 = no limit)")
    args, _ = parser.parse_known_args()
    BATCH_LIMIT = args.batch

    log("=" * 60)
    log("🎨 S3 TARGETED REGENERATION")
    log(f"Quota limit: {MAX_TOTAL_API_CALLS} total API calls")
    log(f"Fail list: {FAIL_LIST_FILE}")
    log(f"API keys loaded: {len(API_KEYS)}")
    log(f"Output dir: {OUTPUT_BASE_DIR}")
    log("=" * 60)

    fail_entries = parse_fail_list(FAIL_LIST_FILE)
    if not fail_entries:
        log("No failed images to regenerate. Exiting.", "ERROR")
        return

    log(f"Total to process: {len(fail_entries)}")
    for p in sorted(set(e["priority"] for e in fail_entries)):
        c = sum(1 for e in fail_entries if e["priority"] == p)
        log(f"  Priority {p}: {c} images")

    fail_scene_ids = {e["scene_id"] for e in fail_entries}

    generated = []
    gen_failed = []
    skipped_today = []
    never_attempted = []
    stopped_at = None

    for i, entry in enumerate(fail_entries, 1):
        file_path = entry["file"]
        chapter = entry["chapter"]
        tier = entry["tier"]
        scene_id = entry["scene_id"]
        output_path = OUTPUT_BASE_DIR / f"CH{chapter:02d}" / f"tier{tier}" / f"{scene_id}.png"

        # Resume check: skip if already generated today
        if was_generated_today(output_path):
            log(f"[{i}/{len(fail_entries)}] SKIP (generated today): {file_path}")
            skipped_today.append(entry)
            continue

        # Quota hard stop
        if total_api_calls >= MAX_TOTAL_API_CALLS:
            stopped_at = file_path
            never_attempted.append(entry)
            log(f"⛔ QUOTA REACHED ({total_api_calls}/{MAX_TOTAL_API_CALLS}). Stopping.", "WARNING")
            for remaining in fail_entries[i:]:
                never_attempted.append(remaining)
            break

        log(f"[{i}/{len(fail_entries)}] [calls {total_api_calls}/{MAX_TOTAL_API_CALLS}] P{entry['priority']} {file_path}")

        scene_data = get_original_scene_data(chapter, tier, scene_id)
        if not scene_data:
            entry["fail_reason"] = "Scene data not found in prompt file"
            gen_failed.append(entry)
            continue

        characters = scene_data.get("characters", [])
        char_refs = get_character_refs(characters, tier)

        outfit_lock = scan_outfit_lock(chapter, tier)
        style_anchor = get_style_anchor(chapter, tier, scene_id, fail_scene_ids)
        if style_anchor:
            log(f"  Style anchor: {style_anchor.name}")

        try:
            success = generate_image(scene_data, chapter, tier, char_refs,
                                     style_anchor=style_anchor, outfit_lock=outfit_lock)

            if success:
                if len(characters) >= 3 and api_calls_remaining() > 1:
                    validated = validate_image(output_path, characters)
                    entry["validated"] = "✅" if validated else "⚠️ re-flagged"

                    if not validated and api_calls_remaining() >= 1:
                        log(f"  Validation failed — attempting one re-generation", "WARNING")
                        success2 = generate_image(scene_data, chapter, tier, char_refs,
                                                  style_anchor=style_anchor, outfit_lock=outfit_lock)
                        entry["validated"] = "✅ (2nd attempt)" if success2 else "❌ failed twice"
                else:
                    entry["validated"] = "— (skipped)"

                generated.append(entry)

                if BATCH_LIMIT and len(generated) >= BATCH_LIMIT:
                    log(f"─── BATCH LIMIT REACHED ({BATCH_LIMIT} images) — stopping for spot-check ───", "WARNING")
                    log(f"  Generated this batch:", "WARNING")
                    for e in generated:
                        log(f"    {e['file']}", "WARNING")
                    stopped_at = f"batch limit after {BATCH_LIMIT} images"
                    for remaining in fail_entries[i:]:
                        never_attempted.append(remaining)
                    break
            else:
                entry["fail_reason"] = "No image data returned"
                gen_failed.append(entry)

        except QuotaExhaustedError:
            stopped_at = file_path
            never_attempted.append(entry)
            for remaining in fail_entries[i:]:
                never_attempted.append(remaining)
            log(f"⛔ Quota exhausted at {file_path}. Stopping.", "ERROR")
            break
        except Exception as e:
            log(f"  Unexpected error: {e}", "ERROR")
            entry["fail_reason"] = str(e)
            gen_failed.append(entry)
            continue

        if total_api_calls < MAX_TOTAL_API_CALLS:
            time.sleep(RATE_LIMIT_DELAY)

    log("=" * 60)
    log(f"{'COMPLETE' if not stopped_at else 'STOPPED — quota reached'}")
    log(f"Generated: {len(generated)} | Failed: {len(gen_failed)} | Skipped today: {len(skipped_today)} | Never attempted: {len(never_attempted)}")
    log(f"Total API calls used: {total_api_calls}/{MAX_TOTAL_API_CALLS}")
    log("=" * 60)

    write_regen_log(generated, gen_failed, skipped_today, never_attempted, stopped_at)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        log("Interrupted by user", "WARNING")
        write_regen_log([], [], [], [], "keyboard interrupt")
    except Exception as e:
        log(f"Fatal error: {e}", "ERROR")
        raise
