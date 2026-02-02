#!/usr/bin/env python3
"""
Remove navigation elements from HTML files for Canvas integration.
Canvas provides its own navigation, so we remove:
- Sidebar navigation (wy-nav-side)
- Top navigation bar (wy-nav-top)
- Breadcrumbs (wy-breadcrumbs)
- Footer prev/next navigation
- Search box
- Version selector
"""

import re
import glob
from pathlib import Path


def remove_navigation_from_html(filepath):
    """Remove navigation elements from a single HTML file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content

    # Remove sidebar navigation (entire wy-nav-side section)
    content = re.sub(
        r'<nav data-toggle="wy-nav-shift" class="wy-nav-side">.*?</nav>',
        '',
        content,
        flags=re.DOTALL
    )

    # Remove top navigation bar
    content = re.sub(
        r'<nav class="wy-nav-top".*?</nav>',
        '',
        content,
        flags=re.DOTALL
    )

    # Remove breadcrumbs navigation
    content = re.sub(
        r'<div role="navigation" aria-label="Page navigation">.*?</div>',
        '',
        content,
        flags=re.DOTALL
    )

    # Remove footer with prev/next buttons
    content = re.sub(
        r'<footer>.*?</footer>',
        '',
        content,
        flags=re.DOTALL
    )

    # Remove "View page source" link and similar
    content = re.sub(
        r'<li class="wy-breadcrumbs-aside">.*?</li>',
        '',
        content,
        flags=re.DOTALL
    )

    # Remove version selector (rst-versions)
    content = re.sub(
        r'<div class="rst-versions".*?</div>',
        '',
        content,
        flags=re.DOTALL
    )

    # Adjust content width since sidebar is gone
    # Change wy-nav-content-wrap to not have left margin
    content = re.sub(
        r'<section data-toggle="wy-nav-shift" class="wy-nav-content-wrap">',
        '<section class="wy-nav-content-wrap" style="margin-left: 0;">',
        content
    )

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
        if remove_navigation_from_html(filepath):
            processed += 1
            print(f"Processed: {filepath}")

    print(f"\nProcessed {processed} files")


if __name__ == '__main__':
    main()
