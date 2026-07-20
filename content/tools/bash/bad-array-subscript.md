---
title: "[Solution] Bad Array Subscript Error"
description: "Resolve 'bad array subscript' error in Bash arrays."
tools: ["bash"]
error-types: ["tool-error"]
severities: ["error"]
---

# [Solution] Bad Array Subscript Error

An invalid index was used to access a Bash array element.

### Common Causes
- Array index is negative.
- Index is not an integer.
- Associative array used with numeric index.

### How to Fix
```bash
# Array indices must be >= 0
arr=(a b c)
echo "${arr[0]}"    # valid
echo "${arr[-1]}"   # error in older bash

# Bash 4.3+ supports negative indices
echo "${arr[-1]}"   # 'c' in bash 4.3+

# Validate index
idx=5
if (( idx >= 0 && idx < ${#arr[@]} )); then
    echo "${arr[$idx]}"
fi
```

### Example
```bash
# Broken
arr=(a b c)
echo "${arr[abc]}"

# Fixed
echo "${arr[1]}"
```
