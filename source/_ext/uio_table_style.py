"""
Inline styling of `:class: uio-table` tables.

Canvas does not load the stylesheets in source/_static/, so a plain
`.. list-table::` ends up without grid lines and row colours in the published
pages. This extension rewrites the generated HTML and puts the styling in
`style` attributes on table/th/td, which Canvas keeps. The same styling is
therefore used both in `make html` and in the pages uploaded by
update_canvas_pages.py - the RST source stays a normal list-table.

Usage in RST:

    .. list-table::
       :header-rows: 1
       :widths: 16 34 18 32
       :class: uio-table

Tweak the constants below to change the look of every uio-table at once.
"""

from bs4 import BeautifulSoup

# Soft greyscale - the course pages already carry plenty of colour (reflect/
# colorbox borders and the red/yellow/green/black dataklasse dots), so the
# table stays neutral: pale header, thin light grid, roomy cells.
# Set ROW_BG_EVEN to '#ffffff' to turn the row striping off completely.
HEADER_BG = '#f5f5f5'
HEADER_FG = '#1a1a1a'
HEADER_RULE = '1px solid #d9d9d9'
BORDER = '1px solid #e3e3e3'
ROW_BG_ODD = '#ffffff'
ROW_BG_EVEN = '#fafafa'
CELL_PADDING = '14px 16px'

TABLE_STYLE = (
    f'width:100%; border-collapse:collapse; table-layout:fixed; '
    f'border:{BORDER}; margin-bottom:1.5em; line-height:1.5;'
)
HEADER_ROW_STYLE = f'background-color:{HEADER_BG}; color:{HEADER_FG};'
HEADER_CELL_STYLE = (
    f'border:{BORDER}; border-bottom:{HEADER_RULE}; padding:{CELL_PADDING}; '
    f'text-align:left; vertical-align:middle; white-space:normal; '
    f'overflow-wrap:break-word; background-color:{HEADER_BG}; '
    f'color:{HEADER_FG}; font-weight:bold;'
)
CELL_STYLE = (
    f'border:{BORDER}; padding:{CELL_PADDING}; text-align:left; '
    f'vertical-align:middle; white-space:normal; overflow-wrap:break-word;'
)


def _add_style(tag, style):
    """Prepend `style` to the tag's existing style attribute (existing wins)."""
    existing = tag.get('style', '').strip()
    tag['style'] = f'{style} {existing}'.strip() if existing else style


def _style_cell(cell, style):
    _add_style(cell, style)
    # docutils wraps cell text in <p>; without this the default paragraph
    # margins give uneven space above/below the text in Canvas.
    for para in cell.find_all('p'):
        _add_style(para, 'margin:0;')


def _style_table(table):
    _add_style(table, TABLE_STYLE)

    body_row = 0
    for row in table.find_all('tr'):
        cells = row.find_all(['th', 'td'])
        if not cells:
            continue
        is_header = all(cell.name == 'th' for cell in cells)
        if is_header:
            _add_style(row, HEADER_ROW_STYLE)
            for cell in cells:
                _style_cell(cell, HEADER_CELL_STYLE)
            continue

        # Alternating white / light grey. The background is repeated on every
        # cell because Canvas' own table CSS overrides a <tr> background.
        bg = ROW_BG_ODD if body_row % 2 == 0 else ROW_BG_EVEN
        body_row += 1
        _add_style(row, f'background-color:{bg};')
        for cell in cells:
            _style_cell(cell, f'{CELL_STYLE} background-color:{bg};')


def inline_table_styles(app, pagename, templatename, context, doctree):
    body = context.get('body')
    if not body or 'uio-table' not in body:
        return

    soup = BeautifulSoup(body, 'html.parser')
    tables = soup.find_all('table', class_='uio-table')
    if not tables:
        return

    for table in tables:
        _style_table(table)

    context['body'] = str(soup)


def setup(app):
    app.connect('html-page-context', inline_table_styles)
    return {
        'version': '1.0',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
