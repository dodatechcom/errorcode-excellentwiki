---
title: "[Solution] GitHub Actions Artifact Path Invalid"
description: "Fix GitHub Actions artifact path invalid errors."
tools: ["github-actions"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Invalid path errors occur when the artifact upload path is incorrect:

```
Error: No files were found with the provided path: ./nonexistent-dir
```

## Common Causes

- Directory or file does not exist at the specified path.
- Build step did not produce the expected output.

## How to Fix

**Verify path exists before upload:**

```yaml
steps:
  - run: npm run build
  - run: ls -la ./dist || echo "dist directory not found"
  - uses: actions/upload-artifact@v4
    with:
      name: build
      path: ./dist
```

## Examples

```yaml
- uses: actions/upload-artifact@v4
  with:
    name: coverage
    path: |
      coverage/
      !coverage/tmp/
```
