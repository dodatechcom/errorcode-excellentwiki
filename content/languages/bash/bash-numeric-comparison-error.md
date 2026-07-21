---
title: "[Solution] Bash Numeric Comparison Error -- String vs Integer Test"
description: "Fix bash numeric comparison errors when using string operators for integer comparisons."
languages: ["bash"]
error-types: ["runtime-error"]
severities: ["error"]
---

# Bash Numeric Comparison Error

This error occurs when bash tests use incorrect operators for comparing numbers versus strings.

## Common Causes

- Using `=` instead of `-eq` for numeric equality
- Using `-eq` with non-numeric values
- Missing quotes around variables in test expressions
- Using `==` inside `[ ]` instead of `[[ ]]`

## How to Fix

### Use correct comparison operators

```bash
# WRONG: string comparison for numbers
[ "$a" = "$b" ]

# CORRECT: numeric comparison
[ "$a" -eq "$b" ]

# In [[ ]], both work but -eq is clearer
[[ "$a" -eq "$b" ]]
```

### Check for numeric values

```bash
# Ensure variable is numeric before comparison
if [[ "$value" =~ ^[0-9]+$ ]]; then
    if [ "$value" -gt 10 ]; then
        echo "Greater than 10"
    fi
fi
```

## Examples

```bash
#!/bin/bash
age=25

# Numeric comparisons
[ "$age" -ge 18 ] && echo "Adult"
[ "$age" -lt 65 ] && echo "Working age"
[ "$age" -eq 25 ] && echo "Exactly 25"
```
