---
title: "[Solution] SQL Lock Wait Timeout Error Fix"
description: "Fix 'Lock wait timeout exceeded' when a transaction waits too long to acquire a row lock."
languages: ["sql"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# SQL Lock Wait Timeout Error Fix

This error occurs when a transaction waits longer than the configured timeout to acquire a lock on a row or table. The message reads: `Lock wait timeout exceeded; try restarting transaction`.

## Description

When a transaction modifies a row, it acquires a lock that prevents other transactions from modifying the same row until the first transaction commits or rolls back. If another transaction tries to modify that row and waits too long, this error is raised.

## Common Causes

- **Long-running transaction** — a transaction holds locks for too long.
- **Deadlock between transactions** — two transactions waiting on each other's locks.
- **High concurrency** — many transactions competing for the same rows.
- **Missing indexes** — locks escalate to table-level when indexes are missing.

## How to Fix

### Fix 1: Reduce transaction duration

```sql
-- Commit quickly — don't hold transactions open
START TRANSACTION;
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
UPDATE accounts SET balance = balance + 100 WHERE id = 2;
COMMIT;  -- Commit immediately, not after more work
```

### Fix 2: Increase lock timeout temporarily

```sql
-- Check current timeout (default is 50 seconds in MySQL)
SHOW VARIABLES LIKE 'innodb_lock_wait_timeout';

-- Increase it (in seconds)
SET innodb_lock_wait_timeout = 120;
```

### Fix 3: Add proper indexes

```sql
-- Missing indexes cause full table locks
-- Add index on the column used in WHERE
CREATE INDEX idx_user_id ON orders(user_id);

-- Now row-level locks are used instead of table locks
UPDATE orders SET status = 'shipped' WHERE user_id = 1;
```

### Fix 4: Use optimistic locking

```sql
-- Instead of locking, use a version check
UPDATE products
SET stock = stock - 1, version = version + 1
WHERE id = 10 AND version = 5;

-- Check if the update succeeded
SELECT ROW_COUNT();
-- If 0, the row was modified by another transaction
```

## Examples

```sql
-- Transaction A holds a lock
START TRANSACTION;
UPDATE accounts SET balance = 500 WHERE id = 1;
-- ... long processing, not yet committed

-- Transaction B waits for the same row
UPDATE accounts SET balance = 300 WHERE id = 1;
-- ERROR 1205: Lock wait timeout exceeded; try restarting transaction
```

## Related Errors

- [Deadlock](deadlock.md) — two transactions waiting on each other.
- [Foreign Key](foreign-key.md) — constraint violations during concurrent updates.
- [Duplicate Entry](duplicate-entry.md) — race conditions in unique constraints.
