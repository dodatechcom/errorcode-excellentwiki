---
title: "[Solution] Bash Arithmetic Expansion Error -- Incorrect $(( )) Usage"
description: "Fix bash arithmetic expansion errors when using $(( )) for calculations incorrectly."
languages: ["bash"]
error-types: ["syntax-error"]
severities: ["error"]
---

# Bash Arithmetic Expansion Error

This error occurs when arithmetic expansion `$(( ))` is used with invalid expressions or incorrect syntax.

## Common Causes

- Using `$(( ))` for string operations (only integers)
- Missing closing `)` in expression
- Using variables without `$` inside arithmetic
- Division by zero in arithmetic expressions

## How to Fix

### Use correct arithmetic syntax

```bash
# WRONG: missing closing paren
result=$((1 + 2

# CORRECT: match parens
result=$((1 + 2))

# Variables don't need $ inside $(( ))
x=5
result=$((x * 2))
```

### Handle division by zero

```bash
a=10
b=0
if [ "$b" -ne 0 ]; then
    result=$((a / b))
else
    echo "Cannot divide by zero"
fi
```

## Examples

```bash
#!/bin/bash
x=10
y=3
echo "Add: $((x + y))"
echo "Sub: $((x - y))"
echo "Mul: $((x * y))"
echo "Div: $((x / y))"
echo "Mod: $((x % y))"
```
