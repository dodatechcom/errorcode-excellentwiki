---
title: "[Solution] ClickHouse Merge Error — How to Fix"
description: "Fix ClickHouse merge errors including background merge failures, too many parts, merge tree configuration issues, and part movement problems"
tools: ["clickhouse"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# ClickHouse Merge Error

Merge errors in ClickHouse occur when the background merge process cannot combine data parts. This includes too many parts, merge conflicts, disk space issues, and configuration problems.

## Why It Happens

- Data is inserted too frequently creating many small parts
- The `max_parts_per_partition` limit is exceeded
- Disk space is insufficient for merge operations
- ZooKeeper is unavailable for replicated table merges
- The merge process encounters corrupt data in a part
- Concurrent merges exceed `number_of_free_entries_in_pool_to_execute_mutation`

## Common Error Messages

```
Code: 252. DB::Exception: Too many parts (300). Merge process cannot keep up
```

```
Code: 396. DB::Exception: Could not calculate expression: Status: 502
```

```
DB::Exception: Part all_0_0_0 already exists, won't add
```

```
Code: 241. DB::Exception: Memory limit exceeded
```

## How to Fix It

### 1. Force Manual Merge

```sql
-- Check parts count
SELECT database, table, count() AS parts
FROM system.parts WHERE active = 1
GROUP BY database, table ORDER BY parts DESC;

-- Force merge on specific table
OPTIMIZE TABLE mydb.events FINAL;

-- Schedule periodic merges
-- In cron: clickhouse-client --query "OPTIMIZE TABLE mydb.events"
```

### 2. Adjust Merge Tree Configuration

```xml
<!-- In config.xml under <merge_tree> -->
<max_parts_per_partition>300</max_parts_per_partition>
<parts_to_delay_insert>300</parts_to_delay_insert>
<parts_to_throw_insert>600</parts_to_throw_insert>
<max_delay_to_insert>2</max_delay_to_insert>
```

### 3. Fix Disk Space Issues

```bash
# Check disk usage
df -h /var/lib/clickhouse

# Find largest tables
SELECT database, table,
  formatReadableSize(sum(bytes_on_disk)) AS size
FROM system.parts WHERE active = 1
GROUP BY database, table ORDER BY sum(bytes_on_disk) DESC;

# Remove old parts or move data to another disk
ALTER TABLE mydb.events DELETE WHERE event_time < now() - INTERVAL 90 DAY;
```

### 4. Configure Background Merge Threads

```xml
<background_pool_size>32</background_pool_size>
<background_merges_mutations_concurrency_ratio>2</background_merges_mutations_concurrency_ratio>
```

## Common Scenarios

- **High insert rate creates too many parts**: Batch inserts every 1-5 seconds instead of per-row.
- **Merge falls behind after disk fill**: Free space, then force merge with `OPTIMIZE TABLE`.
- **Replicated table merge fails**: Ensure ZooKeeper is healthy before merge operations.

## Prevent It

- Batch inserts to reduce parts creation rate (every 1-5 seconds, 1000+ rows)
- Monitor parts count per table and alert at 200+ parts
- Use `max_delay_to_insert` to throttle inserts when parts count is high

## Related Pages

- [ClickHouse Table Error](/tools/clickhouse/clickhouse-table-error)
- [ClickHouse Partition Error](/tools/clickhouse/clickhouse-partition-error)
- [ClickHouse Replication Error](/tools/clickhouse/clickhouse-replication-error)
