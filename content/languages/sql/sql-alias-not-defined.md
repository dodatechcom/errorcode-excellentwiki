---
title: "SQL Table Alias Not Defined Error"
description: "Fix SQL table alias errors when referencing an alias in WHERE or SELECT that was not defined in FROM clause."
languages: ["sql"]
error-types: ["syntax-error"]
severities: ["error"]
weight: 5
---

## Common Causes

- Using alias in SELECT before it is defined in FROM
- Typo in alias name between FROM and WHERE clauses
- Alias defined in subquery but referenced in outer query
- Using table name instead of alias inconsistently
- Circular alias reference in self-join

## How to Fix

```sql
-- WRONG: Alias not defined
SELECT e.name, d.name AS department
FROM employees e
WHERE dept.name = 'Sales';  -- ERROR: 'dept' not defined

-- CORRECT: Use consistent alias
SELECT e.name, d.name AS department
FROM employees e
JOIN departments d ON e.dept_id = d.id
WHERE d.name = 'Sales';
```

```sql
-- WRONG: Alias used before FROM
SELECT t.col1 FROM t AS sub
WHERE sub.col2 = (SELECT t.col1 FROM t);  -- 't' ambiguous

-- CORRECT: Define alias in FROM first
SELECT sub.col1 FROM t sub
WHERE sub.col2 = (SELECT main.col1 FROM t main);
```

## Examples

```sql
-- Example 1: Simple alias usage
SELECT u.name, u.email
FROM users u
WHERE u.active = 1;

-- Example 2: Self-join with aliases
SELECT e.name AS employee, m.name AS manager
FROM employees e
LEFT JOIN employees m ON e.manager_id = m.id;

-- Example 3: Subquery alias
SELECT sub.dept_name, sub.emp_count
FROM (
    SELECT d.name AS dept_name, COUNT(*) AS emp_count
    FROM employees e
    JOIN departments d ON e.dept_id = d.id
    GROUP BY d.name
) sub
WHERE sub.emp_count > 10;
```

## Related Errors

- [Table not found error](table-not-found) -- table reference issues
- [Column not found error](column-not-found) -- column reference failures
