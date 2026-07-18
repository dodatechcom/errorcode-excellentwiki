---
title: "[Solution] Bash Heredoc Delimiter Not Found Error Fix"
description: "Fix 'heredoc: delimiter not found' in Bash. Resolve heredoc EOF marker issues and quoting problems in shell scripts."
languages: ["bash"]
error-types: ["syntax-error"]
severities: ["error"]
weight: 5
---

# Bash Heredoc Delimiter Not Found Error Fix

The `heredoc: delimiter not found` error occurs when the closing delimiter of a heredoc is missing, misspelled, or not placed at the beginning of a line.

## What This Error Means

A heredoc allows you to pass a block of text to a command. The delimiter (like `EOF`) marks where the text starts and ends. If Bash reaches the end of the file without finding the closing delimiter, it reports this error.

A typical error:

```
script.sh: line 8: warning: here-document at line 1 delimited by end-of-file (wanted `EOF')
```

## Why It Happens

Common causes include:

- **Missing closing delimiter** — The `EOF` marker is never written.
- **Indented closing delimiter** — The delimiter must start at column 0 unless using `<<-`.
- **Misspelled delimiter** — Writing `FOE` instead of `EOF`.
- **Using the wrong delimiter** — Quoted vs unquoted delimiters behave differently.
- **Tab characters instead of spaces** — `<<-` strips tabs but not spaces.

## How to Fix It

### Fix 1: Always close heredoc at column 0

```bash
# WRONG: Indented closing delimiter
cat <<EOF
Hello World
    EOF

# RIGHT: Closing delimiter at start of line
cat <<EOF
Hello World
EOF
```

### Fix 2: Use heredoc with indented code using <<-

```bash
# RIGHT: Use <<- to strip leading tabs
if true; then
	cat <<-EOF
	This line is indented with tabs
	But the output won't have leading tabs
	EOF
fi
```

### Fix 3: Quote the delimiter to prevent variable expansion

```bash
# WRONG: Variables get expanded
cat <<EOF
Home directory: $HOME
EOF

# RIGHT: Quote the delimiter to prevent expansion
cat <<'EOF'
Home directory: $HOME
This is printed literally
EOF
```

### Fix 4: Heredoc with commands

```bash
# RIGHT: Execute commands inside heredoc
cat <<EOF
Current date: $(date)
User: $(whoami)
Home: $HOME
EOF
```

### Fix 5: Heredoc with cat and redirect

```bash
# RIGHT: Write heredoc to a file
cat > config.txt <<EOF
host=localhost
port=3306
database=myapp
EOF
```

### Fix 6: Nested heredocs

```bash
# RIGHT: Use different delimiters for nesting
cat <<OUTER
First level
$(cat <<INNER
Second level
INNER
)
OUTER
```

## Common Mistakes

- **Indenting the closing delimiter** — Without `<<-`, the closing marker must start at column 0.
- **Using spaces with `<<-`** — `<<-` only strips tab characters, not spaces.
- **Forgetting that heredoc expands variables by default** — Quote the delimiter to prevent this.
- **Using heredoc inside functions without proper quoting** — Quoted delimiters prevent expansion.

## Related Pages

- [Bash Bad Substitution](bad-substitution) — Variable expansion issues
- [Bash Syntax Error](bash-syntax-error) — General syntax errors
- [Bash Echo Option Error](bash-echo-option-error) — Echo output issues
