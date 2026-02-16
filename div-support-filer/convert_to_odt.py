#!/usr/bin/env python3
"""
Convert all RST course files to a single ODT document.
Alternative to the bash script with better handling of RST syntax.
"""

import os
import subprocess
import sys
from pathlib import Path

def combine_rst_files():
    """Combine all episode RST files into one."""

    output_dir = Path("output")
    output_dir.mkdir(exist_ok=True)

    combined_rst = output_dir / "complete_course.rst"

    print("=== Creating combined RST file ===")

    with open(combined_rst, 'w', encoding='utf-8') as outfile:
        # Title page
        outfile.write("""=======================================
Grunnkurs i generativ KI
=======================================

:Author: KI-initiativet, Universitetet i Oslo
:Date: 2024
:Organization: IT-avdelingen, Universitetet i Oslo

.. contents:: Innholdsfortegnelse
   :depth: 2

----

""")

        # Add index introduction (skip toctree directives)
        index_path = Path("source/index.rst")
        if index_path.exists():
            with open(index_path, 'r', encoding='utf-8') as f:
                for line in f:
                    # Skip sphinx directives that won't work in standalone doc
                    if any(skip in line for skip in ['.. toctree::', ':maxdepth:',
                                                       ':caption:', '   episodes/']):
                        continue
                    outfile.write(line)
            outfile.write("\n\n----\n\n")

        # Add all episodes in order
        for episode in range(1, 7):  # Episodes 1-6
            print(f"Adding Episode {episode}...")

            # Add overview file (episode*_0.rst)
            overview_file = Path(f"source/episodes/episode{episode}_0.rst")
            if overview_file.exists():
                outfile.write("\n")
                with open(overview_file, 'r', encoding='utf-8') as f:
                    outfile.write(f.read())
                outfile.write("\n\n")

            # Add all sub-episodes
            episode_files = sorted(Path("source/episodes").glob(f"episode{episode}_*.rst"))
            for episode_file in episode_files:
                # Skip the overview file (already added)
                if episode_file.name.endswith("_0.rst"):
                    continue

                outfile.write("\n")
                with open(episode_file, 'r', encoding='utf-8') as f:
                    outfile.write(f.read())
                outfile.write("\n\n")

            # Add separator between episodes
            outfile.write("----\n\n")

    print(f"✓ Combined RST file created: {combined_rst}")
    return combined_rst

def convert_with_pandoc(rst_file):
    """Convert RST to ODT using pandoc."""

    # Check if pandoc is installed
    try:
        subprocess.run(['pandoc', '--version'],
                      capture_output=True, check=True)
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("\n⚠️  pandoc is not installed")
        print("\nTo convert to ODT, install pandoc:")
        print("  macOS:   brew install pandoc")
        print("  Linux:   sudo apt-get install pandoc")
        print("  Windows: choco install pandoc")
        print("\nOr download from: https://pandoc.org/installing.html")
        print(f"\nAfter installing, run:")
        print(f"  pandoc {rst_file} -f rst -t odt -o output/Grunnkurs_generativ_KI.odt")
        return False

    # Convert to ODT
    output_odt = Path("output/Grunnkurs_generativ_KI.odt")
    print("\n=== Converting to ODT ===")

    cmd = [
        'pandoc',
        str(rst_file),
        '-f', 'rst',
        '-t', 'odt',
        '-o', str(output_odt),
        '--toc',
        '--toc-depth=2',
        '--standalone'
    ]

    try:
        subprocess.run(cmd, check=True)
        print(f"✓ ODT file created: {output_odt}")
        print(f"\nFile size: {output_odt.stat().st_size / 1024:.1f} KB")
        print("\nYou can now open this file in:")
        print("  - Microsoft Word")
        print("  - LibreOffice Writer")
        print("  - Google Docs (upload the file)")

        # Offer to create DOCX as well
        response = input("\nCreate DOCX version as well? (y/N) ").strip().lower()
        if response == 'y':
            output_docx = Path("output/Grunnkurs_generativ_KI.docx")
            print("\n=== Converting to DOCX ===")
            cmd_docx = [
                'pandoc',
                str(rst_file),
                '-f', 'rst',
                '-t', 'docx',
                '-o', str(output_docx),
                '--toc',
                '--toc-depth=2',
                '--standalone'
            ]
            subprocess.run(cmd_docx, check=True)
            print(f"✓ DOCX file created: {output_docx}")
            print(f"File size: {output_docx.stat().st_size / 1024:.1f} KB")

        return True

    except subprocess.CalledProcessError as e:
        print(f"Error during conversion: {e}")
        return False

def main():
    """Main conversion workflow."""

    # Check we're in the right directory
    if not Path("source/episodes").exists():
        print("Error: Must run from ki-kurs-intro directory")
        sys.exit(1)

    # Combine all RST files
    combined_rst = combine_rst_files()

    # Convert to ODT
    success = convert_with_pandoc(combined_rst)

    if success:
        print("\n✓ Conversion complete!")
    else:
        print(f"\n✓ Combined RST file is ready at: {combined_rst}")
        print("Install pandoc to convert to ODT/DOCX")

if __name__ == '__main__':
    main()
