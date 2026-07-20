---
title: "[Solution] Bash Default Value Error"
description: "Fix 'bash: default value error' when using incorrect default value assignment syntax for variables."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "bash"
tags: ["bash", "shell", "variables", "default-values", "parameter-expansion", "assignment"]
severity: "error"
---

# Default Value Error

## Error Message

```
bash: default value error
```

## Common Causes

- Confusing `${var:-default}` with `${var-default}` (they behave differently)
- Using `${var:=-default}` which tries to assign the literal string instead of the value
- Missing the colon operator in default value syntax
- Using default value syntax in a context where it's not supported (e.g., in `case` patterns)

## Solutions

### Solution 1: Understand Default Value Operator Variants

Bash has different default value operators. `${var:-default}` returns default if unset/empty. `${var-default}` returns default only if unset. `${var:=default}` assigns default to var.

```bash
#!/bin/bash

# ${var:-default} — return default if unset OR empty
unset A
B=""
echo "A=${A:-fallback}"   # Output: A=fallback
echo "B=${B:-fallback}"   # Output: B=fallback

# ${var-default} — return default only if UNSET
unset C
D=""
echo "C=${C-fallback}"    # Output: C=fallback
echo "D=${D-fallback}"    # Output: D= (empty, because D is set)

# ${var:=default} — ASSIGN default if unset OR empty
unset E
E="${E:=assigned}"
echo "E=$E"              # Output: E=assigned 
```

### Solution 2: Use Correct Syntax for Error Messages

Use `${var:?message}` to provide a meaningful error when a required variable is not set. This exits the current subshell or prints the error.

```bash
#!/bin/bash

# ${var:?message} — error with message if unset/empty
: "${DB_HOST:?DB_HOST must be set}"
: "${DB_PORT:?DB_PORT must be set}"

# Use in a function
validate_env() {
    : "${API_KEY:?API_KEY is required}"
    : "${API_SECRET:?API_SECRET is required}"
    echo "Environment validated"
}

# Safe pattern for optional with documented defaults
LOG_LEVEL="${LOG_LEVEL:-info}"
DB_TIMEOUT="${DB_TIMEOUT:-30}"
MAX_RETRIES="${MAX_RETRIES:-3}" 
```

## Prevention Tips

- Remember: `${var:-default}` uses a colon, `${var-default}` does not
- Use `${var:=default}` to both check and assign in one step
- Use `${var:?message}` for mandatory variables with clear error messages

## Related Errors

- [Variable Not Set]({< relref "/languages/bash/variable-not-set" >})
- [Parameter Expansion Error]({< relref "/languages/bash/parameter-expansion" >})
