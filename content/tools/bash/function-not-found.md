---
title: "[Solution] Function Not Found Error"
description: "Resolve 'function not found' or 'command not found' for functions."
tools: ["bash"]
error-types: ["tool-error"]
severities: ["error"]
---

# [Solution] Function Not Found Error

Bash cannot locate the function or command being invoked.

### Common Causes
- Function not defined before being called.
- Function defined in a different scope (subshell, sourced file).
- Typo in function name.

### How to Fix
```bash
# Define function before calling it
my_func() {
    echo "hello"
}
my_func

# Check if function exists
declare -f my_func    # prints function definition
type my_func          # shows where it's defined

# Source files containing functions
source ./my_functions.sh

# List all functions
declare -F
```

### Example
```bash
# Broken
my_func
my_func() { echo "hi"; }

# Fixed
my_func() { echo "hi"; }
my_func
```
