---
title: "SQL HAVING Clause Without GROUP BY Error"
description: "Fix SQL HAVING clause errors when using HAVING without a corresponding GROUP BY clause."
languages: ["sql"]
error-types: ["syntax-error"]
severities: ["error"]
weight: 5
---

## Common Causes

- HAVING clause used without GROUP BY
- HAVING references a non-aggregated column not in GROUP BY
- Using WHERE instead of HAVING for aggregate conditions
- HAVING clause has syntax errors in aggregate expressions
- Mixing aggregate and non-aggregate conditions incorrectly

## How to Fix

```sql
-- WRONG: HAVING without GROUP BY
SELECT name, COUNT(*) FROM employees HAVING COUNT(*) > 5;
-- ERROR in strict SQL mode

-- CORRECT: Add GROUP BY
SELECT name, COUNT(*) FROM employees GROUP BY name HAVING COUNT(*) > 5;
```

```sql
-- WRONG: Aggregate in WHERE
SELECT department, AVG(salary) FROM employees WHERE AVG(salary) > 50000 GROUP BY department;
-- ERROR: aggregate in WHERE clause

-- CORRECT: Use HAVING
SELECT department, AVG(salary) FROM employees GROUP BY department HAVING AVG(salary) > 50000;
```

## Examples

```sql
-- Example 1: Basic HAVING
SELECT customer_id, COUNT(*) AS order_count
FROM orders
GROUP BY customer_id
HAVING COUNT(*) > 3;

-- Example 2: Multiple conditions in HAVING
SELECT department, AVG(salary) AS avg_sal
FROM employees
GROUP BY department
HAVING AVG(salary) > 50000 AND COUNT(*) > 10;

-- Example 3: HAVING with subquery
SELECT dept_name FROM (
    SELECT d.name AS dept_name, AVG(e.salary) AS avg_sal
    FROM employees e
    JOIN departments d ON e.dept_id = d.id
    GROUP BY d.name
) sub
WHERE avg_sal > 60000;
```

## Related Errors

- [Group by error](sql-group-by-error) -- GROUP BY clause issues
- [Having clause error](sql-no-having) -- HAVING syntax problems
