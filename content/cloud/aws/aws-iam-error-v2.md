---
title: "[Solution] AWS IAM — Access Denied policy denied"
description: "Fix AWS IAM Access Denied policy denied. Resolve IAM policy permission issues."
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

An IAM Access Denied policy denied error means an AWS identity lacks the required IAM policy permissions for the requested action. The request is authenticated but explicitly denied by an IAM policy.

## What This Error Means

AWS IAM evaluates all applicable policies (identity-based, resource-based, SCPs, permission boundaries) when processing an API request. If any explicit `Deny` statement matches the action and resource, the request is denied regardless of any `Allow` statements. The error message contains the ARN of the identity, the denied action, and the resource. This is the most common AWS authorization error and affects all AWS services.

## Common Causes

- IAM policy does not include an `Allow` statement for the required action
- An explicit `Deny` statement in any attached policy overrides all allows
- Permission boundary restricts the effective permissions
- Service Control Policy (SCP) denies the action at the organization level
- Resource-based policy on the target resource blocks the identity
- IAM policy condition keys do not match the request context

## How to Fix

### Check Policy Simulations

```bash
aws iam simulate-principal-policy \
  --policy-source-arn arn:aws:iam::123456789012:role/my-role \
  --action-names s3:GetObject s3:ListBucket
```

### List Attached Policies

```bash
aws iam list-attached-role-policies --role-name my-role
aws iam list-role-policies --role-name my-role
```

### Check for Explicit Deny

```bash
aws iam get-role-policy --role-name my-role --policy-name my-policy
```

### Grant Required Permissions

```json
{
  "Version": "2012-10-17",
  "Statement": [{
    "Effect": "Allow",
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

### Check Permission Boundary

```bash
aws iam get-role --role-name my-role --query 'Role.PermissionsBoundary'
```

### Review Access Advisor

```bash
aws iam generate-service-last-accessed-details --arn arn:aws:iam::123456789012:role/my-role
aws iam get-service-last-accessed-details --job-id <job-id>
```

## Related Errors

- [AWS S3 Error]({{< relref "/cloud/aws/aws-s3-error-v2" >}}) — S3 access denied
- [AWS Lambda Error]({{< relref "/cloud/aws/aws-lambda-error-v2" >}}) — Lambda runtime error
- [GCP IAM Error]({{< relref "/cloud/gcp/gcp-iam-error-v2" >}}) — GCP permission denied
