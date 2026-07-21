---
title: "[Solution] AWS S3 Bucket Access Denied"
description: "AccessDenied when accessing an S3 bucket without proper permissions."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `S3 Bucket Access Denied` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- Bucket policy denies the request
- IAM policy does not grant required S3 permissions
- Bucket in different account without cross-account access
- S3 Block Public Access enabled

## How to Fix

### Check bucket policy

```bash
aws s3api get-bucket-policy --bucket my-bucket --output json
```
### Check ACL

```bash
aws s3api get-bucket-acl --bucket my-bucket
```
### Set bucket policy

```bash
aws s3api put-bucket-policy --bucket my-bucket --policy file://policy.json
```

## Examples

- IAM user without s3:GetObject tries to read from bucket
- Bucket policy has explicit Deny for user IP range

## Related Errors

- [S3 Error]({{< relref "/cloud/aws/aws-s3-error" >}}) -- General S3 errors
- [IAM Error]({{< relref "/cloud/aws/aws-iam-error" >}}) -- IAM errors
