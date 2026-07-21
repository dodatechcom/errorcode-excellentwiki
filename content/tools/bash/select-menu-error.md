---
title: "[Solution] Bash Select Menu Error"
description: "Fix Bash select menu errors when the select construct fails or produces unexpected behavior."
tools: ["bash"]
error-types: ["tool-error"]
severities: ["warning"]
---

# Bash Select Menu Error

Bash select menu does not display correctly or REPLY variable behaves unexpectedly.

```
select: not found
```

## Common Causes

- select not available in POSIX sh mode
- Empty list causes no menu display
- PS3 prompt not set before select
- Menu items contain special characters
- Ctrl+D causes unexpected exit

## How to Fix

### Ensure Bash Mode

```bash
#!/bin/bash
# Not #!/bin/sh

select opt in "Option 1" "Option 2" "Option 3" "Quit"; do
    case $opt in
        "Option 1") echo "Selected 1" ;;
        "Option 2") echo "Selected 2" ;;
        "Option 3") echo "Selected 3" ;;
        "Quit") break ;;
        *) echo "Invalid option" ;;
    esac
done
```

### Set PS3 Prompt

```bash
PS3="Select an option: "
select opt in "Start" "Stop" "Restart" "Quit"; do
    [[ "$opt" == "Quit" ]] && break
    echo "You chose: $opt"
done
```

### Handle Empty Input

```bash
select opt in "Yes" "No" "Cancel"; do
    if [[ -z "$opt" ]]; then
        echo "Invalid selection, try again"
        continue
    fi
    echo "Selected: $opt"
    break
done
```

### Handle Ctrl+D Gracefully

```bash
trap 'echo "Menu cancelled"; exit 0' INT

PS3="Choice: "
select opt in "Build" "Test" "Deploy"; do
    [[ -z "$opt" ]] && continue
    echo "Running: $opt"
done
```

## Examples

```bash
#!/bin/bash
PS3="Pick a fruit: "
options=("Apple" "Banana" "Cherry" "Exit")
select opt in "${options[@]}"; do
    case "$opt" in
        "Exit") echo "Goodbye"; break ;;
        *) echo "You chose $opt" ;;
    esac
done
```
