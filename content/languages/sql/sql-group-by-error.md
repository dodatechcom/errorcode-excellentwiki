---
title: "[Solution] SQL GROUP BY Error Fix"
description: "Fix 'Expression not in GROUP BY clause' when a SELECT column is not aggregated or grouped."
languages: ["sql"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["group-by", "aggregate", "select", "sql-mode"]
weight: 5
---

This error occurs when a SELECT statement includes a column that is neither aggregated nor included in the GROUP BY clause. The message reads: `Expression not in GROUP BY clause`.

## What This Error Means

When using GROUP BY, every non-aggregated column in SELECT must appear in the GROUP BY clause. MySQL's `ONLY_FULL_GROUP_BY` mode enforces this ANSI SQL standard.

## Common Causes

- SELECT includes columns not in GROUP BY or aggregate function
- Using `SELECT *` with GROUP BY
- Missing GROUP BY for aggregate queries
- Using `sql_mode=ONLY_FULL_GROUP_BY`

## How to Fix

### Fix 1: Add all non-aggregated columns to GROUP BY

```sql
-- Wrong
SELECT department, name, COUNT(*)
FROM employees
GROUP BY department;

-- Correct
SELECT department, name, COUNT(*)
FROM employees
GROUP BY department, name;
```

### Fix 2: Use aggregate functions

```sql
-- Get one name per department
SELECT department, MAX(name) AS sample_name, COUNT(*)
FROM employees
GROUP BY department;
```

### Fix 3: Use ANY_VALUE for non-deterministic columns

```sql
SELECT department, ANY_VALUE(name), COUNT(*)
FROM employees
GROUP BY department;
```

## Examples

```sql
SELECT user_id, created_at, COUNT(*)
FROM orders
GROUP BY user_id;
-- ERROR 1055: Expression not in GROUP BY clause
```

## Related Errors

- [No GROUP BY Expression](no-grouping.md) — related GROUP BY issue
- [Unknown Column in ORDER BY](sql-unknown-column-orderby.md) — ORDER BY references non-grouped column
