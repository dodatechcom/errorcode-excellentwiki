---
title: "SQL Server Lock Timeout Error"
description: "SQL Server lock wait exceeds the configured timeout."
tools: ["sqlserver"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
---

# SQL Server Lock Timeout Error

A SQL Server lock timeout error occurs when a transaction waits longer than the configured timeout to acquire a lock. This is different from deadlocks — here one transaction is blocking another.

## Common Causes

- Long-running query holding locks
- Uncommitted transactions blocking others
- Missing indexes causing large lock ranges
- Inappropriate isolation level

## How to Fix

### Set Lock Timeout

```sql
SET LOCK_TIMEOUT 5000;  -- 5 seconds
```

### Check Blocking Processes

```sql
SELECT blocking_session_id, session_id, wait_type, wait_time
FROM sys.dm_exec_requests
WHERE blocking_session_id > 0;
```

### Kill Blocking Process

```sql
KILL <blocking_session_id>;
```

### Find Long-Running Queries

```sql
SELECT session_id, start_time, status, command
FROM sys.dm_exec_requests
WHERE DATEDIFF(MINUTE, start_time, GETDATE()) > 10;
```

### Use NOLOCK Hint (Careful)

```sql
SELECT * FROM users WITH (NOLOCK) WHERE id = 1;
-- Reads uncommitted data, may be inaccurate
```

### Optimize Queries

```sql
-- Add appropriate indexes
CREATE INDEX idx_users_email ON users(email);
```

### Check Isolation Level

```sql
-- Use READ COMMITTED SNAPSHOT
ALTER DATABASE mydb SET READ_COMMITTED_SNAPSHOT ON;
```

## Examples

```sql
-- Transaction 1 holds lock
BEGIN TRANSACTION
UPDATE users SET name = 'Alice' WHERE id = 1;
-- Takes 30 seconds...

-- Transaction 2 times out
SET LOCK_TIMEOUT 5000;
SELECT * FROM users WHERE id = 1;
-- Lock request time out period exceeded.
```

## Related Errors

- [Deadlock Error]({{< relref "/tools/sqlserver/sqlserver-deadlock-error" >}}) — deadlock detected
- [Transaction Error]({{< relref "/tools/sqlserver/sqlserver-transaction-error" >}}) — transaction error
