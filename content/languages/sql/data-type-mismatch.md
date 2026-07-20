---
title: "[Solution] Data Type Mismatch in WHERE Clause"
description: "Fix 'Data type mismatch' when comparing columns of incompatible types in a WHERE clause."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "sql"
tags: ["sql", "data-type, type-mismatch"]
severity: "error"
---

# Data Type Mismatch in WHERE Clause

## Error Message

```
ORA-01722: invalid number / ERROR 1365: Division by 0 / Conversion failed when converting the nvarchar value to data type int.
```

## Common Causes

- Comparing a string column to a numeric value without explicit conversion
- Implicit type conversion fails due to incompatible data types
- WHERE clause uses a function that changes the column's data type unexpectedly
- JOIN condition compares columns of different types

## Solutions

### Solution 1: Cast values explicitly to match column types

Use CAST or CONVERT to ensure both sides of a comparison have the same data type.

```sql
-- Wrong: comparing string column to number
SELECT * FROM users WHERE phone = 1234567890;

-- Correct: cast the number to string
SELECT * FROM users WHERE phone = '1234567890';

-- Correct: cast the column (not recommended — may prevent index usage)
SELECT * FROM users WHERE CAST(phone AS UNSIGNED) = 1234567890;

-- PostgreSQL: explicit cast
SELECT * FROM users WHERE phone::VARCHAR = '1234567890';

-- SQL Server: use CONVERT or TRY_CONVERT
SELECT * FROM users WHERE TRY_CONVERT(INT, phone) = 1234567890;
```

### Solution 2: Use the correct data types in table design

Design columns with appropriate data types to avoid implicit conversions.

```sql
-- Wrong: storing numbers as strings
CREATE TABLE users (
    id VARCHAR(10),    -- should be INT
    phone VARCHAR(20), -- acceptable for phone numbers with formatting
    age VARCHAR(3)     -- should be INT
);

-- Correct: use appropriate data types
CREATE TABLE users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    phone VARCHAR(20),
    age INT,
    CHECK (age >= 0 AND age <= 150)
);

-- Fix an existing column's data type
ALTER TABLE users MODIFY id INT NOT NULL;
```

### Solution 3: Use TRY_CAST for safe conversions

TRY_CAST returns NULL instead of an error when conversion fails.

```sql
-- MySQL: use IFNULL with CAST
SELECT * FROM users
WHERE CAST(price AS DECIMAL(10,2)) IS NOT NULL;

-- PostgreSQL: use TRY_CAST (available in PG 14+)
SELECT * FROM products
WHERE TRY_CAST(price AS DECIMAL(10,2)) IS NOT NULL;

-- SQL Server: TRY_CONVERT returns NULL on failure
SELECT name, TRY_CONVERT(INT, age_text) AS age
FROM staging_users
WHERE TRY_CONVERT(INT, age_text) IS NOT NULL;

-- MySQL: validate data before conversion
SELECT * FROM products
WHERE price REGEXP '^[0-9]+\\.?[0-9]*$';
```

## Prevention Tips

- Match data types in JOIN and WHERE conditions to ensure proper index usage and avoid implicit conversions
- Use TRY_CAST or TRY_CONVERT instead of CAST to handle cases where conversion might fail
- Run EXPLAIN to check if type mismatches are causing the database to skip indexes

## Related Errors

- [String Truncation]({{< relref "/languages/sql/string-truncation.md" >}})
- [Numeric Overflow]({{< relref "/languages/sql/numeric-overflow.md" >}})
- [Type Mismatch]({{< relref "/languages/sql/type-mismatch.md" >}})
