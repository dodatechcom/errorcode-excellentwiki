---
title: "[Solution] AWS Organization SCP"
description: "AccessDenied due to Org policy."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Organization SCP` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- SCP at account or OU blocks

## How to Fix

### Describe effective

```bash
aws organizations describe-effective-policy --type SERVICE_CONTROL
```

## Examples

- Example scenario: scp at account or ou blocks

## Related Errors

- [AWS IAM Error]({{< relref "/cloud/aws/aws-iam-error" >}}) -- General iam errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
