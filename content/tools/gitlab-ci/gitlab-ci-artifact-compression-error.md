---
title: "[Solution] GitLab CI Artifact Compression Error"
description: "Fix GitLab CI artifact compression errors when artifact files fail to compress during upload to the GitLab server."
tools: ["gitlab-ci"]
error-types: ["tool-error"]
severities: ["error"]
---

# GitLab CI Artifact Compression Error

Artifact compression errors occur when the runner fails to compress artifacts before uploading them to the GitLab instance, often due to disk or memory constraints.

## Common Causes

- Artifact files exceed the runner's available disk space
- Compression process runs out of memory on the runner
- Temporary directory is full or has restricted permissions
- Artifact paths include special characters or broken symlinks

## How to Fix

### Solution 1: Exclude unnecessary files

Reduce the artifact set before compression:

```yaml
artifacts:
  paths:
    - dist/
  exclude:
    - dist/**/*.map
    - dist/**/*.test.js
    - node_modules/
    - .git/
```

### Solution 2: Compress artifacts manually

Handle compression in the job script:

```yaml
build_job:
  script:
    - npm run build
    - tar -czf dist.tar.gz dist/
  artifacts:
    paths:
      - dist.tar.gz
```

### Solution 3: Increase runner temporary space

```bash
# Set a larger temporary directory
export TMPDIR=/mnt/large-tmp
gitlab-runner start
```

## Examples

```
ERROR: Error uploading artifact: out of memory
WARNING: Artifact compression failed: disk full
```

## Prevent It

- Exclude build intermediates from artifacts
- Monitor runner disk and memory usage
- Use `expire_in` to prevent storage accumulation
