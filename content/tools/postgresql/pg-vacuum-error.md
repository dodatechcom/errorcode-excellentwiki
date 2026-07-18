---
title: "[Solution] PostgreSQL Autovacuum Cannot Keep Up Error — How to Fix"
description: "Fix PostgreSQL autovacuum not keeping up by tuning autovacuum parameters, increasing worker count, optimizing table statistics, and monitoring bloat"
tools: ["postgresql"]
error-types: ["database-error"]
severities: ["warning"]
weight: 5
comments: true
---

# PostgreSQL Autovacuum Cannot Keep Up Error

This error means the autovacuum worker processes are not able to clean up dead tuples fast enough, causing table bloat, transaction ID wraparound risk, and degraded query performance. Tables accumulate dead rows faster than autovacuum can remove them.

## Why It Happens

- Tables with very high write rates generate dead tuples faster than autovacuum processes them
- `autovacuum_max_workers` is too low for the number of busy tables
- `autovacuum_naptime` is too long, causing infrequent vacuum cycles
- Long-running transactions prevent vacuum from cleaning dead tuples (held by old snapshots)
- `autovacuum_vacuum_threshold` and `autovacuum_vacuum_scale_factor` are too conservative
- Heavy UPDATE workload on a few large tables concentrates work on one worker
- `autovacuum_work_mem` is too small, forcing multiple passes over the same table
- Table statistics are stale, causing bad query plans that increase write traffic

## Common Error Messages

```
WARNING: autovacuum: table "public.events" has no autovacuum workers
DETAIL: N dead tuples exceeds the configured autovacuum limit.
```

```
WARNING: oldest xmin needed by vacuum has moved past cutoff
DETAIL: Consider increasing autovacuum_max_workers or reducing autovacuum_naptime.
```

```
WARNING: transaction ID wraparound limit may soon be reached
HINT: Execute VACUUM FREEZE on critical tables.
```

## How to Fix It

### 1. Monitor Autovacuum Activity

```sql
-- Check autovacuum settings
SHOW autovacuum_max_workers;
SHOW autovacuum_naptime;
SHOW autovacuum_vacuum_threshold;
SHOW autovacuum_vacuum_scale_factor;

-- Monitor which tables have the most dead tuples
SELECT
    schemaname,
    relname,
    n_live_tup,
    n_dead_tup,
    round(n_dead_tup::numeric / greatest(n_live_tup, 1) * 100, 1) AS dead_pct,
    last_autovacuum,
    last_autoanalyze
FROM pg_stat_user_tables
WHERE n_dead_tup > 10000
ORDER BY n_dead_tup DESC;
```

### 2. Tune Autovacuum Per Table

```sql
-- For high-write tables, make autovacuum more aggressive
ALTER TABLE events SET (
    autovacuum_vacuum_scale_factor = 0.01,
    autovacuum_analyze_scale_factor = 0.005,
    autovacuum_vacuum_cost_delay = 2,
    autovacuum_vacuum_cost_limit = 1000
);
```

### 3. Increase Autovacuum Workers and Memory

```sql
-- Allow more parallel vacuum workers
ALTER SYSTEM SET autovacuum_max_workers = 6;

-- Run vacuum more frequently
ALTER SYSTEM SET autovacuum_naptime = '30s';

-- Give each worker more memory for vacuum operations
ALTER SYSTEM SET autovacuum_work_mem = '256MB';

SELECT pg_reload_conf();
```

### 4. Kill Long-Running Transactions

```sql
-- Find transactions that prevent vacuum cleanup
SELECT
    pid,
    usename,
    state,
    xact_start,
    now() - xact_start AS duration,
    query,
    backend_xmin
FROM pg_stat_activity
WHERE backend_xmin IS NOT NULL
ORDER BY xact_start;

-- Terminate long-running transactions
SELECT pg_terminate_backend(pid)
FROM pg_stat_activity
WHERE backend_xmin IS NOT NULL
  AND xact_start < now() - interval '1 hour';
```

### 5. Manual VACUUM FREEZE for Critical Tables

```sql
-- If wraparound is approaching, run manual vacuum
VACUUM FREEZE VERBOSE events;

-- Check current transaction ID and wraparound status
SELECT
    datname,
    age(datfrozenxid) AS xid_age,
    2^31 - age(datfrozenxid) AS remaining
FROM pg_database
ORDER BY xid_age DESC;
```

## Common Scenarios

- **Event logging table**: An events table with millions of inserts per day outpaces autovacuum. Set `autovacuum_vacuum_scale_factor = 0.01` on that table.
- **Abandoned script**: A forgotten psql session holds a snapshot, preventing all vacuum cleanup. Kill the idle session.
- **Wraparound warning**: Transaction IDs are approaching 2 billion. Run `VACUUM FREEZE` on the largest tables immediately.

## Prevent It

- Monitor `n_dead_tup` on high-write tables and set per-table autovacuum parameters
- Alert when `age(datfrozenxid)` exceeds 500 million on any database
- Keep long-running transactions under 5 minutes by using `statement_timeout`

## Related Pages

- [PostgreSQL Deadlock Detected](/tools/postgresql/pg-deadlock-detected)
- [PostgreSQL Connection Limit](/tools/postgresql/pg-connection-limit)
- [PostgreSQL Vacuum Error](/tools/postgresql/pg-vacuum-error)
