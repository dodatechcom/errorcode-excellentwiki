---
title: "[Solution] TiDB OOM Error — How to Fix"
description: "Fix TiDB OOM errors by tuning memory settings, optimizing large queries, and configuring memory quotas for TiDB and TiKV"
tools: ["tidb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# TiDB OOM Error

TiDB OOM errors occur when TiDB server or TiKV nodes run out of memory during query execution, compaction, or high-concurrency operations.

## Why It Happens

- Large query result set exhausts memory
- Too many concurrent connections consume memory
- TiKV compaction uses excessive memory
- Sort or hash join operations exceed memory quota
- TiFlash analytics queries use too much memory
- Memory configuration is too low for workload

## Common Error Messages

```
ERROR: out of memory
```

```
ERROR: memory quota exceeded
```

```
FATAL: TiDB server out of memory
```

```
ERROR: TiKV memory limit exceeded
```

## How to Fix It

### 1. Check Memory Usage

```bash
# Check TiDB memory usage
curl http://tidb1:10080/status | jq '.memory'

# Check TiKV memory usage
curl http://tikv1:20180/status | jq '.memory'

# Check system memory
free -h
cat /proc/meminfo | head -5
```

### 2. Configure Memory Limits

```toml
# In tidb.toml
[performance]
max-memory = 10737418240  # 10GB per TiDB server

[mem-quota-query]
quota = 10737418240  # 10GB per query

[tikv-config]
# In tikv.toml
[rocksdb]
block-cache-size = "8GB"

[rocksdb.writecf]
block-cache-size = "4GB"
```

### 3. Fix Query Memory Issues

```sql
-- Set memory quota per session
SET tidb_mem_quota_query = 10737418240;  -- 10GB

-- Kill long-running queries
SHOW PROCESSLIST;
KILL <process_id>;

-- Use EXPLAIN to check memory usage
EXPLAIN ANALYZE SELECT * FROM large_table;
```

### 4. Monitor Memory

```bash
# Check TiDB memory metrics
curl http://tidb1:10080/metrics | grep memory

# Monitor with Prometheus
# Key metrics:
# - tidb_server_memory_quota_bytes
# - tikv_engine_memory_bytes
```

## Common Scenarios

- **Dashboard query OOMs**: Set tidb_mem_quota_query and add LIMIT.
- **TiKV compaction OOM**: Increase RocksDB block cache or reduce concurrent compactions.
- **High concurrency OOM**: Add more TiDB server instances.

## Prevent It

- Set appropriate memory quotas for queries
- Monitor memory usage with Prometheus
- Add more TiDB/TiKV nodes for high-concurrency workloads

## Related Pages

- [TiDB Query Error](/tools/tidb/tidb-query-error)
- [TiDB TiKV Error](/tools/tidb/tidb-tikv-error)
- [TiDB Config Error](/tools/tidb/tidb-gflag-error)
