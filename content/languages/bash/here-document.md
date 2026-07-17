---
title: "[Solution] Bash Here-Document Error"
description: "Fix 'here-document' errors in Bash when heredoc syntax or delimiters are incorrect."
languages: ["bash"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# Bash Here-Document Error Fix

This error occurs when a heredoc (here-document) construct has incorrect syntax, mismatched delimiters, or is used improperly.

## Description

Heredocs allow you to pass multi-line input to a command using `<<DELIMITER ... DELIMITER` syntax. The opening and closing delimiters must match exactly (unless quoted). Malformed heredocs cause parse errors or unexpected behavior.

## Common Causes

- **Mismatched delimiter** — opening `<<EOF` but closing with `END`.
- **Delimiter with trailing spaces** — `<<EOF ` won't match `EOF` (unless using `<<-`).
- **Indentation issues** — closing delimiter indented when not using `<<-`.
- **Missing newline before closing delimiter** — the last line must end with a newline.

## How to Fix

### Fix 1: Ensure delimiter names match exactly

```bash
# Wrong
cat <<EOF
Hello world
END

# Right
cat <<EOF
Hello world
EOF
```

### Fix 2: Quote the delimiter to prevent variable expansion

```bash
# Unquoted — variables are expanded
cat <<EOF
$HOME
EOF

# Quoted — variables treated literally
cat <<'EOF'
$HOME
EOF
```

### Fix 3: Use <<- for indented heredocs

```bash
# Allows indentation of the closing delimiter
cat <<-EOF
Indented content
	EOF
```

### Fix 4: Ensure final newline exists

```bash
# Wrong — no newline after closing EOF
cat <<EOF
content
EOF>

# Right
cat <<EOF
content
EOF
```

## Examples

```bash
$ cat <<EOF
Hello
world
END
bash: heredoc: line 3: syntax error: unexpected end of file

$ cat <<EOF
$HOME is expanded
EOF
/home/user is expanded

$ cat <<'EOF'
$HOME is literal
EOF
$HOME is literal
```

## Related Errors

- [Unmatched Quote](unmatched-quote) — similar unterminated construct error.
- [Syntax Error Near Unexpected Token](syntax-error) — general parse errors.
