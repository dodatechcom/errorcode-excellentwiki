---
title: "[Solution] Bash Globstar Error -- Recursive Directory Traversal"
description: "Fix bash globstar errors when using ** for recursive globbing with incorrect settings."
languages: ["bash"]
error-types: ["runtime-error"]
severities: ["error"]
---

# Bash Globstar Error

This error occurs when the `**` globstar pattern is used without enabling the `globstar` shell option.

## Common Causes

- `globstar` not enabled with `shopt -s globstar`
- Using `**` in non-recursive context
- Performance issues with very deep directory trees
- Including ignored directories unintentionally

## How to Fix

### Enable globstar

```bash
# WRONG: ** treated as two * patterns
for f in **/*.txt; do
    echo "$f"
done

# CORRECT: enable globstar
shopt -s globstar
for f in **/*.txt; do
    echo "$f"
done
```

### Use find for complex patterns

```bash
# Alternative: use find
find . -name "*.txt" -type f
```

## Examples

```bash
#!/bin/bash
shopt -s globstar nullglob

for file in src/**/*.ts; do
    echo "Compiling: $file"
done
```
