---
title: "[Solution] Parameter Null or Not Set"
description: "Fix 'parameter null or not set' error in Bash scripts."
tools: ["bash"]
error-types: ["tool-error"]
severities: ["error"]
---

# [Solution] Parameter Null or Not Set

The variable is either unset or set to an empty string, and `set -u` is active.

### Common Causes
- Environment variable not set by calling script.
- Missing configuration file.
- `set -u` combined with empty optional variables.

### How to Fix
```bash
# Use default value syntax
echo "${CONFIG_FILE:-/etc/myapp.conf}"

# Use error message syntax
: "${DB_HOST:?DB_HOST must be set}"

# Check before use
if [[ -n "${DB_HOST:-}" ]]; then
    connect "$DB_HOST"
else
    echo "DB_HOST is not set" >&2
    exit 1
fi
```

### Example
```bash
# Broken
set -u
echo "$HOME"  # works
echo "$MISSING"  # error

# Fixed
echo "${MISSING:-/tmp}"
```
