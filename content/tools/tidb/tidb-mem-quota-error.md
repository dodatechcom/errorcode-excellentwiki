---
title: "[Solution] TiDB Memory Quota Error — How to Fix"
description: "Fix TiDB memory quota errors by resolving OOM kills, adjusting session memory limits, and optimizing memory-intensive query plans"
tools: ["tidb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# TiDB Memory Quota Error

TiDB memory quota errors occur when a query or session exceeds the configured memory limit, causing the server to cancel the operation or the entire process to be OOM-killed.

## Why It Happens

- Hash Join or Hash Aggregation consumes too much memory
- Large result set materialized in memory
- Prepared statement cache grows without bound
- Subquery materializes entire result in memory
- Memory quota per session is too low for workload
- TiDB server does not have enough OS memory allocated

## Common Error Messages

```
ERROR: Out Of Memory Quota
```

```
ERROR: MEMORY_EXCEEDED
```

```
ERROR: global memory quota exceeded
```

```
FATAL: out of memory (OOM Killed)
```

## How to Fix It

### 1. Set Memory Quota

```sql
-- Set memory quota per session (in bytes)
SET tidb_mem_quota_query = 1073741824;  -- 1GB

-- Check current quota
SHOW VARIABLES LIKE 'tidb_mem_quota_query';

-- Set global default
SET GLOBAL tidb_mem_quota_query = 2147483648;  -- 2GB
```

### 2. Optimize Memory-Intensive Queries

```sql
-- Use LIMIT to reduce result set
SELECT * FROM orders ORDER BY total DESC LIMIT 100;

-- Replace Hash Join with Index Join
SELECT /*+ USE_INDEX(orders, idx_user_id) */
  o.*, u.name
FROM orders o
JOIN users u ON o.user_id = u.id;

-- Use subquery with aggregation instead of full table scan
SELECT user_id, COUNT(*)
FROM orders
GROUP BY user_id
HAVING COUNT(*) > 10;
```

### 3. Configure Server Memory Limits

```toml
# tidb.toml
[performance]
# Maximum memory TiDB can use (bytes)
max-memory = 0  -- 0 means no limit

[mem-quota]
# Query memory quota
tidb_mem_quota_query = 1073741824

# Action when quota exceeded
action = "cancel"  -- or "fallback"
```

### 4. Monitor and Kill Memory-Heavy Queries

```sql
-- Find queries using most memory
SELECT
  stmt_type,
  digest,
  sum_mem,
  count
FROM mysql.tidb_stmt_summary
WHERE sum_mem > 100000000
ORDER BY sum_mem DESC LIMIT 10;

-- Kill the offending query
KILL <process_id>;
```

## Common Scenarios

- **Query killed with OOM**: Increase `tidb_mem_quota_query` or optimize the query to use less memory.
- **TiDB process killed by OS**: Set `max-memory` in tidb.toml to limit TiDB memory usage.
- **Hash Join uses too much memory**: Add appropriate indexes so TiDB can use Index Join instead.

## Prevent It

- Set appropriate `tidb_mem_quota_query` for the workload
- Avoid SELECT * on large tables
- Use EXPLAIN ANALYZE to check memory estimates before running queries
- Add indexes to reduce hash join memory usage

## Related Pages

- [TiDB OOM Error](/tools/tidb/tidb-oom-error)
- [TiDB Slow Query Error](/tools/tidb/tidb-slow-query-error)
- [TiDB Statement Error](/tools/tidb/tidb-statement-error)
