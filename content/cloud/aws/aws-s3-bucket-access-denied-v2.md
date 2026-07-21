---
title: "[Solution] AWS S3 Bucket Access Denied"
description: "AccessDenied for S3 bucket due to permissions."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `S3 Bucket Access Denied` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- Missing s3:ListBucket IAM permission
- Bucket policy denies explicitly
- SCP blocks this action
- Public access block active

## How to Fix

### Simulate IAM

```bash
aws iam simulate-principal-policy --action s3:ListBucket --policy-user arn:aws:iam::123:user/myuser
```

### Check bucket policy

```bash
aws s3api get-bucket-policy --bucket my-bucket
```

### Check public block

```bash
aws s3api get-public-access-block --bucket my-bucket
```

## Examples

- Example scenario: missing s3:listbucket iam permission
- Example scenario: bucket policy denies explicitly
- Example scenario: scp blocks this action
- Example scenario: public access block active

## Related Errors

- [AWS S3 Error]({{< relref "/cloud/aws/aws-s3-error" >}}) -- General s3 errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
