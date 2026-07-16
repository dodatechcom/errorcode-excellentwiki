---
title: "[Solution] Bash Syntax Error Near Unexpected Token"
description: "Fix 'syntax error near unexpected token' in Bash when parsing fails due to quotes, brackets, or special characters."
languages: ["bash"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["syntax-error", "unexpected-token", "parse-error"]
weight: 5
---

# Bash Syntax Error Near Unexpected Token Fix

This error occurs when Bash encounters a character or token it doesn't expect while parsing a command or script.

## Description

Bash follows strict syntax rules for command structure. When it encounters something out of place — like an unclosed quote, misplaced parenthesis, or unexpected character — it throws a parse error before execution even begins.

## Common Causes

- **Unclosed quotes** — a missing closing `"` or `'` makes Bash think the next token is part of the string.
- **Misplaced parentheses or brackets** — using `(` or `)` in the wrong context.
- **Special characters not escaped** — spaces, semicolons, or other metacharacters used literally without quoting.
- **Windows line endings (CRLF)** — carriage return characters confuse the parser.

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
# Or escape it
echo Hello\;World
```

### Fix 3: Convert Windows line endings

```bash
sed -i 's/\r$//' script.sh
```

### Fix 4: Check parenthesis usage

```bash
# Wrong — Bash thinks this is a subshell
var = (1 2 3)

# Right — use proper array syntax
var=(1 2 3)
```

## Examples

```bash
$ echo "Hello
bash: syntax error near unexpected token `newline'

$ echo Hello )world
bash: syntax error near unexpected token `)'

$ ./script.sh
# script.sh has Windows line endings
bash: ./script.sh: line 1: $'\r': command not found
```

## Related Errors

- [Unmatched Quote](unmatched-quote) — unexpected end of file due to unclosed quotes.
- [Here Document Error](here-document) — syntax issues with heredoc syntax.
