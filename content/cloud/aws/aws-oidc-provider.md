---
title: "[Solution] AWS OIDC Provider"
description: "InvalidInput for OIDC providers."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `OIDC Provider` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- URL unreachable
- Thumbprint incorrect

## How to Fix

### List OIDC

```bash
aws iam list-open-id-connect-providers
```

## Examples

- Example scenario: url unreachable
- Example scenario: thumbprint incorrect

## Related Errors

- [AWS IAM Error]({{< relref "/cloud/aws/aws-iam-error" >}}) -- General iam errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
