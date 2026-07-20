---
title: "[Solution] Unterminated Quote Error"
description: "Fix unterminated single or double quote errors in Bash."
tools: ["bash"]
error-types: ["tool-error"]
severities: ["error"]
---

# [Solution] Unterminated Quote Error

A quoted string was opened but never closed before the end of the line or file.

### Common Causes
- Missing closing single or double quote.
- Quote spanning multiple lines unintentionally.
- Escaped quotes confusing the parser.

### How to Fix
```bash
# Highlight quotes in editor
grep -n '"' script.sh | head -20
grep -n "'" script.sh | head -20

# Use shellcheck
shellcheck script.sh

# Count quotes (should be even)
grep -o '"' script.sh | wc -l
```

### Example
```bash
# Broken
echo "hello world

# Fixed
echo "hello world"
```
