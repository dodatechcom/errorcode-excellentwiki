---
title: "[Solution] CockroachDB Timeout Error — How to Fix"
description: "Fix CockroachDB query execution timeouts by optimizing queries, tuning timeout settings, adding indexes, and reducing transaction contention."
tools: ["cockroachdb"]
error-types: ["timeout-error"]
severities: ["error"]
weight: 5
comments: true
---

A CockroachDB timeout error occurs when a query exceeds the configured execution timeout before completing. Timeouts protect the cluster from runaway queries but can also indicate performance issues that need investigation.

## Why It Happens

Query timeouts in CockroachDB are triggered when the statement execution time exceeds the `statement_timeout` setting. The query is cancelled and resources are released, but the application must handle the error.

- The query performs a full table scan on a large table without an appropriate index
- The query is executing a large JOIN that materializes too many rows
- Transaction contention causes the query to wait for locks held by other transactions
- The cluster is overloaded and cannot process the query within the timeout
- The query returns a large result set that exceeds the client-side timeout
- Statistics are stale, causing the optimizer to choose a poor execution plan
- Network latency between the gateway node and the data nodes adds to execution time
- Background operations (compaction, rebalancing) consume resources needed by the query

## Common Error Messages

```text
ERROR: query execution canceled due to statement timeout
```

The query exceeded the `statement_timeout` setting and was cancelled by the server.

```text
ERROR: query execution canceled; query has been running for 30s
```

The default timeout was exceeded. The query needs to be optimized or the timeout increased.

```text
ERROR: QueryMemoryLimitError: memory limit exceeded
```

Not a timeout per se, but a resource limit that can cause queries to fail similarly. The query used more memory than allowed.

```text
ERROR: transaction timeout: deadline exceeded
```

The transaction as a whole exceeded its deadline. This is different from a statement timeout and cannot be configured per-query.

## How to Fix It

### 1. Increase Statement Timeout

```sql
-- Set timeout for the current session
SET statement_timeout = '60s';

-- Set timeout for a specific query
SET statement_timeout = '5m';
SELECT * FROM large_table WHERE created_at > '2024-01-01';

-- Reset to default (no timeout)
SET statement_timeout = 0;

-- Cluster-wide default
SET CLUSTER SETTING sql.defaults.statement_timeout = '30s';
```

### 2. Add Indexes to Avoid Full Table Scans

```sql
-- Check if the query is doing a full table scan
EXPLAIN (VERBOSE) SELECT * FROM orders WHERE customer_id = 12345;

-- If you see "full table scan", add an index
CREATE INDEX idx_orders_customer_id ON orders (customer_id);

-- For composite queries, create a composite index
CREATE INDEX idx_orders_customer_date ON orders (customer_id, created_at DESC);

-- For queries with WHERE and ORDER BY
CREATE INDEX idx_orders_status_date ON orders (status, created_at)
    WHERE status IN ('pending', 'processing');
```

### 3. Optimize the Query

```sql
-- Bad: SELECT * with no limit
SELECT * FROM orders WHERE customer_id = 12345;

-- Good: Select only needed columns with a limit
SELECT id, status, total FROM orders 
WHERE customer_id = 12345 
ORDER BY created_at DESC 
LIMIT 100;

-- Bad: Large JOIN without filtering
SELECT * FROM orders o
JOIN customers c ON o.customer_id = c.id
JOIN products p ON o.product_id = p.id;

-- Good: Join with specific filters
SELECT o.id, o.total, c.name, p.name AS product_name
FROM orders o
JOIN customers c ON o.customer_id = c.id
JOIN products p ON o.product_id = p.id
WHERE o.created_at > '2024-01-01'
LIMIT 500;
```

### 4. Fix Transaction Contention

```sql
-- Check for contention
SELECT 
    key,
    count(*) as count,
    count(DISTINCT txn_id) as txn_count
FROM crdb_internal.transaction_contention_events
GROUP BY key
ORDER BY count DESC LIMIT 10;

-- Use SELECT FOR UPDATE to reduce contention on hot rows
BEGIN;
SELECT balance FROM accounts WHERE id = 1 FOR UPDATE;
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
COMMIT;
```

### 5. Refresh Table Statistics

```sql
-- Check if statistics are stale
SHOW STATISTICS FOR TABLE orders;

-- Force a statistics refresh
ANALYZE orders;

-- Or for all tables in the database
ANALYZE DATABASE mydb;

-- Check the optimizer's plan after refreshing statistics
EXPLAIN ANALYZE SELECT * FROM orders WHERE customer_id = 12345;
```

### 6. Use Pagination for Large Result Sets

```sql
-- Bad: Fetching all rows at once
SELECT * FROM orders WHERE created_at > '2024-01-01';

-- Good: Cursor-based pagination
SELECT id, status, total FROM orders 
WHERE created_at > '2024-01-01' 
  AND (created_at, id) > ('2024-06-15', 'last-seen-id')
ORDER BY created_at, id 
LIMIT 100;
```

## Common Scenarios

**Timeouts only during peak hours.** The cluster is at capacity. Add nodes to distribute the load, or increase the concurrency limit for the application's connection pool.

**Timeouts after adding a new column.** New columns may not have indexes yet. Check the query plan with `EXPLAIN` and add indexes as needed.

**Timeouts on analytical queries.** OLAP queries scanning large tables are inherently slow. Use CockroachDB's follower reads or scheduled materialized views for analytical workloads.

## Prevent It

- Monitor query latency with `crdb_internal.statement_statistics` and alert on queries exceeding p99 thresholds
- Run `EXPLAIN ANALYZE` on all production queries to identify full table scans and suboptimal plans
- Use automatic statistics collection and refresh statistics before critical batch operations
