---
title: "[Solution] Errtrace (set -E) Error"
description: "Fix errtrace (set -E) ERR trap inheritance errors."
tools: ["bash"]
error-types: ["tool-error"]
severities: ["error"]
---

# [Solution] Errtrace (set -E) Error

`set -E` (errtrace) causes ERR traps to fire in functions and subshells.

### Common Causes
- ERR trap fires unexpectedly in called functions.
- Subshells inherit ERR trap causing cascading errors.
- Performance impact from trap propagation.

### How to Fix
```bash
# Enable errtrace (ERR trap in functions)
set -E

# ERR trap fires on any command failure
trap 'echo "Error on line $LINENO" >&2' ERR

# Disable errtrace
set +E

# Check status
set -o | grep errtrace

# Combine with errexit
set -eo pipefail -E    # exit on error + trap in functions
```

### Example
```bash
# Broken (ERR trap fires in every function)
set -E
trap 'echo "Error!" >&2' ERR
helper() { false; }
helper    # ERR trap fires

# Fixed
set -E
trap 'echo "Error at $BASH_COMMAND" >&2' ERR
helper() { false; }
# Disable trap in specific functions
trap - ERR
helper
trap 'echo "Error at $BASH_COMMAND" >&2' ERR
```
