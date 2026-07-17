---
title: "[Solution] Bash Unbound Variable Error"
description: "Fix 'bash: unbound variable' when referencing variables that haven't been set, often with set -u enabled."
languages: ["bash"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["unbound-variable", "set-u", "unset", "variable"]
weight: 5
---

# Bash Unbound Variable Error Fix

The `unbound variable` error occurs when a script uses `$variable` but the variable has not been set, and `set -u` (or `set -o nounset`) is enabled.

## What This Error Means

With `set -u`, Bash treats unset variables as errors rather than silently expanding to empty strings. This catches typos and missing defaults but can also cause legitimate failures.

## Common Causes

- Variable name typo
- Variable not set before use (e.g., optional config values)
- Command-line arguments not checked before use
- Environment variable not exported by parent process

## How to Fix

### 1. Provide default values

```bash
# Set default if variable is unset
echo ${VARIABLE:-"default_value"}

# Set default and assign
VARIABLE=${VARIABLE:-"default_value"}
```

### 2. Check for variable existence

```bash
# Test if variable is set
if [ -z "${MY_VAR+x}" ]; then
    echo "MY_VAR is not set"
fi
```

### 3. Use set +u for optional variables

```bash
set +u  # Temporarily disable unbound variable check
source optional_config.sh
set -u  # Re-enable
```

### 4. Handle missing command-line arguments

```bash
#!/bin/bash
set -u

# WRONG: $1 might not exist
filename=$1

# RIGHT: check first
if [ $# -eq 0 ]; then
    echo "Usage: $0 <filename>" >&2
    exit 1
fi
filename=$1
```

## Related Errors

- [Syntax Error](syntax-error) — general parse errors
- [Conditional Expression Error](conditional-expr) — test expression issues
