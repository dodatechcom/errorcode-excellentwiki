---
title: "[Solution] Bash Array Iteration Error -- Incorrect Loop Patterns"
description: "Fix bash array iteration errors when looping over arrays incorrectly."
languages: ["bash"]
error-types: ["runtime-error"]
severities: ["error"]
---

# Bash Array Iteration Error

This error occurs when arrays are iterated incorrectly, losing elements or causing word splitting.

## Common Causes

- Not quoting `${array[@]}` causing word splitting
- Using wrong syntax for associative array keys
- Iterating over indices instead of values unintentionally
- Empty array elements being skipped

## How to Fix

### Quote array expansion

```bash
# WRONG: unquoted, splits on whitespace
arr=("hello world" "foo bar")
for item in ${arr[@]}; do
    echo "$item"  # splits into "hello" "world" "foo" "bar"
done

# CORRECT: quoted
for item in "${arr[@]}"; do
    echo "$item"  # "hello world" "foo bar"
done
```

### Iterate over indices

```bash
arr=(a b c d)
for i in "${!arr[@]}"; do
    echo "Index $i: ${arr[$i]}"
done
```

## Examples

```bash
#!/bin/bash
fruits=("apple" "banana" "cherry")
for fruit in "${fruits[@]}"; do
    echo "Fruit: $fruit"
done
```
