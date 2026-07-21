---
title: "[Solution] Bash Printf Error -- Incorrect Format String Usage"
description: "Fix bash printf errors when format strings do not match argument types or count."
languages: ["bash"]
error-types: ["syntax-error"]
severities: ["error"]
---

# Bash Printf Error

This error occurs when `printf` format specifiers do not match the provided arguments.

## Common Causes

- Missing arguments for format specifiers
- Wrong specifier for argument type (e.g., %d for string)
- Format string not quoted, causing word splitting
- Extra arguments not consumed by format

## How to Fix

### Match format specifiers

```bash
# WRONG: %d expects number, receives string
printf "%d\n" "hello"

# CORRECT: use %s for strings
printf "%s\n" "hello"
```

### Quote format strings

```bash
# WRONG: format string may split
printf %s hello world

# CORRECT: quote format string
printf "%s %s\n" "hello" "world"
```

## Examples

```bash
#!/bin/bash
printf "%-20s %10d %8.2f\n" "Name" 42 3.14
printf "%-20s %10d %8.2f\n" "Alice" 25 99.50
```
