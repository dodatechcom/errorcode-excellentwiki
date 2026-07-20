---
title: "[Solution] Bash Missing Then Error"
description: "Fix 'bash: syntax error near then' caused by missing or malformed if-then constructs."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "bash"
tags: ["bash", "shell", "syntax", "if-statement", "then-keyword"]
severity: "error"
---

# Missing Then

## Error Message

```
bash: syntax error near `then'
```

## Common Causes

- The `then` keyword is on the same line as `if` but the condition bracket is missing
- The `then` keyword is missing entirely after the condition
- Using `then` without a preceding `if` or `elif`
- The condition uses incorrect bracket syntax (e.g., `[` instead of `[[` for pattern matching)

## Solutions

### Solution 1: Add the `then` Keyword After the Condition

Every `if` statement must be followed by `then` (either on the same line with `;` or on the next line).

```bash
# Wrong — missing then
if [ "$x" -eq 1 ]
echo "x is 1"
fi

# Correct — then on next line
if [ "$x" -eq 1 ]; then
    echo "x is 1"
fi

# Correct — then on same line
if [ "$x" -eq 1 ]; then echo "x is 1"; fi 
```

### Solution 2: Use the Correct Bracket Syntax

Make sure you use matching brackets. Use `[` for POSIX tests or `[[` for Bash-specific tests. Each `[` must have a matching `]`.

```bash
# Wrong — mismatched brackets
if [ "$x" -eq 1
then
    echo "x is 1"
fi

# Correct — proper closing bracket
if [ "$x" -eq 1 ]; then
    echo "x is 1"
fi

# Using double brackets (Bash-specific)
if [[ "$x" -eq 1 ]]; then
    echo "x is 1"
fi 
```

## Prevention Tips

- Always include `then` after every `if` or `elif` condition
- Use `;` to put `then` on the same line as the closing `]`
- Run `bash -n script.sh` to catch missing `then` before execution

## Related Errors

- [Missing Fi]({< relref "/languages/bash/missing-fi" >})
- [Unexpected Token]({< relref "/languages/bash/unexpected-token" >})
