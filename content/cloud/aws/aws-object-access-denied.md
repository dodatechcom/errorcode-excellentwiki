---
title: "[Solution] AWS Object Access Denied"
description: "AccessDenied for object operations."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Object Access Denied` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- s3:GetObject IAM missing
- Object ACL restrictive
- KMS key not accessible

## How to Fix

### Test permissions

```bash
aws s3api get-object --bucket my-bucket --key path/to/object.txt out.txt
```

## Examples

- Example scenario: s3:getobject iam missing
- Example scenario: object acl restrictive
- Example scenario: kms key not accessible

## Related Errors

- [AWS EC2 Error]({{< relref "/cloud/aws/aws-ec2-error" >}}) -- General ec2 errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
