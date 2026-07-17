---
title: "SQL Server Backup Error"
description: "SQL Server backup operation fails."
tools: ["sqlserver"]
error-types: ["database-error"]
severities: ["error"]
tags: ["sqlserver", "backup", "full", "differential", "log"]
weight: 5
---

# SQL Server Backup Error

A SQL Server backup error occurs when a database backup operation fails. Backups are critical for data protection and disaster recovery.

## Common Causes

- Insufficient disk space for backup file
- Backup path does not exist or is not writable
- Database is in an inconsistent state
- VSS (Volume Shadow Copy) issues
- Backup permissions insufficient

## How to Fix

### Check Disk Space

```sql
EXEC xp_fixeddrives;
```

### Create Backup Directory

```bash
mkdir -p /var/opt/mssql/backup
chown mssql:mssql /var/opt/mssql/backup
```

### Backup with T-SQL

```sql
BACKUP DATABASE mydb
TO DISK = '/var/opt/mssql/backup/mydb_full.bak'
WITH FORMAT, COMPRESSION,
NAME = 'My Database Full Backup';
```

### Check Backup History

```sql
SELECT database_name, backup_finish_date, type
FROM msdb.dbo.backupset
ORDER BY backup_finish_date DESC;
```

### Fix Permissions

```bash
# On Linux
sudo chown mssql:mssql /var/opt/mssql/backup
```

### Backup Transaction Log

```sql
BACKUP LOG mydb
TO DISK = '/var/opt/mssql/backup/mydb_log.trn'
WITH NOFORMAT, NOINIT;
```

## Examples

```sql
BACKUP DATABASE mydb TO DISK = '/backup/mydb.bak';
-- Msg 3201: Cannot open backup device '/backup/mydb.bak'.
-- Operating system error 2(The system cannot find the file specified.)

-- Fix: create directory and retry
```

## Related Errors

- [Restore Error]({{< relref "/tools/sqlserver/sqlserver-restore-error" >}}) — restore failure
- [Transaction Error]({{< relref "/tools/sqlserver/sqlserver-transaction-error" >}}) — transaction error
