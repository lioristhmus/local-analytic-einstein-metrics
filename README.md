# Local analytic Einstein metrics from free curvature data in four dimensions

Lior Isthmus · v1.0.1 · [ORCID](https://orcid.org/0009-0004-7908-9876)

This paper reconstructs marked holomorphic Einstein metric germs in four
dimensions from two free chiral curvature records satisfying a factorial
growth bound, for an arbitrary prescribed cosmological constant. It proves
uniform coefficient estimates, convergent record flows, direct radial
Jacobi realization, holomorphic dependence and the Lorentz real form.

- [Paper PDF](paper/manuscript.pdf)
- [Canonical Markdown](paper/manuscript.md), [TeX](paper/manuscript.tex) and [bibliography](paper/references.bib)
- [Computational supplement](computations/README.md), [paper-to-code map](computations/PAPER-CODE-MAP.md) and [coverage index](computations/COVERAGE.json)
- [Build instructions](docs/BUILD.md), [verification](docs/VERIFICATION.md) and [release notes](docs/RELEASE.md)
- [Citation](CITATION.cff) and [licenses](LICENSES.md)

Version 1.0.1 is published on [GitHub](https://github.com/lioristhmus/local-analytic-einstein-metrics/releases/tag/v1.0.1) and
[Zenodo](https://doi.org/10.5281/zenodo.24318760) (DOI: `10.5281/zenodo.24318760`).

## Verify the supplied files

```sh
python3 scripts/validate_release.py
python3 scripts/preflight.py
```

These commands check file integrity, source references and saved results.
They do not run the mathematical workload. The saved results include Kasner geometry through order three, exact
finite-basis and polynomial free-record checks through order four, independent
metric witnesses with convention controls through order two, and separately
classified float64 diagnostics through order eight. The all-order estimates and convergence arguments are the
proofs in the paper.

The Kasner checks compare geometric curvature derivatives with the Spencer
recursion. The AB-* records test the polynomial free-record implementation;
the IW-* group supplies independent metric witnesses and convention controls.
Their precise roles and limits are recorded in the coverage index.

The original Kasner companion, `exact-set-checks-v0.1.1.zip`, is included at
`paper/exact-set-checks-v0.1.1.zip` in the repository and both source and
computation ZIPs.

AI use is disclosed in the manuscript. The computations include code,
specified inputs, recorded environment and exact outputs.
