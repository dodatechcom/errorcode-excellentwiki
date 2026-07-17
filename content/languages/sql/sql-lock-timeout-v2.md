---
title: "[Solution] SQL Lock Wait Timeout Exceeded Error Fix"
description: "Fix SQL lock wait timeout errors when a transaction waits too long for a lock."
languages: ["sql"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["lock-timeout", "innodb-lock", "wait-timeout", "sql"]
weight: 5
---

# SQL Lock Wait Timeout Exceeded Error Fix

A SQL lock timeout error occurs when a transaction waits longer than the configured timeout to acquire a lock held by another transaction.

## What This Error Means

InnoDB and other storage engines use row-level locking. When a transaction tries to lock a row that's already locked by another uncommitted transaction, it waits. If the wait exceeds `innodb_lock_wait_timeout` (default 50 seconds), the error fires.

## Common Causes

- Long-running transaction holding locks
- Uncommitted transaction from another session
- Missing indexes causing wide locks
- Deadlock situation (not yet detected)
- High concurrency with hot rows

## How to Fix

### 1. Reduce lock contention

```sql
-- CORRECT: Use shorter transactions
BEGIN;
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
COMMIT;
-- Don't hold transaction open for other work
```

### 2. Add proper indexes

```sql
-- CORRECT: Index columns used in WHERE
CREATE INDEX idx_orders_status ON orders(status);
-- Prevents table-wide locks from full scans
```

### 3. Increase timeout temporarily

```sql
-- CORRECT: Adjust timeout for long operations
SET innodb_lock_wait_timeout = 120;  -- 2 minutes
-- Run long operation
SET innodb_lock_wait_timeout = 50;  -- Reset to default
```

### 4. Kill blocking transactions

```sql
-- CORRECT: Find and kill blocking transactions
SELECT * FROM information_schema.INNODB_TRX;
SHOW ENGINE INNODB STATUS;

-- Kill the blocking thread
KILL <blocking_thread_id>;
```

## Related Errors

- [SQL Deadlock](sql-deadlock-v2) — circular lock waits
- [SQL Foreign Key](sql-foreign-key-v2) — constraint violations
- [SQL Duplicate Entry](sql-duplicate-entry-v2) — unique constraint
