#!/usr/bin/env python3
"""
Convert sphinx-tabs directives to canvas-tabs directives.
"""

import re
import os
import glob


def convert_tabs_in_file(filepath):
    """Convert tabs in a single file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content

    # Replace .. tabs:: with .. canvas-tabs::
    content = re.sub(r'\.\. tabs::', '.. canvas-tabs::', content)

    # Replace .. tab:: with .. canvas-tab::
    content = re.sub(r'\.\. tab::', '.. canvas-tab::', content)

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
        if convert_tabs_in_file(filepath):
            converted += 1

    print(f"\nConverted {converted} files")


if __name__ == '__main__':
    main()
