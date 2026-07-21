---
title: "[Solution] Bash String Replace Error -- Incorrect Pattern Substitution"
description: "Fix bash string replace errors when using ${var/pattern/replacement} syntax."
languages: ["bash"]
error-types: ["syntax-error"]
severities: ["error"]
---

# Bash String Replace Error

This error occurs when bash string substitution `${var/pattern/replacement}` is used incorrectly.

## Common Causes

- Pattern not matching expected string
- Using wrong number of `/` for global replacement
- Unescaped special characters in pattern
- Missing variable expansion syntax

## How to Fix

### Use correct replacement syntax

```bash
# WRONG: wrong number of slashes
str="hello world"
echo ${str/hello}  # removes first occurrence only

# CORRECT: use // for global replacement
echo ${str//o/0}  # "hell0 w0rld"
```

### Escape special characters

```bash
str="price: $100"
echo ${str/\$/\\\$}  # escape dollar sign
```

## Examples

```bash
#!/bin/bash
path="/home/user/documents/file.txt"
echo ${path//\//_}  # "home_user_documents_file.txt"
echo ${path%.txt}   # remove extension
echo ${path##*/}    # basename
```
