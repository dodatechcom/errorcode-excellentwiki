---
title: "[Solution] Bash Trap Err Error -- Incorrect ERR Signal Handling"
description: "Fix bash trap ERR errors when using trap ERR for error handling in functions."
languages: ["bash"]
error-types: ["runtime-error"]
severities: ["error"]
---

# Bash Trap Err Error

This error occurs when `trap ERR` is not triggered as expected due to shell option settings.

## Common Causes

- `trap ERR` not triggering in functions by default
- `set -e` interacting with ERR trap unexpectedly
- ERR trap inherited by shell functions but not subshells
- Error handler itself causing an error

## How to Fix

### Enable ERR trap in functions

```bash
# WRONG: ERR not triggered in functions
err_handler() {
    echo "Error on line $LINENO"
}
trap err_handler ERR

my_func() {
    false  # this does NOT trigger ERR by default
}

# CORRECT: use set -E for function inheritance
set -E
trap 'echo "Error on line $LINENO"' ERR
```

### Handle errors carefully

```bash
set -E
trap 'echo "Error in ${FUNCNAME[0]:-main} at line $LINENO"' ERR

risky_command || true  # don't trigger ERR
```

## Examples

```bash
#!/bin/bash
set -E
trap 'echo "Error at line $LINENO in ${FUNCNAME[0]:-main}"' ERR

process() {
    false  # this triggers ERR
}

process
```
