---
title: "[Solution] Unbound Variable Error"
description: "Resolve 'unbound variable' errors in Bash with nounset."
tools: ["bash"]
error-types: ["tool-error"]
severities: ["error"]
---

# [Solution] Unbound Variable Error

With `set -u` (nounset), referencing an unset variable causes an error.

### Common Causes
- `set -u` enabled and a variable is not initialized.
- Positional parameter `$1` not provided.
- Environment variable not exported.

### How to Fix
```bash
# Provide default value
echo "${MY_VAR:-default}"

# Check if variable is set
if [[ -v MY_VAR ]]; then
    echo "$MY_VAR"
fi

# For positional parameters
file="${1:?Usage: script.sh <file>}"

# Disable nounset temporarily
set +u
# ... code ...
set -u
```

### Example
```bash
# Broken
set -u
echo "$UNDECLARED_VAR"

# Fixed
set -u
echo "${UNDECLARED_VAR:-fallback}"
```
