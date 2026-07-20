---
title: "[Solution] GitHub Actions Upload Speed Limit"
description: "Fix GitHub Actions artifact upload speed limit and timeout errors."
tools: ["github-actions"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Upload speed limit errors occur during large artifact uploads:

```
Error: Artifact upload timed out after 3600 seconds
```

## Common Causes

- Very large artifact being uploaded.
- Many small files instead of one archive.

## How to Fix

**Compress before upload:**

```yaml
steps:
  - run: tar -czf artifacts.tar.gz ./dist ./test-results
  - uses: actions/upload-artifact@v4
    with:
      name: compressed-build
      path: artifacts.tar.gz
```

## Examples

```yaml
- run: zip -r build.zip ./dist
- uses: actions/upload-artifact@v4
  with:
    name: build
    path: build.zip
```
