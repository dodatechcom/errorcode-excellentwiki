---
title: "[Solution] Bash Arithmetic Incr Decr Error -- Increment Decrement Issues"
description: "Fix bash arithmetic increment/decrement errors when using ++ and -- operators."
languages: ["bash"]
error-types: ["syntax-error"]
severities: ["error"]
---

# Bash Arithmetic Incr Decr Error

This error occurs when increment `++` and decrement `--` operators are used incorrectly in bash arithmetic.

## Common Causes

- Using `++` outside of `$(( ))` or `(( ))` context
- Forgetting that `i++` in `$(( ))` returns old value
- Using pre-increment where post-increment is needed
- Not using `(( ))` for side-effect only increments

## How to Fix

### Use correct increment syntax

```bash
# WRONG: ++ outside arithmetic context
i++
echo $i

# CORRECT: use (( )) for side effects
((i++))
echo "$i"

# Or use arithmetic expansion
i=$((i + 1))
```

### Understand pre vs post increment

```bash
i=5
echo $((i++))  # prints 5, then i becomes 6
echo $((++i))  # prints 7, then i becomes 7
```

## Examples

```bash
#!/bin/bash
count=0
while [ $count -lt 10 ]; do
    ((count++))
    echo "$count"
done
```
