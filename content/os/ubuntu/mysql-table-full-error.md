---
title: "MySQL Table is Full Error"
description: "MySQL reports table is full and cannot accept new data"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# MySQL Table is Full Error

MySQL reports table is full and cannot accept new data

## Common Causes

- Table has reached max table size limit
- Disk space exhausted on MySQL data partition
- Tablespace file size exceeds ext4 max file size
- InnoDB tablespace autoextend exhausted

## How to Fix

1. Check disk space: `df -h /var/lib/mysql/`
2. Check table size: `SELECT table_name, data_length FROM information_schema.tables;`
3. Add disk space or move tablespace to larger disk
4. Consider partitioning large tables

## Examples

```sql
-- Check table sizes
SELECT table_name, round(data_length/1024/1024) as 'Size MB' FROM information_schema.tables WHERE table_schema='mydb';

-- Check InnoDB tablespace
SHOW TABLE STATUS LIKE 'mytable';
```
