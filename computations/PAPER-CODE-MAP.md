# Paper-to-code map: expanded v1.0 preparation

The inherited mathematical files and execution records are unchanged.
`COVERAGE.json` fixes selected IDs, exclusions and formula comparisons.

| Current paper | Precursor evidence | Precise coverage |
| --- | --- | --- |
| Lemma 4.1, `eq:es-recursion` and `eq:es-spencer-spectrum` | AB-PROJECTORS-R1/R4 | Complete finite coefficient bases in both chiralities through order four; complementary inverse and spectrum, not arbitrary antisymmetric-source surjectivity |
| Section 2; Proposition 3.3, `eq:es-algebraic-curvature` | AB-WEYL-ADMISSIBILITY-R1 and AB-WEYL-ADMISSIBILITY | Quartic Weyl basis, curvature constraints and signed -1/4 inverse readout at Lambda=0 |
| Lemma 4.1; Appendix B, `eq:es-q-one/two/three` | AB-EXACT-SET-R1/R4 | Actual polynomial product rule, exact-set compatibility and free projection on the declared mixed nilpotent input family; mixed cubic output required nonzero at r=4 |
| Lemma 4.1; Appendix B geometric example | KASNER-R1/R3 | Independent geometric differentiation at one fixed metric through order three, with Q0 and vacuum checks; geometric HQ is not the polynomial product-rule route |
| Sections 2–4; algebraic curvature and recursion | IW-GEOMETRY-CONTROLS-R2 | Independent implementation through order two on Kasner, mixed wave, two single waves and nonzero-Lambda Kottler; two non-Einstein controls and sensitive convention controls |
| Section 5 recurrence diagnostics | Six B-* records | Float64 residuals/crosschecks and observation completeness through order eight, with the original norm and polarization scope; no test of the new single ordered coefficient or diagram mass |

The first two five-line/spectrum displays match their precursor counterparts
as mathematical text. The Lambda/3 curvature expression and the two signed
readout right-hand sides agree as well. The source-side formal-completion
arguments correspond to Proposition 3.2 here; finite algebraic tests do not
replace that proposition's realization and polynomial-continuation proof.

No Schwarzschild optical, Adamo comparison, two-wave Ricci-repair or matrix-
Schwarzian record is claimed as a theorem check of this extracted paper.
Those files remain available within the unchanged upstream package.

Still outside computational coverage: the general differentiated Bianchi
completion, atomic diagram mass and all-order inverse-order gain, analytic
flows, Jacobi existence and uniform domains, point/spin comparisons and
Lorentz reality. As in the precursor, the independent geometric witness code
does not directly calibrate the primary `ab_exact.py` against metric jets.
