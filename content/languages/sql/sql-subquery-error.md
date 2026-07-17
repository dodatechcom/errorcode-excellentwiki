---
title: "[Solution] SQL Subquery Returns More Than 1 Row Fix"
description: "Fix 'Subquery returns more than 1 row' when a scalar subquery returns multiple results."
languages: ["sql"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["subquery", "scalar", "single-row", "IN", "EXISTS"]
weight: 5
---

This error occurs when a subquery that is expected to return a single value (scalar) returns multiple rows. The message reads: `Subquery returns more than 1 row`.

## What This Error Means

The SQL parser expects a scalar subquery (one row, one column) in contexts like `=`, but the subquery returns multiple rows. This commonly happens in WHERE clauses and SELECT expressions.

## Common Causes

- Using `=` instead of `IN` for multi-row subqueries
- Subquery lacks proper WHERE clause to limit results
- Missing GROUP BY to aggregate results

## How to Fix

### Fix 1: Use IN instead of =

```sql
-- Wrong: subquery returns multiple rows
SELECT * FROM orders
WHERE user_id = (SELECT id FROM users WHERE status = 'active');

-- Correct: use IN
SELECT * FROM orders
WHERE user_id IN (SELECT id FROM users WHERE status = 'active');
```

### Fix 2: Limit the subquery to one row

```sql
-- Use LIMIT 1
SELECT * FROM orders
WHERE user_id = (SELECT id FROM users WHERE status = 'active' LIMIT 1);
```

### Fix 3: Use EXISTS for correlated subqueries

```sql
SELECT * FROM orders o
WHERE EXISTS (
    SELECT 1 FROM users u
    WHERE u.id = o.user_id AND u.status = 'active'
);
```

## Examples

```sql
SELECT name FROM products
WHERE category_id = (SELECT id FROM categories WHERE name = 'Electronics');
-- ERROR 1242: Subquery returns more than 1 row
```

## Related Errors

- [Column Not Found](column-not-found.md) — missing column in subquery
- [GROUP BY Error](group-by-error.md) — aggregation issue
