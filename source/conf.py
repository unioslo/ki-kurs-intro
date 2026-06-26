# Configuration file for the Sphinx documentation builder.

import os
import sys

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
sys.path.insert(0, os.path.abspath('.'))
sys.path.insert(0, os.path.abspath('_ext'))

# -- Project information -----------------------------------------------------

project = 'Grunnkurs KI'
copyright = 'IT-avdelingen Universitetet i Oslo'
author = 'KI-inititaivet, Universitetet i Oslo'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'canvas_tabs',  # Canvas-compatible tabs (no JavaScript)
    'sphinx_rtd_theme',
    'uio_components',  # UiO Canvas design components
    'sphinx_new_tab_link',  # for å automatisk åpne eksterne lenker i ny tab i nettleseren
    'citation_override',
    'sphinx_simplepdf',
    'canvas_file_link',  # Canvas file links
]

# Icon for external links
new_tab_link_show_external_link_icon = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The master toctree document.
master_doc = 'index'

# Add UiO heading stripe to all pages
#rst_prolog = """
#.. raw:: html
#
#   <div class="uio-heading-stripe">&nbsp;</div>
#
#"""

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Custom CSS files
html_css_files = [
    'variables.css',
    'common.css',
    'uio-global-override.css',
    'custom.css',
    'simplepdf.css',  # PDF-specific styling
]

# Custom JavaScript files
html_js_files = [
    'tabs.js',
]

# Don't add <p> tags to simple list items
html_compact_lists = True

# Disable automatic headerlinks (anchor links on headers)
html_permalinks = False

# -- Extension configuration -------------------------------------------------


# Custom CSS for SimplePDF
simplepdf_file_name = 'Grunnkurs-KI.pdf'

# Add custom CSS for PDF output
simplepdf_style_files = [
    '_static/simplepdf.css',
]

# Check if we should load Exercises overrides
import os
if os.environ.get('EXERCISES_PDF'):
    # Override settings for Exercises PDF
    master_doc = 'exercises_only'
    simplepdf_file_name = 'KI-grunnkurs-treningsoppgaver.pdf'

    # Split title into main title and subtitle
    project = 'Treningsoppgaver'
    # SimplePDF uses "Version {release}" so we set release to just the subtitle text
    release = 'KI grunnkurs'
    version = 'KI grunnkurs'

    # Show cover but hide TOC for Episode 5 PDF
    simplepdf_theme_options = {
        "nocover": False,  # Keep the front cover page
        "notoc": True,     # Disable the automatically generated Table of Contents
    }

    # White cover and back cover for printing economy
    simplepdf_vars = {
        'primary': '#0d72c0',
        'cover': '#ffffff',              # White front cover background
        'cover-bg': '#ffffff',           # White front cover background
        'cover-fg': '#000000',           # Black text on front cover
        'back-cover': '#ffffff',         # White back cover background
        'back-cover-bg': '#ffffff',      # White back cover background
        'back-cover-fg': '#000000',      # Black text on back cover
        'cover-overlay': 'rgba(255, 255, 255, 1)',  # White overlay
        'links': '#0d72c0',
        'toc-title': '"" !important',    # Hide TOC title
        'toc-content': '"" !important',  # Hide TOC content
    }

    html_css_files = [
        'variables.css',
        'common.css',
        'uio-global-override.css',
        'custom.css',
        'simplepdf-no-pagenumbers.css',  # No page numbers
    ]

# -- SimplePDF configuration -------------------------------------------------
simplepdf_vars = {
    'primary': '#0d72c0',           # UiO Blue for headings and links
    'primary-opaque': '#0d72c0',
    'cover': '#0d72c0',             # Cover background color
    'cover-bg': '#0d72c0',          # Cover background
    'cover-fg': '#ffffff',          # Cover text (white)
    'cover-overlay': 'rgba(13, 114, 192, 0.95)',
    'white': '#ffffff',
    'links': '#0d72c0',
    'top-header-color': '#0d72c0',  # Top stripe color (was red)
    'header-color': '#0d72c0',
}


# SimplePDF debug settings
simplepdf_debug = False

# Basic settings
numfig = False
html_show_sourcelink = False