---
title: "[Solution] Bash Here Document Error"
description: "Fix 'here document' errors in Bash when heredoc syntax is wrong, delimiter not matched, or variable expansion fails."
languages: ["bash"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["here-document", "heredoc", "delimiter", "eof", "input"]
weight: 5
---

# Bash Here Document Error Fix

Here document errors include unmatched delimiter, unexpected end of file, or variables not expanding inside the heredoc.

## What This Error Means

A here document (`<<DELIMITER ... DELIMITER`) feeds multi-line input to a command. The closing delimiter must appear alone on a line. Errors occur when the delimiter is misspelled or indented when it shouldn't be.

## Common Causes

- Closing delimiter not on its own line
- Indented closing delimiter without `<<-`
- Missing delimiter entirely (unterminated heredoc)
- Quotes around delimiter preventing variable expansion
- Tab/space before closing delimiter

## How to Fix

### 1. Ensure delimiter is on its own line

```bash
# WRONG: delimiter on same line as content
cat << EOF
Hello World EOF

# RIGHT: delimiter on its own line
cat << EOF
Hello World
EOF
```

### 2. Use <<- for indented delimiters

```bash
# WRONG: indented delimiter
cat << EOF
    indented content
    EOF

# RIGHT: use <<- for tab-indented delimiters
cat <<- EOF
	indented content
	EOF
```

### 3. Quote the delimiter to prevent expansion

```bash
# Variables will expand:
cat << EOF
Home directory: $HOME
EOF

# Quote delimiter to prevent expansion:
cat << 'EOF'
Home directory: $HOME  # Literal $HOME
EOF
```

### 4. Handle unterminated heredoc

```bash
# If you see "unexpected end of file"
# Check that you have a closing delimiter
cat << EOF
content here
EOF  # Must exist and be on its own line
```

## Related Errors

- [Syntax Error](syntax-error) — general parse errors
- [Bad Substitution](bash-bad-substitution) — variable expansion issues
