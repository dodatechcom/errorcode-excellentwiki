---
title: "[Solution] GitHub Actions Assume Role Failed"
description: "Fix GitHub Actions assume role failures in cloud workflows."
tools: ["github-actions"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Assume role failures occur when the workflow cannot assume an IAM role:

```
Error: AccessDenied: User is not authorized to assume role
```

## Common Causes

- IAM role trust policy does not allow the GitHub OIDC provider.
- Role ARN is incorrect.
- Role does not exist.

## How to Fix

**Verify role trust policy:**

```yaml
permissions:
  id-token: write
  contents: read
steps:
  - uses: aws-actions/configure-aws-credentials@v4
    with:
      role-to-assume: arn:aws:iam::123456789012:role/github-actions
      aws-region: us-east-1
```

## Examples

```bash
# Verify the role exists
aws iam get-role --role-name github-actions
```
