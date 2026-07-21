---
title: "[Solution] TimescaleDB Lock Error — How to Fix"
description: "Fix TimescaleDB lock errors by resolving lock conflicts on hypertables, fixing AccessExclusiveLock during DDL, and handling chunk-level locking"
tools: ["timescaledb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# TimescaleDB Lock Error

TimescaleDB lock errors occur when operations on hypertables encounter lock conflicts, typically during DDL changes, compression, or concurrent chunk operations.

## Why It Happens

- DDL operation requires AccessExclusiveLock on the hypertable
- Concurrent INSERT and compression operations conflict
- Chunk reorder holds a lock that blocks queries
- Background worker holds a lock during maintenance
- Long-running query prevents DDL from acquiring lock
- DROP CHUNKS conflicts with concurrent reads

## Common Error Messages

```
ERROR: lock timeout expired
```

```
ERROR: could not extend relation due to lock conflict
```

```
WARNING: lock not acquired within timeout
```

```
ERROR: concurrent operation not permitted
```

## How to Fix It

### 1. Check Lock Conflicts

```sql
-- Find blocking queries
SELECT
  blocked.pid AS blocked_pid,
  blocked.query AS blocked_query,
  blocking.pid AS blocking_pid,
  blocking.query AS blocking_query
FROM pg_stat_activity blocked
JOIN pg_locks bl ON bl.pid = blocked.pid AND NOT bl.granted
JOIN pg_locks kl ON kl.locktype = bl.locktype
  AND kl.relation = bl.relation
JOIN pg_stat_activity blocking ON blocking.pid = kl.pid
WHERE kl.granted;
```

### 2. Increase Lock Timeout

```sql
-- Set longer lock timeout for DDL
SET lock_timeout = '120s';

-- Perform the DDL operation
ALTER TABLE sensor_data ADD COLUMN notes TEXT;

-- Reset lock timeout
RESET lock_timeout;
```

### 3. Kill Blocking Queries

```sql
-- Cancel the blocking query
SELECT pg_cancel_backend(<blocking_pid>);

-- Or terminate it (use with caution)
SELECT pg_terminate_backend(<blocking_pid>);
```

### 4. Schedule DDL During Low Traffic

```sql
-- Check for active queries before DDL
SELECT pid, query, state, query_start
FROM pg_stat_activity
WHERE state = 'active'
  AND query NOT LIKE '%pg_stat_activity%';

-- Then perform DDL when no heavy queries are running
```

## Common Scenarios

- **DDL times out waiting for lock**: Kill long-running queries or increase lock_timeout.
- **Compression conflicts with INSERT**: Schedule compression during low-write periods.
- **Chunk operations block queries**: Use non-blocking operations or reduce chunk maintenance frequency.

## Prevent It

- Schedule DDL operations during maintenance windows
- Monitor lock conflicts regularly
- Use lock_timeout to avoid indefinite waits

## Related Pages

- [TimescaleDB DDL Error](/tools/timescaledb/timescaledb-ddl-error)
- [TimescaleDB Chunk Error](/tools/timescaledb/timescale-chunk-error)
- [TimescaleDB Compression Error](/tools/timescaledb/timescale-compression-error)
