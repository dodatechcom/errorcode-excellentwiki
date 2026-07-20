---
title: "[Solution] Missing `fi` Keyword"
description: "Resolve missing fi error in Bash if/else statements."
tools: ["bash"]
error-types: ["tool-error"]
severities: ["error"]
---

# [Solution] Missing `fi` Keyword

Every `if` statement must be closed with `fi`.

### Common Causes
- Unclosed `if` block.
- Mismatched `if`/`then`/`else`/`fi` structure.
- `fi` misspelled or omitted.

### How to Fix
```bash
# Count if/fi pairs
grep -cE '^\s*if ' script.sh
grep -cE '^\s*fi' script.sh

# Use shellcheck
shellcheck script.sh
```

### Example
```bash
# Broken
if [ "$a" = "1" ]; then
    echo "one"

# Fixed
if [ "$a" = "1" ]; then
    echo "one"
fi
```
