---
title: "SQL DISTINCT on Multiple Columns Error"
description: "Fix SQL DISTINCT errors when using DISTINCT with multiple columns does not produce expected unique row results."
languages: ["sql"]
error-types: ["logic-error"]
severities: ["error"]
weight: 5
---

## Common Causes

- DISTINCT applies to all columns, not just the ones in SELECT
- Using DISTINCT to fix a JOIN duplication problem instead of fixing the JOIN
- DISTINCT with ORDER BY on non-selected column
- COUNT(DISTINCT col) returns different count than expected
- DISTINCT does not remove NULL duplicates consistently across databases

## How to Fix

```sql
-- WRONG: DISTINCT does not help with JOIN duplication
SELECT DISTINCT e.name, d.name
FROM employees e
JOIN projects p ON e.id = p.emp_id
JOIN departments d ON e.dept_id = d.id;
-- Still has duplicates from multiple projects

-- CORRECT: Fix the JOIN or use GROUP BY
SELECT e.name, d.name
FROM employees e
JOIN departments d ON e.dept_id = d.id
WHERE e.id IN (SELECT DISTINCT emp_id FROM projects);
```

```sql
-- WRONG: COUNT(DISTINCT) on wrong granularity
SELECT COUNT(DISTINCT customer_id), COUNT(DISTINCT order_id)
FROM orders;
-- Counts unique customers and unique orders separately

-- CORRECT: Understand what you are counting
SELECT COUNT(DISTINCT customer_id) AS unique_customers
FROM orders;
```

## Examples

```sql
-- Example 1: DISTINCT on multiple columns
SELECT DISTINCT city, state FROM addresses;
-- Returns unique city-state combinations

-- Example 2: DISTINCT with aggregation
SELECT customer_id, COUNT(*) AS order_count
FROM orders
GROUP BY customer_id;

-- Example 3: Removing duplicates from result
SELECT DISTINCT
    first_name,
    last_name,
    email
FROM customers
WHERE email IS NOT NULL;
```

## Related Errors

- [Group by error](sql-group-by-error) -- GROUP BY clause issues
- [Duplicate entry error](sql-duplicate-entry) -- duplicate data issues
