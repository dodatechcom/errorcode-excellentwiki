---
title: "[Solution] AWS S3 copy object"
description: "CopyObjectError for cross-bucket copy."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `S3 copy object` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- Source archived in Glacier
- Cross-region rate limits
- KMS key mismatch

## How to Fix

### Copy single

```bash
aws s3api copy-object --copy-source src/object.txt --bucket dest --key object.txt
```

### use multicommand

```bash
aws s3 cp s3://src/ s3://dest/ --recursive
```

## Examples

- Example scenario: source archived in glacier
- Example scenario: cross-region rate limits
- Example scenario: kms key mismatch

## Related Errors

- [AWS S3 Error]({{< relref "/cloud/aws/aws-s3-error" >}}) -- General s3 errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
