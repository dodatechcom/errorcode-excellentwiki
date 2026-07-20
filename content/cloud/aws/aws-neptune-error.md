---
title: "[Solution] AWS Neptune Error — graph/cluster/query failures"
description: "Fix AWS Neptune errors. Resolve graph database cluster, query, and endpoint issues."
error-types: ["api-error"]
severities: ["error"]
weight: 142
---

An AWS Neptune error occurs when graph queries fail, cluster endpoints are unreachable, or database connections timeout. Neptune provides managed graph database but requires proper cluster and query configuration.

## Common Causes

- Neptune cluster is in stopped state
- IAM role lacks Neptune or S3 permissions
- Query timeout exceeds Neptune limits
- Database subnet group has insufficient subnets
- Gremlin/Cypher query syntax errors

## How to Fix

### Check Cluster Status

```bash
aws neptune describe-db-clusters \
  --query 'DBClusters[*].{ID:DBClusterIdentifier,Status:Status,Endpoint:Endpoint}'
```

### Check DB Instances

```bash
aws neptune describe-db-instances \
  --query 'DBInstances[*].{ID:DBInstanceIdentifier,Status:DBInstanceStatus,Class:DBInstanceClass}'
```

### Start Cluster

```bash
aws neptune start-db-cluster \
  --db-cluster-identifier my-neptune-cluster
```

### Create Snapshot

```bash
aws neptune create-db-cluster-snapshot \
  --db-cluster-identifier my-neptune-cluster \
  --db-cluster-snapshot-id my-snapshot
```

### Modify Cluster

```bash
aws neptune modify-db-cluster \
  --db-cluster-identifier my-neptune-cluster \
  --backup-retention-period 14
```

## Examples

```bash
# Example 1: Cluster stopped
# DBClusterNotFoundError: Cluster is not available
# Fix: start the cluster with start-db-cluster

# Example 2: Query timeout
# GremlinTimeoutException: Query exceeded time limit
# Fix: optimize query or increase timeout
```

## Related Errors

- [AWS RDS Error]({{< relref "/cloud/aws/aws-rds-error" >}}) — RDS database errors
- [AWS VPC Error]({{< relref "/cloud/aws/vpc-error" >}}) — VPC connectivity errors
- [AWS IAM Error]({{< relref "/cloud/aws/aws-iam-error" >}}) — IAM permission errors
