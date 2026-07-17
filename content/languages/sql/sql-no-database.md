---
title: "[Solution] SQL No Database Selected Fix"
description: "Fix 'No database selected' when running a SQL query without selecting a database first."
languages: ["sql"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

This error occurs when a SQL query references a table without a database prefix and no database has been selected with `USE`. The message reads: `No database selected`.

## What This Error Means

The database server does not know which database context to use for the query. You must either select a database with `USE` or prefix table names with the database name.

## Common Causes

- Missing `USE database_name` before the query
- Connection does not have a default database set
- Using a table name without database prefix

## How to Fix

### Fix 1: Select the database first

```sql
USE my_database;
SELECT * FROM users;
```

### Fix 2: Prefix table names with database

```sql
SELECT * FROM my_database.users;
```

### Fix 3: Set default database in connection string

```sql
-- MySQL
mysql -u root -p -D my_database

-- Or in connection string
-- jdbc:mysql://localhost:3306/my_database
```

## Examples

```sql
SELECT * FROM users;
-- ERROR 1046: No database selected

-- Fix
USE shop;
SELECT * FROM users;
```

## Related Errors

- [Table Not Found](table-not-found.md) — table doesn't exist in selected database
- [Access Denied](access-denied.md) — no permission to use the database
