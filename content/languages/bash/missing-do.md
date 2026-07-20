---
title: "[Solution] Bash Missing Do Error"
description: "Fix 'bash: syntax error near do' caused by missing `do` keyword in loop constructs."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "bash"
tags: ["bash", "shell", "syntax", "for-loop", "while-loop", "do-keyword"]
severity: "error"
---

# Missing Do

## Error Message

```
bash: syntax error near `do'
```

## Common Causes

- The `do` keyword is missing after `for`, `while`, or `until`
- Using a semicolon on the `for` line without including `do`
- Incorrectly structured loop syntax

## Solutions

### Solution 1: Add `do` After the Loop Header

Every `for`, `while`, or `until` loop must have a `do` keyword to mark the start of the loop body.

```bash
# Wrong — missing do
for i in 1 2 3
    echo "$i"
done

# Correct — do on next line
for i in 1 2 3; do
    echo "$i"
done

# Wrong — missing do in while loop
while read -r line
    echo "$line"
done < file.txt

# Correct
while read -r line; do
    echo "$line"
done < file.txt 
```

### Solution 2: Use One-liner Loop Syntax

For compact loops, place `; do` on the same line as the loop header. Make sure both `do` and `done` are present.

```bash
# Compact for loop
for f in *.txt; do
    echo "Processing $f"
done

# Compact while loop
count=0
while [ $count -lt 5 ]; do
    echo "$count"
    ((count++))
done

# Compact until loop
until ping -c 1 google.com &> /dev/null; do
    echo "Waiting..."
    sleep 1
done 
```

## Prevention Tips

- Remember: `do` starts the loop body, `done` ends it
- Use `bash -n script.sh` to verify loop syntax before running
- Place `; do` on the same line as the loop header for cleaner code

## Related Errors

- [Missing Done]({< relref "/languages/bash/missing-done" >})
- [Missing Then]({< relref "/languages/bash/missing-then" >})
