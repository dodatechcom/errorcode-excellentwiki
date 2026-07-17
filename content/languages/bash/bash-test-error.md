---
title: "[Solution] Bash Test Command Error"
description: "Fix 'bash: test command error' when using [ ] or test builtin incorrectly in conditional expressions."
languages: ["bash"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# Bash Test Command Error Fix

Test command errors occur when `[` or `test` is used with incorrect syntax, wrong operators, or mismatched brackets.

## What This Error Means

The `test` builtin and `[` command evaluate conditional expressions. They require specific syntax: exactly one `]` to close the expression, correct operators, and proper argument count.

## Common Causes

- Missing closing `]` bracket
- Space between `[` and expression or `]`
- Wrong operator for the test type
- Using `==` in `[` instead of `=` (bash-specific)

## How to Fix

### 1. Ensure matching brackets with spaces

```bash
# WRONG: missing spaces
if [$var = "hello"]; then

# RIGHT: spaces required around [ and ]
if [ "$var" = "hello" ]; then
```

### 2. Use = not == in [ ]

```bash
# WRONG: == doesn't work in [ ]
if [ $var == "hello" ]; then

# RIGHT: use =
if [ "$var" = "hello" ]; then

# Or use [[ ]] which supports ==
if [[ $var == "hello" ]]; then
```

### 3. Use [[ ]] for modern bash

```bash
# [[ ]] is safer and more feature-rich
if [[ -f "$file" && -r "$file" ]]; then
    echo "File exists and is readable"
fi
```

### 4. Match operator to comparison type

```bash
# Numeric comparisons use -eq, -ne, -lt, etc.
if [ "$a" -eq "$b" ]; then echo "Equal"; fi

# String comparisons use =, !=, <, >
if [ "$a" = "$b" ]; then echo "Equal"; fi
```

## Related Errors

- [Binary Operator Expected](binary-comparison) — operator argument issues
- [Conditional Expression Error](conditional-expr) — conditional errors
