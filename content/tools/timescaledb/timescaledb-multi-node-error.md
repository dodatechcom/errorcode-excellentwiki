---
title: "TimescaleDB Multi-Node Error"
description: "Multi-node cluster operation failure"
tools:
  - timescaledb
error-types: ["tool-error"]
severities: ["error"]
---
## Error Description
Multi-node TimescaleDB cluster operation is failing.

## Common Causes
- Access node unavailable
- Data node disconnected
- Network partition

## How to Fix
```sql
-- Check cluster status
SELECT * FROM timescaledb_information.data_nodes;

-- Reconnect data node
SELECT attach_data_node('data_node_1', 'host1', 5432);
```

## Examples
```sql
-- Check data node health
SELECT * FROM timescaledb_information.data_nodes WHERE node_type = 'data';
-- Detach and reattach
SELECT detach_data_node('data_node_1');
SELECT attach_data_node('data_node_1', 'host1', 5432);
```

