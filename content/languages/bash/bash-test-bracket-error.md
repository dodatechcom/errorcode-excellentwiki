---
title: "[Solution] Bash Test Bracket Error -- Incorrect Conditional Syntax"
description: "Fix bash test bracket errors when using [ ] or [[ ]] with incorrect syntax."
languages: ["bash"]
error-types: ["syntax-error"]
severities: ["error"]
---

# Bash Test Bracket Error

This error occurs when bash test expressions `[ ]` or `[[ ]]` are written with incorrect syntax.

## Common Causes

- Missing spaces around brackets: `[ "$a"="$b" ]` vs `[ "$a" = "$b" ]`
- Using `==` inside `[ ]` (only `[[ ]]` supports it)
- Unquoted variables causing word splitting
- Using `(` instead of `(` in test expressions

## How to Fix

### Use correct bracket syntax

```bash
# WRONG: missing spaces
[ "$a"="$b" ]  # error: unrecognized operator

# CORRECT: proper spacing
[ "$a" = "$b" ]

# Or use [[ ]] for modern bash
[[ "$a" == "$b" ]]
```

### Quote variables in test

```bash
# WRONG: unquoted variable
[ $name = "Alice" ]  # fails if $name is empty

# CORRECT: quote everything
[ "$name" = "Alice" ]
```

## Examples

```bash
#!/bin/bash
name="Alice"
age=30

if [[ "$name" == "Alice" ]]; then
    echo "Hello Alice"
fi

if [ "$age" -gt 18 ]; then
    echo "Adult"
fi
```
