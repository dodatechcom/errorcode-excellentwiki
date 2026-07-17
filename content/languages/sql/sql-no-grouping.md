---
title: "[Solution] SQL Not a GROUP BY Expression Fix"
description: "Fix 'Not a GROUP BY expression' when a column in SELECT is not grouped or aggregated."
languages: ["sql"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

This error occurs when a column in the SELECT list is neither part of the GROUP BY clause nor wrapped in an aggregate function. It is a variant of the GROUP BY error.

## What This Error Means

With `ONLY_FULL_GROUP_BY` mode, every column in SELECT must either appear in GROUP BY or be used inside an aggregate function like COUNT, SUM, MAX, MIN, or AVG.

## Common Causes

- SELECT includes a raw column without grouping by it
- Using `SELECT *` with GROUP BY
- Mixing aggregated and non-aggregated data incorrectly

## How to Fix

### Fix 1: Include the column in GROUP BY

```sql
-- Wrong
SELECT department, employee_name, COUNT(*)
FROM employees
GROUP BY department;

-- Correct
SELECT department, employee_name, COUNT(*)
FROM employees
GROUP BY department, employee_name;
```

### Fix 2: Use an aggregate function

```sql
SELECT department, MAX(employee_name), COUNT(*)
FROM employees
GROUP BY department;
```

### Fix 3: Use ANY_VALUE

```sql
SELECT department, ANY_VALUE(employee_name), COUNT(*)
FROM employees
GROUP BY department;
```

## Examples

```sql
SELECT category, title, COUNT(*)
FROM products
GROUP BY category;
-- ERROR 1055: Not a GROUP BY expression
```

## Related Errors

- [GROUP BY Error](group-by-error.md) — related GROUP BY issue
- [No GROUP BY](no-grouping.md) — missing GROUP BY clause
