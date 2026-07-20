---
title: "[Solution] Git fatal: Unable to create file"
description: "Fix 'Unable to create file' error. Resolve Git checkout, merge, and pull failures from filesystem permission or space issues."
tools: ["git"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Git fatal: Unable to create file

fatal: Unable to create file '<path>': Permission denied

This error occurs when Git cannot write a file to the working directory during checkout, merge, or pull operations.

## Common Causes

- File permissions prevent writing
- Disk is full or inode exhausted
- File is locked by another process
- Directory does not exist
- File path is too long for the filesystem

## How to Fix

### Check Disk Space

```bash
df -h .
```

### Check File Permissions

```bash
ls -la <directory>
chmod u+w <directory>
```

### Close Programs Locking the File

```bash
lsof <file>
# Kill the process holding the lock
kill <PID>
```

### Check Inode Usage

```bash
df -i .
```

## Examples

```bash
# Example 1: Permission denied
git checkout feature/branch
# fatal: Unable to create file 'src/config.js': Permission denied
# Fix: chmod u+w src/config.js && git checkout feature/branch

# Example 2: Disk full
df -h .
# Filesystem  Size  Used Avail Use% Mounted on
# /dev/sda1   50G   50G     0 100% /
# Fix: free up disk space

# Example 3: File locked by process
lsof src/config.js
# COMMAND  PID  USER   FD   TYPE DEVICE
# vim     1234 user   4r   REG   ...
# Fix: kill -9 1234 && git checkout src/config.js
```

## Related Errors

- [Merge Conflict]({{< relref "/tools/git/merge-conflict" >}}) — resolve merge conflicts
- [Push Rejected]({{< relref "/tools/git/push-rejected" >}}) — fix rejected pushes
