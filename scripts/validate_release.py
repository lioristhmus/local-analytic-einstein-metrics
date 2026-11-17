"""Validate supplied files and saved finite results without running mathematics."""
from pathlib import Path
import hashlib
import json
import zipfile

root = Path(__file__).resolve().parents[1]
digest = lambda data: hashlib.sha256(data).hexdigest()
manifest = json.loads((root / "MANIFEST.json").read_text())
assert manifest["version"] == "1.0.1"
actual = {
    str(p.relative_to(root)) for p in root.rglob("*") if p.is_file()
    and not any(part in {".git", "build", "__pycache__"} for part in p.relative_to(root).parts)
    and p.name != "MANIFEST.json"
}
assert actual == set(manifest["files"]), "Repository inventory differs from the manifest"
for name, expected in manifest["files"].items():
    path = root / name
    assert not path.is_symlink(), name
    assert path.stat().st_size == expected["bytes"], name
    assert digest(path.read_bytes()) == expected["sha256"], name
checked_components = {}
for order, expected_components in [(1, 96), (3, 520)]:
    raw = json.loads((root / f"computations/results/kasner-r{order}-result.json").read_text())
    result = json.loads(raw["output"])
    assert raw["controller_status"] == "STOPPED" and raw["exit_code"] == 0
    assert not raw["oom_killed"] and not raw["timed_out"]
    limits = raw["limits"]
    assert 0 < limits["memory_plus_swap_bytes"] <= 2_000_000_000
    assert limits["nano_cpus"] <= 1_000_000_000 and limits["network"] == "none"
    assert limits["restart"] == "no" and limits["outer_wall_limit_seconds"] < 900
    assert result["status"] == "PASS" and result["max_r"] == order
    assert result["kasner_exponents"] == ["-2/7", "3/7", "6/7"]
    assert result["Lambda"] == 0 and result["at_t"] == 1
    assert {(entry["r"], entry["chirality"]) for entry in result["orders"]} == {
        (r, ch) for r in range(1, order + 1) for ch in ["+", "-"]}
    assert all(entry["recursion_residuals"] == entry["free_projection_residuals"] == 0
               for entry in result["orders"])
    assert sum(entry["components"] for entry in result["orders"]) == expected_components
    checked_components[str(order)] = expected_components

archive = root / "paper/exact-set-checks-v0.1.1.zip"
with zipfile.ZipFile(archive) as bundle:
    prefix = "exact-set-checks-v0.1.1/"
    saved = json.loads(bundle.read(prefix + "SHA256SUMS.json"))
    assert set(bundle.namelist()) == {prefix + name for name in saved} | {prefix + "SHA256SUMS.json"}
    for name, expected in saved.items():
        assert digest(bundle.read(prefix + name)) == expected, name
        if name.endswith(".py"):
            assert bundle.read(prefix + name) == (root / "computations/code" / name).read_bytes()
        elif name.endswith("-result.json"):
            assert bundle.read(prefix + name) == (root / "computations/results" / name).read_bytes()

status = json.loads((root / "docs/publication-status.json").read_text())
assert status["version"] == "1.0.1" and status["hexagon"]["submit"] is False
report = {"status": "PASS", "manifest_files": len(actual),
          "saved_components_by_max_order": checked_components,
          "original_companion_archive": "PASS", "mathematical_jobs_started": 0,
          "scope": "File integrity and saved-result checks, not a rerun or general proof."}
print(json.dumps(report, indent=2))

# File-only validation of the unchanged upstream execution evidence and new map.
import subprocess
import sys
upstream = root / 'computations/precursor'
process = subprocess.run([sys.executable, str(upstream/'code/verify_package.py')],
                         check=True, capture_output=True, text=True)
up_report = json.loads(process.stdout)
assert up_report['status']=='PASS' and up_report['checked_files']==85
coverage = json.loads((root/'computations/COVERAGE.json').read_text())
up_checks = json.loads((upstream/'checks.json').read_text())
expected = {x['id'] for x in up_checks['checks'] if x['id'].startswith(('KASNER-', 'AB-', 'B-'))}
assert expected == {x['id'] for x in coverage['selected_primary_records']}
assert len(expected)==14 and len(coverage['selected_independent_evidence'])==1
assert len(coverage['excluded_primary_records'])==14
assert coverage['current_source_sha256']==digest((root/'paper/manuscript.md').read_bytes())
origin = json.loads((root/'computations/UPSTREAM.json').read_text())
assert len(origin['files'])==85
for rel, value in origin['files'].items():
    assert digest((upstream/rel).read_bytes())==value, rel
print(json.dumps({'expanded_precursor_validation':'PASS','relevant_primary_records':14,
                  'independent_evidence_groups':1,'unchanged_upstream_files':85,
                  'mathematical_jobs_started':0},indent=2))
