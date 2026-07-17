---
title: "[Solution] AWS IAM Access Denied — not authorized to perform"
description: "Fix AWS IAM access denied errors. Resolve IAM permission and authorization issues."
error-types: ["api-error"]
severities: ["error"]
weight: 5
---

An AWS Access Denied error occurs when an IAM identity (user, role, or service) attempts an action without the required IAM permissions.

## Common Causes

- IAM user/role does not have the required policy attached
- Permission boundary restricts effective permissions
- Resource-based policy blocks the action
- Condition keys in the policy do not match
- Service control policy (SCP) denies the action

## How to Fix

### Check Effective Permissions

```bash
aws iam simulate-principal-policy \
  --policy-source-arn arn:aws:iam::123456789012:user/myuser \
  --action-names s3:GetObject
```

### List Attached Policies

```bash
aws iam list-attached-user-policies --user-name myuser
aws iam list-user-policies --user-name myuser
```

### Grant Required Permission

```bash
aws iam put-role-policy \
  --role-name my-role \
  --policy-name S3Access \
  --policy-document '{
    "Version": "2012-10-17",
    "Statement": [{
      "Effect": "Allow",
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::my-bucket/*"
    }]
  }'
```

### Check IAM Access Analyzer

```bash
aws accessanalyzer list-findings --region us-east-1
```

## Examples

```bash
# Example 1: S3 access denied
aws s3 ls s3://my-bucket
# An error occurred (AccessDeniedException)
# Fix: add s3:ListBucket permission

# Example 2: EC2 launch denied
aws ec2 run-instances --image-id ami-xxx
# UnauthorizedOperation
# Fix: add ec2:RunInstances permission
```

## Related Errors

- [AWS S3 Error]({{< relref "/cloud/aws/aws-s3-error" >}}) — S3 access denied
- [GCP IAM Error]({{< relref "/cloud/gcp/gcp-iam-error" >}}) — GCP permission denied
