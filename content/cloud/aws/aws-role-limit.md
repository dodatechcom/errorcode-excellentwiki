---
title: "[Solution] AWS Role Limit"
description: "LimitExceeded for role count."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Role Limit` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- 1000 roles per account default
- Service-linked roles

## How to Fix

### Count roles

```bash
aws iam list-roles --query length(Roles)
```

## Examples

- Example scenario: 1000 roles per account default
- Example scenario: service-linked roles

## Related Errors

- [AWS IAM Error]({{< relref "/cloud/aws/aws-iam-error" >}}) -- General iam errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
