#!/usr/bin/env python3
"""Verify observed UI text without editing or repairing any model reply."""
from pathlib import Path
from datetime import datetime, timezone
import json, hashlib, runpy, subprocess, sys

ROOT = Path(__file__).resolve().parents[3]
RUN = Path(__file__).resolve().parent
checker = runpy.run_path(str(ROOT / "records/observed_tests/run_checks.py"))["schema_check"]
schema = json.loads((ROOT / "core/output_schema.json").read_text())
summary = []
print("UTC execution:", datetime.now(timezone.utc).isoformat())
print("Tested source commit: 4e5dc3d45ff3123ec532cd14bb6217e8917f6501")
print("Each reply is unedited displayed UI text; source page snapshot is retained.")
for name in ("primary", "posture_contrast", "application_contrast", "hype", "insufficient"):
    folder = RUN / name
    raw = (folder / "raw_response.txt").read_bytes()
    prompt = (folder / "prompt.txt").read_bytes()
    expected = (ROOT / "work" / ("team_promethean_" + name + "_prompt.txt")).read_bytes()
    runtime = json.loads((folder / "runtime.json").read_text())
    print("\nCASE", name)
    print("PROMPT_BYTE_IDENTITY", prompt == expected)
    assert prompt == expected
    state = runtime["state"]
    assert state["operation"]["terminal"] == "settled" and state["operation"]["outcome"] == "complete"
    assert state["messageCount"] == 2
    assert all(m["complete"] and not m["streaming"] for m in state["messages"])
    print("COMPLETED_CONVERSATION", state["conversationId"])
    reply = json.loads(raw)
    basic = subprocess.run([sys.executable, str(ROOT / "tools/validate_response.py"), str(folder / "raw_response.txt")], text=True, capture_output=True)
    print("FROZEN_BASIC_VALIDATOR_EXIT", basic.returncode)
    print(basic.stdout.strip())
    errors = []
    try:
        checker(reply, schema)
    except AssertionError as error:
        errors.append(str(error))
    extra = sorted(set(reply) - set(schema["properties"]))
    if extra:
        print("UNEXPECTED_TOP_LEVEL_FIELDS", json.dumps(extra))
    print("STRICT_SCHEMA", "FAIL" if errors else "PASS")
    if errors:
        print("STRICT_ERROR", repr(errors[0]))
    print("RAW_SHA256", hashlib.sha256(raw).hexdigest())
    print("MODEL_EXPOSED", json.dumps(runtime["model_observation"]["selected"]))
    summary.append({"case": name, "prompt_identical": True, "completed": True,
        "basic_validator_exit": basic.returncode, "strict_schema": "FAIL" if errors else "PASS",
        "strict_errors": errors, "unexpected_top_level_fields": extra,
        "raw_sha256": hashlib.sha256(raw).hexdigest(), "prompt_sha256": hashlib.sha256(prompt).hexdigest(),
        "conversation_id": state["conversationId"], "observed_url": runtime["url"],
        "model": runtime["model_observation"]["selected"], "underlying_model_id": "not exposed"})
print("\nCOMPLETED_RUNS", len(summary))
print("STRICT_SCHEMA_PASSES", sum(r["strict_schema"] == "PASS" for r in summary), "of", len(summary))
print("Behavioral findings are separately documented AI review, not inferred from schema validity.")
(RUN / "validation_results.json").write_text(json.dumps(summary, indent=2) + "\n")
sys.exit(1 if any(r["strict_schema"] == "FAIL" for r in summary) else 0)
