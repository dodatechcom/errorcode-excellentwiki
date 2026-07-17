---
title: "[Solution] SQL Deadlock Error Fix"
description: "Fix 'Deadlock found when trying to get lock' when two transactions block each other."
languages: ["sql"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# SQL Deadlock Error Fix

This error occurs when two or more transactions are waiting for each other to release locks, creating a circular dependency. The message reads: `Deadlock found when trying to get lock; try restarting transaction`.

## Description

A deadlock happens when Transaction A locks Row 1 and waits for Row 2, while Transaction B locks Row 2 and waits for Row 1. Neither can proceed. The database detects this and rolls back one transaction (the victim) to allow the other to complete.

## Common Causes

- **Inconsistent lock ordering** — transactions lock tables/rows in different orders.
- **Long-running transactions** — hold locks longer, increasing deadlock windows.
- **High concurrency** — many transactions competing for overlapping rows.
- **Missing indexes** — cause broader locks that increase contention.

## How to Fix

### Fix 1: Lock rows in a consistent order

```sql
-- Always lock tables in the same order across all transactions
-- Transaction 1
START TRANSACTION;
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
UPDATE accounts SET balance = balance + 100 WHERE id = 2;
COMMIT;

-- Transaction 2 (same order: id 1 before id 2)
START TRANSACTION;
UPDATE accounts SET balance = balance - 50 WHERE id = 1;
UPDATE accounts SET balance = balance + 50 WHERE id = 2;
COMMIT;
```

### Fix 2: Keep transactions short

```sql
-- Do all reads first, then writes
START TRANSACTION;
-- Read phase
SELECT balance FROM accounts WHERE id = 1;
SELECT balance FROM accounts WHERE id = 2;
-- Write phase (fast)
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
UPDATE accounts SET balance = balance + 100 WHERE id = 2;
COMMIT;
```

### Fix 3: Use SELECT ... FOR UPDATE explicitly

```sql
-- Acquire locks in a known order
START TRANSACTION;
SELECT * FROM accounts WHERE id = 1 FOR UPDATE;
SELECT * FROM accounts WHERE id = 2 FOR UPDATE;
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
UPDATE accounts SET balance = balance + 100 WHERE id = 2;
COMMIT;
```

### Fix 4: Add indexes to reduce lock scope

```sql
-- Without index, UPDATE locks many rows
-- With index, only the matching row is locked
CREATE INDEX idx_account_id ON accounts(id);
```

## Examples

```sql
-- Transaction A
START TRANSACTION;
UPDATE accounts SET balance = 100 WHERE id = 1;
-- waits...

-- Transaction B (concurrent)
START TRANSACTION;
UPDATE accounts SET balance = 200 WHERE id = 2;
UPDATE accounts SET balance = 300 WHERE id = 1;  -- blocks on A's lock

-- A tries to update id = 2 — blocked by B
-- ERROR 1213: Deadlock found when trying to get lock
-- (One transaction is rolled back as victim)
```

## Related Errors

- [Lock Timeout](lock-timeout.md) — waiting too long for a lock (not a deadlock).
- [Foreign Key](foreign-key.md) — constraint violations during concurrent updates.
- [Duplicate Entry](duplicate-entry.md) — race conditions in unique constraints.
