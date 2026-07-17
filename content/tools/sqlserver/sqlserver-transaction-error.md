---
title: "SQL Server Transaction Error"
description: "SQL Server transaction fails due to errors or rollback."
tools: ["sqlserver"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
---

# SQL Server Transaction Error

A SQL Server transaction error occurs when a transaction fails and must be rolled back. This can be caused by constraint violations, errors in the transaction, or explicit rollback commands.

## Common Causes

- Constraint violation causes automatic rollback
- Error in transaction without TRY/CATCH
- Transaction log full
- XACT_ABORT setting causes rollback on error

## How to Fix

### Use TRY/CATCH

```sql
BEGIN TRY
    BEGIN TRANSACTION;
    INSERT INTO users VALUES (1, 'Alice');
    UPDATE accounts SET balance = balance - 100 WHERE id = 1;
    COMMIT;
END TRY
BEGIN CATCH
    IF @@TRANCOUNT > 0
        ROLLBACK;
    THROW;
END CATCH;
```

### Check XACT_ABORT Setting

```sql
SET XACT_ABORT ON;  -- Auto rollback on error
SET XACT_ABORT OFF; -- Continue after error
```

### Handle Transaction Log

```sql
-- Check log usage
DBCC SQLPERF(LOGSPACE);

-- Backup log
BACKUP LOG mydb TO DISK = '/backup/mydb_log.trn';
```

### Use SAVE TRANSACTION

```sql
BEGIN TRANSACTION;
SAVE TRANSACTION savepoint1;
-- Do something
IF @error GOTO rollback_label;
COMMIT;
```

### Check @@TRANCOUNT

```sql
SELECT @@TRANCOUNT;
-- Always ensure it's 0 after transaction completes
```

### Set Deadlock Priority

```sql
SET DEADLOCK_PRIORITY NORMAL;
```

## Examples

```sql
BEGIN TRANSACTION;
INSERT INTO users VALUES (1, 'Alice');
-- Constraint violation occurs
-- Transaction is automatically rolled back
COMMIT;
-- Msg 3621: The statement has been terminated.
```

## Related Errors

- [Deadlock Error]({{< relref "/tools/sqlserver/sqlserver-deadlock-error" >}}) — deadlock detected
- [Lock Timeout Error]({{< relref "/tools/sqlserver/sqlserver-lock-timeout-error" >}}) — lock timeout
- [Backup Error]({{< relref "/tools/sqlserver/sqlserver-backup-error" >}}) — backup failure
