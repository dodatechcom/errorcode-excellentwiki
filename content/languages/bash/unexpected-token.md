---
title: "[Solution] Bash Unexpected Token Error"
description: "Fix 'bash: syntax error near unexpected token' caused by misplaced characters, missing operators, or malformed expressions."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "bash"
tags: ["bash", "shell", "syntax", "parse-error", "tokens"]
severity: "error"
---

# Unexpected Token

## Error Message

```
bash: syntax error near unexpected token `;'
```

## Common Causes

- Missing space around operators like `;`, `|`, `&`, or `&&`
- Placing a semicolon or pipe where Bash expects a command
- Using Windows-style line endings (CRLF) that inject invisible carriage returns
- Mixing arithmetic and string contexts without proper quoting

## Solutions

### Solution 1: Add Spaces Around Operators

Bash requires spaces around semicolons, pipes, and logical operators. Without them, the shell tries to interpret the token as part of the previous or next word.

```bash
# Wrong — no space before semicolon
echo "hello";;echo "world"

# Correct — proper spacing
echo "hello"; echo "world"

# Wrong — no space around pipe
echo "hello"|grep "hell"

# Correct
echo "hello" | grep "hell" 
```

### Solution 2: Convert CRLF Line Endings

Files created on Windows may have carriage-return characters at the end of each line. These invisible characters cause unexpected token errors. Use dos2unix or sed to fix them.

```bash
# Check for CRLF
cat -A script.sh | grep '\^M'

# Fix with dos2unix
dos2unix script.sh

# Or fix with sed
sed -i 's/\r$//' script.sh

# Or fix with tr
tr -d '\r' < script.sh > script_fixed.sh
```

## Prevention Tips

- Always use spaces around operators: `;`, `|`, `&&`, `||`
- Run `bash -n script.sh` to check syntax without executing
- Use an editor with syntax highlighting to catch token issues visually

## Related Errors

- [Missing Semicolon]({< relref "/languages/bash/missing-semicolon" >})
- [Unmatched Quote]({< relref "/languages/bash/unmatched-quote" >})
