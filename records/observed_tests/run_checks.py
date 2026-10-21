#!/usr/bin/env python3
"""Deterministic artifact checks; never executes a model or verifies source truth."""
import hashlib
import json
from pathlib import Path
import subprocess
import sys
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[2]
CASES = ("primary", "posture_contrast", "application_contrast", "hype", "insufficient")

def read(path):
    return json.loads((ROOT / path).read_text())

def schema_check(value, schema, where="$"):
    # Covers every assertion keyword used by the supplied frozen schemas.
    supported = {"$schema", "title", "type", "required", "properties", "items", "additionalProperties"}
    assert not set(schema) - supported, (where, "unsupported schema keywords")
    types = {"object": dict, "array": list, "string": str}
    if "type" in schema:
        assert schema["type"] in types, (where, "unsupported schema type")
        assert isinstance(value, types[schema["type"]]), (where, "wrong type")
    if isinstance(value, dict):
        assert set(schema.get("required", [])) <= value.keys(), (where, "missing field")
        props = schema.get("properties", {})
        if schema.get("additionalProperties") is False:
            assert set(value) <= props.keys(), (where, "extra field")
        for key, item in value.items():
            if key in props:
                schema_check(item, props[key], where + "." + key)
    elif isinstance(value, list) and "items" in schema:
        for index, item in enumerate(value):
            schema_check(item, schema["items"], where + "[" + str(index) + "]")

def command(*args):
    result = subprocess.run([sys.executable, *args], cwd=ROOT, text=True, capture_output=True)
    print("$ python " + " ".join(args), flush=True)
    # Avoid local temporary absolute paths in the published log.
    print((result.stdout + result.stderr).replace(str(ROOT), "<repository>"), end="", flush=True)
    assert result.returncode == 0, result.returncode

def main():
    print("UTC execution time:", datetime.now(timezone.utc).isoformat(), flush=True)
    print("Package: 0.1.1-team; original repository snapshot: 98022f0", flush=True)
    print("Scope: saved artifacts and deterministic checks; no fresh model execution.", flush=True)
    command("tools/check_frozen_core.py")
    ins, outs = read("core/input_schema.json"), read("core/output_schema.json")
    cases, responses = {}, {}
    for name in CASES:
        case = "agents/team_promethean/cases/" + name + ".json"
        reply = "agents/team_promethean/responses/" + name + "_response.json"
        cases[name], responses[name] = read(case), read(reply)
        schema_check(cases[name], ins)
        schema_check(responses[name], outs)
        command("tools/build_prompt.py", "--agent", "agents/team_promethean", "--case", case)
        command("tools/validate_response.py", reply)
        print("PASS frozen-schema assertions:", name, flush=True)
    diff = {k for k in cases["primary"] if cases["primary"][k] != cases["posture_contrast"][k]}
    assert diff == {"adoption_posture"}, diff
    print("PASS posture intake changes adoption_posture only", flush=True)
    general = {responses[n]["general_et_finding"] for n in CASES if n != "insufficient"}
    assert len(general) == 1
    print("PASS saved general findings identical across primary/posture/application/hype", flush=True)
    for name in ("posture_contrast", "application_contrast", "hype"):
        assert responses[name]["recommendation_management_implication"] != responses["primary"]["recommendation_management_implication"]
    assert "abstain" in responses["insufficient"]["general_et_finding"].lower()
    assert responses["insufficient"]["abstention_or_more_information_needed"]
    print("PASS saved local recommendations differ and insufficient case abstains", flush=True)
    base = ROOT / "records/observed_tests/inherited_quantum"
    for name in ("primary", "contrast_1", "contrast_2"):
        raw = base / ("responses/chatgpt_v04_" + name + "_raw.txt")
        paired = base / ("responses/v04_" + name + "_response.json")
        assert raw.read_bytes() == paired.read_bytes(), name
        reply = json.loads(raw.read_text())
        schema_check(reply, outs)
        assert reply["agent"]["version"] == "0.4"
        print("PASS inherited raw/JSON byte identity and schema:", name, flush=True)
        print("raw_sha256", hashlib.sha256(raw.read_bytes()).hexdigest(), flush=True)
    print("PASS all artifact checks. Fresh-session team-agent replay remains OPEN.", flush=True)

if __name__ == "__main__":
    main()
