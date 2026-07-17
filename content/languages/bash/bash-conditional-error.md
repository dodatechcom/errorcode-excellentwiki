---
title: "[Solution] Bash Conditional Expression Error"
description: "Fix 'bash: conditional expression error' when using [[ ]] with invalid syntax, wrong operators, or unquoted variables."
languages: ["bash"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["conditional", "expression", "bracket", "test", "conditional-expr"]
weight: 5
---

# Bash Conditional Expression Error Fix

Conditional expression errors occur when `[[ ]]` has invalid syntax, uses wrong operators, or has unexpected word splitting on unquoted variables.

## What This Error Means

`[[ ]]` is the bash-specific extended test command. It supports regex matching, pattern matching, and logical operators but still requires correct syntax. Errors include malformed expressions and operator misuse.

## Common Causes

- Using `=` instead of `==` for regex/pattern matching
- Unquoted regex pattern containing spaces
- Mixing `-a`/`-o` with `&&`/`||`
- Using `(( ))` arithmetic inside `[[ ]]` incorrectly
- Missing operands for operators

## How to Fix

### 1. Use == for pattern/regex matching

```bash
# WRONG: = is for string equality
if [[ $var == ^[0-9]+$ ]]; then

# RIGHT: use == (same, but == is conventional for patterns)
if [[ $var =~ ^[0-9]+$ ]]; then
```

### 2. Quote regex patterns

```bash
# WRONG: unquoted pattern
if [[ $var =~ ^[a-z]+$ ]]; then

# RIGHT: quote to prevent special character interpretation
if [[ "$var" =~ ^[a-z]+$ ]]; then
```

### 3. Use && and || instead of -a and -o

```bash
# WRONG: deprecated
if [[ $a -gt 1 -o $b -lt 10 ]]; then

# RIGHT: use logical operators
if [[ $a -gt 1 || $b -lt 10 ]]; then
```

### 4. Handle empty variables

```bash
# [[ ]] doesn't word-split, but be safe
if [[ -n "${var:-}" ]]; then
    echo "var is set and non-empty"
fi
```

## Related Errors

- [Conditional Expression](conditional-expr) — conditional test behavior
- [Test Error](bash-test-error) — test command issues
- [Syntax Error](syntax-error) — general parse errors
