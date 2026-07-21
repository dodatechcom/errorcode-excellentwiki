---
title: "[Solution] Bash Shift Error -- Incorrect Argument Processing"
description: "Fix bash shift errors when processing script arguments with shift command."
languages: ["bash"]
error-types: ["runtime-error"]
severities: ["error"]
---

# Bash Shift Error

This error occurs when `shift` is used incorrectly, such as shifting past the number of arguments.

## Common Causes

- Shifting when no arguments remain
- Not checking `$#` before shifting
- Using `shift N` where N > remaining args
- Infinite loop processing arguments without shift

## How to Fix

### Check argument count before shift

```bash
# WRONG: may shift when no args left
while [ $# -gt 0 ]; do
    case "$1" in
        -f) FILE="$2"; shift 2;;  # may fail if only -f left
    esac
done

# CORRECT: check before shifting
while [ $# -gt 0 ]; do
    case "$1" in
        -f)
            if [ $# -lt 2 ]; then
                echo "Missing argument for -f"
                exit 1
            fi
            FILE="$2"
            shift 2
            ;;
    esac
done
```

## Examples

```bash
#!/bin/bash
while [ $# -gt 0 ]; do
    case "$1" in
        -h|--help) echo "Usage: $0 [-f file] [-v]"; exit 0 ;;
        -f) FILE="$2"; shift 2 ;;
        -v) VERBOSE=1; shift ;;
        *) echo "Unknown: $1"; shift ;;
    esac
done
```
