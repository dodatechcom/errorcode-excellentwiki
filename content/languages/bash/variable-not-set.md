---
title: "[Solution] Bash Variable Not Set Error"
description: "Fix 'bash: VARIABLE: parameter null or not set' when using unset or null variables in parameter expansion."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "bash"
tags: ["bash", "shell", "variables", "parameter-expansion", "null", "not-set"]
severity: "error"
---

# Variable Not Set

## Error Message

```
bash: VARIABLE: parameter null or not set
```

## Common Causes

- Using `${VARIABLE:?}` syntax which errors when the variable is unset or null
- Referencing a variable with `set -u` that has no value
- A variable was set to empty string and then used in a context requiring a non-empty value
- Environment variable not passed from a parent process or configuration

## Solutions

### Solution 1: Use Default Value Syntax

Instead of letting unset variables cause errors, provide default values using `${VAR:-default}`. This returns the default when the variable is unset or null.

```bash
# This will error if CONFIG_FILE is not set
echo "${CONFIG_FILE:?Config file not specified}"

# Use :- for a default value instead
echo "${CONFIG_FILE:-/etc/myapp.conf}"

# Set a default at script startup
CONFIG_FILE="${CONFIG_FILE:-/etc/myapp.conf}"
echo "Using config: $CONFIG_FILE" 
```

### Solution 2: Check if Variables Exist Before Using Them

Use conditional checks to verify a variable is set and non-empty before using it in critical operations.

```bash
#!/bin/bash

# Check if variable is set and non-empty
if [ -z "${DATABASE_URL:-}" ]; then
    echo "Error: DATABASE_URL is not set"
    echo "Set it with: export DATABASE_URL=..."
    exit 1
fi

# Safe to use DATABASE_URL here
echo "Connecting to: $DATABASE_URL"

# Alternative: use ${VAR:?message} for mandatory variables
: "${API_KEY:?API_KEY environment variable is required}" 
```

## Prevention Tips

- Use `${VAR:-default}` for optional variables with sensible defaults
- Use `${VAR:?error message}` for mandatory variables
- Document required environment variables in your script's comments

## Related Errors

- [Unbound Variable]({< relref "/languages/bash/unbound-variable-error" >})
- [Default Value Error]({< relref "/languages/bash/default-value-error" >})
