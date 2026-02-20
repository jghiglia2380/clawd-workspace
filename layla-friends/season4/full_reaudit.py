#!/usr/bin/env python3
"""
Full reaudit script for Layla & Friends S4 scripts.
Validates word counts, MSL, forbidden words, tier inversions, and FL vocabulary.

Usage:
    python3 full_reaudit.py S4-CH01_TIER1.md S4-CH01_TIER2.md S4-CH01_TIER3.md S4-CH01_TIER4.md
    python3 full_reaudit.py --chapter 1
    python3 full_reaudit.py --all
"""

import re
import sys
import os
import math
from pathlib import Path

# ── S2 PRODUCTION BASELINES (override handoff doc word counts) ──
# MSL ranges calibrated against S2 actual production:
#   S2 T1 actual MSL: 5.6  |  S2 T2: 8.2  |  S2 T3: 8.7  |  S2 T4: 11.1
# Key constraint: MSL must monotonically increase T1 < T2 < T3 < T4
TIER_TARGETS = {
    1: {
        "grade": "K-1st",
        "total_words": 600,
        "word_range": (550, 650),
        "wps": 30,
        "wps_range": (28, 33),
        "msl_range": (4, 8),       # S2 actual: 5.6
        "target_wpm": 75,
        "reading_level": "D",
        "fl_vocab_min": 2,
    },
    2: {
        "grade": "2nd",
        "total_words": 900,
        "word_range": (850, 950),
        "wps": 45,
        "wps_range": (42, 48),
        "msl_range": (6, 10),      # S2 actual: 6.7 (fixed splitter)
        "target_wpm": 112,
        "reading_level": "J",
        "fl_vocab_min": 3,
    },
    3: {
        "grade": "3rd",
        "total_words": 1000,
        "word_range": (950, 1050),
        "wps": 50,
        "wps_range": (47, 53),
        "msl_range": (8, 11),      # S2 actual: 8.7
        "target_wpm": 125,
        "reading_level": "M-N",
        "fl_vocab_min": 3,
    },
    4: {
        "grade": "4th",
        "total_words": 1170,
        "word_range": (1100, 1300),
        "wps": 58,
        "wps_range": (55, 62),
        "msl_range": (9, 14),      # S2 actual: 9.1 (fixed splitter)
        "target_wpm": 146,
        "reading_level": "O-P",
        "fl_vocab_min": 5,
    },
}

SCENES_PER_CHAPTER = 20

# ── FORBIDDEN PADDING WORDS ──
FORBIDDEN_WORDS = [
    "genuinely", "absolutely", "completely", "truly", "incredibly",
    "extraordinarily", "meticulously", "enthusiastically", "characteristically",
    "conscientiously", "progressively", "simultaneously", "fundamentally",
    "significantly", "considerably", "painstakingly", "wholeheartedly",
    "undoubtedly", "remarkably", "exceptionally",
]


def count_words(text):
    """Count words in text (split on whitespace)."""
    return len(text.split())


def split_sentences(text):
    """Split text into sentences, handling closing quotes after punctuation."""
    clean = text.strip()
    # Normalize: remove closing quotes that immediately follow sentence-ending
    # punctuation, so ." becomes . and !" becomes ! for splitting purposes.
    # This prevents ." from blocking the sentence-boundary regex.
    # Comma-quotes like ," are NOT affected (comma is not in [.!?]).
    normalized = re.sub(r'([.!?])(["\u201d\'\u2019]+)', r'\1', clean)
    # Split on sentence-ending punctuation followed by whitespace
    sentences = re.split(r'(?<=[.!?])\s+', normalized)
    # Filter empty strings
    return [s.strip() for s in sentences if s.strip()]


def calculate_msl(text):
    """Calculate mean sentence length (words per sentence)."""
    sentences = split_sentences(text)
    if not sentences:
        return 0
    total_words = sum(count_words(s) for s in sentences)
    return total_words / len(sentences)


