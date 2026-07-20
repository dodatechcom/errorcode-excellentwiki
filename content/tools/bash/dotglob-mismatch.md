---
title: "[Solution] Dotglob Globbing Mismatch"
description: "Fix dotglob behavior when globbing hidden files in Bash."
tools: ["bash"]
error-types: ["tool-error"]
severities: ["error"]
---

# [Solution] Dotglob Globbing Mismatch

With `dotglob`, the `*` pattern matches files starting with `.` which may cause unexpected behavior.

### Common Causes
- `shopt -s dotglob` causes `.` and `..` to be included.
- Scripts relying on default behavior break when dotglob is enabled.

### How to Fix
```bash
# Enable dotglob to match hidden files
shopt -s dotglob
for f in *; do
    [[ "$f" == "." || "$f" == ".." ]] && continue
    echo "$f"
done

# Disable if you want default behavior
shopt -u dotglob

# Check setting
shopt dotglob
```

### Example
```bash
# Broken (dotglob enabled, includes . and ..)
shopt -s dotglob
rm *    # tries to remove . and ..

# Fixed
shopt -s dotglob
for f in *; do
    [[ "$f" == "." || "$f" == ".." ]] && continue
    rm "$f"
done
```
