---
title: "[Solution] SQL Syntax Error in Subquery"
description: "Fix 'SQL syntax error in subquery' when a nested query is malformed."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "sql"
tags: ["sql", "syntax, subquery"]
severity: "error"
---

# SQL Syntax Error in Subquery

## Error Message

```
You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'SELECT ...' (subquery)
```

## Common Causes

- Subquery returns more than one row when used with = instead of IN
- Missing parentheses around the subquery
- Correlated subquery references an alias that is not in scope
- Using a subquery in a context that does not support it, such as in DEFAULT values

## Solutions

### Solution 1: Use IN for multi-row subqueries

Use = for scalar subqueries that return one value, and IN for subqueries that return multiple rows.

```sql
-- Wrong: subquery returns multiple rows
SELECT * FROM users WHERE id = (SELECT user_id FROM orders WHERE total > 100);

-- Correct: use IN for multi-row results
SELECT * FROM users WHERE id IN (SELECT user_id FROM orders WHERE total > 100);

-- Correct: use = for scalar subquery (must return exactly one row)
SELECT * FROM users WHERE id = (SELECT MAX(user_id) FROM orders);

-- Correct: use EXISTS for correlated existence checks
SELECT * FROM users u WHERE EXISTS (
    SELECT 1 FROM orders o WHERE o.user_id = u.id AND o.total > 100
);
```

### Solution 2: Wrap subqueries in proper parentheses

Every subquery must be enclosed in parentheses.

```sql
-- Wrong: missing parentheses
SELECT * FROM users WHERE id SELECT user_id FROM orders;

-- Correct
SELECT * FROM users WHERE id IN (SELECT user_id FROM orders);

-- Wrong: nested subquery missing outer parentheses
SELECT * FROM (
    SELECT * FROM users WHERE id IN SELECT user_id FROM orders
) AS sub;

-- Correct
SELECT * FROM (
    SELECT * FROM users WHERE id IN (SELECT user_id FROM orders)
) AS sub;
```

### Solution 3: Use CTEs as a clearer alternative to subqueries

Common Table Expressions (CTEs) can replace complex nested subqueries for better readability.

```sql
-- Complex subquery (hard to read)
SELECT * FROM users WHERE id IN (
    SELECT user_id FROM orders WHERE product_id IN (
        SELECT id FROM products WHERE category = 'electronics'
    )
);

-- Equivalent CTE (clearer)
WITH electronics_products AS (
    SELECT id FROM products WHERE category = 'electronics'
),
electronics_orders AS (
    SELECT user_id FROM orders WHERE product_id IN (SELECT id FROM electronics_products)
)
SELECT * FROM users WHERE id IN (SELECT user_id FROM electronics_orders);
```

## Prevention Tips

- Use EXPLAIN or EXPLAIN ANALYZE to check if your subqueries are executed efficiently
- Convert correlated subqueries to JOINs when possible for better performance
- Test subqueries independently first to verify they return the expected results

## Related Errors

- [Syntax Error Select]({{< relref "/languages/sql/syntax-error-select.md" >}})
- [Syntax Error Join]({{< relref "/languages/sql/syntax-error-join.md" >}})
- [Sql Subquery Error]({{< relref "/languages/sql/sql-subquery-error.md" >}})
