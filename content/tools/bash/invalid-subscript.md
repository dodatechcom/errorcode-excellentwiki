---
title: "[Solution] Invalid Subscript Error"
description: "Fix invalid subscript errors when accessing Bash arrays."
tools: ["bash"]
error-types: ["tool-error"]
severities: ["error"]
---

# [Solution] Invalid Subscript Error

The subscript used to index an array is syntactically invalid.

### Common Causes
- Using a string where an integer is expected.
- Bash version does not support the subscript syntax.
- Incorrect associative array syntax.

### How to Fix
```bash
# Declare associative arrays properly
declare -A mymap
mymap[key]="value"

# Use integer indices for indexed arrays
declare -a arr
arr[0]="first"

# Check bash version
bash --version
```

### Example
```bash
# Broken
declare -A arr
arr[0]="value"     # wrong for associative

# Fixed
declare -A arr
arr[key]="value"
```
