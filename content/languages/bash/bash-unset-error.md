---
title: "[Solution] Bash Unset: Not a Name Reference Error Fix"
description: "Fix bash unset errors when trying to unset a variable that isn't a nameref."
languages: ["bash"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Bash Unset: Not a Name Reference Error Fix

A bash unset error occurs when you try to `unset -n` (nameref unset) on a variable that isn't a nameref, or when unsetting fails for other reasons.

## What This Error Means

The `unset` command removes variables or functions. Using `unset -n` tries to unset the variable referenced by a nameref. If the target isn't a nameref, bash reports "not a name reference."

## Common Causes

- Using `unset -n` on a non-nameref variable
- Trying to unset a readonly variable
- Trying to unset a special variable (like `$1`)
- Unsetting a variable that doesn't exist with strict mode

## How to Fix

### 1. Use correct unset syntax

```bash
# WRONG: Using -n on non-nameref
unset -n regular_var  # Error: not a name reference

# CORRECT: Use unset without -n
unset regular_var
```

### 2. Use nameref correctly

```bash
# CORRECT: Nameref usage
declare -n myref="original_var"
original_var="hello"
echo "${myref}"  # hello
unset -n myref   # Unrefs the nameref
```

### 3. Check variable exists before unsetting

```bash
# CORRECT: Safe unset
varname="some_value"
if [[ -v "varname" ]]; then
    unset varname
fi
```

### 4. Handle readonly variables

```bash
# CORRECT: Don't try to unset readonly
readonly CONST="value"
# unset CONST  # Error: readonly variable
# Instead, use a non-readonly variable if you need to unset
```

## Related Errors

- [Unbound Variable](unbound-variable) — unset variable access
- [Bash Readonly Error](bash-readonly-error) — readonly modification
- [Bash Syntax Error](bash-syntax-error) — general syntax issues
