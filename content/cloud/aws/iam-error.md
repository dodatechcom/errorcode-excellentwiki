---
title: "AWS IAM Error: Not Authorized to Perform"
description: "IAM: not authorized to perform — Fix AWS IAM permission and authorization errors."
cloud: ["aws"]
error-types: ["api-error"]
severities: ["error"]
tags: ["aws", "iam", "not-authorized", "permissions", "policy", "role"]
weight: 5
---

The `not authorized to perform: iam:X` error occurs when an AWS identity attempts an IAM operation (e.g., `iam:CreateUser`, `iam:AttachRolePolicy`) without the required IAM permissions. IAM permissions are separate from the permissions of the service being managed.

## Common Causes

- The IAM user/role does not have `iam:*` permissions for the specific action
- A permission boundary restricts the effective permissions
- The IAM policy references resources (user/role ARNs) that do not exist or are wrong
- The action is not allowed by any attached policy

## How to Fix

Check the effective permissions for the identity:

```bash
# List attached policies for a user
aws iam list-attached-user-policies --user-name <username>

# List inline policies
aws iam list-user-policies --user-name <username>

# Check what the identity can do
aws iam simulate-principal-policy \
  --policy-source-arn arn:aws:iam::123456789012:user/<username> \
  --action-names iam:CreateUser iam:AttachRolePolicy
```

Grant IAM permissions:

```bash
aws iam put-role-policy \
  --role-name admin-role \
  --policy-name IAMFullAccess \
  --policy-document '{
    "Version": "2012-10-17",
    "Statement": [
      {
        "Effect": "Allow",
        "Action": "iam:*",
        "Resource": "*"
      }
    ]
  }'
```

For least-privilege, scope to specific resources:

```bash
aws iam put-role-policy \
  --role-name deployment-role \
  --policy-name CreateServiceRole \
  --policy-document '{
    "Version": "2012-10-17",
    "Statement": [
      {
        "Effect": "Allow",
        "Action": ["iam:CreateRole", "iam:AttachRolePolicy"],
        "Resource": "arn:aws:iam::123456789012:role/myapp-*"
      }
    ]
  }'
```

## Examples

- A deployment user tries to create a new IAM role but only has `iam:ListRoles`
- Terraform cannot create an EC2 instance profile because it lacks `iam:PassRole`
- A Lambda function cannot assume a role because it lacks `sts:AssumeRole`

## Related Errors

- [AWS AccessDenied]({{< relref "/cloud/aws/access-denied" >}}) — generic AWS access denied.
- [AWS S3 AccessDenied]({{< relref "/cloud/aws/s3-access-denied2" >}}) — S3-specific access denied.
- [Azure Auth Failed]({{< relref "/cloud/azure/auth-failed" >}}) — Azure authentication failure.
