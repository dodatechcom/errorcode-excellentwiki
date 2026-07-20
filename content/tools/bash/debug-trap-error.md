---
title: "[Solution] DEBUG Trap Error in Bash"
description: "Fix DEBUG trap handler errors in Bash scripts."
tools: ["bash"]
error-types: ["tool-error"]
severities: ["error"]
---

# [Solution] DEBUG Trap Error in Bash

The DEBUG trap fires before each command and can cause issues if not handled carefully.

### Common Causes
- Trap function has errors causing cascading failures.
- Trap modifies variables used by the current command.
- Infinite recursion from trap calling itself.

### How to Fix
```bash
# Set DEBUG trap
trap 'echo "Line $LINENO: $BASH_COMMAND" >&2' DEBUG

# Use a guard to prevent recursion
__debugging=0
trap '
    if (( __debugging == 0 )); then
        __debugging=1
        echo "Line $LINENO" >&2
        __debugging=0
    fi
' DEBUG

# Disable DEBUG trap
trap - DEBUG

# Check current DEBUG trap
trap -p DEBUG
```

### Example
```bash
# Broken (infinite recursion)
trap 'echo "debug"; false' DEBUG    # false triggers ERR -> more debug

# Fixed
trap 'echo "debug: $BASH_COMMAND" >&2' DEBUG
```
