# Configuration overrides for Exercises PDF
# This file is imported at the end of conf.py when building Exercises PDF

master_doc = 'exercises_only'
simplepdf_file_name = 'Treningsoppgaver.pdf'

# Use the no-pagenumbers CSS instead of regular simplepdf.css
html_css_files = [
    'variables.css',
    'common.css',
    'uio-global-override.css',
    'custom.css',
    'simplepdf-no-pagenumbers.css',  # No page numbers version
]
