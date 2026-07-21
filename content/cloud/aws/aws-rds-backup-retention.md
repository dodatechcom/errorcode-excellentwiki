---
title: "[Solution] AWS RDS Backup Retention"
description: "InvalidParameterValue for backup retention."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `RDS Backup Retention` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- Must be between 0 and 35 days
- Value 0 disables backups

## How to Fix

### Check retention

```bash
aws rds describe-db-instances --db-instance-identifier mydb --query DBInstances[*].BackupRetentionPeriod
```

### Modify

```bash
aws rds modify-db-instance --db-instance-identifier mydb --backup-retention-period 7
```

## Examples

- Example scenario: must be between 0 and 35 days
- Example scenario: value 0 disables backups

## Related Errors

- [AWS RDS Error]({{< relref "/cloud/aws/aws-rds-error" >}}) -- General rds errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
