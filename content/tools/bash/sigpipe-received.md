---
title: "[Solution] SIGPIPE Signal Received"
description: "Handle SIGPIPE (signal 13) errors in Bash scripts."
tools: ["bash"]
error-types: ["tool-error"]
severities: ["error"]
---

# [Solution] SIGPIPE Signal Received

The process received SIGPIPE, meaning it wrote to a pipe with no reader.

### Common Causes
- Downstream command exited early.
- Piped command failed before upstream finished.
- Script receives SIGPIPE unexpectedly.

### How to Fix
```bash
# Ignore SIGPIPE
trap '' PIPE

# Check for broken pipe in pipeline
set -o pipefail
command1 | command2
echo "command2 exit: ${PIPESTATUS[1]}"

# Use pipefail to detect pipeline failures
set -o pipefail
if command1 | command2; then
    echo "pipeline succeeded"
else
    echo "pipeline failed"
fi
```

### Example
```bash
# Broken (SIGPIPE causes script to exit)
#!/bin/bash
set -e
head -1 < <(yes)    # may get SIGPIPE

# Fixed
trap '' PIPE
head -1 < <(yes)
```
