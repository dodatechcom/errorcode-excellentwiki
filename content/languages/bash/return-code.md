---
title: "[Solution] Bash Exit Status Code (Return Code) Check Failed"
description: "Fix exit status check failures in Bash when commands don't return the expected status code."
languages: ["bash"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["return-code", "exit-status", "error-checking"]
weight: 5
---

# Bash Exit Status Code (Return Code) Check Failed Fix

This error occurs when the exit status of a command doesn't match what the script expects, leading to incorrect error handling or unexpected behavior.

## Description

Bash scripts often check `$?` or use `if cmd; then...` to handle failures. When a command returns an unexpected exit code — or when the script continues past a failure it should have caught — downstream commands fail unpredictably.

## Common Causes

- **Not checking exit status** — script continues after a failed command.
- **`set -e` not used** — errors silently ignored, causing cascading failures.
- **`&&` and `||` misuse** — logical operators mask intermediate failures.
- **Function returns unexpected code** — return statement missing or using invalid values.

## How to Fix

### Fix 1: Always check exit status for critical commands

```bash
backup_data
if [[ $? -ne 0 ]]; then
    echo "Backup failed!" >&2
    exit 1
fi
```

### Fix 2: Use the idiom of checking directly

```bash
# Better — check the command directly, not $?
if ! backup_data; then
    echo "Backup failed!" >&2
    exit 1
fi
```

### Fix 3: Enable `set -e` for scripts that should fail fast

```bash
#!/bin/bash
set -e
set -o pipefail

critical_command
depends_on_critical
```

### Fix 4: Ensure functions return valid status codes

```bash
# Wrong — return value must be 0-255
my_func() {
    return 300  # Wraps to 44 (300 - 256)
}

# Right
my_func() {
    return 1  # Use conventional codes
}
```

## Examples

```bash
$ false
$ if true; then echo "ok"; else echo "failed"; fi
ok
# Wrong — always runs true, never checks false

$ set -e
$ false
$ echo "this won't run"
# Script exits immediately

$ function check() { return 1; }
$ check || echo "check failed"
check failed
```

## Related Errors

- [Exit Status](exit-status) — exit status code reference.
- [Pipe Failure](pipe-failure) — exit status with piped commands.
- [Signal Trap](signal-trap) — handling signals during execution.
