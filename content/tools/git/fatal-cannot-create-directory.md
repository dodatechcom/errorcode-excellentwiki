---
title: "[Solution] Git fatal: cannot create directory"
description: "Fix 'cannot create directory' error. Resolve Git checkout failures when it cannot create required directories in the working tree."
tools: ["git"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Git fatal: cannot create directory

fatal: cannot create directory at '<path>': Permission denied

This error occurs when Git needs to create a directory during checkout, but the filesystem does not allow it or the parent directory has insufficient permissions.

## Common Causes

- Parent directory has incorrect permissions
- Disk is full or read-only
- File system is mounted as read-only
- There is a file with the same name as the required directory
- Path contains characters not supported by the filesystem

## How to Fix

### Check Parent Directory Permissions

```bash
ls -la <parent-directory>
chmod u+w <parent-directory>
```

### Check Disk Space

```bash
df -h .
```

### Remove Conflicting File

```bash
rm <path>
git checkout <branch>
```

### Remount Filesystem for Write

```bash
sudo mount -o remount,rw <mount-point>
```

## Examples

```bash
# Example 1: Read-only parent directory
ls -la /path/to/parent
# dr-xr-xr-x   # missing write permission
# Fix: chmod u+w /path/to/parent
git checkout feature/branch

# Example 2: File blocking directory creation
rm src/utils
git checkout main

# Example 3: Remount filesystem
sudo mount -o remount,rw /mnt/data
git pull origin main
```

## Related Errors

- [Merge Conflict]({{< relref "/tools/git/merge-conflict" >}}) — resolve merge conflicts
- [Push Rejected]({{< relref "/tools/git/push-rejected" >}}) — fix rejected pushes
