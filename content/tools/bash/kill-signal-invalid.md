---
title: "[Solution] Invalid Kill Signal Error"
description: "Fix 'invalid signal specification' errors with kill in Bash."
tools: ["bash"]
error-types: ["tool-error"]
severities: ["error"]
---

# [Solution] Invalid Kill Signal Error

The signal name or number given to `kill` is not valid.

### Common Causes
- Typo in signal name (e.g., `SIGKIL`).
- Signal number out of range.
- Using signal name in non-interactive context.

### How to Fix
```bash
# List available signals
kill -l

# Common signals
kill -TERM 1234    # graceful shutdown
kill -KILL 1234    # force kill (cannot be trapped)
kill -HUP 1234     # hangup / reload
kill -INT 1234     # interrupt

# Use signal number
kill -15 1234      # SIGTERM
kill -9 1234       # SIGKILL

# Send to process group
kill -- -1234      # all processes in group
```

### Example
```bash
# Broken
kill -SIGKIL 1234    # typo

# Fixed
kill -9 1234         # or
kill -KILL 1234
```
