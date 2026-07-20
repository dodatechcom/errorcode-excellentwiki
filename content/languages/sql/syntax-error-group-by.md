---
title: "[Solution] SQL Syntax Error Near GROUP BY"
description: "Fix 'SQL syntax error near GROUP BY' when a GROUP BY clause is malformed."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "sql"
tags: ["sql", "syntax, aggregation"]
severity: "error"
---

# SQL Syntax Error Near GROUP BY

## Error Message

```
You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'GROUP BY ...'
```

## Common Causes

- Column in SELECT is not in the GROUP BY clause and is not wrapped in an aggregate function
- GROUP BY position number referencing a column ordinal that does not exist
- Using column aliases in GROUP BY before they are resolved
- GROUP BY with ROLLUP or CUBE syntax used incorrectly

## Solutions

### Solution 1: Include all non-aggregated columns in GROUP BY

Every column in SELECT that is not inside an aggregate function must appear in the GROUP BY clause.

```sql
-- Wrong: 'name' is not aggregated or grouped
SELECT name, department, COUNT(*)
FROM employees
GROUP BY department;

-- Correct: include name in GROUP BY
SELECT name, department, COUNT(*)
FROM employees
GROUP BY name, department;

-- Correct: use an aggregate for name
SELECT MAX(name), department, COUNT(*)
FROM employees
GROUP BY department;
```

### Solution 2: Use GROUP BY with proper aggregate functions

Combine GROUP BY with aggregate functions to summarize data correctly.

```sql
-- Correct: aggregation per department
SELECT
    department,
    COUNT(*) AS employee_count,
    AVG(salary) AS avg_salary,
    MAX(salary) AS max_salary
FROM employees
GROUP BY department
ORDER BY avg_salary DESC;

-- Correct: GROUP BY with multiple columns
SELECT
    department,
    location,
    COUNT(*) AS cnt
FROM employees
GROUP BY department, location
HAVING COUNT(*) > 3;
```

### Solution 3: Use GROUP BY with ROLLUP for subtotals

ROLLUP generates additional subtotal rows for hierarchical grouping.

```sql
-- MySQL / PostgreSQL: GROUP BY with ROLLUP
SELECT
    department,
    location,
    COUNT(*) AS cnt,
    SUM(salary) AS total_salary
FROM employees
GROUP BY ROLLUP (department, location);

-- SQL Server equivalent
SELECT
    department,
    location,
    COUNT(*) AS cnt,
    SUM(salary) AS total_salary
FROM employees
GROUP BY ROLLUP (department, location);
```

## Prevention Tips

- Enable ONLY_FULL_GROUP_BY mode in MySQL to enforce standard SQL GROUP BY behavior
- Use window functions as an alternative to GROUP BY when you need aggregate values alongside individual rows
- Verify your GROUP BY columns by running a DISTINCT query on the same columns first

## Related Errors

- [Syntax Error Having]({{< relref "/languages/sql/syntax-error-having.md" >}})
- [Syntax Error Select]({{< relref "/languages/sql/syntax-error-select.md" >}})
- [Sql Group By Error]({{< relref "/languages/sql/sql-group-by-error.md" >}})
