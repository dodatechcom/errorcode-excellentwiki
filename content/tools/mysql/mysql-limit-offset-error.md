---
title: "[Solution] MySQL Limit Offset Error"
description: "Fix MySQL LIMIT OFFSET error when large offset values cause slow queries or unexpected result sets"
tools: ["mysql"]
error-types: ["tool-error"]
severities: ["error"]
---

# MySQL Limit OFFSET Error

Queries with large OFFSET values in LIMIT clauses become extremely slow because MySQL must scan and discard all preceding rows. This causes timeouts and memory exhaustion.

## Common Causes

- OFFSET is very large (e.g., OFFSET 1000000) on unindexed queries
- Pagination relies on OFFSET instead of cursor-based approach
- LIMIT without ORDER BY produces non-deterministic results
- OFFSET combined with JOINs multiplies the work per row
- SELECT * with large OFFSET consumes excessive memory

## How to Fix

### Use Cursor-Based Pagination

```sql
-- Bad: slow OFFSET-based pagination
SELECT * FROM orders ORDER BY id LIMIT 20 OFFSET 1000000;

-- Good: cursor-based pagination using WHERE
SELECT * FROM orders
WHERE id > 1000000  -- last seen ID
ORDER BY id
LIMIT 20;
```

### Add Index for ORDER BY Column

```sql
-- Without index, MySQL must sort all rows before applying LIMIT
CREATE INDEX idx_orders_created_at ON orders(created_at);

SELECT * FROM orders
ORDER BY created_at DESC
LIMIT 20 OFFSET 1000000;
```

### Use Covering Index for Pagination

```sql
-- Covering index avoids table lookup for each row
CREATE INDEX idx_orders_id_customer_total
  ON orders(id, customer_id, total);

SELECT id, customer_id, total FROM orders
ORDER BY id LIMIT 20 OFFSET 1000000;
```

### Avoid Deep Pagination

```sql
-- Instead of showing page 50000, use "load more"
SELECT * FROM orders
WHERE id < :last_seen_id
ORDER BY id DESC
LIMIT 20;
```

### Use SQL_CALC_FOUND_ROWS Carefully

```sql
-- Get total count without separate query
SELECT SQL_CALC_FOUND_ROWS * FROM orders
WHERE status = 'active'
LIMIT 20 OFFSET 100;

SELECT FOUND_ROWS() as total;
-- Warning: SQL_CALC_FOUND_ROWS can be slow on large tables
```

## Examples

```
-- Query with OFFSET 1000000 takes 45 seconds
-- Same query with cursor pagination takes 0.002 seconds

EXPLAIN SELECT * FROM orders ORDER BY id LIMIT 20 OFFSET 1000000;
-- Shows: Using filesort (no usable index for offset)
```

## Related Errors

- [MySQL Explain Error]({{< relref "/tools/mysql/mysql-explain-error" >}}) -- explain issues
- [MySQL Net Read Timeout]({{< relref "/tools/mysql/mysql-net-read-timeout" >}}) -- timeout issues
- [MySQL Query Too Slow]({{< relref "/tools/mysql/mysql-long-query-error" >}}) -- performance
