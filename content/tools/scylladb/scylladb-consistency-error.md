---
title: "[Solution] ScyllaDB Consistency Error — How to Fix"
description: "Fix ScyllaDB consistency errors by configuring correct consistency levels, resolving insufficient replicas, and tuning timeout settings"
tools: ["scylladb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# ScyllaDB Consistency Error

ScyllaDB consistency errors occur when operations cannot satisfy the requested consistency level due to insufficient replicas or timeouts. Consistency levels control the trade-off between availability and data correctness.

## Why It Happens

- Requested consistency level requires more replicas than available
- Nodes are down and cannot respond to read/write requests
- Network latency causes replica responses to time out
- Consistency level is set too high for the current cluster topology
- Datacenter-aware routing sends requests to wrong DC
- Hinted handoff cannot satisfy the consistency level

## Common Error Messages

```
UnavailableError: Not enough replicas available for query at consistency QUORUM
```

```
ReadTimeout: Not enough replicas responded to meet consistency level LOCAL_QUORUM
```

```
WriteTimeout: Not enough replicas responded to meet consistency level EACH_QUORUM
```

```
ConsistencyError: Consistency level TWO requires 2 replicas, but only 1 is available
```

## How to Fix It

### 1. Check Available Replicas

```bash
# Check node status
nodetool status

# Verify replication factor
DESCRIBE KEYSPACE mykeyspace;

# Check replica placement
nodetool ring | grep -i mykeyspace
```

### 2. Set Appropriate Consistency Level

```cql
-- Use ONE for high availability (default)
SELECT * FROM users WHERE id = '1' USING CONSISTENCY ONE;

-- Use QUORUM for balanced consistency
SELECT * FROM users WHERE id = '1' USING CONSISTENCY QUORUM;

-- Use LOCAL_QUORUM for multi-datacenter
SELECT * FROM users WHERE id = '1' USING CONSISTENCY LOCAL_QUORUM;

-- Use ANY for write availability (lowest consistency)
INSERT INTO users (id, name) VALUES ('1', 'Alice') USING CONSISTENCY ANY;
```

### 3. Configure Default Consistency Level

```cql
-- Set session-level consistency
CONSISTENCY QUORUM;

-- Set per-query consistency
SELECT * FROM users WHERE id = '1' USING CONSISTENCY LOCAL_ONE;

-- Check current consistency level
CONSISTENCY;
```

```python
# Set consistency in driver
from cassandra import ConsistencyLevel

statement = SimpleStatement(
    "SELECT * FROM users WHERE id = '1'",
    consistency_level=ConsistencyLevel.LOCAL_QUORUM
)
```

### 4. Fix Replica Availability Issues

```bash
# Check if nodes are up
nodetool status | grep -E "^(UN|DN|UL|DL)"

# Force a node to join
nodetool join

# Check hinted handoff
nodetool statushints | grep -i hint

# Run repair to sync replicas
nodetool repair mykeyspace
```

## Common Scenarios

- **QUORUM fails with RF=3 and one node down**: Use LOCAL_QUORUM or ONE temporarily.
- **Multi-DC writes fail**: Use EACH_QUORUM to ensure quorum in each datacenter.
- **Read timeout on large partitions**: Increase read timeout or reduce consistency level.

## Prevent It

- Match consistency level to your availability requirements
- Use `LOCAL_QUORUM` for multi-datacenter deployments
- Monitor `UnavailableError` and `ReadTimeout` metrics

## Related Pages

- [ScyllaDB Replication Error](/tools/scylladb/scylladb-replication-error)
- [ScyllaDB Timeout Error](/tools/scylladb/scylladb-timeout-error)
- [ScyllaDB Node Error](/tools/scylladb/scylladb-node-error)
