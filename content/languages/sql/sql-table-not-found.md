---
title: "[Solution] SQL Table Not Found Error Fix"
description: "Fix 'Table X doesn't exist' when a SQL query references a table that does not exist in the database."
languages: ["sql"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

This error occurs when a SQL query references a table that does not exist in the current database. The message reads: `Table 'X' doesn't exist`.

## What This Error Means

The database cannot find the specified table in the current schema. This can happen because the table was never created, was dropped, or you're using the wrong database name.

## Common Causes

- Table was never created or was dropped
- Wrong database selected (`USE database_name`)
- Table name misspelled in the query
- Table exists in a different schema

## How to Fix

### Fix 1: Check available tables

```sql
SHOW TABLES;
-- or
SELECT table_name FROM information_schema.tables
WHERE table_schema = DATABASE();
```

### Fix 2: Verify database selection

```sql
USE my_database;
SHOW TABLES;

-- Now query the correct table
SELECT * FROM users;
```

### Fix 3: Check for table name case sensitivity

```sql
-- Some databases are case-sensitive
-- Wrong on Linux MySQL
SELECT * FROM Users;

-- Correct
SELECT * FROM users;
```

## Examples

```sql
SELECT * FROM orders;
-- ERROR 1146: Table 'shop.orders' doesn't exist

-- Fix: check the correct database
USE ecommerce;
SHOW TABLES;
SELECT * FROM orders;
```

## Related Errors

- [Column Not Found](column-not-found.md) — the table exists but column doesn't
- [Syntax Error](syntax-error.md) — malformed SQL
