---
title: "[Solution] SQL Unknown Function Fix"
description: "Fix 'Unknown function X' when calling a function that does not exist in the database."
languages: ["sql"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["unknown-function", "function", "built-in", "custom-function"]
weight: 5
---

This error occurs when a SQL query calls a function that the database does not recognize. The message reads: `Unknown function 'X'`.

## What This Error Means

The database does not have a built-in or user-defined function with the specified name. This can be due to a typo, using database-specific functions in a different RDBMS, or the function not being installed.

## Common Causes

- Function name is misspelled
- Using database-specific functions (MySQL vs PostgreSQL)
- Function requires an extension or plugin
- Case sensitivity in function names

## How to Fix

### Fix 1: Use correct function name

```sql
-- Wrong: PostgreSQL function in MySQL
SELECT STR_TO_DATE('2024-01-15', 'YYYY-MM-DD');

-- MySQL correct syntax
SELECT STR_TO_DATE('2024-01-15', '%Y-%m-%d');
```

### Fix 2: Check available functions

```sql
-- MySQL
SELECT * FROM information_schema.routines
WHERE routine_type = 'FUNCTION';

-- PostgreSQL
SELECT proname FROM pg_proc WHERE prokind = 'f';
```

### Fix 3: Install required extensions (PostgreSQL)

```sql
-- Enable uuid extension
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
SELECT uuid_generate_v4();
```

## Examples

```sql
SELECT GREATEST(1, 2, 3);  -- Works in MySQL/PostgreSQL
SELECT LEAST(1, 2, 3);     -- Works in MySQL/PostgreSQL
SELECT TOP(3) * FROM users; -- ERROR in MySQL — TOP is SQL Server syntax
```

## Related Errors

- [Syntax Error](syntax-error.md) — malformed SQL
- [Variable Error](variable-error.md) — unknown system variable
