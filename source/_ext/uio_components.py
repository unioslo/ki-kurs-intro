"""
UiO Canvas-compatible components extension.
Generates HTML following UiO design guidelines from:
https://www.uio.no/for-ansatte/arbeidsstotte/sta/canvas/veiledninger/utnytt-mulighetene/designelementer.html
"""

from docutils import nodes
from docutils.parsers.rst import directives
from sphinx.util.docutils import SphinxDirective


class uio_heading_stripe(nodes.General, nodes.Element):
    """Blue heading stripe at top of page."""
    pass


class uio_exercise(nodes.General, nodes.Element):
    """Exercise container - uses uio-icon-box task class."""
    pass


class uio_reflect(nodes.General, nodes.Element):
    """Reflection exercise container - uses uio-icon-box reflect class."""
    pass


class uio_question(nodes.General, nodes.Element):
    """Question container - uses uio-icon-box task class."""
    pass


class uio_solution(nodes.General, nodes.Element):
    """Solution container (accordion) - nested in exercise."""
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


class uio_source(nodes.General, nodes.Element):
    """Source/resources container - uses uio-icon-box source class."""
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


class uio_detail(nodes.General, nodes.Element):
    """Details/accordion element - uses HTML details/summary."""
    pass


class UioExerciseDirective(SphinxDirective):
    """
    UiO exercise directive.

    Usage::

        .. uio-exercise:: Custom Title

           Exercise content here

           .. uio-solution::

              Solution content here (will be collapsible accordion)
    """
    has_content = True
    required_arguments = 0
    optional_arguments = 100
    final_argument_whitespace = True

    def run(self):
        node = uio_exercise()
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


class UioQuestionDirective(SphinxDirective):
    """
    UiO question directive.

    Usage::

        .. uio-question:: Custom Title

           Question content here

           .. uio-answer::

              Answer content here (will be collapsible accordion)
    """
    has_content = True
    required_arguments = 0
    optional_arguments = 100
    final_argument_whitespace = True

    def run(self):
        node = uio_question()
        if self.arguments:
            node['title'] = ' '.join(self.arguments)
        else:
            node['title'] = 'Spørsmål'
        self.state.nested_parse(self.content, self.content_offset, node)
        return [node]


class UioSolutionDirective(SphinxDirective):
    """Collapsible solution directive (accordion)."""
    has_content = True

    def run(self):
        node = uio_solution()
        self.state.nested_parse(self.content, self.content_offset, node)
        return [node]


class UioAnswerDirective(SphinxDirective):
    """Collapsible answer directive (accordion)."""
    has_content = True

    def run(self):
        node = uio_answer()
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


def html_visit_uio_exercise(self, node):
    """Generate UiO exercise HTML."""
    has_solution = any(isinstance(child, uio_solution) for child in node.children)
    title = node.get('title', 'Oppgave')

    self.body.append('<div class="uio-icon-box task">\n')
    self.body.append(f'<h3>{self.encode(title)}</h3>\n')

    # Store state for depart function
    node['has_solution'] = has_solution


def html_depart_uio_exercise(self, node):
    """Close exercise HTML."""
    self.body.append('</div>\n')  # Close uio-icon-box task


def html_visit_uio_reflect(self, node):
    """Generate UiO reflection HTML."""
    has_solution = any(isinstance(child, uio_solution) for child in node.children)
    title = node.get('title', 'Refleksjon')

    self.body.append('<div class="uio-icon-box reflect">\n')
    self.body.append(f'<h3>{self.encode(title)}</h3>\n')

    # Store state for depart function
    node['has_solution'] = has_solution


def html_depart_uio_reflect(self, node):
    """Close reflection HTML."""
    self.body.append('</div>\n')  # Close uio-icon-box reflect


def html_visit_uio_question(self, node):
    """Generate UiO question HTML."""
    has_answer = any(isinstance(child, uio_answer) for child in node.children)
    title = node.get('title', 'Spørsmål')

    self.body.append('<div class="uio-icon-box task">\n')
    self.body.append(f'<h3>{self.encode(title)}</h3>\n')

    # Store state for depart function
    node['has_answer'] = has_answer


def html_depart_uio_question(self, node):
    """Close question HTML."""
    self.body.append('</div>\n')  # Close uio-icon-box task


def html_visit_uio_solution(self, node):
    """Generate collapsible solution HTML (accordion inside exercise)."""
    self.body.append('<details>\n')
    self.body.append('<summary class="uio-solution-summary"><strong>Løsning</strong></summary>\n')


def html_depart_uio_solution(self, node):
    """Close solution HTML."""
    self.body.append('</details>\n')


def html_visit_uio_answer(self, node):
    """Generate collapsible answer HTML (accordion inside question)."""
    self.body.append('<details>\n')
    self.body.append('<summary class="uio-answer-summary"><strong>Svar</strong></summary>\n')


def html_depart_uio_answer(self, node):
    """Close answer HTML."""
    self.body.append('</details>\n')


def html_visit_uio_dont(self, node):
    """Generate UiO don't/warning HTML."""
    title = node.get('title', 'OBS!')

    self.body.append('<div class="uio-icon-box dont">\n')
    self.body.append(f'<h3>{self.encode(title)}</h3>\n')


def html_depart_uio_dont(self, node):
    """Close don't HTML."""
    self.body.append('</div>\n')  # Close uio-icon-box dont


def html_visit_uio_do(self, node):
    """Generate UiO do/tip HTML."""
    title = node.get('title', 'Tips')

    self.body.append('<div class="uio-icon-box do">\n')
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


def html_visit_uio_detail(self, node):
    """Generate details/accordion HTML."""
    summary = node.get('summary', 'Details')
    self.body.append('<details>\n')
    self.body.append(f'<summary><strong>{self.encode(summary)}</strong></summary>\n')


def html_depart_uio_detail(self, node):
    """Close details HTML."""
    self.body.append('</details>\n')


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


def setup(app):
    """Register the UiO components."""

    # Add nodes
    app.add_node(
        uio_exercise,
        html=(html_visit_uio_exercise, html_depart_uio_exercise)
    )
    app.add_node(
        uio_reflect,
        html=(html_visit_uio_reflect, html_depart_uio_reflect)
    )
    app.add_node(
        uio_question,
        html=(html_visit_uio_question, html_depart_uio_question)
    )
    app.add_node(
        uio_solution,
        html=(html_visit_uio_solution, html_depart_uio_solution)
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
        uio_detail,
        html=(html_visit_uio_detail, html_depart_uio_detail)
    )

    # Add directives
    app.add_directive('uio-exercise', UioExerciseDirective)
    app.add_directive('uio-reflect', UioReflectDirective)
    app.add_directive('uio-question', UioQuestionDirective)
    app.add_directive('uio-solution', UioSolutionDirective)
    app.add_directive('uio-answer', UioAnswerDirective)
    app.add_directive('uio-dont', UioDontDirective)
    app.add_directive('uio-do', UioDoDirective)
    app.add_directive('uio-info', UioInfoDirective)
    app.add_directive('uio-source', UioSourceDirective)
    app.add_directive('uio-colorbox-1', UioColorbox1Directive)
    app.add_directive('uio-colorbox-2', UioColorbox2Directive)
    app.add_directive('uio-colorbox-3', UioColorbox3Directive)
    app.add_directive('uio-icon-box', UioIconBoxDirective)
    app.add_directive('uio-detail', UioDetailDirective)

    # Connect to html-page-context to add heading stripe
    app.connect('html-page-context', add_heading_stripe)

    # Connect to build-finished to clean up HTML
    app.connect('build-finished', cleanup_html_post_build)

    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
