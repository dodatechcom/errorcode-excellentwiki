---
title: "[Solution] Linux MySQL Deadlock Found When Trying to Get Lock"
description: "Fix Linux MySQL 'Deadlock found when trying to get lock' errors. Resolve deadlocks, tune InnoDB, and optimize transaction queries."
platforms: ["linux"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["mysql", "deadlock", "lock", "innodb", "transaction", "database"]
weight: 5
---

# Linux: MySQL — Deadlock found when trying to get lock

The `Deadlock found when trying to get lock; try restarting transaction` error means two or more transactions are waiting for each other to release locks, creating a circular dependency. InnoDB automatically detects deadlocks and rolls back one transaction (the victim) to break the cycle.

## What This Error Means

A deadlock occurs when Transaction A holds a lock on Row 1 and waits for a lock on Row 2, while Transaction B holds a lock on Row 2 and waits for a lock on Row 1. Neither can proceed. InnoDB's deadlock detector identifies this and aborts one transaction with error 1213. The application should catch this error and retry the rolled-back transaction.

## Common Causes

- Transactions acquiring locks in inconsistent order
- Long-running transactions holding locks
- Missing indexes causing lock escalation (table locks instead of row locks)
- Large transactions locking many rows
- Gap locks in REPEATABLE READ isolation level
- Application logic performing reads and writes in the wrong order

## How to Fix

### 1. Analyze the Deadlock

```bash
# View the latest deadlock report
SHOW ENGINE INNODB STATUS\G

# Enable deadlock logging
SET GLOBAL innodb_print_all_deadlocks = ON;

# Check current locks
SELECT * FROM information_schema.INNODB_LOCK_WAITS;
SELECT * FROM information_schema.INNODB_TRX;
```

### 2. Reduce Transaction Scope

```sql
-- Shorten transactions: commit as soon as possible
BEGIN;
SELECT ... FOR UPDATE;
UPDATE ...;
COMMIT;  -- Don't hold the transaction open

-- Avoid doing non-database work inside a transaction
-- (file I/O, HTTP calls, etc.)
```

### 3. Ensure Consistent Lock Ordering

```sql
-- Always acquire locks in the same order
-- Bad: Transactions may lock in different order
-- T1: UPDATE accounts SET balance = balance - 100 WHERE id = 1;
--     UPDATE orders SET status = 'paid' WHERE id = 10;
-- T2: UPDATE orders SET status = 'paid' WHERE id = 10;
--     UPDATE accounts SET balance = balance - 100 WHERE id = 1;

-- Good: Always lock accounts first, then orders
-- Both T1 and T2: accounts WHERE id = 1 THEN orders WHERE id = 10
```

### 4. Add Proper Indexes

```sql
-- Check for full table scans causing excessive locking
EXPLAIN SELECT * FROM orders WHERE customer_id = 123;

-- Add index on the filtered column
CREATE INDEX idx_orders_customer ON orders(customer_id);

-- Verify index is used
EXPLAIN SELECT * FROM orders WHERE customer_id = 123;
```

### 5. Tune InnoDB Settings

```ini
# /etc/mysql/my.cnf or /etc/mysql/conf.d/performance.cnf
[mysqld]
# Increase lock wait timeout
innodb_lock_wait_timeout = 50

# Enable deadlock logging
innodb_print_all_deadlocks = ON

# Increase buffer pool for better performance
innodb_buffer_pool_size = 1G
```

### 6. Retry Deadlocked Transactions in Application

```python
# Python example with retry logic
import mysql.connector
from mysql.connector import errors

MAX_RETRIES = 3

for attempt in range(MAX_RETRIES):
    try:
        cursor.execute("UPDATE accounts SET balance = balance - 100 WHERE id = 1")
        cursor.execute("UPDATE orders SET status = 'paid' WHERE id = 10")
        connection.commit()
        break
    except errors.DatabaseError as e:
        if e.errno == 1213:  # Deadlock
            connection.rollback()
            if attempt == MAX_RETRIES - 1:
                raise
            continue
        raise
```

### 7. Monitor Active Transactions

```sql
-- Find long-running transactions
SELECT trx_id, trx_state, trx_started,
       TIMESTAMPDIFF(SECOND, trx_started, NOW()) AS duration_s,
       trx_query
FROM information_schema.INNODB_TRX
ORDER BY trx_started;

-- Kill a long-running transaction
KILL <trx_mysql_thread_id>;
```

## Examples

```sql
mysql> SHOW ENGINE INNODB STATUS\G
...
LATEST DETECTED DEADLOCK
------------------------
2025-07-14 10:00:00 0x7f8b1234abcd
*** (1) TRANSACTION:
TRANSACTION 12345, ACTIVE 10 sec starting index read
mysql tables in use 1, locked 1
LOCK WAIT 3 lock struct(s), heap size 1136, 2 row lock(s)
MySQL thread id 42, handle id 0x7f8b1234abcd
*** (1) WAITING FOR THIS LOCK TO BE GRANTED:
RECORD LOCKS space id 5 page no 3 n bits 72 index PRIMARY of table `db`.`orders`
 trx_id 12345 lock_mode X locks rec but not gap waiting
Record lock, heap no 2 PHYSICAL RECORD: n_fields 5; compact format
...
*** (2) TRANSACTION:
TRANSACTION 12346, ACTIVE 15 sec starting index read
...
*** (2) HOLDS THE LOCK(S):
RECORD LOCKS space id 5 page no 3 n bits 72 index PRIMARY of table `db`.`orders`
 trx_id 12346 lock_mode X locks rec but not gap
...
*** (1) ROLLBACK OF TRANSACTION 2;
```

## Related Errors

- [MySQL connection refused]({{< relref "/os/linux/linux-mysql-connection-refused" >}}) — Server connection issues
- [PostgreSQL role error]({{< relref "/os/linux/linux-postgres-role-error" >}}) — PostgreSQL role issues
- [nginx 504 timeout]({{< relref "/os/linux/linux-nginx-504-timeout" >}}) — Slow upstream responses
