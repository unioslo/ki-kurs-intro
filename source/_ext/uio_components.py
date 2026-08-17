"""
UiO Canvas-compatible components extension.
Generates HTML following UiO design guidelines from:
https://www.uio.no/for-ansatte/arbeidsstotte/sta/canvas/veiledninger/utnytt-mulighetene/designelementer.html
"""

import re

from docutils import nodes
from docutils.parsers.rst import directives
from sphinx.util.docutils import SphinxDirective


# Canvas instance and course used to build chapter-card icon URLs at build time.
# Keep in sync with update_canvas_pages.py (CANVAS_URL / COURSE_ID).
CANVAS_URL = "https://uio.instructure.com"
CANVAS_COURSE_ID = "63248"


class uio_heading_stripe(nodes.General, nodes.Element):
    """Blue heading stripe at top of page."""
    pass


class uio_task(nodes.General, nodes.Element):
    """Task container - uses uio-icon-box task class."""
    pass


class uio_reflect(nodes.General, nodes.Element):
    """Reflection exercise container - uses uio-icon-box reflect class."""
    pass


class uio_answer(nodes.General, nodes.Element):
    """Answer container (accordion) - nested in question."""
    pass


class uio_dont(nodes.General, nodes.Element):
    """Don't/warning container - uses uio-icon-box dont class."""
    pass


class uio_do(nodes.General, nodes.Element):
    """Do/tip container - uses uio-icon-box do class."""
    pass


class uio_info(nodes.General, nodes.Element):
    """Info container - uses uio-icon-box info class."""
    pass

class uio_viktig(nodes.General, nodes.Element):
    """Viktig container - uses uio-icon-box viktig class."""
    pass


class uio_source(nodes.General, nodes.Element):
    """Source/resources container - uses uio-icon-box source class."""
    pass


class uio_chapter_card(nodes.General, nodes.Element):
    """Canvas chapter card - icon + linked heading + description."""
    pass


class uio_module_listing(nodes.General, nodes.Element):
    """Colored container that groups uio-chapter-card entries."""
    pass


class uio_colorbox_1(nodes.General, nodes.Element):
    """Color box 1 container - uses uio-color-box-1 class."""
    pass


class uio_colorbox_2(nodes.General, nodes.Element):
    """Color box 2 container - uses uio-color-box-2 class."""
    pass


class uio_colorbox_3(nodes.General, nodes.Element):
    """Color box 3 container - uses uio-color-box-3 class."""
    pass


class uio_icon_box(nodes.General, nodes.Element):
    """Generic icon box container - plain div with class uio-icon-box."""
    pass


class uio_custom_box(nodes.General, nodes.Element):
    """Icon box with a caller-defined border colour - uses uio-icon-box + inline style."""
    pass


class uio_detail(nodes.General, nodes.Element):
    """Details/accordion element - uses HTML details/summary."""
    pass


class uio_do_dont_container(nodes.General, nodes.Element):
    """Container for do/dont grid row - uses uio-grid-row class."""
    pass


class uio_do_dont_item(nodes.General, nodes.Element):
    """Individual do or dont item in grid - uses uio-icon-box do/dont col-lg."""
    pass


class UioTaskDirective(SphinxDirective):
    """
    UiO task directive.

    Usage::

        .. uio-task:: Custom Title

           Task content here

           .. uio-solution::

              Solution content here (will be collapsible accordion)

           .. uio-answer::

              Answer content here (will be collapsible accordion)
    """
    has_content = True
    required_arguments = 0
    optional_arguments = 100
    final_argument_whitespace = True

    def run(self):
        node = uio_task()
        if self.arguments:
            node['title'] = ' '.join(self.arguments)
        else:
            node['title'] = 'Oppgave'
        self.state.nested_parse(self.content, self.content_offset, node)
        return [node]


class UioReflectDirective(SphinxDirective):
    """
    UiO reflection exercise directive.

    Usage::

        .. uio-reflect:: Custom Title

           Reflection content here

           .. uio-solution::

              Solution content here (will be collapsible accordion)
    """
    has_content = True
    required_arguments = 0
    optional_arguments = 100
    final_argument_whitespace = True

    def run(self):
        node = uio_reflect()
        if self.arguments:
            node['title'] = ' '.join(self.arguments)
        else:
            node['title'] = 'Refleksjon'
        self.state.nested_parse(self.content, self.content_offset, node)
        return [node]


