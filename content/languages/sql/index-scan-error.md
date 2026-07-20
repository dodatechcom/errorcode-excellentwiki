---
title: "[Solution] Full Table Scan Error"
description: "Fix 'Full table scan error' when the database scans entire tables instead of using indexes."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "sql"
tags: ["sql", "performance, index, full-scan"]
severity: "error"
---

# Full Table Scan Error

## Error Message

```
Full table scan detected on large table — The query is performing a full table scan instead of using an index, causing poor performance.
```

## Common Causes

- No index exists on the columns used in WHERE, JOIN, or ORDER BY clauses
- Index is not used because the query violates the leftmost prefix rule for composite indexes
- The optimizer chooses a full table scan because the table is small or the query selects most rows
- Function calls on indexed columns prevent index usage (e.g., WHERE YEAR(date) = 2026)

## Solutions

### Solution 1: Create indexes on columns used in WHERE and JOIN

Add indexes on columns that are frequently filtered or joined.

```sql
-- Check for full table scans (MySQL)
EXPLAIN SELECT * FROM orders WHERE user_id = 100;
-- Look for type: ALL (full scan)

-- Create index on the filtered column
CREATE INDEX idx_orders_user_id ON orders(user_id);

-- Composite index for multi-column queries
CREATE INDEX idx_orders_user_status ON orders(user_id, status);

-- PostgreSQL: check for sequential scans
EXPLAIN ANALYZE SELECT * FROM orders WHERE user_id = 100;
-- Look for Seq Scan

-- Create index (PostgreSQL)
CREATE INDEX CONCURRENTLY idx_orders_user_id ON orders(user_id);
```

### Solution 2: Avoid functions on indexed columns

Wrap the value in the function instead of the column to preserve index usage.

```sql
-- Wrong: function on column prevents index usage
SELECT * FROM orders WHERE YEAR(created_at) = 2026;
SELECT * FROM users WHERE LOWER(email) = 'alice@example.com';
SELECT * FROM orders WHERE DATE(created_at) = '2026-03-15';

-- Correct: apply function to the value instead
SELECT * FROM orders
WHERE created_at >= '2026-01-01' AND created_at < '2027-01-01';

SELECT * FROM users
WHERE email = LOWER('Alice@example.com');

-- PostgreSQL: create expression index for function-based queries
CREATE INDEX idx_users_lower_email ON users(LOWER(email));

-- MySQL 8.0+: functional index
CREATE INDEX idx_orders_date ON orders((DATE(created_at)));
```

### Solution 3: Use covering indexes to avoid table lookups

Include all needed columns in the index so the query is answered from the index alone.

```sql
-- Covering index: includes all columns in the query
-- Query: SELECT user_id, status FROM orders WHERE user_id = 100
CREATE INDEX idx_orders_covering ON orders(user_id, status);

-- PostgreSQL: INCLUDE columns (index-only scan)
CREATE INDEX idx_orders_covering ON orders(user_id) INCLUDE (status, total);

-- SQL Server: included columns
CREATE INDEX idx_orders_covering ON orders(user_id) INCLUDE (status, total);

-- Check if index is being used
EXPLAIN SELECT user_id, status FROM orders WHERE user_id = 100;
-- Look for 'Using index' (MySQL) or 'Index Only Scan' (PostgreSQL)
```

## Prevention Tips

- Run EXPLAIN on slow queries to identify full table scans and add appropriate indexes
- Avoid wrapping indexed columns in functions — apply the function to the value instead
- Use covering indexes for frequently executed queries that select only a few columns

## Related Errors

- [Slow Query]({{< relref "/languages/sql/slow-query.md" >}})
- [Index Constraint Error]({{< relref "/languages/sql/index-constraint-error.md" >}})
- [Sql Missing Index]({{< relref "/languages/sql/sql-missing-index.md" >}})
