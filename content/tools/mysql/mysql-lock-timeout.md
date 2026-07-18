---
title: "[Solution] MySQL Lock Wait Timeout Exceeded - Fix Lock Contention"
description: "Fix MySQL lock wait timeout exceeded errors by analyzing InnoDB locks, reducing transaction duration, and optimizing query performance"
tools: ["mysql"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
---

# MySQL Lock Wait Timeout Exceeded

This error occurs when a transaction waits longer than `innodb_lock_wait_timeout` (default 50 seconds) to acquire a row lock. Unlike a deadlock, there is no circular wait -- one transaction is simply blocked by another for too long.

## What This Error Means

MySQL returns this error when the lock wait timeout expires:

```
ERROR 1205 (HY000): Lock wait timeout exceeded; try restarting transaction
```

InnoDB uses row-level locking, and when one transaction holds a lock on a row, other transactions that need the same row must wait. If the waiting transaction exceeds `innodb_lock_wait_timeout`, it is rolled back and the error is returned.

## Why It Happens

- A long-running transaction holds a lock that blocks other transactions
- An `UPDATE` or `DELETE` scans many rows due to a missing index, holding locks on each row
- A `SELECT ... FOR UPDATE` is waiting for a row locked by another transaction
- A deadlock was detected and the victim was rolled back, but the winning transaction is still slow
- Schema change (`ALTER TABLE`) requires a metadata lock that blocks DML
- High concurrency causes many transactions to compete for the same rows

## How to Fix It

### 1. Find the Blocking Transaction

```sql
-- Check current locks
SELECT
    r.trx_id AS waiting_trx,
    r.trx_mysql_thread_id AS waiting_thread,
    r.trx_query AS waiting_query,
    b.trx_id AS blocking_trx,
    b.trx_mysql_thread_id AS blocking_thread,
    b.trx_query AS blocking_query
FROM information_schema.innodb_lock_waits w
JOIN information_schema.innodb_trx b ON b.trx_id = w.blocking_trx_id
JOIN information_schema.innodb_trx r ON r.trx_id = w.requesting_trx_id;
```

### 2. Kill the Blocking Transaction

```sql
-- Find the process ID of the blocking transaction
SHOW PROCESSLIST;

-- Terminate it
KILL <process_id>;
```

### 3. Reduce innodb_lock_wait_timeout

```sql
-- Fail faster when locks are contested
SET GLOBAL innodb_lock_wait_timeout = 10;

-- Or per-session
SET SESSION innodb_lock_wait_timeout = 10;
```

### 4. Add Indexes to Reduce Lock Scope

```sql
-- Without an index, InnoDB locks every row in the table during a scan
CREATE INDEX idx_orders_status ON orders(status);
```

### 5. Use SELECT ... FOR UPDATE with NOWAIT

```sql
BEGIN;
SELECT * FROM inventory WHERE product_id = 42 FOR UPDATE NOWAIT;
-- Raises error immediately if row is locked
```

### 6. Monitor Metadata Locks

```sql
-- Check for metadata locks (DDL blocking DML)
SELECT
    OBJECT_SCHEMA,
    OBJECT_NAME,
    LOCK_TYPE,
    LOCK_DURATION
FROM performance_schema.metadata_locks
WHERE OBJECT_NAME IS NOT NULL;
```

## Common Mistakes

- Not checking which transaction is blocking before killing processes
- Increasing `innodb_lock_wait_timeout` to avoid timeouts without fixing the root cause
- Running `ALTER TABLE` on a busy table without using `pt-online-schema-change` or `gh-ost`
- Not using indexes on columns in `WHERE` clauses of `UPDATE` and `DELETE` statements
- Assuming the blocking transaction is the "bad" one -- it may be doing necessary work

## Related Pages

- [MySQL Deadlock Detected](/tools/mysql/mysql-deadlock-detected)
- [MySQL InnoDB Error](/tools/mysql/mysql-innodb-error)
- [MySQL Too Many Connections](/tools/mysql/mysql-too-many-connections)
- [PostgreSQL Lock Timeout](/tools/postgresql/pg-locks-timeout)
