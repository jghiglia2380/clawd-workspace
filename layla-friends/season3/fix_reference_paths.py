#!/usr/bin/env python3
"""
Fix character reference image paths in all S3 CH02-04 prompt files.
Replaces incorrect reference filenames with actual filenames from inventory.
"""

import re
from pathlib import Path

# Actual reference image filenames from inventory
MASTER_THOMAS_REFS = {
    1: [
        "Gemini_Generated_Image_3f16l23f16l23f16.png",
        "Gemini_Generated_Image_ihja2oihja2oihja.png",
        "Gemini_Generated_Image_ka0mwoka0mwoka0m.png",
        "Gemini_Generated_Image_t4tqh4t4tqh4t4tq.png",
        "Gemini_Generated_Image_vmgxzbvmgxzbvmgx.png",
        "Gemini_Generated_Image_vpksxdvpksxdvpks.png",
        "Gemini_Generated_Image_wpa821wpa821wpa8.png",
        "Gemini_Generated_Image_yu0wc1yu0wc1yu0w.png",
    ],
    2: [
        "Gemini_Generated_Image_8m5g88m5g88m5g88.png",
        "Gemini_Generated_Image_8tts398tts398tts.png",
        "Gemini_Generated_Image_amsqzvamsqzvamsq.png",
        "Gemini_Generated_Image_jdvhdhjdvhdhjdvh.png",
        "Gemini_Generated_Image_llhk2cllhk2cllhk.png",
        "Gemini_Generated_Image_m2go07m2go07m2go.png",
        "Gemini_Generated_Image_ppcmoqppcmoqppcm.png",
        "Gemini_Generated_Image_t827nrt827nrt827.png",
    ],
    3: [
        "Gemini_Generated_Image_3lhvc63lhvc63lhv.png",
        "Gemini_Generated_Image_4ebjrf4ebjrf4ebj.png",
        "Gemini_Generated_Image_7gex7i7gex7i7gex.png",
        "Gemini_Generated_Image_aldqchaldqchaldq.png",
        "Gemini_Generated_Image_jvd5avjvd5avjvd5.png",
        "Gemini_Generated_Image_rlh6kzrlh6kzrlh6.png",
        "Gemini_Generated_Image_w2ccaw2ccaw2ccaw.png",
        "Thomas tier 3.png",
    ],
    4: [
        "Gemini_Generated_Image_64smbl64smbl64sm.png",
        "Gemini_Generated_Image_diiuh9diiuh9diiu.png",
        "Gemini_Generated_Image_gdfen1gdfen1gdfe.png",
        "Gemini_Generated_Image_hlulcahlulcahlul.png",
        "Gemini_Generated_Image_it8xewit8xewit8x.png",
        "Gemini_Generated_Image_x8eha3x8eha3x8eh.png",
        "Gemini_Generated_Image_xuod8bxuod8bxuod.png",
        "Gemini_Generated_Image_y9qmcy9qmcy9qmcy.png",
    ],
}

