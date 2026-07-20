---
title: "[Solution] Invalid Variable Name"
description: "Fix invalid variable name errors in Bash assignments."
tools: ["bash"]
error-types: ["tool-error"]
severities: ["error"]
---

# [Solution] Invalid Variable Name

Variable names must start with a letter or underscore and contain only alphanumerics and underscores.

### Common Causes
- Variable name starts with a digit.
- Variable name contains hyphens or special characters.
- Spaces around `=` in assignment.

### How to Fix
```bash
# Variable names: [a-zA-Z_][a-zA-Z0-9_]*
my_var=1       # correct
my-var=1       # incorrect
1var=1         # incorrect

# No spaces around =
var="hello"    # correct
var = "hello"  # incorrect (runs command 'var' with args '=' '"hello"')
```

### Example
```bash
# Broken
my-var="test"
123abc="bad"

# Fixed
my_var="test"
_123abc="ok"
```
