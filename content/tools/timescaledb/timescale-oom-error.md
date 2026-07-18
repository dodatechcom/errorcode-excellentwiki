---
title: "[Solution] TimescaleDB OOM Error — How to Fix"
description: "Fix TimescaleDB OOM errors by tuning memory settings, optimizing large queries, and configuring work_mem for hash operations"
tools: ["timescaledb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# TimescaleDB OOM Error

TimescaleDB OOM errors occur when PostgreSQL or TimescaleDB processes exceed memory limits. This is common with large aggregations, joins, or compression operations.

## Why It Happens

- Large aggregation query exceeds work_mem
- Compression operation uses excessive memory
- JOIN operation materializes large intermediate results
- Too many concurrent connections exhaust shared memory
- Continuous aggregate refresh uses too much memory
- Hash joins or sorts exceed memory limits

## Common Error Messages

```
ERROR: out of memory
```

```
ERROR: memory allocation failed
```

```
FATAL: could not allocate memory for buffer
```

```
ERROR: insufficient memory for sort operation
```

## How to Fix It

### 1. Tune Memory Settings

```sql
-- Check current memory settings
SHOW work_mem;
SHOW maintenance_work_mem;
SHOW shared_buffers;
SHOW effective_cache_size;

-- Increase work_mem for large queries
SET work_mem = '256MB';

-- Increase maintenance work_mem for operations
SET maintenance_work_mem = '2GB';
```

### 2. Fix Large Query OOM

```sql
-- BAD: full table aggregation without limits
SELECT AVG(temperature) FROM sensor_data;

-- GOOD: use chunk-aware aggregation
SELECT AVG(temperature)
FROM sensor_data
WHERE time > NOW() - INTERVAL '1 day';

-- Use LIMIT for large result sets
SELECT * FROM sensor_data ORDER BY time DESC LIMIT 1000;
```

### 3. Configure PostgreSQL Memory

```ini
# In postgresql.conf
shared_buffers = '4GB'
work_mem = '256MB'
maintenance_work_mem = '2GB'
effective_cache_size = '12GB'
huge_pages = try
```

```bash
# Restart PostgreSQL after memory changes
sudo systemctl restart postgresql
```

### 4. Optimize Compression Memory

```sql
-- Compress in smaller batches
DO $$
DECLARE
  chunk_rec RECORD;
BEGIN
  FOR chunk_rec IN
    SELECT chunk_schema, chunk_name
    FROM timescaledb_information.chunks
    WHERE hypertable_name = 'sensor_data'
    AND NOT is_compressed
  LOOP
    EXECUTE format('SELECT compress_chunk(%I.%I)',
      chunk_rec.chunk_schema, chunk_rec.chunk_name);
  END LOOP;
END $$;
```

## Common Scenarios

- **Dashboard query OOMs**: Add time range filters to reduce data scanned.
- **Compression OOM on large chunk**: Compress smaller time ranges.
- **Concurrent queries exhaust memory**: Reduce `work_mem` per connection.

## Prevent It

- Set `work_mem` based on available RAM divided by max_connections
- Always filter time-series queries with time range
- Monitor memory usage with `pg_stat_activity`

## Related Pages

- [TimescaleDB Query Error](/tools/timescaledb/timescale-query-error)
- [TimescaleDB Compression Error](/tools/timescaledb/timescale-compression-error)
- [TimescaleDB Config Error](/tools/timescaledb/timescale-config-error)
