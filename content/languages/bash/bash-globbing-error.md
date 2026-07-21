---
title: "[Solution] Bash Globbing Error -- Incorrect File Pattern Matching"
description: "Fix bash globbing errors when file patterns match incorrectly or cause unexpected behavior."
languages: ["bash"]
error-types: ["runtime-error"]
severities: ["error"]
---

# Bash Globbing Error

This error occurs when bash globbing patterns (`*`, `?`, `[a-z]`) produce unexpected results or errors.

## Common Causes

- Glob expanding to too many files causing argument list too long
- Pattern matching hidden files unintentionally
- `[` bracket expressions with incorrect ranges
- Glob inside quotes treating pattern literally

## How to Fix

### Handle large file lists

```bash
# WRONG: argument list too long
rm *.log

# CORRECT: use find with delete
find . -name "*.log" -delete
# or use nullglob
shopt -s nullglob
files=(*.log)
rm "${files[@]}"
```

### Quote to prevent expansion

```bash
# Literal asterisk
echo "*"

# Pattern match
for f in *; do
    echo "$f"
done
```

## Examples

```bash
#!/bin/bash
# Safe glob expansion
shopt -s nullglob
for file in /var/log/*.log; do
    echo "Processing: $file"
done
```
