---
title: "[Solution] Bash Function Redeclaration Error"
description: "Fix Bash function redeclaration errors when functions are defined multiple times causing conflicts."
tools: ["bash"]
error-types: ["tool-error"]
severities: ["warning"]
---

# Bash Function Redeclaration Error

Bash warns or errors when a function is redefined in the same scope.

```
bash: my_func: cannot overwrite existing function
```

## Common Causes

- BASH_ENV or ENV sourcing same file twice
- Source command in loop without guard
- Function defined in both global and sourced file
- set -o funcrestrict enabled
- Recursive source including

## How to Fix

### Use Function Guard Pattern

```bash
if ! declare -f my_func > /dev/null 2>&1; then
    my_func() {
        echo "Function body"
    }
fi
```

### Prevent Multiple Sourcing

```bash
# Guard entire file with sourced flag
if [[ "${_MY_FUNCTIONS_LOADED:-}" == "1" ]]; then
    return 0
fi
_MY_FUNCTIONS_LOADED=1

my_func() {
    echo "Hello"
}
```

### Unset Before Redefining

```bash
# Remove existing function before redefining
unset -f my_func

my_func() {
    echo "New implementation"
}
```

### Check BASH_ENV Usage

```bash
# Verify BASH_ENV does not load conflicting definitions
echo "$BASH_ENV"
# Set BASH_ENV carefully or avoid it
unset BASH_ENV
```

## Examples

```bash
# Safe sourced library pattern
#!/bin/bash
# lib.sh
[[ "${_LIB_LOADED:-}" ]] && return 0
_LIB_LOADED=1

helper() {
    echo "Helper function"
}
```

```bash
# Source without redefinition issues
source lib.sh 2>/dev/null || true
```
