---
title: "[Solution] Out of Memory for Query"
description: "Fix 'Out of memory for query' when a query requires more memory than is available."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "sql"
tags: ["sql", "performance, memory"]
severity: "error"
---

# Out of Memory for Query

## Error Message

```
ERROR 1037: Out of memory / Memory allocation failed — The query requires more memory than the server has available or the configured limit allows.
```

## Common Causes

- Query uses too much temporary memory for sorting, hashing, or grouping large result sets
- Too many concurrent connections each consuming significant memory
- The sort_buffer_size or join_buffer_size settings are too large for the available RAM
- Large result sets loaded entirely into memory instead of being streamed

## Solutions

### Solution 1: Optimize queries to use less memory

Rewrite queries to reduce memory consumption during execution.

```sql
-- Wrong: large DISTINCT on many columns
SELECT DISTINCT * FROM large_table;

-- Correct: only distinct on needed columns
SELECT DISTINCT col1, col2 FROM large_table;

-- Wrong: large GROUP BY without index
SELECT col1, col2, COUNT(*) FROM large_table GROUP BY col1, col2;

-- Correct: add index to avoid in-memory sort
CREATE INDEX idx_large_table_group ON large_table(col1, col2);

-- Use LIMIT to reduce result set
SELECT * FROM large_table ORDER BY created_at DESC LIMIT 100;
```

### Solution 2: Adjust memory configuration settings

Tune database memory settings to match available hardware resources.

```sql
-- MySQL: check and adjust memory settings
SHOW VARIABLES LIKE 'sort_buffer_size';
SHOW VARIABLES LIKE 'join_buffer_size';
SHOW VARIABLES LIKE 'tmp_table_size';
SHOW VARIABLES LIKE 'max_heap_table_size';

-- Reduce buffer sizes if memory is limited
SET SESSION sort_buffer_size = 256 * 1024; -- 256KB
SET SESSION join_buffer_size = 256 * 1024;
SET SESSION tmp_table_size = 64 * 1024 * 1024; -- 64MB

-- PostgreSQL: adjust work memory
SHOW work_mem;
SET work_mem = '256MB'; -- increase for complex queries

-- SQL Server: check memory usage
SELECT * FROM sys.dm_os_memory_clerks ORDER BY pages_kb DESC;
```

### Solution 3: Use pagination to process data in chunks

Instead of loading all results into memory, process them in batches.

```sql
-- Wrong: load all results at once
SELECT * FROM orders ORDER BY created_at;

-- Correct: use pagination (MySQL/PostgreSQL)
SELECT * FROM orders
ORDER BY created_at
LIMIT 1000 OFFSET 0;

-- Next page
SELECT * FROM orders
ORDER BY created_at
LIMIT 1000 OFFSET 1000;

-- SQL Server: use OFFSET FETCH
SELECT * FROM orders
ORDER BY created_at
OFFSET 0 ROWS FETCH NEXT 1000 ROWS ONLY;

-- Use cursor for processing large datasets
DECLARE order_cursor CURSOR FOR SELECT id FROM orders;
OPEN order_cursor;
FETCH NEXT FROM order_cursor INTO @id;
-- process each row
CLOSE order_cursor;
DEALLOCATE order_cursor;
```

## Prevention Tips

- Monitor memory usage with SHOW STATUS (MySQL) or pg_stat_activity (PostgreSQL) to identify memory-hungry queries
- Use EXPLAIN to check if queries use disk-based temporary tables instead of in-memory ones
- Set appropriate work_mem or sort_buffer_size values based on available RAM and concurrent connection count

## Related Errors

- [Slow Query]({{< relref "/languages/sql/slow-query.md" >}})
- [Timeout Error]({{< relref "/languages/sql/timeout-error.md" >}})
- [Connection Pool Error]({{< relref "/languages/sql/connection-pool-error.md" >}})
