---
title: "[Solution] TiDB Statistics Error — How to Fix"
description: "Fix TiDB statistics collection errors when the optimizer cannot access accurate table statistics"
tools: ["tidb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# TiDB Statistics Error

Statistics errors occur when TiDB's query optimizer cannot access or use accurate table statistics, leading to suboptimal query execution plans.

## Why It Happens

- Statistics are outdated and need to be refreshed
- Statistics collection failed due to resource constraints
- Table has too many columns for efficient statistics
- Statistics are locked and cannot be updated
- TiKV nodes cannot provide sample data

## Common Error Messages

```
ERROR: statistics not found for table mydb.mytable
```

```
WARN: using pseudo statistics for table mydb.mytable
```

```
error: statistics collection failed: timeout
```

## How to Fix It

### 1. Update Statistics

```sql
-- Full statistics update
ANALYZE TABLE mydb.mytable;

-- Update specific columns
ANALYZE TABLE mydb.mytable COLUMNS user_id, created_at;
```

### 2. Check Statistics Status

```sql
SELECT * FROM mysql.stats_meta WHERE table_id = (SELECT id FROM information_schema.tables WHERE table_name = 'mytable');
SELECT * FROM mysql.stats_histograms WHERE table_id = (SELECT id FROM information_schema.tables WHERE table_name = 'mytable');
```

### 3. Unlock Statistics

```sql
-- Unlock if statistics are locked
ALTER TABLE mydb.mytable SET TIDB_STATS_UNLOAD;
ANALYZE TABLE mydb.mytable;
```

### 4. Auto-Analyze Configuration

```sql
SET GLOBAL tidb_enable_auto_analyze = 'ON';
SET GLOBAL tidb_auto_analyze_ratio = '0.5';
SET GLOBAL tidb_auto_analyze_start_time = '00:00 +0000';
SET GLOBAL tidb_auto_analyze_end_time = '06:00 +0000';
```

## Examples

```
mysql> ANALYZE TABLE mydb.orders;
+-----------+------------+----------+
| Table     | Op         | Msg_type |
+-----------+------------+----------+
| mydb      | orders     | status   |
+-----------+------------+----------+
1 row in set (15.23 sec)
```

## Prevent It

- Enable auto-analyze for regularly updated tables
- Schedule manual ANALYZE during low-traffic periods
- Monitor statistics freshness

## Related Pages

- [TiDB Statistics Error](/tools/tidb/tidb-statistics-error)
- [TiDB Plan Replayer Error](/tools/tidb/tidb-plan-replayer-error)
- [TiDB Optimizer Error](/tools/tidb/tidb-query-error)
