---
title: "SQL Server Restore Error"
description: "SQL Server restore operation fails."
tools: ["sqlserver"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
---

# SQL Server Restore Error

A SQL Server restore error occurs when a database restore operation fails. This can be caused by backup file issues, version incompatibility, or database state problems.

## Common Causes

- Backup file is corrupted or incomplete
- Version mismatch (backup from newer SQL Server)
- Database is in use during restore
- Insufficient disk space for restored database
- Backup set does not contain the expected data

## How to Fix

### Check Backup File

```sql
RESTORE HEADERONLY FROM DISK = '/backup/mydb_full.bak';
```

### Restore with REPLACE

```sql
RESTORE DATABASE mydb
FROM DISK = '/backup/mydb_full.bak'
WITH REPLACE, RECOVERY;
```

### Set Database to Single User

```sql
ALTER DATABASE mydb SET SINGLE_USER WITH ROLLBACK IMMEDIATE;
RESTORE DATABASE mydb FROM DISK = '/backup/mydb_full.bak';
ALTER DATABASE mydb SET MULTI_USER;
```

### Restore with Move

```sql
RESTORE DATABASE mydb
FROM DISK = '/backup/mydb_full.bak'
WITH MOVE 'mydb' TO '/var/opt/mssql/data/mydb.mdf',
     MOVE 'mydb_log' TO '/var/opt/mssql/data/mydb_log.ldf';
```

### Check Backup Set List

```sql
RESTORE VERIFYONLY FROM DISK = '/backup/mydb_full.bak';
```

### Restore Transaction Log

```sql
RESTORE LOG mydb
FROM DISK = '/backup/mydb_log.trn'
WITH NORECOVERY;
RESTORE DATABASE mydb WITH RECOVERY;
```

## Examples

```sql
RESTORE DATABASE mydb FROM DISK = '/backup/mydb.bak';
-- Msg 3101: Exclusive access could not be obtained because the database is in use.

-- Fix:
ALTER DATABASE mydb SET SINGLE_USER WITH ROLLBACK IMMEDIATE;
RESTORE DATABASE mydb FROM DISK = '/backup/mydb.bak';
ALTER DATABASE mydb SET MULTI_USER;
```

## Related Errors

- [Backup Error]({{< relref "/tools/sqlserver/sqlserver-backup-error" >}}) — backup failure
- [Replication Error]({{< relref "/tools/sqlserver/sqlserver-replication-error" >}}) — replication issues
