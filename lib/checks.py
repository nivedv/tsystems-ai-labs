"""The check function for Lab 2 (provided, so you can focus on the prompt).
Returns ONE reason: pass / not_json / schema_fail / summary_long."""
import json

from jsonschema import validate

REASONS = ["pass", "not_json", "schema_fail", "summary_long", "api_error"]


def check_triage(reply, schema):
    try:
        data = json.loads(reply)
    except Exception:
        return "not_json"
    try:
        validate(data, schema)
    except Exception:
        return "schema_fail"
    if len(data["summary"].split()) > 20:
        return "summary_long"
    return "pass"
