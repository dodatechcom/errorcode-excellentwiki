---
title: "[Solution] AWS Secret Rotation"
description: "InvalidRequestException for rotation."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Secret Rotation` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- Lambda for rotation not exist
- Period invalid

## How to Fix

### Describe secret

```bash
aws secretsmanager describe-secret --secret-id my-secret
```

## Examples

- Example scenario: lambda for rotation not exist
- Example scenario: period invalid

## Related Errors

- [AWS IAM Error]({{< relref "/cloud/aws/aws-iam-error" >}}) -- General iam errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
