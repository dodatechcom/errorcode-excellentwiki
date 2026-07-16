---
title: "ERROR 1050 (42S01): Table 'X' already exists"
description: "Attempted to create a MySQL table that already exists"
tools: ["mysql"]
error-types: ["database-error"]
severities: ["error"]
tags: ["table", "create", "duplicate", "schema"]
weight: 5
---

This error occurs when you try to create a table with a name that already exists in the database.

## Common Causes

- Running CREATE TABLE twice with the same name
- Script executed multiple times without idempotency
- Migration rerun without DROP TABLE
- Schema drift between environments

## How to Fix

1. Use `IF NOT EXISTS` to avoid the error:

```sql
CREATE TABLE IF NOT EXISTS mytable (
    id INT PRIMARY KEY,
    name VARCHAR(255)
);
```

2. Check if the table exists:

```sql
SHOW TABLES LIKE 'mytable';
```

3. Drop the existing table if needed:

```sql
DROP TABLE IF EXISTS mytable;
```

## Examples

```sql
-- This will fail if mytable already exists
CREATE TABLE mytable (id INT PRIMARY KEY);

-- Error output:
-- ERROR 1050 (42S01): Table 'mytable' already exists

-- Safe approach:
CREATE TABLE IF NOT EXISTS mytable (id INT PRIMARY KEY);
```

```bash
# Check if table exists via command line
mysql -e "SHOW TABLES LIKE 'mytable';" mydb

# Create only if not exists
mysql -e "CREATE TABLE IF NOT EXISTS mytable (id INT);" mydb
```

## Related Errors

- [Access Denied](/tools/mysql/access-denied)
- [Database Already Exists](/tools/postgresql/database-exists)
