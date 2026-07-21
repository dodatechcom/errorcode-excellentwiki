---
title: "[Solution] Bash Globstar Pattern Error"
description: "Fix Bash globstar pattern matching errors when using ** recursive glob patterns."
tools: ["bash"]
error-types: ["tool-error"]
severities: ["warning"]
---

# Bash Globstar Pattern Error

Bash globstar `**` pattern does not match files recursively as expected.

```
No matches found for **/*.log pattern
```

## Common Causes

- globstar not enabled with shopt
- Using ** in single quotes prevents expansion
- Directory contains too many files
- Pattern has trailing space
- Using in POSIX mode

## How to Fix

### Enable globstar

```bash
shopt -s globstar

# Now ** matches recursively
for file in /var/log/**/*.log; do
    echo "$file"
done
```

### Disable globstar for Literal Use

```bash
shopt -u globstar

# ** is now treated as literal asterisks
echo "**"  # outputs: **
```

### Use find as Alternative

```bash
# More portable recursive matching
find /var/log -name "*.log" -type f

# With specific depth
find . -maxdepth 3 -name "*.txt"
```

### Handle No Matches

```bash
shopt -s globstar nullglob

files=(**/*.txt)
if [[ ${#files[@]} -eq 0 ]]; then
    echo "No matching files found"
fi
```

### Exclude Directories

```bash
shopt -s globstar

# Skip .git and node_modules
for file in **/*; do
    [[ "$file" == */.git/* || "$file" == */node_modules/* ]] && continue
    echo "$file"
done
```

## Examples

```bash
#!/bin/bash
shopt -s globstar nullglob

# Find all Python files recursively
for py in **/*.py; do
    echo "Checking: $py"
    python3 -m py_compile "$py" || echo "Syntax error in $py"
done

# Find all large files
for f in **/*; do
    size=$(stat -f%z "$f" 2>/dev/null || stat -c%s "$f" 2>/dev/null)
    (( size > 1048576 )) && echo "Large file: $f ($size bytes)"
done
```
