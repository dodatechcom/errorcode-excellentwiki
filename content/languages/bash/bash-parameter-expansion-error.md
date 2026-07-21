---
title: "[Solution] Bash Parameter Expansion Error -- Incorrect Variable Manipulation"
description: "Fix bash parameter expansion errors when using ${var:-default} or other expansion syntax incorrectly."
languages: ["bash"]
error-types: ["syntax-error"]
severities: ["error"]
---

# Bash Parameter Expansion Error

This error occurs when bash parameter expansion syntax is used incorrectly, producing unexpected results.

## Common Causes

- Wrong syntax for default values (`:-` vs `-`)
- Using `${var:?}` when variable should not be required
- Missing colon in expansion operators
- Incorrect substring or pattern matching syntax

## How to Fix

### Use correct expansion syntax

```bash
# WRONG: missing colon
echo ${var-default}  # only if unset, not if empty

# CORRECT: with colon, works for empty too
echo ${var:-default}  # if unset or empty
```

### Use correct substring

```bash
str="hello world"
echo ${str:0:5}    # "hello"
echo ${str:6}      # "world"
echo ${#str}       # 11
```

## Examples

```bash
#!/bin/bash
name="${1:-Guest}"
echo "Hello, $name!"
```
