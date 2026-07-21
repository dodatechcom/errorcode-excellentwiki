---
title: "[Solution] AWS RDS DB Instance Not Found"
description: "DBInstanceNotFound when the specified RDS instance does not exist."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `RDS DB Instance Not Found` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- Instance identifier is incorrect
- Instance was deleted
- Instance is in a different region
- IAM role lacks rds:DescribeDBInstances permission

## How to Fix

### Describe instances

```bash
aws rds describe-db-instances --db-instance-identifier my-db
```
### List all instances

```bash
aws rds describe-db-instances --query "DBInstances[*].[DBInstanceIdentifier,DBInstanceStatus,Engine]" --output table
```
### Check region

```bash
aws rds describe-db-instances --db-instance-identifier my-db --region us-west-2
```

## Examples

- Identifier my-db but actual name is mydb
- Instance my-old-db deleted last week

## Related Errors

- [RDS Error]({{< relref "/cloud/aws/aws-rds-error" >}}) -- General RDS errors
- [Instance Limit]({{< relref "/cloud/aws/aws-rds-instance-limit" >}}) -- Instance limits
