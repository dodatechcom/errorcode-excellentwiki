---
title: "[Solution] Ambiguous Redirect Error"
description: "Fix 'ambiguous redirect' errors in Bash I/O redirection."
tools: ["bash"]
error-types: ["tool-error"]
severities: ["error"]
---

# [Solution] Ambiguous Redirect Error

A redirection has an ambiguous target, usually due to an empty or multi-word variable.

### Common Causes
- Unquoted variable in redirection target.
- Variable is empty or unset.
- Multiple `>` on the same line.

### How to Fix
```bash
# Quote the redirect target
output="/path/to/file"
cat file > "$output"

# Check variable before redirecting
if [[ -n "${output:-}" ]]; then
    echo "data" > "$output"
fi

# Use a single redirect per line
echo "a" > file1
echo "b" > file2
```

### Example
```bash
# Broken
output=""
echo "hello" > $output   # ambiguous redirect

# Fixed
output="/tmp/out.txt"
echo "hello" > "$output"
```
