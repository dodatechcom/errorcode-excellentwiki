---
title: "[Solution] AWS SCP Error"
description: "AccessDenied due to SCP."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `SCP Error` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- SCP denies the action
- Overlapping SCPs

## How to Fix

### List SCPs

```bash
aws organizations list-policies --filter SERVICE_CONTROL_POLICY
```

## Examples

- Example scenario: scp denies the action
- Example scenario: overlapping scps

## Related Errors

- [AWS IAM Error]({{< relref "/cloud/aws/aws-iam-error" >}}) -- General iam errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
