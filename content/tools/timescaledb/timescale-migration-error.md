---
title: "[Solution] TimescaleDB Migration Error — How to Fix"
description: "Fix TimescaleDB migration errors by resolving schema migration failures, fixing data migration issues, and handling version upgrade problems"
tools: ["timescaledb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# TimescaleDB Migration Error

TimescaleDB migration errors occur when migrating data between TimescaleDB versions, PostgreSQL versions, or converting regular tables to hypertables.

## Why It Happens

- Schema migration fails due to incompatible changes
- Data migration exceeds available disk space
- Migration script encounters locked tables
- Extension version mismatch between environments
- Continuous aggregate migration is incomplete
- Migration is interrupted by connection loss

## Common Error Messages

```
ERROR: migration script failed
```

```
ERROR: incompatible schema version
```

```
ERROR: disk space insufficient for migration
```

```
ERROR: table lock timeout during migration
```

## How to Fix It

### 1. Migrate Regular Table to Hypertable

```sql
-- Check if table can be converted
SELECT * FROM timescaledb_information.hypertables
WHERE hypertable_name = 'my_table';

-- Convert with data migration
SELECT create_hypertable('my_table', 'created_at',
  if_not_exists => TRUE,
  migrate_data => TRUE);

-- Monitor migration progress
SELECT * FROM timescaledb_information.jobs
WHERE proc_name = 'convert_to_hypertable';
```

### 2. Migrate Between PostgreSQL Versions

```bash
# Use pg_upgrade for major version upgrades
# 1. Stop PostgreSQL
sudo systemctl stop postgresql

# 2. Run pg_upgrade
pg_upgrade \
  --old-datadir=/var/lib/postgresql/14/main \
  --new-datadir=/var/lib/postgresql/16/main \
  --old-bindir=/usr/lib/postgresql/14/bin \
  --new-bindir=/usr/lib/postgresql/16/bin

# 3. Install TimescaleDB on new version
sudo systemctl start postgresql
psql -d timescaledb -c "CREATE EXTENSION IF NOT EXISTS timescaledb;"
```

### 3. Migrate Continuous Aggregates

```sql
-- Export continuous aggregate definitions
SELECT view_name, view_definition
FROM timescaledb_information.continuous_aggregates;

-- Drop old continuous aggregate
DROP MATERIALIZED VIEW daily_summary;

-- Recreate on new version
CREATE MATERIALIZED VIEW daily_summary
WITH (timescaledb.continuous) AS
SELECT
  time_bucket('1 day', time) AS bucket,
  sensor_id,
  AVG(temperature) AS avg_temp
FROM sensor_data
GROUP BY bucket, sensor_id
WITH NO DATA;

-- Rebuild data
CALL refresh_continuous_aggregate('daily_summary', NULL, NULL);
```

### 4. Validate Migration

```sql
-- Compare row counts
SELECT 'source' as env, count(*) FROM source_db.sensor_data
UNION ALL
SELECT 'target' as env, count(*) FROM target_db.sensor_data;

-- Verify hypertable structure
SELECT * FROM timescaledb_information.hypertables;

-- Test queries on migrated data
SELECT time_bucket('1 hour', time), avg(temperature)
FROM sensor_data
WHERE time > NOW() - INTERVAL '1 day'
GROUP BY 1;
```

## Common Scenarios

- **Migration times out on large tables**: Use `migrate_data => TRUE` for background migration.
- **Extension not found after migration**: Install TimescaleDB extension before data restore.
- **Continuous aggregate data lost**: Recreate and refresh aggregates after migration.

## Prevent It

- Test migrations on staging environment first
- Back up data before any migration
- Monitor migration progress with `timescaledb_information.jobs`

## Related Pages

- [TimescaleDB Upgrade Error](/tools/timescaledb/timescale-upgrade-error)
- [TimescaleDB Backup Error](/tools/timescaledb/timescale-backup-error)
- [TimescaleDB Restore Error](/tools/timescaledb/timescale-restore-error)
