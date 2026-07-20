---
title: "[Solution] Argument List Too Long Error"
description: "Fix 'argument list too long' (E2BIG) error in Bash."
tools: ["bash"]
error-types: ["tool-error"]
severities: ["error"]
---

# [Solution] Argument List Too Long Error

The total size of arguments and environment exceeds the OS limit (ARG_MAX).

### Common Causes
- Glob `*` expanding to thousands of files.
- Very long string passed as argument.

### How to Fix
```bash
# Use find + xargs instead of glob
find /dir -name "*.txt" | xargs rm

# Use find -exec for safety with special characters
find /dir -name "*.txt" -exec rm {} +

# Check ARG_MAX
getconf ARG_MAX

# Use while loop for batch processing
find /dir -name "*.txt" -print0 | while IFS= read -r -d '' f; do
    rm "$f"
done
```

### Example
```bash
# Broken
rm *.log    # if too many .log files

# Fixed
find . -name "*.log" -exec rm {} +
```
