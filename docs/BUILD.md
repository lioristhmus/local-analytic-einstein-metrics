# Build and source

`paper/manuscript.md` is the canonical public source. `paper/manuscript.tex`
is the pdfLaTeX export and is self-contained apart from standard
TeX packages. Its bibliography is already rendered, so rebuilding the PDF
does not need BibTeX or network access.

```sh
bash scripts/build_pdf.sh
```

The script requires `pdflatex` on the command path and compiles the supplied
TeX three times into `build/paper/`. The output is
`build/paper/manuscript.pdf`; the published PDF in `paper/` is preserved.

The published PDF was built with pdfTeX 1.40.29 (TeX Live 2026). Markdown
conversion used Pandoc 3.9.0.2 and pandoc-crossref 0.3.23. To reproduce the
PDF layout, build from the supplied TeX. Different conversion templates,
fonts or TeX versions may change pagination and PDF bytes.
