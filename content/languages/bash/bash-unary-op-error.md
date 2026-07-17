---
title: "[Solution] Bash Unary Operator Expected Error Fix"
description: "Fix bash unary operator expected errors when test expressions are missing the operand before the operator."
languages: ["bash"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Bash Unary Operator Expected Error Fix

A bash unary operator expected error occurs when a unary operator (like `-z`, `-n`, `-f`, `-d`) is used without a proper operand, or the operand is empty.

## What This Error Means

Unary operators take a single argument. `-z` tests for empty string, `-n` tests for non-empty string, `-f` tests for regular file, etc. If the argument is missing (empty variable, unquoted), bash reports "unary operator expected."

## Common Causes

- Empty variable passed to unary operator
- Variable not quoted (word splitting removes it)
- Wrong operator for the data type
- Extra spaces in test expression

## How to Fix

### 1. Quote variables

```bash
# WRONG: Unquoted empty variable
value=""
[ -z $value ]  # Unary operator expected

# CORRECT: Quote the variable
[ -z "$value" ]
```

### 2. Use -z and -n correctly

```bash
# CORRECT: Test for empty and non-empty
name=""
[ -z "$name" ] && echo "Empty"      # true
[ -n "$name" ] && echo "Non-empty"   # false
```

### 3. Use for file tests

```bash
# CORRECT: File existence tests
file=""
[ -f "$file" ] && echo "File exists"
[ -d "$file" ] && echo "Directory exists"
[ -r "$file" ] && echo "Readable"
[ -w "$file" ] && echo "Writable"
```

### 4. Use [[ ]] for safer handling

```bash
# CORRECT: [[ ]] handles empty strings better
[[ -z "$value" ]] && echo "Empty"
[[ -n "$value" ]] && echo "Has value"
```

## Related Errors

- [Binary Operator Expected](bash-binary-op-error) — missing two operands
- [Integer Expression Expected](bash-integer-expr-error) — non-numeric values
- [Test Expression Error](bash-test-expr-error) — invalid test syntax
