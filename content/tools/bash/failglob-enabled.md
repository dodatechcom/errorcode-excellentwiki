---
title: "[Solution] Failglob Enabled Error"
description: "Resolve errors caused by failglob being enabled in Bash."
tools: ["bash"]
error-types: ["tool-error"]
severities: ["error"]
---

# [Solution] Failglob Enabled Error

With `shopt -s failglob`, an unmatched glob causes a shell error.

### Common Causes
- `failglob` enabled in scripts where no-match is expected.
- Globbing in a directory without matching files.

### How to Fix
```bash
# Disable failglob
shopt -u failglob

# Or handle the case explicitly
shopt -s failglob
if ! echo *.txt >/dev/null 2>&1; then
    echo "No files matched"
fi

# Check current setting
shopt failglob
```

### Example
```bash
# Broken
shopt -s failglob
echo *.nonexistent    # error

# Fixed
shopt -u failglob
echo *.nonexistent    # prints literal "*.nonexistent"
```
