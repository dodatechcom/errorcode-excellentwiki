---
title: "[Solution] SQL Server Error 1205: Deadlock Victim"
description: "Fix SQL Server Error 1205 deadlock victim errors. Resolve transaction deadlock and blocking issues."
tools: ["sqlserver"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["sqlserver", "1205", "deadlock", "victim", "blocking", "transaction"]
weight: 5
---

# Error 1205: Deadlock Victim

Error 1205 occurs when SQL Server selects your session as the deadlock victim. A deadlock happens when two or more transactions hold locks that the other needs, creating a circular wait.

## Common Causes

- Two transactions access the same resources in different orders
- Long-running transactions hold locks while waiting for other resources
- Missing indexes cause table scans that acquire more locks
- Lock escalation from row-level to table-level locks

## How to Fix

### Enable Deadlock Logging

```sql
-- Enable trace flag 1222 for detailed deadlock info
DBCC TRACEON(1222, -1);

-- Check deadlocks in error log
EXEC xp_readerrorlog 0, 1, N'deadlock';
```

### Add Proper Indexes

```sql
-- Reduce lock scope by adding indexes on WHERE/JOIN columns
CREATE INDEX idx_orders_customer ON orders(customer_id);
CREATE INDEX idx_orders_status ON orders(status);
```

### Set Deadlock Priority

```sql
-- Prevent specific sessions from being chosen as victim
SET DEADLOCK_PRIORITY HIGH;
-- or
SET DEADLOCK_PRIORITY -10;  -- less likely to be victim
```

### Use Retry Logic

```sql
-- In application code: retry on deadlock
DECLARE @retry INT = 3;
WHILE @retry > 0
BEGIN
    BEGIN TRY
        -- your transaction
        SET @retry = 0;
    END TRY
    BEGIN CATCH
        IF ERROR_NUMBER() = 1205
        BEGIN
            SET @retry = @retry - 1;
            WAITFOR DELAY '00:00:01';
        END
        ELSE THROW;
    END CATCH
END
```

### Optimize Transaction Scope

```sql
-- Keep transactions short
BEGIN TRANSACTION;
    UPDATE accounts SET balance = balance - 100 WHERE id = 1;
    UPDATE accounts SET balance = balance + 100 WHERE id = 2;
COMMIT;
```

## Examples

```sql
-- Session 1
BEGIN TRANSACTION;
UPDATE accounts SET balance = 100 WHERE id = 1;  -- locks row 1

-- Session 2
BEGIN TRANSACTION;
UPDATE accounts SET balance = 200 WHERE id = 2;  -- locks row 2

-- Session 1 tries to update row 2 → waits for session 2
-- Session 2 tries to update row 1 → waits for session 1
-- DEADLOCK: one session is chosen as victim
-- Error 1205: Transaction (Process ID 5) was deadlocked
```

## Related Errors

- [Error 547]({{< relref "/tools/sqlserver/error-547" >}}) — CHECK constraint violation
- [Error 3621]({{< relref "/tools/sqlserver/error-3621" >}}) — statement terminated
