---
title: "[Solution] Bash Subshell Error -- Variable Scope in Parentheses"
description: "Fix bash subshell errors when variables set inside subshells are not visible in the parent shell."
languages: ["bash"]
error-types: ["runtime-error"]
severities: ["error"]
---

# Bash Subshell Error

This error occurs when variables or changes made inside a subshell (created by `()`, pipes, or command substitution) are not visible in the parent shell.

## Common Causes

- Variables set inside `()` lost when subshell exits
- Piped commands create subshells
- Command substitution `$()` creates subshell
- Expecting loop variable to persist after pipe

## How to Fix

### Use process substitution or temp files

```bash
# WRONG: variable lost in pipe subshell
echo "hello" | while read line; do
    result="$line"  # lost after pipe ends
done
echo "$result"  # empty

# CORRECT: use process substitution
while read line; do
    result="$line"
done < <(echo "hello")
echo "$result"  # "hello"
```

### Use temp files for cross-subshell data

```bash
temp=$(mktemp)
echo "data" > "$temp"
# subshell writes to temp
(cat "$temp" | process) 
# read result back
result=$(cat "$temp")
rm "$temp"
```

## Examples

```bash
#!/bin/bash
count=0
while read line; do
    ((count++))
done < <(grep "pattern" file.txt)
echo "Found $count matches"
```
