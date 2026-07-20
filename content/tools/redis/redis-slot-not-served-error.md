---
title: "[Solution] Redis Slot Not Served Error"
description: "How to fix Redis error when a hash slot is not served by any node"
tools: ["redis"]
error-types: ["database-error"]
severities: ["error"]
---

## Causes

- Cluster node failed and its slots are unassigned
- Incomplete cluster setup
- Slot migration failed and left orphaned slots

## Fix

Check unassigned slots:

```bash
redis-cli CLUSTER INFO | grep cluster_slots_ok
redis-cli CLUSTER SLOTS
```

Assign orphaned slots:

```bash
redis-cli CLUSTER ADDSLOTS 0 1 2 3 ... 5460
```

Or use cluster management:

```bash
redis-cli --cluster reshard 127.0.0.1:7001
```

## Examples

```bash
# Check which slots are assigned
redis-cli CLUSTER SLOTS

# Add slots to a node
redis-cli CLUSTER ADDSLOTS 5000 5001 5002

# Check cluster state
redis-cli CLUSTER INFO
```
