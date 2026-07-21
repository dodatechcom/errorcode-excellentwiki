---
title: "[Solution] Bash Shellcheck Warning Error"
description: "Fix Bash shellcheck warnings and errors when scripts fail static analysis checks."
tools: ["bash"]
error-types: ["tool-error"]
severities: ["warning"]
---

# Bash Shellcheck Warning Error

Bash shellcheck reports warnings or errors that indicate potential script problems.

```
SC2086: Double quote to prevent globbing and word splitting
SC2046: Quote this to prevent word splitting
```

## Common Causes

- Unquoted variables in command arguments
- Missing double quotes around $()
- Arithmetic context using $(( )) incorrectly
- Unused variables or assignments
- Deprecated syntax like backticks

## How to Fix

### Quote All Variables

```bash
# Wrong
rm $file
cp $src $dest

# Correct
rm "$file"
cp "$src" "$dest"
```

### Quote Command Substitution

```bash
# Wrong
files=$(ls)
echo $files

# Correct
files=$(ls)
echo "$files"

# Or use array for multiple files
files=(*.txt)
echo "${files[@]}"
```

### Use Modern Syntax

```bash
# Wrong - backticks
result=`command`

# Correct - dollar parentheses
result=$(command)
```

### Add Shellcheck Directive

```bash
#!/bin/bash
# shellcheck disable=SC2086
# Intentional word splitting for this command
echo $unquoted_var | tr ' ' '\n'
```

### Fix Common Patterns

```bash
# SC2046: Quote command substitution
cd $(dirname "$0")  # Wrong
cd "$(dirname "$0")"  # Correct

# SC2034: Variable assigned but not used
# Remove unused variables

# SC2154: Variable referenced but not assigned
# Ensure variables are set or use default
echo "${MY_VAR:-default}"
```

## Examples

```bash
# Clean shellcheck-compliant script
#!/bin/bash
set -euo pipefail

process_files() {
    local dir="${1:-.}"
    local count=0

    while IFS= read -r -d '' file; do
        echo "Processing: $file"
        ((count++))
    done < <(find "$dir" -type f -print0)

    echo "Processed $count files"
}

process_files "/var/log"
```
