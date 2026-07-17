---
title: "[Solution] SQL HAVING Clause Error Fix"
description: "Fix 'Not a GROUP BY expression in HAVING' when HAVING references non-grouped, non-aggregated columns."
languages: ["sql"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["having", "group-by", "aggregate", "filter"]
weight: 5
---

This error occurs when the HAVING clause references columns that are not in the GROUP BY clause or inside aggregate functions.

## What This Error Means

HAVING filters groups after GROUP BY is applied. Like SELECT with GROUP BY, HAVING can only reference grouped columns or aggregate expressions.

## Common Causes

- HAVING references a column not in GROUP BY
- HAVING uses a column without aggregate function
- Confusing WHERE and HAVING usage

## How to Fix

### Fix 1: Use aggregate functions in HAVING

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

### Fix 2: Use WHERE for pre-aggregation filtering

```sql
-- Filter BEFORE grouping — use WHERE
SELECT department, COUNT(*)
FROM employees
WHERE status = 'active'
GROUP BY department
HAVING COUNT(*) > 5;
```

### Fix 3: Include column in GROUP BY

```sql
SELECT department, status, COUNT(*)
FROM employees
GROUP BY department, status
HAVING status = 'active';
```

## Examples

```sql
SELECT user_id, SUM(amount)
FROM orders
GROUP BY user_id
HAVING created_at > '2024-01-01';
-- ERROR 1055: Not a GROUP BY expression in HAVING
```

## Related Errors

- [GROUP BY Error](group-by-error.md) — SELECT not grouped
- [No Grouping](no-grouping.md) — related GROUP BY issue
