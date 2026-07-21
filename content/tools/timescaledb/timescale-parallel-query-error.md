---
title: "[Solution] TimescaleDB Parallel Query Error — How to Fix"
description: "Fix TimescaleDB parallel query errors by resolving parallel worker failures, fixing chunk-level parallelism, and handling parallel aggregation issues"
tools: ["timescaledb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# TimescaleDB Parallel Query Error

TimescaleDB parallel query errors occur when parallel query execution on hypertables fails due to worker limits, chunk-level restrictions, or incompatible parallel plans.

## Why It Happens

- Max parallel workers per gather is too low
- Small chunks do not benefit from parallel execution
- Parallel query plan is not chosen by the optimizer
- Worker process crashes during execution
- Parallel aggregation produces incorrect results
- Memory per worker is insufficient

## Common Error Messages

```
ERROR: could not launch parallel worker
```

```
ERROR: parallel worker failed
```

```
WARNING: parallel query not used
```

```
ERROR: out of memory in parallel worker
```

## How to Fix It

### 1. Configure Parallel Workers

```sql
-- Check parallel settings
SHOW max_parallel_workers_per_gather;
SHOW max_parallel_workers;
SHOW max_worker_processes;

-- Increase parallel workers
ALTER SYSTEM SET max_parallel_workers_per_gather = 4;
ALTER SYSTEM SET max_parallel_workers = 8;
ALTER SYSTEM SET max_worker_processes = 16;
SELECT pg_reload_conf();
```

### 2. Force Parallel Query

```sql
-- Force parallel execution with hint
SELECT /*+ Parallel(sensor_data 4) */
  device_id, AVG(value)
FROM sensor_data
WHERE time > NOW() - INTERVAL '1 day'
GROUP BY device_id;

-- Set minimum parallel table scan size
SET min_parallel_table_scan_size = '8MB';
```

### 3. Fix Parallel Worker Memory

```sql
-- Increase memory per worker
SET max_parallel_maintenance_workers = 4;

-- Increase work_mem for parallel operations
SET parallel_tuple_cost = 0.01;
SET parallel_setup_cost = 100;
```

### 4. Monitor Parallel Execution

```sql
-- Check if parallel workers are being used
EXPLAIN (ANALYZE, BUFFERS)
SELECT device_id, AVG(value)
FROM sensor_data
WHERE time > NOW() - INTERVAL '1 day'
GROUP BY device_id;

-- Check worker usage
SELECT * FROM pg_stat_progress_create_index;
```

## Common Scenarios

- **Parallel workers not being used**: Check min_parallel_table_scan_size and cost settings.
- **Parallel worker crashes**: Increase memory limits and check for OOM.
- **Parallel query is slower**: Small datasets may not benefit from parallelism.

## Prevent It

- Configure parallel worker settings appropriately for the hardware
- Use EXPLAIN ANALYZE to verify parallel plans
- Monitor worker process health

## Related Pages

- [TimescaleDB Query Error](/tools/timescaledb/timescale-query-error)
- [TimescaleDB OOM Query Error](/tools/timescaledb/timescale-oom-query-error)
- [TimescaleDB Config Error](/tools/timescaledb/timescale-config-error)
