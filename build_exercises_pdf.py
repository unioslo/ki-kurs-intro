#!/usr/bin/env python3
"""Build the Exercises (Treningsoppgaver) PDF.

The exercises PDF is produced with:
  - no table of contents
  - no standalone "Prøv selv" title page
  - no "Version ..." subtitle on the cover
  - no page numbers

These are all driven by the ``EXERCISES_PDF`` branch in ``source/conf.py``
(which swaps in ``simplepdf-no-pagenumbers.css`` and a white cover) together with
``source/exercises_only.rst`` (a title-less master doc holding only the hidden
toctree). This script sets that env flag, runs the simplepdf builder, and then
copies the result into ``source/downloads/`` so the ``:download:`` link in
``module7/treningsoppgaver.rst`` (which is what gets uploaded to Canvas) always
matches the freshly built PDF.
"""

import os
import shutil
import sys
from pathlib import Path

# Output file name. Must match the :download: target in
# source/module7/treningsoppgaver.rst so the copy below lands on the right file.
PDF_NAME = 'KI-grunnkurs-treningsoppgaver.pdf'

BUILD_DIR = Path('_build/simplepdf-exercises')
# The committed copy that `make html` bundles and update_canvas_pages.py uploads.
DOWNLOADS_PDF = Path('source/downloads') / PDF_NAME


def main():
    print("Building Exercises PDF...")
    result = os.system(
        'EXERCISES_PDF=1 '
        'sphinx-build -c source -b simplepdf source _build/simplepdf-exercises '
        '-D master_doc=exercises_only '
        f'-D simplepdf_file_name={PDF_NAME}'
    )

    pdf_path = BUILD_DIR / PDF_NAME
    if result != 0 or not pdf_path.exists():
        print("\n✗ PDF creation failed")
        sys.exit(1)

    print(f"\n✓ PDF created: {pdf_path}")
    print(f"  Size: {pdf_path.stat().st_size / 1024:.1f} KB")

    # Copy into source/downloads/ so the Canvas :download: link stays in sync.
    DOWNLOADS_PDF.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(pdf_path, DOWNLOADS_PDF)
    print(f"✓ Copied to: {DOWNLOADS_PDF}")
    print("  (this is the copy that make html bundles and update_canvas_pages.py uploads)")


if __name__ == '__main__':
    main()
