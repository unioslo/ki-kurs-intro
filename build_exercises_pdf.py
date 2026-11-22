#!/usr/bin/env python3
"""Build the Exercises (Treningsoppgaver) PDF.

Supports Norwegian (default) and English builds, plus optional Set 1 / Set 2
only PDFs.

The exercises PDF is produced with:
  - no table of contents
  - no standalone title page
  - no "Version ..." subtitle on the cover
  - no page numbers

These are all driven by the ``EXERCISES_PDF`` branch in ``source/conf.py``
(which swaps in ``simplepdf-no-pagenumbers.css`` and a white cover) together with
title-less master docs (``exercises_only.rst``, ``exercises_set1_only.rst``,
``exercises_set2_only.rst``). This script sets that env flag, runs the simplepdf
builder, and then copies the result into ``source/downloads/`` so the
``:download:`` link in ``module6/treningsoppgaver.rst`` always matches the
freshly built PDF.
"""

import argparse
import os
import shutil
import sys
from pathlib import Path

BUILD_DIR = Path('_build/simplepdf-exercises')
DOWNLOADS_DIR = Path('source/downloads')

# Build configurations: (master_doc, filename, project_name)
CONFIGS = {
    ('no', None):     ('exercises_only',     'KI-grunnkurs-treningsoppgaver.pdf',       'Treningsoppgaver'),
    ('en', None):     ('exercises_only',     'AI-foundation-course-exercises.pdf',      'Exercises'),
    ('no', 'set1'):   ('exercises_set1_only', 'KI-grunnkurs-treningsoppgaver-sett-1.pdf', 'Treningsoppgaver — Sett 1'),
    ('en', 'set1'):   ('exercises_set1_only', 'AI-foundation-course-exercises-set1.pdf',  'Exercises — Set 1'),
    ('no', 'set2'):   ('exercises_set2_only', 'KI-grunnkurs-treningsoppgaver-sett-2.pdf', 'Treningsoppgaver — Sett 2'),
    ('en', 'set2'):   ('exercises_set2_only', 'AI-foundation-course-exercises-set2.pdf',  'Exercises — Set 2'),
}


def build(language, exercise_set=None):
    key = (language, exercise_set)
    if key not in CONFIGS:
        print(f"Unsupported combination: language={language}, set={exercise_set}")
        sys.exit(1)

    master_doc, filename, project = CONFIGS[key]
    build_dir = BUILD_DIR
    if language == 'en':
        build_dir = Path('_build/simplepdf-exercises-en')
    if exercise_set:
        build_dir = Path(f'_build/simplepdf-exercises-{language}-{exercise_set}')

    label = f"{'English' if language == 'en' else 'Norwegian'}"
    if exercise_set:
        label += f" {exercise_set.upper()}"
    label += " exercises PDF"

    print(f"Building {label}...")
    cmd = (
        f'EXERCISES_PDF=1 '
        f'sphinx-build -c source -b simplepdf source {build_dir} '
        f'-D master_doc={master_doc} '
        f'-D simplepdf_file_name={filename} '
        f'-D project="{project}" '
    )
    if language == 'en':
        cmd += '-D language=en '

    result = os.system(cmd)

    pdf_path = build_dir / filename
    if result != 0 or not pdf_path.exists():
        print("\n✗ PDF creation failed")
        sys.exit(1)

    print(f"\n✓ PDF created: {pdf_path}")
    print(f"  Size: {pdf_path.stat().st_size / 1024:.1f} KB")

    # Copy into source/downloads/ so the Canvas :download: link stays in sync.
    DOWNLOADS_DIR.mkdir(parents=True, exist_ok=True)
    downloads_pdf = DOWNLOADS_DIR / filename
    shutil.copy2(pdf_path, downloads_pdf)
    print(f"✓ Copied to: {downloads_pdf}")
    print("  (this is the copy that make html bundles and update_canvas_pages.py uploads)")

    return pdf_path


def main():
    parser = argparse.ArgumentParser(description="Build exercise PDFs")
    parser.add_argument(
        '--english', action='store_true',
        help='Build English version (default: Norwegian)'
    )
    parser.add_argument(
        '--set1', action='store_true',
        help='Build only Set 1'
    )
    parser.add_argument(
        '--set2', action='store_true',
        help='Build only Set 2'
    )
    parser.add_argument(
        '--all', action='store_true',
        help='Build all variants (NO full, EN full, EN set1, EN set2)'
    )
    args = parser.parse_args()

    if args.all:
        build('no', None)
        print()
        build('en', None)
        print()
        build('en', 'set1')
        print()
        build('en', 'set2')
        return

    lang = 'en' if args.english else 'no'
    exercise_set = None
    if args.set1:
        exercise_set = 'set1'
    elif args.set2:
        exercise_set = 'set2'

    build(lang, exercise_set)


if __name__ == '__main__':
    main()
