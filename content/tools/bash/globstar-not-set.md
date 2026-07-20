---
title: "[Solution] Globstar Not Set Error"
description: "Fix globstar (**) recursive glob errors in Bash."
tools: ["bash"]
error-types: ["tool-error"]
severities: ["error"]
---

# [Solution] Globstar Not Set Error

The `**` recursive glob requires `shopt -s globstar` to be enabled.

### Common Causes
- `shopt -s globstar` not set.
- Using `**` in a POSIX `sh` shell.
- Bash version < 4.0.

### How to Fix
```bash
# Enable globstar
shopt -s globstar

# Now ** matches all files recursively
for f in **/*.txt; do
    echo "$f"
done

# Alternative: use find
find . -name "*.txt" -type f

# Check status
shopt globstar
```

### Example
```bash
# Broken
for f in **/*.sh; do echo "$f"; done    # no match

# Fixed
shopt -s globstar
for f in **/*.sh; do echo "$f"; done
```
