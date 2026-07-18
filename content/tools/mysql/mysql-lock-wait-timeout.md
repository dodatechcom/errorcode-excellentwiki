---
title: "[Solution] MySQL Lock Wait Timeout Exceeded Error — How to Fix"
description: "Fix MySQL lock wait timeout exceeded errors by killing blocking transactions, optimizing queries, and adjusting innodb_lock_wait_timeout settings"
tools: ["mysql"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# MySQL Lock Wait Timeout Exceeded Error

This error means a transaction waited too long to acquire a row lock held by another transaction. InnoDB enforces a timeout on lock waits, and when the lock is not released within that window, the waiting transaction is rolled back.

## Why It Happens

- A long-running transaction holds row locks that block other transactions
- An application opens a transaction but forgets to commit or rollback
- High concurrency causes lock contention on the same rows
- A slow query holds locks for an extended period
- Deadlock between two transactions causes one to wait indefinitely until timeout
- `innodb_lock_wait_timeout` is set too low for workload requirements
- Batch operations lock large numbers of rows sequentially

## Common Error Messages

```
ERROR 1205 (HY000): Lock wait timeout exceeded; try restarting transaction
```

```
Cannot execute the statement because it needs to be in a transaction, but lock wait timeout would be exceeded.
```

```
Lock wait timeout exceeded; try restarting transaction
```

## How to Fix It

### 1. Find Blocking Transactions

```sql
-- MySQL 8.0+: Use performance_schema
SELECT
    r.trx_id AS waiting_trx,
    r.trx_mysql_thread_id AS waiting_thread,
    r.trx_query AS waiting_query,
    b.trx_id AS blocking_trx,
    b.trx_mysql_thread_id AS blocking_thread,
    b.trx_query AS blocking_query
FROM performance_schema.data_lock_waits w
JOIN information_schema.innodb_trx r ON r.trx_id = w.REQUESTING_ENGINE_TRANSACTION_ID
JOIN information_schema.innodb_trx b ON b.trx_id = w.BLOCKING_ENGINE_TRANSACTION_ID;
```

### 2. Kill the Blocking Thread

```sql
-- Kill the connection holding the lock
KILL <blocking_thread_id>;

-- Or from the command line
mysqladmin -u root -p kill <blocking_thread_id>
```

### 3. Increase the Lock Wait Timeout

```sql
-- Check current value (default is 50 seconds)
SHOW VARIABLES LIKE 'innodb_lock_wait_timeout';

-- Increase to 120 seconds
SET GLOBAL innodb_lock_wait_timeout = 120;
```

### 4. Optimize Long-Running Queries

```sql
-- Find long-running transactions
SELECT
    trx_id,
    trx_state,
    trx_started,
    TIMESTAMPDIFF(SECOND, trx_started, NOW()) AS duration_sec,
    trx_query
FROM information_schema.innodb_trx
ORDER BY trx_started;
```

### 5. Reduce Lock Scope

```sql
-- Use smaller transactions instead of one large transaction
START TRANSACTION;
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
COMMIT;

START TRANSACTION;
UPDATE accounts SET balance = balance + 100 WHERE id = 2;
COMMIT;
```

## Common Scenarios

- **Batch inserts on a hot table**: Multiple workers insert rows into the same table, causing lock queuing. Increase timeout or use optimistic locking.
- **Read-modify-write cycles**: An application reads a row, modifies it in memory, then writes it back. Use `SELECT ... FOR UPDATE` with fast commits.
- **Idle transactions**: A developer opens a transaction, does some work, then walks away. Set `wait_timeout` and `interactive_timeout` to close idle connections.

## Prevent It

- Always commit transactions promptly and never leave them open unnecessarily
- Monitor `innodb_row_lock_time_avg` in `INFORMATION_SCHEMA.INNODB_METRICS` to detect contention early
- Use application-level timeouts on database connections so abandoned transactions are cleaned up

## Related Pages

- [MySQL Deadlock](/tools/mysql/mysql-deadlock)
- [MySQL InnoDB Error](/tools/mysql/mysql-innodb-error)
- [PostgreSQL Lock Timeout](/tools/postgresql/pg-lock-timeout)
