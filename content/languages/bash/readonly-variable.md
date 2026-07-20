---
title: "[Solution] Bash Readonly Variable Error"
description: "Fix 'bash: VARIABLE: readonly variable' when attempting to modify a read-only variable."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "bash"
tags: ["bash", "shell", "variables", "readonly", "immutable", "assignment"]
severity: "error"
---

# Readonly Variable

## Error Message

```
bash: MY_VAR: readonly variable
```

## Common Causes

- Attempting to reassign a variable declared with `readonly` or `declare -r`
- Trying to modify a Bash built-in read-only variable (like `BASH_VERSION`)
- A variable was made readonly in an earlier part of the script
- Trying to `unset` a readonly variable

## Solutions

### Solution 1: Don't Reassign Readonly Variables

Once a variable is declared as `readonly`, it cannot be changed. Use a different variable name or restructure your code to avoid reassignment.

```bash
# Wrong — MY_VAR is readonly
readonly MY_VAR="constant"
MY_VAR="new value"  # Error: readonly variable

# Right — use a different variable for the new value
readonly MY_VAR="constant"
MY_SECOND_VAR="new value"
echo "$MY_SECOND_VAR"

# Right — compute the readonly value correctly the first time
readonly RESULT=$(compute_value)
echo "$RESULT" 
```

### Solution 2: Unset Readonly Variables When Necessary

In Bash 4.4+, you can use `readonly -n` for namerefs. For older versions, readonly variables can only be unset in a subshell or by exiting the script.

```bash
readonly MY_VAR="constant"

# Cannot unset in the same shell (will error)
# unset MY_VAR  # Error: cannot unset MY_VAR

# But you can work around it in a subshell
(
    unset MY_VAR  # Works in subshell
    MY_VAR="new value"
    echo "$MY_VAR"  # "new value"
)

# Or simply use a different variable name
MY_NEW_VAR="replaced value" 
```

## Prevention Tips

- Plan carefully before marking a variable as `readonly`
- Use `readonly` for values that truly should never change (constants)
- Consider using functions to encapsulate logic around constant values

## Related Errors

- [Invalid Variable Name]({< relref "/languages/bash/invalid-variable-name" >})
- [Unbound Variable]({< relref "/languages/bash/unbound-variable-error" >})
