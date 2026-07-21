---
title: "[Solution] AWS Pre-signed expired"
description: "ExpiredToken/SignatureDoesNotMatch for pre-signed URL."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Pre-signed expired` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- URL expiration passed
- Assumed role expired

## How to Fix

### Generate new URL

```bash
aws s3 presign s3://my-bucket/file.txt --expires 86400
```

## Examples

- Example scenario: url expiration passed
- Example scenario: assumed role expired

## Related Errors

- [AWS EC2 Error]({{< relref "/cloud/aws/aws-ec2-error" >}}) -- General ec2 errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
