---
title: "SQL Window Function ORDER BY Partition Error"
description: "Fix SQL window function errors when PARTITION BY and ORDER BY clauses are used incorrectly together."
languages: ["sql"]
error-types: ["syntax-error"]
severities: ["error"]
weight: 5
---

## Common Causes

- ORDER BY in window function does not match expected sort direction
- Missing PARTITION BY causes entire result to be one window
- ORDER BY column not in SELECT list (some databases require it)
- Aggregate window function used with ORDER BY incorrectly
- FRAME clause conflicts with ORDER BY specification

## How to Fix

```sql
-- WRONG: Missing PARTITION BY
SELECT name, department, salary,
    RANK() OVER (ORDER BY salary DESC) AS rank
FROM employees;
-- Ranks across ALL departments, not within each

-- CORRECT: Add PARTITION BY
SELECT name, department, salary,
    RANK() OVER (PARTITION BY department ORDER BY salary DESC) AS dept_rank
FROM employees;
```

```sql
-- WRONG: Aggregate window without ORDER BY
SELECT name, salary,
    SUM(salary) OVER (PARTITION BY department ORDER BY salary) AS running_total
FROM employees;
-- Frame may be unexpected

-- CORRECT: Specify frame explicitly
SELECT name, salary,
    SUM(salary) OVER (PARTITION BY department ORDER BY salary
        ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS running_total
FROM employees;
```

## Examples

```sql
-- Example 1: ROW_NUMBER with PARTITION
SELECT name, department,
    ROW_NUMBER() OVER (PARTITION BY department ORDER BY hire_date) AS hire_order
FROM employees;

-- Example 2: LAG/LEAD with ORDER BY
SELECT name, salary,
    LAG(salary, 1) OVER (ORDER BY hire_date) AS prev_salary,
    LEAD(salary, 1) OVER (ORDER BY hire_date) AS next_salary
FROM employees;

-- Example 3: NTILE bucketing
SELECT name, salary,
    NTILE(4) OVER (ORDER BY salary DESC) AS salary_quartile
FROM employees;
```

## Related Errors

- [Window function error](sql-window-function) -- window function issues
- [SQL window function error](sql-window-function-error) -- window clause problems
