---
title: "[Solution] Variable Length Expansion Error"
description: "Fix ${#var} string length errors in Bash."
tools: ["bash"]
error-types: ["tool-error"]
severities: ["error"]
---

# [Solution] Variable Length Expansion Error

The `${#var}` syntax for string length failed.

### Common Causes
- Using `${#array[@]}` incorrectly (should be `${#array[@]}` for count, `${#array[0]}` for first element length).
- Variable name contains invalid characters.
- Bash version incompatibility.

### How to Fix
```bash
str="hello"

# Get string length
echo "${#str}"    # 5

# Get array element count
arr=(a b c)
echo "${#arr[@]}" # 3

# Get specific element length
echo "${#arr[0]}" # 1
```

### Example
```bash
# Broken
echo "${#}"    # no variable specified

# Fixed
var="test"
echo "${#var}" # 4
```
