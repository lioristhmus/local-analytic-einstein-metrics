# Build and source

`paper/manuscript.md` is the canonical public source. `paper/manuscript.tex`
is the reviewed pdfLaTeX export and is self-contained apart from standard
TeX packages. Its bibliography is already rendered, so rebuilding the PDF
does not need BibTeX or network access.

```sh
bash scripts/build_pdf.sh
```

The script compiles the supplied TeX three times, with an absolute main-file
path and a recorder, into `build/paper/`. It does not overwrite the release
PDF. The production environment was Pandoc 3.9.0.2, pandoc-crossref 0.3.23
and pdfTeX 1.40.29 (TeX Live 2026). Different fonts or TeX versions may
change pagination or PDF bytes.

The Markdown was exported with the maintained studio standard Pandoc/AMS
profile. The export pipeline is not vendored here. Its scoped output-only
adjustments center three unbreakable tables and use natural page-bottom
spacing, and put subsection 5.3 on its own line before the theorem
heading. For a portable rebuild of this release, use the supplied TeX.
Regenerating TeX from Markdown with a different profile may change layout.

The Abstract heading uses bold upright roman type, like the main text
headings, at the abstract body font size. It remains centered on a separate
line. This styling is included in the supplied TeX.
