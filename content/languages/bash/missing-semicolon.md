---
title: "[Solution] Bash Missing Semicolon Error"
description: "Fix 'bash: command not found' caused by missing semicolons between statements on the same line."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "bash"
tags: ["bash", "shell", "syntax", "semicolons", "command-separator"]
severity: "error"
---

# Missing Semicolon

## Error Message

```
bash: command not found: ;
```

## Common Causes

- Multiple commands are placed on the same line without semicolons
- A semicolon is used in the wrong position, causing Bash to interpret it as a command name
- Using a semicolon inside a quoted string where it's treated as a literal character
- Missing semicolons before `then`, `do`, or after closing brackets on one-liners

## Solutions

### Solution 1: Use Semicolons as Command Separators

When placing multiple commands on one line, separate each command with a semicolon. The semicolon acts as a command terminator.

```bash
# Wrong — Bash tries to run "echo; echo" as one command
echo "first" echo "second"

# Right — semicolon separates commands
echo "first"; echo "second"

# Multiple commands on one line
echo "Start"; date; echo "End"

# Semicolon before then/do in one-liners
if [ -f file.txt ]; then echo "exists"; fi
for i in 1 2 3; do echo "$i"; done 
```

### Solution 2: Use Newlines Instead of Semicolons

For readability, put each command on its own line. This avoids semicolon issues entirely and makes scripts easier to maintain.

```bash
# Instead of cramming everything on one line
echo "first"; echo "second"; echo "third"

# Write each command on its own line
echo "first"
echo "second"
echo "third"

# Each command on its own line is clearer and less error-prone
if [ -f config.txt ]; then
    echo "Config found"
    source config.txt
fi 
```

## Prevention Tips

- Prefer one command per line for cleaner, more readable scripts
- Use `;` to separate commands on the same line when needed
- Remember: `;` is not needed after the last command on a line

## Related Errors

- [Missing Pipe]({< relref "/languages/bash/missing-pipe" >})
- [Unexpected Token]({< relref "/languages/bash/unexpected-token" >})