class UioAnswerDirective(SphinxDirective):
    """Collapsible answer directive (accordion)."""
    has_content = True
    required_arguments = 0
    optional_arguments = 100
    final_argument_whitespace = True

    def run(self):
        node = uio_answer()
        if self.arguments:
            node['title'] = ' '.join(self.arguments)
        else:
            node['title'] = 'Svar'
        self.state.nested_parse(self.content, self.content_offset, node)
        return [node]


class UioDontDirective(SphinxDirective):
    """
    UiO don't/warning directive.

    Usage::

        .. uio-dont:: Custom Title

           Warning content here
    """
    has_content = True
    required_arguments = 0
    optional_arguments = 100
    final_argument_whitespace = True

    def run(self):
        node = uio_dont()
        if self.arguments:
            node['title'] = ' '.join(self.arguments)
        else:
            node['title'] = 'OBS!'
        self.state.nested_parse(self.content, self.content_offset, node)
        return [node]


class UioDoDirective(SphinxDirective):
    """
    UiO do/tip directive.

    Usage::

        .. uio-do:: Custom Title

           Tip content here
    """
    has_content = True
    required_arguments = 0
    optional_arguments = 100
    final_argument_whitespace = True

    def run(self):
        node = uio_do()
        if self.arguments:
            node['title'] = ' '.join(self.arguments)
        else:
            node['title'] = 'Tips'
        self.state.nested_parse(self.content, self.content_offset, node)
        return [node]


class UioInfoDirective(SphinxDirective):
    """
    UiO info directive.

    Usage::

        .. uio-info:: Custom Title

           Info content here
    """
    has_content = True
    required_arguments = 0
    optional_arguments = 100
    final_argument_whitespace = True

    def run(self):
        node = uio_info()
        if self.arguments:
            node['title'] = ' '.join(self.arguments)
        else:
            node['title'] = 'Info'
        self.state.nested_parse(self.content, self.content_offset, node)
        return [node]

class UioViktigDirective(SphinxDirective):
    """
    UiO viktig (important) directive.

    Usage::

        .. uio-viktig:: Custom Title

           Viktig content here
    """
    has_content = True
    required_arguments = 0
    optional_arguments = 100
    final_argument_whitespace = True

    def run(self):
        node = uio_viktig()
        if self.arguments:
            node['title'] = ' '.join(self.arguments)
        else:
            node['title'] = 'Viktig'
        self.state.nested_parse(self.content, self.content_offset, node)
        return [node]


class UioSourceDirective(SphinxDirective):
    """
    UiO source/resources directive.

    Usage::

        .. uio-source:: Custom Title

           Source content here
    """
    has_content = True
    required_arguments = 0
    optional_arguments = 100
    final_argument_whitespace = True

    def run(self):
        node = uio_source()
        if self.arguments:
            node['title'] = ' '.join(self.arguments)
        else:
            node['title'] = 'Kilder / Ressurser'
        self.state.nested_parse(self.content, self.content_offset, node)
        return [node]


class UioColorbox1Directive(SphinxDirective):
    """
    UiO color box 1 directive.

    Usage::

        .. uio-colorbox-1::

           Content without title

        .. uio-colorbox-1:: Optional Title

           Content with title
    """
    has_content = True
    required_arguments = 0
    optional_arguments = 100
    final_argument_whitespace = True

    def run(self):
        node = uio_colorbox_1()
        if self.arguments:
            node['title'] = ' '.join(self.arguments)
        else:
            node['title'] = None
        self.state.nested_parse(self.content, self.content_offset, node)
        return [node]


class UioColorbox2Directive(SphinxDirective):
    """
    UiO color box 2 directive.

    Usage::

        .. uio-colorbox-2::

           Content without title

        .. uio-colorbox-2:: Optional Title

           Content with title
    """
    has_content = True
    required_arguments = 0
    optional_arguments = 100
    final_argument_whitespace = True

    def run(self):
        node = uio_colorbox_2()
        if self.arguments:
            node['title'] = ' '.join(self.arguments)
        else:
            node['title'] = None
        self.state.nested_parse(self.content, self.content_offset, node)
        return [node]


class UioColorbox3Directive(SphinxDirective):
    """
    UiO color box 3 directive.

    Usage::

        .. uio-colorbox-3::

           Content without title

        .. uio-colorbox-3:: Optional Title

           Content with title
    """
    has_content = True
    required_arguments = 0
    optional_arguments = 100
    final_argument_whitespace = True

    def run(self):
        node = uio_colorbox_3()
        if self.arguments:
            node['title'] = ' '.join(self.arguments)
        else:
            node['title'] = None
        self.state.nested_parse(self.content, self.content_offset, node)
        return [node]


