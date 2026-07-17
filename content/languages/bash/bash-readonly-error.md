---
title: "[Solution] Bash Readonly: Cannot Modify Error Fix"
description: "Fix bash readonly variable errors when trying to modify or unset a readonly variable."
languages: ["bash"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["readonly", "constant", "immutable", "bash"]
weight: 5
---

# Bash Readonly: Cannot Modify Error Fix

A bash readonly error occurs when you try to modify, unset, or reassign a variable marked as `readonly`.

## What This Error Means

The `readonly` command makes a variable immutable — it cannot be changed, unset, or reassigned for the lifetime of the shell. Attempting to modify it produces an error.

## Common Causes

- Trying to reassign a readonly variable
- Attempting to `unset` a readonly variable
- Trying to use `declare -r` after initial assignment
- Function parameter reassignment in readonly context

## How to Fix

### 1. Don't modify readonly variables

```bash
# WRONG: Modifying readonly
readonly DEBUG=1
DEBUG=0  # Error: readonly variable

# CORRECT: Use a non-readonly variable if modification needed
DEBUG=1
# ... later
DEBUG=0
```

### 2. Use readonly intentionally

```bash
# CORRECT: Use readonly for constants
readonly CONFIG_DIR="/etc/myapp"
readonly MAX_RETRIES=3

# These cannot be accidentally changed
# CONFIG_DIR="/new/path"  # Would error
```

### 3. Check if variable is readonly

```bash
# CORRECT: Check before modifying
if [[ -R "varname" ]]; then
    echo "Variable is readonly"
else
    varname="new value"
fi
```

### 4. Use function-local variables

```bash
# CORRECT: Use local for function scope
my_func() {
    local result=""
    result="done"
    echo "$result"
}
```

## Related Errors

- [Unbound Variable](unbound-variable) — unset variable errors
- [Bash Syntax Error](bash-syntax-error) — general syntax issues
- [Permission Denied](permission-denied) — access errors
