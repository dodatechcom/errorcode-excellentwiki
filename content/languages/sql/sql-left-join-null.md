---
title: "SQL LEFT JOIN Returning Unexpected NULL Values"
description: "Fix SQL LEFT JOIN errors when unexpected NULL values appear in results due to join condition mismatches."
languages: ["sql"]
error-types: ["logic-error"]
severities: ["error"]
weight: 5
---

## Common Causes

- JOIN condition does not match the actual relationship between tables
- Right table has no matching rows for the join condition
- Data type mismatch in join columns causes silent non-matches
- Join condition uses wrong column (e.g., name instead of id)
- Trailing spaces in VARCHAR comparisons cause non-matches

## How to Fix

```sql
-- WRONG: Joining on wrong column
SELECT o.id, c.name
FROM orders o
LEFT JOIN customers c ON o.customer_name = c.name;
-- NULL if names differ slightly

-- CORRECT: Join on ID columns
SELECT o.id, c.name
FROM orders o
LEFT JOIN customers c ON o.customer_id = c.id;
```

```sql
-- WRONG: Data type mismatch
SELECT * FROM t1
LEFT JOIN t2 ON t1.code = t2.code;
-- t1.code is INT, t2.code is VARCHAR

-- CORRECT: Cast to match types
SELECT * FROM t1
LEFT JOIN t2 ON CAST(t1.code AS VARCHAR) = t2.code;
```

## Examples

```sql
-- Example 1: Basic LEFT JOIN with NULL
SELECT e.name, d.department_name
FROM employees e
LEFT JOIN departments d ON e.dept_id = d.id;
-- NULL in department_name for employees with no department

-- Example 2: Filter NULLs with COALESCE
SELECT e.name, COALESCE(d.department_name, 'Unassigned') AS dept
FROM employees e
LEFT JOIN departments d ON e.dept_id = d.id;

-- Example 3: Check for non-matching rows
SELECT e.name FROM employees e
LEFT JOIN departments d ON e.dept_id = d.id
WHERE d.id IS NULL;
-- Shows employees without a valid department
```

## Related Errors

- [Join error](join-error) -- JOIN clause issues
- [Null value error](null-value-error) -- unexpected NULL results
