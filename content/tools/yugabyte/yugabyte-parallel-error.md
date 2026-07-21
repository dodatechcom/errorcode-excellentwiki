---
title: "[Solution] YugabyteDB Parallel Error — How to Fix"
description: "Fix YugabyteDB parallel query errors by resolving parallel execution failures, fixing worker allocation issues, and handling parallel scan problems"
tools: ["yugabyte"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# YugabyteDB Parallel Error

YugabyteDB parallel errors occur when parallel query execution fails due to worker allocation issues, memory constraints, or incompatible query plans.

## Why It Happens

- Max parallel workers are not configured
- Memory per parallel worker is insufficient
- Query plan does not support parallel execution
- Parallel workers exceed the available worker pool
- Tablet-level parallelism conflicts with query-level parallelism
- Network latency between tablet servers slows parallel operations

## Common Error Messages

```
ERROR: could not launch parallel worker
```

```
ERROR: parallel worker process crashed
```

```
WARNING: parallel query not used
```

```
ERROR: insufficient resources for parallel query
```

## How to Fix It

### 1. Configure Parallel Workers

```sql
-- Check parallel settings
SHOW max_parallel_workers_per_gather;
SHOW max_parallel_workers;
SHOW max_worker_processes;

-- Set parallel worker limits
SET max_parallel_workers_per_gather = 4;
SET max_parallel_workers = 8;
```

### 2. Fix Parallel Memory

```sql
-- Increase memory for parallel operations
SET work_mem = '128MB';

-- Adjust parallel cost settings
SET parallel_tuple_cost = 0.01;
SET parallel_setup_cost = 100;

-- Set maintenance work memory for parallel operations
SET maintenance_work_mem = '512MB';
```

### 3. Optimize Parallel Queries

```sql
-- Force parallel execution
SET force_parallel_mode = on;

-- Check if parallel is used
EXPLAIN (ANALYZE, BUFFERS)
SELECT device_id, AVG(value)
FROM sensor_data
WHERE time > NOW() - INTERVAL '1 day'
GROUP BY device_id;

-- Disable parallel for specific queries
SET max_parallel_workers_per_gather = 0;
```

### 4. Monitor Parallel Execution

```sql
-- Check worker usage
SELECT * FROM pg_stat_activity
WHERE query LIKE '%parallel%';

-- Check worker configuration
SHOW max_worker_processes;
```

## Common Scenarios

- **Parallel workers not being used**: Check cost settings and table size thresholds.
- **Parallel worker crashes**: Increase work_mem and memory limits.
- **Parallel query is slower**: Small queries may not benefit from parallelism.

## Prevent It

- Configure parallel settings appropriately for the hardware
- Test parallel query plans with EXPLAIN ANALYZE
- Monitor parallel worker usage

## Related Pages

- [YugabyteDB Query Error](/tools/yugabyte/yugabyte-query-error)
- [YugabyteDB Tablet Error](/tools/yugabyte/yugabyte-tablet-error)
- [YugabyteDB Config Error](/tools/yugabyte/yugabyte-config-error)
