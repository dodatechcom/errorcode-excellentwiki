---
title: "[Solution] SQL Not A GROUP BY Expression Error Fix"
description: "Fix 'not a GROUP BY expression' in SQL. Add non-aggregated columns to GROUP BY clause and use aggregate functions correctly."
languages: ["sql"]
error-types: ["syntax-error"]
severities: ["error"]
weight: 5
---

# SQL Not A GROUP BY Expression Error Fix

The `not a GROUP BY expression` error occurs when a SELECT column is not included in the GROUP BY clause and is not wrapped in an aggregate function.

## What This Error Means

When you use GROUP BY, every column in the SELECT list must either appear in the GROUP BY clause or be wrapped in an aggregate function (SUM, COUNT, AVG, etc.). Non-aggregated, non-grouped columns produce indeterminate results.

A typical error:

```
ERROR: column "name" must appear in the GROUP BY clause or be used in an aggregate function
```

## Why It Happens

Common causes include:

- **SELECT columns not in GROUP BY** — Selecting columns that are neither grouped nor aggregated.
- **Using non-aggregated in HAVING** — HAVING references columns not in GROUP BY.
- **Mixing aggregate and non-aggregate** — Without proper GROUP BY placement.
- **Using function results in SELECT** — Functions that are not aggregates.

## How to Fix It

### Fix 1: Add all non-aggregated columns to GROUP BY

```sql
-- WRONG: name not in GROUP BY
SELECT department, name, COUNT(*)
FROM employees
GROUP BY department;

-- RIGHT: Include all non-aggregated columns
SELECT department, name, COUNT(*)
FROM employees
GROUP BY department, name;
```

### Fix 2: Use aggregate functions for non-grouped columns

```sql
-- RIGHT: Use aggregate
SELECT department, COUNT(*), MAX(salary)
FROM employees
GROUP BY department;
```

### Fix 3: Use window functions for detailed aggregation

```sql
-- RIGHT: Window function keeps detail rows
SELECT 
    department,
    name,
    salary,
    COUNT(*) OVER (PARTITION BY department) AS dept_count,
    RANK() OVER (PARTITION BY department ORDER BY salary DESC) AS rank
FROM employees;
```

### Fix 4: Use subquery for complex aggregations

```sql
-- RIGHT: Subquery with GROUP BY in inner query
SELECT d.department_name, e.name, e.salary
FROM employees e
JOIN (
    SELECT department, MAX(salary) AS max_salary
    FROM employees
    GROUP BY department
) d ON e.department = d.department AND e.salary = d.max_salary;
```

### Fix 5: Fix HAVING clause

```sql
-- WRONG: name not in GROUP BY
SELECT department, COUNT(*)
FROM employees
GROUP BY department
HAVING name = 'Engineering';

-- RIGHT: Use aggregate in HAVING
SELECT department, COUNT(*)
FROM employees
GROUP BY department
HAVING COUNT(*) > 5;
```

## Common Mistakes

- **Assuming all SQL dialects allow non-grouped columns** — PostgreSQL is strict; MySQL has `ONLY_FULL_GROUP_BY`.
- **Forgetting that ORDER BY columns must also be in GROUP BY or aggregated** — Some databases enforce this.
- **Not using DISTINCT when needed** — `GROUP BY col1, col2` is like `SELECT DISTINCT col1, col2`.

## Related Pages

- [SQL Column Ambiguous](sql-column-ambiguous) — Ambiguous column references
- [SQL Order By Error](sql-order-by-error) — ORDER BY position errors
- [SQL Window Function Error](sql-window-function-error) — Window function issues
