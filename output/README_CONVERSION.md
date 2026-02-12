# Converting Course to ODT/DOCX Format

The complete course content has been combined into a single RST file: **complete_course.rst** (68 KB)

This file contains all 6 episodes with 38 sections in the correct order.

## Quick Start

### Option 1: Using Pandoc (Recommended)

**Install pandoc:**
```bash
# macOS
brew install pandoc

# Linux (Debian/Ubuntu)
sudo apt-get install pandoc

# Windows
choco install pandoc
```

Or download from: https://pandoc.org/installing.html

**Convert to ODT:**
```bash
pandoc complete_course.rst -f rst -t odt -o Grunnkurs_generativ_KI.odt --toc --standalone
```

**Convert to DOCX:**
```bash
pandoc complete_course.rst -f rst -t docx -o Grunnkurs_generativ_KI.docx --toc --standalone
```

### Option 2: Using the Conversion Scripts

From the project root directory:

```bash
# Python script (recommended)
python3 convert_to_odt.py

# Or bash script
./convert_to_odt.sh
```

Both scripts will:
1. Create the combined RST file (already done)
2. Check for pandoc installation
3. Convert to ODT format
4. Optionally convert to DOCX format

### Option 3: Manual Conversion via Sphinx

If you prefer to use Sphinx's built-in converters:

```bash
# Install sphinx with ODT support
pip install sphinx odfpy

# Convert using rst2odt (part of docutils)
rst2odt.py complete_course.rst Grunnkurs_generativ_KI.odt
```

### Option 4: Online Conversion

If you don't want to install anything:

1. Upload **complete_course.rst** to an online converter:
   - https://cloudconvert.com/rst-to-odt
   - https://convertio.co/rst-odt/

2. Or convert to HTML first, then to ODT:
   - https://pandoc.org/try/ (online pandoc)

## What's Included

The combined RST file contains:

- **Title page** with course information
- **Table of contents** (automatically generated)
- **All 6 episodes:**
  1. Hva er KI og generativ KI? (5 sections)
  2. Hvordan fungerer LLM-er egentlig? (6 sections)
  3. Kvalitetssikring og ansvarlig bruk (5 sections)
  4. UiOs KI-tjenester (7 sections)
  5. Grunnleggende prompt engineering (8 sections)
  6. Oppsummering og veien videre (7 sections)

Total: **38 sections** across 6 episodes

## File Structure

The complete_course.rst file is structured as:

```
Title Page
----------
Table of Contents
Introduction (from index.rst)

Episode 1: Hva er KI og generativ KI?
  - Oversikt
  - Hva er kunstig intelligens?
  - Hva er generativ KI?
  - [... all sections ...]

Episode 2: Hvordan fungerer LLM-er egentlig?
  - [... all sections ...]

[Episodes 3-6...]
```

## Customizing the Output

### Add custom styling

For better-looking output, you can create a reference document:

```bash
# Create a reference document with your preferred styles
pandoc complete_course.rst -o reference.odt

# Edit reference.odt in LibreOffice/Word to set your styles
# (headings, fonts, colors, margins)

# Use it as a template for conversion
pandoc complete_course.rst -f rst -t odt -o Grunnkurs_generativ_KI.odt \
  --reference-doc=reference.odt --toc --standalone
```

### Adjust table of contents depth

```bash
# Include only level 1 and 2 headings in TOC
pandoc complete_course.rst -f rst -t odt -o output.odt --toc --toc-depth=2

# Include all heading levels
pandoc complete_course.rst -f rst -t odt -o output.odt --toc --toc-depth=3
```

### Add metadata

Edit the top of complete_course.rst to customize:
```rst
:Author: Your Name
:Date: 2024-02-03
:Organization: Universitetet i Oslo
:Version: 1.0
```

## Troubleshooting

### Issue: Tables or formatting look wrong

**Solution:** RST to ODT conversion can sometimes lose formatting. Try:

1. Convert to DOCX instead (better support):
   ```bash
   pandoc complete_course.rst -f rst -t docx -o output.docx --toc
   ```

2. Or convert to HTML first, then open in Word/LibreOffice:
   ```bash
   pandoc complete_course.rst -f rst -t html -o output.html --standalone
   ```

### Issue: Canvas tabs don't convert well

**Solution:** The `.. canvas-tabs::` directives are Sphinx-specific and won't convert directly.

The combined RST file already includes the tab content in a readable format. If needed, edit complete_course.rst to adjust how tabs are presented in the printed version.

### Issue: Special characters display incorrectly

**Solution:** Ensure UTF-8 encoding:
```bash
pandoc complete_course.rst -f rst -t odt -o output.odt --standalone --metadata charset=UTF-8
```

## Next Steps

Once you have the ODT/DOCX file:

1. **Review and edit** in LibreOffice Writer or Microsoft Word
2. **Adjust styling** (fonts, colors, spacing)
3. **Add images** if needed
4. **Export to PDF** for final distribution:
   - LibreOffice: File → Export as PDF
   - Word: File → Save As → PDF

## Additional Formats

Pandoc can convert to many formats:

```bash
# PDF (requires LaTeX)
pandoc complete_course.rst -f rst -o output.pdf --toc

# EPUB (e-book)
pandoc complete_course.rst -f rst -o output.epub --toc

# HTML (single page)
pandoc complete_course.rst -f rst -o output.html --standalone --toc

# LaTeX
pandoc complete_course.rst -f rst -o output.tex
```

## Questions?

- **Pandoc documentation:** https://pandoc.org/MANUAL.html
- **RST syntax reference:** https://docutils.sourceforge.io/rst.html
- **ODT specification:** https://en.wikipedia.org/wiki/OpenDocument

---

**Generated:** 2024-02-03
**Total content:** 68 KB combined RST file from 44 source files
