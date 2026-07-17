---
title: "Oracle - ORA-01653: unable to extend table"
description: "Oracle cannot extend a table segment because the tablespace has no more free space available"
tools: ["oracle"]
error-types: ["database-error"]
severities: ["error"]
tags: ["oracle", "tablespace", "extend", "storage", "ora-01653", "space"]
weight: 5
---

ORA-01653: unable to extend table occurs when Oracle cannot allocate additional space for a table because the tablespace has no more free extents. This typically happens when the tablespace is full or autoextend is not enabled.

## Common Causes

- Tablespace is full and autoextend is disabled
- Datafile maxsize reached
- Large INSERT or bulk load consuming remaining space
- Tablespace not configured with autoextend
- Temporary tablespace full

## How to Fix

1. Check tablespace usage:

```sql
SELECT tablespace_name, round(sum_bytes/1024/1024/1024, 2) as used_gb,
       round(max_bytes/1024/1024/1024, 2) as max_gb,
       round((sum_bytes/max_bytes)*100, 1) as pct_used
FROM (
  SELECT tablespace_name,
         sum(bytes) as sum_bytes,
         sum(maxbytes) as max_bytes
  FROM dba_data_files
  GROUP BY tablespace_name
);
```

2. Add datafile to tablespace:

```sql
ALTER TABLESPACE users
ADD DATAFILE '/u01/oradata/mydb/users02.dbf'
SIZE 10G
AUTOEXTEND ON NEXT 1G MAXSIZE 50G;
```

3. Enable autoextend on existing datafile:

```sql
ALTER DATABASE DATAFILE '/u01/oradata/mydb/users01.dbf'
AUTOEXTEND ON NEXT 1G MAXSIZE 50G;
```

4. Resize existing datafile:

```sql
ALTER DATABASE DATAFILE '/u01/oradata/mydb/users01.dbf'
RESIZE 20G;
```

5. Drop unused objects to free space:

```sql
SELECT segment_name, segment_type, bytes/1024/1024 as size_mb
FROM dba_segments
WHERE tablespace_name = 'USERS'
ORDER BY bytes DESC;
```

## Examples

```sql
-- Error: ORA-01653: unable to extend table EMPLOYEES by 128 in tablespace USERS
INSERT INTO employees SELECT * FROM large_source_table;
-- ORA-01653: unable to extend table EMPLOYEES by 128 in tablespace USERS

-- Fix: add datafile
ALTER TABLESPACE users
ADD DATAFILE '/u01/oradata/mydb/users03.dbf'
SIZE 5G AUTOEXTEND ON;
```

## Related Errors

- [Sequence error]({{< relref "/tools/oracle/oracle-sequence-error" >}})
- [Tablespace error]({{< relref "/tools/oracle/oracle-tablespace-error" >}})
