---
title: "[Solution] AWS RDS Maintenance Window"
description: "InvalidMaintenanceWindow for scheduling."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `RDS Maintenance Window` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- Window less than 30 min
- Not in UTC

## How to Fix

### Change window

```bash
aws rds modify-db-instance --db-instance-identifier mydb --preferred-maintenance-window mon:03:00-mon:04:30
```

## Examples

- Example scenario: window less than 30 min
- Example scenario: not in utc

## Related Errors

- [AWS RDS Error]({{< relref "/cloud/aws/aws-rds-error" >}}) -- General rds errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
