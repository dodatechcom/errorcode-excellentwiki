---
title: "[Solution] AWS RDS IAM DB Auth"
description: "AccessDeniedException for IAM DB Auth."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `RDS IAM DB Auth` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- IAM DB Auth not enabled
- Resource ID mismatch

## How to Fix

### Check Auth

```bash
aws rds describe-db-instances --db-instance-identifier mydb --query IAMDatabaseAuthenticationEnabled
```

## Examples

- Example scenario: iam db auth not enabled
- Example scenario: resource id mismatch

## Related Errors

- [AWS RDS Error]({{< relref "/cloud/aws/aws-rds-error" >}}) -- General rds errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
