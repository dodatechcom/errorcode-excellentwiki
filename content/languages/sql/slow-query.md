---
title: "[Solution] Slow Query Execution"
description: "Fix 'Slow query execution' when a query takes too long to complete due to performance issues."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "sql"
tags: ["sql", "performance, slow-query, optimization"]
severity: "error"
---

# Slow Query Execution

## Error Message

```
Query is slow to execute / Slow query logged in slow_query_log — The query execution time exceeds the expected threshold.
```

## Common Causes

- Missing indexes on columns used in WHERE, JOIN, or ORDER BY clauses
- SELECT * fetches unnecessary columns increasing I/O and network overhead
- Unoptimized subqueries that could be rewritten as JOINs or CTEs
- Large table scans without filtering, processing millions of unnecessary rows

## Solutions

### Solution 1: Add indexes on frequently queried columns

Create indexes to speed up data retrieval operations.

```sql
-- Find slow queries in MySQL
SHOW VARIABLES LIKE 'slow_query%';
SET GLOBAL slow_query_log = ON;
SET GLOBAL long_query_time = 2; -- log queries > 2 seconds

-- Add index for frequently filtered columns
CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_orders_date ON orders(created_at);
CREATE INDEX idx_orders_user_date ON orders(user_id, created_at);

-- PostgreSQL: find slow queries
SELECT query, mean_exec_time, calls
FROM pg_stat_statements
ORDER BY mean_exec_time DESC LIMIT 10;

-- Create appropriate indexes
CREATE INDEX CONCURRENTLY idx_users_email ON users(email);
```

### Solution 2: Rewrite queries for better performance

Optimize query structure to reduce the work the database needs to do.

```sql
-- Wrong: correlated subquery (runs once per row)
SELECT * FROM users u
WHERE EXISTS (SELECT 1 FROM orders o WHERE o.user_id = u.id AND o.total > 100);

-- Correct: JOIN is more efficient
SELECT DISTINCT u.*
FROM users u
JOIN orders o ON u.id = o.user_id
WHERE o.total > 100;

-- Wrong: subquery in SELECT
SELECT name, (SELECT COUNT(*) FROM orders o WHERE o.user_id = u.id) AS order_count
FROM users u;

-- Correct: LEFT JOIN with GROUP BY
SELECT u.name, COUNT(o.id) AS order_count
FROM users u
LEFT JOIN orders o ON u.id = o.user_id
GROUP BY u.id, u.name;

-- Use EXISTS instead of IN for large subqueries
SELECT * FROM users WHERE id IN (SELECT user_id FROM orders);
-- Better:
SELECT * FROM users u WHERE EXISTS (SELECT 1 FROM orders o WHERE o.user_id = u.id);
```

### Solution 3: Use EXPLAIN to analyze and optimize queries

Examine the query execution plan to identify bottlenecks.

```sql
-- MySQL: analyze the execution plan
EXPLAIN SELECT u.name, o.total
FROM users u
JOIN orders o ON u.id = o.user_id
WHERE o.created_at > '2026-01-01';

-- PostgreSQL: detailed analysis with actual timings
EXPLAIN (ANALYZE, BUFFERS, FORMAT TEXT)
SELECT u.name, o.total
FROM users u
JOIN orders o ON u.id = o.user_id
WHERE o.created_at > '2026-01-01';

-- SQL Server: display execution plan
SET SHOWPLAN_XML ON;
SELECT u.name, o.total
FROM users u
JOIN orders o ON u.id = o.user_id
WHERE o.created_at > '2026-01-01';
```

## Prevention Tips

- Enable the slow query log and regularly review it to identify performance bottlenecks
- Use EXPLAIN or EXPLAIN ANALYZE before deploying complex queries to production
- Monitor the query cache hit ratio and adjust buffer pool size for better performance

## Related Errors

- [Timeout Error]({{< relref "/languages/sql/timeout-error.md" >}})
- [Index Scan Error]({{< relref "/languages/sql/index-scan-error.md" >}})
- [Memory Error]({{< relref "/languages/sql/memory-error.md" >}})
