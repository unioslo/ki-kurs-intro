# -*- coding: utf-8 -*-
"""Sphinx extension to customize citation reference rendering.

This overrides the default HTML translator to emit a custom class
``citation-label`` instead of the generic ``label`` class used by
Canvas. The CSS can then style ``.citation-label`` with a transparent
background. Works with sphinx_new_tab_link for external links.
"""

from sphinx.writers.html import HTMLTranslator
from docutils import nodes

class CitationHTMLTranslator(HTMLTranslator):
    def visit_citation_reference(self, node):
        # Handle citation references in text (e.g., [Hicks]_)
        href = '#' + node['refid']
        self.body.append(self.starttag(
            node, 'a', '',
            CLASS='citation-label',
            href=href
        ))
        self.body.append('[' + node.astext() + ']')

    def depart_citation_reference(self, node):
        self.body.append('</a>')

    def visit_label(self, node):
        # Override label rendering for citations to use citation-label class
        # This is based on Sphinx's default implementation but with custom class
        parent = node.parent

        if isinstance(parent, nodes.citation):
            # Use citation-label class for citations
            self.body.append('<span class="citation-label">')
        else:
            # Use default label class for non-citations
            self.body.append('<span class="label">')

        # Add opening bracket
        self.body.append('<span class="fn-bracket">[</span>')

        # Add backlink if enabled
        if self.settings.footnote_backlinks:
            backrefs = node.parent.get('backrefs', [])
            if len(backrefs) == 1:
                self.body.append('<a role="doc-backlink"'
                                 ' href="#%s">' % backrefs[0])

    def depart_label(self, node):
        # Close backlink if present
        backrefs = []
        if self.settings.footnote_backlinks:
            backrefs = node.parent.get('backrefs', backrefs)
        if len(backrefs) == 1:
            self.body.append('</a>')

        # Add closing bracket and close span
        self.body.append('<span class="fn-bracket">]</span></span>\n')

        # Handle multiple backrefs
        if len(backrefs) > 1:
            backlinks = ['<a role="doc-backlink" href="#%s">%s</a>' % (ref, i)
                         for (i, ref) in enumerate(backrefs, 1)]
            self.body.append('<span class="backrefs">(%s)</span>\n'
                             % ','.join(backlinks))

def setup(app):
    # Replace the default HTML translator with our custom one.
    app.set_translator('html', CitationHTMLTranslator, override=True)
    return {'version': '0.2'}
