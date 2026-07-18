---
title: "[Solution] ScyllaDB Compaction Error — How to Fix"
description: "Fix ScyllaDB compaction errors by resolving disk space issues, fixing SSTable corruption, and tuning compaction strategy settings"
tools: ["scylladb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# ScyllaDB Compaction Error

ScyllaDB compaction errors occur when the compaction process fails to merge SSTables, leading to read amplification and degraded performance. Compaction is critical for maintaining ScyllaDB performance.

## Why It Happens

- Insufficient disk space for compaction output
- SSTable files are corrupted or have integrity errors
- Compaction strategy is misconfigured for the workload
- Tombstone accumulation causes compaction to stall
- Too many SSTables trigger excessive compaction
- Compaction I/O overwhelms the disk subsystem

## Common Error Messages

```
CompactionError: Compaction for table failed
```

```
IOError: Could not create SSTable component
```

```
SSTableCorruptError: Corrupted SSTable detected
```

```
CompactionStopping: Stopping compaction due to disk space
```

## How to Fix It

### 1. Check Compaction Status

```bash
# View compaction statistics
nodetool compactionstats

# View table compaction strategy
nodetool cfstats mykeyspace.mytable | grep -i compaction

# List all SSTables
nodetool tablestats mykeyspace.mytable | grep SSTables
```

### 2. Fix Disk Space Issues

```bash
# Check disk usage
df -h /var/lib/scylla/data

# Find large tables
du -sh /var/lib/scylla/data/*/

# Disable auto-compaction temporarily (emergency only)
nodetool disableautocompaction mykeyspace mytable

# Clear snapshot space
nodetool clearsnapshot --all
```

### 3. Configure Compaction Strategy

```cql
-- STCS: default, good for write-heavy workloads
ALTER TABLE mykeyspace.mytable WITH compaction = {
  'class': 'SizeTieredCompactionStrategy',
  'min_sstable_size': 104857600,
  'min_threshold': 4,
  'max_threshold': 32
};

-- LCS: good for read-heavy workloads
ALTER TABLE mykeyspace.mytable WITH compaction = {
  'class': 'LeveledCompactionStrategy',
  'sstable_size_in_mb': 160
};

-- TWCS: best for time-series workloads
ALTER TABLE mykeyspace.mytable WITH compaction = {
  'class': 'TimeWindowCompactionStrategy',
  'compaction_window_size': 1,
  'compaction_window_unit': 'DAYS'
};
```

### 4. Repair Corrupted SSTable

```bash
# Check for corrupted SSTables
nodetool verify mykeyspace mytable

# If corruption found, try to recover
nodetool scrub mykeyspace mytable

# Last resort: rebuild from replication
nodetool rebuild mykeyspace

# Or delete corrupted SSTable and rebuild
nodetool compact mykeyspace mytable
```

## Common Scenarios

- **Compaction falls behind**: Increase compaction throughput with `nodetool setcompactionthroughput`.
- **Read latency spikes**: Switch from STCS to LCS for better read performance.
- **Time-series data bloat**: Use TWCS with appropriate time window settings.

## Prevent It

- Monitor `PendingCompactions` and `SSTablesPerReadHistogram` metrics
- Use TWCS for time-series data to minimize compaction overhead
- Set up disk space alerts to prevent compaction failures

## Related Pages

- [ScyllaDB SSTable Error](/tools/scylladb/scylladb-sstable-error)
- [ScyllaDB Disk Error](/tools/scylladb/scylladb-disk-error)
- [ScyllaDB Commitlog Error](/tools/scylladb/scylladb-commitlog-error)
