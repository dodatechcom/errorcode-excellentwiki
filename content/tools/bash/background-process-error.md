---
title: "[Solution] Background Process Error"
description: "Fix background process errors in Bash scripts."
tools: ["bash"]
error-types: ["tool-error"]
severities: ["error"]
---

# [Solution] Background Process Error

A background process failed or reported an error.

### Common Causes
- Process tries to read from terminal in background.
- Process depends on a terminal it cannot access.
- SIGHUP sent when parent shell exits.

### How to Fix
```bash
# Use nohup to prevent hangup
nohup command &

# Redirect all I/O for background processes
command </dev/null >output.log 2>&1 &

# Disown to remove from job table
command &
disown

# Use setsid for completely independent process
setsid command </dev/null >output.log 2>&1
```

### Example
```bash
# Broken
sleep 5 &    # may receive SIGHUP when shell exits

# Fixed
nohup sleep 5 >/dev/null 2>&1 &
disown
```
