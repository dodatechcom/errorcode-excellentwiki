---
title: "[Solution] AWS DocumentDB Error — cluster/replica/connection failures"
description: "Fix AWS DocumentDB errors. Resolve cluster, replica, and connection issues."
error-types: ["api-error"]
severities: ["error"]
weight: 143
---

An AWS DocumentDB error occurs when cluster endpoints are unreachable, replicas lag, or connections fail. Amazon DocumentDB provides MongoDB-compatible database but has specific networking and connection requirements.

## Common Causes

- Cluster is in stopped state
- Connection string uses wrong port (27017 vs 8192)
- Security group blocks DocumentDB traffic
- Replica lag exceeds application tolerance
- TLS not enabled on connection

## How to Fix

### Check Cluster Status

```bash
aws docdb describe-db-clusters \
  --query 'DBClusters[*].{ID:DBClusterIdentifier,Status:Status,Endpoint:Endpoint}'
```

### Check Instances

```bash
aws docdb describe-db-instances \
  --db-cluster-identifier my-docdb-cluster \
  --query 'DBInstances[*].{ID:DBInstanceIdentifier,Status:DBInstanceStatus,Class:DBInstanceClass}'
```

### Create Cluster

```bash
aws docdb create-db-cluster \
  --db-cluster-identifier my-docdb-cluster \
  --engine docdb \
  --master-username admin \
  --master-user-password mypassword123
```

### Create Read Replica

```bash
aws docdb create-db-instance \
  --db-instance-identifier my-docdb-replica \
  --db-instance-class db.r5.large \
  --engine docdb \
  --db-cluster-identifier my-docdb-cluster
```

### Modify Cluster

```bash
aws docdb modify-db-cluster \
  --db-cluster-identifier my-docdb-cluster \
  --backup-retention-period 14
```

## Examples

```bash
# Example 1: Connection refused
# MongoDBError: Connection refused on port 27017
# Fix: use correct port 8192 for DocumentDB

# Example 2: Replica lag
# ReplicaLag: Read replica lag exceeds threshold
# Fix: increase instance size or reduce write load
```

## Related Errors

- [AWS RDS Error]({{< relref "/cloud/aws/aws-rds-error" >}}) — RDS database errors
- [AWS VPC Error]({{< relref "/cloud/aws/vpc-error" >}}) — VPC connectivity errors
- [AWS EC2 Error]({{< relref "/cloud/aws/aws-ec2-error" >}}) — EC2 instance errors
