---
title: "[Solution] TimescaleDB Hypertable Rename Error — How to Fix"
description: "Fix TimescaleDB hypertable rename errors by resolving name conflicts, fixing dependent object references, and handling distributed hypertable renames"
tools: ["timescaledb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# TimescaleDB Hypertable Rename Error

TimescaleDB hypertable rename errors occur when renaming a hypertable fails due to naming conflicts, dependent objects, or distributed hypertable restrictions.

## Why It Happens

- New name conflicts with an existing table
- Continuous aggregates reference the old table name
- Views or functions depend on the old name
- Policies reference the hypertable by name
- Distributed hypertable rename not supported
- Another schema has a table with the same name

## Common Error Messages

```
ERROR: relation "new_name" already exists
```

```
ERROR: cannot rename hypertable referenced by continuous aggregate
```

```
ERROR: rename not supported for distributed hypertable
```

```
ERROR: must be owner of hypertable
```

## How to Fix It

### 1. Check for Conflicts

```sql
-- Check if new name already exists
SELECT * FROM information_schema.tables
WHERE table_name = 'new_sensor_data';

-- Check what depends on the current hypertable
SELECT dependent_ns.nspname || '.' || dependent_view.relname
FROM pg_depend
JOIN pg_rewrite ON pg_rewrite.evclass = pg_depend.objid
JOIN pg_class dependent_view ON pg_rewrite.ev_class = dependent_view.oid
JOIN pg_namespace dependent_ns ON dependent_view.relnamespace = dependent_ns.oid
JOIN pg_class source_table ON pg_depend.refobjid = source_table.oid
WHERE source_table.relname = 'sensor_data';
```

### 2. Rename Hypertable Safely

```sql
-- Rename the hypertable
ALTER TABLE sensor_data RENAME TO new_sensor_data;

-- Verify the rename
SELECT * FROM timescaledb_information.hypertables
WHERE hypertable_name = 'new_sensor_data';
```

### 3. Update Dependent Objects

```sql
-- Update continuous aggregate view definition
DROP MATERIALIZED VIEW avg_hourly;
CREATE MATERIALIZED VIEW avg_hourly
WITH (timescaledb.continuous) AS
SELECT
  time_bucket('1 hour', time) AS bucket,
  AVG(temperature) AS avg_temp
FROM new_sensor_data
GROUP BY bucket;

-- Update views
DROP VIEW v_sensor_summary;
CREATE VIEW v_sensor_summary AS
SELECT * FROM new_sensor_data WHERE temperature > 30;
```

### 4. Handle Distributed Hypertables

```sql
-- For distributed hypertables, rename on access node only
-- This may not propagate to all data nodes

-- Alternative: create new hypertable and migrate data
CREATE TABLE new_distributed_sensor (LIKE distributed_sensor INCLUDING ALL);
SELECT create_distributed_hypertable('new_distributed_sensor', 'time');
INSERT INTO new_distributed_sensor SELECT * FROM distributed_sensor;
```

## Common Scenarios

- **Rename fails with dependent objects**: Drop the dependent views/continuous aggregates first, rename, then recreate.
- **Distributed hypertable cannot be renamed**: Create a new hypertable and migrate the data.
- **Rename conflicts with existing table**: Choose a different name or drop the conflicting table.

## Prevent It

- Use descriptive names from the start to avoid future renames
- Document hypertable dependencies before making changes
- Test renames in a staging environment first

## Related Pages

- [TimescaleDB Hypertable Error](/tools/timescaledb/timescale-hypertable-error)
- [TimescaleDB DDL Error](/tools/timescaledb/timescaledb-ddl-error)
- [TimescaleDB Continuous Aggregate Error](/tools/timescaledb/timescale-continuous-aggregate-error)
