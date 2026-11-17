# Verification

Run these lightweight checks from the repository root:

```sh
python3 scripts/validate_release.py
python3 scripts/preflight.py
```

The first command checks the file manifest, the Kasner companion archive,
saved results and their recorded resource limits. It also checks all 85 files
of the upstream computational package and the selected records in the
paper-to-code map. The second checks Markdown anchors, citations and source
structure. Neither command executes the mathematical calculations.

The [computational supplement](../computations/README.md) contains code,
inputs, environments and saved outputs. Its
[coverage index](../computations/COVERAGE.json) distinguishes finite exact
checks, floating-point diagnostics and claims outside their scope.
[UPSTREAM.json](../computations/UPSTREAM.json) identifies the source tag and
hash of each imported file.

The general coefficient estimates, inverse-order gain, analytic convergence
and geometric realization are proved in the paper. Finite computations test
the specified identities and examples. To repeat those calculations, follow
the isolated execution instructions in the supplement.

For downloaded release assets, use the SHA-256 checksums described in the
[release notes](RELEASE.md). For a PDF rebuild, follow the
[build instructions](BUILD.md).
