"""
Canvas-compatible tabs directive for Sphinx.
Generates tabs using Canvas's native format with class="enhanceable_content tabs"
No JavaScript required.
"""

from docutils import nodes
from docutils.parsers.rst import Directive
from sphinx.util.docutils import SphinxDirective
import hashlib


class canvas_tabs(nodes.General, nodes.Element):
    """Container for Canvas tabs."""
    pass


class canvas_tab(nodes.General, nodes.Element):
    """Individual Canvas tab."""
    pass


class CanvasTabsDirective(SphinxDirective):
    """
    Canvas tabs container directive.

    Usage::

        .. canvas-tabs::

           .. canvas-tab:: Title 1

              Content 1

           .. canvas-tab:: Title 2

              Content 2
    """
    has_content = True

    def run(self):
        node = canvas_tabs()
        self.state.nested_parse(self.content, self.content_offset, node)
        return [node]


class CanvasTabDirective(SphinxDirective):
    """Individual tab directive."""
    has_content = True
    required_arguments = 1  # Tab title
    final_argument_whitespace = True

    def run(self):
        title = self.arguments[0]
        node = canvas_tab()
        node['tabtitle'] = title
        self.state.nested_parse(self.content, self.content_offset, node)
        return [node]


def html_visit_canvas_tabs(self, node):
    """Generate Canvas tabs HTML."""
    # Generate unique ID for this tab set
    tab_id = hashlib.md5(str(id(node)).encode()).hexdigest()[:8]

    # Collect all tabs
    tabs = [child for child in node.children if isinstance(child, canvas_tab)]

    # Start tabs container
    self.body.append('<div class="enhanceable_content tabs">\n')
    self.body.append('<ul>\n')

    # Generate tab links
    for i, tab in enumerate(tabs, 1):
        title = tab.get('tabtitle', f'Tab {i}')
        fragment_id = f'fragment-{tab_id}-{i}'
        # HTML escape the title
        safe_title = self.encode(title)
        self.body.append(f'<li><a href="#{fragment_id}">{safe_title}</a></li>\n')

    self.body.append('</ul>\n')

    # Generate tab content sections
    for i, tab in enumerate(tabs, 1):
        fragment_id = f'fragment-{tab_id}-{i}'
        self.body.append(f'<div id="{fragment_id}">\n')

        # Render the tab's content
        for child in tab.children:
            child.walkabout(self)

        self.body.append('</div>\n')

    self.body.append('</div>\n')

    raise nodes.SkipNode


def html_depart_canvas_tabs(self, node):
    pass


def html_visit_canvas_tab(self, node):
    """Skip - handled by parent."""
    raise nodes.SkipNode


def html_depart_canvas_tab(self, node):
    pass


def setup(app):
    """Register the Canvas tabs directives."""
    app.add_node(
        canvas_tabs,
        html=(html_visit_canvas_tabs, html_depart_canvas_tabs)
    )
    app.add_node(
        canvas_tab,
        html=(html_visit_canvas_tab, html_depart_canvas_tab)
    )

    app.add_directive('canvas-tabs', CanvasTabsDirective)
    app.add_directive('canvas-tab', CanvasTabDirective)

    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
