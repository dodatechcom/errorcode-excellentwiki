---
title: "[Solution] TiDB Statistics Error — How to Fix"
description: "Fix TiDB statistics errors by resolving ANALYZE TABLE failures, fixing histogram issues, and handling statistics collection problems"
tools: ["tidb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# TiDB Statistics Error

TiDB statistics errors occur when collecting, maintaining, or using table statistics for query optimization. Statistics are critical for the query optimizer.

## Why It Happens

- ANALYZE TABLE fails due to lock contention
- Statistics are stale or outdated
- Histogram data is corrupted
- Statistics collection uses too much memory
- Auto-analyze is not working
- Statistics for partitioned tables are incorrect

## Common Error Messages

```
ERROR: analyze table failed
```

```
ERROR: statistics collection timeout
```

```
WARNING: statistics are outdated
```

```
ERROR: histogram build failed
```

## How to Fix It

### 1. Collect Statistics

```sql
-- Manual statistics collection
ANALYZE TABLE users;

-- Analyze specific columns
ANALYZE TABLE users COLUMNS name, email;

-- Analyze index statistics
ANALYZE TABLE users INDEX idx_name;
```

### 2. Fix Stale Statistics

```sql
-- Check statistics status
SHOW STATS_META WHERE table_name = 'users';

-- Check histogram status
SHOW STATS_HISTOGRAMS WHERE table_name = 'users';

-- Force statistics refresh
ANALYZE TABLE users;
```

### 3. Configure Auto-Statistics

```toml
# In tidb.toml
[performance]
enable-auto-analyze = true
auto-analyze-ratio = 0.5  # Analyze when 50% of data changes
auto-analyze-start = "00:00 +0000"
auto-analyze-end = "06:00 +0000"
```

### 4. Monitor Statistics

```sql
-- Check table statistics
SHOW STATS_META WHERE table_name = 'users';

-- Check index statistics
SHOW STATS_HISTOGRAMS WHERE table_name = 'users' AND is_index = 1;

-- Check column statistics
SHOW STATS_HISTOGRAMS WHERE table_name = 'users' AND is_index = 0;
```

## Common Scenarios

- **Query plan changes unexpectedly**: Check if statistics are stale and refresh.
- **ANALYZE TABLE is slow**: Run during off-peak hours or analyze specific columns.
- **Auto-analyze not running**: Check tidb.toml configuration and time window.

## Prevent It

- Enable auto-analyze for production databases
- Monitor statistics freshness
- Schedule ANALYZE TABLE during maintenance windows

## Related Pages

- [TiDB Slow Query Error](/tools/tidb/tidb-slow-query-error)
- [TiDB Query Error](/tools/tidb/tidb-query-error)
- [TiDB Plan Replayer Error](/tools/tidb/tidb-plan-replayer-error)
