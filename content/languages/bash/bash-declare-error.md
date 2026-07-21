---
title: "[Solution] Bash Declare Error -- Incorrect Variable Declaration"
description: "Fix bash declare errors when using declare for variable types or attributes incorrectly."
languages: ["bash"]
error-types: ["syntax-error"]
severities: ["error"]
---

# Bash Declare Error

This error occurs when `declare` is used with incorrect flags or for incompatible variable types.

## Common Causes

- Using `declare -i` for string values
- `declare -r` for read-only but then trying to modify
- `declare -A` on bash 3.x (associative arrays)
- Mixing declare flags incorrectly

## How to Fix

### Use correct declare flags

```bash
# WRONG: declare -i for string
declare -i count="hello"  # error or unexpected behavior

# CORRECT: declare -i for integers
declare -i count=0
count=42

# CORRECT: declare -s for strings (or no flag)
declare -- name="Alice"
```

### Use read-only carefully

```bash
# WRONG: trying to modify readonly
declare -r CONST="immutable"
CONST="new"  # error

# CORRECT: only set once
declare -r CONST="immutable"
```

## Examples

```bash
#!/bin/bash
declare -i age=30
declare -r PI=3.14159
declare -- name="Alice"
declare -A settings=([debug]=true [verbose]=false)
```
