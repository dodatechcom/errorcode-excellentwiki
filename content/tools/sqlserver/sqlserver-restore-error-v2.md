---
title: "SQL Server - restore database failed"
description: "SQL Server restore operation fails due to file access issues, version incompatibility, or backup corruption"
tools: ["sqlserver"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
---

A restore database failed error occurs when SQL Server cannot complete a database restore operation. This can happen due to incompatible backup files, missing data/log files, or permission issues on the restore target.

## Common Causes

- Backup file corrupted or incomplete
- Target database already in use (RESTRICTED_USER not set)
- Insufficient disk space for restored database
- Backup from different SQL Server version
- Missing log file for point-in-time recovery

## How to Fix

1. Check backup file validity:

```sql
RESTORE VERIFYONLY
FROM DISK = '/var/opt/mssql/backup/mydb.bak';
```

2. List backup contents:

```sql
RESTORE FILELISTONLY
FROM DISK = '/var/opt/mssql/backup/mydb.bak';
```

3. Restore with REPLACE to overwrite existing:

```sql
RESTORE DATABASE mydb
FROM DISK = '/var/opt/mssql/backup/mydb.bak'
WITH REPLACE, RECOVERY;
```

4. Set database to single user mode before restore:

```sql
ALTER DATABASE mydb SET SINGLE_USER WITH ROLLBACK IMMEDIATE;
RESTORE DATABASE mydb FROM DISK = '/var/opt/mssql/backup/mydb.bak' WITH REPLACE;
ALTER DATABASE mydb SET MULTI_USER;
```

5. Check SQL Server version compatibility:

```sql
SELECT @@VERSION;
-- Restore requires same or newer SQL Server version
```

6. Monitor restore progress:

```sql
SELECT session_id, command, percent_complete
FROM sys.dm_exec_requests
WHERE command = 'RESTORE';
```

## Examples

```sql
-- Error: The database cannot be opened because it is version 869
RESTORE DATABASE mydb FROM DISK = '/backup/mydb.bak';
-- This backup was created with SQL Server 2022 (version 869)
-- Cannot restore to SQL Server 2019 (version 863)

-- Fix: upgrade SQL Server or restore to compatible version
```

```sql
-- Error: Directory listing for the full backup set is incomplete
RESTORE DATABASE mydb FROM DISK = '/backup/mydb.bak';
-- Fix: verify backup first
RESTORE VERIFYONLY FROM DISK = '/backup/mydb.bak';
```

## Related Errors

- [Backup error]({{< relref "/tools/sqlserver/sqlserver-backup-error" >}})
- [Connection error]({{< relref "/tools/sqlserver/sqlserver-connection-error" >}})
