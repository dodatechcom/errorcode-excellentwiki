---
title: "[Solution] AWS S3 Error — access denied or bucket not found"
description: "Fix AWS S3 errors. Resolve S3 access denied and bucket not found issues."
error-types: ["api-error"]
severities: ["error"]
weight: 5
---

An AWS S3 error occurs when you cannot access an S3 bucket or object. This can be due to permissions, wrong bucket name, or region issues.

## Common Causes

- Bucket does not exist or wrong region specified
- IAM policy does not grant S3 access
- Bucket policy blocks the request
- Object does not exist (404)
- Request signed with wrong credentials

## How to Fix

### Check Bucket Exists

```bash
aws s3api head-bucket --bucket my-bucket
```

### Verify Region

```bash
aws s3api get-bucket-location --bucket my-bucket
```

### List Bucket Contents

```bash
aws s3 ls s3://my-bucket/
```

### Check Bucket Policy

```bash
aws s3api get-bucket-policy --bucket my-bucket
```

### Test Access

```bash
aws s3 cp s3://my-bucket/file.txt ./local.txt
```

## Examples

```bash
# Example 1: Bucket not found
aws s3 ls s3://my-bucket
# An error occurred (NoSuchBucket)
# Fix: check bucket name and region

# Example 2: Access denied
aws s3 cp file.txt s3://my-bucket/
# An error occurred (AccessDenied)
# Fix: add s3:PutObject permission
```

## Related Errors

- [AWS IAM Error]({{< relref "/cloud/aws/aws-iam-error" >}}) — IAM permission denied
- [AWS CloudFront Error]({{< relref "/cloud/aws/aws-cloudfront-error" >}}) — CloudFront distribution error
