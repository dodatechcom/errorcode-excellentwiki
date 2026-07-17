---
title: "[Solution] SQL Not a GROUP BY Expression Error Fix"
description: "Fix SQL GROUP BY errors when a selected column isn't in the GROUP BY clause or an aggregate function."
languages: ["sql"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# SQL Not a GROUP BY Expression Error Fix

A SQL GROUP BY error occurs when a SELECT column is neither included in the GROUP BY clause nor wrapped in an aggregate function.

## What This Error Means

When using GROUP BY, every column in SELECT must either be in the GROUP BY clause or used within an aggregate function (COUNT, SUM, AVG, etc.). Non-grouped columns have ambiguous values for each group.

## Common Causes

- SELECT includes columns not in GROUP BY
- Missing aggregate function for non-grouped columns
- Using SELECT * with GROUP BY
- Wanting all columns but grouping by one

## How to Fix

### 1. Add non-grouped columns to GROUP BY

```sql
-- WRONG: "name" not in GROUP BY
SELECT department, name, COUNT(*)
FROM employees
GROUP BY department;

-- CORRECT: Include all non-aggregated columns
SELECT department, name, COUNT(*)
FROM employees
GROUP BY department, name;
```

### 2. Use aggregate functions

```sql
-- CORRECT: Wrap non-grouped columns in aggregates
SELECT department, MAX(salary), COUNT(*)
FROM employees
GROUP BY department;

SELECT department, GROUP_CONCAT(name), COUNT(*)
FROM employees
GROUP BY department;
```

### 3. Don't use SELECT * with GROUP BY

```sql
-- WRONG: SELECT * with GROUP BY
SELECT * FROM employees GROUP BY department;

-- CORRECT: Specify only grouped/aggregated columns
SELECT department, COUNT(*) as emp_count
FROM employees
GROUP BY department;
```

### 4. Use window functions for all-row context

```sql
-- CORRECT: Window function preserves all rows
SELECT department, name, salary,
       COUNT(*) OVER (PARTITION BY department) as dept_count
FROM employees;
```

## Related Errors

- [SQL Subquery Error](sql-subquery-error-v2) — subquery issues
- [SQL Window Function Error](sql-window-function-v2) — window function syntax
- [SQL Syntax Error](sql-syntax-error-v2) — syntax issues
