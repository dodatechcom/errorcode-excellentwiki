---
title: "[Solution] Stopped Job Warning"
description: "Handle stopped jobs and SIGTSTP in Bash."
tools: ["bash"]
error-types: ["tool-error"]
severities: ["error"]
---

# [Solution] Stopped Job Warning

A background job has been stopped (usually via Ctrl+Z sending SIGTSTP).

### Common Causes
- Interactive program sent to background tried to read stdin.
- SIGTSTP signal sent manually.
- Terminal flow control.

### How to Fix
```bash
# List stopped jobs
jobs -l

# Resume in foreground
fg %1

# Resume in background
bg %1

# Send SIGCONT to specific PID
kill -CONT 1234

# Prevent stopping with nohup
nohup command &
```

### Example
```bash
# Broken
vim &    # stopped: needs terminal

# Fixed
vim      # run in foreground
# Or use nohup for long-running processes
nohup long_task &
```
