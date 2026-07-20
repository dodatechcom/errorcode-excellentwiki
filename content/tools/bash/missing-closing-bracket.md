---
title: "[Solution] Missing Closing Bracket `]`"
description: "Resolve 'missing ]' error in Bash test expressions."
tools: ["bash"]
error-types: ["tool-error"]
severities: ["error"]
---

# [Solution] Missing Closing Bracket `]`

The `test` or `[` command requires a matching `]` to close the expression.

### Common Causes
- Forgetting the closing `]` in a test expression.
- Spaces around `[` but not around `]`.
- Nested conditions with missing brackets.

### How to Fix
```bash
# Use [[ ]] instead of [ ] (bash-specific, more forgiving)
[[ -f "$file" ]]

# Always ensure spaces around test operators
[ -z "$var" ]

# shellcheck will flag missing brackets
shellcheck script.sh
```

### Example
```bash
# Broken
if [ -f "$file"
then
    echo "exists"
fi

# Fixed
if [ -f "$file" ]; then
    echo "exists"
fi
```
