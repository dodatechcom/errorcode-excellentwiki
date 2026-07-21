---
title: "[Solution] Bash Exit Code Handling Error -- Incorrect Error Propagation"
description: "Fix bash exit code handling errors when scripts do not properly propagate or check exit codes."
languages: ["bash"]
error-types: ["runtime-error"]
severities: ["error"]
---

# Bash Exit Code Handling Error

This error occurs when exit codes are not properly checked or propagated between commands.

## Common Causes

- Not checking `$?` after critical commands
- Using `&&` or `||` chains incorrectly
- Functions returning wrong exit codes
- `set -e` causing premature exits

## How to Fix

### Check exit codes explicitly

```bash
# WRONG: no exit code check
rm file.txt

# CORRECT: check exit code
rm file.txt
if [ $? -ne 0 ]; then
    echo "Failed to remove file"
    exit 1
fi
```

### Use proper function return codes

```bash
validate_input() {
    if [ -z "$1" ]; then
        return 1  # failure
    fi
    return 0  # success
}

if ! validate_input "$user_input"; then
    echo "Invalid input"
    exit 1
fi
```

## Examples

```bash
#!/bin/bash
backup_file() {
    cp "$1" "$1.bak" || return 1
    echo "Backed up: $1"
}

backup_file "/etc/config" || { echo "Backup failed"; exit 1; }
```
