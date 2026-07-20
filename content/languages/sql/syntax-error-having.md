---
title: "[Solution] SQL Syntax Error Near HAVING"
description: "Fix 'SQL syntax error near HAVING' when a HAVING clause is malformed."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "sql"
tags: ["sql", "syntax, aggregation"]
severity: "error"
---

# SQL Syntax Error Near HAVING

## Error Message

```
You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'HAVING ...'
```

## Common Causes

- Using HAVING without a GROUP BY clause
- Referencing a column in HAVING that is neither in the GROUP BY nor inside an aggregate function
- Placing HAVING before GROUP BY in the statement
- Using HAVING to filter non-aggregated conditions instead of WHERE

## Solutions

### Solution 1: Use HAVING only with GROUP BY

HAVING is designed to filter groups after aggregation. Use WHERE for pre-aggregation filtering.

```sql
-- Wrong: HAVING without GROUP BY
SELECT name FROM users HAVING COUNT(*) > 1;

-- Correct: use GROUP BY with HAVING
SELECT name, COUNT(*) AS cnt
FROM users
GROUP BY name
HAVING COUNT(*) > 1;

-- Correct: use WHERE for non-aggregate filtering
SELECT name, age FROM users WHERE age > 18
GROUP BY name, age
HAVING COUNT(*) > 1;
```

### Solution 2: Reference only valid columns in HAVING

Columns in HAVING must appear in GROUP BY or be wrapped in aggregate functions.

```sql
-- Wrong: 'salary' is not in GROUP BY and not aggregated
SELECT department, COUNT(*)
FROM employees
GROUP BY department
HAVING salary > 50000;

-- Correct: aggregate the column
SELECT department, COUNT(*)
FROM employees
GROUP BY department
HAVING AVG(salary) > 50000;

-- Correct: filter pre-aggregation with WHERE
SELECT department, COUNT(*) AS high_earners
FROM employees
WHERE salary > 50000
GROUP BY department
HAVING COUNT(*) > 3;
```

### Solution 3: Combine WHERE and HAVING correctly

Use WHERE to filter rows before aggregation and HAVING to filter groups after aggregation.

```sql
-- Correct: WHERE filters rows, HAVING filters groups
SELECT
    department,
    COUNT(*) AS total_employees,
    AVG(salary) AS avg_salary
FROM employees
WHERE hire_date >= '2023-01-01'  -- pre-aggregation filter
GROUP BY department
HAVING AVG(salary) > 60000;     -- post-aggregation filter

-- Correct: HAVING with multiple conditions
SELECT category, COUNT(*) AS product_count, AVG(price) AS avg_price
FROM products
GROUP BY category
HAVING COUNT(*) > 10 AND AVG(price) < 50;
```

## Prevention Tips

- Think of WHERE as filtering individual rows before grouping and HAVING as filtering groups after aggregation
- Use HAVING only when you need to filter on aggregate results like COUNT, SUM, AVG, MIN, or MAX
- Place WHERE before GROUP BY and HAVING after GROUP BY to avoid syntax errors

## Related Errors

- [Syntax Error Group By]({{< relref "/languages/sql/syntax-error-group-by.md" >}})
- [Syntax Error Where]({{< relref "/languages/sql/syntax-error-where.md" >}})
- [Syntax Error Select]({{< relref "/languages/sql/syntax-error-select.md" >}})
