---
title: "[Solution] Bash Local Variable Error -- Incorrect Function Scope"
description: "Fix bash local variable errors when variables in functions are not properly scoped."
languages: ["bash"]
error-types: ["runtime-error"]
severities: ["error"]
---

# Bash Local Variable Error

This error occurs when variables in functions modify global state because they are not declared as `local`.

## Common Causes

- Forgetting `local` keyword in function variables
- Using `local` with `declare` incorrectly
- Expecting `local` to persist after function returns
- Global variable accidentally overwritten by function

## How to Fix

### Use local in functions

```bash
# WRONG: modifies global
process() {
    count=0  # global variable
    count=$((count + 1))
}

# CORRECT: use local
process() {
    local count=0
    count=$((count + 1))
}
```

### Check scope with declare

```bash
my_func() {
    declare -i local_count=0
    local_count=$((local_count + 1))
    echo "$local_count"
}
```

## Examples

```bash
#!/bin/bash
result=0

calculate() {
    local x=$1
    local y=$2
    result=$((x + y))
}

calculate 5 3
echo "5 + 3 = $result"
```
