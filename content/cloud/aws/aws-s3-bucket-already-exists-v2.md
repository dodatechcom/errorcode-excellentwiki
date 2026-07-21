---
title: "[Solution] AWS S3 Bucket Already Exists"
description: "BucketAlreadyExists globally taken name."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `S3 Bucket Already Exists` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- Bucket name globally unique
- Another account owns the name

## How to Fix

### Use different name

```bash
aws s3api create-bucket --bucket my-unique-98765 --region us-east-1
```

## Examples

- Example scenario: bucket name globally unique
- Example scenario: another account owns the name

## Related Errors

- [AWS S3 Error]({{< relref "/cloud/aws/aws-s3-error" >}}) -- General s3 errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
