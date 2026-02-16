#!/usr/bin/env python3
"""
Verify all character reference paths and remove any that point to non-existent files.
This ensures the generation script only tries to load files that actually exist.
"""

import re
from pathlib import Path

def verify_and_clean_references(file_path: Path) -> tuple[int, int]:
    """
    Check all reference image paths and remove those that don't exist.
    Returns (total_refs_checked, refs_removed).
    """
    content = file_path.read_text()
    original_content = content

    # Pattern to match reference image lines with paths
    # Format: 1. `/path/to/file.png` - comment
    pattern = r'(\d+)\.\s+`([^`]+)`\s*-\s*([^\n]+)'

    matches = list(re.finditer(pattern, content))
    refs_to_remove = []

    for match in matches:
        line_num = match.group(1)
        file_path_str = match.group(2)
        comment = match.group(3)

        # Check if path exists
        ref_path = Path(file_path_str)
        if not ref_path.exists():
            refs_to_remove.append((match.start(), match.end(), file_path_str))

    # Remove non-existent references (in reverse order to maintain positions)
    for start, end, path in reversed(refs_to_remove):
        # Remove the entire line including newline
        if content[end:end+1] == '\n':
            end += 1
        content = content[:start] + content[end:]

    # Renumber remaining references in each **Reference images** section
    content = renumber_reference_sections(content)

    return len(matches), len(refs_to_remove), content


def renumber_reference_sections(content: str) -> str:
    """Renumber references in each section to be sequential (1, 2, 3...)."""
    # Find all **Reference images (N):** sections
    sections = re.split(r'(\*\*Reference images.*?\*\*\n)', content)

    result = []
    for i, section in enumerate(sections):
        if i % 2 == 0:  # Regular content
            # Renumber any reference lines in this section
            lines = section.split('\n')
            renumbered_lines = []
            ref_num = 1
            for line in lines:
                if re.match(r'\d+\.\s+`', line):
                    # This is a reference line, renumber it
                    line = re.sub(r'^\d+\.', f'{ref_num}.', line)
                    ref_num += 1
                renumbered_lines.append(line)
            result.append('\n'.join(renumbered_lines))
        else:  # Header line
            # Update the count in the header if needed
            # Will update this after we know the actual count
            result.append(section)

    return ''.join(result)


def update_reference_counts(content: str) -> str:
    """Update the (N) count in **Reference images (N):** headers."""
    # Find each **Reference images (N):** header and count references after it
    pattern = r'\*\*Reference images \((\d+)\):\*\*\n'

    def count_following_refs(match_obj):
        # Find how many reference lines follow this header
        start_pos = match_obj.end()
        # Look ahead until we hit another header or end of section
        following_text = content[start_pos:start_pos+5000]  # Look ahead reasonable amount
        ref_lines = re.findall(r'^\d+\.\s+`[^`]+`', following_text, re.MULTILINE)
        actual_count = len(ref_lines)
        return f'**Reference images ({actual_count}):**\n'

    return re.sub(pattern, count_following_refs, content)


def process_file(file_path: Path):
    """Process a single prompt file."""
    print(f"\n📝 {file_path.name}")

    total_refs, removed_refs, cleaned_content = verify_and_clean_references(file_path)

    if removed_refs > 0:
        # Update reference counts in headers
        cleaned_content = update_reference_counts(cleaned_content)

        # Write back
        file_path.write_text(cleaned_content)
        print(f"  ⚠️  Removed {removed_refs} non-existent references (out of {total_refs})")
        print(f"  💾 Saved")
    else:
        print(f"  ✅ All {total_refs} references verified - all files exist")


def main():
    """Verify and clean all CH02-04 prompt files."""
    print("🔍 Verifying character reference paths in S3 CH02-04 prompt files...\n")

    prompts_dir = Path("/Users/justin/clawd-workspace/layla-friends/season3/prompts")

    chapters = [2, 3, 4]
    tiers = [1, 2, 3, 4]

    total_removed = 0

    for chapter in chapters:
        for tier in tiers:
            file_path = prompts_dir / f"S3-CH{chapter:02d}_TIER{tier}_PROMPTS.md"

            if not file_path.exists():
                continue

            process_file(file_path)

    print(f"\n✅ Verification complete!")


if __name__ == "__main__":
    main()
