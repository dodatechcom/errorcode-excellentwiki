---
title: "[Solution] AWS Access Key Expired"
description: "ExpiredToken for expired keys."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Access Key Expired` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- Key not rotated
- Deactivated by admin

## How to Fix

### Create new key

```bash
aws iam create-access-key
```

## Examples

- Example scenario: key not rotated
- Example scenario: deactivated by admin

## Related Errors

- [AWS IAM Error]({{< relref "/cloud/aws/aws-iam-error" >}}) -- General iam errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
