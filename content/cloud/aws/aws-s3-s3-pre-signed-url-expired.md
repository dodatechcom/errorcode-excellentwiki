---
title: "[Solution] AWS S3 Pre-signed URL Expired"
description: "ExpiredToken/SignatureDoesNotMatch when a pre-signed URL is invalid."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `S3 Pre-signed URL Expired` error occurs when an AWS service cannot complete the requested operation.

## Common Causes

- Pre-signed URL expiration time has passed
- Signing timestamp skews due to client clock difference
- Credential used via assumed role has expired
- URL was generated with expired IAM user keys

## How to Fix

### Generate new pre-signed URL

```bash
aws s3 presign s3://my-bucket/file.txt --expires-in 86400
```

## Examples

- Example scenario: pre-signed url expiration time has passed
- Example scenario: signing timestamp skews due to client clock difference
- Example scenario: credential used via assumed role has expired
- Example scenario: url was generated with expired iam user keys

## Related Errors

- [AWS EC2 Error]({{< relref "/cloud/aws/aws-ec2-error" >}}) -- General EC2 errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
