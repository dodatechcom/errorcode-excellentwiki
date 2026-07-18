---
title: "[Solution] Docker Hub Image Retention Error"
description: "Fix Docker Hub image retention errors. Learn why this happens and how to resolve it quickly."
tools: ["dockerhub"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Docker Hub Image Retention Error

Docker Hub image retention errors occur when image cleanup or archival fails.

## Why This Happens

- Retention policy not set
- Cleanup failed
- Storage limit exceeded
- Archive error

## Common Error Messages

- `retention_not_set_error`
- `retention_cleanup_error`
- `retention_storage_error`
- `retention_archive_error`

## How to Fix It

### Solution 1: Set retention policies

Configure image retention:

```bash
# Via Docker Hub UI
Settings > Repository > Retention Policy
```

### Solution 2: Monitor storage

Track storage usage.

### Solution 3: Clean up manually

Remove old images and tags.


## Common Scenarios

- **Retention not set:** Configure retention policies.
- **Storage limit exceeded:** Clean up old images or upgrade plan.

## Prevent It

- Set appropriate retention
- Monitor storage usage
- Clean up regularly
