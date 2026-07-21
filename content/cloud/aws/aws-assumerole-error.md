---
title: "[Solution] AWS AssumeRole Error"
description: "AccessDenied for AssumeRole."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `AssumeRole Error` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- Trust policy excludes principal
- MFA missing
- Session too long

## How to Fix

### Check trust

```bash
aws iam get-role --role my-role --query AssumeRolePolicy
```

## Examples

- Example scenario: trust policy excludes principal
- Example scenario: mfa missing
- Example scenario: session too long

## Related Errors

- [AWS IAM Error]({{< relref "/cloud/aws/aws-iam-error" >}}) -- General iam errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
