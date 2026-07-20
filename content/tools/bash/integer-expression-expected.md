---
title: "[Solution] Integer Expression Expected"
description: "Fix 'integer expression expected' errors in Bash arithmetic."
tools: ["bash"]
error-types: ["tool-error"]
severities: ["error"]
---

# [Solution] Integer Expression Expected

A command expecting an integer received a non-numeric value.

### Common Causes
- Variable contains non-numeric data.
- Missing quotes around variables with possible spaces.
- Comparison operator used on strings.

### How to Fix
```bash
# Validate before arithmetic
if [[ "$var" =~ ^[0-9]+$ ]]; then
    echo $(( var + 1 ))
fi

# Use default value
val=$(( ${var:-0} + 1 ))

# Use [[ ]] for integer comparison
[[ "$a" =~ ^[0-9]+$ ]] && [[ "$b" =~ ^[0-9]+$ ]] && echo $(( a + b ))
```

### Example
```bash
# Broken
var="abc"
echo $(( var + 1 ))    # integer expression expected

# Fixed
var="123"
echo $(( var + 1 ))    # 124
```
