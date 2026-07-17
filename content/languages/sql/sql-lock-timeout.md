---
title: "[Solution] SQL Lock Wait Timeout Fix"
description: "Fix 'Lock wait timeout exceeded' when a transaction waits too long for a row lock."
languages: ["sql"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["lock-timeout", "innodb", "transaction", "lock", "wait"]
weight: 5
---

This error occurs when a transaction waits longer than `innodb_lock_wait_timeout` seconds to acquire a row lock. The message reads: `Lock wait timeout exceeded; try restarting transaction`.

## What This Error Means

InnoDB uses row-level locking. When one transaction holds a lock on a row, other transactions must wait. If the wait exceeds the configured timeout, the waiting transaction is rolled back.

## Common Causes

- Long-running transaction holds locks too long
- Missing index causes InnoDB to lock more rows than necessary
- Another transaction has an exclusive lock on the target row
- Gap locking in REPEATABLE READ isolation level

## How to Fix

### Fix 1: Find and kill blocking transactions

```sql
-- Find blocking threads
SELECT * FROM information_schema.innodb_lock_waits;
SELECT * FROM sys.innodb_lock_waits;

-- Kill the blocking thread
KILL <blocking_thread_id>;
```

### Fix 2: Increase lock wait timeout

```sql
SET innodb_lock_wait_timeout = 30; -- default is 50 seconds
```

### Fix 3: Use shorter transactions

```sql
-- Bad: holds lock for a long time
START TRANSACTION;
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
-- ... long processing ...
COMMIT;

-- Good: minimize lock duration
START TRANSACTION;
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
COMMIT;
-- Then process separately
```

### Fix 4: Add indexes to reduce lock scope

```sql
CREATE INDEX idx_orders_status ON orders(status);
```

## Examples

```sql
-- Transaction A holds a lock
START TRANSACTION;
UPDATE products SET stock = stock - 1 WHERE id = 1;
-- ... slow processing ...

-- Transaction B waits
UPDATE products SET stock = stock + 1 WHERE id = 1;
-- ERROR 1205: Lock wait timeout exceeded
```

## Related Errors

- [Deadlock](deadlock.md) — circular lock wait
- [Connection Refused](sql-connection-refused.md) — cannot reach the server
