---
title: "[Solution] TimescaleDB Data Node Error — How to Fix"
description: "Fix TimescaleDB data node errors by resolving connectivity issues, fixing node join failures, and recovering from data node crashes"
tools: ["timescaledb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# TimescaleDB Data Node Error

TimescaleDB data node errors occur when individual data nodes in a distributed hypertable cluster fail, become unreachable, or have configuration issues.

## Why It Happens

- Data node PostgreSQL is down or not accepting connections
- Network firewall blocks inter-node communication
- Data node disk space is full
- Extension version mismatch between access and data nodes
- pg_hba.conf rejects connections from access node
- Data node has too many concurrent connections

## Common Error Messages

```
ERROR: could not connect to data node
```

```
ERROR: data node connection failed
```

```
ERROR: data node version mismatch
```

```
FATAL: connection limit exceeded on data node
```

## How to Fix It

### 1. Check Data Node Status

```sql
-- Check all data nodes
SELECT * FROM timescaledb_information.data_nodes;

-- Test specific data node connection
SELECT * FROM timescaledb_information.data_nodes
WHERE node_name = 'data_node_1';
```

### 2. Fix Connectivity Issues

```bash
# Test data node connectivity from access node
psql -h 10.0.0.2 -p 5432 -U tsdbadmin -d timescaledb

# Check pg_hba.conf on data node
cat /etc/postgresql/*/main/pg_hba.conf | grep -v "^#" | grep -v "^$"

# Add access node to data node pg_hba.conf
# host  all  all  10.0.0.1/32  md5
```

### 3. Fix Data Node Configuration

```sql
-- Remove and re-add data node
SELECT delete_data_node('data_node_1');

SELECT add_data_node('data_node_1',
  host => '10.0.0.2',
  port => 5432,
  dbname => 'timescaledb');

-- Ensure extensions match on both nodes
-- On data node:
CREATE EXTENSION IF NOT EXISTS timescaledb;
```

### 4. Monitor Data Node Health

```bash
# Check data node disk space
ssh data_node_1 "df -h /var/lib/postgresql/data"

# Check data node connections
ssh data_node_1 "psql -c 'SELECT count(*) FROM pg_stat_activity;'"

# Check data node replication lag
ssh data_node_1 "psql -c 'SELECT * FROM pg_stat_replication;'"
```

## Common Scenarios

- **Data node unreachable**: Check firewall rules and PostgreSQL authentication.
- **Extension version mismatch**: Upgrade TimescaleDB on data node to match access node.
- **Data node disk full**: Free space or add storage to the data node.

## Prevent It

- Monitor data node health with automated checks
- Keep TimescaleDB versions consistent across all nodes
- Set up pg_hba.conf rules for inter-node communication

## Related Pages

- [TimescaleDB Multinode Error](/tools/timescaledb/timescale-multinode-error)
- [TimescaleDB Access Node Error](/tools/timescaledb/timescale-access-node-error)
- [TimescaleDB Connection Error](/tools/timescaledb/timescale-connection-error)
