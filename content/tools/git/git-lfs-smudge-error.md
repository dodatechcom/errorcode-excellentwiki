---
title: "[Solution] Git LFS: Smudge error"
description: "Fix Git LFS 'smudge' error. Resolve failures when Git LFS converts LFS pointers to actual file content during checkout."
tools: ["git"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Git LFS: Smudge error

Smudge error: Error downloading <file>: Server error: 404 Not Found

This error occurs when Git LFS fails to download the actual file content during the smudge filter process (converting pointer to actual file on checkout).

## Common Causes

- Network connectivity issues
- LFS object missing from server
- Authentication failure for LFS storage
- LFS storage URL changed
- File was deleted from LFS storage

## How to Fix

### Skip Smudge During Checkout

```bash
GIT_LFS_SKIP_SMUDGE=1 git checkout <branch>
git lfs pull
```

### Disable LFS Temporarily

```bash
git config filter.lfs.smudge "git lfs smudge --skip"
git checkout <branch>
git config filter.lfs.smudge "git lfs smudge -- %f"
```

### Re-authenticate with LFS

```bash
git lfs login
```

### Check LFS Server URL

```bash
git config lfs.url
```

## Examples

```bash
# Example 1: Skip smudge
GIT_LFS_SKIP_SMUDGE=1 git checkout feature/branch
git lfs pull

# Example 2: Re-authenticate
git lfs login
git lfs pull

# Example 3: Check LFS configuration
git lfs env
# Verify URL and access token
```

## Related Errors

- [Merge Conflict]({{< relref "/tools/git/merge-conflict" >}}) — resolve merge conflicts
- [Push Rejected]({{< relref "/tools/git/push-rejected" >}}) — fix rejected pushes
