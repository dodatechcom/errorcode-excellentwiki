---
title: "[Solution] TiDB Stale Read Error — How to Fix"
description: "Fix TiDB stale read errors when reading data from a specific timestamp fails or returns incorrect results"
tools: ["tidb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# TiDB Stale Read Error

Stale read errors occur when TiDB cannot read data from a specified historical timestamp, often due to GC cleanup or timestamp unavailability.

## Why It Happens

- Requested timestamp has been garbage collected
- GC safe point has advanced past the requested timestamp
- TiKV nodes do not have the required historical data
- Timestamp is invalid or out of range
- Stale read is not enabled for the table

## Common Error Messages

```
ERROR 9006: GC life time is shorter than transaction duration
```

```
ERROR 1105: invalid timestamp for stale read
```

```
error: stale read failed, data not available at requested timestamp
```

## How to Fix It

### 1. Enable Stale Read

```sql
SET tidb_read_staleness = '-5m';
SELECT * FROM mytable AS OF TIMESTAMP NOW() - INTERVAL 5 MINUTE;
```

### 2. Extend GC Life Time

```sql
SET GLOBAL tidb_gc_life_time = '30m';
```

### 3. Use Correct Syntax

```sql
-- Read data from 5 minutes ago
SELECT * FROM mytable AS OF TIMESTAMP NOW() - INTERVAL 5 MINUTE;

-- Read data at specific time
SELECT * FROM mytable AS OF TIMESTAMP '2024-01-15 10:00:00';
```

### 4. Check GC Configuration

```sql
SHOW VARIABLES LIKE 'tidb_gc_life_time';
SELECT * FROM mysql.tidb WHERE VARIABLE_NAME = 'tikv_gc_safe_point';
```

## Examples

```
mysql> SELECT * FROM orders AS OF TIMESTAMP NOW() - INTERVAL 1 HOUR LIMIT 10;
+----+-----------+-----------+
| id | user_id   | amount    |
+----+-----------+-----------+
| 1  | 1001      | 59.99     |
+----+-----------+-----------+
```

## Prevent It

- Set GC life time long enough for historical reads
- Use AS OF TIMESTAMP for specific time reads
- Monitor GC safe point advancement

## Related Pages

- [TiDB Stale Read Error](/tools/tidb/tidb-stale-read-error)
- [TiDB GC Error](/tools/tidb/tidb-gc-error)
- [TiDB Transaction Error](/tools/tidb/tidb-transaction-error)
