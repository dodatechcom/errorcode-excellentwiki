---
title: "[Solution] Bash Derefence Error -- Variable Indirection Issues"
description: "Fix bash variable dereference errors when using indirect variable references incorrectly."
languages: ["bash"]
error-types: ["runtime-error"]
severities: ["error"]
---

# Bash Variable Derefence Error

This error occurs when variable indirection (`${!var}`) is used incorrectly or on unset variables.

## Common Causes

- Using `eval` instead of `${!var}` for indirect access
- Indirect variable name not matching any existing variable
- Syntax error in variable indirection
- Using indirection on arrays incorrectly

## How to Fix

### Use correct indirection syntax

```bash
# WRONG: eval with untrusted input
eval "value=\$$varname"

# CORRECT: use ${!varname}
varname="config_host"
config_host="localhost"
echo "${!varname}"  # localhost
```

### Check variable exists first

```bash
if declare -p "$varname" &>/dev/null; then
    echo "${!varname}"
else
    echo "Variable not found"
fi
```

## Examples

```bash
#!/bin/bash
# Dynamic variable access
for env in DB_HOST DB_PORT DB_NAME; do
    value="${!env:-not set}"
    echo "$env = $value"
done
```
