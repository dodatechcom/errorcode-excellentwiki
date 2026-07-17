---
title: "SQL Server - transaction rollback error"
description: "SQL Server transaction fails to commit and must be rolled back due to errors or constraint violations"
tools: ["sqlserver"]
error-types: ["database-error"]
severities: ["error"]
tags: ["sqlserver", "transaction", "rollback", "commit", "xact"]
weight: 5
---

A transaction rollback error occurs when a SQL Server transaction encounters an error that forces it to roll back all changes. This can happen due to constraint violations, deadlock victim selection, or explicit ROLLBACK commands.

## Common Causes

- Constraint violation during transaction
- Deadlock causing victim rollback
- Explicit ROLLBACK triggered by error handling
- Log file full preventing commit
- XACT_ABORT ON causing automatic rollback on any error

## How to Fix

1. Use TRY/CATCH for proper error handling:

```sql
BEGIN TRY
  BEGIN TRANSACTION;
    INSERT INTO orders (id, amount) VALUES (1, 100);
    UPDATE accounts SET balance = balance - 100 WHERE id = 1;
    UPDATE accounts SET balance = balance + 100 WHERE id = 2;
  COMMIT TRANSACTION;
END TRY
BEGIN CATCH
  IF @@TRANCOUNT > 0
    ROLLBACK TRANSACTION;
  THROW;
END CATCH;
```

2. Check XACT_ABORT setting:

```sql
-- Default is OFF (individual statements can fail)
SET XACT_ABORT OFF;

-- When ON, any error rolls back the entire transaction
SET XACT_ABORT ON;
```

3. Check transaction state:

```sql
SELECT @@TRANCOUNT AS transaction_count;
-- Returns number of active transactions
```

4. Use SAVE TRANSACTION for partial rollbacks:

```sql
BEGIN TRANSACTION;
  INSERT INTO orders VALUES (1, 100);
  SAVE TRANSACTION savepoint1;
  BEGIN TRY
    INSERT INTO orders VALUES (2, 200);
  END TRY
  BEGIN CATCH
    ROLLBACK TRANSACTION savepoint1; -- undo only the failed part
  END CATCH;
COMMIT TRANSACTION;
```

5. Monitor transaction log usage:

```sql
SELECT
  name,
  log_reuse_wait_desc,
  recovery_model_desc
FROM sys.databases
WHERE name = 'mydb';
```

6. Check for orphaned transactions:

```sql
SELECT
  s.session_id,
  s.login_name,
  t.transaction_id,
  at.transaction_state
FROM sys.dm_tran_active_transactions at
JOIN sys.dm_tran_session_transactions t ON at.transaction_id = t.transaction_id
JOIN sys.dm_exec_sessions s ON t.session_id = s.session_id;
```

## Examples

```sql
-- Error: Transaction (Process ID 52) was deadlocked on lock resources
-- and has been chosen as the deadlock victim. ROLLBACK TRANSACTION.

BEGIN TRANSACTION;
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
-- ... deadlock occurs ...
-- Automatic rollback, all changes undone

-- Fix: add retry logic
DECLARE @retries INT = 3;
WHILE @retries > 0
BEGIN
  BEGIN TRY
    BEGIN TRANSACTION;
    UPDATE accounts SET balance = balance - 100 WHERE id = 1;
    COMMIT;
    SET @retries = 0;
  END TRY
  BEGIN CATCH
    ROLLBACK;
    SET @retries -= 1;
  END CATCH;
END
```

## Related Errors

- [Deadlock error]({{< relref "/tools/sqlserver/sqlserver-deadlock-error" >}})
- [Backup error]({{< relref "/tools/sqlserver/sqlserver-backup-error" >}})
