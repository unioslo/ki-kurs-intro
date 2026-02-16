#!/usr/bin/env python3
"""
Convert HTML course files to editable formats (DOCX, ODT, PDF).
This preserves the actual rendered content with styling.
"""

import subprocess
import sys
from pathlib import Path
from bs4 import BeautifulSoup
import shutil

def check_dependencies():
    """Check for required tools."""
    tools = {
        'pandoc': False,
        'wkhtmltopdf': False,
        'weasyprint': False
    }

    # Check pandoc
    try:
        subprocess.run(['pandoc', '--version'], capture_output=True, check=True)
        tools['pandoc'] = True
    except (subprocess.CalledProcessError, FileNotFoundError):
        pass

    # Check wkhtmltopdf
    try:
        subprocess.run(['wkhtmltopdf', '--version'], capture_output=True, check=True)
        tools['wkhtmltopdf'] = True
    except (subprocess.CalledProcessError, FileNotFoundError):
        pass

    # Check weasyprint
    try:
        import weasyprint
        tools['weasyprint'] = True
    except ImportError:
        pass

    return tools

def extract_html_content(html_file):
    """Extract the main content from an HTML file."""
    with open(html_file, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')

    # Find the main content div
    content = soup.find('div', {'itemprop': 'articleBody'})
    if content:
        return str(content)

    # Fallback to whole document
    return soup.prettify()

def create_combined_html():
    """Create a single HTML file with all episodes."""

    html_dir = Path("_build/html/episodes")
    output_dir = Path("output")
    output_dir.mkdir(exist_ok=True)

    combined_html_file = output_dir / "combined_course.html"

    print("=== Creating combined HTML file ===")

    # Read the CSS from _static/custom.css
    custom_css = ""
    css_file = Path("_build/html/_static/custom.css")
    if css_file.exists():
        with open(css_file, 'r', encoding='utf-8') as f:
            custom_css = f.read()

    # Start HTML document
    html_parts = [
        '<!DOCTYPE html>',
        '<html lang="no">',
        '<head>',
        '<meta charset="utf-8">',
        '<title>Grunnkurs i generativ KI</title>',
        '<style>',
        '''
        body {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
            line-height: 1.6;
            max-width: 1000px;
            margin: 0 auto;
            padding: 20px;
            color: #333;
        }
        h1 {
            color: #2c3e50;
            border-bottom: 3px solid #3498db;
            padding-bottom: 10px;
            page-break-after: avoid;
        }
        h2 {
            color: #34495e;
            margin-top: 30px;
            page-break-after: avoid;
        }
        h3 {
            color: #7f8c8d;
            page-break-after: avoid;
        }
        .episode {
            page-break-before: always;
            margin-bottom: 50px;
        }
        .episode:first-child {
            page-break-before: auto;
        }

        /* UiO icon boxes */
        .uio-icon-box {
            border-left: 4px solid #ddd;
            padding: 15px 20px;
            margin: 20px 0;
            background-color: #f8f9fa;
            page-break-inside: avoid;
        }
        .uio-icon-box.task { border-left-color: #2c5aa0; }
        .uio-icon-box.reflect { border-left-color: #6c757d; }
        .uio-icon-box.dont { border-left-color: #dc3545; }
        .uio-icon-box.source { border-left-color: #17a2b8; }
        .uio-icon-box.do { border-left-color: #28a745; }
        .uio-icon-box.info { border-left-color: #ffc107; }

        /* Canvas tabs */
        .enhanceable_content.tabs {
            margin: 20px 0;
            border: 1px solid #dee2e6;
            border-radius: 5px;
            page-break-inside: avoid;
        }
        .enhanceable_content.tabs ul {
            list-style: none;
            padding: 0;
            margin: 0;
            display: flex;
            border-bottom: 2px solid #0066cc;
            background-color: #f8f9fa;
        }
        .enhanceable_content.tabs ul li {
            margin: 0;
        }
        .enhanceable_content.tabs ul li a {
            display: block;
            padding: 10px 20px;
            text-decoration: none;
            color: #495057;
            font-weight: bold;
            border-right: 1px solid #dee2e6;
        }
        .enhanceable_content.tabs ul li:first-child a {
            background-color: white;
            color: #0066cc;
        }
        .enhanceable_content.tabs > div {
            padding: 20px;
            background-color: white;
        }

        /* Details/Summary (accordions) */
        details {
            margin: 15px 0;
            border: 1px solid #dee2e6;
            border-radius: 5px;
            padding: 10px;
            page-break-inside: avoid;
        }
        summary {
            cursor: pointer;
            font-weight: bold;
            color: #28a745;
            padding: 5px;
        }
        summary:hover {
            background-color: #f8f9fa;
        }

        /* Lists */
        ul, ol {
            margin: 10px 0;
            padding-left: 30px;
        }
        li {
            margin: 5px 0;
        }

        /* Tables */
        table {
            border-collapse: collapse;
            width: 100%;
            margin: 20px 0;
        }
        th, td {
            border: 1px solid #dee2e6;
            padding: 8px 12px;
            text-align: left;
        }
        th {
            background-color: #f8f9fa;
            font-weight: bold;
        }

        /* Print/PDF specific */
        @media print {
            body { max-width: 100%; }
            .episode { page-break-before: always; }
            a { color: #0066cc; text-decoration: none; }
        }
        ''',
        custom_css,
        '</style>',
        '</head>',
        '<body>',
        '<h1 style="text-align: center; font-size: 2.5em; margin-bottom: 10px;">Grunnkurs i generativ KI</h1>',
        '<p style="text-align: center; color: #7f8c8d; margin-bottom: 50px;">IT-avdelingen, Universitetet i Oslo</p>',
        '<hr style="margin-bottom: 50px;">',
    ]

    # Add all episodes
    for episode in range(1, 7):
        print(f"Adding Episode {episode}...")

        # Find all files for this episode
        episode_files = sorted(html_dir.glob(f"episode{episode}_*.html"))

        if episode_files:
            html_parts.append(f'<div class="episode" id="episode{episode}">')

            for html_file in episode_files:
                content = extract_html_content(html_file)
                html_parts.append(content)

            html_parts.append('</div>')

    # Close HTML
    html_parts.extend([
        '</body>',
        '</html>'
    ])

    # Write combined HTML
    with open(combined_html_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(html_parts))

    print(f"✓ Combined HTML created: {combined_html_file}")
    print(f"  Size: {combined_html_file.stat().st_size / 1024:.1f} KB")

    return combined_html_file

def convert_to_docx(html_file, tools):
    """Convert HTML to DOCX using pandoc."""

    if not tools['pandoc']:
        print("\n⚠️  pandoc not available for DOCX conversion")
        return None

    output_file = Path("output/Grunnkurs_generativ_KI.docx")
    print(f"\n=== Converting to DOCX ===")

    cmd = [
        'pandoc',
        str(html_file),
        '-f', 'html',
        '-t', 'docx',
        '-o', str(output_file),
        '--standalone',
        '--metadata', 'title=Grunnkurs i generativ KI'
    ]

    try:
        subprocess.run(cmd, check=True)
        print(f"✓ DOCX created: {output_file}")
        print(f"  Size: {output_file.stat().st_size / 1024:.1f} KB")
        return output_file
    except subprocess.CalledProcessError as e:
        print(f"Error creating DOCX: {e}")
        return None

def convert_to_odt(html_file, tools):
    """Convert HTML to ODT using pandoc."""

    if not tools['pandoc']:
        print("\n⚠️  pandoc not available for ODT conversion")
        return None

    output_file = Path("output/Grunnkurs_generativ_KI.odt")
    print(f"\n=== Converting to ODT ===")

    cmd = [
        'pandoc',
        str(html_file),
        '-f', 'html',
        '-t', 'odt',
        '-o', str(output_file),
        '--standalone',
        '--metadata', 'title=Grunnkurs i generativ KI'
    ]

    try:
        subprocess.run(cmd, check=True)
        print(f"✓ ODT created: {output_file}")
        print(f"  Size: {output_file.stat().st_size / 1024:.1f} KB")
        return output_file
    except subprocess.CalledProcessError as e:
        print(f"Error creating ODT: {e}")
        return None

def convert_to_pdf_weasyprint(html_file):
    """Convert HTML to PDF using weasyprint."""

    try:
        from weasyprint import HTML
    except ImportError:
        print("\n⚠️  weasyprint not available")
        return None

    output_file = Path("output/Grunnkurs_generativ_KI.pdf")
    print(f"\n=== Converting to PDF (weasyprint) ===")

    try:
        HTML(filename=str(html_file)).write_pdf(str(output_file))
        print(f"✓ PDF created: {output_file}")
        print(f"  Size: {output_file.stat().st_size / 1024:.1f} KB")
        return output_file
    except Exception as e:
        print(f"Error creating PDF: {e}")
        return None

def convert_to_pdf_wkhtmltopdf(html_file, tools):
    """Convert HTML to PDF using wkhtmltopdf."""

    if not tools['wkhtmltopdf']:
        print("\n⚠️  wkhtmltopdf not available")
        return None

    output_file = Path("output/Grunnkurs_generativ_KI.pdf")
    print(f"\n=== Converting to PDF (wkhtmltopdf) ===")

    cmd = [
        'wkhtmltopdf',
        '--enable-local-file-access',
        '--print-media-type',
        '--no-background',
        str(html_file),
        str(output_file)
    ]

    try:
        subprocess.run(cmd, check=True, capture_output=True)
        print(f"✓ PDF created: {output_file}")
        print(f"  Size: {output_file.stat().st_size / 1024:.1f} KB")
        return output_file
    except subprocess.CalledProcessError as e:
        print(f"Error creating PDF: {e}")
        return None

def main():
    """Main conversion workflow."""

    # Check we're in the right directory
    if not Path("_build/html/episodes").exists():
        print("Error: HTML files not found. Run 'make html' first.")
        sys.exit(1)

    # Check available tools
    print("Checking available conversion tools...")
    tools = check_dependencies()

    print(f"  pandoc: {'✓' if tools['pandoc'] else '✗'}")
    print(f"  wkhtmltopdf: {'✓' if tools['wkhtmltopdf'] else '✗'}")
    print(f"  weasyprint: {'✓' if tools['weasyprint'] else '✗'}")
    print()

    # Create combined HTML
    html_file = create_combined_html()

    # Convert to requested formats
    created_files = []

    # DOCX (most editable)
    docx_file = convert_to_docx(html_file, tools)
    if docx_file:
        created_files.append(('DOCX (editable)', docx_file))

    # ODT (open standard, editable)
    odt_file = convert_to_odt(html_file, tools)
    if odt_file:
        created_files.append(('ODT (editable)', odt_file))

    # PDF (best for review, not editable)
    pdf_file = None
    if tools['weasyprint']:
        pdf_file = convert_to_pdf_weasyprint(html_file)
    elif tools['wkhtmltopdf']:
        pdf_file = convert_to_pdf_wkhtmltopdf(html_file, tools)

    if pdf_file:
        created_files.append(('PDF (read-only)', pdf_file))

    # Summary
    print("\n" + "="*60)
    print("CONVERSION COMPLETE")
    print("="*60)

    if created_files:
        print("\nCreated files:")
        for desc, filepath in created_files:
            print(f"  ✓ {desc}: {filepath}")
    else:
        print("\n⚠️  No files created. Install conversion tools:")
        print("\nFor DOCX/ODT (most editable):")
        print("  brew install pandoc")
        print("\nFor PDF:")
        print("  pip3 install weasyprint")
        print("  OR: brew install wkhtmltopdf")

    print(f"\nSource HTML available at: {html_file}")

    print("\n" + "="*60)
    print("RECOMMENDATIONS:")
    print("="*60)
    print("✓ DOCX - Best for editing and reviewing content")
    print("✓ ODT  - Open format, editable in LibreOffice/Word")
    print("✓ PDF  - Best for final review, preserves layout")
    print("✓ HTML - Can be opened in browser for preview")

if __name__ == '__main__':
    main()
