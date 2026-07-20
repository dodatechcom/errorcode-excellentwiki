---
title: "[Solution] Heredoc Delimiter Error"
description: "Fix heredoc delimiter mismatch errors in Bash."
tools: ["bash"]
error-types: ["tool-error"]
severities: ["error"]
---

# [Solution] Heredoc Delimiter Error

The heredoc closing delimiter does not match the opening delimiter.

### Common Causes
- Quoted vs unquoted delimiter mismatch.
- Closing delimiter has extra whitespace.
- Indented heredoc with wrong syntax.

### How to Fix
```bash
# Simple heredoc
cat <<EOF
hello world
EOF

# Quoted delimiter (no variable expansion)
cat <<'EOF'
$HOME is not expanded
EOF

# Indented heredoc (use <<-)
cat <<-EOF
	indented content
	EOF

# Tab-indented closing delimiter must use tabs, not spaces
```

### Example
```bash
# Broken
cat <<EOF
hello
eoF    # wrong case

# Fixed
cat <<EOF
hello
EOF
```
