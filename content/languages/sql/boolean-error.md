---
title: "[Solution] Invalid Boolean Value"
description: "Fix 'Invalid boolean value' when a non-boolean value is used in a boolean context."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "sql"
tags: ["sql", "data-type, boolean"]
severity: "error"
---

# Invalid Boolean Value

## Error Message

```
ERROR 1064: You have an error in your SQL syntax / Invalid input syntax for type boolean — A value of the wrong type was used in a boolean expression.
```

## Common Causes

- Using string values like 'true'/'false' instead of proper boolean constants in some databases
- Comparing a non-boolean column with boolean operators (AND, OR, NOT)
- Different databases represent booleans differently (TRUE/FALSE vs 1/0 vs 'Y'/'N')
- Application code sends incorrect boolean type to parameterized queries

## Solutions

### Solution 1: Use the correct boolean syntax for your database

Different databases have different ways to represent boolean values.

```sql
-- MySQL: no native BOOLEAN, uses TINYINT(1)
-- TRUE = 1, FALSE = 0
SELECT * FROM users WHERE is_active = 1;
SELECT * FROM users WHERE is_active = 0;

-- PostgreSQL: native BOOLEAN type
-- TRUE, FALSE, or NULL
SELECT * FROM users WHERE is_active = TRUE;
SELECT * FROM users WHERE is_active = FALSE;

-- SQL Server: no native BOOLEAN, uses BIT
-- 1 = true, 0 = false
SELECT * FROM users WHERE is_active = 1;
SELECT * FROM users WHERE is_active = 0;
```

### Solution 2: Use CASE expressions to convert to boolean

Convert string or numeric values to boolean using CASE.

```sql
-- MySQL: convert 'Y'/'N' to boolean
SELECT name,
    CASE WHEN status = 'Y' THEN 1 ELSE 0 END AS is_active
FROM users;

-- PostgreSQL: convert text to boolean
SELECT name,
    CASE WHEN status = 'Y' THEN TRUE ELSE FALSE END AS is_active
FROM users;

-- SQL Server: convert VARCHAR to BIT
SELECT name,
    CASE WHEN status = 'Y' THEN 1 ELSE 0 END AS is_active
FROM users;

-- MySQL: use boolean literals in newer versions
SELECT * FROM users WHERE is_active IS TRUE;
SELECT * FROM users WHERE is_active IS FALSE;
```

### Solution 3: Use IS NULL for NULL boolean checks

Handle the three-valued logic of SQL booleans correctly.

```sql
-- Wrong: NULL comparison with =
SELECT * FROM users WHERE is_active = NULL;

-- Correct: use IS NULL / IS NOT NULL
SELECT * FROM users WHERE is_active IS NULL;
SELECT * FROM users WHERE is_active IS NOT NULL;

-- PostgreSQL: use IS TRUE / IS FALSE / IS UNKNOWN
SELECT * FROM users WHERE is_active IS TRUE;
SELECT * FROM users WHERE is_active IS FALSE;
SELECT * FROM users WHERE is_active IS UNKNOWN;

-- Include NULLs in results (three-valued logic)
SELECT * FROM users WHERE is_active = TRUE OR is_active IS NULL;

-- MySQL: NULL-safe comparison
SELECT * FROM users WHERE is_active <=> TRUE;
```

## Prevention Tips

- Understand that your database represents booleans differently — MySQL uses TINYINT(1), SQL Server uses BIT, PostgreSQL uses native BOOLEAN
- Always use IS NULL or IS NOT NULL for checking NULL boolean values, never = NULL
- Define BOOLEAN or BIT columns as NOT NULL with a DEFAULT value to avoid three-valued logic complications

## Related Errors

- [Null Value Error]({{< relref "/languages/sql/null-value-error.md" >}})
- [Data Type Mismatch]({{< relref "/languages/sql/data-type-mismatch.md" >}})
- [Not Null Constraint]({{< relref "/languages/sql/not-null-constraint.md" >}})
