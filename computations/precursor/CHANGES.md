# Computational checks and interpretation

The source supplement checks selected formulas in Section 9, Appendix D.2
and Appendices A/B of the projective twistor paper; see
[NEW-CHECKS.md](NEW-CHECKS.md). The following conventions determine how its
results should be read.

- Numerical `F2` and `F3` values are identified as unscaled labeled polarized
  coefficient sums. Their norm interpretation concerns those maps, not a
  separately identified single ordered coefficient of Appendix B.
- Residual diagnostics are described in their actual unweighted coefficient
  norm. The quadratic `JstarHQ` diagnostic is named directly, rather than
  described as an explicit all-degree free-projection check.
- Nonfinite scalars are rejected before maxima or conditional denominators;
  every required table field and every printed residual is parsed. Insertion
  tables are checked for finiteness. Production-parser regression controls
  include a valid synthetic record and fourteen rejected NaN/Inf/missing-data
  cases; these are reporting QA, separate from mathematical results.
- The Schwarzschild rotational Jacobi calculation derives radial acceleration
  from the computed Christoffels and differentiates the amplitude. The scalar
  Laplacian uses the computed metric determinant/inverse, and all three tractor
  parallel equations are checked in the declared negative-signature auxiliary
  metric. The screen calculation still excludes $f=0$ in its literal velocity
  formula and covers only the polar component.
- The Kasner test explicitly checks $Q_0=0$. Its later $HQ$ is identified as a
  geometric derivative, whereas the A/B test implements the polynomial
  product rule on independent free inputs. The Kasner chiral records are
  conjugate on the real input and are not advertised as independent lists.
- The actual K.5 wedge expression is compared to the adopted bilinear component
  matrix. The projector trace and $J^2=-I$ are also asserted. External Adamo
  equation (2.13) remains a scalar-coefficient comparison; its result field is
  named accordingly. The Schwarzschild Ricci index no longer suggests that the
  general-lapse static formula was executed.

The A/B backend uses explicit rational scaling and type assertions; no
floating tolerance is substituted for exact zero. It inverts the signed Weyl
readout on all ten quartic basis inputs. This tests the curvature normalization
separately from recursion compatibility, which can be insensitive to a
consistent parameter rescaling.

Accepted execution records are bound to their actual code and input hashes.
The separate [audit record](REVIEW-STATUS.json) and
[findings](RECONCILIATION.md) describe the review scope. The independent witness
group enforces its listed sign, Lambda and non-Einstein controls through r=2;
it does not extend primary `ab_exact.py` to a metric-witness or nonzero-Lambda
test.
