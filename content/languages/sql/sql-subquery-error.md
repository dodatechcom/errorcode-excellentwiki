---
title: "[Solution] SQL Subquery Returns More Than One Row Error Fix"
description: "Fix 'subquery returns more than one row' in SQL. Use IN, ANY, or ALL operators when subqueries return multiple values."
languages: ["sql"]
error-types: ["logic-error"]
severities: ["error"]
weight: 5
---

# SQL Subquery Returns More Than One Row Error Fix

The `subquery returns more than one row` error occurs when a scalar subquery (expected to return a single value) returns multiple rows instead.

## What This Error Means

SQL expects a scalar subquery to return exactly one value when used with `=`, `>`, `<`, or in a SELECT list. When the subquery returns multiple rows, the database cannot compare a single value to a result set.

A typical error:

```
ERROR: subquery must return only one column
```

Or:

```
ERROR: more than one row returned by a subquery used as an expression
```

## Why It Happens

Common causes include:

- **Missing WHERE clause** — Subquery returns all rows instead of one.
- **Using = instead of IN** — `WHERE id = (SELECT id FROM table)` fails if multiple rows.
- **No GROUP BY in subquery** — Aggregation missing from subquery.
- **Incorrect correlation** — Subquery not properly filtered.
- **Using ANY/ALL incorrectly** — Wrong operator for the comparison.

## How to Fix It

### Fix 1: Use IN for multiple values

```sql
-- WRONG: Subquery returns multiple rows
SELECT * FROM orders
WHERE user_id = (SELECT id FROM users WHERE active = 1);

-- RIGHT: Use IN
SELECT * FROM orders
WHERE user_id IN (SELECT id FROM users WHERE active = 1);
```

### Fix 2: Use ANY or ALL for comparisons

```sql
-- RIGHT: Compare against multiple values
SELECT * FROM products
WHERE price > ALL (SELECT price FROM products WHERE category = 'budget');

SELECT * FROM products
WHERE price < ANY (SELECT price FROM products WHERE category = 'premium');
```

### Fix 3: Add LIMIT 1 for single row expected

```sql
-- RIGHT: Force single row
SELECT * FROM orders
WHERE user_id = (SELECT id FROM users WHERE active = 1 LIMIT 1);
```

### Fix 4: Add aggregation to subquery

```sql
-- RIGHT: Aggregate to single value
SELECT * FROM orders
WHERE total = (SELECT MAX(total) FROM orders);
```

### Fix 5: Use EXISTS for existence checks

```sql
-- RIGHT: Check if any row exists
SELECT * FROM users u
WHERE EXISTS (
    SELECT 1 FROM orders o WHERE o.user_id = u.id
);
```

## Common Mistakes

- **Using `=` with a subquery that returns multiple rows** — Use `IN` instead.
- **Forgetting that EXISTS is more efficient than IN for large datasets** — EXISTS short-circuits.
- **Not adding DISTINCT when using IN** — Duplicates can cause unexpected behavior.

## Related Pages

- [SQL Column Ambiguous](sql-column-ambiguous) — Ambiguous column references
- [SQL Group By Error](sql-group-by-error) — GROUP BY expression issues
- [SQL Recursive CTE Error](sql-recursive-cte-error) — CTE recursion issues
