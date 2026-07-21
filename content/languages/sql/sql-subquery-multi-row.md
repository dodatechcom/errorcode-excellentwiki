---
title: "SQL WHERE Clause Subquery Returns Multiple Rows"
description: "Fix SQL subquery errors when a subquery in WHERE clause returns more than one row causing comparison failure."
languages: ["sql"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## Common Causes

- Subquery returns multiple rows but is used with = comparison
- Missing GROUP BY in subquery that should aggregate
- Subquery should use IN instead of =
- Correlated subquery references wrong outer table column
- Subquery lacks DISTINCT when duplicates cause multiple rows

## How to Fix

```sql
-- WRONG: Subquery returns multiple rows with =
SELECT * FROM employees
WHERE department_id = (SELECT id FROM departments WHERE location = 'NYC');
-- ERROR: subquery returns more than one row

-- CORRECT: Use IN for multiple values
SELECT * FROM employees
WHERE department_id IN (SELECT id FROM departments WHERE location = 'NYC');
```

```sql
-- WRONG: Subquery should aggregate
SELECT * FROM orders
WHERE amount = (SELECT MAX(amount) FROM orders WHERE customer_id = orders.customer_id);
-- ERROR if multiple orders share the max

-- CORRECT: Add aggregation
SELECT * FROM orders o
WHERE amount = (SELECT MAX(amount) FROM orders WHERE customer_id = o.customer_id);
-- or use LIMIT 1
```

## Examples

```sql
-- Example 1: Fix with IN
SELECT name FROM products
WHERE category_id IN (SELECT id FROM categories WHERE active = 1);

-- Example 2: Fix with ALL/ANY
SELECT name, salary FROM employees
WHERE salary > ALL (SELECT salary FROM employees WHERE dept_id = 10);

-- Example 3: Fix with EXISTS
SELECT e.name FROM employees e
WHERE EXISTS (
    SELECT 1 FROM sales s WHERE s.emp_id = e.id AND s.amount > 10000
);
```

## Related Errors

- [Subquery error](subquery-error) -- general subquery issues
- [SQL subquery error](sql-subquery-error) -- subquery failures
