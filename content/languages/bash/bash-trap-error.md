---
title: "[Solution] Bash Trap Error -- Incorrect Signal Handling"
description: "Fix bash trap errors when signal traps are not set up correctly or cause unexpected script behavior."
languages: ["bash"]
error-types: ["runtime-error"]
severities: ["error"]
---

# Bash Trap Error

This error occurs when bash trap statements are not set up correctly, leading to unexpected behavior on signals.

## Common Causes

- Trap function not handling the signal argument correctly
- Missing trap for EXIT signal in cleanup-heavy scripts
- Trap overriding previous traps without chaining
- Using trap in subshells where it has no effect

## How to Fix

### Set up proper cleanup traps

```bash
# WRONG: no cleanup on exit
temp_file=$(mktemp)
do_work "$temp_file"

# CORRECT: trap EXIT for cleanup
temp_file=$(mktemp)
trap 'rm -f "$temp_file"' EXIT
do_work "$temp_file"
```

### Chain traps correctly

```bash
original_trap=$(trap -p INT)
trap 'cleanup; eval "$original_trap"' INT
```

## Examples

```bash
#!/bin/bash
cleanup() {
    echo "Cleaning up..."
    rm -f "$TEMP_DIR"/*
    rmdir "$TEMP_DIR" 2>/dev/null
}

trap cleanup EXIT INT TERM

TEMP_DIR=$(mktemp -d)
echo "Working in $TEMP_DIR"
```
