---
title: "[Solution] Builtin Command Not Found"
description: "Fix 'builtin not found' errors in Bash."
tools: ["bash"]
error-types: ["tool-error"]
severities: ["error"]
---

# [Solution] Builtin Command Not Found

A shell builtin command is not recognized, possibly due to shell version or type.

### Common Causes
- Using a Bash builtin in `sh` or `dash`.
- Builtin was removed or renamed in newer Bash versions.
- PATH manipulation hiding builtins.

### How to Fix
```bash
# Check if command is a builtin
type echo
type cd

# Force builtin usage
builtin echo "hello"
builtin cd /path

# Builtin vs external command
command -v echo    # /bin/echo or builtin
enable echo        # ensure builtin is active

# Disable a builtin (then use external)
enable -n echo
echo "hello"    # now uses /bin/echo
```

### Example
```bash
# Broken (in dash/sh)
#!/bin/sh
mapfile -t arr < <(echo "a\nb")    # mapfile not in sh

# Fixed
#!/bin/bash
mapfile -t arr < <(echo -e "a\nb")
```
