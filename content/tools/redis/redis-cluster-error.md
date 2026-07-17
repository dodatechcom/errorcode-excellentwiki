---
title: "Redis Cluster Error"
description: "Redis cluster encounters issues with slot distribution, node communication, or failover."
tools: ["redis"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
---

# Redis Cluster Error

A Redis cluster error occurs when the Redis cluster encounters issues with slot distribution, node communication, or failover. Clusters provide horizontal scaling and high availability.

## Common Causes

- Node failure or unreachable
- Slot migration in progress
- Cluster configuration outdated
- Not enough master nodes for quorum

## How to Fix

### Check Cluster Status

```bash
redis-cli CLUSTER INFO
redis-cli CLUSTER NODES
```

### Check Slot Distribution

```bash
redis-cli CLUSTER SLOTS
```

### Fix Cluster Configuration

```bash
# Fix a node that lost its configuration
redis-cli CLUSTER MEET <ip> <port>
```

### Reshard Slots

```bash
redis-cli CLUSTER ADDSLOTS 0 1 2 3 4 5
redis-cli CLUSTER DELSLOTS 0 1 2 3 4 5
```

### Add New Node to Cluster

```bash
redis-cli CLUSTER MEET <new_node_ip> <new_node_port>
redis-cli CLUSTER REPLICATE <master_node_id>
```

### Fix Split-Brain

```bash
# Check cluster health
redis-cli CLUSTER INFO | grep cluster_state
# If cluster_state:fail, fix the failing nodes
```

## Examples

```bash
redis-cli CLUSTER INFO
cluster_state:fail
cluster_slots_assigned:16384
cluster_slots_ok:16383
cluster_slots_pfail:0
cluster_slots_fail:1
```

## Related Errors

- [Connection Error]({{< relref "/tools/redis/redis-connection-error" >}}) — connection failure
- [Sentinel Error]({{< relref "/tools/redis/redis-sentinel-error" >}}) — sentinel issues
