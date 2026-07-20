---
title: "[Solution] GitHub Actions AWS Credential Error"
description: "Fix GitHub Actions AWS credential configuration errors."
tools: ["github-actions"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

AWS credential errors occur when the workflow cannot authenticate with AWS:

```
Error: Unable to locate credentials
```

## Common Causes

- AWS credentials not configured.
- IAM role not assumed via OIDC.

## How to Fix

**Configure AWS credentials via OIDC:**

```yaml
permissions:
  id-token: write
  contents: read
steps:
  - uses: aws-actions/configure-aws-credentials@v4
    with:
      role-to-assume: ${{ secrets.AWS_ROLE_ARN }}
      aws-region: us-east-1
  - run: aws s3 ls
```

## Examples

```yaml
# OIDC approach (preferred)
permissions:
  id-token: write
  contents: read
steps:
  - uses: aws-actions/configure-aws-credentials@v4
    with:
      role-to-assume: ${{ secrets.AWS_ROLE_ARN }}
      aws-region: us-east-1
```
