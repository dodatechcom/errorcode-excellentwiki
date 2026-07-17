---
title: "[Solution] SQL Using Filesort Missing Index Fix"
description: "Fix slow queries using filesort by adding appropriate indexes for ORDER BY and GROUP BY."
languages: ["sql"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["filesort", "index", "order-by", "performance", "query-optimization"]
weight: 5
---

This error occurs when MySQL cannot use an index to satisfy an ORDER BY or GROUP BY clause and must perform a filesort. While not always an error, it indicates a performance problem.

## What This Error Means

When EXPLAIN shows `Using filesort`, MySQL is sorting the result set in memory or on disk instead of reading rows in index order. This significantly impacts query performance on large tables.

## Common Causes

- No index on the ORDER BY column
- ORDER BY mixes ASC and DESC directions
- ORDER BY references expressions instead of raw columns
- Multiple ORDER BY columns not covered by a composite index

## How to Fix

### Fix 1: Add index for ORDER BY columns

```sql
-- Slow: filesort on large table
SELECT * FROM orders ORDER BY created_at DESC;

-- Fix: add index
CREATE INDEX idx_orders_created_at ON orders(created_at);
```

### Fix 2: Create composite index for multi-column ORDER BY

```sql
-- Query
SELECT * FROM orders WHERE user_id = 1 ORDER BY created_at DESC;

-- Composite index
CREATE INDEX idx_orders_user_created ON orders(user_id, created_at);
```

### Fix 3: Avoid expressions in ORDER BY

```sql
-- Bad: expression in ORDER BY
SELECT * FROM orders ORDER BY YEAR(created_at) DESC;

-- Good: order by the column directly
SELECT * FROM orders ORDER BY created_at DESC;
```

### Fix 4: Use EXPLAIN to verify

```sql
EXPLAIN SELECT * FROM orders WHERE user_id = 1 ORDER BY created_at DESC;
-- Check that type is ref and Extra does NOT say "Using filesort"
```

## Examples

```sql
EXPLAIN SELECT * FROM orders ORDER BY total DESC;
-- type: ALL, Extra: Using filesort (bad — full table scan + sort)

CREATE INDEX idx_orders_total ON orders(total);
EXPLAIN SELECT * FROM orders ORDER BY total DESC;
-- type: index, Extra: (no filesort — good)
```

## Related Errors

- [Missing Index Error](missing-index.md) — related performance issue
- [Column Not Found](column-not-found.md) — column doesn't exist
