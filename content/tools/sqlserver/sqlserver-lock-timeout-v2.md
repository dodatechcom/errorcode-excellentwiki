---
title: "SQL Server - lock request timeout exceeded"
description: "SQL Server session times out waiting to acquire a lock held by another session"
tools: ["sqlserver"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
---

A lock request timeout error occurs when a SQL Server session waits longer than the configured timeout to acquire a lock held by another session. Unlike deadlocks, this is a simple lock contention issue where one session blocks another.

## Common Causes

- Long-running transaction holding exclusive locks
- Missing indexes causing lock escalation
- UPDATE or DELETE operations on large tables without proper isolation
- Lock timeout too short for the workload
- Blocking chains involving multiple sessions

## How to Fix

1. Increase the lock timeout:

```sql
-- Set lock timeout to 60 seconds (default is -1 = wait forever)
SET LOCK_TIMEOUT 60000;
```

2. Find blocking sessions:

```sql
SELECT
  blocking.session_id AS blocking_session,
  blocked.session_id AS blocked_session,
  blocked.wait_type,
  blocked.wait_time,
  t.text AS blocking_sql
FROM sys.dm_exec_requests blocked
JOIN sys.dm_exec_sessions blocking
  ON blocked.blocking_session_id = blocking.session_id
CROSS APPLY sys.dm_exec_sql_text(blocking.most_recent_sql_handle) t
WHERE blocked.blocking_session_id > 0;
```

3. Kill the blocking session:

```sql
KILL blocking_session_id;
```

4. Use snapshot isolation to reduce blocking:

```sql
ALTER DATABASE mydb SET READ_COMMITTED_SNAPSHOT ON;
-- Then use snapshot isolation level
SET TRANSACTION ISOLATION LEVEL SNAPSHOT;
```

5. Optimize queries to reduce lock scope:

```sql
-- Instead of updating all rows
UPDATE orders SET status = 'processed';

-- Update in batches
WHILE 1 = 1
BEGIN
  UPDATE TOP (1000) orders
  SET status = 'processed'
  WHERE status = 'pending';

  IF @@ROWCOUNT = 0 BREAK;
END
```

6. Check lock escalation settings:

```sql
-- Prevent lock escalation on a table
ALTER TABLE orders SET (LOCK_ESCALATION = DISABLE);
```

## Examples

```sql
-- Error: Lock request time out period exceeded.
SET LOCK_TIMEOUT 5000;
SELECT * FROM orders WHERE id = 1 FOR UPDATE;
-- Lock request time out period exceeded.

-- Fix: increase timeout or find blocker
SET LOCK_TIMEOUT 60000;
-- Or check who is blocking
SELECT * FROM sys.dm_exec_requests WHERE blocking_session_id > 0;
```

## Related Errors

- [Deadlock error]({{< relref "/tools/sqlserver/sqlserver-deadlock-error" >}})
- [Transaction error]({{< relref "/tools/sqlserver/sqlserver-transaction-error" >}})
