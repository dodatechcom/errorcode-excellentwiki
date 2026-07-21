---
title: "[Solution] AWS RDS Multi-AZ Failover"
description: "FailoverError when Multi-AZ failover fails."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `RDS Multi-AZ Failover` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- Standby unsynchronized
- Replication stall
- Network partition

## How to Fix

### Reboot with failover

```bash
aws rds reboot-db-instance --db-instance-identifier mydb --force-failover
```

## Examples

- Example scenario: standby unsynchronized
- Example scenario: replication stall
- Example scenario: network partition

## Related Errors

- [AWS RDS Error]({{< relref "/cloud/aws/aws-rds-error" >}}) -- General rds errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
