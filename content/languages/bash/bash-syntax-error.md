---
title: "[Solution] Bash Syntax Error Near Unexpected Token"
description: "Fix 'syntax error near unexpected token' in Bash when parsing fails due to quotes, brackets, or special characters."
languages: ["bash"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["syntax-error", "unexpected-token", "parse-error"]
weight: 5
---

# Bash Syntax Error Near Unexpected Token

This error occurs when Bash encounters a character or token it doesn't expect while parsing a command or script.

## What This Error Means

Bash follows strict syntax rules for command structure. When it encounters something out of place, it throws a parse error before execution begins.

## Common Causes

- Unclosed quotes
- Misplaced parentheses or brackets
- Special characters not escaped
- Windows line endings (CRLF)

## How to Fix

### Fix 1: Check and close all quotes

```bash
# Wrong
echo "Hello world

# Right
echo "Hello world"
```

### Fix 2: Escape special characters

```bash
# Wrong
echo Hello;World

# Right
echo "Hello;World"
echo Hello\;World
```

### Fix 3: Convert Windows line endings

```bash
sed -i 's/\r$//' script.sh
```

### Fix 4: Check parenthesis usage

```bash
# Wrong
var = (1 2 3)

# Right
var=(1 2 3)
```

## Examples

```bash
$ echo "Hello
bash: syntax error near unexpected token `newline'

$ echo Hello )world
bash: syntax error near unexpected token `)'
```

## Related Errors

- [Unmatched Quote](unmatched-quote) - unexpected end of file due to unclosed quotes
- [Here Document Error](here-document) - syntax issues with heredoc syntax
