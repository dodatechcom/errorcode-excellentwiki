---
title: "[Solution] ClickHouse Async Insert Error — How to Fix"
description: "Fix ClickHouse async insert errors including buffer overflow, flush failures, and async insert configuration issues"
tools: ["clickhouse"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# ClickHouse Async Insert Error

Async insert errors in ClickHouse occur when the async insert mechanism fails to batch and flush data correctly. ClickHouse buffers inserts and flushes them in batches for better performance.

## Why It Happens

- The async insert buffer is full and cannot accept more data
- The flush interval is too long, causing memory pressure
- The `async_insert_max_data_size` is exceeded
- Too many pending async inserts overwhelm the buffer
- The async insert mechanism encounters a schema change
- The client disconnects before the flush completes

## Common Error Messages

```
Code: 271. DB::Exception: Async insert buffer is full
```

```
Code: 241. DB::Exception: Memory limit exceeded while processing async inserts
```

```
Code: 225. DB::Exception: Failed to flush async inserts
```

```
Code: 107. DB::Exception: Too many parts after async insert flush
```

## How to Fix It

### 1. Increase Async Insert Buffer Size

```sql
-- Check current settings
SELECT name, value FROM system.settings
WHERE name LIKE '%async_insert%';

-- Increase buffer size
SET async_insert_max_data_size = 104857600;  -- 100MB
SET async_insert_busy_timeout_ms = 200;  -- flush after 200ms
```

### 2. Fix Flush Configuration

```xml
<!-- In config.xml -->
<async_insert>1</async_insert>
<wait_for_async_insert>1</wait_for_async_insert>
<async_insert_max_data_size>104857600</async_insert_max_data_size>
<async_insert_busy_timeout_ms>200</async_insert_busy_timeout_ms>
```

### 3. Monitor Async Insert Health

```sql
-- Check async insert status
SELECT * FROM system.asynchronous_inserts;

-- Check pending inserts
SELECT * FROM system.parts WHERE active = 1
ORDER BY modification_time DESC LIMIT 5;
```

### 4. Disable Async Insert If Needed

```sql
-- Disable async insert for specific connection
SET async_insert = 0;

-- Or for specific table
ALTER TABLE mydb.events MODIFY SETTING async_insert = 0;
```

## Common Scenarios

- **High write rate overwhelms async insert**: Increase buffer size or flush interval.
- **Memory pressure from large buffers**: Reduce `async_insert_max_data_size`.
- **Client timeout during flush**: Set `wait_for_async_insert = 0` for fire-and-forget inserts.

## Prevent It

- Monitor async insert buffer usage and flush rates
- Tune `async_insert_max_data_size` based on available memory
- Use `wait_for_async_insert = 0` for non-critical data where durability is less important

## Related Pages

- [ClickHouse Table Error](/tools/clickhouse/clickhouse-table-error)
- [ClickHouse Memory Error](/tools/clickhouse/clickhouse-memory-error)
- [ClickHouse Merge Error](/tools/clickhouse/clickhouse-merge-error)
