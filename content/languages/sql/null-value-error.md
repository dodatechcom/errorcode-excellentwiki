---
title: "[Solution] Cannot Convert Null Value"
description: "Fix 'Cannot convert null value' when a NULL value is encountered in an expression expecting a non-null value."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "sql"
tags: ["sql", "data-type, null"]
severity: "error"
---

# Cannot Convert Null Value

## Error Message

```
Conversion failed when converting from a varchar to a data type / Cannot convert null value — A NULL value was encountered where a non-null value is required.
```

## Common Causes

- A NULL value is used in arithmetic operations, which always produces NULL
- NULL is passed to a function that requires non-null arguments
- A NOT NULL column is being set to NULL through a JOIN or subquery
- Aggregate functions like COUNT(col) ignore NULLs, producing unexpected results

## Solutions

### Solution 1: Use COALESCE to provide default values for NULL

Replace NULL with a sensible default before using it in calculations.

```sql
-- Wrong: NULL in arithmetic produces NULL
SELECT salary + bonus FROM employees;
-- If bonus is NULL, result is NULL

-- Correct: use COALESCE
SELECT salary + COALESCE(bonus, 0) FROM employees;

-- MySQL: use IFNULL
SELECT salary + IFNULL(bonus, 0) FROM employees;

-- SQL Server: use ISNULL
SELECT salary + ISNULL(bonus, 0) FROM employees;

-- PostgreSQL: use COALESCE
SELECT salary + COALESCE(bonus, 0) FROM employees;
```

### Solution 2: Use NULL-safe comparison operators

Use IS NULL and IS NOT NULL instead of = and <> for NULL comparisons.

```sql
-- Wrong: NULL = NULL returns NULL (not TRUE)
SELECT * FROM users WHERE email = NULL;

-- Correct: use IS NULL
SELECT * FROM users WHERE email IS NULL;

-- Correct: use IS NOT NULL
SELECT * FROM users WHERE email IS NOT NULL;

-- MySQL: use <=> (NULL-safe equality)
SELECT * FROM users WHERE email <=> NULL;

-- PostgreSQL: use IS DISTINCT FROM
SELECT * FROM users WHERE email IS DISTINCT FROM NULL;
```

### Solution 3: Handle NULLs in aggregate functions

Use aggregate functions that handle NULL values correctly.

```sql
-- COUNT(column) ignores NULLs
SELECT COUNT(email) FROM users;
-- Only counts non-NULL emails

-- COUNT(*) counts all rows including NULLs
SELECT COUNT(*) FROM users;

-- SUM and AVG ignore NULLs
SELECT AVG(bonus) FROM employees;
-- Only averages non-NULL bonuses

-- Use COALESCE with aggregates
SELECT AVG(COALESCE(bonus, 0)) FROM employees;
-- Treats NULL bonuses as 0

-- PostgreSQL: use FILTER clause
SELECT COUNT(*) FILTER (WHERE email IS NOT NULL) FROM users;
```

## Prevention Tips

- Always use IS NULL or IS NOT NULL for NULL comparisons — equality operators with NULL never evaluate to TRUE
- Use COALESCE, IFNULL, or ISNULL to replace NULL with default values before using them in calculations
- Define NOT NULL constraints and DEFAULT values on columns where NULL is not acceptable

## Related Errors

- [Not Null Constraint]({{< relref "/languages/sql/not-null-constraint.md" >}})
- [Data Type Mismatch]({{< relref "/languages/sql/data-type-mismatch.md" >}})
- [Null Constraint]({{< relref "/languages/sql/null-constraint.md" >}})
