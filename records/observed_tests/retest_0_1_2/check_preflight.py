#!/usr/bin/env python3
from pathlib import Path
import hashlib, json, subprocess, sys
from datetime import datetime, timezone
ROOT = Path(__file__).resolve().parents[3]
RUN = Path(__file__).resolve().parent
print("UTC execution:", datetime.now(timezone.utc).isoformat())
print("Model replies: unavailable; no model result is assessed by this script.")
p = subprocess.run([sys.executable, "tools/check_frozen_core.py"], cwd=ROOT, capture_output=True, text=True)
print(p.stdout.strip())
assert p.returncode == 0
for name in ("primary", "posture_contrast", "application_contrast", "hype", "insufficient"):
    data = (RUN / name / "prompt.txt").read_bytes()
    expected = (ROOT / "work" / ("team_promethean_" + name + "_prompt.txt")).read_bytes()
    assert data == expected, name
    print(name, "PREPARED_PROMPT_MATCH", hashlib.sha256(data).hexdigest())
    baseline = ROOT / "records/observed_tests/live_20261020" / name / "raw_response.txt"
    result = subprocess.run([sys.executable, str(ROOT / "agents/team_promethean/validate_strict_response.py"), str(baseline)], capture_output=True, text=True)
    expected_code = 0 if name == "posture_contrast" else 1
    assert result.returncode == expected_code, (name, result.stdout)
    print(name, "BASELINE_STRICT_VALIDATOR_EXIT", result.returncode)
    print(result.stdout.strip())
print("PASS preflight and baseline-validator regression checks. Revised model acceptance remains pending.")
