---
title: "[Solution] fg/bg Job Control Error"
description: "Fix foreground and background job control errors in Bash."
tools: ["bash"]
error-types: ["tool-error"]
severities: ["error"]
---

# [Solution] fg/bg Job Control Error

The `fg` or `bg` command cannot operate on the specified job.

### Common Causes
- No current job to send to foreground/background.
- Job ID syntax is wrong.
- Job control is disabled in non-interactive shell.

### How to Fix
```bash
# Check job control is enabled
set -m    # enable job control
set +m    # disable job control

# List available jobs
jobs -l

# fg sends job to foreground
fg %1

# bg resumes job in background
bg %1

# Check if interactive
[[ $- == *i* ]] && echo "interactive" || echo "non-interactive"
```

### Example
```bash
# Broken (non-interactive shell)
command &
fg %1    # fg: no job control

# Fixed: ensure interactive shell or use different approach
#!/bin/bash
set -m    # enable job control
command &
fg %1
```
