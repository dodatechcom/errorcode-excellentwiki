---
title: "S3 Access Denied"
description: "AccessDenied - User is not authorized to perform s3:GetObject"
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
tags: ["aws", "s3", "iam", "access-denied", "permissions"]
weight: 5
---

The `AccessDenied` error occurs when an AWS IAM user or role attempts to perform an S3 operation (e.g., `s3:GetObject`) without the required permissions.

## Common Causes

- The IAM user/role does not have an explicit `Allow` policy for the S3 action
- A resource-based bucket policy denies access
- The S3 Object Ownership setting restricts access (e.g., bucket owner enforced)
- An SCP or permission boundary limits the allowed actions

## How to Fix

Verify and attach the required IAM policy:

```bash
aws iam put-user-policy \
  --user-name <username> \
  --policy-name S3ReadAccess \
  --policy-document '{
    "Version": "2012-10-17",
    "Statement": [
      {
        "Effect": "Allow",
        "Action": "s3:GetObject",
        "Resource": "arn:aws:s3:::my-bucket/*"
      }
    ]
  }'
```

Test access:

```bash
aws s3 cp s3://my-bucket/file.txt .
```

## Examples

- Attempting to download an object from a bucket where the IAM user has no `s3:GetObject` permission
- Using temporary credentials from an STS assume-role call where the target role lacks S3 access

## Related Errors

- [EC2 Instance Limit Exceeded]({{< relref "/cloud/aws/ec2-instance-limit" >}})
- [Azure Authentication Failed]({{< relref "/cloud/azure/authentication-failed" >}})
- [GCP Permission Denied]({{< relref "/cloud/gcp/permission-denied" >}})
