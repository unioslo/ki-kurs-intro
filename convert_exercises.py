#!/usr/bin/env python3
"""
Convert exercise/solution directives to canvas-exercise/canvas-solution.
"""

import re
import os
import glob


def convert_exercises_in_file(filepath):
    """Convert exercises in a single file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content

    # Replace .. exercise:: with .. canvas-exercise::
    content = re.sub(r'\.\. exercise::', '.. canvas-exercise::', content)

    # Replace .. solution:: with .. canvas-solution::
    content = re.sub(r'\.\. solution::', '.. canvas-solution::', content)

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
        if convert_exercises_in_file(filepath):
            converted += 1

    print(f"\nConverted {converted} files")


if __name__ == '__main__':
    main()
