---
title: "[Solution] Bash Trap Error"
description: "Fix bash trap errors when signal handlers are set incorrectly, trap functions fail, or trap cleanup doesn't execute."
languages: ["bash"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["trap", "signal", "cleanup", "err", "exit"]
weight: 5
---

# Bash Trap Error Fix

Trap errors occur when signal handlers are set incorrectly, the trap function produces errors, or cleanup code doesn't execute on script exit.

## What This Error Means

The `trap` command registers signal handlers that execute code when signals are received (EXIT, INT, TERM, ERR, etc.). Errors happen when the trap command itself has syntax issues or the handler function fails.

## Common Causes

- Trap command syntax error (missing signal name)
- Handler function not defined before trap
- Recursive trap (handler triggering itself)
- Trap in subshell doesn't affect parent
- Missing quotes around handler code

## How to Fix

### 1. Define handler before trap

```bash
# WRONG: function not yet defined
trap cleanup EXIT
cleanup() { rm -f /tmp/lockfile; }

# RIGHT: define function first
cleanup() { rm -f /tmp/lockfile; }
trap cleanup EXIT
```

### 2. Use proper trap syntax

```bash
# WRONG: missing signal
trap 'echo "cleaning"'

# RIGHT: with signal
trap 'echo "cleaning"' EXIT
```

### 3. Prevent recursive traps

```bash
# WRONG: handler might trigger ERR recursively
trap 'echo "Error on line $LINENO"' ERR

# RIGHT: disable trap inside handler
trap_handler() {
    trap - ERR  # Temporarily disable
    echo "Error occurred"
    # cleanup code
}
trap trap_handler ERR
```

### 4. Handle EXIT trap in subshells

```bash
# Subshell trap doesn't affect parent
( trap 'echo "done"' EXIT; sleep 1 )
# Parent doesn't see this trap
```

## Related Errors

- [Signal Trap](signal-trap) — signal handling behavior
- [Return Code](return-code) — exit status handling
