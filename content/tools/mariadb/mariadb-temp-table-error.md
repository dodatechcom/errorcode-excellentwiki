---
title: "[Solution] MariaDB Temp Table Error"
description: "Fix MariaDB temporary table errors when creating or using temporary tables fails"
tools: ["mariadb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# MariaDB Temp Table Error

Temporary table errors occur when MariaDB cannot create or manage temporary tables correctly.

## Common Causes

- tmp_table_size or max_heap_table_size too small
- Too many temporary tables on disk
- Temporary table name collision
- Disk full preventing temp table creation

## Common Error Messages

```
ERROR 1114 (HY000): The table 'my_tmp_table' is full
```

## How to Fix It

### 1. Check Temp Table Settings

```sql
SHOW VARIABLES LIKE '%tmp_table_size%';
SHOW VARIABLES LIKE '%max_heap_table_size%';
```

### 2. Increase Temp Table Size

```sql
SET SESSION tmp_table_size = 67108864;
SET SESSION max_heap_table_size = 67108864;
```

### 3. Check Temp Table Usage

```sql
SHOW STATUS LIKE 'Created_tmp%';
```

## Examples

```sql
SELECT * FROM information_schema.TABLES WHERE table_type = 'TEMPORARY';
```
