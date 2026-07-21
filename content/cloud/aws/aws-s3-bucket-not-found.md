---
title: "[Solution] AWS S3 Bucket Not Found"
description: "NoSuchBucket error when the specified S3 bucket does not exist."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `S3 Bucket Not Found` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- The bucket name is incorrect
- The bucket was deleted
- The bucket is in a different AWS account
- The bucket is in a different region

## How to Fix

### List buckets

```bash
aws s3 ls
```
### Check bucket in region

```bash
aws s3api head-bucket --bucket my-bucket --region us-west-2
```
### Create bucket

```bash
aws s3 mb s3://my-new-bucket --region us-east-1
```

## Examples

- Accessing a bucket named my-bucket but actual name is my-bucket-12345
- Bucket deleted but still referenced in config

## Related Errors

- [S3 Error]({{< relref "/cloud/aws/aws-s3-error" >}}) -- General S3 errors
- [S3 Access Denied]({{< relref "/cloud/aws/s3-access-denied" >}}) -- S3 access denied
