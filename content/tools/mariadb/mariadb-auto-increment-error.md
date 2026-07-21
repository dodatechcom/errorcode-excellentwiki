---
title: "[Solution] MariaDB Auto Increment Error"
description: "Fix MariaDB auto-increment errors when ID generation fails or produces duplicates"
tools: ["mariadb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# MariaDB Auto Increment Error

Auto-increment errors occur when MariaDB cannot generate unique sequential IDs for new rows.

## Common Causes

- Auto-increment value exhausted (unsigned int overflow)
- Table truncated resetting auto-increment
- InnoDB auto-increment lock contention
- Mixing InnoDB and MyISAM tables

## Common Error Messages

```
ERROR 1062 (23000): Duplicate entry for key 'PRIMARY'
```

## How to Fix It

### 1. Check Current Auto-Increment

```sql
SHOW CREATE TABLE my_table;
```

### 2. Reset Auto-Increment

```sql
ALTER TABLE my_table AUTO_INCREMENT = 1;
```

### 3. Use Larger Integer Type

```sql
ALTER TABLE my_table MODIFY id BIGINT UNSIGNED AUTO_INCREMENT;
```

## Examples

```sql
SELECT MAX(id) + 1 AS next_id FROM my_table;
```
