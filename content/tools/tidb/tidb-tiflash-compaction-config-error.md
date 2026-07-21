---
title: "[Solution] TiDB TiFlash Compaction Error — How to Fix"
description: "Fix TiDB TiFlash compaction errors when the columnar storage engine fails to compact DeltaStore or Stable data"
tools: ["tidb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# TiDB TiFlash Compaction Error

TiFlash compaction errors occur when the DeltaMerge storage engine in TiFlash fails to merge DeltaStore data into Stable storage, causing read performance degradation.

## Why It Happens

- DeltaStore is too large relative to Stable storage
- Disk I/O is too slow for compaction operations
- Memory is insufficient for compaction process
- Compaction conflicts with ongoing reads
- TiFlash node is overloaded

## Common Error Messages

```
TiFlash: DeltaStore compaction failed
```

```
error: DeltaMerge: unable to merge DeltaStore into Stable
```

```
TiFlash: compaction is lagging behind ingestion rate
```

## How to Fix It

### 1. Check TiFlash Compaction Status

```bash
curl -s http://tiflash:9090/metrics | grep tiflash_storage
```

### 2. Force Compaction

```sql
-- Force compaction on a table
ALTER TABLE mydb.mytable COMPACT;
```

### 3. Increase Compaction Threads

```toml
# In tiflash.toml
[storage]
background_pool_size = 16
```

### 4. Monitor DeltaStore Size

```bash
curl -s http://tiflash:9090/metrics | grep tiflash_storage_delta_rows
```

## Examples

```
$ curl -s http://tiflash:9090/metrics | grep delta
tiflash_storage_delta_rows 500000
tiflash_storage_total_rows 5000000
```

## Prevent It

- Monitor DeltaStore to Stable row ratio
- Ensure sufficient I/O and memory for compaction
- Schedule heavy DML operations during low-traffic periods

## Related Pages

- [TiDB TiFlash Compaction Error](/tools/tidb/tidb-tiflash-compaction-error)
- [TiDB TiFlash Error](/tools/tidb/tidb-tiflash-error)
- [TiDB TiFlash Disk Error](/tools/tidb/tidb-tiflash-disk-error)
