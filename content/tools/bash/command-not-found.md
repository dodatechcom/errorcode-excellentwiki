---
title: "[Solution] Command Not Found Error"
description: "Fix 'command not found' error in Bash shell."
tools: ["bash"]
error-types: ["tool-error"]
severities: ["error"]
---

# [Solution] Command Not Found Error

Bash cannot locate the command in `PATH` or as a builtin.

### Common Causes
- Command is not installed.
- Program directory not in `PATH`.
- Typo in the command name.
- Script uses a non-standard shell.

### How to Fix
```bash
# Check if command exists
which command_name
type command_name

# Search for package
apt search command_name    # Debian/Ubuntu
yum search command_name    # RHEL/CentOS

# Add directory to PATH
export PATH="/new/path:$PATH"

# Verify PATH
echo "$PATH" | tr ':' '\n'
```

### Example
```bash
# Broken
myapp --version    # myapp not in PATH

# Fixed
export PATH="$HOME/.local/bin:$PATH"
myapp --version
```