class UioIconBoxDirective(SphinxDirective):
    """
    UiO icon box directive - generic container.

    Usage::

        .. uio-icon-box::

           .. uio-detail:: Details title

              Content here
    """
    has_content = True

    def run(self):
        node = uio_icon_box()
        self.state.nested_parse(self.content, self.content_offset, node)
        return [node]


# Named colours for uio-custom-box. The four first are UiOs dataklassifisering
# (grønn / gul / rød / svart) so pages can name the class instead of a hex value.
CUSTOM_BOX_COLORS = {
    'gronn': '#7FBF8C',
    'grønn': '#7FBF8C',
    'green': '#7FBF8C',
    'gul': '#E8C46A',
    'yellow': '#E8C46A',
    'rod': '#DE8A8A',
    'rød': '#DE8A8A',
    'red': '#DE8A8A',
    'svart': '#57575C',
    'black': '#57575C',
}

# Only hex colours are allowed through to the style attribute - the generated
# HTML is pushed to Canvas, so nothing unvalidated should end up in an attribute.
CSS_HEX_COLOR = re.compile(r'^#(?:[0-9a-fA-F]{3}|[0-9a-fA-F]{6})$')

DEFAULT_CUSTOM_BOX_COLOR = '#8595BC'

# Litt tynnere enn do/dont/info (10/5) for et mykere uttrykk.
CUSTOM_BOX_BORDER_TOP = 7
CUSTOM_BOX_BORDER_BOTTOM = 3


def custom_box_color(argument):
    """Option validator: a name from CUSTOM_BOX_COLORS or a #rgb / #rrggbb value."""
    value = (argument or '').strip()
    if not value:
        raise ValueError('a colour name or hex value is required')

    named = CUSTOM_BOX_COLORS.get(value.lower())
    if named:
        return named

    if CSS_HEX_COLOR.match(value):
        return value

    raise ValueError(
        f"'{value}' is not a hex colour (#rgb or #rrggbb) or one of: "
        + ', '.join(sorted(set(CUSTOM_BOX_COLORS)))
    )


class UioCustomBoxDirective(SphinxDirective):
    """
    UiO icon box with a caller-defined border colour.

    Same look as uio-do / uio-info / uio-dont (the shared uio-icon-box styling
    with a thick top border and a thinner bottom border), but the colour is set
    per box instead of coming from a do/dont/info class.

    Usage::

        .. uio-custom-box:: 🟢 Grønn: Åpen informasjon
           :color: gronn

           Content here

        .. uio-custom-box:: Egen farge
           :color: #7ED321
           :background: #f7fcf2

           Content here
    """
    has_content = True
    required_arguments = 0
    optional_arguments = 100
    final_argument_whitespace = True
    option_spec = {
        'color': custom_box_color,
        'background': custom_box_color,
    }

    def run(self):
        node = uio_custom_box()
        node['title'] = ' '.join(self.arguments) if self.arguments else None
        node['color'] = self.options.get('color', DEFAULT_CUSTOM_BOX_COLOR)
        node['background'] = self.options.get('background')
        self.state.nested_parse(self.content, self.content_offset, node)
        return [node]


class UioDetailDirective(SphinxDirective):
    """
    UiO detail/accordion directive.

    Usage::

        .. uio-detail:: Summary text here

           Content that will be hidden/collapsible
    """
    has_content = True
    required_arguments = 0
    optional_arguments = 100
    final_argument_whitespace = True

    def run(self):
        node = uio_detail()
        # Get summary text from directive arguments
        if self.arguments:
            node['summary'] = ' '.join(self.arguments)
        else:
            node['summary'] = 'Detaljer'
        self.state.nested_parse(self.content, self.content_offset, node)
        return [node]


class UioDoDontDirective(SphinxDirective):
    """
    UiO do/don't grid directive.

    Usage::

        .. uio-do-dont::

           .. uio-do:: Gjør / Do / Positivt

              Content for do section

           .. uio-dont:: Ikke gjør / Don't / Negativt

              Content for dont section
    """
    has_content = True

    def run(self):
        container = uio_do_dont_container()
        self.state.nested_parse(self.content, self.content_offset, container)
        return [container]


def html_visit_uio_task(self, node):
    """Generate UiO task HTML."""
    title = node.get('title', 'Oppgave')

    self.body.append('<div class="uio-icon-box task">\n')
    self.body.append(f'<h3>{self.encode(title)}</h3>\n')


