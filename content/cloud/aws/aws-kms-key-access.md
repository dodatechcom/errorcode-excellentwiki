---
title: "[Solution] AWS KMS key access"
description: "KMS.AccessDenied for S3 accessing the key."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `KMS key access` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- KMS key policy doesn't allow S3
- Cross-account permissions missing

## How to Fix

### Get key policy

```bash
aws kms get-key-policy --key alias/s3-key --name default
```

## Examples

- Example scenario: kms key policy doesn't allow s3
- Example scenario: cross-account permissions missing

## Related Errors

- [AWS KMS Error]({{< relref "/cloud/aws/aws-kms-error" >}}) -- General kms errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
