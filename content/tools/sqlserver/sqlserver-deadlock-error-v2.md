---
title: "SQL Server - deadlock victim selected"
description: "SQL Server detects a deadlock between two or more sessions and terminates one as the victim"
tools: ["sqlserver"]
error-types: ["database-error"]
severities: ["error"]
tags: ["sqlserver", "deadlock", "victim", "lock", "graph", "transaction"]
weight: 5
---

A deadlock victim selected error occurs when SQL Server detects two or more sessions blocking each other in a circular pattern. SQL Server automatically terminates one session (the victim) to break the deadlock and allow the other to proceed.

## Common Causes

- Two transactions acquiring locks in opposite order
- Missing indexes causing table scans with locks
- Long-running transactions holding locks
- Hot table contention from concurrent inserts
- Foreign key constraints causing lock escalation

## How to Fix

1. Enable deadlock tracing:

```sql
-- Enable trace flag 1222 for detailed deadlock logs
DBCC TRACEON(1222, -1);

-- Check deadlock graph from Extended Events
SELECT * FROM sys.fn_xe_file_target_read_file('system_health*');
```

2. Add proper indexes to reduce lock scope:

```sql
-- Missing index causes table scan
CREATE INDEX idx_orders_customer ON orders(customer_id);
CREATE INDEX idx_orders_status ON orders(status);
```

3. Use deadlock priority to control victim selection:

```sql
SET DEADLOCK_PRIORITY LOW; -- or HIGH, NORMAL
```

4. Reduce transaction duration:

```sql
-- Bad: long transaction
BEGIN TRANSACTION;
  UPDATE accounts SET balance = balance - 100 WHERE id = 1;
  -- ... many more operations ...
  UPDATE accounts SET balance = balance + 100 WHERE id = 2;
COMMIT;

-- Better: minimize transaction scope
BEGIN TRANSACTION;
  UPDATE accounts SET balance = balance - 100 WHERE id = 1;
COMMIT;
BEGIN TRANSACTION;
  UPDATE accounts SET balance = balance + 100 WHERE id = 2;
COMMIT;
```

5. Use TRY/CATCH for deadlock retry logic:

```sql
DECLARE @retry INT = 3;
WHILE @retry > 0
BEGIN
  BEGIN TRY
    -- Your transaction here
    SET @retry = 0;
  END TRY
  BEGIN CATCH
    IF ERROR_NUMBER() = 1205 -- deadlock
    BEGIN
      SET @retry = @retry - 1;
      WAITFOR DELAY '00:00:01'; -- wait 1 second
    END
    ELSE
      THROW;
  END CATCH
END
```

6. Use snapshot isolation:

```sql
ALTER DATABASE mydb SET READ_COMMITTED_SNAPSHOT ON;
```

## Examples

```sql
-- Deadlock detected
-- Process 528dead88 was selected as the victim.
-- TranCount: 2
-- U locks: (0x68e64e7c0) (keylock...)

-- Check deadlock details
SELECT * FROM sys.dm_tran_locks;
SELECT * FROM sys.dm_exec_requests WHERE blocking_session_id > 0;
```

## Related Errors

- [Lock timeout]({{< relref "/tools/sqlserver/sqlserver-lock-timeout" >}})
- [Transaction error]({{< relref "/tools/sqlserver/sqlserver-transaction-error" >}})
