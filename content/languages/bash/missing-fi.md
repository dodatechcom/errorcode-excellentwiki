---
title: "[Solution] Bash Missing Fi Error"
description: "Fix 'bash: syntax error near fi' caused by missing or unmatched `fi` closing an if-statement."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "bash"
tags: ["bash", "shell", "syntax", "if-statement", "fi-keyword", "unclosed-block"]
severity: "error"
---

# Missing Fi

## Error Message

```
bash: syntax error near `fi'
```

## Common Causes

- An `if` statement is missing its closing `fi`
- An `elif` or `else` block is not properly terminated with `fi`
- Nested if statements where an inner `fi` is missing
- Accidentally deleting or commenting out the `fi` line

## Solutions

### Solution 1: Add the Missing `fi` Keyword

Every `if` block must end with `fi`. If you have nested if statements, each one needs its own closing `fi`.

```bash
# Wrong — missing fi
if [ "$x" -gt 0 ]; then
    echo "Positive"
elif [ "$x" -lt 0 ]; then
    echo "Negative"
else
    echo "Zero"

# Correct
if [ "$x" -gt 0 ]; then
    echo "Positive"
elif [ "$x" -lt 0 ]; then
    echo "Negative"
else
    echo "Zero"
fi 
```

### Solution 2: Match Nested if-fi Pairs

When nesting if statements, ensure each `if` has a corresponding `fi`. Use indentation to keep the structure clear.

```bash
# Nested if — both fi present
if [ -f "$file" ]; then
    if grep -q "error" "$file"; then
        echo "Found errors in $file"
    fi
fi

# Check with bash -n to verify structure
bash -n nested_script.sh && echo "Syntax OK" 
```

## Prevention Tips

- Count your `if` and `fi` keywords — they must match 1:1
- Use consistent indentation to visually match if/fi pairs
- Run `bash -n script.sh` to detect missing `fi` before execution

## Related Errors

- [Missing Then]({< relref "/languages/bash/missing-then" >})
- [Missing Done]({< relref "/languages/bash/missing-done" >})
