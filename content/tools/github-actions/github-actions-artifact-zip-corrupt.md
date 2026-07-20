---
title: "[Solution] GitHub Actions Artifact Zip Corrupt"
description: "Fix GitHub Actions corrupt artifact zip errors."
tools: ["github-actions"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Corrupt artifact errors occur when the downloaded artifact is damaged:

```
Error: zip: not a valid zip file
```

## Common Causes

- Upload was interrupted.
- Storage backend corruption.

## How to Fix

**Verify artifact integrity:**

```yaml
- run: |
    sha256sum ./artifact.zip
    unzip -t ./artifact.zip
```

## Examples

```yaml
- run: echo "${{ steps.upload.outputs.checksum }}" > checksum.txt
```
