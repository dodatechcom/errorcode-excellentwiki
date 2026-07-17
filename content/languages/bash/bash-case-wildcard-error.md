---
title: "[Solution] Bash Case: Syntax Error Fix"
description: "Fix bash case statement syntax errors. Learn proper case/esac syntax."
languages: ["bash"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Bash Case: Syntax Error Fix

A bash case syntax error occurs when the `case ... esac` statement has malformed patterns, missing `;;`, or incorrect syntax.

## What This Error Means

The `case` statement in bash matches a variable against patterns. Syntax errors include missing `;;` terminators, unmatched parentheses in patterns, or missing `esac`.

## Common Causes

- Missing `;;` between patterns
- Missing closing `esac`
- Wrong pattern syntax (using regex instead of glob)
- Missing `(` or `)` in pattern

## How to Fix

### 1. Use correct case syntax

```bash
# WRONG: Missing ;;
case "$action" in
    start) echo "Starting"
    stop) echo "Stopping"

# CORRECT: End each pattern with ;;
case "$action" in
    start) echo "Starting" ;;
    stop) echo "Stopping" ;;
    *) echo "Unknown" ;;
esac
```

### 2. Use glob patterns, not regex

```bash
# WRONG: Regex syntax in case
case "$file" in
    *.py$) echo "Python" ;;  # Wrong: $ not needed
esac

# CORRECT: Use glob patterns
case "$file" in
    *.py) echo "Python" ;;
    *.js) echo "JavaScript" ;;
    *) echo "Other" ;;
esac
```

### 3. Group patterns correctly

```bash
# CORRECT: Multiple patterns with |
case "$ext" in
    jpg|jpeg|png) echo "Image" ;;
    mp3|wav|ogg) echo "Audio" ;;
    mp4|avi|mkv) echo "Video" ;;
    *) echo "Unknown" ;;
esac
```

### 4. Handle empty input

```bash
# CORRECT: Default case handles everything
case "${input:-}" in
    "") echo "No input" ;;
    *) echo "Input: $input" ;;
esac
```

## Related Errors

- [Bash Syntax Error](bash-syntax-error) — general syntax issues
- [Bash For Error](bash-for-error) — loop syntax errors
- [Bash Conditional Error](bash-conditional-error) — condition evaluation
