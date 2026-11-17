# Computational supplement

Code, inputs, environments and saved results accompany
*Local analytic Einstein metrics from free curvature data in four dimensions*.
The supplement includes the Kasner companion linked from the PDF and the
computational package published with
[the projective twistor paper, tag `paper-v1.1`](https://github.com/lioristhmus/projective-twistor-einstein-germs/tree/paper-v1.1/computations).
[UPSTREAM.json](UPSTREAM.json) identifies the original file hashes and the
documentation updates. Computational code, inputs and saved results retain
their original bytes.

| Relevant group | Retained evidence | Scope |
| --- | --- | --- |
| Kasner recurrence | Both chiralities through r=3; 520 entries | Fixed vacuum metric; explicit vacuum and Q0 checks in the precursor code |
| Spencer maps | All 880 basis vectors through r=4 | Finite projection decomposition, compressed spectrum and complementary inverse |
| Algebraic Weyl reconstruction | Ten quartic basis vectors; 320 signed readout components | Lambda-zero algebraic curvature and normalization |
| Polynomial free records | 7,040 scalar coefficient slots through r=4; required nonzero mixed cubic output | One specified independent mixed chiral family over a nilpotent rational coefficient algebra |
| Independent geometry | Five Einstein metrics and two non-Einstein controls through r=2 | Separate implementation, Q0 and polynomial/geometric comparison; curvature-sign and Lambda-coefficient controls |
| Coefficient diagnostics | float64 profiles through r=4 and r=8 | Finite residual/crosschecks and observations, not certified norm bounds |

These comprise 14 relevant primary record IDs (8 finite-exact and 6 numerical)
and one independent finite-exact evidence group. Pilots overlap the larger runs;
coefficient slots include zeros and are not independent examples. The remaining
14 primary IDs in `precursor/` concern claims outside this paper and are not
counted here.

[PAPER-CODE-MAP.md](PAPER-CODE-MAP.md) maps the paper; [COVERAGE.json](COVERAGE.json) records all selected and
excluded IDs. The five-line recurrence and Spencer spectrum match the precursor
mathematical text exactly after whitespace normalization. Algebraic curvature
and signed readout conventions also agree. All-order diagram masses and
convergence remain proofs in the paper, not results of these finite tests.

## Validate files and saved evidence

```sh
python3 scripts/validate_release.py
```

Run that command from the repository root. It also runs the precursor's file-only
QA, checking all 85 files, 84 checksums, source/log/input correspondence and
the independent convention controls. No mathematical program is invoked.

For the computations-only ZIP, run its self-contained upstream validator from
the archive root instead:

```sh
python3 computations/precursor/code/verify_package.py
```

That command checks the 85-file precursor package. The archive's
`ARCHIVE-MANIFEST.json` additionally records the wrapper files and current-paper map.

## Reproduce mathematical jobs

Use the pinned, isolated controller and new output directories documented in
`precursor/README.md`. The most relevant primary jobs are `ab-r1`, `ab-r4`,
`kasner-r1`, `kasner-r3`, `b-low4` and `b-low8`; the independent job is
`independent/code/run.py --job witness-r2`. The shared machine-wide lock,
memory-plus-swap below 2GB, one CPU, no network and finite container deadlines
are enforced by those controllers. Saved result files record the execution
environment, limits and exit status. [INDEPENDENT-EVIDENCE.md](precursor/INDEPENDENT-EVIDENCE.md)
distinguishes the independent metric calculations from earlier audit logs.
