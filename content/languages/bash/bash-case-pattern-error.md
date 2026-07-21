---
title: "[Solution] Bash Case Pattern Error -- Incorrect Case Statement Syntax"
description: "Fix bash case statement errors when patterns are incorrectly matched or terminated."
languages: ["bash"]
error-types: ["syntax-error"]
severities: ["error"]
---

# Bash Case Pattern Error

This error occurs when bash `case` statements have incorrect pattern syntax or missing terminators.

## Common Causes

- Missing `;;` terminator after case arm
- Patterns using unquoted special characters
- Wrong order of patterns (general before specific)
- Missing closing `esac`

## How to Fix

### Use correct case syntax

```bash
# WRONG: missing ;;
case "$color" in
    red) echo "Red"
    blue) echo "Blue"  # falls through to blue

# CORRECT: proper terminators
case "$color" in
    red) echo "Red";;
    blue) echo "Blue";;
esac
```

### Quote special characters in patterns

```bash
# WRONG: glob expansion in pattern
case "$file" in
    *.txt) echo "Text";;  # unquoted *

# CORRECT: glob patterns work but be aware
case "$file" in
    *.txt) echo "Text file";;
    *.csv) echo "CSV file";;
    *) echo "Unknown";;
esac
```

## Examples

```bash
#!/bin/bash
case "$1" in
    start) start_service ;;
    stop) stop_service ;;
    restart) stop_service; start_service ;;
    status) check_status ;;
    *) echo "Usage: $0 {start|stop|restart|status}" ;;
esac
```
