---
title: "[Solution] AWS S3 Bucket Already Exists"
description: "BucketAlreadyExists when creating a bucket with a taken name."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `S3 Bucket Already Exists` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- Bucket name is globally unique and taken
- Bucket recently deleted but DNS still resolves
- You own the bucket in another region
- Bucket name reserved by AWS

## How to Fix

### Try unique name

```bash
aws s3 mb s3://my-unique-bucket-$(date +%s)
```
### Check ownership

```bash
aws s3api list-buckets --query "Buckets[?Name==`my-bucket`]"
```
### List owned buckets

```bash
aws s3api list-buckets --query "Buckets[*].[Name,CreationDate]" --output table
```

## Examples

- Creating bucket my-company-prod when account 111111 already owns it
- Deleted bucket myapp-v1 but trying to recreate immediately

## Related Errors

- [S3 Error]({{< relref "/cloud/aws/aws-s3-error" >}}) -- General S3 errors
- [Bucket Not Found]({{< relref "/cloud/aws/aws-s3-bucket-not-found" >}}) -- Bucket not found
