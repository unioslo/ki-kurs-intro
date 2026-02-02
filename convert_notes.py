#!/usr/bin/env python3
"""
Convert .. note:: to .. uio-note::
"""

import re
import glob


def convert_notes(filepath):
    """Convert notes in a single file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content

    # Replace .. note:: with .. uio-note::
    content = re.sub(r'\.\. note::', '.. uio-note::', content)

    # Only write if changed
    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Converted: {filepath}")
        return True
    return False


def main():
    """Convert all RST files in source/episodes/."""
    pattern = 'source/episodes/*.rst'
    files = glob.glob(pattern)

    converted = 0
    for filepath in files:
        if convert_notes(filepath):
            converted += 1

    print(f"\nConverted {converted} files")


if __name__ == '__main__':
    main()
