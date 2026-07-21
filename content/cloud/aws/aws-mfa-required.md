---
title: "[Solution] AWS MFA Required"
description: "AccessDenied when MFA enforced."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `MFA Required` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- MFA not configured
- Session without token

## How to Fix

### List MFA

```bash
aws iam list-virtual-mfa-devices
```

## Examples

- Example scenario: mfa not configured
- Example scenario: session without token

## Related Errors

- [AWS IAM Error]({{< relref "/cloud/aws/aws-iam-error" >}}) -- General iam errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
