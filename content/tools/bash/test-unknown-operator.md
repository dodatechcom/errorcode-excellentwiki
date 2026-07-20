---
title: "[Solution] Test Command: Unknown Operator"
description: "Fix 'test: unknown operator' errors in Bash conditionals."
tools: ["bash"]
error-types: ["tool-error"]
severities: ["error"]
---

# [Solution] Test Command: Unknown Operator

The test command received an operator it does not recognize.

### Common Causes
- Using `==` inside `[ ]` (only valid in `[[ ]]`).
- Typo in operator (e.g., `-efile` instead of `-f`).
- Using Bash-specific operators in POSIX `[ ]`.

### How to Fix
```bash
# Use = for string comparison in [ ]
[ "$a" = "$b" ]

# Use == for string comparison in [[ ]]
[[ "$a" == "$b" ]]

# Valid [ ] operators: -f, -d, -e, -r, -w, -x, -s, -z, -n, =, !=, -eq, -ne, etc.

# Use [[ ]] for regex and pattern matching
[[ "$file" == *.txt ]]
[[ "$var" =~ ^[0-9]+$ ]]
```

### Example
```bash
# Broken
[ "$a" == "$b" ]    # == not valid in [ ]

# Fixed
[ "$a" = "$b" ]
# or
[[ "$a" == "$b" ]]
```
