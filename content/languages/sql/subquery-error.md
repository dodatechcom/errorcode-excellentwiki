---
title: "[Solution] SQL Subquery Returns More Than One Row Error Fix"
description: "Fix 'Subquery returns more than 1 row' when a scalar subquery unexpectedly returns multiple rows."
languages: ["sql"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["subquery", "more-than-one-row", "scalar-subquery"]
weight: 5
---

# SQL Subquery Returns More Than One Row Error Fix

This error occurs when a subquery used in a scalar context returns more than one row. The message reads: `Subquery returns more than 1 row`.

## Description

Some SQL contexts expect a single value (scalar): comparisons with `=`, assignments in UPDATE, or columns in SELECT. If the subquery returns multiple rows, the database cannot map them to a single value and raises an error.

## Common Causes

- **Missing WHERE clause** — subquery returns all rows instead of one.
- **Missing aggregate function** — need MAX/MIN/SUM but used a bare SELECT.
- **Incorrect correlation** — subquery isn't properly linked to the outer query.
- **Using = instead of IN** — the subquery legitimately returns multiple rows.

## How to Fix

### Fix 1: Use IN instead of =

```sql
-- Wrong — subquery returns multiple rows
SELECT * FROM orders
WHERE user_id = (SELECT id FROM users WHERE role = 'admin');

-- Correct — use IN for multiple values
SELECT * FROM orders
WHERE user_id IN (SELECT id FROM users WHERE role = 'admin');
```

### Fix 2: Add an aggregate function

```sql
-- Wrong — returns multiple rows
SELECT * FROM orders
WHERE total = (SELECT total FROM orders WHERE user_id = 1);

-- Correct — use MAX to get a single value
SELECT * FROM orders
WHERE total = (SELECT MAX(total) FROM orders WHERE user_id = 1);
```

### Fix 3: Add a LIMIT clause

```sql
-- Return only one row
SELECT * FROM orders
WHERE user_id = (SELECT id FROM users WHERE role = 'admin' LIMIT 1);
```

### Fix 4: Use EXISTS for existence checks

```sql
-- Instead of comparing to a subquery, check if rows exist
SELECT * FROM users u
WHERE EXISTS (SELECT 1 FROM orders o WHERE o.user_id = u.id);
```

## Examples

```sql
SELECT name FROM departments
WHERE id = (SELECT department_id FROM employees WHERE status = 'active');
-- ERROR 1242: Subquery returns more than 1 row

UPDATE users SET role = 'premium'
WHERE id = (SELECT user_id FROM payments WHERE amount > 100);
-- ERROR 1242: Subquery returns more than 1 row
```

## Related Errors

- [Join Error](join-error.md) — invalid use of JOIN with aggregates.
- [Aggregate Error](aggregate-error.md) — GROUP BY misuse.
- [Null Constraint](null-constraint.md) — subquery returns NULL unexpectedly.
