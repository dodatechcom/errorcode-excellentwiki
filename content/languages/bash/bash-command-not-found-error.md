---
title: "[Solution] Bash Command Not Found Error -- Missing Executable"
description: "Fix bash command not found errors when the shell cannot locate the executable in PATH."
languages: ["bash"]
error-types: ["runtime-error"]
severities: ["error"]
---

# Bash Command Not Found Error

This error occurs when bash tries to execute a command that does not exist in any directory listed in PATH.

## Common Causes

- Typo in command name
- Command not installed on the system
- PATH variable does not include the directory
- Shell function or alias not defined

## How to Fix

### Check command existence

```bash
# WRONG: blindly running command
mycommand  # command not found

# CORRECT: check first
if command -v mycommand &> /dev/null; then
    mycommand
else
    echo "mycommand not found, installing..."
    sudo apt-get install -y mycommand
fi
```

### Update PATH

```bash
# Add custom directory to PATH
export PATH="/usr/local/bin:$PATH"
```

## Examples

```bash
#!/bin/bash
set -euo pipefail

# Verify required commands
for cmd in curl jq grep; do
    if ! command -v "$cmd" &> /dev/null; then
        echo "Error: $cmd is required but not installed."
        exit 1
    fi
done
```
