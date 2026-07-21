---
title: "SQL Unknown Column in Field List Error"
description: "Fix SQL unknown column errors when SELECT references a column name that does not exist in the specified table."
languages: ["sql"]
error-types: ["syntax-error"]
severities: ["error"]
weight: 5
---

## Common Causes

- Column name typo in SELECT statement
- Column belongs to a different table not included in JOIN
- Column was dropped or renamed but query was not updated
- Using column alias before it is defined in the same SELECT
- Case sensitivity mismatch on case-sensitive databases

## How to Fix

```sql
-- WRONG: Typo in column name
SELECT namme, age FROM users;
-- ERROR: Unknown column 'namme' in field list

-- CORRECT: Verify column name
SELECT name, age FROM users;
```

```sql
-- WRONG: Column from wrong table in JOIN
SELECT employees.name, departments.salary
FROM employees
JOIN departments ON employees.dept_id = departments.id;
-- ERROR: departments.salary does not exist

-- CORRECT: Use correct table alias
SELECT e.name, e.salary
FROM employees e
JOIN departments d ON e.dept_id = d.id;
```

## Examples

```sql
-- Example 1: Simple column typo
-- Table: products(id, name, price, category_id)
SELECT product_name, prce FROM products;
-- Fix:
SELECT name, price FROM products;

-- Example 2: Ambiguous column in JOIN
SELECT id, name, department_name
FROM employees e
JOIN departments d ON e.dept_id = d.id;
-- 'id' is ambiguous -- fix:
SELECT e.id, e.name, d.department_name
FROM employees e
JOIN departments d ON e.dept_id = d.id;

-- Example 3: Column from subquery
SELECT first_name, last_name, total_sales
FROM employees
WHERE total_sales > 100000;
-- total_sales is not in employees table
-- Fix: use subquery or JOIN
SELECT e.first_name, e.last_name, s.total_sales
FROM employees e
JOIN (SELECT emp_id, SUM(amount) AS total_sales
      FROM sales GROUP BY emp_id) s ON e.id = s.emp_id
WHERE s.total_sales > 100000;
```

## Related Errors

- [Column not found error](column-not-found) -- column reference failures
- [Table not found error](table-not-found) -- missing table references
