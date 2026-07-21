---
title: "[Solution] TimescaleDB Dist Hypertable Attach Error — How to Fix"
description: "Fix TimescaleDB distributed hypertable attach errors by resolving data node connection failures, fixing chunk distribution, and handling attach conflicts"
tools: ["timescaledb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# TimescaleDB Dist Hypertable Attach Error

TimescaleDB distributed hypertable attach errors occur when attaching data nodes to a distributed hypertable fails due to connectivity, schema mismatch, or configuration issues.

## Why It Happens

- Data node is not reachable from the access node
- Schema on the data node does not match the access node
- Hypertable does not exist on the target data node
- Network firewall blocks inter-node communication
- Data node is already attached to a different distributed hypertable
- Replication factor exceeds the number of available data nodes

## Common Error Messages

```
ERROR: could not connect to data node
```

```
ERROR: schema mismatch between nodes
```

```
ERROR: data node already attached
```

```
ERROR: hypertable not found on data node
```

## How to Fix It

### 1. Check Data Node Connectivity

```sql
-- Test connection to data node
SELECT * FROM pg_foreign_server WHERE srvname = 'dn1';

-- Check data node health
SELECT node_name, is_available
FROM timescaledb_information.data_nodes;

-- Test with pg_basebackup or psql
-- psql -h node1.example.com -p 5432 -U postgres
```

### 2. Verify Schema Consistency

```sql
-- Check table schema on both nodes
-- Access node:
\d sensor_data

-- Data node:
-- psql -h node1 -c "\d sensor_data"

-- Create matching hypertable on data node if needed
SELECT create_hypertable('sensor_data', 'time');
```

### 3. Attach Data Node

```sql
-- Attach a new data node
SELECT attach_data_node('dn1', 'distributed_sensor');

-- Verify attachment
SELECT * FROM timescaledb_information.data_nodes
WHERE hypertable_name = 'distributed_sensor';

-- Check data node options
SELECT srvoptions FROM pg_foreign_server
WHERE srvname = 'dn1';
```

### 4. Fix Attach Conflicts

```sql
-- Detach node from wrong hypertable first
SELECT detach_data_node('dn1', 'other_hypertable');

-- Now attach to the correct one
SELECT attach_data_node('dn1', 'distributed_sensor');

-- Distribute existing chunks
SELECT redistribute_data('distributed_sensor');
```

## Common Scenarios

- **Cannot connect to data node**: Check firewall rules and ensure the port is open.
- **Schema mismatch after DDL change**: Run schema updates on all data nodes.
- **Node attach times out**: Check network latency and increase timeout settings.

## Prevent It

- Ensure all data nodes have the same schema before distributing
- Test connectivity between all nodes before deployment
- Use consistent PostgreSQL versions across all nodes

## Related Pages

- [TimescaleDB Distributed Error](/tools/timescaledb/timescale-distributed-error)
- [TimescaleDB Data Node Error](/tools/timescaledb/timescale-data-node-error)
- [TimescaleDB Multi-node Error](/tools/timescaledb/timescale-multinode-error)
