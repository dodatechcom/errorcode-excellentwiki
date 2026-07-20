---
title: "[Solution] Permission Denied Error"
description: "Resolve 'Permission denied' errors when running Bash commands."
tools: ["bash"]
error-types: ["tool-error"]
severities: ["error"]
---

# [Solution] Permission Denied Error

The current user lacks execute or read permissions for the target file or directory.

### Common Causes
- Script file lacks execute permission.
- Trying to write to a read-only directory or file.
- Insufficient user/group permissions.

### How to Fix
```bash
# Add execute permission to a script
chmod +x script.sh

# Check current permissions
ls -la script.sh

# Change ownership
sudo chown user:group file

# Use sudo if needed (carefully)
sudo command
```

### Example
```bash
# Broken
./deploy.sh    # -rw-r--r-- permissions

# Fixed
chmod +x deploy.sh
./deploy.sh
```
