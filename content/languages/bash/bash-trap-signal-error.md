---
title: "[Solution] Bash Trap Invalid Signal Specification Error Fix"
description: "Fix 'trap: invalid signal specification' in Bash. Learn correct trap syntax for signal handling in shell scripts."
languages: ["bash"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Bash Trap Invalid Signal Specification Error Fix

The `trap: invalid signal specification` error occurs when you provide an unrecognized signal name, number, or malformed syntax to the `trap` command in Bash.

## What This Error Means

The `trap` command in Bash is used to catch signals and execute code when they are received. When Bash cannot parse the signal specification you provide, it throws this error. The trap will not be set, leaving your script vulnerable to unexpected termination.

A typical error looks like:

```
bash: trap: SIGINVALID: invalid signal specification
```

## Why It Happens

This error is caused by:

- **Typo in signal name** — Using `SIGKIL` instead of `SIGKILL` or `KILL`.
- **Using signal numbers incorrectly** — Passing `9` instead of `SIGKILL` or not prefixing with `SIG`.
- **Missing or extra arguments** — Calling `trap` with insufficient parameters.
- **Using platform-specific signals** — Some signals exist only on certain operating systems.
- **Improper quoting** — Signal names containing special characters are not quoted.
- **Mixing signal numbers and names** — Using `trap 'echo hi' 0 SIGINT` with incompatible formats.

## How to Fix It

### Fix 1: Use correct signal names with SIG prefix

```bash
# WRONG: Invalid signal name
trap 'echo " caught"' SIGINVALID

# RIGHT: Use valid signal names
trap 'echo "Interrupt caught"' SIGINT
trap 'echo "Terminated"' SIGTERM
trap 'echo "Hangup"' SIGHUP
```

### Fix 2: Use numeric signal codes correctly

```bash
# Signal numbers work without SIG prefix
trap 'echo "Interrupt"' 2
trap 'echo "Terminated"' 15
trap 'echo "Hangup"' 1

# Or with SIG prefix
trap 'echo "Interrupt"' SIG2  # This also works
```

### Fix 3: List all valid signals before using them

```bash
# List all available signals
trap -l

# Common signals and their numbers
# SIGHUP    = 1    hangup
# SIGINT    = 2    interrupt
# SIGQUIT   = 3    quit
# SIGKILL   = 9    kill
# SIGTERM   = 15   terminate
# SIGSTOP   = 17,19,23  stop
```

### Fix 4: Handle traps properly with quotes

```bash
# WRONG: Unquoted command with spaces
trap echo caught SIGINT

# RIGHT: Quote the command string
trap 'echo "caught"' SIGINT

# Use function for complex logic
cleanup() {
    echo "Cleaning up..."
    rm -f /tmp/lockfile
}
trap cleanup EXIT INT TERM
```

### Fix 5: Use EXIT signal for cleanup

```bash
#!/bin/bash
# EXIT trap always fires regardless of signal
cleanup() {
    echo "Script ending, cleaning up..."
    rm -f /tmp/myapp.lock
}
trap cleanup EXIT

# Your script logic here
echo "Running..."
sleep 5
```

### Fix 6: Ignore specific signals safely

```bash
# Ignore SIGINT (Ctrl+C) during critical section
trap '' SIGINT
echo "Critical operation in progress..."
# ... critical code here ...
trap - SIGINT  # Restore default behavior
```

## Common Mistakes

- **Using `KILL` instead of `SIGKILL`** — The `kill -9` signal cannot be trapped.
- **Forgetting that `SIGKILL` and `SIGSTOP` cannot be caught** — These signals bypass traps entirely.
- **Not quoting the command string** — Always wrap the command in single quotes.
- **Using `trap` without arguments to view current traps** — Run `trap -p` to see active traps.
- **Assuming signals work the same across platforms** — macOS and Linux differ on signal numbers.

## Related Pages

- [Bash Arithmetic Error](arithmetic-error) — Syntax errors in Bash expressions
- [Bash Syntax Error](bash-syntax-error) — General Bash syntax issues
- [Bash Recursive Descent](bash-recursive-descent) — Stack overflow in scripts
