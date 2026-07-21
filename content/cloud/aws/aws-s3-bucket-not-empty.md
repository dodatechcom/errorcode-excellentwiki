---
title: "[Solution] AWS S3 Bucket Not Empty"
description: "BucketNotEmpty when trying to delete a bucket that still contains objects."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `S3 Bucket Not Empty` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- Bucket contains objects
- Bucket has versions with versioning enabled
- Incomplete multipart uploads exist
- Delete markers present

## How to Fix

### List objects

```bash
aws s3 ls s3://my-bucket --recursive
```
### Remove all objects

```bash
aws s3 rm s3://my-bucket --recursive
```
### Delete bucket

```bash
aws s3 rb s3://my-bucket
```

## Examples

- Trying to delete my-bucket but it has 500 objects
- Versioning enabled and delete markers exist

## Related Errors

- [S3 Error]({{< relref "/cloud/aws/aws-s3-error" >}}) -- General S3 errors
- [Bucket Not Found]({{< relref "/cloud/aws/aws-s3-bucket-not-found" >}}) -- Bucket not found
