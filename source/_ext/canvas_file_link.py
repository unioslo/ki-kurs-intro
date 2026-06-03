"""
Sphinx extension for Canvas file links.

Usage in RST:
    .. canvas-file:: 3906804
       :text: KI-grunnkurs-treningsoppgaver.pdf
       :title: Lenke

Or inline:
    :canvas-file:`3906804|KI-grunnkurs-treningsoppgaver.pdf`
"""

from docutils import nodes
from docutils.parsers.rst import Directive, directives
from docutils.parsers.rst.roles import set_classes
from sphinx.util.docutils import SphinxRole


class CanvasFileNode(nodes.General, nodes.Element):
    """Node for Canvas file links."""
    pass


class CanvasFileDirective(Directive):
    """
    Directive for Canvas file links.

    .. canvas-file:: FILE_ID
       :text: Link text to display
       :title: Tooltip title
    """
    required_arguments = 1  # File ID
    optional_arguments = 0
    final_argument_whitespace = False
    has_content = False
    option_spec = {
        'text': directives.unchanged,
        'title': directives.unchanged,
    }

    def run(self):
        file_id = self.arguments[0]
        link_text = self.options.get('text', f'File {file_id}')
        title = self.options.get('title', 'Lenke')

        node = CanvasFileNode()
        node['file_id'] = file_id
        node['link_text'] = link_text
        node['title'] = title

        return [node]


class CanvasFileRole(SphinxRole):
    """
    Inline role for Canvas file links.

    :canvas-file:`FILE_ID|Link text`
    """
    def run(self):
        text = self.text
        if '|' in text:
            file_id, link_text = text.split('|', 1)
        else:
            file_id = text
            link_text = f'File {file_id}'

        node = CanvasFileNode()
        node['file_id'] = file_id.strip()
        node['link_text'] = link_text.strip()
        node['title'] = 'Lenke'

        return [node], []


def visit_canvas_file_html(self, node):
    """Render Canvas file link as HTML."""
    file_id = node['file_id']
    link_text = node['link_text']
    title = node['title']

    # Generate Canvas file link HTML
    html = f'''<p><a id="{file_id}" class="instructure_file_link instructure_scribd_file inline_disabled" title="{title}" href="/courses/COURSE_ID/files/{file_id}?wrap=1" target="_blank" rel="noopener noreferrer" data-canvas-previewable="true">{link_text}</a></p>'''

    self.body.append(html)


def depart_canvas_file_html(self, node):
    """No closing tag needed."""
    pass


def setup(app):
    """Register the extension."""
    app.add_node(CanvasFileNode,
                 html=(visit_canvas_file_html, depart_canvas_file_html))
    app.add_directive('canvas-file', CanvasFileDirective)
    app.add_role('canvas-file', CanvasFileRole())

    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
