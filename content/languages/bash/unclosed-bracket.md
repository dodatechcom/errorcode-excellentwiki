---
title: "[Solution] Bash Unclosed Bracket Error"
description: "Fix 'bash: unexpected EOF while looking for matching bracket' caused by unclosed parentheses, braces, or brackets."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "bash"
tags: ["bash", "shell", "syntax", "brackets", "parentheses", "eof", "grouping"]
severity: "error"
---

# Unclosed Bracket

## Error Message

```
bash: unexpected EOF while looking for matching `)'
```

## Common Causes

- A command substitution `$( ... )` is missing the closing `)`
- An arithmetic expansion `$(( ... ))` is missing a closing `))`
- A brace `{` for command grouping or parameter expansion is unclosed
- An array definition or subscript bracket `[` is missing its closer

## Solutions

### Solution 1: Close All Open Brackets

Search backwards from the EOF error line to find the opening bracket that was never closed. Common patterns include `$(`, `((`, `${`, and `{`.

```bash
# Wrong — missing closing )
result=$(echo "test"

# Right
result=$(echo "test")

# Wrong — missing closing ))
total=$(( a + b

# Right
total=$(( a + b ))

# Wrong — unclosed brace group
{
    echo "line 1"
    echo "line 2"

# Right
{
    echo "line 1"
    echo "line 2"
} 
```

### Solution 2: Verify Bracket Matching with a Linter

Use shellcheck or bash -n to quickly identify where the bracket mismatch occurs. Count opening and closing brackets in the file to find discrepancies.

```bash
# Quick syntax check
bash -n script.sh

# Use shellcheck for detailed analysis
shellcheck script.sh

# Count brackets manually
echo "Open parens: $(grep -o '(' script.sh | wc -l)"
echo "Close parens: $(grep -o ')' script.sh | wc -l)"
echo "Open braces: $(grep -o '{' script.sh | wc -l)"
echo "Close braces: $(grep -o '}' script.sh | wc -l)" 
```

## Prevention Tips

- Use `bash -n script.sh` to locate the line with the bracket error
- Enable bracket-matching highlighting in your editor
- Use `shellcheck` for comprehensive syntax analysis

## Related Errors

- [Unmatched Quote]({< relref "/languages/bash/unmatched-quote-EOF" >})
- [Unexpected Token]({< relref "/languages/bash/unexpected-token" >})
