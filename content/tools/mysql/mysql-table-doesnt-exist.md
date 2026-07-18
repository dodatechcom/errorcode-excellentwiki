---
title: "[Solution] MySQL Table Does Not Exist - Fix Missing Table Errors"
description: "Fix MySQL table does not exist errors by verifying table names, checking the active database, and ensuring correct case sensitivity settings"
tools: ["mysql"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
---

# MySQL Table Does Not Exist

This error occurs when a SQL statement references a table that is not found in the current database. The table may have been dropped, the name may be wrong, or the wrong database is selected.

## What This Error Means

MySQL returns this error when it cannot find the table:

```
ERROR 1146 (42S02): Table 'mydb.mytable' does not exist
```

The error includes the database and table name. MySQL checks for the table in the currently selected database (`USE mydb`). If the table exists in a different database, you must prefix it with the database name.

## Why It Happens

- The table was dropped and not recreated
- A typo in the table name
- The wrong database is selected with `USE`
- Case sensitivity: on Linux, `mytable` and `MyTable` are different tables
- The table was created in a different database
- A migration script ran partially and did not create all tables
- The table was renamed without updating all references

## How to Fix It

### 1. Check Which Tables Exist

```sql
-- List tables in the current database
SHOW TABLES;

-- Search across all databases
SELECT TABLE_SCHEMA, TABLE_NAME
FROM information_schema.TABLES
WHERE TABLE_NAME = 'mytable';
```

### 2. Verify the Current Database

```sql
-- Check which database is selected
SELECT DATABASE();

-- Select the correct database
USE mydb;
```

### 3. Use IF EXISTS for Idempotent Operations

```sql
-- Safe drop
DROP TABLE IF EXISTS mytable;

-- Safe create
CREATE TABLE IF NOT EXISTS mytable (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL
);
```

### 4. Check Case Sensitivity

```sql
-- On Linux, table names are case-sensitive by default
-- Check the lower_case_table_names setting
SHOW VARIABLES LIKE 'lower_case_table_names';

-- 0 = case-sensitive (Linux default)
-- 1 = case-insensitive (stores in lowercase)
-- 2 = case-insensitive for查找, preserves case on disk
```

### 5. Check Table Naming with Backticks

```sql
-- Use backticks to escape reserved words and special characters
SELECT * FROM `order`;

-- Without backticks, MySQL may interpret "order" as a keyword
```

## Common Mistakes

- Assuming table names are case-insensitive on Linux -- they are case-sensitive by default
- Not checking which database is active before running queries
- Using the wrong `lower_case_table_names` setting across environments
- Dropping tables in migration scripts without `IF EXISTS` causing partial failures
- Forgetting that MySQL stores table names as files on Linux, so the filesystem case sensitivity matters

## Related Pages

- [MySQL Column Does Not Exist](/tools/mysql/mysql-column-doesnt-exist)
- [MySQL Access Denied](/tools/mysql/mysql-access-denied)
- [MySQL Duplicate Entry](/tools/mysql/mysql-duplicate-entry)
- [PostgreSQL Database Does Not Exist](/tools/postgresql/pg-database-does-not-exist)
