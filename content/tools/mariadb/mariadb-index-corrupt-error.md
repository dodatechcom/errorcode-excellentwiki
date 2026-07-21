---
title: "[Solution] MariaDB Index Corrupt Error"
description: "Fix MariaDB index corruption errors when indexes become damaged and queries fail"
tools: ["mariadb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# MariaDB Index Corrupt Error

Index corruption errors occur when MariaDB detects that an index structure is damaged.

## Common Causes

- Server crash during index write
- Disk hardware failure
- Memory corruption during index rebuild
- Power outage during ALTER TABLE

## Common Error Messages

```
ERROR 144 (HY000): Table './mydb/my_table' is marked as crashed and should be repaired
```

## How to Fix It

### 1. Check Table Status

```sql
CHECK TABLE my_table EXTENDED;
```

### 2. Repair Table

```sql
REPAIR TABLE my_table;
```

### 3. Rebuild Index

```sql
ALTER TABLE my_table ENGINE=InnoDB;
```

## Examples

```sql
SELECT table_name, engine, table_rows FROM information_schema.TABLES
WHERE table_schema = 'mydb';
```
