---
title: "[Solution] TiDB GC Error — How to Fix"
description: "Fix TiDB GC errors by resolving garbage collection failures, fixing GC lifetime issues, and handling MVCC data cleanup problems"
tools: ["tidb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# TiDB GC Error

TiDB GC (Garbage Collection) errors occur when the MVCC garbage collection process fails. GC removes old data versions that are no longer needed.

## Why It Happens

- GC lifetime is too short causing data loss
- GC lifetime is too long causing storage bloat
- GC cannot clean up locked keys
- GC is blocked by long-running transactions
- GC worker encounters I/O errors
- GC safe point is not advancing

## Common Error Messages

```
ERROR: GC life time is too short
```

```
WARNING: GC blocked by long transaction
```

```
ERROR: GC worker failed
```

```
ERROR: GC safe point not advancing
```

## How to Fix It

### 1. Check GC Status

```sql
-- Check GC status
SELECT * FROM mysql.tidb WHERE variable_name LIKE 'gc%';

-- Check GC lifetime
SHOW VARIABLES LIKE 'tidb_gc_life_time';

-- Check GC safe point
SELECT * FROM mysql.tidb WHERE variable_name = 'tikv_gc_safe_point';
```

### 2. Configure GC Lifetime

```sql
-- Set GC lifetime (default 10m)
SET GLOBAL tidb_gc_life_time = '10m';

-- Increase for backup operations
SET GLOBAL tidb_gc_life_time = '24h';

-- Check current setting
SELECT @@tidb_gc_life_time;
```

### 3. Fix GC Blocked by Long Transactions

```sql
-- Check for long-running transactions
SELECT * FROM information_schema.tikv_locks WHERE lock_type != 'READ';

-- Kill long-running transaction if needed
KILL <session_id>;
```

### 4. Monitor GC

```sql
-- Check GC status
SELECT * FROM mysql.tidb WHERE variable_name LIKE 'gc%';

-- Monitor TiKV GC metrics
curl http://tikv1:20180/metrics | grep gc

-- Check storage size
SELECT table_name, 
  ROUND(data_length/1024/1024, 2) AS data_mb,
  ROUND(index_length/1024/1024, 2) AS index_mb
FROM information_schema.tables
WHERE table_schema = 'mydb';
```

## Common Scenarios

- **Storage grows too fast**: Decrease GC lifetime to clean up faster.
- **GC blocked by transaction**: Kill long-running transactions.
- **GC lifetime too short**: Increase to prevent data loss during backups.

## Prevent It

- Monitor GC safe point advancement
- Keep GC lifetime appropriate for workload
- Kill long-running transactions that block GC

## Related Pages

- [TiDB Region Error](/tools/tidb/tidb-region-error)
- [TiDB TiKV Error](/tools/tidb/tidb-tikv-error)
- [TiDB Config Error](/tools/tidb/tidb-gflag-error)
