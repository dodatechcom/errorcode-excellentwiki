---
title: "[Solution] Bash Array Error"
description: "Fix bash array errors when creating, accessing, or iterating over arrays incorrectly in Bash."
languages: ["bash"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["array", "index", "elements", "subscript", "declaration"]
weight: 5
---

# Bash Array Error Fix

Array errors include incorrect declaration, accessing non-existent indices, word splitting on array expansion, or mixing indexed and associative arrays.

## What This Error Means

Bash supports indexed arrays (integer indices) and associative arrays (string keys). Errors occur from incorrect syntax for declaration, expansion, or assignment.

## Common Causes

- Using `${arr[0]}` instead of `${arr[@]}` to expand all elements
- Missing `[@]` when expanding entire array
- Associative array missing `declare -A`
- Array index out of bounds (returns empty, not error)
- Assigning to array element before declaring array

## How to Fix

### 1. Declare arrays correctly

```bash
# Indexed array
arr=(a b c)

# Associative array (must use declare)
declare -A assoc
assoc[name]="value"
```

### 2. Expand all elements with [@

```bash
arr=("one two" "three four")

# WRONG: word splits "one two" into two elements
echo ${arr[@]}

# RIGHT: quoted to preserve elements
echo "${arr[@]}"
```

### 3. Access individual elements

```bash
arr=(a b c)

echo ${arr[0]}  # First element (a)
echo ${arr[2]}  # Third element (c)
echo ${#arr[@]} # Length (3)
```

### 4. Append to arrays properly

```bash
arr=()
arr+=(new1)
arr+=(new2)
echo "${arr[@]}"  # new1 new2
```

## Related Errors

- [Associative Array](bash-associative-array) — associative array errors
- [Bad Substitution](bash-bad-substitution) — variable expansion issues
