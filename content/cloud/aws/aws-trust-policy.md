---
title: "[Solution] AWS Trust Policy"
description: "MalformedPolicyDocument."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Trust Policy` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- Principal invalid
- Missing sts:AssumeRole

## How to Fix

### Get trust policy

```bash
aws iam get-role --role my-role --query AssumeRolePolicy
```

## Examples

- Example scenario: principal invalid
- Example scenario: missing sts:assumerole

## Related Errors

- [AWS IAM Error]({{< relref "/cloud/aws/aws-iam-error" >}}) -- General iam errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
