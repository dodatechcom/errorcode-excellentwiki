---
title: "[Solution] SQL Division by Zero Error Fix"
description: "Fix 'Division by zero' when a SQL expression divides by a zero value."
languages: ["sql"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["division-by-zero", "arithmetic-error", "math"]
weight: 5
---

# SQL Division by Zero Error Fix

This error occurs when a SQL expression attempts to divide by zero. The message reads: `ERROR 1365: Division by 0` or `Division by zero`.

## Description

Arithmetic division by zero is undefined. In SQL, dividing any number by zero — whether literal or from a column value — raises an error. This commonly happens in calculations involving ratios, percentages, or averages where the denominator can be zero.

## Common Causes

- **Column value is zero** — a denominator column contains 0.
- **COUNT or SUM returns zero** — aggregate used as a divisor evaluates to 0.
- **Hardcoded zero literal** — accidentally writing `/ 0` in an expression.
- **NULL denominator misinterpreted** — some databases convert NULL to 0 for division.

## How to Fix

### Fix 1: Use IFNULL / COALESCE to provide a default

```sql
-- Avoid division by zero by defaulting to 1 (or 0 result)
SELECT
    name,
    revenue / IFNULL(NULLIF(units, 0), 1) AS price_per_unit
FROM products;
```

### Fix 2: Use CASE to guard the division

```sql
SELECT
    name,
    CASE
        WHEN units > 0 THEN revenue / units
        ELSE 0
    END AS price_per_unit
FROM products;
```

### Fix 3: Filter out zero values

```sql
-- Only calculate where denominator is non-zero
SELECT name, revenue / units AS price_per_unit
FROM products
WHERE units > 0;
```

### Fix 4: Enable safe division mode (MySQL 8.0.14+)

```sql
-- MySQL returns NULL instead of error for division by zero
SET sql_mode = 'ERROR_FOR_DIVISION_BY_ZERO';
```

## Examples

```sql
SELECT 10 / 0;
-- ERROR 1365: Division by 0

SELECT revenue / units FROM products WHERE id = 5;
-- ERROR 1365: Division by 0 (if units is 0 for that row)

SELECT COUNT(*) / SUM(CASE WHEN active = 1 THEN 1 ELSE 0 END) AS avg_active
FROM users;
-- ERROR 1365: Division by 0 (if no active users exist)
```

## Related Errors

- [Type Mismatch](type-mismatch.md) — incorrect data type in an expression.
- [Aggregate Error](aggregate-error.md) — misuse of aggregate functions.
- [Null Constraint](null-constraint.md) — unexpected NULL in calculations.
