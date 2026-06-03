# Configuration overrides for Episode 5 PDF
# This file is imported at the end of conf.py when building Episode 5 PDF

master_doc = 'episode5_only'
simplepdf_file_name = 'Episode5-Oppgaver.pdf'

# Use the no-pagenumbers CSS instead of regular simplepdf.css
html_css_files = [
    'variables.css',
    'common.css',
    'uio-global-override.css',
    'custom.css',
    'simplepdf-no-pagenumbers.css',  # No page numbers version
]
