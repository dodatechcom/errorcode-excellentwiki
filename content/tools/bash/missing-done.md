---
title: "[Solution] Missing `done` Keyword"
description: "Bash script error: missing done keyword for loop."
tools: ["bash"]
error-types: ["tool-error"]
severities: ["error"]
---

# [Solution] Missing `done` Keyword

Every `for`, `while`, `until`, or `select` loop must end with `done`.

### Common Causes
- Typo in `done` (e.g., `don`).
- `done` placed inside a subshell accidentally.
- Early `return` or `exit` skipping the `done`.

### How to Fix
```bash
# Validate loop structure
grep -c 'do$' script.sh   # should match loop count
grep -c '^done' script.sh  # should match loop count

# Use indent-based linting
shellcheck script.sh
```

### Example
```bash
# Broken
for f in *.txt; do
    cat "$f"

# Fixed
for f in *.txt; do
    cat "$f"
done
```
