---
title: "[Solution] Integer vs String Comparison Error"
description: "Fix integer (-eq) vs string (=) comparison errors in Bash."
tools: ["bash"]
error-types: ["tool-error"]
severities: ["error"]
---

# [Solution] Integer vs String Comparison Error

Using the wrong comparison operator for the data type.

### Common Causes
- Using `-eq` on strings containing non-numeric data.
- Using `=` on integers (works but less efficient).
- Mixing numeric and string comparison operators.

### How to Fix
```bash
# Integer comparison
[[ 5 -eq 5 ]]    # true (integer equal)
[[ 5 -gt 3 ]]    # true (greater than)
[[ 5 -lt 10 ]]   # true (less than)

# String comparison
[[ "abc" == "abc" ]]    # true (string equal)
[[ "abc" != "xyz" ]]    # true (string not equal)

# Never do:
# [ "abc" -eq "abc" ]    # error: not an integer
```

### Example
```bash
# Broken
a="hello"
[ "$a" -eq "hello" ]    # error: not an integer

# Fixed
[[ "$a" == "hello" ]]
```