def html_depart_uio_task(self, node):
    """Close task HTML."""
    self.body.append('</div>\n')  # Close uio-icon-box task


def html_visit_uio_reflect(self, node):
    """Generate UiO reflection HTML."""
    has_answer = any(isinstance(child, uio_answer) for child in node.children)
    title = node.get('title', 'Refleksjon')

    self.body.append('<div class="uio-icon-box reflect">\n')
    self.body.append(f'<h3>{self.encode(title)}</h3>\n')

    # Store state for depart function
    node['has_answer'] = has_answer


def html_depart_uio_reflect(self, node):
    """Close reflection HTML."""
    self.body.append('</div>\n')  # Close uio-icon-box reflect


def html_visit_uio_answer(self, node):
    """Generate collapsible answer HTML (accordion inside question)."""
    title = node.get('title', 'Svar')
    self.body.append('<details>\n')
    self.body.append(f'<summary class="uio-answer-summary"><strong>{self.encode(title)}</strong></summary>\n')


def html_depart_uio_answer(self, node):
    """Close answer HTML."""
    self.body.append('</details>\n')


def html_visit_uio_dont(self, node):
    """Generate UiO don't/warning HTML."""
    title = node.get('title', 'OBS!')

    # Check if this is inside a do-dont grid container
    in_grid = isinstance(node.parent, uio_do_dont_container)
    css_class = 'uio-icon-box dont col-lg' if in_grid else 'uio-icon-box dont'

    self.body.append(f'<div class="{css_class}">\n')
    self.body.append(f'<h3>{self.encode(title)}</h3>\n')


def html_depart_uio_dont(self, node):
    """Close don't HTML."""
    self.body.append('</div>\n')  # Close uio-icon-box dont


def html_visit_uio_do(self, node):
    """Generate UiO do/tip HTML."""
    title = node.get('title', 'Tips')

    # Check if this is inside a do-dont grid container
    in_grid = isinstance(node.parent, uio_do_dont_container)
    css_class = 'uio-icon-box do col-lg' if in_grid else 'uio-icon-box do'

    self.body.append(f'<div class="{css_class}">\n')
    self.body.append(f'<h3>{self.encode(title)}</h3>\n')


def html_depart_uio_do(self, node):
    """Close do HTML."""
    self.body.append('</div>\n')  # Close uio-icon-box do


def html_visit_uio_info(self, node):
    """Generate UiO info HTML."""
    title = node.get('title', 'Info')

    self.body.append('<div class="uio-icon-box info">\n')
    self.body.append(f'<h3>{self.encode(title)}</h3>\n')


def html_depart_uio_info(self, node):
    """Close info HTML."""
    self.body.append('</div>\n')  # Close uio-icon-box info


# New vikt ig node handling

def html_visit_uio_viktig(self, node):
    """Generate UiO viktig (important) HTML."""
    title = node.get('title', 'Viktig')
    self.body.append('<div class="uio-icon-box viktig">\n')
    self.body.append(f'<h3>{self.encode(title)}</h3>\n')


def html_depart_uio_viktig(self, node):
    """Close viktig HTML."""
    self.body.append('</div>\n')  # Close uio-icon-box viktig


def html_visit_uio_source(self, node):
    """Generate UiO source/resources HTML."""
    title = node.get('title', 'Kilder / Ressurser')

    self.body.append('<div class="uio-icon-box source">\n')
    self.body.append(f'<h3>{self.encode(title)}</h3>\n')


def html_depart_uio_source(self, node):
    """Close source HTML."""
    self.body.append('</div>\n')  # Close uio-icon-box source


def html_visit_uio_colorbox_1(self, node):
    """Generate UiO color box 1 HTML."""
    title = node.get('title')

    self.body.append('<div class="uio-color-box-1">\n')
    if title:
        self.body.append(f'<h3>{self.encode(title)}</h3>\n')


def html_depart_uio_colorbox_1(self, node):
    """Close color box 1 HTML."""
    self.body.append('</div>\n')


def html_visit_uio_colorbox_2(self, node):
    """Generate UiO color box 2 HTML."""
    title = node.get('title')

    self.body.append('<div class="uio-color-box-2">\n')
    if title:
        self.body.append(f'<h3>{self.encode(title)}</h3>\n')


def html_depart_uio_colorbox_2(self, node):
    """Close color box 2 HTML."""
    self.body.append('</div>\n')


