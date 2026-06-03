#!/usr/bin/env python3
"""Build PDF for Episode 5 only without page numbers."""

import os
import sys
import shutil
from pathlib import Path

# Create a temporary conf.py that overrides settings
conf_override = """
# Override master_doc to use episode5_only
master_doc = 'episode5_only'

# Override PDF filename
simplepdf_file_name = 'Episode5-Oppgaver.pdf'

# Replace simplepdf.css with no-pagenumbers version in CSS files
html_css_files = [
    'variables.css',
    'common.css',
    'uio-global-override.css',
    'custom.css',
    'simplepdf-no-pagenumbers.css',  # Use version without page numbers
]
"""

def main():
    # Write temporary config override
    conf_override_path = Path('source/conf_episode5.py')

    # Read original conf.py
    with open('source/conf.py', 'r') as f:
        original_conf = f.read()

    # Write override file
    with open(conf_override_path, 'w') as f:
        f.write(original_conf)
        f.write('\n\n# Episode 5 overrides\n')
        f.write(conf_override)

    # Build with override config
    print("Building Episode 5 PDF...")
    os.system(f'sphinx-build -c source -b simplepdf source _build/simplepdf-episode5 -D master_doc=episode5_only -D simplepdf_file_name=Episode5-Oppgaver.pdf')

    # Clean up
    conf_override_path.unlink()

    # Check if PDF was created
    pdf_path = Path('_build/simplepdf-episode5/Episode5-Oppgaver.pdf')
    if pdf_path.exists():
        print(f"\n✓ PDF created: {pdf_path}")
        print(f"  Size: {pdf_path.stat().st_size / 1024:.1f} KB")
    else:
        print("\n✗ PDF creation failed")
        sys.exit(1)

if __name__ == '__main__':
    main()
