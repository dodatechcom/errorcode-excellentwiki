---
title: "[Solution] Bash Readonly Variable Is Read-Only Error Fix"
description: "Fix 'readonly: variable is read-only' in Bash. Resolve read-only variable assignment and readonly declaration errors."
languages: ["bash"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Bash Readonly Variable Is Read-Only Error Fix

The `readonly: variable is read-only` error occurs when you attempt to modify a variable that has been declared as read-only using `readonly` or `declare -r`.

## What This Error Means

Readonly variables cannot be changed after declaration. This is a safety feature to protect constants and important configuration values. Attempting to reassign, unset, or modify a readonly variable fails with this error.

A typical error:

```
bash: MY_VAR: readonly variable
```

## Why It Happens

Common causes include:

- **Reassigning a readonly variable** — `MY_VAR=2` after `readonly MY_VAR=1`.
- **Using unset on a readonly variable** — `unset MY_VAR` fails.
- **Sourcing a file that redefines a readonly** — Two files set the same readonly variable.
- **Function modifying a readonly** — A function tries to change a global readonly.
- **Loop trying to update a constant** — Accumulator variable was made readonly.

## How to Fix It

### Fix 1: Check before declaring readonly

```bash
# RIGHT: Only declare once
if [ -z "${MY_VAR+x}" ]; then
    readonly MY_VAR="initial_value"
fi
```

### Fix 2: Use a regular variable when modification is needed

```bash
# WRONG: Making something readonly that needs changing
readonly counter=0
counter=$((counter + 1))  # Error!

# RIGHT: Use regular variable
counter=0
counter=$((counter + 1))
```

### Fix 3: Use functions with local variables

```bash
# RIGHT: Use local variables that can be modified
my_function() {
    local result="$1"
    result="${result}_modified"
    echo "$result"
}
```

### Fix 4: Override readonly in a subshell if needed

```bash
# Subshell can reassign (parent shell is unaffected)
(
    readonly VAR="original"
    VAR="modified"  # Works in subshell
    echo "$VAR"
)
```

### Fix 5: Check if variable is readonly before modifying

```bash
# RIGHT: Safe modification attempt
modify_var() {
    if readonly | grep -q "MY_VAR="; then
        echo "Cannot modify readonly variable MY_VAR" >&2
        return 1
    fi
    MY_VAR="new_value"
}
```

## Common Mistakes

- **Forgetting that readonly is permanent in the shell session** — You cannot undo it.
- **Sourcing files that conflict** — Check for duplicate readonly declarations across sourced files.
- **Using readonly for configuration that might change** — Use environment variables instead.

## Related Pages

- [Bash Unset Error](bash-unset-error) — Variable unset issues
- [Bash Shift Error](bash-shift-error) — Argument shift errors
- [Bash Unbound Variable](unbound-variable) — Unset variable errors
