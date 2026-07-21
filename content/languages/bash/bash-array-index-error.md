---
title: "[Solution] Bash Array Index Error -- Out of Bounds Array Access"
description: "Fix bash array index errors when accessing array elements with invalid indices."
languages: ["bash"]
error-types: ["runtime-error"]
severities: ["error"]
---

# Bash Array Index Error

This error occurs when bash arrays are accessed with indices that do not exist or are out of bounds.

## Common Causes

- Accessing array element with index greater than array length
- Using negative indices (not supported in bash arrays)
- Forgetting that arrays are 0-indexed
- Accessing associative array with non-existent key

## How to Fix

### Check array length first

```bash
# WRONG: may access out of bounds
arr=(a b c)
echo "${arr[5]}"  # empty, but no error

# CORRECT: check length
if [ ${#arr[@]} -gt 5 ]; then
    echo "${arr[5]}"
else
    echo "Index out of bounds"
fi
```

### Use safe access patterns

```bash
# Safe element access
element="${arr[$index]:-}"
if [ -n "$element" ]; then
    echo "Got: $element"
fi
```

## Examples

```bash
#!/bin/bash
fruits=(apple banana cherry)
echo "First: ${fruits[0]}"
echo "Last index: $((${#fruits[@]} - 1))"
echo "Last: ${fruits[$((${#fruits[@]} - 1))]}"
```
