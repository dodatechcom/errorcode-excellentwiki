---
title: "[Solution] Bash Infinite Loop Error -- Never-Terminating While/For Loop"
description: "Fix bash infinite loop errors when while or for loops never terminate due to incorrect exit conditions."
languages: ["bash"]
error-types: ["runtime-error"]
severities: ["error"]
---

# Bash Infinite Loop Error

This error occurs when a loop's exit condition is never met, causing the script to run indefinitely.

## Common Causes

- Counter variable not incremented inside loop
- Exit condition always evaluates to true
- Missing break statement in infinite loop
- Loop variable not updated in while loop

## How to Fix

### Ensure loop variable is updated

```bash
# WRONG: counter never incremented
count=0
while [ $count -lt 5 ]; do
    echo "$count"
done

# CORRECT: increment counter
count=0
while [ $count -lt 5 ]; do
    echo "$count"
    ((count++))
done
```

### Use for loops with known ranges

```bash
# Preferred: explicit range
for i in {1..5}; do
    echo "$i"
done
```

## Examples

```bash
# Safe infinite loop with break
while true; do
    read -p "Continue? (y/n) " answer
    [ "$answer" = "y" ] || break
    echo "Continuing..."
done
```
