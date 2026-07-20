---
title: "[Solution] BASH_XTRACEFD Error in Bash"
description: "Fix BASH_XTRACEFD file descriptor redirection errors."
tools: ["bash"]
error-types: ["tool-error"]
severities: ["error"]
---

# [Solution] BASH_XTRACEFD Error in Bash

`BASH_XTRACEFD` is used to redirect xtrace output to a file descriptor, but the fd is invalid.

### Common Causes
- File descriptor not opened before setting BASH_XTRACEFD.
- FD number is already in use.
- BASH_XTRACEFD set to invalid value.

### How to Fix
```bash
# Open file descriptor and redirect xtrace
exec {fd}> /tmp/trace.log
BASH_XTRACEFD=$fd
set -x
# ... commands ...
set +x
exec {fd}>&-

# Reset to default (stderr)
unset BASH_XTRACEFD
set -x

# Check current value
echo "$BASH_XTRACEFD"

# Use a safe pattern
trace_to_file() {
    local fd=$1
    local logfile=$2
    eval "exec {$fd}> $logfile"
    BASH_XTRACEFD=$fd
    set -x
}
```

### Example
```bash
# Broken
BASH_XTRACEFD=99    # fd 99 not open
set -x    # xtrace goes to nowhere

# Fixed
exec {fd}> /tmp/trace.log
BASH_XTRACEFD=$fd
set -x
# ... commands ...
set +x
exec {fd}>&-
```
