---
title: "[Solution] AWS Secret Not Found"
description: "ResourceNotFoundException for Secrets Manager."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Secret Not Found` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- Name/ARN incorrect
- Deleted or scheduled for deletion

## How to Fix

### List secrets

```bash
aws secretsmanager list-secrets
```

## Examples

- Example scenario: name/arn incorrect
- Example scenario: deleted or scheduled for deletion

## Related Errors

- [AWS IAM Error]({{< relref "/cloud/aws/aws-iam-error" >}}) -- General iam errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
