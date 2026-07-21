---
title: "TimescaleDB Distributed Hypertable Error"
description: "Distributed hypertable operation failure"
tools:
  - timescaledb
error-types: ["tool-error"]
severities: ["error"]
---
## Error Description
Distributed hypertable across data nodes is failing.

## Common Causes
- Data node unreachable
- Distribution policy error
- Chunk replication failed

## How to Fix
```sql
-- Check data nodes
SELECT * FROM timescaledb_information.data_nodes;

-- Check distributed hypertable
SELECT * FROM timescaledb_information.hypertables WHERE is_distributed;
```
n## Examples
```sql
-- Create distributed hypertable
SELECT create_distributed_hypertable('mytable', 'time',
  data_nodes => ARRAY['data_node_1', 'data_node_2']);
-- Check chunk distribution
SELECT * FROM timescaledb_information.chunks WHERE hypertable_name = 'mytable';
```

