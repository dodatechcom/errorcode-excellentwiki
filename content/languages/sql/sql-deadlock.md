---
title: "[Solution] SQL Deadlock Error Fix"
description: "Fix 'Deadlock found when trying to get lock' when two transactions block each other."
languages: ["sql"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["deadlock", "lock", "transaction", "concurrency", "innodb"]
weight: 5
---

This error occurs when two or more transactions are waiting for each other to release locks, creating a circular dependency. The database detects the deadlock and rolls back one transaction. The message reads: `Deadlock found when trying to get lock`.

## What This Error Means

InnoDB detects a deadlock when two transactions hold locks that the other needs. To break the cycle, InnoDB rolls back the transaction with the least amount of effort (smallest undo log).

## Common Causes

- Two transactions update rows in opposite order
- Long-running transactions hold locks too long
- Lack of proper indexing causes full table locks
- Mixed read/write operations in transactions

## How to Fix

### Fix 1: Always lock rows in the same order

```sql
-- Transaction A
START TRANSACTION;
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
UPDATE accounts SET balance = balance + 100 WHERE id = 2;
COMMIT;

-- Transaction B — same order
START TRANSACTION;
UPDATE accounts SET balance = balance - 50 WHERE id = 1;
UPDATE accounts SET balance = balance + 50 WHERE id = 2;
COMMIT;
```

### Fix 2: Use shorter transactions

```sql
-- Bad: long transaction
START TRANSACTION;
-- ... many queries ...
-- ... more queries ...
COMMIT;

-- Good: keep transactions short
START TRANSACTION;
UPDATE orders SET status = 'shipped' WHERE id = 100;
COMMIT;
```

### Fix 3: Add proper indexes

```sql
-- Without index, InnoDB locks entire table
CREATE INDEX idx_orders_user_id ON orders(user_id);

-- Now InnoDB only locks matching rows
```

### Fix 4: Use SELECT ... FOR UPDATE with timeout

```sql
SET innodb_lock_wait_timeout = 5; -- seconds
SELECT * FROM accounts WHERE id = 1 FOR UPDATE;
```

## Examples

```sql
-- Transaction 1                         -- Transaction 2
START TRANSACTION;                       START TRANSACTION;
UPDATE t SET a=1 WHERE id=1;            UPDATE t SET a=2 WHERE id=2;
UPDATE t SET a=2 WHERE id=2;            UPDATE t SET a=1 WHERE id=1;
-- Deadlock detected! Transaction 2 is rolled back
```

## Related Errors

- [Lock Timeout](lock-timeout.md) — waiting too long for a lock
- [Duplicate Entry](duplicate-entry.md) — constraint violation
