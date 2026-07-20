---
title: "[Solution] Redis Cluster State Changed Error"
description: "How to handle Redis cluster state transitions between ok and fail"
tools: ["redis"]
error-types: ["database-error"]
severities: ["error"]
---

## Causes

- Node joining or leaving the cluster
- Network partition between nodes
- Node failure or recovery
- Resharding in progress

## Fix

Monitor cluster state:

```bash
watch -n 2 'redis-cli CLUSTER INFO | grep cluster_state'
```

Check node status:

```bash
redis-cli CLUSTER NODES
```

Wait for cluster to stabilize:

```bash
sleep 15 && redis-cli CLUSTER INFO | grep cluster_state
```

If cluster is in fail, check which nodes are down:

```bash
redis-cli CLUSTER NODES | grep "fail"
```

## Examples

```bash
# Monitor cluster changes
redis-cli CLUSTER INFO

# Check node connectivity
redis-cli CLUSTER NODES | grep -v "connected"

# Check cluster epoch
redis-cli CLUSTER INFO | grep cluster_current_epoch
```
