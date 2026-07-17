---
title: "[Solution] SQL Unknown Column in ORDER BY Fix"
description: "Fix 'Unknown column in ORDER BY clause' when ORDER BY references a non-existent or non-grouped column."
languages: ["sql"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

This error occurs when the ORDER BY clause references a column that does not exist or is not available in the current query context.

## What This Error Means

The database cannot find the column specified in the ORDER BY clause. This can happen when the column doesn't exist, or when using GROUP BY and the column is not in SELECT or GROUP BY.

## Common Causes

- Column name misspelled in ORDER BY
- Column not in SELECT list when using ONLY_FULL_GROUP_BY
- Ordering by alias that wasn't defined
- Column from a table not in the FROM clause

## How to Fix

### Fix 1: Verify the column exists

```sql
-- Check available columns
SHOW COLUMNS FROM orders;

-- Use correct column name
SELECT * FROM orders ORDER BY created_at DESC;
```

### Fix 2: Order by column alias

```sql
SELECT name, price * quantity AS total
FROM order_items
ORDER BY total DESC;
```

### Fix 3: Order by column position

```sql
SELECT name, price, quantity
FROM order_items
ORDER BY 3 DESC; -- orders by the 3rd column (quantity)
```

## Examples

```sql
SELECT id, name FROM users ORDER BY email;
-- ERROR 1054: Unknown column 'email' in 'order clause'
```

## Related Errors

- [Column Not Found](column-not-found.md) — column doesn't exist
- [GROUP BY Error](group-by-error.md) — GROUP BY related issue
