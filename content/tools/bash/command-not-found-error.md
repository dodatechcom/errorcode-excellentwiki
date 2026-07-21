---
title: "[Solution] Bash Command Not Found Error"
description: "Fix Bash command not found errors when commands are not in PATH or not installed."
tools: ["bash"]
error-types: ["tool-error"]
severities: ["error"]
---

# Bash Command Not Found Error

Bash cannot find a command in the PATH or locate the executable.

```
bash: command_name: command not found
```

## Common Causes

- Command not installed
- Command not in PATH
- PATH variable overwritten or empty
- Typo in command name
- Script not marked as executable

## How to Fix

### Check Command Location

```bash
# Find where a command is located
which command_name
type command_name

# Search for it
find /usr -name "command_name" 2>/dev/null
```

### Fix PATH Issues

```bash
# Check current PATH
echo "$PATH"

# Add directory to PATH
export PATH="/usr/local/bin:/usr/bin:$PATH"

# Make persistent in .bashrc
echo 'export PATH="/usr/local/bin:$PATH"' >> ~/.bashrc
```

### Install Missing Package

```bash
# Debian/Ubuntu
apt install package-name

# RHEL/CentOS
yum install package-name

# Python
pip install package-name

# Node.js
npm install -g package-name
```

### Make Script Executable

```bash
chmod +x my_script.sh
./my_script.sh
```

### Use Full Path as Workaround

```bash
# Instead of just the command
/usr/local/bin/python3 script.py
```

## Examples

```bash
#!/bin/bash
# Safe command execution
safe_command() {
    if ! command -v "$1" &>/dev/null; then
        echo "Command not found: $1" >&2
        return 1
    fi
    "$@"
}

safe_command docker ps
safe_command node --version
```

```bash
# Check multiple commands
for cmd in git node npm python3; do
    if command -v "$cmd" &>/dev/null; then
        echo "Found: $cmd ($(command -v "$cmd"))"
    else
        echo "Missing: $cmd"
    fi
done
```
