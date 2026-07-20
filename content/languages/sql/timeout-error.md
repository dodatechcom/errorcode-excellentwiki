---
title: "[Solution] Query Timeout Expired"
description: "Fix 'Query timeout expired' when a query runs longer than the allowed time limit."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "sql"
tags: ["sql", "performance, timeout"]
severity: "error"
---

# Query Timeout Expired

## Error Message

```
ERROR 1836: Managed thread timeout expired / Query timeout has expired — The query execution exceeded the configured timeout limit.
```

## Common Causes

- Query is too complex and takes longer than the application or database timeout setting
- Missing indexes force the database to perform full table scans on large tables
- Lock contention causes the query to wait for other transactions to release locks
- Network latency between application and database adds to total query execution time

## Solutions

### Solution 1: Optimize the query to reduce execution time

Rewrite slow queries to be more efficient.

```sql
-- Wrong: SELECT * fetches unnecessary columns
SELECT * FROM orders o
JOIN users u ON o.user_id = u.id
JOIN products p ON o.product_id = p.id
WHERE o.created_at > '2026-01-01';

-- Correct: select only needed columns
SELECT o.id, o.total, u.name, p.title
FROM orders o
JOIN users u ON o.user_id = u.id
JOIN products p ON o.product_id = p.id
WHERE o.created_at > '2026-01-01';

-- Add appropriate indexes
CREATE INDEX idx_orders_created ON orders(created_at);
CREATE INDEX idx_orders_user ON orders(user_id);
```

### Solution 2: Increase timeout settings appropriately

Adjust the timeout configuration if the query is legitimately long-running.

```sql
-- MySQL: increase timeout
SET SESSION max_execution_time = 300000; -- 5 minutes in ms

-- PostgreSQL: increase statement timeout
SET statement_timeout = '300s'; -- 5 minutes

-- SQL Server: increase timeout (in seconds)
SET LOCK_TIMEOUT 300000; -- 5 minutes

-- Application-level: set connection timeout
-- JDBC: DriverManager.getConnection(url, props)
-- props.setProperty("socketTimeout", "300");

-- Use SHOW PROCESSLIST to check running queries
SHOW PROCESSLIST; -- MySQL
SELECT * FROM pg_stat_activity; -- PostgreSQL
SELECT * FROM sys.dm_exec_requests; -- SQL Server
```

### Solution 3: Use query profiling to identify bottlenecks

Analyze query execution to find and fix performance issues.

```sql
-- MySQL: use EXPLAIN to analyze
EXPLAIN SELECT o.id, o.total, u.name
FROM orders o
JOIN users u ON o.user_id = u.id
WHERE o.created_at > '2026-01-01';

-- PostgreSQL: use EXPLAIN ANALYZE
EXPLAIN ANALYZE
SELECT o.id, o.total, u.name
FROM orders o
JOIN users u ON o.user_id = u.id
WHERE o.created_at > '2026-01-01';

-- SQL Server: include actual execution plan
SET STATISTICS IO ON;
SET STATISTICS TIME ON;
SELECT o.id, o.total, u.name
FROM orders o
JOIN users u ON o.user_id = u.id
WHERE o.created_at > '2026-01-01';
```

## Prevention Tips

- Use EXPLAIN or EXPLAIN ANALYZE regularly to identify slow queries before they cause timeout errors
- Add indexes on columns used in WHERE, JOIN, and ORDER BY clauses to speed up query execution
- Set reasonable timeout values — too short causes unnecessary failures, too long ties up resources

## Related Errors

- [Slow Query]({{< relref "/languages/sql/slow-query.md" >}})
- [Lock Timeout]({{< relref "/languages/sql/lock-timeout.md" >}})
- [Deadlock Error]({{< relref "/languages/sql/deadlock-error.md" >}})
