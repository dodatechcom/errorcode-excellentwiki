---
title: "[Solution] = vs == in Bash Test Expressions"
description: "Understand the difference between = and == in Bash tests."
tools: ["bash"]
error-types: ["tool-error"]
severities: ["error"]
---

# [Solution] = vs == in Bash Test Expressions

Using the wrong equality operator in the wrong context causes errors.

### Common Causes
- `==` in `[ ]` (only works in Bash, not POSIX sh).
- `=` in `[[ ]]` (works but `==` is conventional).
- Confusion about string vs regex matching.

### How to Fix
```bash
# POSIX: use = in [ ]
[ "$a" = "$b" ]

# Bash: use == in [[ ]] for string comparison
[[ "$a" == "$b" ]]

# Bash: use == for regex in [[ ]]
[[ "$a" =~ ^[0-9]+$ ]]

# For pattern matching in [[ ]]
[[ "$file" == *.log ]]

# Shorthand
[[ "$a" == "$b" ]] && echo "equal"
```

### Example
```bash
# Portable (POSIX)
[ "$a" = "$b" ]

# Bash-specific
[[ "$a" == "$b" ]]
```
