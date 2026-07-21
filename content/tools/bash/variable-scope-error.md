---
title: "[Solution] Bash Variable Scope Error"
description: "Fix Bash variable scope errors when variables behave unexpectedly across functions and subshells."
tools: ["bash"]
error-types: ["tool-error"]
severities: ["warning"]
---

# Bash Variable Scope Error

Bash variables lose values or behave unexpectedly due to scope issues.

```
Variable value lost after function call
```

## Common Causes

- Variables inside functions are global by default
- Subshell loses variable modifications
- Pipe creates implicit subshell
- local keyword not used
- eval modifying wrong variable scope

## How to Fix

### Use local Keyword in Functions

```bash
my_func() {
    local result=""
    local count=0

    result=$(compute_something)
    count=$((count + 1))
    echo "$result"
}
# result and count are not accessible here
```

### Understand Subshell Scope

```bash
# Subshell loses changes
my_func() {
    value="changed"  # Lost after function
}

# Use command substitution - also loses changes
value=$(echo "original")

# Fix: use process substitution or temp files
my_func > >(read -r value)
```

### Export Variables for Child Processes

```bash
MY_VAR="global_value"
export MY_VAR

# Now child processes can see MY_VAR
bash -c 'echo $MY_VAR'
```

### Use Global Variables Explicitly

```bash
declare -g GLOBAL_VAR="initial"

modify_global() {
    GLOBAL_VAR="modified"
}

modify_global
echo "$GLOBAL_VAR"  # "modified"
```

### Handle Pipe Scope Issues

```bash
# Pipe creates subshell - variable changes lost
echo "test" | while read -r line; do
    count=$((count + 1))  # Lost after pipe
done

# Fix: use process substitution
count=0
while read -r line; do
    ((count++))
done < <(echo "test")
echo "$count"  # 1
```

## Examples

```bash
#!/bin/bash
# Proper variable scoping example
process_items() {
    local items=("$@")
    local processed=0

    for item in "${items[@]}"; do
        echo "Processing: $item"
        ((processed++))
    done

    echo "Total processed: $processed"
}

main() {
    local data=("a" "b" "c")
    process_items "${data[@]}"
}

main
```
