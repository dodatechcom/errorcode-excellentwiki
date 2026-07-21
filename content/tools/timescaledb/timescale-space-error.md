---
title: "[Solution] TimescaleDB Space Error — How to Fix"
description: "Fix TimescaleDB space errors by resolving disk space exhaustion, fixing chunk storage bloat, and handling tablespace allocation issues"
tools: ["timescaledb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# TimescaleDB Space Error

TimescaleDB space errors occur when disk space is exhausted or insufficient for new chunks, compression operations, or background worker activities.

## Why It Happens

- Chunks accumulate without retention policies
- Compression is not enabled or configured properly
- WAL files accumulate faster than they are recycled
- Temporary files from operations consume disk space
- Backup files are stored on the same volume as data
- Tablespace is misconfigured or full

## Common Error Messages

```
ERROR: could not extend file
```

```
ERROR: no space left on device
```

```
ERROR: disk full
```

```
WARNING: chunk creation failed due to disk space
```

## How to Fix It

### 1. Check Disk Usage

```sql
-- Check total database size
SELECT pg_size_pretty(pg_database_size(current_database()));

-- Check hypertable sizes
SELECT
  hypertable_name,
  pg_size_pretty(hypertable_size(hypertable_name::regclass)) AS total_size
FROM timescaledb_information.hypertables;

-- Check chunk sizes
SELECT
  chunk_name,
  pg_size_pretty(pg_total_relation_size(chunk_name::regclass)) AS chunk_size
FROM timescaledb_information.chunks
WHERE hypertable_name = 'sensor_data';
```

### 2. Free Up Space

```sql
-- Drop old chunks
SELECT drop_chunks('sensor_data', older_than => INTERVAL '90 days');

-- Drop all chunks older than a date
SELECT drop_chunks('sensor_data',
  older_than => '2024-01-01'::TIMESTAMPTZ);

-- Check space after cleanup
SELECT pg_size_pretty(pg_database_size(current_database()));
```

### 3. Enable Compression

```sql
-- Enable compression on the hypertable
ALTER TABLE sensor_data SET (
  timescaledb.compress,
  timescaledb.compress_segmentby = 'device_id',
  timescaledb.compress_orderby = 'time'
);

-- Add compression policy
SELECT add_compression_policy('sensor_data', INTERVAL '7 days');
```

### 4. Add Retention Policy

```sql
-- Automatically drop old data
SELECT add_retention_policy('sensor_data', INTERVAL '180 days');

-- Check active policies
SELECT * FROM timescaledb_information.jobs
WHERE proc_name = 'policy_retention';
```

## Common Scenarios

- **Disk full after months of data**: Add retention policy and enable compression.
- **Chunk creation fails**: Check disk space and drop old chunks if needed.
- **WAL files fill disk**: Configure WAL archiving or increase wal_keep_size.

## Prevent It

- Set up retention policies before data accumulation
- Enable compression on all hypertables
- Monitor disk usage with alerts at 70% and 85%

## Related Pages

- [TimescaleDB Chunk Error](/tools/timescaledb/timescale-chunk-error)
- [TimescaleDB Drop Chunk Error](/tools/timescaledb/timescale-drop-chunk-error)
- [TimescaleDB Retention Error](/tools/timescaledb/timescaledb-retention-error)
