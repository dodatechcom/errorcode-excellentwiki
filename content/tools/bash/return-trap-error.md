---
title: "[Solution] RETURN Trap Error in Bash"
description: "Fix RETURN trap handler errors in Bash functions."
tools: ["bash"]
error-types: ["tool-error"]
severities: ["error"]
---

# [Solution] RETURN Trap Error in Bash

The RETURN trap fires when a function or source completes and may have issues.

### Common Causes
- RETURN trap fires in functions that should not be trapped.
- Trap modifies the return value unexpectedly.
- RETURN trap in sourced files fires at script end.

### How to Fix
```bash
# Set RETURN trap in a function
my_func() {
    trap 'echo "Returning from my_func"' RETURN
    # ... function body ...
}

# The trap fires automatically when function exits
my_func

# Remove RETURN trap
trap - RETURN

# Check current RETURN trap
trap -p RETURN

# Use in sourced files
trap 'cleanup_on_return' RETURN
```

### Example
```bash
# Broken (RETURN trap in every function)
trap 'echo "return"' RETURN
func_a() { :; }    # fires trap
func_b() { :; }    # fires trap

# Fixed (trap only in specific function)
func_a() {
    trap 'echo "returning from func_a"' RETURN
    echo "inside func_a"
}
```
