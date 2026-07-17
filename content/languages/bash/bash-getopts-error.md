---
title: "[Solution] Bash Getopts: Invalid Option Error Fix"
description: "Fix bash getopts errors when an invalid option is passed to a script."
languages: ["bash"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["getopts", "options", "flags", "argument-parsing", "bash"]
weight: 5
---

# Bash Getopts: Invalid Option Error Fix

A bash getopts error occurs when a script receives an option that isn't defined in the optstring.

## What This Error Means

`getopts` parses command-line options defined in an optstring (e.g., `"hf:v"`). If the script receives an option not in the optstring, getopts sets `opt` to `?` and optionally triggers an error message.

## Common Causes

- User passes undefined option (e.g., `-x` when only `-h`, `-f`, `-v` are defined)
- Missing colon for required arguments
- Optstring doesn't include all valid options
- Not handling the `?` case for unknown options

## How to Fix

### 1. Handle unknown options

```bash
# WRONG: Not handling unknown options
while getopts "hf:v" opt; do
    case "$opt" in
        h) show_help ;;
        f) FILE="$OPTARG" ;;
        v) VERBOSE=1 ;;
    esac
done

# CORRECT: Handle ? for unknown options
while getopts "hf:v" opt; do
    case "$opt" in
        h) show_help ;;
        f) FILE="$OPTARG" ;;
        v) VERBOSE=1 ;;
        ?) echo "Invalid option: -$OPTARG"; exit 1 ;;
    esac
done
```

### 2. Define complete optstring

```bash
# CORRECT: Include all valid options
getopts "hf:vo:q" opt
# h = help flag
# f = file (requires arg)
# v = verbose flag
# o = output (requires arg)
# q = quiet flag
```

### 3. Use - for silent error handling

```bash
# CORRECT: Suppress getopts error messages
while getopts "hf:v" opt; do
    case "$opt" in
        h) show_help ;;
        f) FILE="$OPTARG" ;;
        v) VERBOSE=1 ;;
        :) echo "Option -$OPTARG requires an argument"; exit 1 ;;
        ?) echo "Unknown option: -$OPTARG"; exit 1 ;;
    esac
done
```

### 4. Support long options with manual parsing

```bash
# CORRECT: For long options, parse before getopts
while [[ $# -gt 0 ]]; do
    case "$1" in
        --help) show_help; shift ;;
        --file) FILE="$2"; shift 2 ;;
        -*) echo "Unknown option: $1"; exit 1 ;;
        *) break ;;
    esac
done
# Then use getopts for short options
```

## Related Errors

- [Too Many Arguments](too-many-arguments) — argument limits
- [Bash Shift Error](bash-shift-error) — shift out of range
- [Command Not Found](command-not-found) — missing commands
