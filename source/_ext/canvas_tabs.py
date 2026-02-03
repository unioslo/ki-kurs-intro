"""
Canvas-compatible tabs extension.
Uses HTML with class="enhanceable_content tabs" and URL fragments (no JavaScript).
"""

import hashlib
from docutils import nodes
from sphinx.util.docutils import SphinxDirective


class canvas_tabs(nodes.General, nodes.Element):
    """Container for Canvas tabs."""
    pass


class canvas_tab(nodes.General, nodes.Element):
    """Individual Canvas tab."""
    pass


class CanvasTabsDirective(SphinxDirective):
    """
    Canvas tabs directive.

    Usage::

        .. canvas-tabs::

           .. canvas-tab:: Tab Title 1

              Content for tab 1

           .. canvas-tab:: Tab Title 2

              Content for tab 2
    """
    has_content = True

    def run(self):
        node = canvas_tabs()
        self.state.nested_parse(self.content, self.content_offset, node)
        return [node]


class CanvasTabDirective(SphinxDirective):
    """Individual tab directive."""
    has_content = True

    def run(self):
        node = canvas_tab()
        # Get tab title from the argument
        node['tabtitle'] = ' '.join(self.arguments) if self.arguments else 'Tab'
        self.state.nested_parse(self.content, self.content_offset, node)
        return [node]

    @property
    def arguments(self):
        # Everything after ".. canvas-tab::" is the title
        return self.content[0].strip().split() if self.content else []

    has_content = True
    required_arguments = 0
    optional_arguments = 100
    final_argument_whitespace = True


class CanvasTabDirectiveFixed(SphinxDirective):
    """Individual tab directive with proper argument handling."""
    has_content = True
    required_arguments = 0
    optional_arguments = 100
    final_argument_whitespace = True

    def run(self):
        node = canvas_tab()
        # Get tab title from directive arguments
        if self.arguments:
            node['tabtitle'] = ' '.join(self.arguments)
        else:
            node['tabtitle'] = 'Tab'
        self.state.nested_parse(self.content, self.content_offset, node)
        return [node]


def html_visit_canvas_tabs(self, node):
    """Generate Canvas-compatible tabs HTML."""
    # Generate unique ID for this tab set
    tab_id = hashlib.md5(str(id(node)).encode()).hexdigest()[:8]

    # Get all tab children
    tabs = [child for child in node.children if isinstance(child, canvas_tab)]

    # Start the tabs container
    self.body.append('<div class="enhanceable_content tabs" style="margin-bottom: 2em;">\n')
    self.body.append('<ul>\n')

    # Generate tab navigation
    for i, tab in enumerate(tabs, 1):
        title = tab.get('tabtitle', f'Tab {i}')
        fragment_id = f'fragment-{tab_id}-{i}'
        self.body.append(f'<li><a href="#{fragment_id}" style="font-size: 1.2em; font-weight: bold;">{self.encode(title)}</a></li>\n')

    self.body.append('</ul>\n')

    # Generate tab content divs
    for i, tab in enumerate(tabs, 1):
        fragment_id = f'fragment-{tab_id}-{i}'
        self.body.append(f'<div id="{fragment_id}" style="font-size: 1.2em;">\n')

        # Process the tab's content
        for child in tab.children:
            child.walkabout(self)

        self.body.append('</div>\n')

    self.body.append('</div>\n')

    # Prevent further processing of children
    raise nodes.SkipNode


def html_depart_canvas_tabs(self, node):
    """Close tabs HTML (not called due to SkipNode)."""
    pass


def setup(app):
    """Register the Canvas tabs directives."""
    app.add_node(
        canvas_tabs,
        html=(html_visit_canvas_tabs, html_depart_canvas_tabs)
    )
    app.add_node(canvas_tab)

    app.add_directive('canvas-tabs', CanvasTabsDirective)
    app.add_directive('canvas-tab', CanvasTabDirectiveFixed)

    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
