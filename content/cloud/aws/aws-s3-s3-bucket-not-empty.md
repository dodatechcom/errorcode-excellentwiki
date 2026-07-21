---
title: "[Solution] AWS S3 Bucket Not Empty"
description: "BucketNotEmpty when trying to delete a non-empty bucket."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `S3 Bucket Not Empty` error occurs when an AWS service cannot complete the requested operation.

## Common Causes

- Bucket contains objects
- Bucket versioning enabled and has versions
- Delete markers present in versioned bucket
- Incomplete multipart uploads exist
- Object ACLs reference the bucket

## How to Fix

### List objects

```bash
aws s3 ls s3://my-bucket/ --recursive
```

### Delete all objects

```bash
aws s3 rm s3://my-bucket/ --recursive
```

### Delete versioned objects

```bash
aws s3api delete-objects --bucket my-bucket --delete file://delete.json
```

### Abort multipart uploads

```bash
aws s3api list-multipart-uploads --bucket my-bucket
```

### Force bucket deletion

```bash
aws s3 rb s3://my-bucket --force
```

## Examples

- Example scenario: bucket contains objects
- Example scenario: bucket versioning enabled and has versions
- Example scenario: delete markers present in versioned bucket
- Example scenario: incomplete multipart uploads exist

## Related Errors

- [AWS EC2 Error]({{< relref "/cloud/aws/aws-ec2-error" >}}) -- General EC2 errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
