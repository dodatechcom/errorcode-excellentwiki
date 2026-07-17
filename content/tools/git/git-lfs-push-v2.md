---
title: "[Solution] Git LFS Push Failed"
description: "Fix Git LFS upload failures. Resolve LFS push errors when uploading large files to the remote server."
tools: ["git"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["lfs", "push", "upload", "large-files", "server", "git"]
weight: 5
---

## What This Error Means

A Git LFS push failure means the large file objects tracked by LFS could not be uploaded to the remote server. This can happen due to network issues, authentication problems, or server-side limits.

## Common Causes

- LFS server is unreachable or has connectivity issues
- Authentication credentials expired or invalid
- File exceeds server-side size limit
- LFS server storage quota exceeded
- Network timeout on large file uploads
- Server does not support LFS or LFS endpoint is misconfigured

## How to Fix

### Check LFS Endpoint Configuration

```bash
git lfs env
```

### Retry the Push

```bash
git lfs push origin main
```

### Push Specific Files

```bash
git lfs push --include="*.zip" origin main
```

### Set Authentication Credentials

```bash
git lfs env
# Check the LFS endpoint URL
# Configure credentials in .netrc or credential helper
```

### Verify LFS Server Access

```bash
git lfs ls-files
git lfs status
```

### Set Transfer Timeout

```bash
git config lfs.activitytimeout 3600
git config lfs.concurrenttransfers 3
```

## Examples

```bash
# Example 1: Push LFS objects
git push origin main
# Uploading LFS objects: 100% (3/3), 256 MB | 10 MB/s, done

# If it fails:
git lfs push origin main

# Example 2: Push with retry
git lfs push --all origin main

# Example 3: Push specific file types
git lfs push --include="*.psd,*.zip" origin main

# Example 4: Check server connectivity
git lfs env
# Endpoint=basic https://user@github.com/user/repo.git/info/lfs
# Adapter=http
```

## Related Errors

- [Git LFS Error]({{< relref "/tools/git/git-lfs-error-v2" >}}) — LFS pointer mismatch
- [Git Push Error]({{< relref "/tools/git/git-push-error-v2" >}}) — push rejected
- [Git Fetch Error]({{< relref "/tools/git/git-fetch-error" >}}) — fetch failed
