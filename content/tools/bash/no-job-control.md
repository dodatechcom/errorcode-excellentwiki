---
title: "[Solution] No Job Control in Non-Interactive Shell"
description: "Resolve 'no job control' errors in Bash scripts."
tools: ["bash"]
error-types: ["tool-error"]
severities: ["error"]
---

# [Solution] No Job Control in Non-Interactive Shell

Job control features (fg, bg, Ctrl+Z) are disabled in non-interactive shells.

### Common Causes
- Script runs non-interactively (piped or crontab).
- `set +m` was called.
- Running in a subshell.

### How to Fix
```bash
# Enable job control in scripts (may not work everywhere)
set -m

# Check if interactive
if [[ $- == *i* ]]; then
    echo "Interactive: job control available"
else
    echo "Non-interactive: no job control"
fi

# Use process management without job control
command &
PID=$!
wait "$PID"
```

### Example
```bash
# Broken
#!/bin/bash
command &
fg %1    # no job control in script

# Fixed
#!/bin/bash
command &
PID=$!
wait "$PID"
```
