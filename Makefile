# ============================================================================
# Factor Skyline — Reproducibility Harness Makefile
# ============================================================================

PYTHON = python
OUTDIR = reproducibility/tables/output

# ----------------------------------------------------------------------------
# Default target
# ----------------------------------------------------------------------------

.PHONY: all
all: tables

# ----------------------------------------------------------------------------
# tables — Run the full reproducibility harness (all 20 table scripts)
# ----------------------------------------------------------------------------

.PHONY: tables
tables:
	@echo "=== Factor Skyline: running reproducibility harness ==="
	$(PYTHON) reproducibility/run_all.py
	@echo "=== Factor Skyline: harness complete ==="

# ----------------------------------------------------------------------------
# clean — Delete all timestamped output directories
# ----------------------------------------------------------------------------

.PHONY: clean
clean:
	@echo "Removing all timestamped runs from $(OUTDIR)/"
	rm -rf $(OUTDIR)/*/
	@echo "Clean complete."

# ----------------------------------------------------------------------------
# list — List all timestamped run directories, sorted by name
# ----------------------------------------------------------------------------

.PHONY: list
list:
	@echo "Timestamped runs in $(OUTDIR)/:"
	@ls -1 $(OUTDIR)/ 2>/dev/null || echo "  (none)"

# ----------------------------------------------------------------------------
# compare — Diff two timestamped runs
# Usage: make compare A=20260321_122818 B=20260321_143012
# ----------------------------------------------------------------------------

.PHONY: compare
compare:
	@test -n "$(A)" || { echo "Usage: make compare A=<timestamp> B=<timestamp>"; exit 1; }
	@test -n "$(B)" || { echo "Usage: make compare A=<timestamp> B=<timestamp>"; exit 1; }
	@test -d "$(OUTDIR)/$(A)" || { echo "Error: $(OUTDIR)/$(A) not found."; exit 1; }
	@test -d "$(OUTDIR)/$(B)" || { echo "Error: $(OUTDIR)/$(B) not found."; exit 1; }
	diff -r $(OUTDIR)/$(A) $(OUTDIR)/$(B)

# ----------------------------------------------------------------------------
# notebooks — Execute Jupyter notebooks (placeholder)
# ----------------------------------------------------------------------------

.PHONY: notebooks
notebooks:
	@echo "Notebook execution not yet implemented."

# ============================================================================
# PDF Export Pipeline
# ============================================================================

PANDOC = pandoc
PANDOC_FLAGS = --from markdown --pdf-engine=xelatex --toc --number-sections

# ----------------------------------------------------------------------------
# pdfs — Export all documents to PDF
# ----------------------------------------------------------------------------

.PHONY: pdfs
pdfs: monograph glossary map papers

# ----------------------------------------------------------------------------
# monograph — Export the monograph to PDF
# ----------------------------------------------------------------------------

.PHONY: monograph
monograph:
	@echo "Exporting monograph to PDF..."
	$(PANDOC) monograph/FS_monograph.md -o monograph/FS_monograph.pdf \
		$(PANDOC_FLAGS) \
		--metadata title="Factor Skyline Monograph"
	@echo "monograph/FS_monograph.pdf created."

# ----------------------------------------------------------------------------
# glossary — Export the glossary to PDF
# ----------------------------------------------------------------------------

.PHONY: glossary
glossary:
	@echo "Exporting glossary to PDF..."
	$(PANDOC) monograph/FS_glossary.md -o monograph/FS_glossary.pdf \
		$(PANDOC_FLAGS) \
		--metadata title="Factor Skyline Glossary"
	@echo "monograph/FS_glossary.pdf created."

# ----------------------------------------------------------------------------
# map — Export the architectural map to PDF
# ----------------------------------------------------------------------------

.PHONY: map
map:
	@echo "Exporting architectural map to PDF..."
	$(PANDOC) maps/FS_architectural_map.md -o maps/FS_architectural_map.pdf \
		$(PANDOC_FLAGS) \
		--metadata title="Factor Skyline Architectural Map"
	@echo "maps/FS_architectural_map.pdf created."

# ----------------------------------------------------------------------------
# papers — Export all papers to PDF
# ----------------------------------------------------------------------------

.PHONY: papers
papers:
	@echo "Exporting papers to PDF..."
	@for f in papers/*.md; do \
		out=$${f%.md}.pdf; \
		echo "  $$f -> $$out"; \
		$(PANDOC) $$f -o $$out $(PANDOC_FLAGS); \
	done
	@echo "All papers exported."

# ----------------------------------------------------------------------------
# pdf-clean — Delete all generated PDFs
# ----------------------------------------------------------------------------

.PHONY: pdf-clean
pdf-clean:
	@echo "Removing generated PDFs..."
	rm -f monograph/FS_monograph.pdf monograph/FS_glossary.pdf
	rm -f maps/FS_architectural_map.pdf
	rm -f papers/*.pdf
	@echo "PDF clean complete."
