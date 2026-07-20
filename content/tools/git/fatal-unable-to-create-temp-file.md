---
title: "[Solution] Git fatal: Unable to create temporary file"
description: "Fix 'unable to create temporary file' error. Resolve Git failures caused by disk space, permission, or temporary directory issues."
tools: ["git"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Git fatal: Unable to create temporary file

fatal: Unable to create temporary file '/path/to/tmp/': Permission denied

This error occurs when Git cannot create temporary files in the system temp directory. The operation fails due to filesystem limitations.

## Common Causes

- Disk space is exhausted
- Temp directory has wrong permissions
- Temp directory is on a read-only filesystem
- System temp directory is full
- Inode exhaustion on the filesystem

## How to Fix

### Check Disk Space

```bash
df -h
```

### Check Temp Directory Permissions

```bash
ls -la /tmp
ls -la /var/tmp
```

### Set Custom Temp Directory

```bash
git config --global core.tmpdir /path/to/large/tmp
```

### Clean Temp Files

```bash
rm -rf /tmp/*
```

### Point TMPDIR Environment Variable

```bash
export TMPDIR=/path/to/tmp
git clone <repo>
```

## Examples

```bash
# Example 1: Disk full
df -h /
# Filesystem  Size  Used Avail Use% Mounted on
# /dev/sda1   50G   50G     0 100% /
# Fix: free up space or use different disk

# Example 2: Temp directory permissions
sudo chmod 1777 /tmp
git pull origin main

# Example 3: Use alternative temp dir
mkdir ~/mytmp
export TMPDIR=~/mytmp
git push origin main
```

## Related Errors

- [Merge Conflict]({{< relref "/tools/git/merge-conflict" >}}) — resolve merge conflicts
- [Push Rejected]({{< relref "/tools/git/push-rejected" >}}) — fix rejected pushes
