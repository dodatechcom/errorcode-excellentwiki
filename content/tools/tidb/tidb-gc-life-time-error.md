---
title: "[Solution] TiDB GC Life Time Error — How to Fix"
description: "Fix TiDB garbage collection lifetime errors when GC cannot proceed or causes data inconsistency"
tools: ["tidb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# TiDB GC Life Time Error

GC life time errors occur when TiDB's garbage collection process fails to clean up old data versions, potentially causing storage bloat and performance degradation.

## Why It Happens

- GC safe point is stuck due to long-running transactions
- TiKV nodes cannot process GC tasks
- GC life time is set too short, causing data loss
- GC life time is too long, causing excessive storage usage
- GC worker threads are exhausted

## Common Error Messages

```
GC failed: GC life time is less than GC safe point
```

```
error: GC cannot proceed, safe point is stuck
```

```
GC: unable to clean up old versions
```

## How to Fix It

### 1. Check GC Status

```sql
SELECT * FROM mysql.tidb WHERE variable_name = 'tikv_gc_safe_point';
SHOW CONFIG WHERE Variable_name = 'tidb_gc_life_time';
```

### 2. Adjust GC Life Time

```sql
-- Set GC life time to 10 minutes
SET GLOBAL tidb_gc_life_time = '10m0s';

-- Set to 10 minutes
UPDATE mysql.tidb SET VARIABLE_VALUE = '10m0s' WHERE VARIABLE_NAME = 'tidb_gc_life_time';
```

### 3. Kill Long-Running Transactions

```sql
-- Find long-running transactions
SELECT * FROM information_schema.tidb_trx WHERE now() - start_time > INTERVAL 10 MINUTE;
KILL <session_id>;
```

### 4. Trigger Manual GC

```sql
-- Trigger garbage collection manually
ADMIN CHECK TABLE mydb.mytable;
```

## Examples

```
$ SELECT * FROM mysql.tidb WHERE variable_name = 'tikv_gc_safe_point';
+---------------------+---------------------+
| VARIABLE_NAME       | VARIABLE_VALUE      |
+---------------------+---------------------+
| tikv_gc_safe_point  | 2024-01-15 10:00:00 |
+---------------------+---------------------+
```

## Prevent It

- Monitor GC safe point advancement
- Kill long-running transactions regularly
- Set appropriate GC life time based on backup requirements

## Related Pages

- [TiDB GC Error](/tools/tidb/tidb-gc-error)
- [TiDB GC Error Code](/tools/tidb/tidb-gc-error-code)
- [TiDB Transaction Error](/tools/tidb/tidb-transaction-error)
