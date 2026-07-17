---
title: "Oracle - ORA-00054: resource busy (NOWAIT)"
description: "Oracle operation fails because the requested resource is locked by another session and NOWAIT was specified"
tools: ["oracle"]
error-types: ["database-error"]
severities: ["error"]
tags: ["oracle", "lock", "busy", "nowait", "ora-00054", "contention"]
weight: 5
---

ORA-00054: resource busy and acquire with NOWAIT specified or timeout expired occurs when a DDL or SELECT FOR UPDATE statement tries to access a table that is currently locked by another session, and the NOWAIT option prevents waiting.

## Common Causes

- Another session holds an exclusive lock on the table
- Long-running transaction holding locks
- DDL operation on a table with active DML
- SELECT FOR UPDATE with NOWAIT on locked rows
- Application not releasing connections/locks promptly

## How to Fix

1. Check what is locking the table:

```sql
SELECT s.serial#, s.sid, s.username, l.locked_mode, o.object_name
FROM v$locked_object l
JOIN dba_objects o ON l.object_id = o.object_id
JOIN v$session s ON l.session_id = s.sid
WHERE o.object_name = 'EMPLOYEES';
```

2. Remove the blocking session:

```sql
-- Kill the blocking session
ALTER SYSTEM KILL SESSION 'sid,serial#' IMMEDIATE;
```

3. Use WAIT with timeout instead of NOWAIT:

```sql
SELECT * FROM employees WHERE employee_id = 100
FOR UPDATE WAIT 30; -- wait up to 30 seconds
```

4. Use LOCK TABLE with WAIT option:

```sql
LOCK TABLE employees IN EXCLUSIVE MODE WAIT 60;
```

5. Check for lock chains:

```sql
SELECT
  s.sid, s.serial#, s.username, s.blocking_session,
  o.object_name, l.locked_mode
FROM v$locked_object l
JOIN dba_objects o ON l.object_id = o.object_id
JOIN v$session s ON l.session_id = s.sid;
```

6. Reduce transaction duration to minimize lock contention:

```sql
-- Commit frequently during batch operations
BEGIN
  FOR rec IN (SELECT * FROM large_table) LOOP
    -- process
    COMMIT; -- release locks periodically
  END LOOP;
END;
```

## Examples

```sql
-- Error: ORA-00054: resource busy and acquire with NOWAIT specified
SELECT * FROM employees WHERE employee_id = 100 FOR UPDATE NOWAIT;
-- ORA-00054: resource busy and acquire with NOWAIT specified or timeout expired

-- Fix: use WAIT instead
SELECT * FROM employees WHERE employee_id = 100 FOR UPDATE WAIT 30;
```

## Related Errors

- [Flashback error]({{< relref "/tools/oracle/oracle-flashback-error" >}})
- [Trigger error]({{< relref "/tools/oracle/oracle-trigger-error" >}})
