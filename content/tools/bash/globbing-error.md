---
title: "[Solution] Bash Globbing Error"
description: "Fix Bash globbing errors when filename pattern expansion produces unexpected matches."
tools: ["bash"]
error-types: ["tool-error"]
severities: ["warning"]
---

# Bash Globbing Error

Bash filename globbing produces unexpected results or fails silently.

```
ls: cannot access *.txt: No such file or directory
```

## Common Causes

- nofail or failglob set differently than expected
- Pattern does not match any files
- Files have spaces or special characters
- noclobber option prevents overwriting
- Hidden files excluded by default

## How to Fix

### Handle No Matches

```bash
# Disable error on no match
shopt -u failglob

# Or handle explicitly
shopt -s nullglob
files=(*.txt)
if [[ ${#files[@]} -eq 0 ]]; then
    echo "No .txt files found"
fi
```

### Expand Hidden Files

```bash
# By default hidden files are not matched
ls *  # Does not show .hidden files

# Include hidden files
shopt -s dotglob
ls *
shopt -u dotglob
```

### Handle Spaces in Filenames

```bash
# Wrong - word splitting
for f in *.txt; do
    rm $f  # Breaks on spaces
done

# Correct - quote everything
for f in *.txt; do
    rm "$f"
done
```

### Disable Globbing Temporarily

```bash
# Use set -f to disable globbing
set -f
echo "*.txt"  # Literal string
set +f
```

### Use extglob for Advanced Patterns

```bash
shopt -s extglob

# Match files NOT matching pattern
rm !(*.bak).txt

# Match files matching multiple patterns
ls *.(jpg|png|gif)
```

## Examples

```bash
#!/bin/bash
# Safe globbing patterns
shopt -s nullglob

# Find and process files
for file in /var/log/*.log; do
    echo "Processing: $file"
    gzip "$file"
done

# Recursive glob with globstar
shopt -s globstar
find_count=0
for py in **/*.py; do
    ((find_count++))
done
echo "Found $find_count Python files"
```
