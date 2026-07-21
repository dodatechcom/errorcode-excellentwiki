---
title: "MySQL Table Corruption Error"
description: "MySQL detects table corruption during query execution"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# MySQL Table Corruption Error

MySQL detects table corruption during query execution

## Common Causes

- Disk write failure during table update
- Crash during InnoDB flush operation
- Memory corruption in buffer pool
- Hardware failure (bad sectors on disk)

## How to Fix

1. Check tables: `mysqlcheck --all-databases -u root -p`
2. Repair table: `REPAIR TABLE <table>;`
3. Check InnoDB: `CHECK TABLE <table> EXTENDED;`
4. Restore from backup if corruption severe

## Examples

```sql
-- Check table integrity
CHECK TABLE mydb.mytable EXTENDED;

-- Repair table (MyISAM)
REPAIR TABLE mydb.mytable;

-- Check all databases
-- Run from shell: mysqlcheck --all-databases -u root -p
```
