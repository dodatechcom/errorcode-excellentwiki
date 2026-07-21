---
title: "[Solution] Bash Lock File Error -- Preventing Concurrent Execution"
description: "Fix bash lock file errors when using lock files to prevent concurrent script execution."
languages: ["bash"]
error-types: ["runtime-error"]
severities: ["error"]
---

# Bash Lock File Error

This error occurs when lock files are not properly created or released, preventing concurrent execution.

## Common Causes

- Lock file not removed on script exit
- Using regular file instead of flock for atomic locking
- Lock file left behind after crash
- Not using trap to clean up lock file

## How to Fix

### Use flock for atomic locking

```bash
# WRONG: regular file lock
LOCKFILE="/tmp/myapp.lock"
echo $$ > "$LOCKFILE"

# CORRECT: use flock
exec 9>"${LOCKFILE}"
flock -n 9 || { echo "Already running"; exit 1; }
```

### Clean up with trap

```bash
LOCKFILE="/tmp/myapp.lock"
trap 'rm -f "$LOCKFILE"' EXIT

if [ -f "$LOCKFILE" ]; then
    echo "Already running"
    exit 1
fi
echo $$ > "$LOCKFILE"
```

## Examples

```bash
#!/bin/bash
LOCKFILE="/var/lock/myapp.lock"

exec 200>"$LOCKFILE"
flock -n 200 || { echo "Script already running"; exit 1; }

# Script logic here
echo "Running exclusively"
```
