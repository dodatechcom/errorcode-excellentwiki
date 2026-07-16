---
title: "CLUSTERDOWN The cluster is down"
description: "Redis Cluster refuses commands because one or more hash slots are not covered by any node"
tools: ["redis"]
error-types: ["database-error"]
severities: ["error"]
tags: ["cluster", "sharding", "slots", "availability"]
weight: 5
---

This error occurs when a Redis Cluster is in a degraded state and some hash slots are not served by any node. The cluster refuses writes and possibly reads until the slots are covered.

## Common Causes

- A cluster node failed and slots are not reassigned
- Slot migration between nodes is incomplete
- Not enough master nodes to cover all 16384 hash slots
- Cluster is still in the process of recovering from a failover

## How to Fix

1. Check cluster status:

```bash
redis-cli CLUSTER INFO
```

2. Verify slot coverage:

```bash
redis-cli CLUSTER SLOTS
```

3. Fix by ensuring enough nodes cover all slots:

```bash
redis-cli CLUSTER REPLICATE <node-id>
```

4. Wait for automatic slot migration to complete, or manually reassign slots:

```bash
redis-cli CLUSTER SETSLOT <slot> NODE <node-id>
```

## Examples

```bash
redis-cli CLUSTER INFO
# cluster_state:fail
# cluster_slots_assigned:16382
# cluster_slots_ok:16382
# cluster_slots_pfail:0
# cluster_slots_fail:2
# (error) CLUSTERDOWN The cluster is down
```

## Related Errors

- [ERR Client sent AUTH but no password is set](/tools/redis/auth-error2)
