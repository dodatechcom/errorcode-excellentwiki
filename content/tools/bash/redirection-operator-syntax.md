---
title: "[Solution] Redirection Operator Syntax Error"
description: "Fix redirection operator syntax errors in Bash."
tools: ["bash"]
error-types: ["tool-error"]
severities: ["error"]
---

# [Solution] Redirection Operator Syntax Error

A redirection operator is used incorrectly or has malformed syntax.

### Common Causes
- `>>` vs `>` confusion (append vs overwrite).
- Invalid fd combination (e.g., `2>&1>`).
- Missing space around operators.

### How to Fix
```bash
# Append stderr and stdout
command &> file          # bash: both to file
command > file 2>&1      # POSIX: both to file
command >> file 2>&1     # append both

# Redirect specific fd
command 2>/dev/null      # suppress stderr
command 1>/dev/null      # suppress stdout

# Duplicate fd
exec 3>&1               # save stdout to fd 3
```

### Example
```bash
# Broken
command > file &>       # syntax error

# Fixed
command > file 2>&1
```
