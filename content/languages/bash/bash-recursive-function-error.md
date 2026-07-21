---
title: "[Solution] Bash Recursive Function Error -- Stack Overflow in Recursion"
description: "Fix bash recursive function errors when recursion depth exceeds the stack limit."
languages: ["bash"]
error-types: ["runtime-error"]
severities: ["error"]
---

# Bash Recursive Function Error

This error occurs when bash recursive functions exceed the stack depth limit, causing the script to crash.

## Common Causes

- Unbounded recursion without proper base case
- Base case condition never true due to logic error
- Deep recursion exceeding ulimit stack size
- Using recursion for tasks better suited to iteration

## How to Fix

### Ensure proper base case

```bash
# WRONG: no base case
factorial() {
    echo $(( $1 * factorial($1 - 1) ))
}

# CORRECT: proper base case
factorial() {
    if [ "$1" -le 1 ]; then
        echo 1
    else
        echo $(( $1 * $(factorial $(( $1 - 1 ))) ))
    fi
}
```

### Convert to iteration when possible

```bash
# Iterative factorial (no stack overflow risk)
factorial() {
    local result=1
    for ((i=2; i<=$1; i++)); do
        ((result *= i))
    done
    echo "$result"
}
```

## Examples

```bash
#!/bin/bash
# Safe recursive directory walk with depth limit
walk() {
    local depth=$1
    local path=$2
    [ "$depth" -le 0 ] && return
    
    for item in "$path"/*; do
        [ -d "$item" ] && walk $((depth - 1)) "$item"
    done
}

walk 5 "/home"
```
