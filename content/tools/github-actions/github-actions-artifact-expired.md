---
title: "[Solution] GitHub Actions Artifact Expired"
description: "Fix GitHub Actions artifact expired and unavailable errors."
tools: ["github-actions"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Artifact expired errors occur when artifacts are past their retention period:

```
Error: Artifact has expired and cannot be downloaded
```

## Common Causes

- Artifact retention period reached.
- Organization-level retention policies.

## How to Fix

**Upload with appropriate retention:**

```yaml
- uses: actions/upload-artifact@v4
  with:
    name: long-lived-artifact
    path: ./dist
    retention-days: 90
```

## Examples

```yaml
retention-days: 30  # Short-term
retention-days: 90  # Long-term
```
