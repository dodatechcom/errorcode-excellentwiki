---
title: "[Solution] Bash Heredoc Error -- Incorrect Here Document Syntax"
description: "Fix bash heredoc errors when heredoc delimiters are mismatched or incorrectly indented."
languages: ["bash"]
error-types: ["syntax-error"]
severities: ["error"]
---

# Bash Heredoc Error

This error occurs when heredoc syntax is incorrect, such as mismatched delimiters or indentation issues.

## Common Causes

- Closing delimiter not at the start of the line (no indentation)
- Mismatched opening and closing delimiters
- Using quoted delimiter to prevent variable expansion when expansion is wanted
- Missing newline after closing delimiter

## How to Fix

### Use correct heredoc syntax

```bash
# WRONG: closing delimiter indented
cat <<EOF
hello
    EOF  # error: not found

# CORRECT: delimiter at start of line
cat <<EOF
hello
EOF
```

### Use indented heredoc

```bash
# For scripts with indentation
cat <<-EOF
    This content will have leading tabs stripped
    and will work inside indented code blocks
EOF
```

## Examples

```bash
#!/bin/bash
cat <<EOF
Server: $(hostname)
Date: $(date)
User: $USER
EOF
```
