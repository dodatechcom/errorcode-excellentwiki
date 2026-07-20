---
title: "[Solution] Local Variable Scope Error"
description: "Fix 'local: can only be used in a function' error."
tools: ["bash"]
error-types: ["tool-error"]
severities: ["error"]
---

# [Solution] Local Variable Scope Error

The `local` keyword is used outside of a function definition.

### Common Causes
- `local` used in main script body.
- `local` in a sourced file that is not inside a function.
- Missing function wrapper.

### How to Fix
```bash
# local only works inside functions
my_func() {
    local var="value"    # scoped to function
    echo "$var"
}

# At script level, don't use local
global_var="value"    # global scope

# Use subshell for local scope at script level
(
    local_var="scoped_to_subshell"
    echo "$local_var"
)
echo "$local_var"    # empty
```

### Example
```bash
# Broken
local myvar="test"    # outside function

# Fixed
my_func() {
    local myvar="test"
    echo "$myvar"
}
my_func
```
