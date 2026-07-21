---
title: "[Solution] MySQL Divide By Zero Error"
description: "Fix MySQL divide by zero error when a division operation encounters a zero divisor value"
tools: ["mysql"]
error-types: ["tool-error"]
severities: ["error"]
---

# MySQL Divide By Zero Error

A division operation attempts to divide by zero. MySQL returns an error in strict mode or NULL in non-strict mode, depending on the SQL mode setting.

## Common Causes

- Column values contain zeros from incomplete data
- Aggregate functions (SUM, COUNT) return zero in denominators
- Calculations use user-provided data without validation
- JOIN produces unmatched rows where the divisor column is NULL or zero
- Division by a computed expression that evaluates to zero

## How to Fix

### Use NULLIF to Prevent Division by Zero

```sql
-- NULLIF returns NULL when values are equal, preventing division by zero
SELECT
  order_id,
  revenue / NULLIF(units, 0) AS price_per_unit
FROM orders;
```

### Use CASE Statement

```sql
SELECT
  order_id,
  CASE
    WHEN units = 0 THEN NULL
    ELSE revenue / units
  END AS price_per_unit
FROM orders;
```

### Set SQL Mode Appropriately

```sql
-- Check current mode
SELECT @@sql_mode;

-- Remove ERROR_FOR_DIVISION_BY_ZERO for legacy behavior
SET SESSION sql_mode = 'STRICT_TRANS_TABLES,NO_ZERO_DATE,NO_ZERO_IN_DATE';
```

### Validate Before Division

```sql
-- Add a WHERE clause to skip zero divisors
SELECT
  order_id,
  revenue / units AS price_per_unit
FROM orders
WHERE units > 0;
```

### Use IFNULL for Display

```sql
-- Return 0 instead of NULL when division by zero occurs
SELECT
  order_id,
  IFNULL(revenue / NULLIF(units, 0), 0) AS price_per_unit
FROM orders;
```

## Examples

```
ERROR 1365 (22012): Division by 0

-- In non-strict mode, returns NULL instead of error
SELECT 10 / 0;  -- NULL (non-strict) or ERROR (strict)
```

## Related Errors

- [MySQL Incorrect Datetime]({{< relref "/tools/mysql/mysql-incorrect-datetime" >}}) -- type errors
- [MySQL Data Truncated]({{< relref "/tools/mysql/mysql-data-truncated" >}}) -- truncation issues
- [MySQL Out of Range]({{< relref "/tools/mysql/mysql-out-of-range" >}}) -- value range issues
