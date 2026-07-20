---
title: "[Solution] Uppercase/Lowercase Transformation Error"
description: "Fix ${var^^} ${var,,} case transformation errors in Bash."
tools: ["bash"]
error-types: ["tool-error"]
severities: ["error"]
---

# [Solution] Uppercase/Lowercase Transformation Error

Case transformation operators `${var^^}`, `${var,,}`, `${var^}`, `${var,}` failed.

### Common Causes
- Using case transformation in Bash < 4.0.
- Applying to an unset variable.
- Incorrect syntax with count parameter.

### How to Fix
```bash
# Bash 4.0+ required
str="hello"

echo "${str^^}"    # HELLO (all upper)
echo "${str,,}"    # hello (all lower)
echo "${str^}"     # Hello (first upper)
echo "${str,}"     # hello (first lower)

# With count parameter (Bash 4.4+)
echo "${str^^1}"   # Hello (first 1 char upper)

# Fallback for older Bash
echo "$str" | tr '[:lower:]' '[:upper:]'
```

### Example
```bash
# Broken (Bash 3.x)
echo "${str^^}"

# Fixed
echo "$str" | tr '[:lower:]' '[:upper:]'
```
