---
title: "[Solution] MySQL Deadlock Found When Trying to Get Lock - Fix Deadlocks"
description: "Fix MySQL deadlock found errors by analyzing InnoDB status, reordering queries, adding indexes, and tuning innodb_lock_wait_timeout settings"
tools: ["mysql"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
---

# MySQL Deadlock Found When Trying to Get Lock

A deadlock in MySQL (InnoDB) occurs when two or more transactions are waiting for each other to release locks, creating a circular dependency. InnoDB automatically detects deadlocks and rolls back the transaction with the least amount of change.

## What This Error Means

MySQL returns this error when InnoDB detects a deadlock:

```
ERROR 1213 (40001): Deadlock found when trying to get lock; try restarting transaction
```

InnoDB maintains a wait-for graph to detect deadlocks. When a cycle is found, InnoDB rolls back one transaction (the "victim") and returns the error to its client. The other transaction can proceed.

The last deadlock detail can be viewed with:

```sql
SHOW ENGINE INNODB STATUS;
```

## Why It Happens

- Two transactions update rows in opposite order
- InnoDB gap locks create lock conflicts on index ranges
- Foreign key constraints cause implicit locking
- Long-running transactions hold locks while waiting for additional locks
- High concurrency causes many transactions to compete for the same rows
- Missing indexes cause InnoDB to lock more rows than necessary during scans

## How to Fix It

### 1. Analyze the Last Deadlock

```sql
-- The LATEST DETECTED DEADLOCK section shows which transactions were involved
SHOW ENGINE INNODB STATUS;
```

### 2. Lock Rows in Consistent Order

```sql
-- WRONG: opposite ordering causes deadlocks
-- Transaction A
BEGIN;
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
UPDATE accounts SET balance = balance + 100 WHERE id = 2;

-- Transaction B
BEGIN;
UPDATE accounts SET balance = balance - 50 WHERE id = 2;
UPDATE accounts SET balance = balance + 50 WHERE id = 1;

-- CORRECT: always lock in ascending order
UPDATE accounts SET balance = balance - 100 WHERE id = LEAST(1, 2);
UPDATE accounts SET balance = balance + 100 WHERE id = GREATEST(1, 2);
```

### 3. Add Proper Indexes

```sql
-- Without an index, InnoDB scans and locks many rows
CREATE INDEX idx_orders_customer ON orders(customer_id);
```

### 4. Use SELECT ... FOR UPDATE NOWAIT

```sql
-- Fail immediately if lock cannot be acquired
BEGIN;
SELECT * FROM accounts WHERE id = 1 FOR UPDATE NOWAIT;
-- If lock is unavailable, raises error 3572 instead of waiting
```

### 5. Adjust InnoDB Lock Wait Timeout

```sql
-- Default is 50 seconds. Reduce to fail faster on contention
SET GLOBAL innodb_lock_wait_timeout = 10;
```

### 6. Reduce Transaction Duration

```sql
-- Process in smaller batches
-- WRONG: one giant transaction
BEGIN;
UPDATE orders SET status = 'processed' WHERE status = 'pending';
COMMIT;

-- BETTER: batch processing
REPEAT
    UPDATE orders SET status = 'processed'
    WHERE status = 'pending' LIMIT 1000;
UNTIL ROW_COUNT() = 0 END REPEAT;
```

## Common Mistakes

- Ignoring deadlock logs because "MySQL handles it automatically" -- frequent deadlocks indicate design problems
- Increasing `innodb_lock_wait_timeout` to avoid deadlocks -- this just delays detection
- Using `SELECT ... FOR UPDATE` without considering whether the lock is really necessary
- Not checking `SHOW ENGINE INNODB STATUS` to understand which specific queries are deadlocking
- Using gap locks unnecessarily by running with the default `REPEATABLE READ` isolation level

## Related Pages

- [MySQL Lock Timeout](/tools/mysql/mysql-lock-timeout)
- [MySQL InnoDB Error](/tools/mysql/mysql-innodb-error)
- [PostgreSQL Deadlock Detected](/tools/postgresql/pg-deadlock-detected)
- [MySQL Duplicate Entry](/tools/mysql/mysql-duplicate-entry)
