#!/usr/bin/env python3
"""
Replace admonition note classes with uio-icon-box info.
"""

import re
import glob


def replace_admonition_note(filepath):
    """Replace admonition note with uio-icon-box info in a single file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content

    # Replace class="admonition note" with class="uio-icon-box info"
    content = re.sub(r'class="admonition note"', 'class="uio-icon-box info"', content)

    # Only write if changed
    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False


def main():
    """Process all HTML files in _build/html/."""
    pattern = '_build/html/**/*.html'
    files = glob.glob(pattern, recursive=True)

    processed = 0
    for filepath in files:
        if replace_admonition_note(filepath):
            processed += 1
            print(f"Processed: {filepath}")

    print(f"\nProcessed {processed} files")


if __name__ == '__main__':
    main()
