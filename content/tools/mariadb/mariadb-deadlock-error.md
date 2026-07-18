---
title: "[Solution] MariaDB Deadlock Error — How to Fix"
description: "Resolve MariaDB deadlocks by analyzing InnoDB monitor output, optimizing transaction order, adding indexes, and tuning lock wait timeouts"
tools: ["mariadb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# MariaDB Deadlock Error

A deadlock occurs when two or more transactions are blocked waiting for locks held by each other. InnoDB automatically detects deadlocks and rolls back the victim transaction to break the cycle.

## Why It Happens

- Two transactions lock rows in different orders
- Long-running transactions hold locks that block shorter transactions
- Missing indexes cause InnoDB to lock more rows than necessary
- Foreign key constraints acquire additional locks
- Large batch updates touch many rows in non-deterministic order

## Common Error Messages

```
ERROR 1213 (40001): Deadlock found when trying to get lock; try restarting transaction
```

```
LATEST DETECTED DEADLOCK
*** (1) TRANSACTION: TRANSACTION 54321, ACTIVE 12 sec
*** (1) WAITING FOR THIS LOCK TO BE GRANTED:
RECORD LOCKS space id 234 index PRIMARY of table `mydb`.`orders`
```

```
*** (2) TRANSACTION: TRANSACTION 54322, ACTIVE 8 sec
*** (2) HOLDS THE LOCK(S):
RECORD LOCKS space id 234 index PRIMARY of table `mydb`.`orders`
```

```
1213 - Deadlock found when trying to get lock; try restarting transaction,
Query: 'UPDATE inventory SET stock = stock - 1 WHERE product_id = 100'
```

## How to Fix It

### 1. Enable InnoDB Deadlock Logging

```sql
SHOW ENGINE INNODB STATUS\G

SET GLOBAL innodb_print_all_deadlocks = ON;

-- In my.cnf
-- [mysqld]
-- innodb_print_all_deadlocks = ON
```

### 2. Enforce Consistent Lock Ordering

```sql
-- Both transactions lock accounts first (by ascending ID)
START TRANSACTION;
SELECT * FROM accounts WHERE id = 1 FOR UPDATE;
SELECT * FROM orders WHERE account_id = 1 FOR UPDATE;
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
UPDATE orders SET status = 'charged' WHERE account_id = 1;
COMMIT;
```

### 3. Use NOWAIT or SKIP LOCKED

```sql
-- Fail immediately if row is locked
SELECT * FROM inventory WHERE product_id = 10 FOR UPDATE NOWAIT;

-- Skip locked rows (good for job queues)
SELECT * FROM job_queue WHERE status = 'pending' FOR UPDATE SKIP LOCKED LIMIT 10;
```

### 4. Add Indexes to Reduce Lock Scope

```sql
ALTER TABLE orders ADD INDEX idx_status (status);
ALTER TABLE inventory ADD INDEX idx_product (product_id);

EXPLAIN UPDATE orders SET status = 'shipped' WHERE order_id = 123;
```

### 5. Tune Lock Wait Timeout

```sql
SET GLOBAL innodb_lock_wait_timeout = 10;
```

## Common Scenarios

- **E-commerce checkout**: Two purchases try to deduct from the same inventory row. Use `FOR UPDATE` with consistent ordering.
- **Payment processing**: Transfer locks accounts in different orders. Always lock by ascending ID.
- **Batch job processing**: Worker processes rows out of order causing conflicts. Use `SKIP LOCKED`.

## Prevent It

- Always acquire locks in the same global order across all transactions
- Use `SELECT ... FOR UPDATE NOWAIT` to fail fast
- Keep transactions short and avoid holding locks across network calls

## Related Pages

- [MariaDB Lock Error](/tools/mariadb/mariadb-lock-error)
- [MariaDB InnoDB Error](/tools/mariadb/mariadb-innodb-error)
- [MySQL Deadlock Detected](/tools/mysql/mysql-deadlock-detected)
