---
title: "[Solution] MySQL Index Corruption Error"
description: "Fix MySQL index corruption error when InnoDB or MyISAM indexes become inconsistent and cause query failures"
tools: ["mysql"]
error-types: ["tool-error"]
severities: ["error"]
---

# MySQL Index Corruption Error

MySQL detects inconsistency between index entries and actual table data. Corrupted indexes produce wrong query results, crashes, or explicit corruption errors.

## Common Causes

- Server crashed during an index build or write operation
- Hardware disk errors wrote partial index pages
- Bug in MySQL version corrupted the index structure
- Incomplete ALTER TABLE operation left indexes in inconsistent state
- Power failure during concurrent DDL and DML operations

## How to Fix

### Check MyISAM Index Integrity

```sql
-- Check for corruption
CHECK TABLE orders EXTENDED;

-- Repair corrupted MyISAM table
REPAIR TABLE orders;

-- Or using myisamchk
-- $ myisamchk --check /var/lib/mysql/mydb/orders
-- $ myisamchk --recover /var/lib/mysql/mydb/orders
```

### Rebuild InnoDB Indexes

```sql
-- Rebuild table (creates new indexes)
ALTER TABLE orders ENGINE=InnoDB;

-- Or use OPTIMIZE TABLE
OPTIMIZE TABLE orders;
```

### Rebuild Specific Index

```sql
-- Drop and recreate the index
ALTER TABLE orders DROP INDEX idx_status;
ALTER TABLE orders ADD INDEX idx_status (status);
```

### Check InnoDB Tablespace Consistency

```sql
-- MySQL 8.0+: use innodb_checksum_algorithm
SELECT @@innodb_checksum_algorithm;

-- Force checksum verification
SET GLOBAL innodb_checksum_algorithm = crc32;
ALTER TABLE orders ENGINE=InnoDB;
```

### Recover from Crash Recovery

```bash
# Check InnoDB error log for corruption details
tail -100 /var/log/mysql/error.log

# If needed, force InnoDB recovery
# Edit my.cnf:
# innodb_force_recovery = 1  (try 1-6)
# Start MySQL, export data, recreate tables
```

## Examples

```
ERROR 144 (HY000): Table './mydb/orders' is marked as crashed
  and should be repaired

[ERROR] InnoDB: Page [page id] is corrupt, unable to read.
  You may need to recover from a backup.
```

## Related Errors

- [MySQL InnoDB Error]({{< relref "/tools/mysql/mysql-innodb-error" >}}) -- InnoDB issues
- [MySQL Crash Recovery]({{< relref "/tools/mysql/mysql-crash-recovery" >}}) -- crash recovery
- [MySQL Optimize Table]({{< relref "/tools/mysql/mysql-optimize-table" >}}) -- table optimization
