---
title: "[Solution] AWS S3 — Access Denied to bucket"
description: "Fix AWS S3 Access Denied. Resolve S3 bucket access and permission issues."
cloud: ["aws"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["aws", "s3", "access-denied", "bucket", "permission", "object"]
weight: 5
---

An S3 Access Denied error means the AWS identity does not have permission to access the S3 bucket or object. The request is authenticated but blocked by bucket policies, ACLs, or IAM policies.

## What This Error Means

S3 access control is layered: IAM policies, S3 bucket policies, S3 ACLs, and S3 Block Public Access settings all affect access. An Access Denied error (HTTP 403) occurs when the combination of these controls denies the request. The specific error text helps identify which control is blocking — `AccessDenied` from IAM vs bucket policy vs public access block. Even if IAM allows access, a restrictive bucket policy can still deny it.

## Common Causes

- IAM role or user missing required S3 permissions (s3:GetObject, s3:PutObject, s3:ListBucket)
- S3 bucket policy explicitly denies the requesting identity
- S3 Block Public Access enabled on the bucket
- Bucket is in a different AWS account with no cross-account policy
- Object-level ACLs restricting access
- VPC endpoint policy blocking S3 access

## How to Fix

### Check Bucket Policy

```bash
aws s3api get-bucket-policy --bucket my-bucket
```

### Test Access with IAM Policy

```bash
aws iam simulate-principal-policy \
  --policy-source-arn arn:aws:iam::123456789012:role/my-role \
  --action-names s3:GetObject \
  --resource-arns arn:aws:s3:::my-bucket/*
```

### Grant Bucket Access

```json
{
  "Version": "2012-10-17",
  "Statement": [{
    "Effect": "Allow",
    "Principal": {
      "AWS": "arn:aws:iam::123456789012:role/my-role"
    },
    "Action": [
      "s3:GetObject",
      "s3:ListBucket"
    ],
    "Resource": [
      "arn:aws:s3:::my-bucket",
      "arn:aws:s3:::my-bucket/*"
    ]
  }]
}
```

### Check Block Public Access

```bash
aws s3api get-public-access-block --bucket my-bucket
```

### Disable Block Public Access (If Intended)

```bash
aws s3api delete-public-access-block --bucket my-bucket
```

### Check VPC Endpoint Policy

```bash
aws ec2 describe-vpc-endpoints \
  --filters "Name=vpc-id,Values=vpc-xxx" \
  --query 'VpcEndpoints[*].PolicyDocument'
```

## Related Errors

- [AWS IAM Error]({{< relref "/cloud/aws/aws-iam-error-v2" >}}) — IAM access denied
- [AWS Lambda Error]({{< relref "/cloud/aws/aws-lambda-error-v2" >}}) — Lambda runtime error
- [AWS RDS Error]({{< relref "/cloud/aws/aws-rds-error-v2" >}}) — RDS connection failed
