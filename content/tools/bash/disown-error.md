---
title: "[Solution] Disown Error in Bash"
description: "Fix 'disown' job control errors in Bash."
tools: ["bash"]
error-types: ["tool-error"]
severities: ["error"]
---

# [Solution] Disown Error in Bash

The `disown` command failed to remove the job from the job table.

### Common Causes
- Job ID does not exist.
- Job has already completed.
- Using `disown` on a job from a different subshell.

### How to Fix
```bash
# List current jobs
jobs -l

# Disown specific job
command &
disown %1

# Disown all jobs
disown -a

# Disown without sending SIGHUP
disown -h %1

# Use nohup as alternative
nohup command &
```

### Example
```bash
# Broken
command &
# ... time passes, job finishes ...
disown %1    # error: no such job

# Fixed
command &
disown %1    # immediately after backgrounding
```