def parse_script(filepath):
    """Parse a script markdown file into structured data."""
    with open(filepath, 'r') as f:
        content = f.read()

    # Extract tier from filename
    tier_match = re.search(r'TIER(\d)', str(filepath))
    tier = int(tier_match.group(1)) if tier_match else None

    # Extract chapter from filename
    ch_match = re.search(r'CH(\d+)', str(filepath))
    chapter = int(ch_match.group(1)) if ch_match else None

    # Parse scenes: ### Scene N (XX words)
    scene_pattern = r'### Scene (\d+) \((\d+) words?\)\n(.*?)(?=### Scene|\n---|\Z)'
    scenes = []
    for match in re.finditer(scene_pattern, content, re.DOTALL):
        scene_num = int(match.group(1))
        claimed_words = int(match.group(2))
        text = match.group(3).strip()
        actual_words = count_words(text)
        msl = calculate_msl(text)
        scenes.append({
            "number": scene_num,
            "claimed_words": claimed_words,
            "actual_words": actual_words,
            "msl": msl,
            "text": text,
        })

    # Extract FL vocabulary section
    fl_section = re.search(r'## FL VOCABULARY.*?\n(.*?)(?=\n---|\n## |\Z)', content, re.DOTALL)
    fl_terms = []
    if fl_section:
        fl_terms = re.findall(r'\*\*(.+?)\*\*', fl_section.group(1))

    return {
        "filepath": str(filepath),
        "tier": tier,
        "chapter": chapter,
        "scenes": scenes,
        "fl_terms": fl_terms,
        "raw": content,
    }


def find_forbidden_words(scenes):
    """Find any forbidden padding words in scene text."""
    findings = []
    for scene in scenes:
        text_lower = scene["text"].lower()
        for word in FORBIDDEN_WORDS:
            if word in text_lower:
                findings.append((scene["number"], word))
    return findings


def audit_script(filepath):
    """Full audit of a single script file."""
    data = parse_script(filepath)
    tier = data["tier"]
    targets = TIER_TARGETS.get(tier, {})
    issues = []
    warnings = []

    if not targets:
        issues.append(f"Unknown tier: {tier}")
        return data, issues, warnings

    # ── Scene count ──
    if len(data["scenes"]) != SCENES_PER_CHAPTER:
        issues.append(f"SCENE COUNT: {len(data['scenes'])} scenes (expected {SCENES_PER_CHAPTER})")

    # ── Total word count ──
    total_words = sum(s["actual_words"] for s in data["scenes"])
    lo, hi = targets["word_range"]
    if total_words < lo or total_words > hi:
        issues.append(f"TOTAL WORDS: {total_words} (target range {lo}-{hi})")
    else:
        pass  # OK

    # ── Words per scene ──
    wps_lo, wps_hi = targets["wps_range"]
    for scene in data["scenes"]:
        if scene["actual_words"] < wps_lo - 2 or scene["actual_words"] > wps_hi + 2:
            issues.append(
                f"  Scene {scene['number']}: {scene['actual_words']} wps "
                f"(target {wps_lo}-{wps_hi})"
            )

    # ── Claimed vs actual word count ──
    for scene in data["scenes"]:
        diff = abs(scene["actual_words"] - scene["claimed_words"])
        if diff > 2:
            warnings.append(
                f"  Scene {scene['number']}: claims {scene['claimed_words']}w, "
                f"actual {scene['actual_words']}w (off by {diff})"
            )

    # ── Mean sentence length ──
    all_text = " ".join(s["text"] for s in data["scenes"])
    overall_msl = calculate_msl(all_text)
    msl_lo, msl_hi = targets["msl_range"]
    if overall_msl < msl_lo - 1 or overall_msl > msl_hi + 1:
        issues.append(f"MSL: {overall_msl:.1f} words/sentence (target {msl_lo}-{msl_hi})")
    elif overall_msl < msl_lo or overall_msl > msl_hi:
        warnings.append(f"MSL: {overall_msl:.1f} words/sentence (target {msl_lo}-{msl_hi}, slightly off)")

    # ── Forbidden words ──
    forbidden = find_forbidden_words(data["scenes"])
    for scene_num, word in forbidden:
        issues.append(f"FORBIDDEN WORD: '{word}' in Scene {scene_num}")

    # ── FL vocabulary count ──
    if len(data["fl_terms"]) < targets["fl_vocab_min"]:
        warnings.append(
            f"FL VOCAB: {len(data['fl_terms'])} terms "
            f"(minimum {targets['fl_vocab_min']})"
        )

    data["total_words"] = total_words
    data["overall_msl"] = overall_msl
    return data, issues, warnings


def check_inversions(tier_data):
    """Check for tier inversions across all 4 tiers of a chapter."""
    inversions = []

    # Sort by tier
    sorted_tiers = sorted(tier_data, key=lambda d: d["tier"])

    for i in range(len(sorted_tiers) - 1):
        lower = sorted_tiers[i]
        upper = sorted_tiers[i + 1]

        # Word count should increase
        if lower["total_words"] >= upper["total_words"]:
            inversions.append(
                f"WORD COUNT INVERSION: T{lower['tier']} ({lower['total_words']}w) "
                f">= T{upper['tier']} ({upper['total_words']}w)"
            )

        # MSL should increase
        if lower["overall_msl"] >= upper["overall_msl"]:
            inversions.append(
                f"MSL INVERSION: T{lower['tier']} ({lower['overall_msl']:.1f}) "
                f">= T{upper['tier']} ({upper['overall_msl']:.1f})"
            )

    return inversions


