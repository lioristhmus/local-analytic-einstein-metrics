# Verification scope

The release is derived from the completed editorial v0.1.12. The PDF and
TeX are byte-identical to that version; the Markdown changes only its
version metadata to 1.0. All 977 mathematical segments, 113 displays,
24 formal statements, 156 generated labels and 104 equation numbers are
retained. The 39-page PDF has 112 resolved internal named links.

The preceding editorial checks included all-page rendered overview and
readable inspection of the introduction, page 9, tables and final page.
They found no clipping, missing glyphs or unresolved references. These
checks establish artifact fidelity, not an independent proof audit.

The finite exact results are described in `../computations/README.md`.
`scripts/validate_release.py` checks their saved PASS status, resource
bounds, zero residuals, file hashes and archive membership. It does not
execute Sage or certify the general theorem.

The expanded local preparation also retains the precursor r3 package byte for
byte and maps every relevant A/B, Kasner and B diagnostic ID plus its independent
witness group. `computations/COVERAGE.json` separates exact tests, numerical
diagnostics and excluded claims. No inherited run is relabeled as a fresh run.
