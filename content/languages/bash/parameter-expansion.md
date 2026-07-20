---
title: "[Solution] Bash Parameter Expansion Error"
description: "Fix 'bash: parameter expansion error' when using incorrect syntax for variable expansion operators."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "bash"
tags: ["bash", "shell", "variables", "parameter-expansion", "operators", "syntax"]
severity: "error"
---

# Parameter Expansion Error

## Error Message

```
bash: parameter expansion error
```

## Common Causes

- Using an invalid operator in parameter expansion (e.g., `${var:?}` with malformed syntax)
- Missing the colon in parameter expansion operators like `${var:-default}`
- Using parameter expansion features not available in the current shell version
- Mismatched braces in complex parameter expansion expressions

## Solutions

### Solution 1: Use the Correct Parameter Expansion Operators

Bash parameter expansion uses specific operators. Make sure you're using the correct syntax for each operation.

```bash
#!/bin/bash
name="Hello"

# Default value
echo "${name:-default}"       # Output: Hello (or "default" if empty)

# Assign default if unset/empty
echo "${name:=assigned}"      # Output: Hello

# Error if unset/empty
# echo "${name:?not set}"    # Would error if name is empty

# Remove shortest/longest pattern from end
path="/usr/local/bin/script.sh"
echo "${path##*/}"            # Output: script.sh
echo "${path%/*}"             # Output: /usr/local/bin

# Length
echo "${#name}"               # Output: 5 
```

### Solution 2: Match Braces and Colons in Expansion

Every `${` must have a matching `}`. In operators like `${var:-default}`, the colon is required — `${var-default}` behaves differently (only checks unset, not empty).

```bash
#!/bin/bash
val=""

# Without colon — only checks if variable is UNSET
echo "${val-default}"    # Output: (empty, because val is set, just empty)

# With colon — checks if variable is UNSET or EMPTY
echo "${val:-default}"   # Output: default

# Make sure braces are balanced
name="test"
echo "${name}"           # Right
# echo "${name"          # Wrong — missing }
# echo "${name}}"        # Wrong — extra }

# Use bash -n to verify
bash -n script.sh 
```

## Prevention Tips

- Remember the colon: `${var:-default}` checks unset AND empty
- Count your braces carefully in nested expansions
- Use `bash -n script.sh` to catch parameter expansion syntax errors

## Related Errors

- [Default Value Error]({< relref "/languages/bash/default-value-error" >})
- [Variable Substitution Error]({< relref "/languages/bash/variable-substitution" >})
