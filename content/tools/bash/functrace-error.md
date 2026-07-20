---
title: "[Solution] Functrace (set -T) Error"
description: "Fix functrace (set -T) and function tracing errors in Bash."
tools: ["bash"]
error-types: ["tool-error"]
severities: ["error"]
---

# [Solution] Functrace (set -T) Error

`set -T` inherits ERR and DEBUG traps in functions, causing unexpected behavior.

### Common Causes
- `set -T` causes traps to fire in nested functions.
- Performance degradation from trap inheritance.
- Unexpected debug output from library functions.

### How to Fix
```bash
# Enable function tracing
set -T

# Inherit DEBUG trap (see function calls)
trap 'echo "DEBUG: $BASH_COMMAND" >&2' DEBUG

# Disable function tracing
set +T

# Check functrace status
set -o | grep functrace

# Use errtrace for ERR trap inheritance
set -E    # or set -o errtrace
```

### Example
```bash
# Broken (triggers in every function call)
set -T
trap 'echo "debug: $BASH_COMMAND"' DEBUG
func() { :; }    # prints debug for every command in func

# Fixed (targeted tracing)
set -T
trap 'echo "debug: $BASH_COMMAND" >&2' DEBUG
# Only trace specific function
my_debug_func
set +T
```
