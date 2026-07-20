---
title: "[Solution] No Match for Glob Pattern"
description: "Resolve 'no matches found' glob errors in Bash."
tools: ["bash"]
error-types: ["tool-error"]
severities: ["error"]
---

# [Solution] No Match for Glob Pattern

A glob pattern did not match any files and `failglob` is enabled.

### Common Causes
- `shopt -s failglob` is active.
- Files matching the pattern do not exist.
- Directory context changed unexpectedly.

### How to Fix
```bash
# Check if files exist before globbing
shopt -s nullglob
files=(*.txt)
if [[ ${#files[@]} -gt 0 ]]; then
    process "${files[@]}"
fi

# Disable failglob temporarily
shopt -u failglob

# Use find for complex matching
find . -maxdepth 1 -name "*.txt" -print0 | while IFS= read -r -d '' f; do
    echo "$f"
done
```

### Example
```bash
# Broken
shopt -s failglob
echo *.txt    # error if no .txt files

# Fixed
shopt -s nullglob
for f in *.txt; do
    echo "$f"
done
```
