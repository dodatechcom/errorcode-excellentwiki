---
title: "[Solution] Bash Missing Done Error"
description: "Fix 'bash: syntax error near done' caused by missing or unmatched `done` in loop constructs."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "bash"
tags: ["bash", "shell", "syntax", "for-loop", "while-loop", "done-keyword", "unclosed-loop"]
severity: "error"
---

# Missing Done

## Error Message

```
bash: syntax error near `done'
```

## Common Causes

- A `for`, `while`, or `until` loop is missing its closing `done`
- Nested loops where an inner `done` is missing
- The `done` keyword was deleted or commented out by accident
- A `select` statement is missing its closing `done`

## Solutions

### Solution 1: Add the Missing `done` Keyword

Every loop that starts with `do` must end with `done`. Check for accidentally deleted or commented lines.

```bash
# Wrong — missing done
for i in 1 2 3; do
    echo "$i"

# Correct
for i in 1 2 3; do
    echo "$i"
done

# Wrong — missing done in while loop
while read -r line; do
    process_line "$line"
done < input.txt

# Check count of do/done
grep -cw "do" script.sh
grep -cw "done" script.sh 
```

### Solution 2: Fix Nested Loop Structure

When loops are nested, each `do` needs a matching `done`. Make sure you haven't accidentally removed one of the closing keywords.

```bash
# Nested loops — each do has a done
for i in 1 2 3; do
    for j in a b c; do
        echo "$i-$j"
    done
done

# Debug: count do vs done
echo "do count: $(grep -cw 'do' script.sh)"
echo "done count: $(grep -cw 'done' script.sh)" 
```

## Prevention Tips

- Count `do` and `done` keywords — they must be equal
- Use proper indentation to track nested loop boundaries
- Run `bash -n script.sh` to check for unmatched loop keywords

## Related Errors

- [Missing Do]({< relref "/languages/bash/missing-do" >})
- [Missing Fi]({< relref "/languages/bash/missing-fi" >})
