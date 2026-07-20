---
title: "[Solution] Bash Unmatched Quote Error"
description: "Fix 'bash: unexpected EOF while looking for matching quote' caused by unclosed string literals."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "bash"
tags: ["bash", "shell", "syntax", "quoting", "eof", "string-literal"]
severity: "error"
---

# Unmatched Quote

## Error Message

```
bash: unexpected EOF while looking for matching `"'
```

## Common Causes

- A double quote `"` was opened but never closed before the end of the file
- A single quote `'` was opened but never closed
- A multi-line string is missing its closing delimiter
- An escaped quote inside a string broke the quoting context

## Solutions

### Solution 1: Find and Close the Unclosed Quote

Search through the file for unmatched quotes. Use `bash -n` to identify the line where parsing fails, then look backwards for the unclosed opening quote.

```bash
# Wrong — missing closing quote
echo "This is a test
echo "Another line"

# Right
echo "This is a test"
echo "Another line"

# Find the problematic line
bash -n script.sh 2>&1 
```

### Solution 2: Escape Quotes Inside Strings

If you need a literal quote character inside a quoted string, escape it with a backslash. Alternatively, use single quotes for strings that contain double quotes.

```bash
# Wrong — unescaped quote breaks the string
echo "He said "hello" to me"

# Correct — escaped inner quotes
echo "He said \"hello\" to me"

# Correct — use single quotes for strings with double quotes
echo 'He said "hello" to me'

# Correct — mix quote types
echo "He said 'hello' to me" 
```

## Prevention Tips

- Use `bash -n script.sh` to detect unmatched quotes before running
- Most editors highlight matching quotes — enable this feature
- Use single quotes when the string contains double quotes and vice versa

## Related Errors

- [Unclosed Bracket]({< relref "/languages/bash/unclosed-bracket" >})
- [Unmatched Quote]({< relref "/languages/bash/unmatched-quote" >})
