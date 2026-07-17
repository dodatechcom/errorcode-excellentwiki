---
title: "[Solution] Bash Heredoc Delimiter Not Found Error Fix"
description: "Fix bash heredoc delimiter errors when the closing delimiter is missing or mismatched."
languages: ["bash"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Bash Heredoc Delimiter Not Found Error Fix

A bash heredoc error occurs when the closing delimiter of a heredoc is not found, is misspelled, or is indented when it shouldn't be.

## What This Error Means

Heredocs in bash (`<<DELIMITER ... DELIMITER`) read multi-line input until the closing delimiter is found on a line by itself. If the delimiter is missing, the shell reads until EOF and then fails with a "heredoc delimiter not found" error.

## Common Causes

- Misspelled closing delimiter
- Indented closing delimiter when not using `<<-`
- Missing newline before closing delimiter
- Delimiter text appears inside the heredoc body

## How to Fix

### 1. Match delimiters exactly

```bash
# WRONG: Mismatched delimiters
cat <<EOF
Hello World
END  # Wrong delimiter

# CORRECT: Match exactly
cat <<EOF
Hello World
EOF
```

### 2. Use <<- for indented delimiters

```bash
# WRONG: Indented delimiter with <<
cat <<EOF
	Hello World
	EOF  # Error: indentation

# CORRECT: Use <<- to allow tab indentation
cat <<-EOF
	Hello World
	EOF
```

### 3. Ensure closing delimiter is on its own line

```bash
# WRONG: No newline before delimiter
cat <<EOF
Hello World
EOF

# CORRECT: Empty line before delimiter is fine, but delimiter must be alone
cat <<EOF
Hello World

EOF
```

### 4. Quote the delimiter to prevent variable expansion

```bash
# WRONG: Variables expanded inside heredoc
cat <<EOF
User: $USER
Home: $HOME
EOF

# CORRECT: Quote the delimiter to prevent expansion
cat <<'EOF'
User: $USER
Home: $HOME
EOF
```

## Related Errors

- [Bash Syntax Error](syntax-error) — general syntax issues
- [Bash Bad Substitution](bad-substitution) — variable expansion errors
- [Unmatched Quote](unmatched-quote) — quote matching issues
