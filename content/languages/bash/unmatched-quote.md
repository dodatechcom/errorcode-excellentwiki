---
title: "[Solution] Bash Unexpected End of File (Unmatched Quote)"
description: "Fix 'unexpected end of file' in Bash caused by unclosed quotes, missing delimiters, or incomplete constructs."
languages: ["bash"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["unexpected-eof", "unmatched-quote", "parse-error"]
weight: 5
---

# Bash Unexpected End of File (Unmatched Quote) Fix

This error occurs when Bash reaches the end of input while still inside an unclosed quote, command substitution, or other delimited construct.

## Description

Bash tracks open quotes, parentheses, braces, and command substitutions. If input ends before these are closed, Bash reports an unexpected end of file. The most common cause is a missing closing quote.

## Common Causes

- **Unclosed double or single quote** — the opening `"` or `'` has no matching closer.
- **Missing closing bracket** — `$(command` without `)`.
- **Incomplete here-document** — missing `EOF` delimiter.
- **Multi-line string without proper continuation** — forgetting the closing delimiter.

## How to Fix

### Fix 1: Find and close unclosed quotes

```bash
# Wrong
msg="Hello world

# Right
msg="Hello world"
```

### Fix 2: Close command substitutions

```bash
# Wrong
result=$(echo "test"

# Right
result=$(echo "test")
```

### Fix 3: Use syntax highlighting to spot mismatches

Most editors highlight matching quotes and brackets. Enable it to visually track unclosed delimiters.

### Fix 4: Verify with a dry parse

```bash
bash -n script.sh
# Reports the line where the unclosed construct started
```

## Examples

```bash
$ echo "hello
bash: unexpected end of file

$ cat <<EOF
This is a heredoc
bash: unexpected end of file

$ x=$(echo test
bash: unexpected end of file
```

## Related Errors

- [Syntax Error Near Unexpected Token](syntax-error) — other parse failures.
- [Here Document Error](here-document) — issues with heredoc delimiters.
