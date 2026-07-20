---
title: "[Solution] Nounset (set -u) Conflict Error"
description: "Fix conflicts with nounset (set -u) in Bash scripts."
tools: ["bash"]
error-types: ["tool-error"]
severities: ["error"]
---

# [Solution] Nounset (set -u) Conflict Error

`set -u` causes errors when accessing unset variables, which can conflict with common patterns.

### Common Causes
- `${var:-default}` not used for optional variables.
- Positional parameters not checked before access.
- Array expansion `"${arr[@]}"` on empty array (Bash < 4.4).

### How to Fix
```bash
# Use default values for optional variables
echo "${MY_VAR:-default_value}"

# Check positional parameters
[[ $# -ge 1 ]] || { echo "Usage: script.sh <arg>" >&2; exit 1; }
file="$1"

# Handle empty arrays safely (Bash 4.4+)
arr=()
if (( ${#arr[@]} > 0 )); then
    echo "${arr[@]}"
fi

# Temporarily disable for known-safe code
set +u
# ... access potentially unset vars ...
set -u
```

### Example
```bash
# Broken
set -u
arr=()
echo "${arr[@]}"    # error: unbound variable

# Fixed
set -u
arr=()
[[ ${#arr[@]} -gt 0 ]] && echo "${arr[@]}"
```
