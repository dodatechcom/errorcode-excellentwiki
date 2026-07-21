---
title: "[Solution] AWS Delete non-empty bucket"
description: "BucketNotEmpty for deleting a non-empty bucket."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Delete non-empty bucket` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- Bucket contains objects
- Versioning enabled with delete markers
- Multipart uploads in progress

## How to Fix

### Delete all objects

```bash
aws s3 rm s3://my-bucket/ --recursive
```

### Force bucket deletion

```bash
aws s3 rb s3://my-bucket --force
```

## Examples

- Example scenario: bucket contains objects
- Example scenario: versioning enabled with delete markers
- Example scenario: multipart uploads in progress

## Related Errors

- [AWS EC2 Error]({{< relref "/cloud/aws/aws-ec2-error" >}}) -- General ec2 errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
