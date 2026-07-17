---
title: "Oracle Tablespace Error"
description: "Oracle tablespace is full or encounters storage issues."
tools: ["oracle"]
error-types: ["database-error"]
severities: ["error"]
tags: ["oracle", "tablespace", "storage", "quota", "space"]
weight: 5
---

# Oracle Tablespace Error

An Oracle tablespace error occurs when the tablespace is full, has insufficient space, or encounters storage allocation issues. This prevents DDL and DML operations.

## Common Causes

- Tablespace is full (datafile cannot extend)
- Tablespace autoextend is disabled
- User quota on tablespace exceeded
- Temporary tablespace is full

## How to Fix

### Check Tablespace Usage

```sql
SELECT tablespace_name,
       ROUND(SUM(bytes)/1024/1024) AS used_mb,
       ROUND(SUM(maxbytes)/1024/1024) AS max_mb
FROM dba_data_files
GROUP BY tablespace_name;
```

### Add Datafile

```sql
ALTER TABLESPACE users ADD DATAFILE '/path/to/newfile.dbf' SIZE 1G AUTOEXTEND ON;
```

### Enable Autoextend

```sql
ALTER DATABASE DATAFILE '/path/to/file.dbf' AUTOEXTEND ON MAXSIZE 10G;
```

### Check User Quota

```sql
SELECT tablespace_name, bytes, max_bytes
FROM dba_ts_quotas
WHERE username = 'MYUSER';
```

### Increase User Quota

```sql
ALTER USER myuser QUOTA 5G ON users;
```

### Check Temporary Tablespace

```sql
SELECT tablespace_name, SUM(bytes)/1024/1024 AS temp_mb
FROM dba_temp_files
GROUP BY tablespace_name;
```

## Examples

```sql
INSERT INTO big_table VALUES (1, 'data');
ORA-01653: unable to extend table ADMIN.BIG_TABLE by 128 in tablespace USERS

-- Fix: add datafile
ALTER TABLESPACE users ADD DATAFILE '/u01/oradata/users02.dbf' SIZE 2G;
```

## Related Errors

- [Permission Error]({{< relref "/tools/oracle/permission-error" >}}) — permission denied
- [Sequence Error]({{< relref "/tools/oracle/sequence-error" >}}) — sequence issues
