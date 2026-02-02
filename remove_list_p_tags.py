#!/usr/bin/env python3
"""
Remove <p> tags from list items in HTML files.
"""

import re
import glob


def remove_list_p_tags(filepath):
    """Remove <p></p> tags from list items in a single file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content

    # Replace <li><p>content</p></li> with <li>content</li>
    # This regex handles single-line list items
    content = re.sub(r'<li><p>(.*?)</p></li>', r'<li>\1</li>', content, flags=re.DOTALL)

    # Also handle multi-line cases where <p> and </p> are on different lines
    # Replace <li><p> followed by content and </p> with just the content
    content = re.sub(r'<li><p>(.*?)</p>', r'<li>\1', content, flags=re.DOTALL)

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
        if remove_list_p_tags(filepath):
            processed += 1
            print(f"Processed: {filepath}")

    print(f"\nProcessed {processed} files")


if __name__ == '__main__':
    main()
