---
title: "SQL GROUPING SETS Cube Rollup Error"
description: "Fix SQL GROUPING SETS, CUBE, and ROLLUP errors when subtotal aggregation produces unexpected NULL grouping columns."
languages: ["sql"]
error-types: ["syntax-error"]
severities: ["error"]
weight: 5
---

## Common Causes

- Confusing NULL in grouping column with NULL data values
- ROLLUP produces subtotals in unexpected order
- CUBE generates more groupings than expected
- GROUPING() function not used to distinguish subtotal NULLs
- Mixing GROUPING SETS with regular GROUP BY

## How to Fix

```sql
-- WRONG: Cannot distinguish subtotal NULL from data NULL
SELECT department, SUM(salary)
FROM employees
GROUP BY ROLLUP(department);
-- NULL department could be subtotal or actual NULL department

-- CORRECT: Use GROUPING() function
SELECT
    CASE WHEN GROUPING(department) = 1 THEN 'ALL DEPTS'
         ELSE COALESCE(department, 'Unknown')
    END AS dept,
    SUM(salary)
FROM employees
GROUP BY ROLLUP(department);
```

## Examples

```sql
-- Example 1: ROLLUP for hierarchical subtotals
SELECT department, role, SUM(salary)
FROM employees
GROUP BY ROLLUP(department, role);

-- Example 2: CUBE for all combinations
SELECT department, role, SUM(salary)
FROM employees
GROUP BY CUBE(department, role);

-- Example 3: GROUPING SETS for specific subtotals
SELECT department, role, SUM(salary)
FROM employees
GROUP BY GROUPING SETS (
    (department, role),
    (department),
    ()
);
```

## Related Errors

- [Group by error](sql-group-by-error) -- GROUP BY clause issues
- [No grouping error](sql-no-grouping) -- missing GROUP BY