def html_visit_uio_colorbox_3(self, node):
    """Generate UiO color box 3 HTML."""
    title = node.get('title')

    self.body.append('<div class="uio-color-box-3">\n')
    if title:
        self.body.append(f'<h3>{self.encode(title)}</h3>\n')


def html_depart_uio_colorbox_3(self, node):
    """Close color box 3 HTML."""
    self.body.append('</div>\n')


def html_visit_uio_icon_box(self, node):
    """Generate UiO icon box HTML."""
    self.body.append('<div class="uio-icon-box">\n')


def html_depart_uio_icon_box(self, node):
    """Close icon box HTML."""
    self.body.append('</div>\n')


def html_visit_uio_custom_box(self, node):
    """Generate icon box HTML with a caller-defined border colour.

    The colour goes in an inline style rather than in a new CSS class: the
    generated HTML is uploaded to Canvas, where only UiOs own classes exist.
    """
    color = node.get('color') or DEFAULT_CUSTOM_BOX_COLOR
    background = node.get('background')
    title = node.get('title')

    style = f'border-top: {CUSTOM_BOX_BORDER_TOP}px solid {color}; border-bottom: {CUSTOM_BOX_BORDER_BOTTOM}px solid {color};'
    if background:
        style += f' background-color: {background};'

    self.body.append(f'<div class="uio-icon-box" style="{style}">\n')
    if title:
        self.body.append(f'<h3>{self.encode(title)}</h3>\n')


def html_depart_uio_custom_box(self, node):
    """Close custom box HTML."""
    self.body.append('</div>\n')  # Close uio-icon-box (custom colour)


def html_visit_uio_detail(self, node):
    """Generate details/accordion HTML."""
    summary = node.get('summary', 'Details')
    self.body.append('<details>\n')
    self.body.append(f'<summary><strong>{self.encode(summary)}</strong></summary>\n')


def html_depart_uio_detail(self, node):
    """Close details HTML."""
    self.body.append('</details>\n')


def html_visit_uio_do_dont_container(self, node):
    """Generate UiO do/dont grid row HTML."""
    self.body.append('<div class="uio-grid-row">\n')


def html_depart_uio_do_dont_container(self, node):
    """Close do/dont grid row HTML."""
    self.body.append('</div>\n')


def add_heading_stripe(app, pagename, templatename, context, doctree):
    """Add blue heading stripe to every page."""
    if doctree and hasattr(context, 'body'):
        # Inject heading stripe HTML at the beginning
        stripe_html = '<div class="uio-heading-stripe">&nbsp;</div>\n'
        if 'body' in context:
            context['body'] = stripe_html + context['body']


