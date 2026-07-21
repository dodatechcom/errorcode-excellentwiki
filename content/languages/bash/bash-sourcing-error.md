---
title: "[Solution] Bash Sourcing Error -- Incorrect Source/ dot Command Usage"
description: "Fix bash sourcing errors when using source or . command to load external scripts."
languages: ["bash"]
error-types: ["runtime-error"]
severities: ["error"]
---

# Bash Sourcing Error

This error occurs when sourced scripts cause errors, change the current shell state unexpectedly, or are not found.

## Common Causes

- Sourced script using `exit` which exits the parent shell
- Variable or function name collision with parent script
- Sourced script not found due to PATH issues
- Circular sourcing between scripts

## How to Fix

### Check file existence before sourcing

```bash
# WRONG: assumes file exists
source "$CONFIG_FILE"

# CORRECT: check first
if [ -f "$CONFIG_FILE" ]; then
    source "$CONFIG_FILE"
else
    echo "Config not found: $CONFIG_FILE"
    exit 1
fi
```

### Avoid exit in sourced scripts

```bash
# In sourced script, use return instead of exit
if [ ! -f "$REQUIRED_FILE" ]; then
    echo "Missing required file"
    return 1  # not exit
fi
```

## Examples

```bash
#!/bin/bash
# Safe sourcing with namespace
config_file="/etc/myapp/config.sh"

if [ -f "$config_file" ]; then
    # shellcheck source=/dev/null
    source "$config_file"
fi
```
