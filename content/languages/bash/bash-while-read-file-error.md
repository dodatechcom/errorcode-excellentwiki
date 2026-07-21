---
title: "[Solution] Bash While Read File Error -- Incorrect File Line Reading"
description: "Fix bash while read file errors when reading files line by line incorrectly."
languages: ["bash"]
error-types: ["runtime-error"]
severities: ["error"]
---

# Bash While Read File Error

This error occurs when reading files line by line with `while read` is done incorrectly, causing data loss or corruption.

## Common Causes

- Missing `-r` flag causing backslash interpretation
- Not quoting `$line` in loop body
- Using `cat file | while read` instead of redirect
- Empty last line being skipped

## How to Fix

### Use correct while read pattern

```bash
# WRONG: cat pipe creates subshell
cat file.txt | while read line; do
    echo "$line"
done

# CORRECT: redirect input
while IFS= read -r line; do
    echo "$line"
done < file.txt
```

### Handle empty lines

```bash
while IFS= read -r line || [ -n "$line" ]; do
    process "$line"
done < file.txt
```

## Examples

```bash
#!/bin/bash
while IFS= read -r -u 3 line; do
    echo "Line: $line"
done 3< file.txt
```
