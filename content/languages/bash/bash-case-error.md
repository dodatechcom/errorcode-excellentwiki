---
title: "[Solution] Bash Case Syntax Error"
description: "Fix 'case syntax error' in Bash when case/esac statements have incorrect syntax or missing terminators."
languages: ["bash"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["case", "esac", "pattern-match", "switch", "syntax"]
weight: 5
---

# Bash Case Syntax Error Fix

Case syntax errors occur when the `case ... esac` statement has incorrect pattern syntax, missing `;;` terminators, or mismatched parentheses.

## What This Error Means

The `case` statement pattern-matches a variable against multiple patterns. Each pattern must end with `;;`, and the entire block must close with `esac`. Errors indicate malformed syntax.

## Common Causes

- Missing `;;` after a pattern's body
- Missing `esac` to close the case block
- Unclosed quote in a pattern
- `|` used incorrectly in pattern alternatives
- Missing `)` after pattern

## How to Fix

### 1. Ensure each pattern ends with ;;

```bash
# WRONG: missing ;;
case "$1" in
    start) echo "Starting"
    stop) echo "Stopping"
esac

# RIGHT:
case "$1" in
    start) echo "Starting" ;;
    stop) echo "Stopping" ;;
esac
```

### 2. Check for matching esac

```bash
# WRONG: missing esac
case "$1" in
    a) echo "A" ;;
esac  # This must be present

# Check: every case must have a matching esac
```

### 3. Use proper pattern syntax

```bash
# WRONG: missing )
case "$1" in
    start echo "Starting"  # Missing )

# RIGHT:
case "$1" in
    start) echo "Starting" ;;
esac
```

### 4. Quote patterns with special characters

```bash
case "$1" in
    "file.txt") echo "Got filename" ;;  # Quote if needed
    *.log) echo "Got log file" ;;       # Glob is fine
esac
```

## Related Errors

- [Syntax Error](syntax-error) — general parse errors
- [Select Error](bash-select-error) — select statement issues
