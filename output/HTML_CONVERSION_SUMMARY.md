# HTML to Editable Formats - Conversion Summary

✓ **Successfully converted all HTML course content to editable formats!**

## Created Files

All files are in the `output/` directory:

### 1. **Grunnkurs_generativ_KI.docx** (43 KB)
- **Best for editing and reviewing**
- Open in Microsoft Word or LibreOffice Writer
- Fully editable - can modify text, formatting, add comments
- Can be converted to PDF from Word (File → Save As → PDF)
- **Recommended for collaborative review**

### 2. **Grunnkurs_generativ_KI.odt** (46 KB)
- **Open document format (editable)**
- Open in LibreOffice Writer, Microsoft Word, or Google Docs
- Fully editable open standard format
- Good for archiving and cross-platform compatibility

### 3. **Grunnkurs_generativ_KI.pdf** (108 KB)
- **Best for final review and distribution**
- Preserves all layout and formatting
- Can be annotated with PDF readers
- Not directly editable (need PDF editor or convert back to DOCX)
- **Recommended for sharing with reviewers**

### 4. **combined_course.html** (106 KB)
- **Source HTML with all styling**
- Can be opened in any web browser
- Preserves all Canvas tabs, UiO icon boxes, and interactive elements
- Can be printed to PDF from browser (Cmd/Ctrl+P → Save as PDF)

## What's Included

All files contain the complete course content:

✓ All 6 episodes with 38 sections
✓ UiO design elements (icon boxes for exercises, notes, tips)
✓ Canvas tabs with content
✓ Collapsible solutions/answers (expanded in documents)
✓ All formatting and styling
✓ Norwegian course content preserved

## How to Use

### For Editing and Review

**Option 1: Microsoft Word (DOCX)**
```bash
open output/Grunnkurs_generativ_KI.docx
```
- Edit content directly
- Add comments and track changes
- Share with colleagues for review
- Export to PDF when final

**Option 2: LibreOffice (ODT or DOCX)**
```bash
open output/Grunnkurs_generativ_KI.odt
# or
open output/Grunnkurs_generativ_KI.docx
```
- Free and open source
- Full editing capabilities
- Can export to many formats

**Option 3: Google Docs**
1. Go to https://docs.google.com
2. Click "New" → "File upload"
3. Upload either the DOCX or ODT file
4. Edit online, share with collaborators

### For Review Only

**PDF (best for distribution)**
```bash
open output/Grunnkurs_generativ_KI.pdf
```
- Read in any PDF viewer
- Add annotations and comments
- Share via email or print
- Professional appearance

**HTML (interactive preview)**
```bash
open output/combined_course.html
```
- View in web browser
- See all interactive elements working
- Print to PDF if needed (Cmd/Ctrl+P)

## Styling Preserved

The converted documents include:

### UiO Icon Boxes
- **Task boxes** (exercises) - blue border
- **Reflection boxes** - gray border
- **Warning boxes** (OBS!) - red border
- **Info boxes** - yellow border
- **Do boxes** (tips) - green border

### Canvas Tabs
- Converted to collapsible sections or separate headings
- All tab content is visible (expanded state)
- Styling preserved with borders and colors

### Typography
- Heading hierarchy maintained (H1, H2, H3)
- Bold and italic formatting preserved
- Lists (bullets and numbered) formatted correctly
- Code blocks and special formatting included

## Regenerating Files

If you make changes to the HTML and want to reconvert:

```bash
# Rebuild HTML from RST
make html

# Convert to all formats
python3 convert_html_to_editable.py
```

Or manually:

```bash
# DOCX
pandoc output/combined_course.html -f html -t docx -o output/Grunnkurs_generativ_KI.docx

# ODT
pandoc output/combined_course.html -f html -t odt -o output/Grunnkurs_generativ_KI.odt

# PDF
python3 -c "from weasyprint import HTML; HTML('output/combined_course.html').write_pdf('output/Grunnkurs_generativ_KI.pdf')"
```

## Comparison with RST Conversion

You also have **complete_course.rst** which was created earlier:

| Format | Source | Best For | Editable |
|--------|--------|----------|----------|
| **DOCX/ODT** (from HTML) | Rendered content | **Editing & Review** | ✓✓✓ |
| **PDF** (from HTML) | Rendered content | Distribution & Reading | ✗ |
| **HTML** | Rendered content | Interactive preview | ✓ (in code editor) |
| **RST** | Source files | Version control, technical editing | ✓ (if you know RST) |

**Recommendation:**
- Use **DOCX** for editing and collaborative review
- Use **PDF** for final distribution and formal review
- Use **HTML** for quick previews and printing
- Use **RST** only if you need to edit source and rebuild

## File Sizes

| File | Size | Pages (approx) |
|------|------|----------------|
| combined_course.html | 106 KB | - |
| Grunnkurs_generativ_KI.docx | 43 KB | ~50-60 pages |
| Grunnkurs_generativ_KI.odt | 46 KB | ~50-60 pages |
| Grunnkurs_generativ_KI.pdf | 108 KB | ~55 pages |

## Next Steps

### For Internal Review
1. Share **Grunnkurs_generativ_KI.docx** with colleagues
2. Use Word's "Track Changes" feature
3. Collect feedback and comments
4. Make edits in the RST source files
5. Rebuild and regenerate documents

### For Publication
1. Finalize content in DOCX
2. Export to PDF from Word (better quality)
3. Or use the generated PDF for distribution
4. Upload to Canvas LMS (use individual HTML pages from _build/html)

### For Archiving
1. Keep **Grunnkurs_generativ_KI.odt** (open standard)
2. Keep **complete_course.rst** (source)
3. Keep PDF for record
4. Store in version control

## Troubleshooting

### Issue: Formatting looks wrong in Word

**Solution:** Try opening in LibreOffice first, then re-save as DOCX

### Issue: Tabs appear as separate sections

**Solution:** This is expected - tabs are expanded to show all content in documents

### Issue: Special characters display incorrectly

**Solution:** Ensure file is opened with UTF-8 encoding

### Issue: Want better PDF quality

**Solution:**
1. Open DOCX in Word
2. File → Export → Create PDF
3. Use "Best for electronic distribution" quality

---

**Generated:** 2026-02-03
**Conversion tool:** `convert_html_to_editable.py`
**Source:** 44 HTML files from _build/html/episodes/
**Total content:** 6 episodes, 38 sections
