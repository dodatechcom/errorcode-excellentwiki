---
title: "[Solution] AWS IAM role"
description: "InvalidParameterException for IAM role."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `IAM role` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- Role ARN invalid or deleted
- Trust policy missing Lambda service

## How to Fix

### Check role

```bash
aws iam get-role --role my-lambda-role
```

## Examples

- Example scenario: role arn invalid or deleted
- Example scenario: trust policy missing lambda service

## Related Errors

- [AWS LAMBDA Error]({{< relref "/cloud/aws/aws-lambda-error" >}}) -- General lambda errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
