---
title: "[Solution] Nullglob Configuration Error"
description: "Fix nullglob behavior when no files match a glob pattern."
tools: ["bash"]
error-types: ["tool-error"]
severities: ["error"]
---

# [Solution] Nullglob Configuration Error

With `nullglob` enabled, an unmatched glob expands to nothing instead of the literal pattern.

### Common Causes
- `nullglob` not set when relying on empty expansion.
- Script behavior differs between environments.

### How to Fix
```bash
# Enable nullglob for safe glob handling
shopt -s nullglob
files=(*.txt)
if [[ ${#files[@]} -eq 0 ]]; then
    echo "No .txt files found"
fi

# Use nullglob in loops
shopt -s nullglob
for f in *.log; do
    process "$f"
done

# Disable if you want literal pattern
shopt -u nullglob
```

### Example
```bash
# Broken (no nullglob)
echo *.txt    # prints "*.txt" even if no match

# Fixed
shopt -s nullglob
for f in *.txt; do
    echo "$f"
done
```
