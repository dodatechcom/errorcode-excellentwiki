---
title: "[Solution] Regex Matching Error in [[ ]]"
description: "Fix regex matching errors with =~ in Bash [[ ]]."
tools: ["bash"]
error-types: ["tool-error"]
severities: ["error"]
---

# [Solution] Regex Matching Error in [[ ]]

The `=~` regex operator in `[[ ]]` has an invalid pattern.

### Common Causes
- Unquoted regex pattern (subject to word splitting).
- Invalid regex syntax.
- Using `=~` in `[ ]` instead of `[[ ]]`.

### How to Fix
```bash
# Use =~ inside [[ ]] only
[[ "$var" =~ ^[0-9]+$ ]]    # check if numeric

# Store regex in variable (Bash 3.2+)
re='^[0-9]+$'
[[ "$var" =~ $re ]]

# Capture groups (Bash 3.0+)
if [[ "$var" =~ ([0-9]+)-([0-9]+) ]]; then
    echo "Start: ${BASH_REMATCH[1]}"
    echo "End: ${BASH_REMATCH[2]}"
fi

# Quote the regex pattern in variable
pattern="^[a-z]{3}$"
[[ "$var" =~ $pattern ]]
```

### Example
```bash
# Broken
[[ "$var" =~ "^[0-9]+$" ]]    # quoted pattern treated as literal

# Fixed
[[ "$var" =~ ^[0-9]+$ ]]
```
