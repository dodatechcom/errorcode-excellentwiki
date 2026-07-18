---
title: "[Solution] ClickHouse Memory Error — How to Fix"
description: "Fix ClickHouse memory limit exceeded errors by tuning query memory settings, configuring max_memory_usage, and optimizing large query execution"
tools: ["clickhouse"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# ClickHouse Memory Error

Memory errors in ClickHouse occur when queries exceed the allocated memory limit. ClickHouse is designed for analytical queries on large datasets, and memory management is critical for stability.

## Why It Happens

- A query processes more data than `max_memory_usage` allows
- Multiple concurrent queries exhaust available RAM
- GROUP BY with high cardinality uses excessive memory
- JOIN operations materialize large right-hand tables
- The `max_bytes_before_external_sort` threshold is too high
- No swap space is configured on the server

## Common Error Messages

```
Code: 241. DB::Exception: Memory limit (for query) exceeded: would use 10.00 GiB
```

```
Code: 241. DB::Exception: Memory limit (total) exceeded
```

```
Code: 241. DB::Exception: Failed to allocate memory for query processing
```

```
Code: 177. DB::Exception: Received from localhost:9000
```

## How to Fix It

### 1. Increase Memory Limit for Specific Query

```sql
-- Set higher memory limit for a specific query
SET max_memory_usage = 20000000000;  -- 20GB
SELECT count() FROM large_table GROUP BY high_cardinality_column;
```

### 2. Configure System-Wide Memory Settings

```xml
<!-- In config.xml -->
<max_server_memory_usage_to_ram_ratio>0.8</max_server_memory_usage_to_ram_ratio>
<max_memory_usage>10000000000</max_memory_usage>
```

```sql
-- Check current settings
SELECT name, value, changed FROM system.settings
WHERE name LIKE '%memory%';
```

### 3. Enable External Sorting and Grouping

```sql
-- Enable external sorting when memory is insufficient
SET max_bytes_before_external_sort = 10000000000;  -- 10GB
SET max_bytes_before_external_group_by = 10000000000;  -- 10GB

-- This allows ClickHouse to spill to disk when memory is low
```

### 4. Optimize Memory-Heavy Queries

```sql
-- BAD: GROUP BY with millions of unique keys
SELECT user_id, count() FROM events GROUP BY user_id;

-- GOOD: use approximate aggregation
SELECT uniqCombined(user_id) FROM events;

-- Or use sampling
SELECT user_id, count() FROM events SAMPLE 0.1 GROUP BY user_id;
```

### 5. Monitor Memory Usage

```sql
-- Check current memory usage per query
SELECT query, memory_usage, peak_memory_usage
FROM system.processes
ORDER BY memory_usage DESC;

-- Check server memory settings
SELECT name, value FROM system.settings
WHERE name IN ('max_memory_usage', 'max_server_memory_usage_to_ram_ratio');
```

## Common Scenarios

- **Dashboard query OOMs**: A dashboard runs a GROUP BY on millions of unique keys. Use sampling or approximate functions.
- **Concurrent query memory exhaustion**: Multiple queries run simultaneously. Reduce `max_memory_usage` per query.
- **JOIN materializes large table**: Use `partial_merge` JOIN algorithm for large right tables.

## Prevent It

- Set `max_memory_usage` per query based on available RAM divided by expected concurrency
- Use `max_bytes_before_external_group_by` for queries with high-cardinality GROUP BY
- Monitor `system.processes` for memory usage patterns

## Related Pages

- [ClickHouse Query Error](/tools/clickhouse/clickhouse-query-error)
- [ClickHouse Function Error](/tools/clickhouse/clickhouse-function-error)
- [ClickHouse Join Error](/tools/clickhouse/clickhouse-join-error)
