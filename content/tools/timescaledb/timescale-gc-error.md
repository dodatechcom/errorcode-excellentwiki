---
title: "[Solution] TimescaleDB GC Error — How to Fix"
description: "Fix TimescaleDB garbage collection errors by resolving dead row accumulation, fixing autovacuum failures, and handling chunk cleanup issues"
tools: ["timescaledb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# TimescaleDB GC Error

TimescaleDB garbage collection errors occur when dead rows, old chunk data, or obsolete catalog entries are not properly cleaned up, leading to disk bloat and performance degradation.

## Why It Happens

- Autovacuum is disabled or too slow for hypertables
- Dead rows accumulate faster than they can be cleaned
- Chunk deletion leaves orphaned catalog entries
- VACUUM FULL is not run periodically on compressed chunks
- Background worker for cleanup is not running
- Transaction ID wraparound prevention fails

## Common Error Messages

```
WARNING: dead row count exceeds threshold
```

```
ERROR: could not remove orphaned chunks
```

```
WARNING: autovacuum not keeping up
```

```
ERROR: transaction ID wraparound imminent
```

## How to Fix It

### 1. Enable and Configure Autovacuum

```sql
-- Check autovacuum settings
SHOW autovacuum;
SHOW autovacuum_vacuum_threshold;
SHOW autovacuum_vacuum_scale_factor;

-- Enable autovacuum for the hypertable
ALTER TABLE sensor_data SET (
  autovacuum_enabled = on,
  autovacuum_vacuum_threshold = 50,
  autovacuum_vacuum_scale_factor = 0.1
);

-- Force manual vacuum
VACUUM sensor_data;
```

### 2. Run VACUUM on Compressed Chunks

```sql
-- Decompress, vacuum, then recompress
SELECT decompress_chunk('sensor_data_2024_01_chunk');
VACUUM sensor_data_2024_01_chunk;
SELECT compress_chunk('sensor_data_2024_01_chunk');

-- Or vacuum the parent table
VACUUM ANALYZE sensor_data;
```

### 3. Clean Up Orphaned Chunks

```sql
-- Check for orphaned chunks
SELECT chunk_name
FROM _timescaledb_catalog.chunk c
WHERE NOT EXISTS (
  SELECT 1 FROM pg_class
  WHERE relname = c.chunk_name
);

-- Clean up orphaned catalog entries
SELECT _timescaledb_internal.drop_orphaned_chunks();
```

### 4. Monitor GC Health

```sql
-- Check dead row count
SELECT
  schemaname, relname,
  n_dead_tup, n_live_tup,
  last_vacuum, last_autovacuum
FROM pg_stat_user_tables
WHERE relname LIKE 'sensor_data_%'
ORDER BY n_dead_tup DESC;

-- Check transaction ID age
SELECT
  datname,
  age(datfrozenxid) AS xid_age
FROM pg_database
WHERE datname = current_database();
```

## Common Scenarios

- **Disk usage keeps growing despite deletes**: Autovacuum is not running; enable and configure it.
- **VACUUM is slow on large chunks**: Vacuum chunks individually before they grow too large.
- **Transaction ID wraparound warning**: Run VACUUM FREEZE on the oldest tables immediately.

## Prevent It

- Enable autovacuum for all hypertables
- Schedule regular VACUUM ANALYZE during maintenance windows
- Monitor dead row counts and transaction ID age

## Related Pages

- [TimescaleDB Chunk Error](/tools/timescaledb/timescale-chunk-error)
- [TimescaleDB Retention Error](/tools/timescaledb/timescaledb-retention-error)
- [TimescaleDB Compression Error](/tools/timescaledb/timescale-compression-error)
