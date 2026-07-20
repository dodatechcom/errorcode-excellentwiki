---
title: "[Solution] Glob Pattern Too Large"
description: "Fix 'argument list too long' from large glob expansions."
tools: ["bash"]
error-types: ["tool-error"]
severities: ["error"]
---

# [Solution] Glob Pattern Too Large

The glob pattern expands to more files than the argument list limit allows.

### Common Causes
- Too many files matching the pattern.
- Deep directory recursion.
- No `nullglob` or batching.

### How to Fix
```bash
# Use find + xargs instead of direct glob
find . -name "*.txt" -print0 | xargs -0 -n 100 process

# Batch processing with while loop
find . -name "*.log" -print0 | while IFS= read -r -d '' f; do
    process "$f"
done

# Limit glob with extglob
shopt -s extglob
rm -f !(keep_me|and_this).txt
```

### Example
```bash
# Broken
rm *.tmp    # if millions of .tmp files

# Fixed
find . -name "*.tmp" -print0 | xargs -0 rm
```
