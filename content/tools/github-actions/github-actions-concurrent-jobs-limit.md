---
title: "[Solution] GitHub Actions Concurrent Jobs Limit"
description: "Fix GitHub Actions concurrent jobs limit exceeded errors."
tools: ["github-actions"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Concurrent jobs limit errors occur when too many jobs run simultaneously:

```
Error: Maximum number of concurrent jobs reached (20)
```

## Common Causes

- Multiple workflows triggering at the same time.
- Large matrix strategies.

## How to Fix

**Limit concurrency:**

```yaml
concurrency:
  group: build-${{ github.ref }}
  cancel-in-progress: true
```

## Examples

```yaml
concurrency:
  group: deploy-production
  cancel-in-progress: false
```
