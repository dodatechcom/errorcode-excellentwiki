---
title: "[Solution] Bash Permission Denied Error -- Script Execution Issues"
description: "Fix bash permission denied errors when executing scripts or accessing files without proper permissions."
languages: ["bash"]
error-types: ["runtime-error"]
severities: ["error"]
---

# Bash Permission Denied Error

This error occurs when a script or command lacks the necessary file system permissions to execute or access a file.

## Common Causes

- Script file not marked as executable
- Insufficient read permissions on source files
- Attempting to write to system directories without sudo
- Incorrect file ownership

## How to Fix

### Make script executable

```bash
# WRONG: no execute permission
./myscript.sh  # permission denied

# CORRECT: add execute permission
chmod +x myscript.sh
./myscript.sh
```

### Check and fix permissions

```bash
# Check permissions
ls -la script.sh

# Add execute permission
chmod u+x script.sh

# Or run with bash explicitly
bash script.sh
```

## Examples

```bash
#!/bin/bash
# Ensure this script is executable: chmod +x deploy.sh

if [ ! -x "$0" ]; then
    echo "Making script executable..."
    chmod +x "$0"
fi
```
