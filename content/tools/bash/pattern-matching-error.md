---
title: "[Solution] Pattern Matching Error in Variable Expansion"
description: "Fix pattern matching errors in Bash ${var/pattern/replacement}."
tools: ["bash"]
error-types: ["tool-error"]
severities: ["error"]
---

# [Solution] Pattern Matching Error in Variable Expansion

The pattern in `${var/pattern/replacement}` has invalid syntax.

### Common Causes
- Unescaped special regex characters in the pattern.
- Using extended regex where basic glob is expected.
- Unbalanced brackets in the pattern.

### How to Fix
```bash
str="hello.world"

# Escape dots and special characters
echo "${str/./_}"       # hello_world

# Use glob patterns, not regex
echo "${str/*.*/match}" # match

# For complex patterns, use sed
echo "$str" | sed 's/\./-/g'
```

### Example
```bash
# Broken
echo "${str/[a-z]/X}"   # brackets interpreted as glob

# Fixed
echo "${str//./-}"      # hello-world
```
