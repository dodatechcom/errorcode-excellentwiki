---
title: "[Solution] AWS S3 Object Access Denied"
description: "AccessDenied when S3 object get/put is denied."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `S3 Object Access Denied` error occurs when an AWS service cannot complete the requested operation.

## Common Causes

- IAM permissions missing for s3:GetObject
- Object ACL has restrictive grants
- Bucket policy overrides allow with deny
- KMS key used for encryption not accessible
- Pre-signed URL expired or signature invalid

## How to Fix

### Test IAM permissions

```bash
aws s3api get-object --bucket my-bucket --key path/to/object.txt out.txt
```

### Check bucket policy

```bash
aws s3api get-bucket-policy --bucket my-bucket
```

### Get object ACL

```bash
aws s3api get-object-acl --bucket my-bucket --key path/to/object.txt
```

### Check encryption settings

```bash
aws s3api get-object-attributes --bucket my-bucket --key path/to/object.txt
```

## Examples

- Example scenario: iam permissions missing for s3:getobject
- Example scenario: object acl has restrictive grants
- Example scenario: bucket policy overrides allow with deny
- Example scenario: kms key used for encryption not accessible

## Related Errors

- [AWS EC2 Error]({{< relref "/cloud/aws/aws-ec2-error" >}}) -- General EC2 errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
