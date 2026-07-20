---
title: "[Solution] Syntax Error Near Unexpected Token"
description: "Fix 'syntax error near unexpected token' in Bash scripts."
tools: ["bash"]
error-types: ["tool-error"]
severities: ["error"]
---

# [Solution] Syntax Error Near Unexpected Token

Bash encounters a token it does not expect at the current position in the script.

### Common Causes
- Windows-style line endings (CRLF `
`) in a Unix script.
- Missing semicolons or newlines between statements on the same line.
- Typo in a keyword or use of a reserved word incorrectly.

### How to Fix
```bash
# Convert CRLF to LF
dos2unix script.sh
# Or with sed
sed -i 's/\r$//' script.sh

# Check for stray characters
cat -A script.sh | head -20

# Run shellcheck for diagnostics
shellcheck script.sh
```

### Example
```bash
# Broken (CRLF)
echo "hello"$''

# Fixed
echo "hello"
```
