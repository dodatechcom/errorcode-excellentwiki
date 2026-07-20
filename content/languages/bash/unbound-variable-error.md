---
title: "[Solution] Bash Unbound Variable Error"
description: "Fix 'bash: unbound variable' when referencing undefined variables with strict mode enabled."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "bash"
tags: ["bash", "shell", "variables", "strict-mode", "set-u", "unbound"]
severity: "error"
---

# Unbound Variable

## Error Message

```
bash: MY_VAR: unbound variable
```

## Common Causes

- Using `set -u` (or `set -o nounset`) which treats unset variables as errors
- Referencing a variable that was never assigned a value
- A typo in the variable name causing it to not match the assignment
- The variable was unset with `unset` and then referenced again

## Solutions

### Solution 1: Initialize Variables Before Use

Always assign a value to a variable before referencing it, especially when using `set -u`. Use default values for optional variables.

```bash
#!/bin/bash
set -u  # Treat unset variables as an error

# Wrong — MY_VAR is never set
echo "$MY_VAR"

# Right — initialize before use
MY_VAR="default value"
echo "$MY_VAR"

# Right — use a default value with parameter expansion
echo "${MY_VAR:-"fallback value"}" 
```

### Solution 2: Check if a Variable is Set Before Using It

Use parameter expansion or conditional checks to provide a default value when a variable might not be set.

```bash
#!/bin/bash
set -u

# Use ${VAR:-default} to provide a fallback
RESULT="${RESULT:-"default_result"}"
echo "$RESULT"

# Check if a variable is set with a conditional
if [ -n "${MY_VAR:-}" ]; then
    echo "MY_VAR is set to: $MY_VAR"
else
    echo "MY_VAR is not set"
fi

# For arrays, check length
if [ "${#ARRAY[@]}" -gt 0 ]; then
    echo "Array has elements"
fi 
```

## Prevention Tips

- Always use `${VAR:-default}` syntax when a variable might be unset under `set -u`
- Initialize all variables at the top of your script
- Use `bash -n script.sh` to check for obvious variable issues

## Related Errors

- [Variable Not Set]({< relref "/languages/bash/variable-not-set" >})
- [Invalid Variable Name]({< relref "/languages/bash/invalid-variable-name" >})
