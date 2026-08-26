#!/usr/bin/env python3
"""
Generate the chapter icons for the course front page ("Kapitler" box).

Each icon is a wide rounded bar in the chapter's colour: the chapter NUMBER on
the left and the chapter TITLE beside it (word-wrapped), both vertically centred.
On the front page the bars are stacked full-width and the whole bar is clickable.
The SVGs reuse the Lato font that Canvas' Icon-Maker embedded in the original
icons (extracted once to icon_assets/lato-extended.svgstyle), so the text renders
correctly even when Canvas shows the SVG as an <img>.

SINGLE SOURCE OF TRUTH: the chapters are read straight from the
``uio-chapter-card`` entries in source/forside.rst. Each card supplies the
title, the icon filename and the icon colour (``:icon_color:``); the chapter
NUMBER baked into the icon is the card's position in the "Kapitler" listing.
Change a card's title / colour / filename (or reorder them) and the icons
regenerate to match — there is no separate chapter table to keep in sync.

WORKFLOW (all local, no Canvas web UI):
    1. Edit the uio-chapter-card entries in source/forside.rst.
    2. python build_icons.py                # regenerate source/_static/icons/ikon*.svg
    3. Open one in a browser to eyeball it.
    4. python update_canvas_pages.py --upload-icons     # push them to Canvas
    5. python update_canvas_pages.py --front-page       # rebuild the front page

``update_canvas_pages.py`` calls parse_chapters()/generate_icons() from here so
that --front-page and --upload-icons always regenerate the icons first.

Tweak the SIZE / FONT constants below to taste.
"""

import re
from pathlib import Path
from xml.sax.saxutils import escape

# --- Locations -------------------------------------------------------------
ICON_DIR = Path(__file__).parent / "source" / "_static" / "icons"
FONT_STYLE_FILE = Path(__file__).parent / "icon_assets" / "lato-extended.svgstyle"
FRONT_PAGE_RST = Path(__file__).parent / "source" / "forside.rst"

DEFAULT_COLOR = "#7ED321"   # fallback if a card omits :icon_color:

# --- Bar size / layout (px) ------------------------------------------------
# A 5:1 bar sized to fill the 1/4-width "Kapitler" column (card uses
# width:100%). These are the intrinsic/reference dimensions; the icon scales to
# the column, so the on-screen bar height and text size are HEIGHT /
# NUMBER_SIZE / TITLE_SIZE * (column / WIDTH). Narrowing the column therefore
# shrinks the bar and its text: these constants are sized for a ~1/4-page column
# (~270px), which lands the number near 1.3x and the title near 1.05x the ~16px
# body font.
WIDTH = 400
HEIGHT = 80
CORNER_RADIUS = 10
PADDING_RIGHT = 16      # right-hand padding used for title word wrapping

NUMBER_SIZE = 30        # chapter-number font size (~1.3x body when column-filled)
NUMBER_CENTER_X = 32    # horizontal centre of the number column (left of title)
NUMBER_BASELINE = 51    # y baseline for the number (vertically centred)

TITLE_SIZE = 25         # chapter-title font size (~1.05x body when column-filled)
TITLE_X = 62            # left edge of the title (to the right of the number)
TITLE_LINE_HEIGHT = 30  # vertical distance between wrapped title lines
TITLE_BLOCK_CENTER = 47 # vertical centre (baseline) of the title block

TEXT_COLOR = "#FFFFFF"
FONT_FAMILY = "Lato Extended"
# Rough average glyph advance as a fraction of font size for Lato bold; used to
# estimate how many characters fit per line (no font-metrics dependency).
CHAR_WIDTH_FACTOR = 0.52

_CARD_RE = re.compile(r'^\s*\.\.\s+uio-chapter-card::')
_OPTION_RE = re.compile(r'^\s*:(\w+):\s*(.*)$')


def parse_chapters(rst_path=FRONT_PAGE_RST):
    """
    Read the chapter definitions from the uio-chapter-card entries in forside.rst.

    Returns a list of dicts: {number, title, icon_filename, icon_color, url}.
    The NUMBER is the card's 1-based position in the file (== chapter number).
    forside.rst is the single source of truth; the icons are generated to match.
    """
    text = Path(rst_path).read_text(encoding="utf-8")
    chapters = []
    current = None

    def flush():
        if current is not None:
            current['number'] = len(chapters) + 1
            chapters.append(current)

    for raw in text.splitlines():
        if _CARD_RE.match(raw):
            flush()
            current = {'number': 0, 'title': '', 'icon_filename': '',
                       'icon_color': '', 'url': ''}
            continue
        if current is None:
            continue
        m = _OPTION_RE.match(raw)
        if m:
            key, val = m.group(1), m.group(2).strip()
            if key in current:
                current[key] = val
        elif raw.strip() and not raw.lstrip().startswith(':'):
            # A non-option content line ends the current card's option block.
            # (Cards are option-only, so this just guards against stray text.)
            pass
    flush()

    for ch in chapters:
        if not ch['icon_color']:
            ch['icon_color'] = DEFAULT_COLOR
    return chapters


