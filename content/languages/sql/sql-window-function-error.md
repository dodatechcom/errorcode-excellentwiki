---
title: "[Solution] SQL Window Function Not In SELECT List Error Fix"
description: "Fix 'window function not in SELECT list' in SQL. Correct window function placement and usage in queries."
languages: ["sql"]
error-types: ["syntax-error"]
severities: ["error"]
weight: 5
---

# SQL Window Function Not In SELECT List Error Fix

The `window function not in SELECT list` error occurs when a window function is used in a WHERE, GROUP BY, or HAVING clause instead of the SELECT or ORDER BY clause.

## What This Error Means

Window functions (ROW_NUMBER, RANK, SUM OVER, etc.) can only appear in the SELECT list or ORDER BY clause. They cannot be used in WHERE, GROUP BY, or HAVING because they are computed after those operations.

A typical error:

```
ERROR: window function ROW_NUMBER() is not allowed in WHERE clause
```

## Why It Happens

Common causes include:

- **Window function in WHERE** — Trying to filter by row number.
- **Window function in GROUP BY** — Cannot group by window function result.
- **Window function in HAVING** — HAVING only allows aggregates.
- **Missing OVER clause** — Window functions require OVER().
- **Subquery not wrapping window function** — Need subquery to filter window results.

## How to Fix It

### Fix 1: Wrap window function in subquery

```sql
-- WRONG: Window function in WHERE
SELECT id, name, ROW_NUMBER() OVER (ORDER BY salary DESC) AS rn
FROM employees
WHERE ROW_NUMBER() OVER (ORDER BY salary DESC) <= 10;

-- RIGHT: Use subquery
SELECT * FROM (
    SELECT id, name, 
           ROW_NUMBER() OVER (ORDER BY salary DESC) AS rn
    FROM employees
) sub
WHERE rn <= 10;
```

### Fix 2: Use window function in SELECT only

```sql
-- RIGHT: Window function in SELECT
SELECT 
    id,
    name,
    department,
    salary,
    RANK() OVER (PARTITION BY department ORDER BY salary DESC) AS dept_rank,
    SUM(salary) OVER (PARTITION BY department) AS dept_total
FROM employees;
```

### Fix 3: Filter window function results with subquery

```sql
-- RIGHT: Filter top N per group
SELECT * FROM (
    SELECT 
        id, name, department, salary,
        ROW_NUMBER() OVER (PARTITION BY department ORDER BY salary DESC) AS rn
    FROM employees
) sub
WHERE rn <= 3;
```

### Fix 4: Use window function in ORDER BY

```sql
-- RIGHT: ORDER BY can use window function
SELECT id, name, 
       DENSE_RANK() OVER (ORDER BY salary DESC) AS rank
FROM employees
ORDER BY rank;
```

### Fix 5: Common window functions

```sql
-- Row numbering
ROW_NUMBER() OVER (ORDER BY col)

-- Rank with ties
RANK() OVER (PARTITION BY dept ORDER BY salary DESC)

-- Running total
SUM(amount) OVER (ORDER BY date ROWS UNBOUNDED PRECEDING)

-- Lag/Lead
LAG(salary, 1) OVER (ORDER BY hire_date)
LEAD(salary, 1) OVER (ORDER BY hire_date)
```

## Common Mistakes

- **Using window function without OVER clause** — OVER() is mandatory.
- **Forgetting PARTITION BY for grouped window** — Without it, the whole result set is one partition.
- **Not aliasing window function** — Always give window functions a clear alias.

## Related Pages

- [SQL Group By Error](sql-group-by-error) — GROUP BY expression issues
- [SQL Order By Error](sql-order-by-error) — ORDER BY position errors
- [SQL Recursive CTE Error](sql-recursive-cte-error) — CTE recursion issues
