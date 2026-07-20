---
title: "[Solution] Tee Permission or Usage Error"
description: "Fix tee command errors when writing to files in Bash."
tools: ["bash"]
error-types: ["tool-error"]
severities: ["error"]
---

# [Solution] Tee Permission or Usage Error

The `tee` command fails to write to the specified output file.

### Common Causes
- Output file location is read-only.
- Permission denied on the directory.
- Too many open file descriptors.

### How to Fix
```bash
# Basic tee usage
command | tee output.txt

# Append mode
command | tee -a output.txt

# Suppress tee output to terminal
command | tee output.txt >/dev/null

# Multiple outputs
command | tee file1.txt file2.txt

# Check directory permissions
ls -ld "$(dirname output.txt)"
```

### Example
```bash
# Broken
command | tee /root/output.txt    # permission denied

# Fixed
command | tee "$HOME/output.txt"
```
