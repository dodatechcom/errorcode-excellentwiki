---
title: "[Solution] AWS Origin Access Denied"
description: "OriginAccessIdentityAccessDenied."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Origin Access Denied` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- Bucket ACL missing perms
- Protocol mismatch

## How to Fix

### Check bucket policy

```bash
aws s3api get-bucket-policy --bucket my-bucket
```

## Examples

- Example scenario: bucket acl missing perms
- Example scenario: protocol mismatch

## Related Errors

- [AWS CLOUDFRONT Error]({{< relref "/cloud/aws/aws-cloudfront-error" >}}) -- General cloudfront errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
