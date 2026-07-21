---
title: "[Solution] TiDB Stats Error — How to Fix"
description: "Fix TiDB stats errors by resolving stale statistics, fixing ANALYZE failures, and correcting histogram issues in the query optimizer"
tools: ["tidb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# TiDB Stats Error

TiDB stats errors occur when table or index statistics become stale, corrupt, or fail to update, leading to suboptimal query plans or ANALYZE failures.

## Why It Happens

- Statistics have not been refreshed after bulk data changes
- ANALYZE TABLE fails due to insufficient memory
- Histogram data becomes corrupted after node crash
- Auto-analyze job cannot keep up with write rate
- Statistics collection timeout on very large tables
- Column statistics contain out-of-range values

## Common Error Messages

```
ERROR: statistics is not initialized
```

```
ERROR: ANALYZE table timeout
```

```
ERROR: table stats is corrupted
```

```
ERROR: invalid histogram version
```

## How to Fix It

### 1. Manually Update Statistics

```sql
-- Analyze the full table
ANALYZE TABLE my_table;

-- Analyze specific columns
ANALYZE TABLE my_table COLUMNS id, name, total;

-- Analyze with increased timeout
SET tidb_analyze_version = 2;
ANALYZE TABLE my_table WITH 256 BUCKETS;

-- Check statistics status
SHOW STATS_META WHERE table_name = 'my_table';
```

### 2. Fix Auto-Analyze Configuration

```sql
-- Enable auto-analyze
SET GLOBAL tidb_enable_auto_analyze = ON;

-- Set auto-analyze time window
SET GLOBAL tidb_auto_analyze_start_time = '00:00 +0000';
SET GLOBAL tidb_auto_analyze_end_time = '06:00 +0000';

-- Set threshold for auto-analyze trigger
SET GLOBAL tidb_auto_analyze_ratio = 0.1;

-- Check auto-analyze status
SHOW VARIABLES LIKE 'tidb_enable_auto_analyze';
```

### 3. Recover Corrupted Statistics

```sql
-- Drop and rebuild statistics
DROP STATS my_table;

-- Re-analyze after dropping
ANALYZE TABLE my_table;

-- Check for corrupted stats
SELECT table_name, modify_count, version
FROM mysql.stats_meta
WHERE table_name = 'my_table';
```

### 4. Monitor Statistics Health

```sql
-- Check last analyze time
SELECT
  table_name,
  update_time,
  modify_count
FROM information_schema.tables t1
JOIN mysql.stats_meta t2 ON t1.TABLE_NAME = t2.table_name
WHERE t1.TABLE_SCHEMA = 'mydb';

-- List tables with stale stats
SELECT * FROM mysql.stats_meta
WHERE modify_count > 10000
ORDER BY modify_count DESC;
```

## Common Scenarios

- **Queries slow after data load**: Run ANALYZE TABLE to update statistics.
- **ANALYZE fails with timeout**: Analyze in smaller batches using COLUMNS option.
- **Query plan changes unexpectedly**: Check if statistics were recently updated.

## Prevent It

- Enable auto-analyze for all production databases
- Schedule manual ANALYZE after bulk data operations
- Monitor statistics freshness with the tidb dashboard

## Related Pages

- [TiDB Statistics Refresh Error](/tools/tidb/tidb-statistics-refresh-error)
- [TiDB Slow Query Error](/tools/tidb/tidb-slow-query-error)
- [TiDB Plan Replayer Error](/tools/tidb/tidb-plan-replayer-error)
