---
title: "SQL BETWEEN Boundary Inclusive Exclusive Error"
description: "Fix SQL BETWEEN errors when boundary values are inclusive by default causing unexpected range results."
languages: ["sql"]
error-types: ["logic-error"]
severities: ["error"]
weight: 5
---

## Common Causes

- BETWEEN is inclusive on both ends (unexpected extra values)
- Date ranges with BETWEEN include midnight of end date
- Floating point boundaries produce unexpected matches
- NOT BETWEEN does not exclude NULLs as expected
- Using BETWEEN with datetime when time component matters

## How to Fix

```sql
-- WRONG: BETWEEN includes both boundaries
SELECT * FROM orders WHERE amount BETWEEN 100 AND 200;
-- Includes exactly 100 and exactly 200

-- CORRECT: Use exclusive boundary if needed
SELECT * FROM orders WHERE amount >= 100 AND amount < 200;
```

```sql
-- WRONG: Date BETWEEN includes full end date
SELECT * FROM orders WHERE order_date BETWEEN '2024-01-01' AND '2024-01-31';
-- Includes all of Jan 31st (midnight to midnight)

-- CORRECT: For month ranges use < next month
SELECT * FROM orders
WHERE order_date >= '2024-01-01' AND order_date < '2024-02-01';
```

## Examples

```sql
-- Example 1: Numeric BETWEEN
SELECT * FROM products WHERE price BETWEEN 10.00 AND 50.00;
-- Returns prices from 10.00 to 50.00 inclusive

-- Example 2: Date range for today only
SELECT * FROM logs
WHERE log_date = CAST(GETDATE() AS DATE);

-- Example 3: NOT BETWEEN with NULL
SELECT * FROM employees
WHERE salary NOT BETWEEN 30000 AND 60000;
-- NULL salaries are NOT included in result
-- Use: WHERE salary < 30000 OR salary > 60000 OR salary IS NULL
```

## Related Errors

- [Date format error](date-format-error) -- date parsing issues
- [Data truncation error](data-truncation) -- data size problems