def wrap_title(title, max_width, font_size):
    """Greedy word-wrap by estimated pixel width (no font-metrics dependency)."""
    max_chars = max(1, int(max_width / (CHAR_WIDTH_FACTOR * font_size)))
    words = title.split()
    lines, current = [], ""
    for word in words:
        candidate = f"{current} {word}".strip()
        if len(candidate) <= max_chars or not current:
            current = candidate
        else:
            lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


def build_svg(number, color, title, font_style):
    """Return the SVG markup for one chapter bar (number left, title beside it)."""
    usable_width = WIDTH - TITLE_X - PADDING_RIGHT
    lines = wrap_title(title, usable_width, TITLE_SIZE)

    # Vertically centre the wrapped title block around TITLE_BLOCK_CENTER, and
    # left-align it (text-anchor="start") beside the number.
    total_height = (len(lines) - 1) * TITLE_LINE_HEIGHT
    first_baseline = TITLE_BLOCK_CENTER - total_height / 2

    tspans = []
    for i, line in enumerate(lines):
        dy = 0 if i == 0 else TITLE_LINE_HEIGHT
        tspans.append(f'<tspan x="{TITLE_X:g}" dy="{dy:g}">{escape(line)}</tspan>')
    tspans_markup = "".join(tspans)

    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" fill="none" '
        f'width="{WIDTH}px" height="{HEIGHT}px" viewBox="0 0 {WIDTH} {HEIGHT}">'
        f'<rect x="0" y="0" width="{WIDTH}" height="{HEIGHT}" rx="{CORNER_RADIUS}" fill="{color}"></rect>'
        f'<text x="{NUMBER_CENTER_X:g}" y="{NUMBER_BASELINE:g}" fill="{TEXT_COLOR}" '
        f'font-family="{FONT_FAMILY}" font-weight="bold" font-size="{NUMBER_SIZE}" '
        f'text-anchor="middle">{number}</text>'
        f'<text x="{TITLE_X:g}" y="{first_baseline:g}" fill="{TEXT_COLOR}" '
        f'font-family="{FONT_FAMILY}" font-weight="bold" font-size="{TITLE_SIZE}" '
        f'text-anchor="start">{tspans_markup}</text>'
        f'{font_style}'
        f'</svg>'
    )


def generate_icons(rst_path=FRONT_PAGE_RST, icon_dir=ICON_DIR, verbose=True):
    """
    Regenerate every chapter icon from the cards in forside.rst so the baked
    number / title / colour always match the front page. Returns the list of
    written Path objects.
    """
    if not FONT_STYLE_FILE.exists():
        raise SystemExit(
            f"Font style not found: {FONT_STYLE_FILE}\n"
            "Extract it once from an original Icon-Maker SVG, e.g.:\n"
            "  python3 -c \"import re,pathlib; "
            "s=pathlib.Path('source/_static/icons/ikon1.svg').read_text(); "
            "pathlib.Path('icon_assets/lato-extended.svgstyle').write_text("
            "re.search(r'<style.*?</style>', s, re.DOTALL).group(0))\""
        )

    chapters = parse_chapters(rst_path)
    if not chapters:
        raise SystemExit(f"No uio-chapter-card entries found in {rst_path}")

    font_style = FONT_STYLE_FILE.read_text(encoding="utf-8")
    icon_dir = Path(icon_dir)
    icon_dir.mkdir(parents=True, exist_ok=True)

    written = []
    for ch in chapters:
        filename = ch['icon_filename']
        if not filename:
            if verbose:
                print(f"Skipping chapter {ch['number']} (\"{ch['title']}\"): "
                      "no :icon_filename:")
            continue
        svg = build_svg(ch['number'], ch['icon_color'], ch['title'], font_style)
        out = icon_dir / filename
        out.write_text(svg, encoding="utf-8")
        written.append(out)
        if verbose:
            print(f"Wrote {out}  (nr {ch['number']}, {ch['icon_color']}, "
                  f"\"{ch['title']}\")")
    return written


def main():
    written = generate_icons()
    print(f"\nDone: {len(written)} icon(s) in {ICON_DIR}")
    print("Preview one in a browser, then upload with:")
    print("  python update_canvas_pages.py --upload-icons")


if __name__ == "__main__":
    main()
