#!/usr/bin/env python3
"""
Remove excessive padding and unnatural phrasing from Tier 4 scripts
"""

import re
from pathlib import Path

SCRIPTS_DIR = Path('/Users/justin/clawd-workspace/layla-friends/season3/scripts')

# Get all TIER4 files
tier4_files = sorted(SCRIPTS_DIR.glob('S3-CH*_TIER4.md'))

# Padding patterns to remove (narrator-level fixes)
NARRATOR_FIXES = [
    # Double/triple modifiers
    (r'\bgenuinely and demonstrably\b', 'genuinely'),
    (r'\bspecifically and methodically\b', 'methodically'),
    (r'\bcompletely and totally\b', 'completely'),
    (r'\bobvious and evident\b', 'obvious'),
    (r'\babsolutely critical and essential\b', 'essential'),

    # Redundant intensifiers
    (r'\bvery, very\b', 'very'),
    (r'\bthroughout the entire surface\b', 'throughout'),
    (r'\bcompletely pitch black\b', 'pitch black'),
    (r'\bstill brilliantly visible\b', 'still visible'),
    (r'\bsmall ephemeral clouds\b', 'small clouds'),

    # Verbose phrases - shorten
    (r'\bwith unwavering certainty\b', ''),
    (r'\bwith characteristic precision and attention to detail\b', 'with characteristic precision'),
    (r'\bwith growing wonder and amazement\b', 'with wonder'),
    (r'\bwith obvious pride and satisfaction\b', 'with pride'),
    (r'\bwith genuine surprise and curiosity\b', 'with surprise'),
    (r'\bsteadily growing wonder\b', 'growing wonder'),
    (r'\bmounting excitement and anticipation\b', 'mounting excitement'),
    (r'\bevident seriousness and gravity\b', 'evident seriousness'),

    # Excessive adverb stacking
    (r'\babsolutely and demonstrably\b', 'clearly'),
    (r'\bprecisely and methodically\b', 'methodically'),
    (r'\bcarefully and thoroughly\b', 'carefully'),
    (r'\bdeeply and sincerely\b', 'sincerely'),
    (r'\bcompletely and irrevocably\b', 'completely'),
    (r'\bincredibly thick\b', 'thick'),
    (r'\bsubstantially larger\b', 'larger'),
    (r'\bnoticeably faster\b', 'faster'),
    (r'\bprogressively tired\b', 'tired'),
    (r'\bsteadily growing\b', 'growing'),

    # "And" connector padding
    (r'\bbright and intelligent\b', 'bright'),
    (r'\bwarm and genuine\b', 'warm'),
    (r'\bkind and bright\b', 'kind'),
    (r'\bhonest and direct\b', 'honest'),
    (r'\bcalm and patience\b', 'calm'),

    # Remove "genuinely/absolutely/clearly" when overused
    (r'\babsolutely crucial\b', 'crucial'),
    (r'\bgenuinely important\b', 'important'),
    (r'\bclearly visible\b', 'visible'),
    (r'\bobviously important\b', 'important'),
    (r'\bdemonstrablyright\b', 'right'),

    # Specific verbose patterns from the scripts
    (r'\bwith meticulous care\b', 'carefully'),
    (r'\bwith quiet authority and unmistakable confidence\b', 'with quiet authority'),
    (r'\bwith characteristic calm and patience\b', 'calmly'),
    (r'\bfor maximum impact\b', ''),
    (r'\bin equal measure\b', ''),
    (r'\bto full strength\b', 'completely'),
    (r'\bto full bonding strength\b', 'completely'),
]

def apply_padding_fixes(file_path):
    """Remove padding from narrator text"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content
    changes = []

    for pattern, replacement in NARRATOR_FIXES:
        matches = len(re.findall(pattern, content, re.IGNORECASE))
        if matches > 0:
            content = re.sub(pattern, replacement, content, flags=re.IGNORECASE)
            if replacement:
                changes.append(f"{matches}x: trimmed '{pattern}' -> '{replacement}'")
            else:
                changes.append(f"{matches}x: removed '{pattern}'")

    if content != original:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return changes
    return None

print("Removing padding from Tier 4 scripts...")
print("=" * 60)

total_changes = 0
for file_path in tier4_files:
    changes = apply_padding_fixes(file_path)
    if changes:
        print(f"\n✓ {file_path.name}:")
        for change in changes[:10]:  # Show first 10 changes
            print(f"  - {change}")
        if len(changes) > 10:
            print(f"  ... and {len(changes) - 10} more changes")
        total_changes += len(changes)

print("\n" + "=" * 60)
print(f"✅ Removed {total_changes} instances of padding across {len(tier4_files)} Tier 4 scripts")
print("\nNote: Child dialogue fixes require manual review for naturalness.")
