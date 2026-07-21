---
title: "[Solution] AWS IAM Role Not Found"
description: "NoSuchEntity when the specified IAM role does not exist."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `IAM Role Not Found` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- Role name or ARN is incorrect
- Role was deleted
- Role in different AWS account
- IAM user lacks iam:GetRole permission

## How to Fix

### Get role

```bash
aws iam get-role --role-name my-role
```
### List roles

```bash
aws iam list-roles --query "Roles[*].[RoleName,CreateDate]" --output table
```
### Create role

```bash
aws iam create-role --role-name my-role --assume-role-policy-document file://trust-policy.json
```

## Examples

- Calling get-role with my-role but role is named myrole
- Role deleted last week

## Related Errors

- [IAM Error]({{< relref "/cloud/aws/aws-iam-error" >}}) -- General IAM errors
- [Policy Not Found]({{< relref "/cloud/aws/aws-iam-policy-not-found" >}}) -- Policy not found
