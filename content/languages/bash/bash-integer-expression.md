---
title: "[Solution] Bash Integer Expression Expected"
description: "Fix 'bash: integer expression expected' when a string is used where a number is required in arithmetic or test expressions."
languages: ["bash"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["integer", "expression", "number", "comparison", "type"]
weight: 5
---

# Bash Integer Expression Expected Fix

The `integer expression expected` error occurs when Bash tries to evaluate a non-numeric string as an integer in arithmetic or comparison contexts.

## What This Error Means

Bash requires integer values for arithmetic operations and numeric comparisons (`-eq`, `-ne`, `-lt`, etc.). When a variable contains a string, these operations fail.

## Common Causes

- Variable contains non-numeric characters
- Command output used directly without validation
- Empty variable used in arithmetic
- File path or string accidentally used as number

## How to Fix

### 1. Validate before using as integer

```bash
value="abc"
if [[ "$value" =~ ^[0-9]+$ ]]; then
    echo "Valid number: $((value + 1))"
else
    echo "Not a number"
fi
```

### 2. Provide default for empty variables

```bash
# WRONG: empty variable
count=""
echo $((count + 1))

# RIGHT: default to 0
count=${count:-0}
echo $((count + 1))
```

### 3. Use correct comparison operators

```bash
# For integers, use -eq -ne -lt -le -gt -ge
if [ "$a" -eq "$b" ]; then echo "Equal"; fi

# For strings, use = != < >
if [ "$a" = "$b" ]; then echo "Equal"; fi
```

### 4. Extract numbers from strings

```bash
str="File count: 42"
num=$(echo "$str" | grep -o '[0-9]*')
echo $((num + 1))
```

## Related Errors

- [Binary Operator Expected](binary-comparison) — test expression issues
- [Arithmetic Error](bash-arithmetic-error) — arithmetic syntax issues