MAESTRO_GEARSMITH_REFS = {
    1: [],  # Directory not found - no Tier 1 references available
    2: [
        "Gemini_Generated_Image_1iegvp1iegvp1ieg.png",
        "Gemini_Generated_Image_2l7jhv2l7jhv2l7j.png",
        "Gemini_Generated_Image_bjoycsbjoycsbjoy.png",
        "Gemini_Generated_Image_ersjhhersjhhersj.png",
        "Gemini_Generated_Image_euo9q6euo9q6euo9.png",
        "Gemini_Generated_Image_ldq78zldq78zldq7.png",
        "Gemini_Generated_Image_lnfb2ylnfb2ylnfb.png",
        "Gemini_Generated_Image_vd6aa4vd6aa4vd6a.png",
        "Gemini_Generated_Image_yt5h0dyt5h0dyt5h.png",
    ],
    3: [
        "Gemini_Generated_Image_4kav2g4kav2g4kav.png",
        "Gemini_Generated_Image_4lmp5y4lmp5y4lmp.png",
        "Gemini_Generated_Image_4t2plk4t2plk4t2p.png",
        "Gemini_Generated_Image_f2l5rgf2l5rgf2l5.png",
        "Gemini_Generated_Image_fsngqkfsngqkfsng.png",
        "Gemini_Generated_Image_nuh6m7nuh6m7nuh6.png",
        "Gemini_Generated_Image_sdlo1lsdlo1lsdlo.png",
        "Gemini_Generated_Image_smrr0ysmrr0ysmrr.png",
        "Gemini_Generated_Image_vp2s7jvp2s7jvp2s.png",
        "Gemini_Generated_Image_xteyfgxteyfgxtey.png",
    ],
    4: [
        "Gemini_Generated_Image_225h3s225h3s225h.png",
        "Gemini_Generated_Image_2lv9qh2lv9qh2lv9.png",
        "Gemini_Generated_Image_3fqi233fqi233fqi.png",
        "Gemini_Generated_Image_68mgy768mgy768mg.png",
        "Gemini_Generated_Image_d791ynd791ynd791.png",
        "Gemini_Generated_Image_hf8ub9hf8ub9hf8u.png",
        "Gemini_Generated_Image_hkrppmhkrppmhkrp.png",
        "Gemini_Generated_Image_i8vs1gi8vs1gi8vs.png",
        "Gemini_Generated_Image_kjvuhokjvuhokjvu.png",
    ],
}

MASTER_POTTER_REFS = {
    1: [
        "Gemini_Generated_Image_71g3go71g3go71g3.png",
        "Gemini_Generated_Image_7xdykh7xdykh7xdy.png",
        "Gemini_Generated_Image_99lcvs99lcvs99lc.png",
        "Gemini_Generated_Image_bwhymsbwhymsbwhy.png",
        "Gemini_Generated_Image_bxcxcubxcxcubxcx.png",
        "Gemini_Generated_Image_c424elc424elc424.png",
        "Gemini_Generated_Image_iwrwjriwrwjriwrw.png",
        "Gemini_Generated_Image_qbq5dfqbq5dfqbq5.png",
        "Gemini_Generated_Image_u2mq10u2mq10u2mq.png",
    ],
    2: [
        "Gemini_Generated_Image_1p4m8b1p4m8b1p4m.png",
        "Gemini_Generated_Image_2am3de2am3de2am3.png",
        "Gemini_Generated_Image_8e5i4d8e5i4d8e5i.png",
        "Gemini_Generated_Image_b84mgbb84mgbb84m.png",
        "Gemini_Generated_Image_cf1e9pcf1e9pcf1e.png",
        "Gemini_Generated_Image_icb57qicb57qicb5.png",
        "Gemini_Generated_Image_iwvo0diwvo0diwvo.png",
        "Gemini_Generated_Image_j48766j48766j487.png",
        "Gemini_Generated_Image_nqwbkinqwbkinqwb.png",
    ],
    3: [
        "Gemini_Generated_Image_4cvu3n4cvu3n4cvu.png",
        "Gemini_Generated_Image_5e89rf5e89rf5e89.png",
        "Gemini_Generated_Image_ds7e3zds7e3zds7e.png",
        "Gemini_Generated_Image_eye6m5eye6m5eye6.png",
        "Gemini_Generated_Image_kw0qkgkw0qkgkw0q.png",
        "Gemini_Generated_Image_lzir5nlzir5nlzir.png",
        "Gemini_Generated_Image_ntpzu1ntpzu1ntpz.png",
        "Gemini_Generated_Image_oexecqoexecqoexe.png",
        "Gemini_Generated_Image_t6wjx5t6wjx5t6wj.png",
        "Gemini_Generated_Image_ukb0geukb0geukb0.png",
    ],
    4: [
        "Gemini_Generated_Image_22e76f22e76f22e7.png",
        "Gemini_Generated_Image_8auq698auq698auq.png",
        "Gemini_Generated_Image_azka6qazka6qazka.png",
        "Gemini_Generated_Image_ful51bful51bful5.png",
        "Gemini_Generated_Image_oj4z6doj4z6doj4z.png",
        "Gemini_Generated_Image_t81n6yt81n6yt81n.png",
        "Gemini_Generated_Image_ulh1uulh1uulh1uu.png",
        "Gemini_Generated_Image_vu3oajvu3oajvu3o.png",
    ],
}

