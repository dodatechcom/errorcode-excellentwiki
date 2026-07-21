---
title: "[Solution] GitLab CI Runner Cache Permission"
description: "Fix GitLab CI runner cache permission errors when the runner cannot read or write cache files on disk."
tools: ["gitlab-ci"]
error-types: ["tool-error"]
severities: ["error"]
---

# GitLab CI Runner Cache Permission

Runner cache permission errors happen when the GitLab Runner process lacks file system permissions to access or create cache directories.

## Common Causes

- Runner user does not own the cache directory
- SELinux or AppArmor policies block access
- Cache directory on a read-only or mounted volume
- Docker executor volume mount lacks correct permissions
- Multiple runners sharing a cache path with different UIDs

## How to Fix

### Solution 1: Fix directory ownership

Ensure the runner user owns the cache directory:

```bash
sudo chown -R gitlab-runner:gitlab-runner /home/gitlab-runner/cache
```

### Solution 2: Configure runner cache path

Edit `config.toml` to use a path with correct permissions:

```toml
[[runners]]
  [runners.cache]
    Type = "s3"
    [runners.cache.s3]
      BucketName = "gitlab-runner-cache"
      BucketLocation = "us-east-1"
```

### Solution 3: Use distributed cache

Move cache to S3 or GCS to avoid local file system issues:

```toml
[[runners]]
  [runners.cache]
    Type = "gcs"
    [runners.cache.gcs]
      BucketName = "my-runner-cache"
```

## Examples

```
WARNING: Failed to create cache: permission denied
cache: not uploading cache due to local file permission error
```

## Prevent It

- Use dedicated cache directories with correct ownership
- Consider S3/GCS cache backends for multi-runner setups
- Check SELinux contexts on cache paths
