---
title: "[Solution] Bash String Length Error -- Incorrect String Operations"
description: "Fix bash string length errors when using ${#var} or other string operations on non-string variables."
languages: ["bash"]
error-types: ["runtime-error"]
severities: ["error"]
---

# Bash String Length Error

This error occurs when string operations like `${#var}` are used on unset or non-string variables.

## Common Causes

- Using `${#var}` on an unset variable with `set -u`
- Array length vs string length confusion
- Special characters in variable values affecting expansion
- Multibyte characters not counted correctly

## How to Fix

### Check variable before operations

```bash
# WRONG: may fail with set -u
len=${#UNSET_VAR}

# CORRECT: provide default
len=${#UNSET_VAR:-0}
```

### Use correct length operation

```bash
str="hello world"
echo "Length: ${#str}"  # 11

# For arrays, use ${#array[@]} for element count
arr=(a b c)
echo "Elements: ${#arr[@]}"  # 3
```

## Examples

```bash
#!/bin/bash
read -r input
if [ "${#input}" -lt 3 ]; then
    echo "Input too short"
    exit 1
fi
echo "Input: $input (${#input} chars)"
```
