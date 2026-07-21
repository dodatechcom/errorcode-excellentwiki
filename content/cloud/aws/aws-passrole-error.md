---
title: "[Solution] AWS PassRole Error"
description: "AccessDenied for PassRole."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `PassRole Error` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- Missing PassRole permission
- Boundary blocking

## How to Fix

### Simulate passrole

```bash
aws iam simulate-custom-policy --action PassRole
```

## Examples

- Example scenario: missing passrole permission
- Example scenario: boundary blocking

## Related Errors

- [AWS IAM Error]({{< relref "/cloud/aws/aws-iam-error" >}}) -- General iam errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
