---
title: "[Solution] Export Function Error"
description: "Fix 'export -f' function export errors in Bash."
tools: ["bash"]
error-types: ["tool-error"]
severities: ["error"]
---

# [Solution] Export Function Error

The `export -f` command failed to export a function to child processes.

### Common Causes
- Function not defined before export.
- Using `export -f` in non-bash shell.
- Function name contains invalid characters.

### How to Fix
```bash
# Define then export
my_func() {
    echo "hello from child"
}
export -f my_func

# Verify export
export -p | grep my_func

# Run child process
bash -c 'my_func'

# Fallback: source the function file
bash -c 'source functions.sh; my_func'
```

### Example
```bash
# Broken
export -f undefined_func

# Fixed
defined_func() { echo "ok"; }
export -f defined_func
```
