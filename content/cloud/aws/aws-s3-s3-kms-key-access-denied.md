---
title: "[Solution] AWS S3 KMS Key Access Denied"
description: "KMS.AccessDeniedException when S3 cannot access the KMS key."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `S3 KMS Key Access Denied` error occurs when an AWS service cannot complete the requested operation.

## Common Causes

- KMS key IAM policy does not allow S3 service
- Cross-account KMS key permissions missing
- KMS key is disabled or pending deletion
- Grant for S3 service expired or revoked
- Region mismatch between bucket and KMS key

## How to Fix

### Check KMS key policy

```bash
aws kms get-key-policy --key-id alias/my-s3-key --policy-name default
```

### Enable key

```bash
aws kms enable-key --key-id alias/my-s3-key
```

## Examples

- Example scenario: kms key iam policy does not allow s3 service
- Example scenario: cross-account kms key permissions missing
- Example scenario: kms key is disabled or pending deletion
- Example scenario: grant for s3 service expired or revoked

## Related Errors

- [AWS EC2 Error]({{< relref "/cloud/aws/aws-ec2-error" >}}) -- General EC2 errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
