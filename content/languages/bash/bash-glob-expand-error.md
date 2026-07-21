---
title: "[Solution] Bash Glob Expand Error -- Incorrect Filename Expansion"
description: "Fix bash glob expansion errors when wildcard patterns expand unexpectedly or fail."
languages: ["bash"]
error-types: ["runtime-error"]
severities: ["error"]
---

# Bash Glob Expand Error

This error occurs when glob patterns (`*`, `?`, `[...]`) expand incorrectly or cause errors due to unexpected matches.

## Common Causes

- Unquoted globs expanding to unexpected files
- Glob matching dotfiles by default (or not matching them)
- Empty directory causing glob to remain unexpanded
- Using globs in wrong context (e.g., inside [[ ]])

## How to Fix

### Quote globs when literal expansion is needed

```bash
# WRONG: glob expands unexpectedly
echo "*.txt"  # prints all .txt files instead of literal "*.txt"

# CORRECT: quote to prevent expansion
echo "*.txt"
```

### Use nullglob for empty matches

```bash
shopt -s nullglob
for f in *.txt; do
    echo "$f"
done
# Nothing happens if no .txt files exist
```

## Examples

```bash
#!/bin/bash
# Find files safely
shopt -s nullglob dotglob
files=(*.log)
if [ ${#files[@]} -eq 0 ]; then
    echo "No log files found"
else
    echo "Found ${#files[@]} log files"
fi
```
