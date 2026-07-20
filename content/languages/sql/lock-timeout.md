---
title: "[Solution] Lock Wait Timeout Exceeded"
description: "Fix 'Lock wait timeout exceeded' when a transaction waits too long for a lock held by another transaction."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "sql"
tags: ["sql", "lock, timeout"]
severity: "error"
---

# Lock Wait Timeout Exceeded

## Error Message

```
ERROR 1205: Lock wait timeout exceeded; try restarting transaction — The transaction waited longer than the lock_wait_timeout setting for a lock held by another transaction.
```

## Common Causes

- Another transaction holds a lock on the rows or table for too long
- High concurrency with many transactions competing for the same rows
- Long-running SELECT queries hold shared locks that block WRITE operations
- Lock_wait_timeout is set too low for the workload

## Solutions

### Solution 1: Reduce lock hold time

Release locks as quickly as possible by keeping transactions short.

```sql
-- Wrong: long transaction holds locks
START TRANSACTION;
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
-- ... long processing ...
-- ... even more processing ...
UPDATE accounts SET balance = balance + 100 WHERE id = 2;
-- ... more work while holding lock ...
COMMIT;

-- Correct: minimize lock hold time
START TRANSACTION;
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
UPDATE accounts SET balance = balance + 100 WHERE id = 2;
COMMIT; -- commit immediately after updates
```

### Solution 2: Increase lock wait timeout if needed

Adjust the timeout setting to allow longer waits for legitimate lock contention.

```sql
-- MySQL: increase lock wait timeout
SET SESSION innodb_lock_wait_timeout = 60; -- 60 seconds

-- PostgreSQL: increase lock timeout
SET lock_timeout = '60s'; -- 60 seconds

-- SQL Server: increase lock timeout (default is -1 = wait forever)
SET LOCK_TIMEOUT 60000; -- 60 seconds in milliseconds

-- Check current timeout settings
SHOW VARIABLES LIKE 'innodb_lock_wait_timeout'; -- MySQL
SHOW lock_timeout; -- PostgreSQL
SELECT LOCK_TIMEOUT; -- SQL Server
```

### Solution 3: Identify and terminate blocking transactions

Find long-running transactions and terminate them if necessary.

```sql
-- MySQL: find blocking transactions
SELECT * FROM information_schema.INNODB_TRX;
SHOW ENGINE INNODB STATUS;
SELECT * FROM information_schema.INNODB_LOCK_WAITS;

-- PostgreSQL: find blocking queries
SELECT
    blocked.pid AS blocked_pid,
    blocked.query AS blocked_query,
    blocking.pid AS blocking_pid,
    blocking.query AS blocking_query
FROM pg_stat_activity blocked
JOIN pg_locks bl ON blocked.pid = bl.pid
JOIN pg_locks kl ON bl.locktype = kl.locktype
    AND bl.database IS NOT DISTINCT FROM kl.database
    AND bl.relation IS NOT DISTINCT FROM kl.relation
    AND bl.page IS NOT DISTINCT FROM kl.page
    AND bl.tuple IS NOT DISTINCT FROM kl.tuple
    AND bl.transactionid IS NOT DISTINCT FROM kl.transactionid
JOIN pg_stat_activity blocking ON kl.pid = blocking.pid
WHERE NOT bl.granted;

-- SQL Server: find blocking processes
SELECT * FROM sys.dm_exec_requests WHERE blocking_session_id > 0;
KILL <blocking_session_id>;
```

## Prevention Tips

- Monitor lock wait timeouts to identify patterns of contention and redesign affected queries
- Use SELECT ... FOR UPDATE with SKIP LOCKED to avoid waiting for locked rows in queue-like workloads
- Implement exponential backoff retry logic in application code to handle lock timeouts gracefully

## Related Errors

- [Deadlock Error]({{< relref "/languages/sql/deadlock-error" >}})
- [Table Lock Error]({{< relref "/languages/sql/table-lock-error" >}})
- [Timeout Error]({{< relref "/languages/sql/timeout-error" >}})
