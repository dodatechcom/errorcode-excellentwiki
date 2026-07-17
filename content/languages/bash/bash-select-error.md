---
title: "[Solution] Bash Select Syntax Error"
description: "Fix 'select syntax error' in Bash when the select loop has incorrect syntax or is used in a non-interactive shell."
languages: ["bash"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["select", "menu", "interactive", "loop", "ps3"]
weight: 5
---

# Bash Select Syntax Error Fix

Select syntax errors occur when the `select` loop has incorrect syntax, is used non-interactively, or has mismatched `do`/`done` blocks.

## What This Error Means

The `select` statement creates a numbered menu from a list and reads user input. It requires an interactive shell or proper stdin redirection. Errors indicate syntax problems or non-interactive usage.

## Common Causes

- Used in non-interactive shell (piped or redirected input)
- Missing `in` keyword
- Missing `do`/`done` block
- PS3 prompt not set
- Missing `esac` or `done`

## How to Fix

### 1. Ensure correct syntax

```bash
# RIGHT:
PS3="Select option: "
select opt in "Start" "Stop" "Quit"; do
    case $opt in
        Start) echo "Starting" ;;
        Stop) echo "Stopping" ;;
        Quit) break ;;
        *) echo "Invalid option" ;;
    esac
done
```

### 2. Set PS3 before select

```bash
PS3="Choose: "  # Must be set before select
select item in apple banana cherry; do
    echo "You chose: $item"
    break
done
```

### 3. Use with proper shell

```bash
#!/bin/bash  # select is a bash feature, not sh
PS3="Pick one: "
select choice in A B C; do
    echo "$choice"
    break
done
```

## Related Errors

- [Case Error](bash-case-error) — case statement syntax
- [While Error](bash-while-error) — loop syntax issues