def cleanup_html_post_build(app, exception):
    """Clean up HTML files after build is complete."""
    import re
    import glob
    from pathlib import Path

    if exception is not None:
        return  # Build failed, don't process

    # Get the output directory
    outdir = Path(app.outdir)

    # Process all HTML files
    for html_file in outdir.rglob('*.html'):
        try:
            with open(html_file, 'r', encoding='utf-8') as f:
                content = f.read()

            original = content

            # 1. Remove <p> tags from list items
            content = re.sub(r'<li><p>(.*?)</p></li>', r'<li>\1</li>', content, flags=re.DOTALL)
            content = re.sub(r'<li><p>(.*?)</p>', r'<li>\1', content, flags=re.DOTALL)

            # 2. Replace admonitions with appropriate uio-icon-box types
            content = re.sub(r'class="admonition note"', 'class="uio-icon-box source"', content)
            content = re.sub(r'class="admonition tip"', 'class="uio-icon-box do"', content)
            content = re.sub(r'class="admonition warning"', 'class="uio-icon-box dont"', content)
            content = re.sub(r'class="admonition important"', 'class="uio-icon-box source"', content)
            content = re.sub(r'class="admonition caution"', 'class="uio-icon-box dont"', content)
            content = re.sub(r'class="admonition danger"', 'class="uio-icon-box dont"', content)
            content = re.sub(r'class="admonition hint"', 'class="uio-icon-box do"', content)
            content = re.sub(r'class="admonition seealso"', 'class="uio-icon-box source"', content)

            # Remove admonition-title paragraphs
            content = re.sub(r'<p class="admonition-title">[^<]*</p>\s*', '', content)

            # 3. Remove any existing page-navigation divs (from previous builds)
            content = re.sub(r'<div class="page-navigation".*?</div>\s*</div>\s*</div>\s*\n', '', content, flags=re.DOTALL)

            # 4. Extract prev/next navigation before removing
            prev_link = re.search(r'<link rel="prev" title="([^"]*)" href="([^"]*)"', content)
            next_link = re.search(r'<link rel="next" title="([^"]*)" href="([^"]*)"', content)

            # Build navigation HTML with just "Prev" and "Next"
            nav_html = '<div class="page-navigation">'
            if prev_link:
                prev_href = prev_link.group(2)
                nav_html += f'<div class="prev-link"><a href="{prev_href}">← Forrige</a></div>'
            else:
                nav_html += '<div class="prev-link"></div>'

            if next_link:
                next_href = next_link.group(2)
                nav_html += f'<div class="next-link"><a href="{next_href}">Neste →</a></div>'
            else:
                nav_html += '<div class="next-link"></div>'
            nav_html += '</div>\n'

            # Insert navigation before closing </section> - more flexible regex
            # Match </section> followed by closing divs, with flexible whitespace
            content = re.sub(r'(</section>)\s*(\n\s*</div>)', nav_html + r'\1\2', content, count=1)

            # Remove navigation elements
            content = re.sub(r'<nav data-toggle="wy-nav-shift" class="wy-nav-side">.*?</nav>', '', content, flags=re.DOTALL)
            content = re.sub(r'<nav class="wy-nav-top".*?</nav>', '', content, flags=re.DOTALL)
            content = re.sub(r'<div role="navigation".*?</div>', '', content, flags=re.DOTALL)
            content = re.sub(r'<footer>.*?</footer>', '', content, flags=re.DOTALL)
            content = re.sub(r'<li class="wy-breadcrumbs-aside">.*?</li>', '', content, flags=re.DOTALL)
            content = re.sub(r'<div class="rst-versions".*?</div>', '', content, flags=re.DOTALL)
            # Remove any existing prev/next navigation links in the content
            content = re.sub(r'<a[^>]*rel="prev"[^>]*>.*?</a>', '', content, flags=re.DOTALL)
            content = re.sub(r'<a[^>]*rel="next"[^>]*>.*?</a>', '', content, flags=re.DOTALL)
            content = re.sub(r'<section data-toggle="wy-nav-shift" class="wy-nav-content-wrap">',
                           '<section class="wy-nav-content-wrap" style="margin-left: 0;">', content)

            # 4. Remove RTD theme wrapper divs
            content = re.sub(r'<body class="wy-body-for-nav">', '<body>', content)
            content = re.sub(r'<div class="wy-grid-for-nav">\s*', '', content)
            # Remove the closing div for wy-grid-for-nav (comes after the last </section>)
            content = re.sub(r'(</section>\s*</div>\s*</body>)', r'</section></body>', content)

            # Only write if changed
            if content != original:
                with open(html_file, 'w', encoding='utf-8') as f:
                    f.write(content)

        except Exception as e:
            print(f"Warning: Could not process {html_file}: {e}")


class UioChapterCardDirective(SphinxDirective):
    """
    UiO chapter card directive.

    Usage::

        .. uio-chapter-card::
           :title: Introduksjon til "KI-språket"
           :icon_filename: kap2-ikon.svg
           :icon_file_id: 3954816
           :url: https://uio.instructure.com/courses/63248/pages/introduksjon-til-ki-spraket-3
           :description: Kort beskrivelse

    The icon ``<img>`` is emitted as a placeholder carrying a ``data-icon-file``
    attribute (no invented class names). If ``:icon_file_id:`` (the Canvas file id,
    entered by hand) is given, ``update_canvas_pages.py`` builds the Canvas
    Icon-Maker reference directly from it; otherwise it looks the file up by filename.
    The heading link is built from ``:url:`` at build time; if ``:url:`` is omitted, a
    fallback anchor carrying ``data-card-title`` is emitted for title-based resolution
    against ``page_id_mapping.json`` at upload time.
    """
    has_content = False
    required_arguments = 0
    optional_arguments = 0
    option_spec = {
        'title': directives.unchanged,
        'icon_filename': directives.unchanged,
        'icon_file_id': directives.unchanged,
        'icon_color': directives.unchanged,
        'url': directives.unchanged,
        'description': directives.unchanged,
    }

    def run(self):
        node = uio_chapter_card()
        node['title'] = self.options.get('title', '')
        node['icon'] = self.options.get('icon_filename', '')
        node['icon_file_id'] = self.options.get('icon_file_id', '')
        # icon_color drives local icon generation (build_icons.py); it is not
        # used in the emitted HTML, but is declared here so `make html` accepts it.
        node['icon_color'] = self.options.get('icon_color', '')
        node['url'] = self.options.get('url', '')
        node['description'] = self.options.get('description', '')
        # Number of "../" needed for the local-preview icon src to resolve from
        # this document's build location (e.g. module2/foo.html -> depth 1).
        node['static_prefix'] = '../' * self.env.docname.count('/')
        return [node]


