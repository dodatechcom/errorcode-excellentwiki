---
title: "[Solution] CircleCI Artifact Compression Error"
description: "Fix CircleCI artifact compression errors when artifacts fail to compress and upload due to size or disk space constraints."
tools: ["circleci"]
error-types: ["tool-error"]
severities: ["error"]
---

# CircleCI Artifact Compression Error

Artifact compression errors occur when CircleCI cannot compress and upload job artifacts due to excessive size, disk space limits, or compression failures.

## Common Causes

- Artifact files exceed the maximum allowed size
- Disk space on the executor is exhausted during compression
- Artifact paths include binary files that are difficult to compress
- Too many small files increase compression overhead

## How to Fix

### Solution 1: Reduce artifact size

```yaml
steps:
  - run:
      name: Clean artifacts
      command: |
        find dist/ -name "*.map" -delete
        rm -rf dist/*.test.*
  - store_artifacts:
      path: dist
```

### Solution 2: Compress before storing

```yaml
steps:
  - run:
      name: Compress artifacts
      command: tar -czf artifacts.tar.gz dist/
  - store_artifacts:
      path: artifacts.tar.gz
      destination: build-output
```

### Solution 3: Use selective artifact storage

```yaml
steps:
  - store_artifacts:
      path: dist/index.js
      destination: dist/index.js
  - store_artifacts:
      path: dist/style.css
      destination: dist/style.css
```

## Examples

```
Error: artifact upload failed: file too large
WARNING: Artifact compression exceeded disk space limit
```

## Prevent It

- Exclude unnecessary files from artifacts
- Set artifact retention policies
- Monitor artifact sizes in the CircleCI UI
