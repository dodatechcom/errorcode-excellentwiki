---
title: "SQL Transaction Isolation Level Dirty Read Error"
description: "Fix SQL transaction isolation level errors when dirty reads, non-repeatable reads, or phantom reads occur."
languages: ["sql"]
error-types": ["runtime-error"]
severities: ["error"]
weight: 5
---

## Common Causes

- Using READ UNCOMMITTED allowing dirty reads
- Default isolation level allows non-repeatable reads
- Long-running transactions holding locks
- Phantom reads when new rows inserted during query
- Inconsistent isolation levels across application code

## How to Fix

```sql
-- WRONG: READ UNCOMMITTED allows dirty reads
SET TRANSACTION ISOLATION LEVEL READ UNCOMMITTED;
SELECT * FROM accounts;  -- may read uncommitted data

-- CORRECT: Use READ COMMITTED or higher
SET TRANSACTION ISOLATION LEVEL READ COMMITTED;
SELECT * FROM accounts;
```

```sql
-- WRONG: Non-repeatable read in long transaction
BEGIN TRANSACTION;
SELECT balance FROM accounts WHERE id = 1;  -- reads 100
-- Another transaction updates balance to 150 and commits
SELECT balance FROM accounts WHERE id = 1;  -- reads 150!

-- CORRECT: Use REPEATABLE READ
SET TRANSACTION ISOLATION LEVEL REPEATABLE READ;
BEGIN TRANSACTION;
SELECT balance FROM accounts WHERE id = 1;
-- ... other operations ...
SELECT balance FROM accounts WHERE id = 1;  -- still 100
COMMIT;
```

## Examples

```sql
-- Example 1: SERIALIZABLE for strictest isolation
SET TRANSACTION ISOLATION LEVEL SERIALIZABLE;
BEGIN TRANSACTION;
SELECT COUNT(*) FROM inventory WHERE product_id = 1;
-- No phantom reads even if new rows inserted
COMMIT;

-- Example 2: Snapshot isolation (SQL Server)
ALTER DATABASE mydb SET ALLOW_SNAPSHOT_ISOLATION ON;
SET TRANSACTION ISOLATION LEVEL SNAPSHOT;

-- Example 3: PostgreSQL READ COMMITTED (default)
BEGIN TRANSACTION;
SET TRANSACTION ISOLATION LEVEL READ COMMITTED;
SELECT * FROM orders WHERE status = 'pending';
COMMIT;
```

## Related Errors

- [Deadlock error](deadlock) -- concurrent transaction conflicts
- [Lock timeout error](lock-timeout) -- waiting for locks
