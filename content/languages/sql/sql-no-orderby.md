---
title: "[Solution] SQL Not a GROUP BY Clause Fix"
description: "Fix 'Not a GROUP BY clause' when ORDER BY or HAVING references non-grouped columns."
languages: ["sql"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["group-by", "having", "order-by", "aggregation"]
weight: 5
---

This error occurs when ORDER BY or HAVING clauses reference columns that are not part of the GROUP BY clause or aggregate functions.

## What This Error Means

After GROUP BY is applied, only grouped columns and aggregates are available. Referencing other columns in ORDER BY or HAVING violates this constraint.

## Common Causes

- ORDER BY references a column not in SELECT or GROUP BY
- HAVING clause uses a non-aggregated column
- Incorrect GROUP BY placement in the query

## How to Fix

### Fix 1: Order by grouped or aggregated columns

```sql
-- Wrong
SELECT department, COUNT(*)
FROM employees
GROUP BY department
ORDER BY employee_name;

-- Correct
SELECT department, COUNT(*)
FROM employees
GROUP BY department
ORDER BY COUNT(*) DESC;
```

### Fix 2: Use column aliases in ORDER BY

```sql
SELECT department, COUNT(*) AS dept_count
FROM employees
GROUP BY department
ORDER BY dept_count DESC;
```

### Fix 3: Fix HAVING to use aggregates

```sql
-- Wrong
SELECT department, COUNT(*)
FROM employees
GROUP BY department
HAVING department = 'Engineering';

-- Correct
SELECT department, COUNT(*)
FROM employees
GROUP BY department
HAVING COUNT(*) > 5;
```

## Examples

```sql
SELECT user_id, SUM(amount)
FROM orders
GROUP BY user_id
ORDER BY created_at;
-- ERROR 1055: Not a GROUP BY clause
```

## Related Errors

- [GROUP BY Error](group-by-error.md) — SELECT not grouped
- [Unknown Column ORDER BY](sql-unknown-column-orderby.md) — column doesn't exist
