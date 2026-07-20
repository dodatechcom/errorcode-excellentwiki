---
title: "[Solution] String Null/Empty Check Error"
description: "Fix string null and empty check errors in Bash."
tools: ["bash"]
error-types: ["tool-error"]
severities: ["error"]
---

# [Solution] String Null/Empty Check Error

Incorrect syntax for checking if a string is null or empty.

### Common Causes
- Using `[ -z $var ]` without quotes.
- Mixing `-z` and `-n` logic.
- Confusing unset with empty.

### How to Fix
```bash
# Check if empty string
[[ -z "$var" ]]      # true if empty or unset
[[ -n "$var" ]]      # true if non-empty

# Use parameter expansion
[[ -z "${var:-}" ]]  # true if unset or empty
[[ -n "${var:-}" ]]  # true if set and non-empty

# Quote variables always
[[ -z "$var" ]]      # correct
[[ -z $var ]]        # may fail if var contains spaces
```

### Example
```bash
# Broken
var=""
[ -z $var ]    # error: too many arguments

# Fixed
[ -z "$var" ]
```
