---
title: "[Solution] TimescaleDB Multinode Error — How to Fix"
description: "Fix TimescaleDB multinode errors by resolving distributed hypertable issues, fixing data node connectivity, and correcting shard configuration"
tools: ["timescaledb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# TimescaleDB Multinode Error

TimescaleDB multinode errors occur when configuring or operating distributed hypertables across multiple data nodes. Multinode requires Enterprise license.

## Why It Happens

- Data node is not accessible from access node
- Shard creation fails due to disk space on data nodes
- Distributed hypertable has too many data nodes
- Network latency between access and data nodes
- Data node version is incompatible
- Multinode features require Enterprise license

## Common Error Messages

```
ERROR: data node is not available
```

```
ERROR: distributed hypertable creation failed
```

```
ERROR: insufficient data nodes for replication
```

```
ERROR: multinode requires Enterprise license
```

## How to Fix It

### 1. Add Data Nodes

```sql
-- Add a data node
SELECT add_data_node('data_node_1',
  host => '10.0.0.2',
  port => 5432,
  dbname => 'timescaledb');

-- Check data node status
SELECT * FROM timescaledb_information.data_nodes;

-- Verify connectivity
SELECT * FROM timescaledb_information.data_nodes
WHERE node_name = 'data_node_1';
```

### 2. Create Distributed Hypertable

```sql
-- Create distributed hypertable
CREATE TABLE distributed_events (
  time TIMESTAMPTZ NOT NULL,
  device_id INTEGER NOT NULL,
  data JSONB
);

SELECT create_distributed_hypertable('distributed_events', 'time',
  data_nodes => '{"data_node_1", "data_node_2", "data_node_3"}');
```

### 3. Fix Data Node Issues

```sql
-- Remove unhealthy data node
SELECT delete_data_node('data_node_1');

-- Re-add data node
SELECT add_data_node('data_node_1',
  host => '10.0.0.2',
  port => 5432);

-- Refresh data node configuration
SELECT refresh_data_node_configuration('data_node_1');
```

### 4. Monitor Distributed Hypertable

```sql
-- Check chunk distribution
SELECT * FROM timescaledb_information.chunks
WHERE hypertable_name = 'distributed_events';

-- Check data node health
SELECT * FROM timescaledb_information.data_nodes;

-- Check distributed hypertable stats
SELECT hypertable_name, num_chunks
FROM timescaledb_information.hypertables
WHERE hypertable_name = 'distributed_events';
```

## Common Scenarios

- **Data node goes down**: Remove and re-add the node, then rebalance chunks.
- **Shard creation fails**: Ensure all data nodes have sufficient disk space.
- **Query fails across nodes**: Check network connectivity between access and data nodes.

## Prevent It

- Monitor data node health with `timescaledb_information.data_nodes`
- Ensure low-latency network between access and data nodes
- Use at least 3 data nodes for redundancy

## Related Pages

- [TimescaleDB Data Node Error](/tools/timescaledb/timescale-data-node-error)
- [TimescaleDB Access Node Error](/tools/timescaledb/timescale-access-node-error)
- [TimescaleDB Replication Error](/tools/timescaledb/timescale-replication-error)
