---
title: "[Solution] SQL Table Doesn't Exist Error Fix"
description: "Fix SQL errors when a query references a table that doesn't exist in the database."
languages: ["sql"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# SQL Table Doesn't Exist Error Fix

A SQL table not found error occurs when a query references a table that doesn't exist in the current database or schema.

## What This Error Means

The database cannot find the specified table. This happens when the table hasn't been created, you're using the wrong database/schema, or the table name is misspelled.

## Common Causes

- Table not created yet (missing migration/DDL)
- Wrong database or schema selected
- Typo in table name
- Table was dropped
- Missing schema prefix

## How to Fix

### 1. Check which database is selected

```sql
-- CORRECT: Verify current database
SELECT DATABASE();  -- MySQL
SELECT current_database();  -- PostgreSQL

-- Use fully qualified name
SELECT * FROM mydb.mytable WHERE id = 1;
```

### 2. List available tables

```sql
-- CORRECT: Show tables in current database
SHOW TABLES;  -- MySQL
\dt  -- PostgreSQL
SELECT table_name FROM information_schema.tables
WHERE table_schema = 'public';  -- PostgreSQL
```

### 3. Create table if missing

```sql
-- CORRECT: Create table
CREATE TABLE users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### 4. Use correct schema prefix

```sql
-- WRONG: Missing schema
SELECT * FROM users;

-- CORRECT: Include schema when needed
SELECT * FROM public.users;  -- PostgreSQL
SELECT * FROM dbo.users;  -- SQL Server
```

## Related Errors

- [SQL Column Not Found](sql-column-not-found-v2) — column missing
- [SQL Syntax Error](sql-syntax-error-v2) — syntax issues
- [SQL Access Denied](sql-access-denied-v2) — permission errors
