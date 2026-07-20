---
title: "[Solution] Nameref Not Found Error"
description: "Resolve 'nameref not found' error in Bash nameref variables."
tools: ["bash"]
error-types: ["tool-error"]
severities: ["error"]
---

# [Solution] Nameref Not Found Error

A `nameref` (namered) variable references a variable that does not exist.

### Common Causes
- `declare -n ref=target` where `target` is undefined.
- `target` variable name itself is invalid.
- Using nameref in a subshell where target was local.

### How to Fix
```bash
# Ensure target variable exists
target="hello"
declare -n ref=target
echo "$ref"    # hello

# Check variable existence
if declare -p target &>/dev/null; then
    declare -n ref=target
fi

# Avoid namerefs in subshells
```

### Example
```bash
# Broken
declare -n ref=nonexistent
echo "$ref"    # error

# Fixed
nonexistent="value"
declare -n ref=nonexistent
echo "$ref"    # value
```
