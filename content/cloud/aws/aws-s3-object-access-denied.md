---
title: "[Solution] AWS S3 Object Access Denied"
description: "403 Forbidden when accessing a specific S3 object without permission."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `S3 Object Access Denied` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- Object-level ACL denies access
- IAM policy lacks s3:GetObject for specific key
- Bucket policy denies access to key prefix
- SSE-KMS key access not granted

## How to Fix

### Check object ACL

```bash
aws s3api get-object-acl --bucket my-bucket --key file.txt
```
### Check KMS permissions

```bash
aws kms describe-key --key-id alias/my-key
```
### Grant read access

```bash
aws s3api put-object-acl --bucket my-bucket --key file.txt --grant-read uri=http://acs.amazonaws.com/groups/global/AuthenticatedUsers
```

## Examples

- IAM role has s3:GetObject on bucket but not specific key prefix
- SSE-KMS encrypted object but role lacks kms:Decrypt

## Related Errors

- [S3 Error]({{< relref "/cloud/aws/aws-s3-error" >}}) -- General S3 errors
- [S3 Access Denied]({{< relref "/cloud/aws/s3-access-denied" >}}) -- Bucket-level access denied
