---
title: "[Solution] Indirect Expansion Error"
description: "Fix Bash indirect variable expansion (!) errors."
tools: ["bash"]
error-types: ["tool-error"]
severities: ["error"]
---

# [Solution] Indirect Expansion Error

Indirect expansion `${!var}` fails when the variable does not contain a valid variable name.

### Common Causes
- `var` contains a value that is not a valid variable name.
- Using `${!var}` on an unset variable.
- Bash version too old for indirect expansion.

### How to Fix
```bash
# Indirect expansion
var=" greeting"
greeting="hello"
echo "${!var}"    # prints 'hello'

# Validate before using
if [[ -n "${!ref:-}" ]]; then
    echo "${!ref}"
fi

# Use eval carefully (security risk)
eval "echo \$$ref"
```

### Example
```bash
# Broken
ref=""
echo "${!ref}"    # empty variable name error

# Fixed
ref="HOME"
echo "${!ref}"    # prints /home/user
```
