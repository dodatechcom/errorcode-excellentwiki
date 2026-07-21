---
title: "[Solution] AWS S3 Bucket Access Denied"
description: "AccessDenied when S3 bucket access is denied due to permissions."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `S3 Bucket Access Denied` error occurs when an AWS service cannot complete the requested operation.

## Common Causes

- IAM role/user lacks s3:ListBucket permission
- Bucket policy denies access explicitly
- SCP or Organization policy blocks access
- Public access block prevents anonymous access
- Cross-account bucket policy misconfiguration

## How to Fix

### Check IAM permissions

```bash
aws iam simulate-principal-policy --action s3:ListBucket --resource-arn arn:aws:s3:::my-bucket --policy-source-user arn:aws:iam::123456789012:user/myuser
```

### Check bucket policy

```bash
aws s3api get-bucket-policy --bucket my-bucket
```

### Check public access block

```bash
aws s3api get-public-access-block --bucket my-bucket
```

### List buckets

```bash
aws s3 ls
```

### Cross-account check

```bash
aws s3api get-bucket-acl --bucket my-bucket --expected-bucket-owner 123456789012
```

## Examples

- Example scenario: iam role/user lacks s3:listbucket permission
- Example scenario: bucket policy denies access explicitly
- Example scenario: scp or organization policy blocks access
- Example scenario: public access block prevents anonymous access

## Related Errors

- [AWS EC2 Error]({{< relref "/cloud/aws/aws-ec2-error" >}}) -- General EC2 errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
