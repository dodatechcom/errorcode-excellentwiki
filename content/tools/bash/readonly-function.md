---
title: "[Solution] Cannot Reassign Readonly Function"
description: "Fix 'readonly function' error in Bash."
tools: ["bash"]
error-types: ["tool-error"]
severities: ["error"]
---

# [Solution] Cannot Reassign Readonly Function

A function marked as `readonly` cannot be redefined or unset.

### Common Causes
- Function declared with `readonly -f`.
- Attempting to redefine a readonly function.
- Trying to `unset` a readonly function.

### How to Fix
```bash
# Check if function is readonly
readonly -f my_func

# Define readonly function
my_func() { echo "original"; }
readonly -f my_func

# Cannot redefine:
# my_func() { echo "new"; }    # error

# Use a wrapper or variable instead
my_func_wrapper() {
    if [[ -n "${OVERRIDE:-}" ]]; then
        echo "overridden"
    else
        my_func
    fi
}
```

### Example
```bash
# Broken
readonly -f my_func
my_func() { echo "new"; }    # error

# Fixed: use a different name or variable-based dispatch
func_name="original_func"
dispatch() { "$func_name" "$@"; }
```
