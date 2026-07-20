---
title: "[Solution] GitHub Actions Artifact Retention Exceeded"
description: "Fix GitHub Actions artifact retention period exceeded errors."
tools: ["github-actions"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Retention exceeded errors occur when artifacts are accessed after their retention period:

```
Error: Artifact has expired and is no longer available
```

## Common Causes

- Default retention is 90 days.
- Artifact was uploaded with short retention.

## How to Fix

**Set longer retention period:**

```yaml
- uses: actions/upload-artifact@v4
  with:
    name: important-build
    path: ./dist
    retention-days: 365
```

## Examples

```yaml
# Maximum retention (90 days for free, 400 for enterprise)
retention-days: 90
```
