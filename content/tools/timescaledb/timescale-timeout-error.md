---
title: "[Solution] TimescaleDB Timeout Error — How to Fix"
description: "Fix TimescaleDB timeout errors by resolving query timeouts, fixing lock timeouts, and handling statement timeout configuration on hypertables"
tools: ["timescaledb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# TimescaleDB Timeout Error

TimescaleDB timeout errors occur when queries, locks, or background operations exceed their configured timeout limits, causing the operation to be cancelled.

## Why It Happens

- Statement timeout is too short for the workload
- Lock timeout expires during chunk operations
- Background worker operations time out on large chunks
- Network latency causes distributed query timeouts
- Deadlock detection timeout triggers too early
- Idle transaction timeout disconnects sessions

## Common Error Messages

```
ERROR: canceling statement due to statement timeout
```

```
ERROR: lock timeout expired
```

```
ERROR: canceling due to user request
```

```
WARNING: query timeout exceeded
```

## How to Fix It

### 1. Increase Statement Timeout

```sql
-- Check current timeout
SHOW statement_timeout;

-- Increase for current session
SET statement_timeout = '300s';

-- Increase globally
ALTER SYSTEM SET statement_timeout = '300s';
SELECT pg_reload_conf();

-- Increase for specific user
ALTER ROLE app_user SET statement_timeout = '600s';
```

### 2. Fix Lock Timeout

```sql
-- Check lock timeout
SHOW lock_timeout;

-- Increase lock timeout
SET lock_timeout = '120s';

-- Check for blocking locks
SELECT
  blocked_locks.pid AS blocked_pid,
  blocked_activity.usename AS blocked_user,
  blocking_locks.pid AS blocking_pid,
  blocking_activity.usename AS blocking_user
FROM pg_catalog.pg_locks blocked_locks
JOIN pg_catalog.pg_stat_activity blocked_activity
  ON blocked_activity.pid = blocked_locks.pid
JOIN pg_catalog.pg_locks blocking_locks
  ON blocking_locks.locktype = blocked_locks.locktype
  AND blocking_locks.relation = blocked_locks.relation
JOIN pg_catalog.pg_stat_activity blocking_activity
  ON blocking_activity.pid = blocking_locks.pid
WHERE NOT blocked_locks.granted;
```

### 3. Optimize Slow Queries

```sql
-- Check for slow queries
SELECT pid, query, state, query_start
FROM pg_stat_activity
WHERE state = 'active'
  AND NOW() - query_start > INTERVAL '10 seconds';

-- Kill long-running queries
SELECT pg_cancel_backend(pid);
```

### 4. Set Per-Operation Timeouts

```sql
-- Different timeout for compression
SET timescaledb.max_compress_chunk_time = '600s';

-- Different timeout for continuous aggregate refresh
CALL refresh_continuous_aggregate('hourly_avg',
  NOW() - INTERVAL '1 day', NOW());
SET statement_timeout = '0';
```

## Common Scenarios

- **Query times out on large dataset**: Increase statement_timeout or optimize the query.
- **Lock timeout during DDL**: Wait for blocking queries to finish or increase lock_timeout.
- **Background worker times out**: Increase the worker timeout or reduce the operation scope.

## Prevent It

- Set appropriate timeouts for different workload types
- Monitor slow queries and optimize them
- Use per-session timeouts for critical operations

## Related Pages

- [TimescaleDB Query Error](/tools/timescaledb/timescale-query-error)
- [TimescaleDB Connection Error](/tools/timescaledb/timescale-connection-error)
- [TimescaleDB Job Error](/tools/timescaledb/timescale-job-error)
