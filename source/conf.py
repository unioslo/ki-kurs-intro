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
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx.ext.intersphinx',
    'sphinx.ext.githubpages',
    'canvas_tabs',  # Canvas-compatible tabs (no JavaScript)
    'canvas_exercise',  # Canvas-compatible collapsible exercises
    'sphinx_lesson',
    'sphinx_rtd_theme',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The master toctree document.
master_doc = 'index'

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Custom CSS to fix solution button styling
html_css_files = [
    'custom.css',
]

# Hide navigation for Canvas integration
html_sidebars = {
    '**': []  # No sidebars on any page
}

# RTD theme options to hide navigation
html_theme_options = {
    'navigation_depth': -1,  # Hide navigation tree
    'collapse_navigation': True,
    'sticky_navigation': False,
    'includehidden': False,
    'titles_only': True,
    'prev_next_buttons_location': None,  # Remove prev/next buttons
    'display_version': False,
}

# -- Extension configuration -------------------------------------------------

# Example configuration for intersphinx extension:
intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'numpy': ('https://numpy.org/doc/stable/', None),
}