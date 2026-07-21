---
title: "[Solution] Bash Function Return Error -- Incorrect Return Value Handling"
description: "Fix bash function return errors when using return vs echo for function output."
languages: ["bash"]
error-types: ["runtime-error"]
severities: ["error"]
---

# Bash Function Return Error

This error occurs when functions use `return` instead of `echo` for output, or when return values are not captured correctly.

## Common Causes

- Using `return` for output (return only sets exit status 0-255)
- Not using `$()` to capture function output
- Forgetting that return values only work in subshells
- Function called without capturing output

## How to Fix

### Use echo for output, return for status

```bash
# WRONG: return can only return 0-255
get_value() {
    return "some string"  # error
}

# CORRECT: use echo for output
get_value() {
    echo "some string"
}

# Capture output
result=$(get_value)
```

### Use return for exit status

```bash
validate() {
    if [ -f "$1" ]; then
        return 0  # success
    else
        return 1  # failure
    fi
}

if validate "config.txt"; then
    echo "Config exists"
fi
```

## Examples

```bash
#!/bin/bash
add() {
    echo $(( $1 + $2 ))
}

sum=$(add 5 3)
echo "5 + 3 = $sum"
```
