---
title: "[Solution] AWS S3 Bucket Already Exists"
description: "BucketAlreadyExists when the S3 bucket name is already taken."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `S3 Bucket Already Exists` error occurs when an AWS service cannot complete the requested operation.

## Common Causes

- Bucket name must be globally unique across all AWS accounts
- Account already owns a bucket with the name
- Another account owns the bucket name
- Bucket was recently deleted and name not released yet
- DNS propagation of deleted bucket name not complete

## How to Fix

### Use a different bucket name

```bash
aws s3api create-bucket --bucket my-unique-name-98765 --region us-east-1
```

### Check existing buckets

```bash
aws s3 ls
```

### Verify ownership

```bash
aws s3api get-bucket-location --bucket my-bucket
```

## Examples

- Example scenario: bucket name must be globally unique across all aws accounts
- Example scenario: account already owns a bucket with the name
- Example scenario: another account owns the bucket name
- Example scenario: bucket was recently deleted and name not released yet

## Related Errors

- [AWS EC2 Error]({{< relref "/cloud/aws/aws-ec2-error" >}}) -- General EC2 errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
