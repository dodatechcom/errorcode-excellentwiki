---
title: "[Solution] Bash Bad Array Subscript Error"
description: "Fix 'bash: bad array subscript' when accessing or modifying array elements with invalid indices."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "bash"
tags: ["bash", "shell", "arrays", "subscript", "index", "negative-index"]
severity: "error"
---

# Array Error

## Error Message

```
bash: bad array subscript
```

## Common Causes

- Using a negative index to access an array element (not supported in Bash)
- Using a non-integer value as an array index
- Accessing an array element beyond its bounds
- Using `unset` with an invalid index on an associative array

## Solutions

### Solution 1: Use Non-Negative Integer Indices

Array indices in Bash must be non-negative integers starting from 0. Use `${#arr[@]}` to get the array length and check bounds before accessing.

```bash
#!/bin/bash
arr=("apple" "banana" "cherry")

# Wrong — negative index
echo "${arr[-1]}"  # Error: bad array subscript

# Right — use length to access last element
echo "${arr[${#arr[@]}-1]}"  # Output: cherry

# Right — use positive indices
echo "${arr[0]}"   # Output: apple
echo "${arr[1]}"   # Output: banana
echo "${arr[2]}"   # Output: cherry

# Check array length before accessing
if [ "${#arr[@]}" -gt 2 ]; then
    echo "${arr[2]}"
fi 
```

### Solution 2: Use Associative Arrays for Non-Numeric Keys

If you need string keys, use Bash associative arrays (`declare -A`) instead of indexed arrays. This avoids index validation issues.

```bash
#!/bin/bash
# Associative array with string keys
declare -A config
config[host]="localhost"
config[port]="8080"
config[debug]="true"

echo "${config[host]}:${config[port]}"

# Iterate over associative array
for key in "${!config[@]}"; do
    echo "$key = ${config[$key]}"
done

# Safely access with default
echo "${config[missing_key]:-not set}" 
```

## Prevention Tips

- Array indices in Bash are 0-based non-negative integers only
- Use `${#arr[@]}` to get array length before accessing elements
- Use `declare -A` for associative (string-keyed) arrays

## Related Errors

- [Indirect Reference Error]({< relref "/languages/bash/indirect-reference" >})
- [Variable Substitution Error]({< relref "/languages/bash/variable-substitution" >})
