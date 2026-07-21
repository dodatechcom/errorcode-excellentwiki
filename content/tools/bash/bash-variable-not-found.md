---
title: "[Solution] Bash Variable Not Found Error"
description: "Fix Bash variable not found errors when referencing undefined or unset variables in scripts."
tools: ["bash"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Variable name typo
- Variable defined in a different scope (subshell or function)
- Variable not exported to child processes
- nounset option enabled but variable is unset
- Variable defined after it is referenced

## How to Fix

- Verify the variable is defined before use
- Check for typos in variable names
- Export variables when needed for child processes
- Use default values with `${var:-default}` syntax

## Examples

```bash
#!/bin/bash
set -u  # nounset - treat unset variables as error

# This will fail if MY_VAR is not set
echo "$MY_VAR"

# Use a default value
echo "${MY_VAR:-default_value}"

# Export variable for subprocesses
export MY_VAR="hello"
bash -c 'echo "$MY_VAR"'
```
