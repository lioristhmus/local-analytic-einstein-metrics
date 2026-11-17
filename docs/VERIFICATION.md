# Verification scope

The release derives from editorial v0.1.12, with copyediting, bibliographic
and layout corrections following prepublication review. The mathematical
content, assumptions, notation and theorem numbers are unchanged. Equation
IDs, theorem headings and the order of mathematical expressions are retained.
The only punctuation change within a mathematical expression replaces a period
between the two formulas in the second low-order correction with a comma.

Revision 3 retains 977 mathematical segments, 113 displays, 24 formal statement
headings, 156 generated labels and 104 equation numbers. The 39-page PDF has
112 resolved internal named links.

The preparation checks compare the Markdown, exported TeX, rendered PDF and
release archives. They include an all-page overview, readable inspection of
changed pages, reference resolution and file hashes. These checks establish
source and artifact fidelity. The retained finite results are not rerun as
part of this preparation.

The finite exact results are described in `../computations/README.md`.
`scripts/validate_release.py` checks their saved PASS status, resource
bounds, zero residuals, file hashes and archive membership. It does not
execute Sage or certify the general theorem.

The expanded local preparation also retains the precursor r3 package byte for
byte and maps every relevant A/B, Kasner and B diagnostic ID plus its independent
witness group. `computations/COVERAGE.json` separates exact tests, numerical
diagnostics and excluded claims. No inherited run is relabeled as a fresh run.
