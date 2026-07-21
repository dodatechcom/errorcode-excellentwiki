---
title: "[Solution] AWS S3 Copy Object Failed"
description: "CopyObjectError when cross-bucket or cross-region copy fails."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `S3 Copy Object Failed` error occurs when an AWS service cannot complete the requested operation.

## Common Causes

- Source object is archived (Glacier/Deep Archive)
- Cross-region copy rate limits hit
- Source or destination bucket access denied
- KMS key mismatch between source and destination
- Object size exceeds 5 GB (use multipart copy)

## How to Fix

### Single object copy

```bash
aws s3api copy-object --copy-source source-bucket/path/to/object.txt --bucket destination-bucket --key copied/object.txt
```

### Use multipart copy for large files

```bash
aws s3 cp s3://source-bucket/path/ s3://dest-bucket/path/ --recursive --cli-connect-timeout 0
```

### Restore from Glacier first

```bash
aws s3api restore-object --bucket source-bucket --key path/to/object.txt
```

## Examples

- Example scenario: source object is archived (glacier/deep archive)
- Example scenario: cross-region copy rate limits hit
- Example scenario: source or destination bucket access denied
- Example scenario: kms key mismatch between source and destination

## Related Errors

- [AWS EC2 Error]({{< relref "/cloud/aws/aws-ec2-error" >}}) -- General EC2 errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
