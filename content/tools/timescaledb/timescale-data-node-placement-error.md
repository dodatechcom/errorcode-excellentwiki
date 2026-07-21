---
title: "[Solution] TimescaleDB Data Node Placement Error — How to Fix"
description: "Fix TimescaleDB data node placement errors by resolving chunk distribution conflicts, fixing placement policies, and handling node affinity issues"
tools: ["timescaledb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# TimescaleDB Data Node Placement Error

TimescaleDB data node placement errors occur when chunks cannot be placed on the intended data node due to placement policy conflicts, node availability issues, or distribution constraints.

## Why It Happens

- Data node is not attached to the distributed hypertable
- Placement policy restricts the target node
- Node is overloaded and rejects new chunk placement
- Replication factor exceeds available data nodes
- Chunk placement conflicts with existing data distribution
- Network partition prevents communication with data node

## Common Error Messages

```
ERROR: no available data node for chunk placement
```

```
ERROR: data node not attached to hypertable
```

```
ERROR: placement policy violation
```

```
ERROR: insufficient data nodes for replication factor
```

## How to Fix It

### 1. Check Data Node Status

```sql
-- List attached data nodes
SELECT * FROM timescaledb_information.data_nodes
WHERE hypertable_name = 'distributed_sensor';

-- Check data node health
SELECT * FROM pg_foreign_server;
```

### 2. Fix Placement Issues

```sql
-- Add a data node to the hypertable
SELECT attach_data_node('dn1', 'distributed_sensor');

-- Set placement policy to all nodes
SELECT set_chunk_time_interval('distributed_sensor', INTERVAL '7 days');

-- Check chunk distribution
SELECT chunk_name, data_nodes
FROM timescaledb_information.chunks
WHERE hypertable_name = 'distributed_sensor';
```

### 3. Adjust Replication Factor

```sql
-- Reduce replication factor if not enough nodes
ALTER DISTRIBUTION distributed_sensor
  SET (number_replicas = 1);

-- Add more data nodes
SELECT add_data_node('dn3', host => 'node3.example.com');

-- Verify replication factor
SELECT * FROM timescaledb_information.hypertables
WHERE hypertable_name = 'distributed_sensor';
```

### 4. Handle Node Failures

```sql
-- Check which chunks are affected
SELECT chunk_name, data_nodes
FROM timescaledb_information.chunks
WHERE hypertable_name = 'distributed_sensor'
  AND NOT 'dn1' = ANY(data_nodes);

-- Repair chunk placement
CALL rebalance_chunk('distributed_sensor', 'chunk_name');
```

## Common Scenarios

- **New chunk cannot be placed**: Add more data nodes or reduce replication factor.
- **Chunks not distributed evenly**: Use rebalance_chunk to redistribute.
- **Data node offline**: Bring the node back online or remove it from the hypertable.

## Prevent It

- Always have more data nodes than the replication factor
- Monitor data node health regularly
- Use placement policies appropriate for your workload

## Related Pages

- [TimescaleDB Data Node Error](/tools/timescaledb/timescale-data-node-error)
- [TimescaleDB Distributed Error](/tools/timescaledb/timescale-distributed-error)
- [TimescaleDB Multi-node Error](/tools/timescaledb/timescale-multinode-error)
