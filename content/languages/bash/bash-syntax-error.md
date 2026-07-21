---
title: "[Solution] Bash Syntax Error -- Unexpected Token Near Quote"
description: "Fix bash syntax errors when the shell encounters unexpected tokens due to unclosed quotes or misplaced operators."
languages: ["bash"]
error-types: ["syntax-error"]
severities: ["error"]
---

# Bash Syntax Error -- Unexpected Token Near Quote

This error occurs when bash finds an unexpected token, often caused by unclosed quotes or incorrect command syntax.

## Common Causes

- Unclosed single or double quotes in command arguments
- Missing space before or after operators like `||`, `&&`, `;`
- Unescaped special characters in strings
- Missing closing delimiter for subshell or group

## How to Fix

### Close all quotes

```bash
# WRONG: unclosed double quote
echo "hello world

# CORRECT: close the quote
echo "hello world"
```

### Escape special characters

```bash
# WRONG: unescaped semicolon
echo "value: 10;20"

# CORRECT: escape semicolons
echo "value: 10\;20"
```

## Examples

```bash
# Proper quoting with variables
name="Alice"
echo "Hello $name"

# Escaped quotes
echo "He said \"hello\""
```
