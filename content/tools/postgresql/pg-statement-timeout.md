---
title: "[Solution] PostgreSQL Canceling Statement Due to Statement Timeout"
description: "Fix PostgreSQL statement timeout errors by optimizing slow queries, adjusting timeout settings, and adding proper indexes for better performance"
tools: ["postgresql"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
---

# PostgreSQL Canceling Statement Due to Statement Timeout

This error occurs when a SQL statement runs longer than the configured `statement_timeout` and PostgreSQL automatically cancels it. This is a safety mechanism to prevent runaway queries from consuming resources indefinitely.

## What This Error Means

PostgreSQL returns this error when the statement timeout is exceeded:

```
ERROR: canceling statement due to statement timeout
```

The statement is terminated and any changes it made (in a single statement context) are rolled back. Unlike `lock_timeout`, `statement_timeout` measures the total execution time of the statement, including time spent waiting for locks.

The default `statement_timeout` is 0 (no timeout). When set, it applies to all statements in the session unless overridden.

## Why It Happens

- A query performs a sequential scan on a large table without an index
- The query planner chose a poor execution plan due to outdated statistics
- A complex `JOIN` between large tables produces a cartesian product
- An `UPDATE` or `DELETE` modifies millions of rows in a single statement
- The database server is under heavy load and queries are queued
- A `SELECT` with `FOR UPDATE` is waiting for locks (lock wait time counts)
- Statistics are stale, causing the planner to underestimate row counts

## How to Fix It

### 1. Check the Current Timeout

```sql
SHOW statement_timeout;
```

### 2. Analyze the Slow Query

```sql
-- Add EXPLAIN ANALYZE to understand the execution plan
EXPLAIN (ANALYZE, BUFFERS, FORMAT TEXT)
SELECT * FROM large_table JOIN another_table ON ...;
```

### 3. Add Appropriate Indexes

```sql
-- Check if the query uses an index
EXPLAIN SELECT * FROM orders WHERE customer_id = 123;

-- If it shows Seq Scan, add an index
CREATE INDEX idx_orders_customer_id ON orders(customer_id);
```

### 4. Adjust the Timeout for Specific Operations

```sql
-- Allow long-running reports to complete
SET statement_timeout = '300s';
SELECT generate_report();

-- Or per-session
SET LOCAL statement_timeout = '10min';
```

### 5. Update Table Statistics

```sql
-- Stale statistics cause bad plans
ANALYZE large_table;

-- For more detailed analysis
VACUUM ANALYZE large_table;
```

### 6. Optimize Large Updates and Deletes

```sql
-- WRONG: single statement updating millions of rows
UPDATE orders SET status = 'archived' WHERE created_at < '2023-01-01';

-- BETTER: batch with explicit timeout awareness
DO $$
DECLARE
    batch_size INT := 10000;
    affected INT;
BEGIN
    LOOP
        WITH to_update AS (
            SELECT id FROM orders
            WHERE status = 'archived'
            LIMIT batch_size
        )
        UPDATE orders SET status = 'done'
        FROM to_update
        WHERE orders.id = to_update.id;

        GET DIAGNOSTICS affected = ROW_COUNT;
        EXIT WHEN affected = 0;
        COMMIT;
    END LOOP;
END $$;
```

## Common Mistakes

- Setting `statement_timeout` without first ensuring queries have proper indexes
- Using `SET LOCAL` to increase the timeout -- this only works within the current transaction
- Not investigating the actual cause of the slow query and just increasing the timeout
- Running `EXPLAIN ANALYZE` on queries that modify data -- use `EXPLAIN (ANALYZE, BUFFERS)` on a `SELECT` equivalent instead
- Forgetting that `statement_timeout` includes lock wait time, so lock contention can cause timeout even for fast queries

## Related Pages

- [PostgreSQL Lock Timeout](/tools/postgresql/pg-locks-timeout)
- [PostgreSQL Deadlock Detected](/tools/postgresql/pg-deadlock-detected)
- [PostgreSQL OOM](/tools/postgresql/pg-oom)
- [MySQL Lock Timeout](/tools/mysql/mysql-lock-timeout)
