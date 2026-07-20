---
title: "[Solution] AWS ElastiCache Error — Redis/Memcached connection/failover failures"
description: "Fix AWS ElastiCache errors. Resolve Redis and Memcached connection, failover, and cluster issues."
error-types: ["api-error"]
severities: ["error"]
weight: 134
---

An AWS ElastiCache error occurs when cache connections fail, Redis failover does not complete, or Memcached nodes become unreachable. ElastiCache provides managed caching but requires proper networking and configuration.

## Common Causes

- Cache subnet group has no available subnets
- Security group does not allow cache port (6379/11211)
- Redis cluster node failure during failover
- Connection pool exhaustion in application
- Parameter group incompatible with engine version

## How to Fix

### Check Cache Cluster Status

```bash
aws elasticache describe-cache-clusters \
  --query 'CacheClusters[*].{ID:CacheClusterId,Status:CacheClusterStatus,Node:CacheNodeType}'
```

### Describe Replication Group

```bash
aws elasticache describe-replication-groups \
  --replication-group-id my-redis
```

### Test Connectivity

```bash
aws elasticache describe-cache-security-groups \
  --cache-security-group-name default
```

### Create Cache Cluster

```bash
aws elasticache create-cache-cluster \
  --cache-cluster-id my-memcached \
  --cache-node-type cache.t3.micro \
  --engine memcached \
  --num-cache-nodes 2
```

### Modify Parameter Group

```bash
aws elasticache modify-cache-parameter-group \
  --cache-parameter-group-name default.redis7 \
  --parameter-name-values ParameterName=maxmemory-policy,ParameterValue=allkeys-lru
```

## Examples

```bash
# Example 1: Connection refused
# ERR Connection refused to cache cluster
# Fix: verify security group allows traffic on port 6379

# Example 2: Failover stuck
# Status: modifying, FailoverStatus: in-progress
# Fix: wait for failover to complete or check node health
```

## Related Errors

- [AWS EC2 Error]({{< relref "/cloud/aws/aws-ec2-error" >}}) — EC2 instance errors
- [AWS VPC Error]({{< relref "/cloud/aws/vpc-error" >}}) — VPC connectivity errors
- [AWS RDS Error]({{< relref "/cloud/aws/aws-rds-error" >}}) — RDS database errors
