#!/usr/bin/env python3
"""Check every assertion used by the frozen output schema; never repair a reply."""
from pathlib import Path
import json, sys

ROOT = Path(__file__).resolve().parents[2]
SUPPORTED = {"$schema", "title", "type", "required", "properties", "items", "additionalProperties"}

def errors(value, schema, location="$"):
    unknown = set(schema) - SUPPORTED
    if unknown:
        return [f"{location}: unsupported schema keywords {sorted(unknown)}"]
    types = {"object": dict, "array": list, "string": str}
    expected = schema.get("type")
    if expected not in types:
        return [f"{location}: unsupported schema type {expected}"]
    if not isinstance(value, types[expected]):
        return [f"{location}: expected {expected}"]
    issues = []
    if isinstance(value, dict):
        for key in schema.get("required", []):
            if key not in value:
                issues.append(f"{location}: missing {key}")
        properties = schema.get("properties", {})
        if schema.get("additionalProperties") is False:
            for key in sorted(set(value) - set(properties)):
                issues.append(f"{location}: unexpected {key}")
        for key, item in value.items():
            if key in properties:
                issues.extend(errors(item, properties[key], location + "." + key))
    if isinstance(value, list) and "items" in schema:
        for index, item in enumerate(value):
            issues.extend(errors(item, schema["items"], location + f"[{index}]"))
    return issues

def validate(path):
    try:
        value = json.loads(Path(path).read_text())
    except (ValueError, OSError) as exc:
        return [f"Invalid or unreadable JSON: {exc}"]
    return errors(value, json.loads((ROOT / "core/output_schema.json").read_text()))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("Usage: python agents/team_promethean/validate_strict_response.py response.txt")
    found = validate(sys.argv[1])
    print("STRICT VALIDATION FAILED" if found else "STRICT VALIDATION PASSED")
    for issue in found:
        print("-", issue)
    sys.exit(1 if found else 0)