class UioModuleListingDirective(SphinxDirective):
    """
    UiO module listing directive.

    A colored container that groups one or more uio-chapter-card entries under a
    heading.

    Usage::

        .. uio-module-listing:: Emnemoduler:

           .. uio-chapter-card::
              :title: Introduksjon til "KI-språket"
              :icon_filename: kap2-ikon.svg
              :url: https://uio.instructure.com/courses/63248/pages/introduksjon-til-ki-spraket-3
              :description: Kort beskrivelse

           .. uio-chapter-card::
              :title: KI-tjenester ved UiO
              :icon_filename: kap6-ikon.svg
              :url: https://uio.instructure.com/courses/63248/pages/ki-tjenester-ved-uio
              :description: Godkjente verktøy og datasikkerhet

    The heading defaults to "Emnemoduler:" when no argument is given.
    """
    has_content = True
    required_arguments = 0
    optional_arguments = 100
    final_argument_whitespace = True

    def run(self):
        node = uio_module_listing()
        if self.arguments:
            node['title'] = ' '.join(self.arguments)
        else:
            node['title'] = 'Emnemoduler:'
        self.state.nested_parse(self.content, self.content_offset, node)
        return [node]


def html_visit_uio_module_listing(self, node):
    """Open the UiO module listing container.

    The child cards each render as their own ``<div class="float-left">`` (see
    the chapter-card visitor), so this container only emits the colored box and
    heading -- no extra float wrapper.
    """
    title = node.get('title', 'Emnemoduler:')
    self.body.append('<div class="uio-color-box-3 uio-module-listing">\n')
    if title:
        self.body.append(f'<h2>{self.encode(title)}</h2>\n')


def html_depart_uio_module_listing(self, node):
    """Close the UiO module listing container."""
    self.body.append('</div>\n')  # Close uio-color-box-3 uio-module-listing


def html_visit_uio_chapter_card(self, node):
    """Generate a full-width, clickable chapter bar (icon only).

    Each chapter renders as a single wide icon whose number and title are baked
    into the SVG; the icon fills the width of the "Kapitler" box and the whole
    bar is a link to the chapter's first Canvas page. There is no separate text
    heading or description (the title lives inside the icon). Build-time hooks for
    update_canvas_pages.py are carried on ``data-*`` attributes (``data-icon-file``
    on the img; ``data-card-title`` on the link when ``:url:`` is omitted), which
    are consumed and removed at upload time.
    """
    title = node.get('title', '')
    icon = node.get('icon', '')
    icon_file_id = node.get('icon_file_id', '')
    url = node.get('url', '')
    prefix = node.get('static_prefix', '')

    # Whole-bar link. With :url: emit the final Canvas anchor; otherwise emit a
    # data-card-title marker that update_canvas_pages.py resolves at upload time.
    link_style = 'display:block; margin-bottom:12px; text-decoration:none;'
    if url:
        api_endpoint = url.replace('/courses/', '/api/v1/courses/', 1)
        self.body.append(
            '<a href="%s" title="%s" data-course-type="wikiPages" data-published="true" '
            'data-api-endpoint="%s" data-api-returntype="Page" style="%s">'
            % (self.encode(url), self.encode(title), self.encode(api_endpoint), link_style)
        )
    else:
        self.body.append(
            '<a href="#" title="%s" data-card-title="%s" style="%s">'
            % (self.encode(title), self.encode(title), link_style)
        )

    # Icon fills the bar width. When :icon_file_id: is given (the Canvas file id),
    # emit the final Canvas Icon-Maker <img>; otherwise a local-preview <img>
    # (src into _static/icons/) carrying a data-icon-file marker resolved by
    # filename at upload time.
    # Icon fills the full width of the (1/3-page) "Kapitler" column.
    img_style = 'width:100%; height:auto; display:block;'
    if icon_file_id:
        canvas_src = f'{CANVAS_URL}/courses/{CANVAS_COURSE_ID}/files/{icon_file_id}/download'
        download_url = f'/files/{icon_file_id}/download?download_frd=1&icon_maker_icon=1'
        api_endpoint = f'{CANVAS_URL}/api/v1/courses/{CANVAS_COURSE_ID}/files/{icon_file_id}'
        self.body.append(
            '<img style="%s" role="presentation" '
            'src="%s" alt="" data-inst-icon-maker-icon="true" '
            'data-download-url="%s" data-api-endpoint="%s" data-api-returntype="File" />'
            % (img_style, self.encode(canvas_src), self.encode(download_url),
               self.encode(api_endpoint))
        )
    else:
        icon_src = f'{prefix}_static/icons/{icon}'
        self.body.append(
            '<img style="%s" role="presentation" src="%s" alt="" data-icon-file="%s" />'
            % (img_style, self.encode(icon_src), self.encode(icon))
        )


