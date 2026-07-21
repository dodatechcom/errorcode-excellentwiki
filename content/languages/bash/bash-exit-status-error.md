---
title: "[Solution] Bash Exit Status Error -- Incorrect Error Handling"
description: "Fix bash exit status errors when $? is not checked after critical commands."
languages: ["bash"]
error-types: ["runtime-error"]
severities: ["warning"]
---

# Bash Exit Status Error

This error occurs when scripts do not check the exit status of commands, allowing failures to go unnoticed.

## Common Causes

- Not checking `$?` after important commands
- Using `set -e` but not handling expected failures
- Pipe commands where middle failure is ignored
- Missing `||` or `&&` for error handling

## How to Fix

### Check exit status explicitly

```bash
# WRONG: no error checking
rm important_file.txt
cp backup.txt important_file.txt

# CORRECT: check after each command
rm important_file.txt || { echo "Failed to remove"; exit 1; }
cp backup.txt important_file.txt || { echo "Failed to copy"; exit 1; }
```

### Use set -e with error traps

```bash
set -e
trap 'echo "Error on line $LINENO"' ERR

# Commands will fail the script on error
```

## Examples

```bash
#!/bin/bash
set -euo pipefail

backup_database() {
    pg_dump "$DB_NAME" > "backup_$(date +%Y%m%d).sql"
}

backup_database || {
    echo "Backup failed!"
    exit 1
}
```
