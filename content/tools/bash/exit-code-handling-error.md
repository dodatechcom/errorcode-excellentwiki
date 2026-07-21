---
title: "[Solution] Bash Exit Code Handling Error"
description: "Fix Bash exit code errors when scripts return incorrect or unexpected exit status codes."
tools: ["bash"]
error-types: ["tool-error"]
severities: ["warning"]
---

# Bash Exit Code Handling Error

Bash scripts return unexpected exit codes or fail to propagate errors correctly.

```
Script exited with status 0 despite command failure
```

## Common Causes

- Missing set -e causing silent failures
- Exit code overwritten by subsequent command
- Using return instead of exit in non-function context
- Pipelines hiding intermediate failures
- Trap not handling EXIT signal properly

## How to Fix

### Enable Strict Error Handling

```bash
#!/bin/bash
set -euo pipefail

# -e: exit on error
# -u: treat unset variables as error
# -o pipefail: return last non-zero exit code in pipeline
```

### Capture and Check Exit Codes

```bash
#!/bin/bash
set -e

command1
exit_code=$?

if [[ $exit_code -ne 0 ]]; then
    echo "command1 failed with exit code $exit_code" >&2
    exit "$exit_code"
fi
```

### Handle Pipeline Failures

```bash
# Without pipefail, only last command's exit code matters
set -o pipefail

# Check pipeline exit code
if ! output=$(cmd1 | cmd2 | cmd3); then
    echo "Pipeline failed with exit code $?" >&2
fi
```

### Use trap for Cleanup

```bash
#!/bin/bash
set -e

cleanup() {
    echo "Cleaning up..." >&2
    rm -f "$TEMP_FILE"
}
trap cleanup EXIT

TEMP_FILE=$(mktemp)
```

## Examples

```bash
# Proper exit code propagation
#!/bin/bash
set -euo pipefail

run_tests() {
    local failures=0
    for test in test_*.sh; do
        if ! bash "$test"; then
            ((failures++))
        fi
    done
    return "$failures"
}

if ! run_tests; then
    echo "Some tests failed" >&2
    exit 1
fi
```
