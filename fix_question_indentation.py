#!/usr/bin/env python3
"""
Fix indentation for canvas-answer to be nested under canvas-question.
"""

import re


def fix_question_indentation(filepath):
    """Fix question/answer indentation in a single file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    original_lines = lines[:]
    new_lines = []
    i = 0

    while i < len(lines):
        line = lines[i]

        # Check if this is a canvas-answer at column 0
        if line.strip() == '.. canvas-answer::' and not line.startswith(' '):
            # This answer needs to be indented under the question
            # Add 3 spaces to the directive
            new_lines.append('   .. canvas-answer::\n')
            i += 1

            # Skip blank line if present
            if i < len(lines) and lines[i].strip() == '':
                new_lines.append('\n')
                i += 1

            # Now indent all following content until we hit a dedented line or new directive
            while i < len(lines):
                content_line = lines[i]

                # If blank line, keep it
                if content_line.strip() == '':
                    new_lines.append(content_line)
                    i += 1
                    continue

                # If it's a new directive at column 0, stop indenting
                if content_line.startswith('.. ') and not content_line.startswith('   '):
                    break

                # If line is already indented, keep relative indentation but add 6 spaces total
                # If line starts at column 0, indent by 6 spaces
                if content_line.startswith('   '):
                    # Already has some indent, add 3 more
                    new_lines.append('   ' + content_line)
                else:
                    # No indent, add 6 spaces
                    new_lines.append('      ' + content_line)

                i += 1
        else:
            new_lines.append(line)
            i += 1

    # Only write if changed
    if new_lines != original_lines:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.writelines(new_lines)
        print(f"Fixed: {filepath}")
        return True
    return False


def main():
    """Fix all RST files with canvas-question."""
    files = [
        'source/episodes/episode1_2.rst',
        'source/episodes/episode1.rst',
        'source/episodes/episode2_3.rst',
        'source/episodes/episode2.rst',
        'source/episodes/episode3_2.rst',
        'source/episodes/episode3.rst',
    ]

    fixed = 0
    for filepath in files:
        if fix_question_indentation(filepath):
            fixed += 1

    print(f"\nFixed {fixed} files")


if __name__ == '__main__':
    main()
