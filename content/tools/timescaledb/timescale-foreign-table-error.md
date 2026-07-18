---
title: "[Solution] TimescaleDB Foreign Table Error — How to Fix"
description: "Fix TimescaleDB foreign table errors by resolving FDW connection failures, fixing import schema issues, and handling distributed query problems"
tools: ["timescaledb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# TimescaleDB Foreign Table Error

TimescaleDB foreign table errors occur when using PostgreSQL Foreign Data Wrappers (FDW) to access data from external sources within TimescaleDB.

## Why It Happens

- Foreign server connection is not established
- FDW extension is not installed
- Schema import fails for foreign tables
- Foreign table data types are incompatible
- FDW connection times out
- Foreign table is used in hypertable creation

## Common Error Messages

```
ERROR: foreign server does not exist
```

```
ERROR: could not connect to foreign server
```

```
ERROR: schema import failed
```

```
ERROR: foreign table cannot be hypertable
```

## How to Fix It

### 1. Configure Foreign Data Wrapper

```sql
-- Install FDW extension
CREATE EXTENSION IF NOT EXISTS postgres_fdw;

-- Create foreign server
CREATE SERVER foreign_db
  FOREIGN DATA WRAPPER postgres_fdw
  OPTIONS (host '10.0.0.2', port '5432', dbname 'remote_db');

-- Create user mapping
CREATE USER MAPPING FOR local_user
  SERVER foreign_db
  OPTIONS (user 'remote_user', password 'remote_password');
```

### 2. Import Foreign Schema

```sql
-- Import all tables from foreign server
IMPORT FOREIGN SCHEMA public
  LIMIT TO (sensor_data)
  FROM SERVER foreign_db
  INTO local_schema;

-- Import with filter
IMPORT FOREIGN SCHEMA public
  FROM SERVER foreign_db
  INTO local_schema
  OPTIONS (import_default => 'false');
```

### 3. Query Foreign Tables

```sql
-- Query foreign table directly
SELECT * FROM local_schema.sensor_data
WHERE time > NOW() - INTERVAL '1 day';

-- Use in joins
SELECT l.time, l.temperature, r.humidity
FROM local_schema.sensor_data l
JOIN foreign_schema.sensor_readings r
  ON l.time = r.time AND l.sensor_id = r.sensor_id;
```

### 4. Fix Foreign Table Issues

```sql
-- Check foreign server status
SELECT * FROM pg_foreign_server;

-- Check user mappings
SELECT * FROM pg_user_mappings;

-- Refresh foreign table schema
IMPORT FOREIGN SCHEMA public
  FROM SERVER foreign_db
  INTO local_schema;
```

## Common Scenarios

- **Foreign server unreachable**: Check network connectivity and pg_hba.conf on remote server.
- **Schema import fails**: Ensure FDW extension is installed on both local and remote servers.
- **Foreign table cannot be hypertable**: Copy data to local table first, then create hypertable.

## Prevent It

- Test foreign server connectivity regularly
- Use connection pooling for frequent FDW queries
- Monitor FDW query performance

## Related Pages

- [TimescaleDB Query Error](/tools/timescaledb/timescale-query-error)
- [TimescaleDB Connection Error](/tools/timescaledb/timescale-connection-error)
- [TimescaleDB Config Error](/tools/timescaledb/timescale-config-error)
