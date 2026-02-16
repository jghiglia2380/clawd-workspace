#!/usr/bin/env python3
"""
Fix Potter name references - add "Celeste" where appropriate
"""

import re
from pathlib import Path

SCRIPTS_DIR = Path('/Users/justin/clawd-workspace/layla-friends/season3/scripts')

# Potter chapters (5-7)
potter_files = []
for ch in ['01', '05', '06', '07', '12']:
    for tier in ['TIER1', 'TIER2', 'TIER3', 'TIER4']:
        file_path = SCRIPTS_DIR / f'S3-CH{ch}_{tier}.md'
        if file_path.exists():
            potter_files.append(file_path)

def fix_potter_intro(file_path):
    """Fix the Potter's introduction to include name Celeste"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content

    # Pattern 1: "I am the Potter" -> "I am Celeste, the Potter"
    content = re.sub(
        r'I am the Potter\b',
        'I am Celeste, the Potter',
        content
    )

    # Pattern 2: Standalone dialogue references where personal name is better
    # Only in dialogue, not narrative
    # This is more nuanced and we'll do selectively

    if content != original:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

print("Fixing Potter name introductions...")
for file_path in potter_files:
    if fix_potter_intro(file_path):
        print(f"✓ {file_path.name}")

print("\n✅ Potter name fixes complete!")
print("\nNote: 'the Potter' can remain as a title in most narrative contexts.")
print("Celeste is used for personal address and introductions.")
