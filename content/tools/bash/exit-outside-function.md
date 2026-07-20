---
title: "[Solution] Exit in Subshell Error"
description: "Understand exit vs return in Bash subshells and functions."
tools: ["bash"]
error-types: ["tool-error"]
severities: ["error"]
---

# [Solution] Exit in Subshell Error

`exit` in a subshell only exits the subshell, not the parent script.

### Common Causes
- Using `exit` inside `()` expecting to stop the script.
- `exit` in a piped subshell.
- Unexpected subshell creation.

### How to Fix
```bash
# exit in () only exits the subshell
(echo "inside"; exit 1)    # parent continues
echo "parent continues"

# To exit the parent, use a temp file or exit code check
( exit 1 )
if [[ $? -ne 0 ]]; then
    echo "subshell failed"
    exit 1
fi

# For functions, use return (not exit) unless you want to stop everything
my_func() {
    return 1    # returns to caller
}
```

### Example
```bash
# Broken
(exit 1)    # parent doesn't see the exit

# Fixed
if ! (exit 1); then
    echo "subshell failed"
fi
```
