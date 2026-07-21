---
title: "[Solution] AWS Policy Size Too Large"
description: "LimitExceeded for policy size."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Policy Size Too Large` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- Policy more than 6144 bytes
- SCP more than 5120 bytes

## How to Fix

### Create new

```bash
aws iam create-policy --policy my-policy --file policy.json
```

## Examples

- Example scenario: policy more than 6144 bytes
- Example scenario: scp more than 5120 bytes

## Related Errors

- [AWS IAM Error]({{< relref "/cloud/aws/aws-iam-error" >}}) -- General iam errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
