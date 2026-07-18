---
title: "[Solution] ScyllaDB Replication Error — How to Fix"
description: "Fix ScyllaDB replication errors by correcting replication factor settings, resolving data inconsistency, and fixing node-level replication failures"
tools: ["scylladb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# ScyllaDB Replication Error

ScyllaDB replication errors occur when data fails to replicate across nodes in the cluster. Replication ensures data durability and availability across multiple nodes.

## Why It Happens

- Replication factor exceeds available nodes
- Network partition prevents replica communication
- Node is down and cannot accept writes
- Snitch configuration does not match datacenter topology
- Keyspace replication strategy is misconfigured
- Hinted handoff queue is full

## Common Error Messages

```
UnavailableError: Not enough replicas available for query at consistency QUORUM
```

```
WriteTimeout: Operation timed out for table - received only 0 of 3 expected responses
```

```
OverloadedError: Too many in-flight requests
```

```
UnavailabilityError: Failed to connect to 10.0.0.2:9042
```

## How to Fix It

### 1. Verify Replication Factor

```cql
-- Check keyspace replication
DESCRIBE KEYSPACE mykeyspace;

-- Fix replication factor
ALTER KEYSPACE mykeyspace WITH replication = {
  'class': 'NetworkTopologyStrategy',
  'dc1': 3,
  'dc2': 3
};

-- Check replication status
nodetool status
```

### 2. Run Repair to Fix Inconsistencies

```bash
# Full repair
nodetool repair mykeyspace

# Repair specific table
nodetool repair mykeyspace mytable

# Repair with specific parallelism
nodetool repair -pr mykeyspace

# Schedule regular repairs (before gc_grace_seconds)
```

### 3. Fix Hinted Handoff

```bash
# Check hint queue status
nodetool tpstats | grep -i hint

# Increase hint window
# In scylla.yaml:
# hinted_handoff_timeout_in_ms: 10000
# max_hint_window_in_ms: 10800000  # 3 hours

# Replay hints after node recovery
nodetool statushints
```

### 4. Configure Multi-DC Replication

```cql
-- Multi-datacenter replication
ALTER KEYSPACE mykeyspace WITH replication = {
  'class': 'NetworkTopologyStrategy',
  'us-east': 3,
  'eu-west': 3
};

-- Use LOCAL_QUORUM for latency-sensitive operations
SELECT * FROM mytable USING CONSISTENCY LOCAL_QUORUM WHERE id = 'key1';
```

## Common Scenarios

- **Replication lag after node restart**: Run `nodetool repair` to sync data.
- **Writes fail with QUORUM**: Check that enough replicas are available in each datacenter.
- **Hinted handoff fills disk**: Monitor hint queue size and add nodes if needed.

## Prevent It

- Use `NetworkTopologyStrategy` for multi-datacenter deployments
- Schedule regular repairs with `nodetool repair`
- Monitor `WriteTimeout` and `ReadTimeout` metrics

## Related Pages

- [ScyllaDB Node Error](/tools/scylladb/scylladb-node-error)
- [ScyllaDB Streaming Error](/tools/scylladb/scylladb-streaming-error)
- [ScyllaDB Consistency Error](/tools/scylladb/scylladb-consistency-error)
