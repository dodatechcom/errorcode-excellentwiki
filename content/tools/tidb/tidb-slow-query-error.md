---
title: "[Solution] TiDB Slow Query Error — How to Fix"
description: "Fix TiDB slow query errors by analyzing slow query logs, optimizing query performance, and resolving timeout issues"
tools: ["tidb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# TiDB Slow Query Error

TiDB slow query errors occur when queries exceed the slow query threshold. TiDB automatically logs slow queries for performance analysis.

## Why It Happens

- Query execution time exceeds slow_log_threshold
- Query scans too many rows
- Query uses inefficient execution plan
- Query lacks appropriate indexes
- Query has large result set
- Query involves expensive operations (sort, hash join)

## Common Error Messages

```
WARNING: slow query detected
```

```
ERROR: query timeout
```

```
ERROR: transaction duration exceeded
```

```
WARNING: coprocessor request exceeded
```

## How to Fix It

### 1. Enable Slow Query Log

```toml
# In tidb.toml
[log]
slow-threshold = 300  # 300ms threshold
query-log-max-len = 2048
```

### 2. Analyze Slow Queries

```sql
-- Check slow queries
SELECT * FROM information_schema.slow_query
ORDER BY query_time DESC
LIMIT 10;

-- Analyze specific slow query
SELECT query, query_time, process_time, total_keys
FROM information_schema.slow_query
WHERE query LIKE '%users%'
ORDER BY query_time DESC;
```

### 3. Optimize Slow Queries

```sql
-- Use EXPLAIN to analyze
EXPLAIN ANALYZE SELECT * FROM users WHERE name = 'Alice';

-- Add appropriate index
CREATE INDEX idx_users_name ON users (name);

-- Use covering index
CREATE INDEX idx_users_name_email ON users (name, email);
```

### 4. Monitor Slow Queries

```sql
-- Check slow query count
SELECT COUNT(*) FROM information_schema.slow_query
WHERE start_time > DATE_SUB(NOW(), INTERVAL 1 HOUR);

-- Check slow query trends
SELECT DATE(start_time), COUNT(*)
FROM information_schema.slow_query
GROUP BY DATE(start_time);
```

## Common Scenarios

- **Dashboard shows slow queries**: Add indexes for frequently queried columns.
- **Query times out**: Increase tidb_mem_quota_query or add indexes.
- **Slow query log too verbose**: Adjust slow-threshold in tidb.toml.

## Prevent It

- Monitor slow query log regularly
- Add indexes for frequently queried columns
- Use EXPLAIN ANALYZE to verify query plans

## Related Pages

- [TiDB Query Error](/tools/tidb/tidb-query-error)
- [TiDB Plan Replayer Error](/tools/tidb/tidb-plan-replayer-error)
- [TiDB Statistics Error](/tools/tidb/tidb-statistics-error)
