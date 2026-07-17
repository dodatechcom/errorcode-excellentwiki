---
title: "[Solution] Bash Trap: Invalid Signal Specification Error Fix"
description: "Fix bash trap invalid signal errors. Learn how to properly set signal traps in bash scripts."
languages: ["bash"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Bash Trap: Invalid Signal Specification Error Fix

A bash trap signal error occurs when you specify an invalid signal name or number in the `trap` command.

## What This Error Means

The `trap` command registers handlers for signals. If you provide a signal name that doesn't exist (e.g., `SIGTYPO`), bash reports "invalid signal specification."

## Common Causes

- Typo in signal name (e.g., `SIGINTT` instead of `SIGINT`)
- Using wrong signal number
- Using platform-specific signals not available on all systems
- Missing signal name argument

## How to Fix

### 1. Use correct signal names

```bash
# WRONG: Typo in signal name
trap 'echo "caught"' SIGINTT

# CORRECT: Use valid signal name
trap 'echo "caught"' SIGINT
```

### 2. List available signals

```bash
# Check available signals
kill -l

# Use numeric signal codes
trap 'echo "caught"' 2  # SIGINT
```

### 3. Handle common signals properly

```bash
# CORRECT: Handle common signals
cleanup() {
    rm -f /tmp/lockfile
    echo "Cleaned up"
}
trap cleanup EXIT INT TERM
```

### 4. Use ERR for error handling

```bash
# CORRECT: Trap errors
trap 'echo "Error on line $LINENO"' ERR
set -e
```

## Related Errors

- [Signal Trap](signal-trap) — signal handling behavior
- [Return Code](return-code) — exit status handling
- [Command Not Found](command-not-found) — missing commands
