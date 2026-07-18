---
title: "[Solution] Bash Case Statement Syntax Error Near Token Fix"
description: "Fix 'case: syntax error near unexpected token' in Bash. Correct case statement pattern matching syntax errors."
languages: ["bash"]
error-types: ["syntax-error"]
severities: ["error"]
weight: 5
---

# Bash Case Statement Syntax Error Near Token Fix

The `case: syntax error near unexpected token` error occurs when a `case` statement has incorrect pattern syntax, missing `esac`, or malformed case arms.

## What This Error Means

The `case` statement in Bash is used for pattern matching. It requires a specific structure: `case` followed by the variable, `in`, pattern arms separated by `;;`, and closed with `esac`. Syntax errors prevent the script from parsing.

A typical error:

```
script.sh: line 5: syntax error near unexpected token `esac'
```

## Why It Happens

Common causes include:

- **Missing `esac`** — The case statement is never closed.
- **Missing `;;`** — Pattern arms are not properly terminated.
- **Wrong pattern syntax** — Using invalid glob patterns or missing `|` for alternatives.
- **Missing `in` keyword** — Writing `case $var` instead of `case $var in`.
- **Unclosed parentheses in patterns** — Pattern `foo(|bar)` is invalid.
- **Missing closing `esac`** — The most common cause of parse errors.

## How to Fix It

### Fix 1: Complete case statement structure

```bash
# WRONG: Missing esac
case "$choice" in
    start) echo "Starting" ;;
    stop) echo "Stopping" ;;

# RIGHT: Always close with esac
case "$choice" in
    start) echo "Starting" ;;
    stop) echo "Stopping" ;;
esac
```

### Fix 2: Terminate each pattern with ;;

```bash
# WRONG: Missing ;;
case "$choice" in
    start) echo "Starting"
    stop) echo "Stopping"

# RIGHT: Each arm ends with ;;
case "$choice" in
    start) echo "Starting" ;;
    stop) echo "Stopping" ;;
esac
```

### Fix 3: Use proper pattern syntax

```bash
# RIGHT: Multiple patterns with |
case "$file" in
    *.tar.gz|*.tgz) echo "tarball" ;;
    *.zip) echo "archive" ;;
    *.jpg|*.png|*.gif) echo "image" ;;
    *) echo "unknown" ;;
esac
```

### Fix 4: Handle empty or special characters

```bash
# RIGHT: Quote the variable
case "${choice:-default}" in
    yes) echo "Affirmative" ;;
    no) echo "Negative" ;;
    *) echo "Invalid" ;;
esac
```

### Fix 5: Nested case statements

```bash
# RIGHT: Nested case with proper closing
case "$os" in
    linux)
        case "$distro" in
            ubuntu) echo "Ubuntu Linux" ;;
            centos) echo "CentOS Linux" ;;
            *) echo "Other Linux" ;;
        esac
        ;;
    darwin) echo "macOS" ;;
    *) echo "Unknown OS" ;;
esac
```

## Common Mistakes

- **Forgetting `esac`** — Every `case` must end with `esac` (case spelled backwards).
- **Using `;;` at the end of the last arm before `esac`** — This is correct and required.
- **Not quoting `$variable`** — Word splitting can cause unexpected pattern matches.

## Related Pages

- [Bash For Syntax Error](bash-for-syntax-error) — For loop syntax issues
- [Bash While Syntax Error](bash-while-syntax-error) — While loop syntax errors
- [Bash Bad Substitution](bad-substitution) — Variable expansion issues
