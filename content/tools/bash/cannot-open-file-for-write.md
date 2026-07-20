---
title: "[Solution] Cannot Open File for Writing"
description: "Fix 'cannot open file for writing' errors in Bash."
tools: ["bash"]
error-types: ["tool-error"]
severities: ["error"]
---

# [Solution] Cannot Open File for Writing

The output target file cannot be opened for writing.

### Common Causes
- Directory does not exist.
- File permissions are read-only.
- Disk is full.
- File descriptor limit reached.

### How to Fix
```bash
# Check disk space
df -h .

# Ensure directory exists
mkdir -p "$(dirname "$outfile")"

# Use umask for file creation permissions
umask 022

# Check writable
[[ -w "$(dirname "$outfile")" ]] || { echo "Cannot write to directory" >&2; exit 1; }
```

### Example
```bash
# Broken
echo "data" > /readonly/dir/file.txt

# Fixed
mkdir -p /tmp/output
echo "data" > /tmp/output/file.txt
```
