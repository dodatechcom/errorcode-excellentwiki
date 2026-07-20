---
title: "[Solution] Redis Cluster Failover Timeout Error"
description: "How to fix Redis cluster failover timeout when automatic failover takes too long"
tools: ["redis"]
error-types: ["database-error"]
severities: ["error"]
---

## Causes

- Cluster nodes cannot agree on failover
- Network latency between nodes
- Not enough replicas to perform failover
- `cluster-node-timeout` set too low

## Fix

Check cluster node timeout:

```bash
redis-cli CONFIG GET cluster-node-timeout
```

Increase timeout:

```bash
redis-cli CONFIG SET cluster-node-timeout 15000
```

Check cluster state:

```bash
redis-cli CLUSTER NODES | grep -E "fail|fail?"
```

Force manual failover:

```bash
redis-cli CLUSTER FAILOVER
```

## Examples

```bash
# Check failover status
redis-cli CLUSTER INFO | grep cluster_state

# Trigger manual failover
redis-cli -h replica-host -p 7001 CLUSTER FAILOVER

# Check node timeout
redis-cli CONFIG GET cluster-node-timeout
```
