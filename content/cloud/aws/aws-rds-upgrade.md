---
title: "[Solution] AWS RDS Upgrade"
description: "UpgradeFailed when engine upgrade fails."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `RDS Upgrade` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- Major requires reboot
- PostgreSQL heuristic failure

## How to Fix

### Describe instance

```bash
aws rds describe-db-instances --db-instance-identifier mydb
```

## Examples

- Example scenario: major requires reboot
- Example scenario: postgresql heuristic failure

## Related Errors

- [AWS RDS Error]({{< relref "/cloud/aws/aws-rds-error" >}}) -- General rds errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
