---
title: "[Solution] Bash Exec Redirection Error -- Incorrect File Descriptor Usage"
description: "Fix bash exec redirection errors when using exec for file descriptor manipulation."
languages: ["bash"]
error-types: ["syntax-error"]
severities: ["error"]
---

# Bash Exec Redirection Error

This error occurs when `exec` is used incorrectly for file descriptor redirection.

## Common Causes

- `exec` replacing shell process when not intended
- File descriptors not properly closed
- Redirecting to closed file descriptors
- Not using exec correctly for persistent redirections

## How to Fix

### Use exec for shell-wide redirection

```bash
# WRONG: this redirect only applies in subshell
(cmd > file)  # only cmd's output redirected

# CORRECT: exec redirects everything after it
exec >logfile.txt 2>&1
echo "This goes to logfile.txt"
```

### Close file descriptors properly

```bash
exec 3>output.txt
echo "data" >&3
exec 3>&-  # close fd 3
```

## Examples

```bash
#!/bin/bash
# Redirect all output to log
exec > >(tee -a logfile.txt) 2>&1

echo "Starting script..."
# All output now goes to logfile.txt and stdout
```
