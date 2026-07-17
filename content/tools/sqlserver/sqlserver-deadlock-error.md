---
title: "SQL Server Deadlock Error"
description: "SQL Server detects a deadlock between two or more transactions."
tools: ["sqlserver"]
error-types: ["database-error"]
severities: ["error"]
tags: ["sqlserver", "deadlock", "lock", "transaction", "concurrency"]
weight: 5
---

# SQL Server Deadlock Error

A SQL Server deadlock error occurs when two or more transactions are waiting for each other to release locks, creating a circular dependency. SQL Server automatically detects and resolves deadlocks by killing one transaction.

## Common Causes

- Transactions access tables in different order
- Long-running transactions hold locks too long
- Missing indexes cause table scans that increase lock scope
- High concurrency with insufficient isolation

## How to Fix

### Enable Deadlock Logging

```sql
-- Enable trace flag 1222 for detailed deadlock info
DBCC TRACEON(1222, -1);
```

### Check Deadlock Graph

```sql
-- In SQL Server Profiler or Extended Events
SELECT * FROM sys.dm_tran_locks;
```

### Fix Transaction Ordering

```sql
-- Always access tables in the same order
BEGIN TRANSACTION
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
UPDATE accounts SET balance = balance + 100 WHERE id = 2;
COMMIT
```

### Use SET DEADLOCK_PRIORITY

```sql
SET DEADLOCK_PRIORITY LOW;  -- This session will be chosen as victim
```

### Add Indexes

```sql
CREATE INDEX idx_accounts_id ON accounts(id);
```

### Reduce Lock Duration

```sql
-- Use shorter transactions
BEGIN TRANSACTION
-- Quick operations
COMMIT
```

### Use Snapshot Isolation

```sql
ALTER DATABASE mydb SET ALLOW_SNAPSHOT_ISOLATION ON;
```

## Examples

```sql
-- Transaction 1
BEGIN TRANSACTION
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
-- Waits for Transaction 2 to release lock on id=2

-- Transaction 2
BEGIN TRANSACTION
UPDATE accounts SET balance = balance + 100 WHERE id = 2;
-- Waits for Transaction 1 to release lock on id=1

-- DEADLOCK: Transaction 1 chosen as victim
```

## Related Errors

- [Lock Timeout Error]({{< relref "/tools/sqlserver/sqlserver-lock-timeout-error" >}}) — lock timeout
- [Transaction Error]({{< relref "/tools/sqlserver/sqlserver-transaction-error" >}}) — transaction error
