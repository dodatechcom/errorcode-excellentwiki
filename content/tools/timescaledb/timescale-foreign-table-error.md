---
title: "[Solution] TimescaleDB Foreign Table Error — How to Fix"
description: "Fix TimescaleDB foreign table errors by resolving foreign data wrapper issues, fixing distributed table access, and handling remote query failures"
tools: ["timescaledb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# TimescaleDB Foreign Table Error

TimescaleDB foreign table errors occur when the foreign data wrapper (FDW) used for distributed hypertables fails to connect, query, or synchronize data with remote data nodes.

## Why It Happens

- Foreign server connection parameters are incorrect
- FDW extension is not installed or loaded
- Remote data node is unreachable
- Foreign table schema does not match the local schema
- FDW connection pool is exhausted
- SSL certificate verification fails on remote connection

## Common Error Messages

```
ERROR: foreign-data wrapper "timescaledb_fdw" not found
```

```
ERROR: could not connect to server
```

```
ERROR: foreign table schema mismatch
```

```
ERROR: FDW connection pool exhausted
```

## How to Fix It

### 1. Check FDW Extension

```sql
-- Verify FDW extension is installed
SELECT * FROM pg_extension
WHERE extname = 'timescaledb_fdw';

-- Install if missing
CREATE EXTENSION IF NOT EXISTS timescaledb_fdw;
```

### 2. Fix Foreign Server Configuration

```sql
-- Check foreign server options
SELECT srvname, srvoptions
FROM pg_foreign_server;

-- Create or update foreign server
CREATE SERVER dn1
  FOREIGN DATA WRAPPER timescaledb_fdw
  OPTIONS (host 'node1.example.com', port '5432', dbname 'tsdb');

-- Create user mapping
CREATE USER MAPPING FOR postgres
  SERVER dn1
  OPTIONS (user 'postgres', password 'secret');
```

### 3. Test Remote Connection

```sql
-- Test connection to data node
SELECT * FROM pg_foreign_server WHERE srvname = 'dn1';

-- Import foreign schema
IMPORT FOREIGN SCHEMA public
  LIMIT TO (sensor_data)
  FROM SERVER dn1
  INTO remote_schema;
```

### 4. Fix Schema Mismatch

```sql
-- Check local schema
\d sensor_data

-- Check remote schema via psql
-- psql -h node1 -c "\d sensor_data"

-- Drop and recreate foreign table with correct schema
DROP FOREIGN TABLE IF EXISTS remote_sensor_data;
CREATE FOREIGN TABLE remote_sensor_data (
  time TIMESTAMPTZ NOT NULL,
  device_id INT NOT NULL,
  value NUMERIC(10,2)
) SERVER dn1 OPTIONS (table_name 'sensor_data');
```

## Common Scenarios

- **FDW extension not found**: Create the timescaledb_fdw extension.
- **Cannot connect to remote node**: Check firewall rules and connection parameters.
- **Schema mismatch after DDL change**: Re-import the foreign schema.

## Prevent It

- Verify FDW extension is installed before creating distributed hypertables
- Test foreign server connectivity regularly
- Keep schema in sync across all nodes

## Related Pages

- [TimescaleDB Distributed Error](/tools/timescaledb/timescale-distributed-error)
- [TimescaleDB Data Node Error](/tools/timescaledb/timescale-data-node-error)
- [TimescaleDB Connection Error](/tools/timescaledb/timescale-connection-error)
