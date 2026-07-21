---
title: "[Solution] Bash Arithmetic Error -- Integer Division Issues"
description: "Fix bash arithmetic errors when performing integer division or modulus operations."
languages: ["bash"]
error-types: ["runtime-error"]
severities: ["error"]
---

# Bash Arithmetic Error

This error occurs when bash arithmetic expressions encounter division by zero or invalid operations.

## Common Causes

- Division by zero in `$(( ))` or `let` expressions
- Using float values in integer-only arithmetic
- Modulus operator with zero divisor
- Uninitialized variables in arithmetic context

## How to Fix

### Check for division by zero

```bash
# WRONG: potential division by zero
result=$((10 / divisor))

# CORRECT: check first
if [ "$divisor" -ne 0 ]; then
    result=$((10 / divisor))
else
    echo "Error: division by zero"
    exit 1
fi
```

### Use bc for floating point

```bash
# WRONG: bash only does integer arithmetic
result=$((10 / 3))  # result is 3, not 3.333

# CORRECT: use bc for floats
result=$(echo "scale=2; 10 / 3" | bc)
```

## Examples

```bash
#!/bin/bash
a=17
b=5
echo "Add: $((a + b))"
echo "Sub: $((a - b))"
echo "Mul: $((a * b))"
echo "Div: $((a / b))"
echo "Mod: $((a % b))"
```
