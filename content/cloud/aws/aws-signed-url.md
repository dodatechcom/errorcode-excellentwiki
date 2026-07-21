---
title: "[Solution] AWS Signed URL"
description: "AccessDenied for signed URLs."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Signed URL` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- Policy invalid
- Expired signature
- Resource mismatch

## How to Fix

### Generate signed URL

```bash
aws cloudfront sign --url https://xxx.cloudfront.net/file.txt --key-pair-id K12XYZ
```

## Examples

- Example scenario: policy invalid
- Example scenario: expired signature
- Example scenario: resource mismatch

## Related Errors

- [AWS CLOUDFRONT Error]({{< relref "/cloud/aws/aws-cloudfront-error" >}}) -- General cloudfront errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
