---
title: "[Solution] CockroachDB Statement Error - Fix Statement Timeout or Canceled"
description: "Fix CockroachDB statement timeout and cancellation errors. Resolve query timeouts, statement limits, and cancellation issues."
tools: ["cockroachdb"]
error-types: ["statement-error"]
severities: ["error"]
weight: 5
---

This error means a CockroachDB statement was canceled due to a timeout or resource limit. Long-running queries are terminated to prevent resource exhaustion.

## What This Error Means

When a statement times out or is canceled, you see:

```
statement_timeout: canceling statement due to user request
# or
query canceled: executed too long
# or
SQLSTATE 57014: canceling statement due to statement timeout
```

CockroachDB enforces statement timeouts to protect cluster stability. Queries that exceed the configured limit are automatically terminated.

## Why It Happens

- The query is too complex and runs longer than the timeout
- Missing indexes cause full table scans on large tables
- Lock contention from concurrent transactions
- The cluster is overloaded and cannot process queries quickly
- The statement timeout is set too low
- Network latency between the application and CockroachDB

## How to Fix It

### Increase the statement timeout

```sql
SET statement_timeout = '30s';
-- or for longer queries
SET statement_timeout = '300s';
```

### Check current timeout settings

```sql
SHOW statement_timeout;
SHOW idle_in_transaction_session_timeout;
SHOW locks_timeout;
SHOW query_timeout;
```

### Add indexes for slow queries

```sql
CREATE INDEX idx_orders_customer ON orders (customer_id);
```

### Analyze the query plan

```sql
EXPLAIN ANALYZE SELECT * FROM orders WHERE customer_id = 123;
```

Identify bottlenecks in the query execution.

### Use statement_timeout per session

```sql
SET SESSION statement_timeout = '60s';
```

Per-session settings allow different timeouts for different workloads.

### Monitor long-running queries

```sql
SELECT * FROM [SHOW CLUSTER SESSIONS]
  WHERE status = 'ACTIVE'
  AND now() - active_start > interval '30 seconds';
```

### Cancel stuck statements manually

```sql
CANCEL QUERY (SELECT query_id FROM [SHOW QUERIES] WHERE query LIKE '%slow query%');
```

### Optimize the query

```sql
-- Add LIMIT for large result sets
SELECT * FROM orders WHERE customer_id = 123 LIMIT 100;
```

### Use prepared statements for repeated queries

```go
// Go example
stmt, _ := db.Prepare("SELECT * FROM orders WHERE customer_id = $1")
```

Prepared statements are parsed once and reused.

### Check for lock contention

```sql
SELECT * FROM [SHOW CLUSTER SESSIONS] WHERE wait_type = 'LOCK';
```

Lock contention can cause queries to wait indefinitely.

## Common Mistakes

- Not setting statement timeouts, allowing runaway queries
- Not adding indexes for WHERE clauses on large tables
- Using SELECT * instead of selecting specific columns
- Not using EXPLAIN to understand query performance
- Setting timeouts too low for legitimate analytical queries

## Related Pages

- [CockroachDB Timeout]({{< relref "/tools/cockroachdb/cockroach-timeout" >}}) -- general timeouts
- [CockroachDB Serializable Error]({{< relref "/tools/cockroachdb/cockroach-serializable-error" >}}) -- transaction isolation
- [CockroachDB Node Unavailable]({{< relref "/tools/cockroachdb/cockroach-node-unavailable" >}}) -- node issues
