---
title: "[Solution] File Descriptor Not Found"
description: "Resolve 'Bad file descriptor' errors in Bash redirection."
tools: ["bash"]
error-types: ["tool-error"]
severities: ["error"]
---

# [Solution] File Descriptor Not Found

A file descriptor referenced in redirection does not exist or was already closed.

### Common Causes
- Using `>&3` without first opening fd 3.
- Closing a file descriptor and then trying to use it.
- Invalid file descriptor number.

### How to Fix
```bash
# Open a file descriptor before using it
exec 3> output.txt
echo "data" >&3
exec 3>&-

# Use valid fd numbers (0-9, or higher with caution)
exec 4< input.txt
read -r line <&4
exec 4<&-

# Check open descriptors
ls -la /proc/$$/fd/
```

### Example
```bash
# Broken
echo "data" >&3    # fd 3 not opened

# Fixed
exec 3> /tmp/output.txt
echo "data" >&3
exec 3>&-
```
