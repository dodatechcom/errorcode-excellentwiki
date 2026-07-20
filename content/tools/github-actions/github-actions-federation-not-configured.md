---
title: "[Solution] GitHub Actions Federation Not Configured"
description: "Fix GitHub Actions federation not configured errors for cloud providers."
tools: ["github-actions"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Federation not configured errors occur when OIDC federation is not set up:

```
Error: OIDC provider not found for this repository
```

## Common Causes

- OIDC provider not created in the cloud account.
- Repository not added to the trust policy.

## How to Fix

**Set up OIDC federation:**

```bash
# AWS
aws iam create-open-id-connect-provider   --url https://token.actions.githubusercontent.com   --thumbprint-list 6938fd4d98bab03faadb97b34396831e3780aea1   --client-id-list sts.amazonaws.com
```

## Examples

```yaml
permissions:
  id-token: write
  contents: read
steps:
  - uses: aws-actions/configure-aws-credentials@v4
    with:
      role-to-assume: ${{ secrets.AWS_ROLE_ARN }}
      aws-region: us-east-1
```
