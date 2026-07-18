---
title: "[Solution] TimescaleDB Distributed Error — How to Fix"
description: "Fix TimescaleDB distributed hypertable errors by resolving shard placement, fixing cross-node queries, and handling distributed operations"
tools: ["timescaledb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# TimescaleDB Distributed Error

TimescaleDB distributed hypertable errors occur when operating on data spread across multiple data nodes. Distributed hypertables require careful configuration.

## Why It Happens

- Not enough data nodes for distributed hypertable
- Shard placement is uneven across data nodes
- Cross-node query fails due to network issues
- Data node version is incompatible with access node
- Distributed hypertable has too many chunks
- Replication factor exceeds available data nodes

## Common Error Messages

```
ERROR: insufficient data nodes for distributed hypertable
```

```
ERROR: distributed query failed on data node
```

```
ERROR: shard placement error
```

```
ERROR: distributed hypertable operation not supported
```

## How to Fix It

### 1. Verify Data Nodes

```sql
-- Check available data nodes
SELECT * FROM timescaledb_information.data_nodes;

-- Ensure at least 2 data nodes for distributed hypertable
-- Add data node if needed
SELECT add_data_node('data_node_1', host => '10.0.0.2');
SELECT add_data_node('data_node_2', host => '10.0.0.3');
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
  data_nodes => '{"data_node_1", "data_node_2"}',
  replication_factor => 2);
```

### 3. Fix Cross-Node Query Issues

```sql
-- Check query plan for distributed query
EXPLAIN ANALYZE
SELECT time_bucket('1 hour', time), count(*)
FROM distributed_events
WHERE time > NOW() - INTERVAL '1 day'
GROUP BY 1;

-- Force query to specific node if needed
SELECT * FROM distributed_events
WHERE time > NOW() - INTERVAL '1 hour'
AND device_id = 1;
```

### 4. Monitor Distributed Hypertable

```sql
-- Check chunk distribution across nodes
SELECT chunk_name, node_name
FROM timescaledb_information.chunks
WHERE hypertable_name = 'distributed_events';

-- Check data node health
SELECT * FROM timescaledb_information.data_nodes;

-- Monitor distributed query performance
SELECT * FROM pg_stat_statements
WHERE query LIKE '%distributed_events%';
```

## Common Scenarios

- **Not enough data nodes**: Add more data nodes before creating distributed hypertable.
- **Query fails on one node**: Check data node connectivity and health.
- **Uneven data distribution**: Use space partitioning for better distribution.

## Prevent It

- Ensure low-latency network between all data nodes
- Monitor data node health continuously
- Keep TimescaleDB versions consistent across nodes

## Related Pages

- [TimescaleDB Multinode Error](/tools/timescaledb/timescale-multinode-error)
- [TimescaleDB Data Node Error](/tools/timescaledb/timescale-data-node-error)
- [TimescaleDB Shard Error](/tools/timescaledb/timescale-shard-error)
