#!/usr/bin/env python3
"""
Convert existing directives to UiO components.
- exercise:: -> uio-exercise:: or uio-reflect::
- solution:: -> uio-solution::
- admonition:: Spørsmål -> uio-question::
- admonition:: Svar -> uio-answer::
"""

import re
import glob


def convert_file(filepath):
    """Convert directives in a single file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content

    # Convert .. exercise:: to .. uio-exercise:: or .. uio-reflect::
    # Need to check if the exercise contains "Refleksjon" text
    def convert_exercise(match):
        full_match = match.group(0)
        # Look ahead in the content to check if this is a reflection
        exercise_content = match.group(1)
        if 'Refleksjon' in exercise_content or 'refleksjon' in exercise_content:
            return '.. uio-reflect::\n' + exercise_content
        else:
            return '.. uio-exercise::\n' + exercise_content

    # Match exercise directive and its content (indented lines following it)
    content = re.sub(
        r'\.\. exercise::\n((?:   .*\n|\n)*)',
        convert_exercise,
        content
    )

    # Convert .. solution:: to .. uio-solution::
    content = re.sub(r'\.\. solution::', '.. uio-solution::', content)

    # Convert .. admonition:: Spørsmål to .. uio-question::
    content = re.sub(r'\.\. admonition:: Spørsmål', '.. uio-question::', content)

    # Convert .. admonition:: Svar to .. uio-answer::
    # Handle both with and without :class: line
    content = re.sub(r'\.\. admonition:: Svar\n   :class: tip', '.. uio-answer::', content)
    content = re.sub(r'\.\. admonition:: Svar', '.. uio-answer::', content)

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
        if convert_file(filepath):
            converted += 1

    print(f"\nConverted {converted} files")


if __name__ == '__main__':
    main()
