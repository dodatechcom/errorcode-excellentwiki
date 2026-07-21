---
title: "[Solution] Bash Glob Ignore Error -- Incorrect Filename Filtering"
description: "Fix bash glob ignore errors when using GLOBIGNORE or dotglob options incorrectly."
languages: ["bash"]
error-types: ["runtime-error"]
severities: ["error"]
---

# Bash Glob Ignore Error

This error occurs when glob ignore options like `GLOBIGNORE` or `dotglob` cause unexpected file matching.

## Common Causes

- `dotglob` matching hidden files unintentionally
- `GLOBIGNORE` patterns not working as expected
- Pattern syntax incorrect for ignore list
- Glob behavior changing between bash versions

## How to Fix

### Set glob options carefully

```bash
# WRONG: dotglob matches hidden files
shopt -s dotglob
for f in *; do
    echo "$f"  # includes .bashrc etc
done

# CORRECT: check for hidden files
for f in *; do
    [[ "$f" == .* ]] && continue
    echo "$f"
done
```

### Use GLOBIGNORE correctly

```bash
# Ignore specific patterns
GLOBIGNORE="*.log:*.tmp"
for f in *; do
    echo "$f"
done
```

## Examples

```bash
#!/bin/bash
shopt -s nullglob
files=(*.txt)
echo "Found ${#files[@]} text files"
```
