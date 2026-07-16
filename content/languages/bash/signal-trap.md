---
title: "[Solution] Bash Signal Handling Error"
description: "Fix signal handling and trap errors in Bash when signals aren't caught or handled properly."
languages: ["bash"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["signal-trap", "trap", "signal-handling"]
weight: 5
---

# Bash Signal Handling Error Fix

This error occurs when signal handling via `trap` is misconfigured or signals aren't properly caught during script execution.

## Description

Bash uses signals (like SIGINT, SIGTERM, EXIT) to communicate with running processes. The `trap` command lets you intercept these signals to perform cleanup or custom behavior. Misconfigured traps or unhandled signals can leave resources in inconsistent states.

## Common Causes

- **Missing EXIT trap for cleanup** — temp files and locks left behind on exit.
- **Signal number vs name confusion** — using numeric signals incorrectly.
- **Trap in subshell doesn't propagate** — traps set in subshells don't affect the parent.
- **Overwriting previous traps** — setting a new trap replaces the old one silently.

## How to Fix

### Fix 1: Always set an EXIT trap for cleanup

```bash
cleanup() {
    rm -f /tmp/myapp.lock
}
trap cleanup EXIT
```

### Fix 2: Use signal names instead of numbers

```bash
# Wrong — fragile, platform-dependent
trap "echo caught" 1 2 15

# Right — use names
trap "echo caught" HUP INT TERM
```

### Fix 3: Chain multiple signals with braces

```bash
trap 'echo "Caught signal"; cleanup' EXIT INT TERM HUP
```

### Fix 4: Preserve previous traps while adding new behavior

```bash
# Save and chain existing trap
eval "old_cleanup() { $(trap -p EXIT | sed "s/trap -- '//;s/' EXIT//") }"
new_cleanup() {
    old_cleanup
    my_cleanup
}
trap new_cleanup EXIT
```

## Examples

```bash
$ trap 'echo "Goodbye"' EXIT
$ exit
Goodbye

$ trap -l  # List all signals
 1) SIGHUP       2) SIGINT       3) SIGQUIT      4) SIGILL

$ trap 'echo "Ctrl+C caught"' INT
$ # Ctrl+C
Ctrl+C caught
```

## Related Errors

- [Exit Status](exit-status) — understanding exit codes when signals terminate scripts.
- [Pipe Failure](pipe-failure) — signal-related issues in pipelines.
