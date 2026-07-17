---
title: "Oracle LOB Error"
description: "Oracle LOB (Large Object) operations fail during read, write, or manipulation."
tools: ["oracle"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
---

# Oracle LOB Error

An Oracle LOB error occurs when operations on Large Object (LOB) data types (CLOB, BLOB, NCLOB, BFILE) fail. LOBs store large text or binary data.

## Common Causes

- LOB segment is full
- LOB column exceeds maximum size
- LOB locator is invalid or expired
- LOB storage parameters not configured

## How to Fix

### Check LOB Segment Usage

```sql
SELECT table_name, column_name, segment_name
FROM user_lobs
WHERE table_name = 'MY_TABLE';
```

### Check LOB Space

```sql
SELECT tablespace_name, SUM(bytes)/1024/1024 AS mb
FROM user_segments
WHERE segment_type = 'LOBSEGMENT'
GROUP BY tablespace_name;
```

### Add LOB Space

```sql
ALTER TABLE my_table MODIFY lob(my_clob) (
  ALTER STORAGE (NEXT 10M)
);
```

### Read LOB Data

```sql
SELECT DBMS_LOB.SUBSTR(my_clob, 100, 1) FROM my_table WHERE id = 1;
```

### Write LOB Data

```sql
UPDATE my_table SET my_clob = TO_CLOB('New content') WHERE id = 1;
```

### Check LOB Inode

```sql
SELECT id, INSTR(my_clob, 'search text') FROM my_table;
```

### Fix LOB Corruption

```sql
-- Check for corrupted LOBs
SELECT id FROM my_table
WHERE DBMS_LOB.INSTR(my_clob, CHR(0)) > 0;
```

## Examples

```sql
INSERT INTO documents (id, content) VALUES (1, TO_CLOB('Large text...'));
-- ORA-01691: unable to extend lob segment SYS_LOB001

-- Fix: add tablespace
ALTER TABLESPACE lob_data ADD DATAFILE 'lob02.dbf' SIZE 1G;
```

## Related Errors

- [Tablespace Error]({{< relref "/tools/oracle/oracle-tablespace-error" >}}) — tablespace issues
- [Permission Error]({{< relref "/tools/oracle/permission-error" >}}) — permission denied
