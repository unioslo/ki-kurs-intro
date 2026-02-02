#!/usr/bin/env python3
"""
Fix indentation for uio-answer to be nested under uio-question.
"""

import glob


def is_section_underline(line):
    """Check if a line is a RST section underline."""
    stripped = line.strip()
    if not stripped:
        return False
    # Check if line is all the same character and it's a section marker
    if len(set(stripped)) == 1 and stripped[0] in '=-~`:\'"^_*+#<>':
        return True
    return False


def fix_answer_indentation(filepath):
    """Fix answer indentation in a single file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    original_lines = lines[:]
    new_lines = []
    i = 0

    while i < len(lines):
        line = lines[i]

        # Check if this is a uio-answer at column 0
        if line.strip() == '.. uio-answer::' and not line.startswith(' '):
            # This answer needs to be indented under the question
            # Add 3 spaces to the directive
            new_lines.append('   .. uio-answer::\n')
            i += 1

            # Skip blank line if present
            if i < len(lines) and lines[i].strip() == '':
                new_lines.append('\n')
                i += 1

            # Now indent all following content until we hit a dedented line or new directive
            while i < len(lines):
                content_line = lines[i]

                # If blank line, keep it but check next line
                if content_line.strip() == '':
                    # Look ahead to see if next line is a section title or directive
                    if i + 1 < len(lines):
                        next_line = lines[i + 1]
                        # If next line is not indented and not blank, we're done
                        if next_line.strip() and not next_line.startswith(' '):
                            break
                    new_lines.append(content_line)
                    i += 1
                    continue

                # If it's a new directive at column 0, stop indenting
                if content_line.startswith('.. ') and not content_line.startswith('   '):
                    break

                # If it's a section underline, stop (and the title should already be there)
                if is_section_underline(content_line):
                    break

                # Check if this looks like a section title (followed by underline)
                if i + 1 < len(lines) and is_section_underline(lines[i + 1]):
                    break

                # If line starts at column 0 and is not blank, stop
                if not content_line.startswith(' ') and content_line.strip():
                    break

                # If line is already indented, add 3 more spaces
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
    """Fix all RST files in source/episodes/."""
    pattern = 'source/episodes/*.rst'
    files = glob.glob(pattern)

    fixed = 0
    for filepath in files:
        if fix_answer_indentation(filepath):
            fixed += 1

    print(f"\nFixed {fixed} files")


if __name__ == '__main__':
    main()
