---
title: "[Solution] Bash Command Substitution Error -- Incorrect $( ) Usage"
description: "Fix bash command substitution errors when using $( ) or backticks incorrectly."
languages: ["bash"]
error-types: ["syntax-error"]
severities: ["error"]
---

# Bash Command Substitution Error

This error occurs when command substitution `$()` or backticks are used incorrectly, causing unexpected results.

## Common Causes

- Nested backticks require complex escaping
- Command substitution capturing stderr along with stdout
- Not quoting command substitution results
- Using backticks instead of `$()`

## How to Fix

### Use $() instead of backticks

```bash
# WRONG: backticks are harder to read/escape
result=`ls -la`

# CORRECT: use $()
result=$(ls -la)
```

### Capture only stdout

```bash
# WRONG: captures error messages
files=$(ls nonexistent_dir)

# CORRECT: redirect stderr
files=$(ls nonexistent_dir 2>/dev/null)

# Or capture separately
result=$(ls nonexistent_dir 2>&1)
```

## Examples

```bash
#!/bin/bash
count=$(find . -name "*.txt" | wc -l)
echo "Found $count text files"
```
