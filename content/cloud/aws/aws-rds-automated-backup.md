---
title: "[Solution] AWS RDS Automated Backup"
description: "AutomatedBackupDisabled error."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `RDS Automated Backup` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- Retention set to 0
- Not enabled on instance

## How to Fix

### Change retention

```bash
aws rds modify-db-instance --db-instance-identifier mydb --backup-retention-period 7
```

## Examples

- Example scenario: retention set to 0
- Example scenario: not enabled on instance

## Related Errors

- [AWS RDS Error]({{< relref "/cloud/aws/aws-rds-error" >}}) -- General rds errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
