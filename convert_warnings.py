#!/usr/bin/env python3
"""
Convert .. warning:: to .. uio-dont::
"""

import re
import glob


def convert_warnings(filepath):
    """Convert warnings in a single file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content

    # Replace .. warning:: with .. uio-dont::
    content = re.sub(r'\.\. warning::', '.. uio-dont::', content)

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
        if convert_warnings(filepath):
            converted += 1

    print(f"\nConverted {converted} files")


if __name__ == '__main__':
    main()
