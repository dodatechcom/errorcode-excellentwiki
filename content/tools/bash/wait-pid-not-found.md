---
title: "[Solution] Wait PID Not Found Error"
description: "Resolve 'wait: pid not a child' errors in Bash."
tools: ["bash"]
error-types: ["tool-error"]
severities: ["error"]
---

# [Solution] Wait PID Not Found Error

The `wait` command is given a PID that is not a child of the current shell.

### Common Causes
- Waiting on a PID from a different shell.
- Process already exited.
- PID was reassigned to a different process.

### How to Fix
```bash
# Wait for specific child process
command &
PID=$!
wait "$PID"
echo "Exit code: $?"

# Wait for all background jobs
wait

# Wait with timeout (Bash 4.3+)
wait -n    # wait for next child to finish
wait -t 10 $PID    # wait up to 10 seconds

# Check if PID is a child
jobs -l
```

### Example
```bash
# Broken
PID=1234    # from different shell
wait "$PID" # error: not a child

# Fixed
command &
PID=$!
wait "$PID" # correct
```
