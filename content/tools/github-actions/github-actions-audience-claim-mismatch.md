---
title: "[Solution] GitHub Actions Audience Claim Mismatch"
description: "Fix GitHub Actions audience claim mismatch errors in OIDC tokens."
tools: ["github-actions"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Audience claim mismatch errors occur when the OIDC token audience does not match:

```
Error: audience claim does not match expected value
```

## Common Causes

- OIDC token audience is not set correctly.
- Cloud provider expects a different audience.

## How to Fix

**Set correct audience in cloud configuration:**

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

## Examples

```yaml
# AWS expects sts.amazonaws.com as audience
# Azure expects api://AzureADTokenExchange
```
