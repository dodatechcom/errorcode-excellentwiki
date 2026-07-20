---
title: "[Solution] Trap Command Error"
description: "Fix trap signal handler errors in Bash scripts."
tools: ["bash"]
error-types: ["tool-error"]
severities: ["error"]
---

# [Solution] Trap Command Error

The `trap` command has invalid syntax or references an invalid signal.

### Common Causes
- Invalid signal name in trap.
- Trap handler has syntax errors.
- Using trap in non-bash shell.

### How to Fix
```bash
# Correct trap syntax
trap 'echo "Caught signal"' INT TERM

# Clean up temp files on exit
cleanup() {
    rm -f /tmp/mytempfile_$$
}
trap cleanup EXIT

# Reset a trap
trap - INT TERM    # remove handlers

# Ignore signal
trap '' INT TERM    # signals are ignored

# List active traps
trap -p
```

### Example
```bash
# Broken
trap 'echo error' INVALID_SIGNAL

# Fixed
trap 'echo "cleaning up"; rm -f "$tmpfile"' EXIT INT TERM
```
