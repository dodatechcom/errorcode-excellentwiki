---
title: "[Solution] Connection Pool Exhausted"
description: "Fix 'Connection pool exhausted' when all available database connections are in use."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "sql"
tags: ["sql", "performance, connection, pool"]
severity: "error"
---

# Connection Pool Exhausted

## Error Message

```
Cannot acquire connection from pool / Connection pool exhausted — All connections in the pool are in use and no new connections can be created.
```

## Common Causes

- Too many concurrent queries running and not releasing connections back to the pool
- Connection leaks where connections are opened but never closed or returned
- Pool size is too small for the application's concurrency requirements
- Slow queries hold connections for longer than expected, reducing pool throughput

## Solutions

### Solution 1: Fix connection leaks in application code

Ensure connections are properly closed and returned to the pool after use.

```sql
-- Wrong: connection not closed on error
-- conn = pool.get_connection()
-- cursor = conn.cursor()
-- cursor.execute("SELECT * FROM users")
-- result = cursor.fetchall()
-- # connection never returned to pool!

-- Correct: use try/finally or context managers
-- Python example:
-- with pool.get_connection() as conn:
--     with conn.cursor() as cursor:
--         cursor.execute("SELECT * FROM users")
--         result = cursor.fetchall()
--     # connection auto-returned to pool

-- SQL: use proper connection cleanup
-- Always COMMIT or ROLLBACK to release server-side resources
```

### Solution 2: Increase the connection pool size

Adjust pool settings to handle expected concurrent load.

```sql
-- MySQL: increase max connections
SET GLOBAL max_connections = 200;

-- Check current connections
SHOW STATUS LIKE 'Threads_connected';
SHOW VARIABLES LIKE 'max_connections';

-- PostgreSQL: adjust max connections
SHOW max_connections;
ALTER SYSTEM SET max_connections = 200;
-- Requires server restart

-- SQL Server: check connection count
SELECT COUNT(*) AS connection_count
FROM sys.dm_exec_sessions;

-- Application pool settings (common patterns):
-- min_pool_size: 5
-- max_pool_size: 50
-- connection_timeout: 30 seconds
-- idle_timeout: 300 seconds
```

### Solution 3: Optimize slow queries to free connections faster

Reduce query execution time so connections are released sooner.

```sql
-- Add indexes to speed up slow queries
CREATE INDEX idx_orders_user ON orders(user_id);
CREATE INDEX idx_orders_date ON orders(created_at);

-- Use query caching for repeated queries (MySQL)
SELECT SQL_CACHE * FROM users WHERE id = 1;

-- PostgreSQL: use prepared statements
PREPARE user_query AS
SELECT * FROM users WHERE id = $1;
EXECUTE user_query(1);

-- Monitor long-running queries
SELECT * FROM information_schema.PROCESSLIST
WHERE TIME > 30; -- MySQL: queries running > 30 seconds

SELECT pid, query, state, wait_event_type
FROM pg_stat_activity
WHERE state = 'active'; -- PostgreSQL
```

## Prevention Tips

- Always use connection pooling in production applications to manage database connections efficiently
- Set connection timeouts and idle timeouts to reclaim unused connections
- Monitor connection pool metrics (active, idle, waiting) to detect issues before they cause errors

## Related Errors

- [Timeout Error]({{< relref "/languages/sql/timeout-error.md" >}})
- [Memory Error]({{< relref "/languages/sql/memory-error.md" >}})
- [Transaction Error]({{< relref "/languages/sql/transaction-error.md" >}})
