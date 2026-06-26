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

.PHONY: help Makefile deploy-from-local deploy-from-local-dry-run deploy-from-github deploy-from-github-dry-run exercises-pdf

# Deploy to Canvas from local HTML files
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

# Build PDF for Exercises/Treningsoppgaver only (without page numbers)
exercises-pdf:
	@echo "Building Exercises PDF (no page numbers, no cover, no TOC)..."
	@EXERCISES_PDF=1 $(SPHINXBUILD) -b simplepdf "$(SOURCEDIR)" "_build/simplepdf-exercises"
	@echo ""

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)