---
title: "[Solution] MySQL Correlated Subquery Performance Error"
description: "Fix MySQL correlated subquery performance error when nested queries execute once per row causing extreme slowness"
tools: ["mysql"]
error-types: ["tool-error"]
severities: ["error"]
---

# MySQL Correlated Subquery Performance Error

A correlated subquery references the outer query and executes once for each row in the outer result set. This creates O(n*m) complexity that causes severe performance degradation on large tables.

## Common Causes

- Subquery in WHERE clause references outer table columns
- SELECT list contains a correlated subquery for each row
- NOT EXISTS with correlated subquery scans the full table per row
- MySQL optimizer cannot decorrelate the subquery
- Missing indexes on columns used in the correlation

## How to Fix

### Convert to JOIN

```sql
-- Slow: correlated subquery
SELECT o.id, o.total,
  (SELECT MAX(created_at) FROM orders o2 WHERE o2.customer_id = o.id) as last_order
FROM orders o;

-- Fast: LEFT JOIN
SELECT o.id, o.total, MAX(o2.created_at) as last_order
FROM orders o
LEFT JOIN orders o2 ON o2.customer_id = o.id
GROUP BY o.id, o.total;
```

### Rewrite EXISTS as JOIN

```sql
-- Slow: correlated NOT EXISTS
SELECT * FROM customers c
WHERE NOT EXISTS (
  SELECT 1 FROM orders o WHERE o.customer_id = c.id AND o.status = 'active'
);

-- Fast: LEFT JOIN with NULL check
SELECT c.* FROM customers c
LEFT JOIN orders o ON o.customer_id = c.id AND o.status = 'active'
WHERE o.id IS NULL;
```

### Add Indexes for Correlation

```sql
-- Index on the correlation column
CREATE INDEX idx_orders_customer_id ON orders(customer_id);
```

### Use Window Functions (MySQL 8.0+)

```sql
-- Instead of correlated subquery for ranking
SELECT *,
  ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY created_at DESC) as rn
FROM orders;
```

### Force Subquery Materialization

```sql
-- MySQL can sometimes optimize by materializing the subquery
SELECT * FROM orders o
WHERE o.total > (
  SELECT AVG(o2.total) FROM orders o2
  WHERE o2.region = o.region
)
LIMIT 1000;
```

## Examples

```
Query runs in 45 minutes on 1M rows because the correlated
subquery executes 1,000,000 times. After converting to JOIN,
execution time drops to 2 seconds.
```

## Related Errors

- [MySQL Subquery Return More]({{< relref "/tools/mysql/mysql-subquery-return-more" >}}) -- subquery issues
- [MySQL Select Into Error]({{< relref "/tools/mysql/mysql-select-into-error" >}}) -- select issues
- [MySQL Explain Error]({{< relref "/tools/mysql/mysql-explain-error" >}}) -- explain issues
