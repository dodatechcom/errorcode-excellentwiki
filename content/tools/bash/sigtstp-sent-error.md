---
title: "[Solution] SIGTSTP Signal Sent Error"
description: "Handle SIGTSTP (terminal stop) signal errors in Bash."
tools: ["bash"]
error-types: ["tool-error"]
severities: ["error"]
---

# [Solution] SIGTSTP Signal Sent Error

A process received SIGTSTP (signal 20), typically from Ctrl+Z or `kill -TSTP`.

### Common Causes
- Interactive program run in background.
- Terminal flow control (Ctrl+Z).
- Explicit `kill -TSTP` sent to process.

### How to Fix
```bash
# Send SIGTSTP to a process
kill -TSTP 1234

# Resume the process
kill -CONT 1234

# Prevent SIGTSTP with nohup
nohup command &

# Trap SIGTSTP in a script
trap 'echo "Received SIGTSTP"; sleep 1; kill -CONT $$' TSTP
```

### Example
```bash
# Broken
long_running_process &
kill -TSTP $!    # process stopped, need to resume

# Fixed
long_running_process &
kill -TSTP $!
# later
kill -CONT $!
```
