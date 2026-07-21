---
title: "[Solution] AWS RDS Read Replica Lag"
description: "ReadReplicaLagError when read replicas fall behind."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `RDS Read Replica Lag` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- Heavy write traffic to primary
- Network latency between primary and replica
- Replica instance class too small
- Large transactions on primary

## How to Fix

### Check replica lag

```bash
aws rds describe-db-instances --db-instance-identifier my-replica --query "DBInstances[*].StatusInfos"
```
### Monitor lag

```bash
aws cloudwatch get-metric-statistics --namespace AWS/RDS --metric-name ReplicaLag --dimensions Name=DBInstanceIdentifier,Value=my-replica --start-time $(date -u -d "1 hour ago" +\%FT\%TZ) --end-time $(date -u +\%FT\%TZ) --period 60 --statistics Maximum
```
### Scale up replica

```bash
aws rds modify-db-instance --db-instance-identifier my-replica --db-instance-class db.r5.large --apply-immediately
```

## Examples

- Replica lag 300 seconds but threshold is 30
- Bulk inserts of 1M rows causing lag

## Related Errors

- [RDS Error]({{< relref "/cloud/aws/aws-rds-error" >}}) -- General RDS errors
- [Multi-AZ Failover]({{< relref "/cloud/aws/aws-rds-multi-az-failover" >}}) -- Failover
