---
title: "[Solution] TimescaleDB OOM Query Error — How to Fix"
description: "Fix TimescaleDB OOM query errors by resolving out-of-memory failures during queries, fixing hash join memory limits, and handling large result set processing"
tools: ["timescaledb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# TimescaleDB OOM Query Error

TimescaleDB OOM query errors occur when individual queries consume excessive memory, causing the PostgreSQL OOM killer to terminate the backend process.

## Why It Happens

- Hash join on large hypertable data exceeds work_mem
- Gapfill function materializes entire time range in memory
- Continuous aggregate refresh query is too large
- Sort operation on unindexed columns uses too much memory
- Aggregate function over too many rows without partitioning
- COPY operation with large batch size exhausts memory

## Common Error Messages

```
ERROR: out of memory
```

```
FATAL: server process (PID) was terminated by exception
```

```
ERROR: could not allocate memory for sort
```

```
ERROR: memory allocation failed
```

## How to Fix It

### 1. Adjust Work Memory

```sql
-- Check current work_mem
SHOW work_mem;

-- Increase for current session
SET work_mem = '256MB';

-- Increase globally
ALTER SYSTEM SET work_mem = '128MB';
SELECT pg_reload_conf();
```

### 2. Optimize Memory-Intensive Queries

```sql
-- Replace hash join with merge join
SELECT /*+ MergeJoin(a b) */ a.*, b.*
FROM sensor_data a
JOIN device_info b ON a.device_id = b.id
WHERE a.time > NOW() - INTERVAL '1 day';

-- Use subquery to reduce data before join
SELECT a.*, b.*
FROM (
  SELECT * FROM sensor_data
  WHERE time > NOW() - INTERVAL '1 day'
) a
JOIN device_info b ON a.device_id = b.id;
```

### 3. Reduce Result Set Size

```sql
-- Add LIMIT to reduce memory usage
SELECT * FROM sensor_data
WHERE time > NOW() - INTERVAL '1 day'
LIMIT 10000;

-- Paginate large result sets
SELECT * FROM sensor_data
WHERE time > NOW() - INTERVAL '1 day'
ORDER BY time
LIMIT 1000 OFFSET 0;
```

### 4. Fix COPY Memory Issues

```bash
# Reduce COPY batch size
psql -c "\copy sensor_data FROM 'data.csv' CSV HEADER"
# Instead of loading all at once, split the file:
split -l 100000 data.csv chunk_
for f in chunk_*; do
  psql -c "\copy sensor_data FROM '$f' CSV"
done
```

## Common Scenarios

- **Query killed by OOM**: Reduce work_mem or optimize the query to process less data.
- **Gapfill uses too much memory**: Reduce the time range in the gapfill window.
- **COPY fails with OOM**: Split the data file into smaller batches.

## Prevent It

- Set appropriate work_mem for the workload
- Add LIMIT clauses to exploratory queries
- Monitor query memory usage in pg_stat_activity

## Related Pages

- [TimescaleDB OOM Error](/tools/timescaledb/timescale-oom-error)
- [TimescaleDB Query Error](/tools/timescaledb/timescale-query-error)
- [TimescaleDB Timeout Error](/tools/timescaledb/timescale-timeout-error)
