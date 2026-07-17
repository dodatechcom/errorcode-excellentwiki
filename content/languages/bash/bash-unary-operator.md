---
title: "[Solution] Bash Unary Operator Expected"
description: "Fix 'bash: unary operator expected' when a test expression has a missing or empty operand before the operator."
languages: ["bash"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["unary-operator", "test", "conditional", "empty", "variable"]
weight: 5
---

# Bash Unary Operator Expected Fix

The `unary operator expected` error occurs when a test expression has an empty or missing left-hand operand, making the operator appear unary when it should be binary.

## What This Error Means

Unary operators like `-z`, `-n`, `-f`, `-d` take one argument. Binary operators like `=`, `-eq`, `-gt` take two. When a variable is empty, `[` sees the operator as the first argument and expects it to be unary.

## Common Causes

- Empty variable before comparison operator
- Missing left-hand side of comparison
- Variable not set due to command failure
- Glob expansion producing unexpected results

## How to Fix

### 1. Quote all variables

```bash
# WRONG: $file is empty
if [ $file = "test.txt" ]; then

# RIGHT: quoted
if [ "$file" = "test.txt" ]; then
```

### 2. Check variable is set first

```bash
# Use -n to check if non-empty
if [ -n "$file" ] && [ "$file" = "test.txt" ]; then
    echo "match"
fi
```

### 3. Use [[ ]] which handles empty vars

```bash
# [[ ]] doesn't word-split or glob-expand variables
if [[ $file = "test.txt" ]]; then
    echo "match"
fi
```

### 4. Provide defaults for potentially empty variables

```bash
file=${file:-""}
if [ "$file" = "test.txt" ]; then
    echo "match"
fi
```

## Related Errors

- [Binary Operator Expected](bash-binary-comparison) — binary operator issues
- [Conditional Expression Error](conditional-expr) — conditional errors
