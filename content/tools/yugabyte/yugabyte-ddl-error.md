---
title: "[Solution] YugabyteDB DDL Error — How to Fix"
description: "Fix YugabyteDB DDL errors by resolving CREATE TABLE failures, fixing ALTER TABLE issues, and handling index creation problems"
tools: ["yugabyte"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# YugabyteDB DDL Error

YugabyteDB DDL errors occur when Data Definition Language operations like CREATE TABLE, ALTER TABLE, or DROP TABLE fail in a distributed environment.

## Why It Happens

- DDL operation times out waiting for tablet creation
- Master cannot allocate tablets for new table
- Index creation fails due to tablet split conflicts
- ALTER TABLE is blocked by long-running transactions
- Table already exists when creating without IF NOT EXISTS
- DDL operation fails on one TServer in the cluster

## Common Error Messages

```
ERROR: CREATE TABLE timed out
```

```
ERROR: could not create tablet for table
```

```
ERROR: ALTER TABLE failed - operation in progress
```

```
ERROR: index creation failed
```

## How to Fix It

### 1. Create Tables Correctly

```sql
-- Use IF NOT EXISTS
CREATE TABLE IF NOT EXISTS sensor_data (
  sensor_id UUID NOT NULL,
  event_time TIMESTAMPTZ NOT NULL,
  temperature DOUBLE PRECISION,
  PRIMARY KEY (sensor_id, event_time)
) WITH (replicas = 3);

-- Create table with hash sharding
CREATE TABLE users (
  user_id UUID DEFAULT gen_random_uuid(),
  name TEXT,
  email TEXT
) SPLIT INTO 10 TABLETS;
```

### 2. Fix DDL Timeout

```bash
# Increase DDL timeout
# In tserver.gflags:
--ysql_pg_conf_csv=statement_timeout=120000

# Or set per session
SET statement_timeout = '120s';
```

### 3. Create Indexes

```sql
-- Create index on table
CREATE INDEX idx_sensor_time ON sensor_data (event_time);

-- Create unique index
CREATE UNIQUE INDEX idx_users_email ON users (email);

-- Create partial index
CREATE INDEX idx_active_users ON users (email) WHERE active = true;
```

### 4. Monitor DDL Operations

```bash
# Check active DDL operations
/home/yugabyte/master/bin/yb-admin list_tables

# Monitor DDL in Master logs
grep "DDL" /home/yugabyte/yugabyte-data/master/logs/yb-master.INFO | tail -10
```

## Common Scenarios

- **CREATE TABLE times out**: Ensure all Master and TServer nodes are running.
- **ALTER TABLE blocked**: Kill long-running transactions that hold locks.
- **Index creation fails**: Check available disk space on all TServers.

## Prevent It

- Use IF NOT EXISTS/IF EXISTS for DDL operations
- Run DDL operations during low-traffic periods
- Monitor DDL completion with Master logs

## Related Pages

- [YugabyteDB Query Error](/tools/yugabyte/yugabyte-query-error)
- [YugabyteDB DML Error](/tools/yugabyte/yugabyte-dml-error)
- [YugabyteDB Tablet Error](/tools/yugabyte/yugabyte-tablet-error)
