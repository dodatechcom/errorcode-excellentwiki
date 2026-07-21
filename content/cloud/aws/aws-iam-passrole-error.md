---
title: "[Solution] AWS IAM PassRole Error"
description: "AccessDenied when PassRole restriction prevents passing a role."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `IAM PassRole Error` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- iam:PassRole permission not granted
- Role ARN does not match resource constraint
- PassRole wildcard restricted by org policy
- Role cannot be passed to the service

## How to Fix

### Check permission

```bash
aws iam simulate-principal-policy --policy-source-arn arn:aws:iam::123456789012:role/my-role --action-names iam:PassRole --resource-arns arn:aws:iam::123456789012:role/my-role
```
### Grant PassRole

```bash
aws iam put-role-policy --role-name caller-role --policy-name PassRolePolicy --policy-document file://passrole.json
```

## Examples

- Lambda role lacks iam:PassRole
- PassRole resource is * but org policy restricts it

## Related Errors

- [IAM Error]({{< relref "/cloud/aws/aws-iam-error" >}}) -- General IAM errors
- [AssumeRole Error]({{< relref "/cloud/aws/aws-iam-assume-role-error" >}}) -- AssumeRole
