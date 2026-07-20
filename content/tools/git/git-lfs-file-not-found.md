---
title: "[Solution] Git LFS: File not found in LFS store"
description: "Fix Git LFS 'file not found' error. Resolve missing LFS objects when pulling or cloning repositories using Git Large File Storage."
tools: ["git"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Git LFS: File not found in LFS store

Error downloading object: <file> (xx bytes): Smudge error: Error downloading <file> (<hash>): Object not found

This error occurs when Git LFS cannot find a file in the remote LFS storage. The LFS object is missing from the server.

## Common Causes

- LFS object was deleted from the storage server
- LFS storage migration without updating pointers
- Permissions to access the LFS storage are insufficient
- Branch contains LFS objects not pushed to the server
- LFS storage quota exceeded

## How to Fix

### Fetch LFS Objects Manually

```bash
git lfs fetch --all
```

### Check LFS Status

```bash
git lfs status
```

### Pull LFS Objects

```bash
git lfs pull
```

### Point to New LFS Storage

```bash
git config lfs.url <new-lfs-url>
```

## Examples

```bash
# Example 1: Missing LFS object
git lfs pull
# Error downloading object: design.psd (15 MB)
# Fix: git lfs fetch --all origin main

# Example 2: LFS storage migrated
git config lfs.url https://github.com/user/repo.git/info/lfs
git lfs fetch --all

# Example 3: Verify LFS tracked files
git lfs ls-files --all
# Check which files are tracked
```

## Related Errors

- [Merge Conflict]({{< relref "/tools/git/merge-conflict" >}}) — resolve merge conflicts
- [Push Rejected]({{< relref "/tools/git/push-rejected" >}}) — fix rejected pushes
