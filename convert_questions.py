#!/usr/bin/env python3
"""
Convert admonition Spørsmål/Svar to canvas-question/canvas-answer.
"""

import re
import os
import glob


def convert_questions_in_file(filepath):
    """Convert questions in a single file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content

    # Replace .. admonition:: Spørsmål with .. canvas-question::
    content = re.sub(r'\.\. admonition:: Spørsmål', '.. canvas-question::', content)

    # Replace .. admonition:: Svar (with optional :class: tip) with .. canvas-answer::
    # Match both with and without :class: line
    content = re.sub(r'\.\. admonition:: Svar\n   :class: tip', '.. canvas-answer::', content)
    content = re.sub(r'\.\. admonition:: Svar', '.. canvas-answer::', content)

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
        if convert_questions_in_file(filepath):
            converted += 1

    print(f"\nConverted {converted} files")


if __name__ == '__main__':
    main()
