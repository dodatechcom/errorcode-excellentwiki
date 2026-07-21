---
title: "[Solution] TimescaleDB Migrate Error — How to Fix"
description: "Fix TimescaleDB migration errors by resolving schema transfer failures, fixing version upgrade issues, and handling data migration conflicts"
tools: ["timescaledb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# TimescaleDB Migrate Error

TimescaleDB migration errors occur when migrating from standard PostgreSQL to TimescaleDB, upgrading between TimescaleDB versions, or moving hypertables between clusters.

## Why It Happens

- Target database does not have the TimescaleDB extension
- Schema differences between source and target
- Hypertable metadata is not properly transferred
- Extension version mismatch between source and target
- Data type incompatibilities between PostgreSQL versions
- Backup format is incompatible with restore process

## Common Error Messages

```
ERROR: timescaledb extension not found
```

```
ERROR: hypertable metadata mismatch
```

```
ERROR: migration version conflict
```

```
ERROR: could not restore hypertable
```

## How to Fix It

### 1. Prepare Target Database

```sql
-- Install TimescaleDB extension on target
CREATE EXTENSION IF NOT EXISTS timescaledb CASCADE;

-- Verify extension
SELECT extname, extversion
FROM pg_extension
WHERE extname = 'timescaledb';
```

### 2. Migrate Schema and Data

```bash
# Dump schema only
pg_dump -s -h source -U postgres mydb > schema.sql

# Dump data
pg_dump -h source -U postgres -Fc mydb > data.dump

# Restore on target
psql -h target -U postgres -d mydb -f schema.sql
pg_restore -h target -U postgres -d mydb -Fc data.dump
```

### 3. Recreate Hypertables on Target

```sql
-- If hypertable metadata is lost, recreate them
-- First check if table is already a hypertable
SELECT * FROM timescaledb_information.hypertables
WHERE hypertable_name = 'sensor_data';

-- If not, convert it
SELECT create_hypertable('sensor_data', 'time');
```

### 4. Fix Version Upgrade Issues

```sql
-- Check current version
SELECT extversion FROM pg_extension
WHERE extname = 'timescaledb';

-- Upgrade extension
ALTER EXTENSION timescaledb UPDATE;

-- If upgrade fails, check for stuck migrations
SELECT * FROM _timescaledb_catalog.timescaledb_version;
```

## Common Scenarios

- **pg_restore fails on hypertable**: The target must have TimescaleDB extension installed before restore.
- **Hypertable loses metadata after migration**: Re-run create_hypertable to register the table.
- **Version mismatch after upgrade**: Run ALTER EXTENSION timescaledb UPDATE on all databases.

## Prevent It

- Install TimescaleDB extension before restoring backups
- Match TimescaleDB versions between source and target
- Test migration process on a staging cluster first

## Related Pages

- [TimescaleDB Upgrade Error](/tools/timescaledb/timescale-upgrade-error)
- [TimescaleDB Extension Error](/tools/timescaledb/timescale-extension-error)
- [TimescaleDB Restore Error](/tools/timescaledb/timescale-restore-error)
