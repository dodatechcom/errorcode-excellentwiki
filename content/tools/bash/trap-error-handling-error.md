---
title: "[Solution] Bash Trap Error Handling Error"
description: "Fix Bash trap signal handling errors when traps fail to execute or cause unexpected behavior."
tools: ["bash"]
error-types: ["tool-error"]
severities: ["error"]
---

# Bash Trap Error Handling Error

Bash trap signals fail to fire or cause unexpected behavior during script execution.

```
trap: ERR: bad signal name
trap: 'function_name': not a valid signal specification
```

## Common Causes

- Invalid signal name in trap
- Trap function calls a command that fails
- Recursive trap invocation
- Trap defined after signal already received
- Trap function references unset variables

## How to Fix

### Use Valid Signal Names

```bash
# List available signals
trap -l

# Correct trap syntax
trap 'cleanup' EXIT INT TERM
trap 'error_handler' ERR
trap '' HUP  # Ignore SIGHUP
```

### Error Trap with Function

```bash
#!/bin/bash
set -e

error_handler() {
    local exit_code=$?
    echo "Error on line $LINENO, exit code: $exit_code" >&2
    cleanup
    exit "$exit_code"
}
trap error_handler ERR

cleanup() {
    rm -f "${TEMP_FILES[@]}"
}
trap cleanup EXIT
```

### Prevent Recursive Traps

```bash
error_handler() {
    # Disable trap to prevent recursion
    trap - ERR
    echo "Handling error..." >&2
    cleanup
    exit 1
}
trap error_handler ERR
```

### Handle Multiple Signals

```bash
#!/bin/bash
TEMP_FILE=$(mktemp)

cleanup() {
    rm -f "$TEMP_FILE"
}
trap cleanup EXIT

on_interrupt() {
    echo "Interrupted, cleaning up..." >&2
    exit 130
}
trap on_interrupt INT TERM

# Main script logic
while true; do
    process_data >> "$TEMP_FILE"
done
```

## Examples

```bash
#!/bin/bash
# Robust trap setup
set -euo pipefail

on_error() {
    echo "ERROR: Script failed at line $1" >&2
    echo "Command: $2" >&2
    exit 1
}

trap 'on_error ${LINENO} "${BASH_COMMAND}"' ERR
trap 'echo "Interrupted"; exit 130' INT TERM
trap 'echo "Cleaned up"; rm -f /tmp/myapp_*' EXIT
```
