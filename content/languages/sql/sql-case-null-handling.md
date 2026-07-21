---
title: "SQL CASE Expression NULL Handling Error"
description: "Fix SQL CASE expression errors when NULL values are not handled properly in WHEN conditions."
languages: ["sql"]
error-types: ["logic-error"]
severities: ["error"]
weight: 5
---

## Common Causes

- WHEN condition uses `column = NULL` instead of `IS NULL`
- CASE does not have an ELSE clause, returning NULL implicitly
- NULL in arithmetic within CASE produces NULL
- CASE with IN clause does not match NULL values
- ORDER BY on CASE expression sorts NULLs unexpectedly

## How to Fix

```sql
-- WRONG: NULL comparison with =
SELECT name,
    CASE status
        WHEN NULL THEN 'Unknown'  -- NEVER matches!
        WHEN 'active' THEN 'Active'
    END AS status_label
FROM users;

-- CORRECT: Use IS NULL or handle in WHEN
SELECT name,
    CASE
        WHEN status IS NULL THEN 'Unknown'
        WHEN status = 'active' THEN 'Active'
        ELSE 'Other'
    END AS status_label
FROM users;
```

```sql
-- WRONG: Missing ELSE returns NULL
SELECT amount,
    CASE
        WHEN amount > 1000 THEN 'Large'
        WHEN amount > 100 THEN 'Medium'
    END AS size_category
FROM orders;
-- Rows with amount <= 100 return NULL

-- CORRECT: Add ELSE
SELECT amount,
    CASE
        WHEN amount > 1000 THEN 'Large'
        WHEN amount > 100 THEN 'Medium'
        ELSE 'Small'
    END AS size_category
FROM orders;
```

## Examples

```sql
-- Example 1: CASE with NULL handling
SELECT employee_name,
    CASE
        WHEN commission IS NULL THEN 'No commission'
        WHEN commission = 0 THEN 'Zero commission'
        ELSE CAST(commission AS VARCHAR)
    END AS commission_status
FROM employees;

-- Example 2: CASE in ORDER BY
SELECT * FROM products
ORDER BY
    CASE WHEN stock_quantity = 0 THEN 0 ELSE 1 END,
    name;

-- Example 3: CASE with aggregation
SELECT department,
    SUM(CASE WHEN gender = 'M' THEN 1 ELSE 0 END) AS male_count,
    SUM(CASE WHEN gender = 'F' THEN 1 ELSE 0 END) AS female_count
FROM employees GROUP BY department;
```

## Related Errors

- [Null constraint error](null-constraint) -- NULL handling in constraints
- [Null value error](null-value-error) -- unexpected NULL values
