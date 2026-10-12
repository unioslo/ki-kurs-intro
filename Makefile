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

.PHONY: help Makefile deploy-from-local deploy-from-local-dry-run deploy-from-github deploy-from-github-dry-run exercises-pdf html-en gettext-update

# -- Translation (English) ---------------------------------------------------
# Norwegian is the source language; English lives in source/locale/en/*.po.

# Build the English site into _build/html/en (uses the gettext catalogs).
html-en:
	@$(SPHINXBUILD) -b html -D language=en "$(SOURCEDIR)" "$(BUILDDIR)/html/en" $(SPHINXOPTS) $(O)
	@echo "English HTML is in $(BUILDDIR)/html/en"

# Re-extract strings from the Norwegian source and refresh the English catalogs.
# Changed Norwegian paragraphs show up as fuzzy/untranslated in source/locale/en.
gettext-update:
	@$(SPHINXBUILD) -b gettext "$(SOURCEDIR)" "$(BUILDDIR)/gettext" $(SPHINXOPTS) $(O)
	@sphinx-intl update -p "$(BUILDDIR)/gettext" -l en
	@echo "Catalogs refreshed. Review fuzzy/untranslated entries in source/locale/en, then: make html-en"

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