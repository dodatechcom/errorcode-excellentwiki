---
title: "[Solution] Unterminated Here-Document"
description: "Resolve unterminated here-doc (<<) errors in Bash scripts."
tools: ["bash"]
error-types: ["tool-error"]
severities: ["error"]
---

# [Solution] Unterminated Here-Document

A heredoc was opened with `<<` but the closing delimiter was never found.

### Common Causes
- Closing delimiter has leading whitespace when it should not (or vice versa).
- Delimiter is quoted in the opening but not in the closing.
- Missing newline before the closing delimiter.

### How to Fix
```bash
# Ensure closing delimiter is on its own line with no indentation
cat <<EOF
content
EOF

# If using tab-indented heredoc, use <<-
cat <<-EOF
	content
	EOF

shellcheck script.sh
```

### Example
```bash
# Broken
cat <<EOF
hello world
  EOF    # leading whitespace causes error

# Fixed
cat <<EOF
hello world
EOF
```