def print_report(data, issues, warnings):
    """Print audit report for a single script."""
    tier = data["tier"]
    targets = TIER_TARGETS[tier]
    total = data["total_words"]
    msl = data["overall_msl"]

    status = "PASS" if not issues else "FAIL"
    icon = "✅" if not issues else "❌"

    print(f"\n{'='*60}")
    print(f"{icon} TIER {tier} ({targets['grade']}) — {status}")
    print(f"   File: {data['filepath']}")
    print(f"   Total words: {total} (target: {targets['word_range'][0]}-{targets['word_range'][1]})")
    print(f"   Avg wps: {total/len(data['scenes']):.1f} (target: ~{targets['wps']})")
    print(f"   MSL: {msl:.1f} (target: {targets['msl_range'][0]}-{targets['msl_range'][1]})")
    print(f"   Scenes: {len(data['scenes'])}")
    print(f"   FL terms: {len(data['fl_terms'])} ({', '.join(data['fl_terms']) if data['fl_terms'] else 'none'})")

    if issues:
        print(f"\n   ISSUES ({len(issues)}):")
        for issue in issues:
            print(f"   ❌ {issue}")

    if warnings:
        print(f"\n   WARNINGS ({len(warnings)}):")
        for w in warnings:
            print(f"   ⚠️  {w}")

    # Per-scene word counts
    print(f"\n   Scene breakdown:")
    for s in data["scenes"]:
        flag = ""
        wps_lo, wps_hi = targets["wps_range"]
        if s["actual_words"] < wps_lo - 2 or s["actual_words"] > wps_hi + 2:
            flag = " ⚠️"
        claimed_ok = "✓" if abs(s["actual_words"] - s["claimed_words"]) <= 2 else "✗"
        print(f"   SC{s['number']:02d}: {s['actual_words']}w (claimed {s['claimed_words']}w {claimed_ok}) MSL={s['msl']:.1f}{flag}")


def main():
    scripts_dir = Path(__file__).parent / "scripts"

    if "--all" in sys.argv:
        # Audit all chapters
        for ch in range(1, 13):
            files = []
            for tier in range(1, 5):
                f = scripts_dir / f"S4-CH{ch:02d}_TIER{tier}.md"
                if f.exists():
                    files.append(str(f))
            if files:
                print(f"\n{'#'*60}")
                print(f"# CHAPTER {ch}")
                print(f"{'#'*60}")
                run_audit(files)
    elif "--chapter" in sys.argv:
        idx = sys.argv.index("--chapter") + 1
        ch = int(sys.argv[idx])
        files = []
        for tier in range(1, 5):
            f = scripts_dir / f"S4-CH{ch:02d}_TIER{tier}.md"
            if f.exists():
                files.append(str(f))
        if files:
            run_audit(files)
        else:
            print(f"No scripts found for chapter {ch}")
    else:
        # Audit specific files passed as arguments
        files = [a for a in sys.argv[1:] if not a.startswith("--")]
        if files:
            run_audit(files)
        else:
            print("Usage: python3 full_reaudit.py --chapter 1")
            print("       python3 full_reaudit.py --all")
            print("       python3 full_reaudit.py file1.md file2.md ...")


def run_audit(files):
    """Run audit on a list of script files."""
    all_data = []
    all_pass = True

    for filepath in sorted(files):
        data, issues, warnings = audit_script(filepath)
        print_report(data, issues, warnings)
        all_data.append(data)
        if issues:
            all_pass = False

    # Check inversions if we have multiple tiers
    if len(all_data) > 1:
        inversions = check_inversions(all_data)
        print(f"\n{'='*60}")
        print("TIER INVERSION CHECK")
        if inversions:
            all_pass = False
            for inv in inversions:
                print(f"   ❌ {inv}")
        else:
            print("   ✅ No inversions detected")

    # Summary
    print(f"\n{'='*60}")
    if all_pass:
        print("✅ ALL CHECKS PASSED")
    else:
        print("❌ SOME CHECKS FAILED — fix issues above")
    print(f"{'='*60}\n")

    return all_pass


if __name__ == "__main__":
    main()
