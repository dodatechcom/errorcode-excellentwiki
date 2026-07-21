---
title: "[Solution] ScyllaDB Compaction Throughput Error — How to Fix"
description: "Fix ScyllaDB compaction throughput errors when compaction cannot keep up with write workload"
tools: ["scylladb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# ScyllaDB Compaction Throughput Error

Compaction throughput errors occur when ScyllaDB compaction falls behind the write rate, causing an accumulation of SSTables and degraded read performance.

## Why It Happens

- Write throughput exceeds compaction throughput capacity
- Compaction I/O scheduler is throttled by system limits
- Too many concurrent compactions compete for resources
- Large partitions create oversized SSTables
- Compaction strategy is not optimal for the workload

## Common Error Messages

```
WARN: Compaction is lagging behind writes
```

```
ERROR: Too many SSTables for table mykeyspace.users (500+)
```

```
compaction: unable to keep up with write throughput
```

## How to Fix It

### 1. Increase Compaction Throughput

```bash
nodetool setcompactionthroughput -t 256
```

### 2. Tune I/O Scheduler

```yaml
# In scylla.yaml
compaction_large_partition_warning_threshold_mb: 100
compaction_enforce_min_throughput: false
```

### 3. Use LCS for Write-Heavy Workloads

```cql
ALTER TABLE mykeyspace.events WITH compaction = {
  'class': 'LeveledCompactionStrategy',
  'sstable_size_in_mb': '160'
};
```

### 4. Monitor SSTable Count

```bash
nodetool tablestats mykeyspace.users | grep "SSTable count"
```

## Examples

```
$ nodetool tablestats mykeyspace.users | grep -E "(SSTable|Write)"
  SSTable count:     350
  Write latency:     1.2ms
  Compaction bytes:  50GB
```

## Prevent It

- Match compaction strategy to workload pattern
- Monitor SSTable count per table
- Schedule compaction-heavy operations during low-traffic periods

## Related Pages

- [ScyllaDB Compaction Error](/tools/scylladb/scylladb-compaction-error)
- [ScyllaDB Compaction Failed](/tools/scylladb/scylladb-compaction-failed)
- [ScyllaDB Compaction Strategy Error](/tools/scylladb/scylladb-compaction-strategy-error)
