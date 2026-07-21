---
title: "[Solution] Bash Array Append Error"
description: "Fix Bash array append errors when adding elements to arrays produces unexpected results."
tools: ["bash"]
error-types: ["tool-error"]
severities: ["warning"]
---

# Bash Array Append Error

Bash array append operations produce unexpected results or fail.

```
bash: arr: not found
```

## Common Causes

- Array not declared before use
- Using wrong append syntax
- Associative vs indexed array confusion
- Unquoted array expansion splitting words
- Array in subshell lost

## How to Fix

### Append with += Operator

```bash
#!/bin/bash
# Indexed array
arr=()
arr+=("first")
arr+=("second")
arr+=("third")

echo "${arr[@]}"  # first second third
```

### Append Multiple Elements

```bash
arr=(1 2)
arr+=(3 4 5)
echo "${arr[@]}"  # 1 2 3 4 5
```

### Append to Associative Array

```bash
declare -A hash
hash[key1]="value1"
hash[key2]="value2"
hash[key3]="value3"

echo "${hash[key1]}"
```

### Preserve Array in Functions

```bash
# Wrong - array lost in subshell
append_item() {
    arr+=("$1")  # Lost
}

# Correct - use global array or return via output
append_to_array() {
    local -n ref=$1
    ref+=("$2")
}

my_arr=()
append_to_array my_arr "hello"
echo "${my_arr[@]}"  # hello
```

### Expand Array Safely

```bash
arr=("file 1.txt" "file 2.txt")

# Wrong - word splitting
for f in ${arr[@]}; do echo "$f"; done

# Correct - preserve elements
for f in "${arr[@]}"; do echo "$f"; done
```

## Examples

```bash
#!/bin/bash
# Build array dynamically
declare -a files=()

while IFS= read -r -d '' file; do
    files+=("$file")
done < <(find . -name "*.log" -print0)

echo "Found ${#files[@]} log files"

for f in "${files[@]}"; do
    echo "  - $f"
done
```
