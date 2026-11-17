# Finite exact Kasner checks

The supplied SageMath code differentiates a Kasner vacuum metric, projects
the ordered curvature tensors to the two chiral records, and independently
evaluates the normalized Spencer recurrence. The input is in `input.json`;
conventions and spin-basis normalization are in `ORIGINAL-COMPANION.md`.

| Recorded run | Orders | Chiralities | Components | Recurrence residuals | Free-projection residuals |
| --- | --- | --- | --- | --- | --- |
| `results/kasner-r1-result.json` | 1 | both | 96 | 0 | 0 |
| `results/kasner-r3-result.json` | 1–3 | both | 520 | 0 | 0 |

The order-one run overlaps the order-three run; these are not 616 distinct
tests. These finite equalities do not prove the all-order estimates or
convergence. See [PAPER-CODE-MAP.md](PAPER-CODE-MAP.md).

The original companion archive is preserved byte for byte at
`../paper/exact-set-checks-v0.1.1.zip`, where the PDF's relative link resolves.
Its original title/version is historical; this repository supplies the
current paper and mapping. The code and saved controller results are
unchanged. The image identifier in the records is a local image ID,
not a registry repository digest. `environment.json` records that distinction.

## Reproduction

Run the controller from a writable checkout. It writes each result beside
the code; use a separate working copy to preserve the supplied records.

```sh
python3 code/run_isolated_check.py --max-r 1
python3 code/run_isolated_check.py --max-r 3
```

The controller is host-specific. It uses the shared lock path documented in
`ORIGINAL-COMPANION.md`, checks existing Docker services and refuses unknown
running containers. It enforces at most 1,992,294,400 bytes of memory plus
swap, one CPU, no network, 64 PIDs, bounded logs and temporary files, no
restart and foreground termination within 895 seconds. Inspect and adapt
the host-specific service policy before running elsewhere; do not bypass
isolation or invoke the mathematical program directly on the host.

No mathematical job was rerun for this release preparation. The records
include the original resource readings, exit status and exact output.
