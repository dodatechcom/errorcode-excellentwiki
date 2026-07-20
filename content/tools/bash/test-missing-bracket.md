---
title: "[Solution] Test Command: Missing `]`"
description: "Fix '[: missing `]' errors in Bash test expressions."
tools: ["bash"]
error-types: ["tool-error"]
severities: ["error"]
---

# [Solution] Test Command: Missing `]`

The `[` command requires a matching `]` as the last argument.

### Common Causes
- Forgetting closing `]`.
- Using `]` with wrong spacing.
- Nested test expressions without proper syntax.

### How to Fix
```bash
# Correct [ ] syntax (spaces required)
[ -f "$file" ] && echo "exists"

# Use [[ ]] instead (no closing bracket needed in if-then)
if [[ -f "$file" ]]; then
    echo "exists"
fi

# Correct brace placement
[ -n "$var" ]    # -n tests non-empty string
```

### Example
```bash
# Broken
if [ -f "$file"    # missing ]

# Fixed
if [ -f "$file" ]; then
    echo "exists"
fi
```
