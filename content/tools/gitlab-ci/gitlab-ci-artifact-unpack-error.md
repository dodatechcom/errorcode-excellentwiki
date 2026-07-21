---
title: "[Solution] GitLab CI Artifact Unpack Error"
description: "Fix GitLab CI artifact unpack errors when downloaded artifacts cannot be extracted or are corrupted."
tools: ["gitlab-ci"]
error-types: ["tool-error"]
severities: ["error"]
---

# GitLab CI Artifact Unpack Error

Artifact unpack errors occur when artifacts downloaded from a previous job cannot be extracted, are corrupted, or have an unsupported format.

## Common Causes

- Artifact file is corrupted during upload or download
- Network interruption caused partial artifact transfer
- Artifact exceeds maximum allowed size
- Disk space on runner is insufficient for extraction
- Artifact format mismatch (expected archive but received raw file)

## How to Fix

### Solution 1: Verify artifact integrity

Add a checksum verification step:

```yaml
build_job:
  script:
    - npm run build
    - tar -czf artifacts.tar.gz dist/
    - sha256sum artifacts.tar.gz > artifacts.sha256
  artifacts:
    paths:
      - artifacts.tar.gz
      - artifacts.sha256
```

### Solution 2: Increase runner disk space

Ensure sufficient disk space on the runner for artifact extraction:

```bash
# Check available disk space
df -h /home/gitlab-runner/builds
```

### Solution 3: Use artifact compression

Compress artifacts before upload to reduce transfer issues:

```yaml
artifacts:
  paths:
    - dist/
  expire_in: 1 week
```

## Examples

```
ERROR: artifact unpack failed: unexpected end of data
WARNING: Error downloading artifact: connection reset
```

## Prevent It

- Monitor runner disk usage
- Set appropriate artifact expiration policies
- Use `needs:artifact: true` to control artifact downloads
