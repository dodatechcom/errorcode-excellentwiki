---
title: "[Solution] PostgreSQL Lock Timeout Expired - Fix Lock Wait Issues"
description: "Fix PostgreSQL lock timeout expired errors by analyzing lock conflicts, optimizing transaction scope, and configuring lock_timeout appropriately"
tools: ["postgresql"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
---

# PostgreSQL Lock Timeout Expired

A lock timeout error means a statement waited longer than the configured `lock_timeout` duration to acquire a lock and gave up. This is different from a deadlock -- there is no circular wait, just a long wait.

## What This Error Means

PostgreSQL returns this error when a statement cannot acquire the lock it needs within the timeout period:

```
ERROR: lock timeout expired
```

The `lock_timeout` setting limits how long a statement will wait for any lock (table-level or row-level). The default is 0 (no timeout), meaning statements wait indefinitely. When set, it prevents queries from blocking other queries for too long.

The timeout applies per lock acquisition attempt -- a single statement may need multiple locks and each one is checked separately.

## Why It Happens

- A long-running transaction holds an exclusive lock that blocks new operations
- A `LOCK TABLE` statement in another session prevents DDL or DML
- A `VACUUM` operation on a table blocks writes
- Schema migration (`ALTER TABLE`) requires an `ACCESS EXCLUSIVE` lock
- High concurrency causes many transactions to compete for the same row locks
- A `SELECT FOR UPDATE` is waiting for a row that is locked by another transaction
- An index build (`CREATE INDEX`) locks the table during certain phases

## How to Fix It

### 1. Check What Is Holding the Lock

```sql
-- See all current locks
SELECT
    l.locktype,
    l.relation::regclass,
    l.mode,
    l.granted,
    a.pid,
    a.query,
    a.state
FROM pg_locks l
JOIN pg_stat_activity a ON l.pid = a.pid
WHERE NOT l.granted
   OR l.relation = 'mytable'::regclass;
```

### 2. Set a Reasonable lock_timeout

```sql
-- Don't wait more than 5 seconds for any lock
SET lock_timeout = '5s';

-- This applies to the current session only
-- For all sessions, use ALTER SYSTEM
ALTER SYSTEM SET lock_timeout = '5s';
SELECT pg_reload_conf();
```

### 3. Kill Long-Running Transactions

```sql
-- Find transactions holding locks for too long
SELECT
    pid,
    now() - xact_start AS duration,
    query,
    state
FROM pg_stat_activity
WHERE state != 'idle'
ORDER BY duration DESC;

-- Terminate a blocking session
SELECT pg_terminate_backend(12345);
```

### 4. Use Statement-Level Lock Timeout for Migrations

```sql
-- For a specific DDL operation
SET LOCAL lock_timeout = '10s';
ALTER TABLE mytable ADD COLUMN newcol INT;
```

### 5. Reduce Transaction Duration

```sql
-- WRONG: long transaction holding locks
BEGIN;
SELECT * FROM mytable WHERE id = 1 FOR UPDATE;
-- ... long processing ...
UPDATE mytable SET status = 'done' WHERE id = 1;
COMMIT;

-- BETTER: acquire lock as late as possible
-- ... processing ...
BEGIN;
UPDATE mytable SET status = 'done' WHERE id = 1;
COMMIT;
```

## Common Mistakes

- Not setting `lock_timeout` at all -- this allows statements to block indefinitely
- Setting `lock_timeout` too low and causing spurious failures under normal load
- Using `SET LOCAL lock_timeout` but forgetting it only applies to the current transaction
- Not checking `pg_locks` before running migrations -- always verify no conflicting locks exist
- Running `ALTER TABLE` on a busy production table during peak hours without a timeout

## Related Pages

- [PostgreSQL Deadlock Detected](/tools/postgresql/pg-deadlock-detected)
- [PostgreSQL Statement Timeout](/tools/postgresql/pg-statement-timeout)
- [PostgreSQL Serialization Failure](/tools/postgresql/pg-serialization-failure)
- [MySQL Lock Timeout](/tools/mysql/mysql-lock-timeout)
