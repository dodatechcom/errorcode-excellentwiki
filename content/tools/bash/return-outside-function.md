---
title: "[Solution] Return Outside Function Error"
description: "Fix 'return: can only `return' from a function' error."
tools: ["bash"]
error-types: ["tool-error"]
severities: ["error"]
---

# [Solution] Return Outside Function Error

The `return` statement is used outside of a function definition.

### Common Causes
- `return` used in main script body.
- `return` in a sourced file that runs code outside functions.
- Mixing `return` and `exit`.

### How to Fix
```bash
# Use return inside functions
my_func() {
    if [[ ! -f "$1" ]]; then
        echo "File not found" >&2
        return 1
    fi
    echo "File found"
    return 0
}

# Use exit in main script body
if [[ ! -f "$config" ]]; then
    echo "Missing config" >&2
    exit 1
fi

# Use source for sourced files
# In sourced file, use return
# In main script, use exit
```

### Example
```bash
# Broken
return 1    # at script top level

# Fixed
exit 1      # at script top level
```
