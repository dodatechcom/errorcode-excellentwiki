---
title: "[Solution] Job Not Found Error"
description: "Resolve 'job not found' errors with fg, bg, and jobs in Bash."
tools: ["bash"]
error-types: ["tool-error"]
severities: ["error"]
---

# [Solution] Job Not Found Error

The job ID or process referenced does not exist in the current session.

### Common Causes
- Job has already completed.
- Job was started in a different subshell.
- Using job ID after the shell session was restarted.

### How to Fix
```bash
# List current jobs
jobs -l

# Bring specific job to foreground
%1        # job number 1
%+        # current job
%-        # previous job

# Check if process is running
ps aux | grep process_name

# Use PID instead of job ID
kill %1    # by job number
kill 1234  # by PID
```

### Example
```bash
# Broken
sleep 100 &
jobs
# job finishes before next command
fg %1     # job not found

# Fixed
sleep 100 &
jobs -l   # see PID
fg %1     # works while job is running
```
