---
title: "[Solution] Git LFS Push Failed — upload failed"
description: "Fix Git LFS push/upload failures. Resolve LFS object upload errors."
tools: ["git"]
error-types: ["tool-error"]
severities: ["error"]
tags: ["lfs", "push", "upload", "large-files", "git"]
weight: 5
---

A Git LFS push error occurs when LFS objects cannot be uploaded to the remote server. This can be caused by network issues, authentication problems, or file size limits.

## Common Causes

- Network timeout or connectivity issues during upload
- Authentication token expired or insufficient permissions
- File exceeds the LFS server's maximum file size limit
- LFS server is unavailable or has storage quota exceeded
- Corrupted LFS objects locally

## How to Fix

### Check LFS Status

```bash
git lfs status
git lfs ls-files
```

### Retry the Push

```bash
git lfs push --all origin main
```

### Check Authentication

```bash
git credential fill <<EOF
protocol=https
host=github.com
EOF
```

### Verify File Size Limits

```bash
git lfs env
```

### Force Re-Upload LFS Objects

```bash
git lfs push --force origin main
```

## Examples

```bash
# Example 1: Push LFS objects manually
git lfs push --all origin main

# Example 2: Check LFS environment and limits
git lfs env
# endpoint=https://github.com/user/repo.git (auth=basic)
# max concurrent transfers=8

# Example 3: Re-initialize and push
git lfs install
git lfs track "*.zip"
git add .gitattributes
git commit -m "Update LFS tracking"
git push origin main
```

## Related Errors

- [Git LFS Error]({{< relref "/tools/git/git-lfs-error" >}}) — pointer file mismatch
- [Git Merge Conflict]({{< relref "/tools/git/git-merge-conflict" >}}) — merge conflict resolution
