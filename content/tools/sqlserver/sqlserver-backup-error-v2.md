---
title: "SQL Server - backup device error"
description: "SQL Server backup fails because the backup device or target path cannot be written to"
tools: ["sqlserver"]
error-types: ["database-error"]
severities: ["error"]
tags: ["sqlserver", "backup", "device", "disk", "path", "write"]
weight: 5
---

A backup device error occurs when SQL Server cannot write the backup to the specified device or path. This can be caused by disk space issues, permission problems, or invalid device configuration.

## Common Causes

- Insufficient disk space for backup file
- Backup path does not exist or is not writable
- Device already in use by another backup operation
- Network path inaccessible
- SQL Server service account lacks write permissions

## How to Fix

1. Verify disk space:

```bash
df -h /var/opt/mssql/backup/
```

2. Check backup path exists:

```bash
ls -la /var/opt/mssql/backup/
mkdir -p /var/opt/mssql/backup/
```

3. Test backup to local disk:

```sql
BACKUP DATABASE mydb
TO DISK = '/var/opt/mssql/backup/mydb_full.bak'
WITH FORMAT, INIT, NAME = 'Full Backup';
```

4. Check SQL Server service permissions:

```bash
ls -la /var/opt/mssql/backup/
# Should show mssql:mssql ownership
chown mssql:mssql /var/opt/mssql/backup/
```

5. Verify backup device status:

```sql
SELECT name, physical_name, type_desc
FROM sys.backup_devices;
```

6. Clean up old backups to free space:

```bash
find /var/opt/mssql/backup/ -name "*.bak" -mtime +7 -delete
```

## Examples

```sql
-- Error: Cannot open backup device '/backup/mydb.bak'
BACKUP DATABASE mydb TO DISK = '/backup/mydb.bak';
-- Operating system error 2(The system cannot find the path specified.)

-- Fix: create directory first
-- In bash: mkdir -p /backup/
BACKUP DATABASE mydb TO DISK = '/backup/mydb.bak';
```

```sql
-- Error: There is not enough disk space
BACKUP DATABASE mydb TO DISK = '/var/opt/mssql/backup/mydb.bak';
-- Write error: "There is insufficient disk space to continue..."

-- Fix: free space or use different path
BACKUP DATABASE mydb TO DISK = '/tmp/mydb.bak';
```

## Related Errors

- [Restore error]({{< relref "/tools/sqlserver/sqlserver-restore-error" >}})
- [Connection error]({{< relref "/tools/sqlserver/sqlserver-connection-error" >}})
