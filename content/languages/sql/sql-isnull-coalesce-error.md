---
title: "SQL ISNULL Coalesce Function Error"
description: "Fix SQL ISNULL and COALESCE function errors when replacement values have incompatible types with the original column."
languages: ["sql"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## Common Causes

- ISNULL replacement value has different data type causing truncation
- COALESCE arguments have mismatched types across databases
- ISNULL in SQL Server treats empty string as NULL for varchar
- Using ISNULL with numeric column and string replacement
- Multiple COALESCE arguments with different lengths

## How to Fix

```sql
-- WRONG: Type mismatch in ISNULL
SELECT ISNULL(salary, 'N/A') FROM employees;
-- salary is DECIMAL, replacement is VARCHAR

-- CORRECT: Match types
SELECT ISNULL(CAST(salary AS VARCHAR(20)), 'N/A') FROM employees;
-- or
SELECT COALESCE(CAST(salary AS VARCHAR), 'N/A') FROM employees;
```

```sql
-- WRONG: COALESCE with different lengths
SELECT COALESCE(name, 'Unknown User') FROM users;
-- If name is VARCHAR(50), result is VARCHAR(50) -- OK
-- But in some databases, shorter replacement extends result type

-- CORRECT: Explicitly cast
SELECT COALESCE(name, CAST('Unknown' AS VARCHAR(50))) FROM users;
```

## Examples

```sql
-- Example 1: Basic COALESCE
SELECT name, COALESCE(nickname, name, 'Anonymous') AS display_name
FROM users;

-- Example 2: ISNULL vs COALESCE
-- SQL Server
SELECT ISNULL(salary, 0) FROM employees;  -- returns salary type
SELECT COALESCE(salary, 0) FROM employees; -- may return wider type

-- Example 3: COALESCE with multiple sources
SELECT COALESCE(work_phone, mobile_phone, home_phone, 'No phone')
AS contact_number
FROM contacts;
```

## Related Errors

- [Null value error](null-value-error) -- NULL handling issues
- [Data type mismatch](data-type-mismatch) -- type incompatibility