def html_depart_uio_chapter_card(self, node):
    """Close the chapter bar link opened in the visit function."""
    self.body.append('</a>\n')  # Close whole-bar link


def setup(app):
    """Register the UiO components."""

    # Add nodes
    app.add_node(
        uio_task,
        html=(html_visit_uio_task, html_depart_uio_task)
    )
    app.add_node(
        uio_reflect,
        html=(html_visit_uio_reflect, html_depart_uio_reflect)
    )
    app.add_node(
        uio_answer,
        html=(html_visit_uio_answer, html_depart_uio_answer)
    )
    app.add_node(
        uio_dont,
        html=(html_visit_uio_dont, html_depart_uio_dont)
    )
    app.add_node(
        uio_do,
        html=(html_visit_uio_do, html_depart_uio_do)
    )
    app.add_node(
        uio_info,
        html=(html_visit_uio_info, html_depart_uio_info)
    )
    # Register the new viktig node
    app.add_node(
        uio_viktig,
        html=(html_visit_uio_viktig, html_depart_uio_viktig)
    )
    app.add_node(
        uio_source,
        html=(html_visit_uio_source, html_depart_uio_source)
    )
    app.add_node(
        uio_colorbox_1,
        html=(html_visit_uio_colorbox_1, html_depart_uio_colorbox_1)
    )
    app.add_node(
        uio_colorbox_2,
        html=(html_visit_uio_colorbox_2, html_depart_uio_colorbox_2)
    )
    app.add_node(
        uio_colorbox_3,
        html=(html_visit_uio_colorbox_3, html_depart_uio_colorbox_3)
    )
    app.add_node(
        uio_icon_box,
        html=(html_visit_uio_icon_box, html_depart_uio_icon_box)
    )
    app.add_node(
        uio_custom_box,
        html=(html_visit_uio_custom_box, html_depart_uio_custom_box)
    )
    app.add_node(
        uio_detail,
        html=(html_visit_uio_detail, html_depart_uio_detail)
    )
    app.add_node(
        uio_do_dont_container,
        html=(html_visit_uio_do_dont_container, html_depart_uio_do_dont_container)
    )
    app.add_node(
        uio_chapter_card,
        html=(html_visit_uio_chapter_card, html_depart_uio_chapter_card)
    )
    app.add_node(
        uio_module_listing,
        html=(html_visit_uio_module_listing, html_depart_uio_module_listing)
    )

    # Add directives
    app.add_directive('uio-task', UioTaskDirective)
    app.add_directive('uio-reflect', UioReflectDirective)
    app.add_directive('uio-answer', UioAnswerDirective)
    app.add_directive('uio-dont', UioDontDirective)
    app.add_directive('uio-do', UioDoDirective)
    app.add_directive('uio-info', UioInfoDirective)
    app.add_directive('uio-viktig', UioViktigDirective)
    app.add_directive('uio-source', UioSourceDirective)
    app.add_directive('uio-colorbox-1', UioColorbox1Directive)
    app.add_directive('uio-colorbox-2', UioColorbox2Directive)
    app.add_directive('uio-colorbox-3', UioColorbox3Directive)
    app.add_directive('uio-icon-box', UioIconBoxDirective)
    app.add_directive('uio-custom-box', UioCustomBoxDirective)
    app.add_directive('uio-detail', UioDetailDirective)
    app.add_directive('uio-do-dont', UioDoDontDirective)
    app.add_directive('uio-chapter-card', UioChapterCardDirective)
    app.add_directive('uio-module-listing', UioModuleListingDirective)

    # Connect to html-page-context to add heading stripe
    app.connect('html-page-context', add_heading_stripe)

    # Connect to build-finished to clean up HTML
    app.connect('build-finished', cleanup_html_post_build)

    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
