---
title: "[Solution] Bash Export Error -- Environment Variable Scope Issues"
description: "Fix bash export errors when environment variables are not properly exported to child processes."
languages: ["bash"]
error-types: ["runtime-error"]
severities: ["error"]
---

# Bash Export Error

This error occurs when environment variables are not exported, making them unavailable to child processes.

## Common Causes

- Setting variable without `export` -- only local to shell
- Forgetting that `export` does not work for array variables
- Export after process start has no effect
- Inconsistent export in sourced scripts

## How to Fix

### Export variables correctly

```bash
# WRONG: variable only exists in current shell
MY_VAR="hello"
./child_script.sh  # MY_VAR not available

# CORRECT: export makes it available
export MY_VAR="hello"
./child_script.sh  # MY_VAR available
```

### Export for arrays (bash 4+)

```bash
# Arrays need special handling
declare -A config
config[host]="localhost"
export config  # works in bash 4+
```

## Examples

```bash
#!/bin/bash
export DATABASE_URL="postgres://localhost/mydb"
export APP_ENV="production"

# Child processes see these
env | grep DATABASE
```
