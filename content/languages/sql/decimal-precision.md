---
title: "[Solution] Decimal Precision Error"
description: "Fix 'Decimal precision error' when numeric values lose precision during calculations or storage."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "sql"
tags: ["sql", "data-type, decimal, precision"]
severity: "error"
---

# Decimal Precision Error

## Error Message

```
ERROR 1365: Division by 0 / Loss of precision in decimal calculation — The decimal value has more digits than the column's precision allows, or rounding produces unexpected results.
```

## Common Causes

- Column is defined with insufficient precision or scale for the data being stored
- Arithmetic operations produce more decimal places than the result column can hold
- Floating-point types (FLOAT/DOUBLE) are used instead of exact types (DECIMAL) for financial calculations
- Implicit type conversion from DECIMAL to FLOAT introduces rounding errors

## Solutions

### Solution 1: Increase the precision of DECIMAL columns

Define DECIMAL columns with enough precision and scale for your data.

```sql
-- Wrong: DECIMAL(5,2) only stores up to 999.99
ALTER TABLE orders MODIFY COLUMN total DECIMAL(5,2);

-- Correct: increase precision for large values
ALTER TABLE orders MODIFY COLUMN total DECIMAL(18,4);

-- DECIMAL precision guide:
-- DECIMAL(10,2):  up to 99,999,999.99
-- DECIMAL(18,4):  up to 999,999,999,999.9999
-- DECIMAL(20,8):  up to 99,999,999,999,999.99999999

CREATE TABLE financial_records (
    id INT PRIMARY KEY,
    amount DECIMAL(20,4) NOT NULL,
    rate DECIMAL(10,8) NOT NULL,
    total DECIMAL(24,8) GENERATED ALWAYS AS (amount * rate) STORED
);
```

### Solution 2: Use ROUND to control decimal places in calculations

Explicitly round the results of arithmetic operations to the expected precision.

```sql
-- Wrong: implicit precision loss
UPDATE products SET price = price * 1.15;
-- May produce values with many decimal places

-- Correct: explicitly round
UPDATE products SET price = ROUND(price * 1.15, 2);

-- Correct: use CAST with precision
SELECT ROUND(salary * 0.15, 2) AS bonus FROM employees;

-- PostgreSQL: use NUMERIC function
SELECT (amount * rate)::NUMERIC(20,4) FROM calculations;

-- SQL Server: use ROUND with style
SELECT ROUND(amount * rate, 4, 1) FROM calculations;
```

### Solution 3: Avoid FLOAT for financial calculations

Use DECIMAL or NUMERIC types for exact arithmetic in financial applications.

```sql
-- Wrong: FLOAT introduces rounding errors
CREATE TABLE prices (
    amount FLOAT  -- imprecise: 0.1 + 0.2 != 0.3
);

-- Correct: DECIMAL for exact precision
CREATE TABLE prices (
    amount DECIMAL(18,4)  -- exact: no rounding errors
);

-- Demonstrate FLOAT imprecision
SELECT 0.1 + 0.2 = 0.3;  -- Returns 0 in FLOAT comparison

-- Correct with DECIMAL
SELECT CAST(0.1 AS DECIMAL(10,4)) + CAST(0.2 AS DECIMAL(10,4))
    = CAST(0.3 AS DECIMAL(10,4));  -- Returns 1 (true)
```

## Prevention Tips

- Always use DECIMAL or NUMERIC for financial calculations where exact precision is critical
- Define DECIMAL columns with enough precision to accommodate future growth in value size
- Apply ROUND explicitly in calculations to control the number of decimal places in results

## Related Errors

- [Numeric Overflow]({{< relref "/languages/sql/numeric-overflow.md" >}})
- [Integer Overflow]({{< relref "/languages/sql/integer-overflow.md" >}})
- [Data Type Mismatch]({{< relref "/languages/sql/data-type-mismatch.md" >}})
