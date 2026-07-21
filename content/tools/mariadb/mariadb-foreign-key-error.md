---
title: "[Solution] MariaDB Foreign Key Error"
description: "Fix MariaDB foreign key errors when constraint references fail or block operations"
tools: ["mariadb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# MariaDB Foreign Key Error

Foreign key errors occur when MariaDB cannot create, enforce, or drop foreign key constraints.

## Common Causes

- Referenced table does not have matching index
- Foreign key column type mismatch
- Trying to drop table with foreign key references
- Circular foreign key references

## Common Error Messages

```
ERROR 1215 (HY000): Cannot add foreign key constraint
```

## How to Fix It

### 1. Check Foreign Keys

```sql
SELECT * FROM information_schema.TABLE_CONSTRAINTS
WHERE CONSTRAINT_TYPE = 'FOREIGN KEY' AND TABLE_NAME = 'my_table';
```

### 2. Create Index on Referenced Column

```sql
CREATE INDEX idx_id ON parent_table (id);
```

### 3. Disable Checks Temporarily

```sql
SET FOREIGN_KEY_CHECKS = 0;
-- perform operation
SET FOREIGN_KEY_CHECKS = 1;
```

## Examples

```sql
SELECT CONSTRAINT_NAME, TABLE_NAME, COLUMN_NAME, REFERENCED_TABLE_NAME
FROM information_schema.KEY_COLUMN_USAGE
WHERE REFERENCED_TABLE_NAME IS NOT NULL;
```
