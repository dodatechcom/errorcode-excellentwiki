---
title: "[Solution] Bash While Loop Error"
description: "Fix while loop errors in Bash when loops don't terminate, have syntax errors, or pipe/subshell issues cause variable loss."
languages: ["bash"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["while", "loop", "infinite", "read", "pipe"]
weight: 5
---

# Bash While Loop Error Fix

While loop errors include infinite loops, syntax errors in the condition, variables losing values after the loop (subshell issue), or `read` not working as expected.

## What This Error Means

The `while` loop executes a block as long as a condition is true. Common pitfalls include pipes creating subshells that lose variable changes, and conditions that never become false.

## Common Causes

- Pipe before while creates a subshell (variables lost)
- Condition always true (infinite loop)
- Missing `do`/`done` keywords
- `read` at end of file doesn't return false
- Comparison using `=` instead of `==` or `-eq`

## How to Fix

### 1. Use process substitution to avoid subshell

```bash
# WRONG: pipe creates subshell, count is lost
count=0
cat file.txt | while read line; do
    count=$((count + 1))
done
echo "Lines: $count"  # Shows 0

# RIGHT: process substitution or redirect
count=0
while read line; do
    count=$((count + 1))
done < file.txt
echo "Lines: $count"  # Shows correct count
```

### 2. Prevent infinite loops

```bash
# WRONG: condition never changes
while [ $i -lt 10 ]; do
    echo $i
    # Missing: i=$((i + 1))
done

# RIGHT:
i=0
while [ $i -lt 10 ]; do
    echo $i
    i=$((i + 1))
done
```

### 3. Check for end-of-file properly

```bash
# While read returns true even at EOF sometimes
while read line; do
    echo "$line"
done < file.txt
```

### 4. Fix comparison operators

```bash
# WRONG: string comparison for numbers
while [ $count = 10 ]

# RIGHT: numeric comparison
while [ $count -eq 10 ]
# Or with [[ ]] in bash
while [[ $count -eq 10 ]]
```

## Related Errors

- [For Loop Error](bash-for-error) — for loop issues
- [Pipe Error](bash-pipe-error) — pipe-related problems
