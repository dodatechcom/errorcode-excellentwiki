---
title: "[Solution] TiDB TiKV Scheduler Error — How to Fix"
description: "Fix TiDB TiKV scheduler errors when the scheduler cannot process transaction requests"
tools: ["tidb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# TiDB TiKV Scheduler Error

TiKV scheduler errors occur when the scheduler component in TiKV cannot process incoming transaction requests due to resource constraints or internal errors.

## Why It Happens

- Scheduler is overloaded with concurrent transactions
- Latches are contended, causing transaction queuing
- Memory allocated for scheduler is insufficient
- Disk I/O bottleneck prevents transaction processing
- Scheduler thread pool is exhausted

## Common Error Messages

```
TiKV: scheduler latch wait timeout
```

```
error: scheduler busy, unable to process request
```

```
tikv: transaction timeout, scheduler unable to commit
```

## How to Fix It

### 1. Check Scheduler Metrics

```bash
curl -s http://tikv:20180/metrics | grep tikv_scheduler
```

### 2. Increase Scheduler Threads

```toml
# In tikv.toml
[storage]
scheduler-worker-pool-size = 16
```

### 3. Increase Latch Wait Timeout

```toml
# In tikv.toml
[storage]
scheduler-max-waiting-ms = 2000
```

### 4. Monitor Contention

```bash
curl -s http://tikv:20180/metrics | grep tikv_scheduler_latch_wait_duration
```

## Examples

```
$ curl -s http://tikv:20180/metrics | grep scheduler
tikv_scheduler_cmd_duration_seconds_bucket{type="prewrite",le="0.01"} 50000
tikv_scheduler_latch_wait_duration_seconds_bucket{le="0.1"} 45000
```

## Prevent It

- Size scheduler worker pool based on CPU cores
- Monitor latch contention metrics
- Use appropriate transaction isolation levels

## Related Pages

- [TiDB TiKV Scheduler Error](/tools/tidb/tidb-tikv-scheduler-error)
- [TiDB TiKV Error](/tools/tidb/tidb-tikv-error)
- [TiDB Transaction Error](/tools/tidb/tidb-transaction-error)
