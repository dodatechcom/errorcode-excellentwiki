---
title: "[Solution] Assigning to Readonly Variable"
description: "Resolve 'readonly variable' error in Bash scripts."
tools: ["bash"]
error-types: ["tool-error"]
severities: ["error"]
---

# [Solution] Assigning to Readonly Variable

A variable marked `readonly` or with `-r` cannot be reassigned.

### Common Causes
- Reassigning a variable after `readonly` or `declare -r`.
- Modifying a read-only positional parameter.
- Attempting to unset a readonly variable.

### How to Fix
```bash
# Check if variable is readonly
readonly -p varname

# Use a different variable name
readonly CONST="value"
CONST="new"       # error
NEW_CONST="value" # works

# Temporarily disable (not recommended)
unset CONST 2>/dev/null || true
```

### Example
```bash
# Broken
readonly PI=3.14
PI=3.14159  # error: readonly variable

# Fixed
readonly PI=3.14
# Use a new variable for the adjusted value
PI_ADJUSTED=3.14159
```
