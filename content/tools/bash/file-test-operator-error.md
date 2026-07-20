---
title: "[Solution] File Test Operator Error"
description: "Fix file test operator errors (-f, -d, -e) in Bash."
tools: ["bash"]
error-types: ["tool-error"]
severities: ["error"]
---

# [Solution] File Test Operator Error

A file test operator received an invalid or missing argument.

### Common Causes
- Variable is empty or unset.
- Path contains special characters.
- File does not exist.

### How to Fix
```bash
# Quote variable in file tests
[[ -f "$file" ]]    # file exists and is regular
[[ -d "$dir" ]]     # directory exists
[[ -e "$path" ]]    # path exists (any type)
[[ -r "$file" ]]    # readable
[[ -w "$file" ]]    # writable
[[ -x "$file" ]]    # executable
[[ -s "$file" ]]    # non-empty file
[[ -L "$file" ]]    # symbolic link

# Always check for empty variable
[[ -n "${file:-}" ]] && [[ -f "$file" ]]
```

### Example
```bash
# Broken
[[ -f $undefined_var ]]    # unbound variable

# Fixed
file="${1:-/etc/hostname}"
[[ -f "$file" ]] && cat "$file"
```
