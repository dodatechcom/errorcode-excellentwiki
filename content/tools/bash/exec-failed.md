---
title: "[Solution] Exec Command Failed"
description: "Fix 'exec failed' errors when replacing shell process."
tools: ["bash"]
error-types: ["tool-error"]
severities: ["error"]
---

# [Solution] Exec Command Failed

The `exec` command could not replace the current shell process.

### Common Causes
- Binary file does not exist or is not executable.
- Insufficient permissions.
- `exec` fails and shell continues unexpectedly.

### How to Fix
```bash
# Check if command exists before exec
if [[ -x "/path/to/command" ]]; then
    exec /path/to/command "$@"
else
    echo "Command not found" >&2
    exit 1
fi

# exec for fd redirection (no replacement)
exec 3> output.txt
echo "data" >&3
exec 3>&-

# exec to change shell settings
exec bash    # start new bash
exec zsh     # switch to zsh
```

### Example
```bash
# Broken
exec /nonexistent/command    # fails silently

# Fixed
command -v mytool >/dev/null 2>&1 || { echo "mytool not found" >&2; exit 1; }
exec mytool "$@"
```
