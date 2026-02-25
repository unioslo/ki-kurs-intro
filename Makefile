# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = source
BUILDDIR      = _build

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile deploy-from-local deploy-from-local-dry-run deploy-from-github deploy-from-github-dry-run

# Deploy to Canvas from local HTML files in _build/html/episodes
deploy-from-local:
	@python div-support-filer/update_canvas_pages.py

# Deploy from local (dry-run): preview what would be deployed without making changes
deploy-from-local-dry-run:
	@python div-support-filer/update_canvas_pages.py --dry-run

# Deploy to Canvas from GitHub html-pages branch
deploy-from-github:
	@python div-support-filer/update_canvas_pages.py --from-github

# Deploy from GitHub (dry-run): preview what would be deployed without making changes
deploy-from-github-dry-run:
	@python div-support-filer/update_canvas_pages.py --from-github --dry-run

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)