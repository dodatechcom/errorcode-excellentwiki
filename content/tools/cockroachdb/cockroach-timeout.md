---
title: "[Solution] CockroachDB Gateway Timeout - Fix SQL Query Timeouts"
description: "Fix CockroachDB gateway timeout errors by optimizing slow queries with EXPLAIN ANALYZE, adding proper indexes on columns, and increasing statement timeout setti"
tools: ["cockroachdb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
---

A CockroachDB gateway timeout occurs when a SQL query takes longer than the configured timeout limit and is cancelled by the server. The error message is `gateway timeout` or `query execution canceled due to statement timeout`.

## What This Error Means

CockroachDB enforces statement and transaction timeouts to prevent long-running queries from consuming resources. When a query exceeds the `statement_timeout` or `transaction_timeout`, the server cancels the execution and returns an error to the client.

The timeout includes planning, execution, and any retries. A gateway timeout is different from a network timeout because the connection remains open, but the query is aborted.

## Why It Happens

- Full table scans on large tables without proper indexes
- Query planner choosing an inefficient execution plan
- High contention causing transactions to wait for locks
- Large batch operations without pagination
- The default `statement_timeout` is too low for complex queries
- Network latency between the application and the CockroachDB cluster
- Queries with unbounded `SELECT` returning millions of rows

## How to Fix It

### 1. Increase the Statement Timeout

```sql
-- For the current session
SET statement_timeout = '30s';

-- For all sessions
ALTER ROLE root SET statement_timeout = '30s';
```

### 2. Add Proper Indexes

```sql
-- Check if the query is doing a full table scan
EXPLAIN ANALYZE SELECT * FROM orders WHERE customer_id = 123;

-- Add an index if missing
CREATE INDEX idx_orders_customer ON orders (customer_id);
```

### 3. Use EXPLAIN to Optimize

```sql
EXPLAIN (VERBOSE, ANALYZE)
SELECT o.id, c.name
FROM orders o
JOIN customers c ON o.customer_id = c.id
WHERE o.created_at > '2024-01-01';
```

### 4. Paginate Large Results

```sql
-- Instead of fetching all rows
SELECT * FROM orders WHERE status = 'pending'
ORDER BY id
LIMIT 100 OFFSET 0;
```

### 5. Use Follower Reads for Analytics

```sql
-- Read from a follower to avoid impacting the gateway
SELECT count(*) FROM orders AS OF SYSTEM TIME follower_read_timestamp();
```

### 6. Monitor Slow Queries

```sql
-- Check the statement diagnostics
SELECT * FROM crdb_internal.statement_diagnostics_requests
WHERE NOT completed;

-- Check active queries
SHOW QUERIES;
```

## Common Mistakes

- Leaving the default `statement_timeout` at 0 (unlimited) in production and only discovering slow queries after user complaints
- Not running `EXPLAIN ANALYZE` before deploying new queries to production
- Using `OFFSET` pagination on large tables (it scans all previous rows)
- Not setting a transaction timeout when using long-running transactions

## Related Pages

- [CockroachDB Deadlock](/tools/cockroachdb/cockroach-deadlock)
- [CockroachDB Serializable Error](/tools/cockroachdb/cockroach-serializable-error)
- [CockroachDB Node Unavailable](/tools/cockroachdb/cockroach-node-unavailable)
