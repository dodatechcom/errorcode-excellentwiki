---
title: "[Solution] AWS Permissions Boundary"
description: "PermissionsBoundaryNotSupported."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Permissions Boundary` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- Action disallowed by boundary

## How to Fix

### Check boundary

```bash
aws iam get-role --role my-role --query PermissionsBoundary
```

## Examples

- Example scenario: action disallowed by boundary

## Related Errors

- [AWS IAM Error]({{< relref "/cloud/aws/aws-iam-error" >}}) -- General iam errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
