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


class uio_note(nodes.General, nodes.Element):
    """Note container - uses uio-icon-box source class."""
    pass


class uio_do(nodes.General, nodes.Element):
    """Do/tip container - uses uio-icon-box do class."""
    pass


class UioExerciseDirective(SphinxDirective):
    """
    UiO exercise directive.

    Usage::

        .. uio-exercise::

           Exercise content here

           .. uio-solution::

              Solution content here (will be collapsible accordion)
    """
    has_content = True
    option_spec = {
        'title': directives.unchanged,
    }

    def run(self):
        node = uio_exercise()
        node['title'] = self.options.get('title', 'Oppgave')
        self.state.nested_parse(self.content, self.content_offset, node)
        return [node]


class UioReflectDirective(SphinxDirective):
    """
    UiO reflection exercise directive.

    Usage::

        .. uio-reflect::

           Reflection content here

           .. uio-solution::

              Solution content here (will be collapsible accordion)
    """
    has_content = True
    option_spec = {
        'title': directives.unchanged,
    }

    def run(self):
        node = uio_reflect()
        node['title'] = self.options.get('title', 'Refleksjon')
        self.state.nested_parse(self.content, self.content_offset, node)
        return [node]


class UioQuestionDirective(SphinxDirective):
    """
    UiO question directive.

    Usage::

        .. uio-question::

           Question content here

           .. uio-answer::

              Answer content here (will be collapsible accordion)
    """
    has_content = True
    option_spec = {
        'title': directives.unchanged,
    }

    def run(self):
        node = uio_question()
        node['title'] = self.options.get('title', 'Spørsmål')
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

        .. uio-dont::

           Warning content here
    """
    has_content = True
    option_spec = {
        'title': directives.unchanged,
    }

    def run(self):
        node = uio_dont()
        node['title'] = self.options.get('title', 'OBS!')
        self.state.nested_parse(self.content, self.content_offset, node)
        return [node]


class UioNoteDirective(SphinxDirective):
    """
    UiO note directive.

    Usage::

        .. uio-note::

           Note content here
    """
    has_content = True
    option_spec = {
        'title': directives.unchanged,
    }

    def run(self):
        node = uio_note()
        node['title'] = self.options.get('title', 'Merk')
        self.state.nested_parse(self.content, self.content_offset, node)
        return [node]


class UioDoDirective(SphinxDirective):
    """
    UiO do/tip directive.

    Usage::

        .. uio-do::

           Tip content here
    """
    has_content = True
    option_spec = {
        'title': directives.unchanged,
    }

    def run(self):
        node = uio_do()
        node['title'] = self.options.get('title', 'Tips')
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
    self.body.append('<summary class="uio-solution-summary"><strong>Løsning / Solution</strong></summary>\n')


def html_depart_uio_solution(self, node):
    """Close solution HTML."""
    self.body.append('</details>\n')


def html_visit_uio_answer(self, node):
    """Generate collapsible answer HTML (accordion inside question)."""
    self.body.append('<details>\n')
    self.body.append('<summary class="uio-answer-summary"><strong>Svar / Answer</strong></summary>\n')


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


def html_visit_uio_note(self, node):
    """Generate UiO note HTML."""
    title = node.get('title', 'Merk')

    self.body.append('<div class="uio-icon-box source">\n')
    self.body.append(f'<h3>{self.encode(title)}</h3>\n')


def html_depart_uio_note(self, node):
    """Close note HTML."""
    self.body.append('</div>\n')  # Close uio-icon-box source


def html_visit_uio_do(self, node):
    """Generate UiO do/tip HTML."""
    title = node.get('title', 'Tips')

    self.body.append('<div class="uio-icon-box do">\n')
    self.body.append(f'<h3>{self.encode(title)}</h3>\n')


def html_depart_uio_do(self, node):
    """Close do HTML."""
    self.body.append('</div>\n')  # Close uio-icon-box do


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

            # 2. Replace admonition note with uio-icon-box info
            content = re.sub(r'class="admonition note"', 'class="uio-icon-box info"', content)

            # 3. Remove navigation elements
            content = re.sub(r'<nav data-toggle="wy-nav-shift" class="wy-nav-side">.*?</nav>', '', content, flags=re.DOTALL)
            content = re.sub(r'<nav class="wy-nav-top".*?</nav>', '', content, flags=re.DOTALL)
            content = re.sub(r'<div role="navigation" aria-label="Page navigation">.*?</div>', '', content, flags=re.DOTALL)
            content = re.sub(r'<footer>.*?</footer>', '', content, flags=re.DOTALL)
            content = re.sub(r'<li class="wy-breadcrumbs-aside">.*?</li>', '', content, flags=re.DOTALL)
            content = re.sub(r'<div class="rst-versions".*?</div>', '', content, flags=re.DOTALL)
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
        uio_note,
        html=(html_visit_uio_note, html_depart_uio_note)
    )
    app.add_node(
        uio_do,
        html=(html_visit_uio_do, html_depart_uio_do)
    )

    # Add directives
    app.add_directive('uio-exercise', UioExerciseDirective)
    app.add_directive('uio-reflect', UioReflectDirective)
    app.add_directive('uio-question', UioQuestionDirective)
    app.add_directive('uio-solution', UioSolutionDirective)
    app.add_directive('uio-answer', UioAnswerDirective)
    app.add_directive('uio-dont', UioDontDirective)
    app.add_directive('uio-note', UioNoteDirective)
    app.add_directive('uio-do', UioDoDirective)

    # Connect to html-page-context to add heading stripe
    app.connect('html-page-context', add_heading_stripe)

    # Connect to build-finished to clean up HTML
    app.connect('build-finished', cleanup_html_post_build)

    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
