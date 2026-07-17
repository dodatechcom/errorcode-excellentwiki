---
title: "[Solution] SQL Deadlock Wait-for Graph Cycle Error Fix"
description: "Fix SQL deadlock errors when two or more transactions are waiting for each other to release locks."
languages: ["sql"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["deadlock", "wait-for", "lock", "transaction", "sql"]
weight: 5
---

# SQL Deadlock Wait-for Graph Cycle Error Fix

A SQL deadlock error occurs when two or more transactions are waiting for each other to release locks, creating a circular dependency.

## What This Error Means

A deadlock happens when Transaction A holds a lock on Row 1 and needs Row 2, while Transaction B holds a lock on Row 2 and needs Row 1. Neither can proceed. The database detects this cycle and kills one transaction as a victim.

## Common Causes

- Transactions accessing tables in different order
- Long-running transactions holding locks
- Missing indexes causing table scans
- Large batch operations
- Too many concurrent transactions

## How to Fix

### 1. Access tables in consistent order

```sql
-- WRONG: Different order causes deadlock
-- Transaction 1: UPDATE accounts, THEN orders
-- Transaction 2: UPDATE orders, THEN accounts

-- CORRECT: Always access in same order
-- Both transactions: accounts first, then orders
BEGIN TRANSACTION;
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
UPDATE orders SET status = 'paid' WHERE account_id = 1;
COMMIT;
```

### 2. Use shorter transactions

```sql
-- WRONG: Long transaction holds locks
BEGIN TRANSACTION;
-- ... many operations ...
-- ... more operations ...
COMMIT;

-- CORRECT: Keep transactions short
BEGIN TRANSACTION;
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
COMMIT;
```

### 3. Add proper indexes

```sql
-- CORRECT: Index columns used in WHERE and JOIN
CREATE INDEX idx_orders_account_id ON orders(account_id);
CREATE INDEX idx_users_email ON users(email);
```

### 4. Set deadlock priority

```sql
-- CORRECT: Set priority for victim selection
SET DEADLOCK_PRIORITY LOW;  -- This transaction is more likely to be victim
-- Or
SET DEADLOCK_PRIORITY HIGH;  -- Less likely to be killed
```

## Related Errors

- [SQL Lock Timeout](sql-lock-timeout-v2) — lock wait exceeded
- [SQL Foreign Key](sql-foreign-key-v2) — constraint violations
- [SQL Duplicate Entry](sql-duplicate-entry-v2) — unique constraint
