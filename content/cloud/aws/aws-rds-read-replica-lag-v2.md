---
title: "[Solution] AWS RDS Read Replica Lag"
description: "ReplicaLag too high causing issues."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `RDS Read Replica Lag` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- Replica slower than source
- Large write transactions
- Network latency

## How to Fix

### Check lag

```bash
aws rds describe-db-instances --db-instance-identifier mydb-replica --query ReadReplicaSourceDBInstanceIdentifier
```

## Examples

- Example scenario: replica slower than source
- Example scenario: large write transactions
- Example scenario: network latency

## Related Errors

- [AWS RDS Error]({{< relref "/cloud/aws/aws-rds-error" >}}) -- General rds errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
