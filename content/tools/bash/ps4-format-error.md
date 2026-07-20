---
title: "[Solution] PS4 Format and Xtrace Prompt Error"
description: "Fix PS4 custom xtrace prompt format errors in Bash."
tools: ["bash"]
error-types: ["tool-error"]
severities: ["error"]
---

# [Solution] PS4 Format and Xtrace Prompt Error

The `PS4` variable has invalid format specifiers or is not set correctly.

### Common Causes
- Using undefined `PS4` variable references.
- `PS4` set before sourcing the file it references.
- Invalid escape sequences in PS4.

### How to Fix
```bash
# Common PS4 with file and line number
export PS4='+${BASH_SOURCE[0]:-unknown}:${LINENO}: ${FUNCNAME[0]:-main}: '

# With timestamp
export PS4='+$(date +%T.%N) ${BASH_SOURCE[0]}:${LINENO}: '

# Check current PS4
echo "$PS4"

# Safe PS4 with all defaults
PS4='+${BASH_SOURCE:-?}:${LINENO}:${FUNCNAME:-?}: '

# Enable xtrace with custom PS4
set -x
```

### Example
```bash
# Broken
export PS4='+${nonexistent_var}:${LINENO}: '    # unbound variable

# Fixed
export PS4='+${BASH_SOURCE[0]:-?}:${LINENO}: '
set -x
```
