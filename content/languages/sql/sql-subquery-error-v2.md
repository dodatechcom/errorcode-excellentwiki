---
title: "[Solution] SQL Subquery Returns More Than One Row Error Fix"
description: "Fix SQL subquery errors when a subquery expected to return one row returns multiple rows."
languages: ["sql"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["subquery", "scalar", "more-than-one-row", "sql"]
weight: 5
---

# SQL Subquery Returns More Than One Row Error Fix

A SQL subquery error occurs when a subquery used in a scalar context (WHERE, INSERT, assignment) returns multiple rows instead of exactly one.

## What This Error Means

When a subquery is used where a single value is expected (e.g., `WHERE col = (SELECT ...)`) but returns multiple rows, the database cannot assign multiple values to a single comparison.

## Common Causes

- Missing LIMIT or aggregation in subquery
- Using = instead of IN for multi-row subqueries
- Subquery logic returns duplicates
- Correlated subquery not properly filtered

## How to Fix

### 1. Use IN instead of = for multi-row results

```sql
-- WRONG: Subquery returns multiple rows
SELECT * FROM orders
WHERE user_id = (SELECT id FROM users WHERE active = 1);

-- CORRECT: Use IN for multiple values
SELECT * FROM orders
WHERE user_id IN (SELECT id FROM users WHERE active = 1);
```

### 2. Add LIMIT 1 for single-row expectation

```sql
-- CORRECT: If you need exactly one row
SELECT * FROM orders
WHERE user_id = (SELECT id FROM users WHERE active = 1 LIMIT 1);
```

### 3. Use EXISTS for existence checks

```sql
-- CORRECT: Use EXISTS instead of subquery comparison
SELECT * FROM orders o
WHERE EXISTS (
    SELECT 1 FROM users u
    WHERE u.id = o.user_id AND u.active = 1
);
```

### 4. Aggregate the subquery

```sql
-- CORRECT: Use MAX/MIN to get single value
SELECT * FROM orders
WHERE user_id = (SELECT MAX(id) FROM users WHERE active = 1);
```

## Related Errors

- [SQL Column Not Found](sql-column-not-found-v2) — column missing
- [SQL Group By Error](sql-group-by-error-v2) — grouping issues
- [SQL Window Function Error](sql-window-function-v2) — window functions
