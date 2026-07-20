---
title: "[Solution] GitHub Actions OIDC Token Not Available"
description: "Fix GitHub Actions OIDC token not available errors."
tools: ["github-actions"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

OIDC token not available errors occur when the OIDC token cannot be obtained:

```
Error: OIDC token request failed: not authorized
```

## Common Causes

- OIDC not enabled in repository settings.
- `id-token: write` permission not set.

## How to Fix

**Enable OIDC and set permissions:**

```yaml
permissions:
  id-token: write
  contents: read

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: aws-actions/configure-aws-credentials@v4
        with:
          role-to-assume: arn:aws:iam::123456789012:role/github-actions
          aws-region: us-east-1
```

## Examples

```yaml
permissions:
  id-token: write
  contents: read
```
