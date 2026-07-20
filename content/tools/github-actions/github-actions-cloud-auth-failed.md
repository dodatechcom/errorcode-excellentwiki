---
title: "[Solution] GitHub Actions Cloud Auth Failed"
description: "Fix GitHub Actions cloud authentication failures in OIDC workflows."
tools: ["github-actions"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Cloud auth failures occur when OIDC authentication to cloud providers fails:

```
Error: Cloud provider rejected the OIDC token
```

## Common Causes

- OIDC provider not configured in cloud account.
- Trust policy does not match GitHub OIDC claims.

## How to Fix

**Configure AWS OIDC trust:**

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

```json
{
  "Effect": "Allow",
  "Principal": {
    "Federated": "arn:aws:iam::123456789012:oidc-provider/token.actions.githubusercontent.com"
  },
  "Action": "sts:AssumeRoleWithWebIdentity",
  "Condition": {
    "StringEquals": {
      "token.actions.githubusercontent.com:aud": "sts.amazonaws.com"
    },
    "StringLike": {
      "token.actions.githubusercontent.com:sub": "repo:owner/repo:*"
    }
  }
}
```
