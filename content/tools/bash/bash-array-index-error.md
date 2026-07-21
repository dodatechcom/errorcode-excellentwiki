---
title: "[Solution] Bash Array Index Error"
description: "Fix Bash array index errors when accessing arrays with invalid or out-of-range indices."
tools: ["bash"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Index is negative or non-numeric
- Index exceeds the array length
- Array not initialized properly
- Associative array key does not exist
- Off-by-one error with zero-based indexing

## How to Fix

- Validate index before accessing the array
- Check array length with `${#array[@]}`
- Use associative arrays with quoted keys for string indices

## Examples

```bash
#!/bin/bash
arr=("one" "two" "three")

# Check bounds before access
idx=5
if (( idx < ${#arr[@]} )); then
    echo "${arr[$idx]}"
else
    echo "Index out of range"
fi

# Associative array
declare -A map
map["key1"]="value1"
echo "${map["key1"]}"
echo "${map["missing"]:-not found}"
```
