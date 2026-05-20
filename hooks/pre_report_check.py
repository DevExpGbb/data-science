#!/usr/bin/env python3
"""
Pre-report validation hook.
Reads tool invocation context from stdin and blocks report generation
if data quality checks fail.

Exit codes:
  0 - validation passed, allow tool use
  2 - validation failed, block tool use
"""
import json
import sys


def main():
    try:
        event = json.load(sys.stdin)
    except (json.JSONDecodeError, ValueError):
        # If we can't parse input, allow through
        sys.exit(0)

    tool_name = event.get("tool_name", "")

    # Only gate on report-generating tools
    if tool_name not in ("execute", "edit"):
        sys.exit(0)

    # Check for required data files
    import os
    data_dir = "data"
    if not os.path.isdir(data_dir) or not os.listdir(data_dir):
        result = {
            "continue": False,
            "stopReason": "Pre-report check failed: no data files found in ./data/",
            "hookSpecificOutput": {
                "hookEventName": "PreToolUse",
                "permissionDecision": "deny",
                "permissionDecisionReason": "No data available for report generation."
            }
        }
        print(json.dumps(result))
        sys.exit(2)

    sys.exit(0)


if __name__ == "__main__":
    main()
