#!/usr/bin/env python3
"""
Fix headers in episodeX_Y.rst files (Y > 0):
1. Remove the main header with === underline
2. Replace ~~~ section headers with === headers
"""

import glob
import re


def fix_episode_file(filepath):
    """Fix headers in a single episode file."""
    # Skip _0.rst files
    if filepath.endswith('_0.rst'):
        return False

    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    new_lines = []
    skip_next = False
    removed_main_header = False

    for i, line in enumerate(lines):
        if skip_next:
            skip_next = False
            continue

        # Remove the main header (first occurrence of === underline)
        if not removed_main_header and '===' in line and line.strip() and all(c == '=' for c in line.strip()):
            # This is the === underline, skip it and the line before it (the title)
            if new_lines and new_lines[-1].strip():
                new_lines.pop()  # Remove the title line
            removed_main_header = True
            # Also skip any blank lines after
            continue

        # Replace ~~~ underline with === underline
        if '~~~' in line and line.strip() and all(c == '~' for c in line.strip()):
            # Replace ~~~ with ===
            new_lines.append('=' * len(line.strip()) + '\n')
            continue

        new_lines.append(line)

    # Write the modified content
    with open(filepath, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)

    print(f"Fixed: {filepath}")
    return True


def main():
    """Fix all episodeX_Y.rst files where Y > 0."""
    pattern = 'source/episodes/episode*_[1-9]*.rst'
    files = glob.glob(pattern)

    fixed = 0
    for filepath in sorted(files):
        if fix_episode_file(filepath):
            fixed += 1

    print(f"\nFixed {fixed} files")


if __name__ == '__main__':
    main()
