---
title: "[Solution] Bash Source: File Not Found Error Fix"
description: "Fix bash source file not found errors when sourcing scripts that don't exist."
languages: ["bash"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["source", "dot", "include", "file-not-found", "bash"]
weight: 5
---

# Bash Source: File Not Found Error Fix

A bash source error occurs when the `source` or `.` command tries to execute a file that doesn't exist or isn't readable.

## What This Error Means

The `source` command (or `.` shorthand) reads and executes commands from a file in the current shell. If the file doesn't exist, bash reports "file not found." Unlike executing a script, sourcing runs in the current process context.

## Common Causes

- File path is wrong or relative path incorrect
- File doesn't exist at expected location
- File permissions prevent reading
- Working directory changed before sourcing

## How to Fix

### 1. Check file exists before sourcing

```bash
# WRONG: Source without checking
source ./config.sh

# CORRECT: Check first
if [[ -f "./config.sh" ]]; then
    source ./config.sh
else
    echo "config.sh not found"
    exit 1
fi
```

### 2. Use absolute paths

```bash
# WRONG: Relative path may fail
source ../config.sh

# CORRECT: Use absolute path
source /opt/myapp/config.sh
# Or use script directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "$SCRIPT_DIR/config.sh"
```

### 3. Make file executable or readable

```bash
# CORRECT: Ensure readability
chmod +r config.sh
source config.sh
```

### 4. Handle optional config files

```bash
# CORRECT: Optional sourcing with defaults
for conf in /etc/app/conf.d/*.sh; do
    [[ -f "$conf" ]] && source "$conf"
done
```

## Related Errors

- [No Such File](no-such-file) — missing files
- [Permission Denied](permission-denied) — access errors
- [Command Not Found](command-not-found) — missing commands
