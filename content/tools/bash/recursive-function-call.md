---
title: "[Solution] Infinite Recursive Function Call"
description: "Fix infinite recursion and stack overflow in Bash functions."
tools: ["bash"]
error-types: ["tool-error"]
severities: ["error"]
---

# [Solution] Infinite Recursive Function Call

A function calls itself without a proper base case, causing stack overflow.

### Common Causes
- Missing or incorrect base/termination condition.
- Function calls itself with same arguments.
- Stack depth exceeded (typically 1000-10000 levels).

### How to Fix
```bash
# Add a base case
fib() {
    local n=$1
    if (( n <= 1 )); then
        echo "$n"
        return
    fi
    echo $(( $(fib $((n-1))) + $(fib $((n-2))) ))
}

# Track recursion depth
recurse() {
    local depth=${2:-0}
    if (( depth > 100 )); then
        echo "Max recursion depth reached" >&2
        return 1
    fi
    recurse "$1" $((depth + 1))
}
```

### Example
```bash
# Broken
countdown() {
    echo $1
    countdown $(( $1 - 1 ))    # never stops
}

# Fixed
countdown() {
    (( $1 <= 0 )) && return
    echo $1
    countdown $(( $1 - 1 ))
}
countdown 5
```
