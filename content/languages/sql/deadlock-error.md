---
title: "[Solution] Deadlock Detected"
description: "Fix 'Deadlock detected' when two or more transactions block each other waiting for locks."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "sql"
tags: ["sql", "performance, deadlock, concurrency"]
severity: "error"
---

# Deadlock Detected

## Error Message

```
ERROR 1213: Deadlock found when trying to get lock; try restarting transaction — Two or more transactions are in a circular wait for locks.
```

## Common Causes

- Transactions lock rows in different orders, creating a circular dependency
- Long-running transactions hold locks longer, increasing the deadlock window
- High concurrency with many transactions competing for overlapping rows
- Missing or poor indexes cause broader locks that increase contention

## Solutions

### Solution 1: Always lock tables and rows in a consistent order

Prevent circular waits by enforcing a global lock ordering across all transactions.

```sql
-- Transaction 1: lock accounts in order of ID
START TRANSACTION;
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
UPDATE accounts SET balance = balance + 100 WHERE id = 2;
COMMIT;

-- Transaction 2: lock accounts in the SAME order
START TRANSACTION;
UPDATE accounts SET balance = balance - 50 WHERE id = 1;
UPDATE accounts SET balance = balance + 50 WHERE id = 2;
COMMIT;

-- Bad example: lock in different orders (causes deadlock)
-- T1: UPDATE accounts SET ... WHERE id = 1; then WHERE id = 2;
-- T2: UPDATE accounts SET ... WHERE id = 2; then WHERE id = 1;
```

### Solution 2: Keep transactions as short as possible

Minimize the time locks are held by committing quickly.

```sql
-- Wrong: long transaction holds locks
START TRANSACTION;
SELECT * FROM accounts WHERE id = 1;
-- ... application processing (slow) ...
-- ... more application processing ...
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
COMMIT;

-- Correct: do all reads first, then writes
START TRANSACTION;
SELECT balance FROM accounts WHERE id = 1 FOR UPDATE;
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
COMMIT;

-- Use SELECT ... FOR UPDATE to acquire locks early
START TRANSACTION;
SELECT * FROM accounts WHERE id IN (1, 2) FOR UPDATE ORDER BY id;
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
UPDATE accounts SET balance = balance + 100 WHERE id = 2;
COMMIT;
```

### Solution 3: Add proper indexes to reduce lock scope

Indexes allow the database to lock only matching rows instead of entire tables.

```sql
-- Without an index, UPDATE may lock many rows
CREATE INDEX idx_account_id ON accounts(id);
CREATE INDEX idx_account_status ON accounts(status);

-- Use row-level locking instead of table locking
-- InnoDB (MySQL) uses row locks by default with proper indexes
-- PostgreSQL uses row-level locking automatically

-- Check for missing indexes
SELECT * FROM sys.schema_unused_indexes; -- SQL Server
SELECT * FROM pg_stat_user_indexes WHERE idx_scan = 0; -- PostgreSQL
SHOW INDEX FROM accounts; -- MySQL
```

## Prevention Tips

- Use SHOW ENGINE INNODB STATUS (MySQL) or pg_stat_activity (PostgreSQL) to diagnose deadlock details
- Implement retry logic in application code to handle deadlocks gracefully
- Avoid long-running transactions and hold locks for the shortest time possible

## Related Errors

- [Lock Timeout]({{< relref "/languages/sql/lock-timeout.md" >}})
- [Table Lock Error]({{< relref "/languages/sql/table-lock-error.md" >}})
- [Transaction Error]({{< relref "/languages/sql/transaction-error.md" >}})
