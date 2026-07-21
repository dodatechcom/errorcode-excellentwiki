---
title: "[Solution] Bash Unbound Variable Error -- Unset Variable Reference"
description: "Fix bash unbound variable errors when referencing variables that have not been set."
languages: ["bash"]
error-types: ["runtime-error"]
severities: ["error"]
---

# Bash Unbound Variable Error

This error occurs when `set -u` is enabled and a variable is referenced before being assigned a value.

## Common Causes

- `set -u` (or `set -o nounset`) enabled without defaulting unset variables
- Typo in variable name
- Variable set in a subshell but referenced in parent
- Script argument not assigned before use

## How to Fix

### Provide defaults for unset variables

```bash
# WRONG: variable may not be set
set -u
echo "$UNDEFINED_VAR"

# CORRECT: provide default
echo "${UNDEFINED_VAR:-default_value}"
```

### Check if variable is set

```bash
if [ -z "${MY_VAR+x}" ]; then
    MY_VAR="default"
fi
```

## Examples

```bash
#!/bin/bash
set -euo pipefail

# Safe defaults for optional variables
DB_HOST="${DB_HOST:-localhost}"
DB_PORT="${DB_PORT:-5432}"
DB_NAME="${DB_NAME:-myapp}"

echo "Connecting to $DB_HOST:$DB_PORT/$DB_NAME"
```
