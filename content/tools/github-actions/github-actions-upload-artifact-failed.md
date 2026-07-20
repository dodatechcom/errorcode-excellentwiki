---
title: "[Solution] GitHub Actions Upload Artifact Failed"
description: "Fix GitHub Actions upload-artifact action failures."
tools: ["github-actions"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Upload artifact failures occur when the artifact cannot be uploaded:

```
Error: Artifact upload failed: 413 Request Entity Too Large
```

## Common Causes

- Artifact exceeds the 10GB size limit.
- Artifact path does not exist.
- Artifact name conflict with existing artifact.

## How to Fix

**Compress before uploading:**

```yaml
steps:
  - name: Create artifact
    run: tar -czf artifact.tar.gz ./dist
  - uses: actions/upload-artifact@v4
    with:
      name: build-output
      path: artifact.tar.gz
      retention-days: 1
```

## Examples

```yaml
- uses: actions/upload-artifact@v4
  with:
    name: my-artifact
    path: ./dist
    retention-days: 7
    compression-level: 6
```
