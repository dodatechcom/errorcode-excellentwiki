---
title: "[Solution] AWS S3 ACL Error"
description: "AccessControlListError when S3 ACL configuration is invalid."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `S3 ACL Error` error occurs when an AWS service cannot complete the requested operation.

## Common Causes

- ACL grantee email format is incorrect
- URI for group grant does not exist
- Exceeds 100 grants per ACL limit
- Cannot set ACL when bucket policy exists
- Object ACL and bucket ACL conflict

## How to Fix

### Set object ACL

```bash
aws s3api put-object-acl --bucket my-bucket --key file.txt --acl bucket-owner-full-control
```

### Get ACL

```bash
aws s3api get-object-acl --bucket my-bucket --key file.txt
```

## Examples

- Example scenario: acl grantee email format is incorrect
- Example scenario: uri for group grant does not exist
- Example scenario: exceeds 100 grants per acl limit
- Example scenario: cannot set acl when bucket policy exists

## Related Errors

- [AWS EC2 Error]({{< relref "/cloud/aws/aws-ec2-error" >}}) -- General EC2 errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
