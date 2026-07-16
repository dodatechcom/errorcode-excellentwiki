---
title: "AWS AccessDeniedException"
description: "AccessDeniedException / UnauthorizedAccess — Fix AWS API access denied errors."
cloud: ["aws"]
error-types: ["api-error"]
severities: ["error"]
tags: ["aws", "iam", "access-denied", "unauthorized", "permissions"]
weight: 5
---

The `AccessDeniedException` or `UnauthorizedAccess` error occurs when an AWS API call is made by an identity (IAM user, role, or root account) that does not have the required permissions to perform the requested action.

## Common Causes

- The IAM user/role does not have an explicit `Allow` policy for the action and resource
- An explicit `Deny` policy overrides any `Allow` permissions
- The IAM policy is attached to the wrong identity or does not include the resource ARN
- Service Control Policies (SCPs) or permission boundaries restrict the action

## How to Fix

Check the current IAM policy attached to the user or role:

```bash
aws iam list-attached-user-policies --user-name <username>

# Or for roles
aws iam list-attached-role-policies --role-name <role-name>
```

Attach a policy granting the required permissions:

```bash
aws iam put-role-policy \
  --role-name <role-name> \
  --policy-name AllowS3Access \
  --policy-document '{
    "Version": "2012-10-17",
    "Statement": [
      {
        "Effect": "Allow",
        "Action": ["s3:GetObject", "s3:PutObject"],
        "Resource": "arn:aws:s3:::my-bucket/*"
      }
    ]
  }'
```

Verify permissions with the IAM policy simulator:

```bash
aws iam simulate-principal-policy \
  --policy-source-arn arn:aws:iam::123456789012:role/my-role \
  --action-names s3:GetObject \
  --resource-arns arn:aws:s3:::my-bucket/*
```

## Examples

- An IAM user with only `ReadOnlyAccess` tries to call `s3:PutObject`
- A Lambda execution role lacks `dynamodb:PutItem` permission
- An EC2 instance role does not have `ssm:UpdateInstanceInformation` for Systems Manager

## Related Errors

- [AWS S3 Access Denied]({{< relref "/cloud/aws/s3-access-denied" >}}) — S3-specific access denied.
- [AWS IAM Error]({{< relref "/cloud/aws/iam-error" >}}) — IAM authorization failures.
- [GCP Permission Denied]({{< relref "/cloud/gcp/permission-denied10" >}}) — GCP equivalent.
