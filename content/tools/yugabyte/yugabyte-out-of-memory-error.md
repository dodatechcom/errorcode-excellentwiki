---
title: "[Solution] YugabyteDB Out of Memory Error — How to Fix"
description: "Fix YugabyteDB out of memory errors by resolving OOM kills, fixing memory configuration, and handling tablet server memory exhaustion"
tools: ["yugabyte"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# YugabyteDB Out of Memory Error

YugabyteDB out of memory errors occur when tablet servers or processes exceed their memory allocation limits, causing the OOM killer to terminate processes.

## Why It Happens

- Memory allocation per tablet is insufficient
- Too many concurrent queries consume available memory
- Tablet server memory limits are not configured
- Large scan operations exhaust memory
- Compaction memory usage spikes during heavy writes
- Connection pool reserves more memory than available

## Common Error Messages

```
FATAL: out of memory (OOM Killed)
```

```
ERROR: memory limit exceeded for tablet
```

```
ERROR: Could not allocate memory for operation
```

```
WARNING: memory usage exceeds threshold
```

## How to Fix It

### 1. Configure Memory Limits

```bash
# Set tserver memory flags
--memory_limit_hard_bytes=8589934592  # 8GB
--memory_limit_soft_pct=0.8
--ysql_conn_mgr_idle_timeout_ms=300000

# Set per-server memory allocation
--default_mem_limit=4294967296  # 4GB per tserver
```

### 2. Reduce Memory Usage

```sql
-- Reduce work memory for queries
SET work_mem = '64MB';

-- Limit parallel workers
SET max_parallel_workers_per_gather = 2;

-- Kill memory-heavy queries
SELECT pg_terminate_backend(pid)
FROM pg_stat_activity
WHERE state = 'active'
  AND query_start < NOW() - INTERVAL '10 minutes';
```

### 3. Monitor Memory Usage

```bash
# Check system memory
free -h

# Check tserver memory usage
curl http://yugabyte:9000/metrics | grep memory

# Check per-tablet memory
curl http://yugabyte:9000/metrics | grep tablet
```

### 4. Scale Up Memory

```bash
# Increase available memory
--memory_limit_hard_bytes=17179869184  # 16GB

# Or add more tablet servers to distribute load
# Start a new tserver on another node
```

## Common Scenarios

- **Tserver OOM under write load**: Increase memory_limit_hard_bytes or add more tservers.
- **Query causes OOM**: Reduce work_mem or optimize the query to use less memory.
- **Compaction causes OOM**: Reduce concurrent compaction threads.

## Prevent It

- Set memory limits appropriately based on available RAM
- Monitor memory usage with alerts
- Avoid running too many concurrent memory-intensive queries

## Related Pages

- [YugabyteDB TServer Memory Error](/tools/yugabyte/yugabyte-tserver-memory-error)
- [YugabyteDB OOM Error](/tools/yugabyte/yugabyte-tablet-heap-error)
- [YugabyteDB Tablet Error](/tools/yugabyte/yugabyte-tablet-error)
