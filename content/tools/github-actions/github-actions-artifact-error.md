---
title: "GitHub Actions Artifact Upload Error"
description: "GitHub Actions fails to upload or download workflow artifacts."
tools: ["github-actions"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["github-actions", "artifact", "upload", "download", "storage"]
weight: 5
---

# GitHub Actions Artifact Upload Error

An artifact upload error occurs when the `actions/upload-artifact` action fails to save workflow artifacts. This can happen due to size limits, path issues, or permission problems.

## Common Causes

- Artifact size exceeds the 500MB limit per artifact
- File path does not exist or is incorrect
- Artifact name conflicts with existing artifact
- Permissions issue with artifact storage

## How to Fix

### Check File Path Exists

```yaml
- name: Upload build output
  uses: actions/upload-artifact@v4
  with:
    name: build-output
    path: dist/
```

### Reduce Artifact Size

```yaml
- name: Upload artifact
  uses: actions/upload-artifact@v4
  with:
    name: build-output
    path: dist/
    compression-level: 6  # Higher compression
```

### Use Multiple Smaller Artifacts

```yaml
- name: Upload JS artifacts
  uses: actions/upload-artifact@v4
  with:
    name: js-bundle
    path: dist/*.js

- name: Upload CSS artifacts
  uses: actions/upload-artifact@v4
    name: css-bundle
    path: dist/*.css
```

### Fix Artifact Name Conflicts

```yaml
- name: Upload artifact
  uses: actions/upload-artifact@v4
  with:
    name: build-${{ github.run_number }}  # Use unique name
    path: dist/
```

### Check Permissions

```yaml
permissions:
  contents: read
  actions: write
```

## Examples

```yaml
# Error: path does not exist
- uses: actions/upload-artifact@v4
  with:
    name: build
    path: /nonexistent/path

# Error: artifact too large
Error: Artifact size (600MB) exceeds maximum allowed (500MB)
```

## Related Errors

- [Cache Error]({{< relref "/tools/github-actions/github-actions-cache-error" >}}) — cache operation failure
- [Timeout Error]({{< relref "/tools/github-actions/github-actions-timeout-error" >}}) — job timeout
