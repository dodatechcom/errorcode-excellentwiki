---
title: "[Solution] GitHub Actions Deployment Branch Mismatch"
description: "Fix GitHub Actions deployment branch policy mismatch errors."
tools: ["github-actions"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Branch mismatch errors occur when the deployment branch does not match environment policies:

```
Error: Branch 'feature-x' is not allowed to deploy to 'production'
```

## Common Causes

- Environment restricted to specific branches (e.g., main only).
- Deployment triggered from a non-allowed branch.

## How to Fix

**Configure branch policy:**

```yaml
jobs:
  deploy:
    runs-on: ubuntu-latest
    environment:
      name: production
    if: github.ref == 'refs/heads/main'
    steps:
      - uses: actions/checkout@v4
```

## Examples

```yaml
jobs:
  deploy:
    if: github.ref == 'refs/heads/main'
    environment: production
```
