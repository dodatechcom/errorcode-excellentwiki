---
title: "[Solution] SQL GROUP BY / Aggregate Error Fix"
description: "Fix 'In aggregated query without GROUP BY' when a SELECT mixes aggregated and non-aggregated columns."
languages: ["sql"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# SQL GROUP BY / Aggregate Error Fix

This error occurs when a SELECT query mixes aggregated columns (SUM, COUNT, AVG) with non-aggregated columns without a GROUP BY clause. The message reads: `In aggregated query without GROUP BY, expression #X of SELECT list contains nonaggregated column`.

## Description

When you use an aggregate function alongside regular columns, the database needs to know how to group the non-aggregated values. Without GROUP BY, the result is ambiguous — which row's value should be returned for the non-aggregated column?

## Common Causes

- **Missing GROUP BY** — mixing aggregate and non-aggregate columns without grouping.
- **GROUP BY missing a column** — not all non-aggregated columns are in GROUP BY.
- **Using aggregate in WHERE** — aggregates belong in HAVING, not WHERE.
- **SELECT * with aggregates** — wildcard pulls all columns including non-aggregated ones.

## How to Fix

### Fix 1: Add GROUP BY for non-aggregated columns

```sql
-- Wrong — mixing aggregate with non-aggregate
SELECT department, COUNT(*) FROM employees;

-- Correct — group by the non-aggregated column
SELECT department, COUNT(*) FROM employees GROUP BY department;
```

### Fix 2: Include all non-aggregated columns in GROUP BY

```sql
-- Wrong — "name" is not in GROUP BY
SELECT department, name, COUNT(*) FROM employees GROUP BY department;

-- Correct
SELECT department, name, COUNT(*) FROM employees GROUP BY department, name;
```

### Fix 3: Use HAVING instead of WHERE for aggregates

```sql
-- Wrong — can't use aggregate in WHERE
SELECT department, COUNT(*) FROM employees WHERE COUNT(*) > 5 GROUP BY department;

-- Correct — use HAVING
SELECT department, COUNT(*) FROM employees GROUP BY department HAVING COUNT(*) > 5;
```

### Fix 4: Use ONLY_FULL_GROUP_BY mode (MySQL)

```sql
-- Enable strict mode to catch errors at query time
SET sql_mode = 'ONLY_FULL_GROUP_BY';

-- Then always write correct GROUP BY queries
SELECT department, COUNT(*) AS cnt
FROM employees
GROUP BY department;
```

## Examples

```sql
SELECT name, MAX(salary) FROM employees;
-- ERROR 1140: In aggregated query without GROUP BY, expression #1
-- of SELECT list contains nonaggregated column 'name'

SELECT department, name, COUNT(*) FROM employees GROUP BY department;
-- ERROR 1055: Expression #2 of SELECT list is not in GROUP BY clause
```

## Related Errors

- [Join Error](join-error.md) — invalid JOIN with GROUP BY.
- [Subquery Error](subquery-error.md) — subquery returns too many rows.
- [Null Constraint](null-constraint.md) — aggregate returns NULL unexpectedly.