BASE_PATH = "/Volumes/JG DRIVE/Project Explore/Character Reference Images"

def fix_character_references(content: str, character_name: str, tier: int, refs_dict: dict) -> tuple[str, int]:
    """
    Replace incorrect character reference paths with correct ones.
    Returns (updated_content, num_replacements).
    """
    if tier not in refs_dict or not refs_dict[tier]:
        print(f"  ⚠️  WARNING: No references available for {character_name} Tier {tier}")
        return content, 0

    refs = refs_dict[tier]
    replacements = 0

    # Pattern to match existing reference image lines for this character
    # Matches lines like: 1. `/Volumes/.../Master Thomas/Master Thomas Tier X/filename.png` - comment
    pattern = rf'(`{re.escape(BASE_PATH)}/{re.escape(character_name)}/{re.escape(character_name)} Tier {tier}/)(Gemini_Generated_Image_[^`]+\.png|[^`]+\.png)(`)'

    def replace_fn(match):
        nonlocal replacements
        prefix = match.group(1)  # Path up to filename
        old_filename = match.group(2)  # The incorrect filename
        suffix = match.group(3)  # Closing backtick

        # Use references in order - use index based on how many we've replaced
        if replacements < len(refs):
            new_filename = refs[replacements]
            replacements += 1
            return f"{prefix}{new_filename}{suffix}"
        else:
            # If we've run out of references, keep the old one
            return match.group(0)

    updated_content = re.sub(pattern, replace_fn, content)
    return updated_content, replacements


def fix_prompt_file(file_path: Path, tier: int):
    """Fix all character references in a single prompt file."""
    print(f"\n📝 Processing: {file_path.name}")

    content = file_path.read_text()
    original_content = content
    total_replacements = 0

    # Fix Master Thomas references
    content, n = fix_character_references(content, "Master Thomas", tier, MASTER_THOMAS_REFS)
    if n > 0:
        print(f"  ✅ Master Thomas: {n} references updated")
        total_replacements += n

    # Fix Maestro Gearsmith references (only if tier has refs)
    content, n = fix_character_references(content, "Maestro Gearsmith", tier, MAESTRO_GEARSMITH_REFS)
    if n > 0:
        print(f"  ✅ Maestro Gearsmith: {n} references updated")
        total_replacements += n

    # Fix Master Potter references
    content, n = fix_character_references(content, "Master Potter", tier, MASTER_POTTER_REFS)
    if n > 0:
        print(f"  ✅ Master Potter: {n} references updated")
        total_replacements += n

    if content != original_content:
        file_path.write_text(content)
        print(f"  💾 Saved with {total_replacements} total updates")
    else:
        print(f"  ℹ️  No changes needed")


def main():
    """Fix all prompt files for CH02-04, Tiers 1-4."""
    print("🔧 Fixing character reference paths in S3 CH02-04 prompt files...\n")

    prompts_dir = Path("/Users/justin/clawd-workspace/layla-friends/season3/prompts")

    chapters = [2, 3, 4]
    tiers = [1, 2, 3, 4]

    files_processed = 0

    for chapter in chapters:
        for tier in tiers:
            file_path = prompts_dir / f"S3-CH{chapter:02d}_TIER{tier}_PROMPTS.md"

            if not file_path.exists():
                print(f"⚠️  File not found: {file_path.name}")
                continue

            fix_prompt_file(file_path, tier)
            files_processed += 1

    print(f"\n✅ Complete! Processed {files_processed} prompt files.")
    print(f"\n⚠️  NOTE: Maestro Gearsmith Tier 1 has no reference images available.")
    print(f"   Any Tier 1 prompts with Maestro Gearsmith will need manual review.")


if __name__ == "__main__":
    main()
