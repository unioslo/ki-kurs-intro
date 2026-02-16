#!/bin/bash
# Convert RST course files to a single ODT document

set -e

OUTPUT_DIR="output"
COMBINED_RST="$OUTPUT_DIR/complete_course.rst"
OUTPUT_ODT="$OUTPUT_DIR/Grunnkurs_generativ_KI.odt"

# Create output directory
mkdir -p "$OUTPUT_DIR"

echo "=== Creating combined RST file ==="

# Start with a title page
cat > "$COMBINED_RST" << 'EOF'
=======================================
Grunnkurs i generativ KI
=======================================

:Author: KI-initiativet, Universitetet i Oslo
:Date: 2024
:Organization: IT-avdelingen, Universitetet i Oslo

.. raw:: odt

   <text:p text:style-name="PageBreak"/>

.. contents:: Innholdsfortegnelse
   :depth: 2

.. raw:: odt

   <text:p text:style-name="PageBreak"/>

EOF

# Add index content
echo "" >> "$COMBINED_RST"
cat source/index.rst | grep -v "^.. toctree::" | grep -v ":maxdepth:" | grep -v ":caption:" | grep -v "^   episodes/" >> "$COMBINED_RST"

echo "" >> "$COMBINED_RST"
echo ".. raw:: odt" >> "$COMBINED_RST"
echo "" >> "$COMBINED_RST"
echo "   <text:p text:style-name=\"PageBreak\"/>" >> "$COMBINED_RST"
echo "" >> "$COMBINED_RST"

# Add all episodes in order
for episode in 1 2 3 4 5 6; do
    echo "Adding Episode $episode..."

    # Add episode overview (episode*_0.rst)
    if [ -f "source/episodes/episode${episode}_0.rst" ]; then
        echo "" >> "$COMBINED_RST"
        cat "source/episodes/episode${episode}_0.rst" >> "$COMBINED_RST"
        echo "" >> "$COMBINED_RST"
    fi

    # Add all sub-episodes
    for sub in source/episodes/episode${episode}_*.rst; do
        # Skip the _0 file (already added)
        if [[ "$sub" == *"_0.rst" ]]; then
            continue
        fi

        if [ -f "$sub" ]; then
            echo "" >> "$COMBINED_RST"
            cat "$sub" >> "$COMBINED_RST"
            echo "" >> "$COMBINED_RST"
        fi
    done

    # Add page break between episodes
    echo "" >> "$COMBINED_RST"
    echo ".. raw:: odt" >> "$COMBINED_RST"
    echo "" >> "$COMBINED_RST"
    echo "   <text:p text:style-name=\"PageBreak\"/>" >> "$COMBINED_RST"
    echo "" >> "$COMBINED_RST"
done

echo "✓ Combined RST file created: $COMBINED_RST"

# Check if pandoc is installed
if ! command -v pandoc &> /dev/null; then
    echo ""
    echo "⚠️  pandoc is not installed"
    echo ""
    echo "To convert to ODT, install pandoc:"
    echo "  macOS:   brew install pandoc"
    echo "  Linux:   sudo apt-get install pandoc"
    echo "  Windows: choco install pandoc"
    echo ""
    echo "Or download from: https://pandoc.org/installing.html"
    echo ""
    echo "After installing, run:"
    echo "  pandoc $COMBINED_RST -o $OUTPUT_ODT"
    exit 0
fi

# Convert to ODT using pandoc
echo ""
echo "=== Converting to ODT ==="
pandoc "$COMBINED_RST" \
    -f rst \
    -t odt \
    -o "$OUTPUT_ODT" \
    --toc \
    --toc-depth=2 \
    --standalone

echo "✓ ODT file created: $OUTPUT_ODT"
echo ""
echo "You can now open this file in:"
echo "  - Microsoft Word"
echo "  - LibreOffice Writer"
echo "  - Google Docs (upload the file)"
echo ""

# Also create a DOCX version if requested
read -p "Create DOCX version as well? (y/N) " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    OUTPUT_DOCX="$OUTPUT_DIR/Grunnkurs_generativ_KI.docx"
    echo "=== Converting to DOCX ==="
    pandoc "$COMBINED_RST" \
        -f rst \
        -t docx \
        -o "$OUTPUT_DOCX" \
        --toc \
        --toc-depth=2 \
        --standalone
    echo "✓ DOCX file created: $OUTPUT_DOCX"
fi

echo ""
echo "Done!"
