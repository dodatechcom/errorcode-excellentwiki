---
title: "[Solution] Bash Substring Error -- Incorrect String Extraction"
description: "Fix bash substring errors when using ${var:offset:length} syntax incorrectly."
languages: ["bash"]
error-types: ["syntax-error"]
severities: ["error"]
---

# Bash Substring Error

This error occurs when bash substring expansion `${var:offset:length}` is used with incorrect offset or length values.

## Common Causes

- Negative offset not working as expected
- Length exceeding string boundary
- Missing colon in syntax
- Using substring on unset variables

## How to Fix

### Use correct substring syntax

```bash
# WRONG: wrong syntax
str="hello"
echo ${str[0:3]}  # error: arrays use [] differently

# CORRECT: use : for substring
echo ${str:0:3}  # "hel"
echo ${str:2}    # "llo"
echo ${str: -3}  # "llo" (negative offset needs space)
```

### Check string length

```bash
str="hello"
len=${#str}
echo ${str:0:$len}  # full string
```

## Examples

```bash
#!/bin/bash
str="Hello World"
echo "First 5: ${str:0:5}"
echo "Last 5: ${str: -5}"
echo "Middle: ${str:6:5}"
```
