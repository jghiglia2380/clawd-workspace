#!/usr/bin/env python3
"""
Full reaudit of Season 4 scripts to verify tier progression.
Checks that higher tiers are consistently more complex than lower tiers.
"""

import os
import re
from collections import defaultdict

def extract_word_count(filepath):
    """Extract target and actual word counts from script."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract target word count
    target_match = re.search(r'\*\*Target Word Count:\*\* (\d+)', content)
    target_wc = int(target_match.group(1)) if target_match else None

    # Extract actual word count
    actual_match = re.search(r'\*\*Total Word Count: ([\d,]+) words\*\*', content)
    if actual_match:
        actual_wc = int(actual_match.group(1).replace(',', ''))
    else:
        actual_wc = None

    return target_wc, actual_wc

def extract_msl(filepath):
    """Extract mean sentence length from script."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract estimated MSL
    msl_match = re.search(r'\*\*Estimated MSL:\*\* ~?([\d.]+)', content)
    if msl_match:
        return float(msl_match.group(1))
    return None

def check_tier_progression():
    """Check that each tier progresses properly within each chapter."""
    scripts_dir = 'scripts'
    issues = []

    # Group files by chapter
    chapters = defaultdict(dict)

    for filename in os.listdir(scripts_dir):
        if not filename.startswith('S4-CH') or not filename.endswith('.md'):
            continue

        # Parse chapter and tier
        match = re.match(r'S4-CH(\d+)_TIER(\d)', filename)
        if not match:
            continue

        chapter = int(match.group(1))
        tier = int(match.group(2))

        filepath = os.path.join(scripts_dir, filename)
        target_wc, actual_wc = extract_word_count(filepath)
        msl = extract_msl(filepath)

        chapters[chapter][tier] = {
            'filename': filename,
            'target_wc': target_wc,
            'actual_wc': actual_wc,
            'msl': msl
        }

    # Check each chapter for proper progression
    for chapter in sorted(chapters.keys()):
        tiers = chapters[chapter]

        for tier in [1, 2, 3, 4]:
            if tier not in tiers:
                issues.append(f"CH{chapter:02d}: Missing TIER{tier}")
                continue

        # Check word count progression
        for tier in [1, 2, 3]:
            next_tier = tier + 1
            if tier in tiers and next_tier in tiers:
                curr_wc = tiers[tier]['actual_wc']
                next_wc = tiers[next_tier]['actual_wc']

                if curr_wc and next_wc and curr_wc >= next_wc:
                    issues.append(
                        f"CH{chapter:02d}: TIER{tier} word count ({curr_wc}) >= TIER{next_tier} ({next_wc})"
                    )

        # Check MSL progression
        for tier in [1, 2, 3]:
            next_tier = tier + 1
            if tier in tiers and next_tier in tiers:
                curr_msl = tiers[tier]['msl']
                next_msl = tiers[next_tier]['msl']

                if curr_msl and next_msl and curr_msl >= next_msl:
                    issues.append(
                        f"CH{chapter:02d}: TIER{tier} MSL ({curr_msl}) >= TIER{next_tier} ({next_msl})"
                    )

    return issues, chapters

def print_summary(chapters):
    """Print summary of all scripts."""
    print("\n" + "="*80)
    print("SEASON 4 TIER PROGRESSION SUMMARY")
    print("="*80)

    for chapter in sorted(chapters.keys()):
        print(f"\nCHAPTER {chapter:02d}")
        print("-" * 60)
        tiers = chapters[chapter]

        for tier in [1, 2, 3, 4]:
            if tier not in tiers:
                print(f"  TIER{tier}: MISSING")
                continue

            data = tiers[tier]
            wc = data['actual_wc'] or 'N/A'
            msl = data['msl'] or 'N/A'
            print(f"  TIER{tier}: {wc:>5} words | MSL: {msl:>5} | {data['filename']}")

def main():
    print("Running Season 4 Full Reaudit...")
    print("Checking tier progression for all chapters...")

    issues, chapters = check_tier_progression()

    print_summary(chapters)

    print("\n" + "="*80)
    print("TIER PROGRESSION ISSUES")
    print("="*80)

    if issues:
        print(f"\n⚠️  Found {len(issues)} progression issue(s):\n")
        for issue in issues:
            print(f"  ❌ {issue}")
        print("\nFIX REQUIRED: Progression inversions detected!")
        return 1
    else:
        print("\n✅ No progression issues found!")
        print("✅ All chapters have proper tier progression")
        print("✅ Word counts increase across tiers")
        print("✅ MSL increases across tiers")
        return 0

if __name__ == '__main__':
    exit(main())
