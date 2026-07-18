---
title: "[Solution] Cassandra Compaction Error — How to Fix"
description: "Fix Cassandra compaction errors by resolving SSTable conflicts, tuning compaction strategy, managing disk space, and recovering from failed compactions."
tools: ["cassandra"]
error-types: ["compaction-error"]
severities: ["error"]
weight: 5
comments: true
---

A Cassandra compaction error occurs when the compaction process fails to merge SSTables as expected. Compaction is critical for read performance and space reclamation, and failures can degrade the cluster over time.

## Why It Happens

Compaction errors range from temporary failures that self-recover to persistent issues that require manual intervention. Understanding the compaction strategy and its failure modes is essential.

- Insufficient disk space prevents new SSTables from being written during compaction
- The compaction throughput limiter is too low for the workload
- Too many SSTables accumulate and exceed the maximum compaction threshold
- Corrupted SSTables cause checksum failures during merge
- The compaction strategy is mismatched with the write pattern (e.g., STCS for time-series data)
- Node restarts during compaction leave orphaned or partially compacted SSTables
- Memory pressure from large compaction jobs causes OOM kills

## Common Error Messages

```text
CompactionStrategyError: Compaction failed for table keyspace.table: IOException: No space left on device
```

The disk is full. Compaction cannot create new SSTables because the data directory has no remaining capacity.

```text
SSTableReaderException: Cannot open SSTable — corrupted file detected at /var/lib/cassandra/data/ks/table-md-123456-C.db
```

An SSTable file is corrupted. The compaction process cannot read it to merge with other SSTables.

```text
CompactionInterruptedException: Compaction for table was interrupted by node restart
```

The node restarted while compaction was in progress. The compaction state was lost.

```text
StreamingException: Failed to stream SSTable during compaction with remote node
```

Remote compaction or streaming failed during a repair or decommission operation.

## How to Fix It

### 1. Free Disk Space

```bash
# Check disk usage
df -h /var/lib/cassandra

# Find the largest files
du -sh /var/lib/cassandra/data/* | sort -rh | head -20

# Delete old snapshots that are consuming space
nodetool clearsnapshot -t <snapshot_name>

# Remove completed commit log segments
sudo rm /var/lib/cassandra/commitlog/commitlog-*.log
```

```bash
# Set up automatic space monitoring
# Add to crontab:
df -h /var/lib/cassandra | awk 'NR==2{print $5}' | tr -d '%' | \
  xargs -I{} test {} -gt 80 && echo "Disk above 80%" | mail -s "Cassandra Disk Alert" admin@example.com
```

### 2. Increase Compaction Throughput

```yaml
# cassandra.yaml
compaction_throughput_mb_per_sec: 256
concurrent_compactors: 4
```

```bash
# Adjust at runtime without restart
nodetool setcompactionthroughput -t 256
nodetool setconcurrentcompactors -t 4
```

The default throughput is 64 MB/s. Increase it for write-heavy workloads, but monitor I/O to avoid starving reads.

### 3. Repair Corrupted SSTables

```bash
# Verify SSTable integrity
sstableverify /var/lib/cassandra/data/keyspace/table-md-123456-C.db

# Use sstablescrub to fix minor corruption
sstablescrub keyspace table

# If corruption is severe, delete the corrupted SSTable and run repair
nodetool repair keyspace table
```

```bash
# Check for anti-entropy issues
nodetool tablestats keyspace.table | grep "SSTable count"
```

### 4. Switch Compaction Strategy

```cql
-- Bad: STCS for time-series data with range deletes
ALTER TABLE events WITH compaction = {
    'class': 'SizeTieredCompactionStrategy'
};

-- Good: TWCS for time-series with window-based deletes
ALTER TABLE events WITH compaction = {
    'class': 'TimeWindowCompactionStrategy',
    'compaction_window_size': '1',
    'compaction_window_unit': 'DAYS'
};

-- Good: LCS for write-heavy workloads needing predictable read performance
ALTER TABLE users WITH compaction = {
    'class': 'LeveledCompactionStrategy',
    'sstable_size_in_mb': '160'
};
```

### 5. Manage SSTable Count

```bash
# Check SSTable count per table
nodetool tablehistograms keyspace.table | grep "SSTables"

# Trigger manual compaction if needed (use cautiously)
nodetool compact keyspace table

# Flush memtables to disk first
nodetool flush keyspace table
```

Keep SSTable count below 32 per read path. High SSTable counts degrade read performance exponentially.

## Common Scenarios

**Compaction falls behind during write spikes.** If writes exceed compaction throughput, SSTables accumulate and reads slow down. Increase `compaction_throughput_mb_per_sec` temporarily and consider adding nodes to distribute write load.

**TWCS windows create too many SSTables.** If the window size is too small, each window creates separate SSTables. Increase the window size to `1 DAY` or `7 DAYS` for high-volume tables.

**Compaction fails after disk replacement.** The new disk may have different I/O characteristics. Run `nodetool repair` after replacing a disk to ensure data consistency, and benchmark the new disk with fio before returning to production.

## Prevent It

- Monitor SSTable count per table and alert when it exceeds 32, as read performance degrades exponentially beyond this threshold
- Schedule compaction during low-traffic windows using `nodetool setcompactionthroughput` to increase throughput during off-peak hours
- Choose the correct compaction strategy at table creation time — TWCS for time-series, LCS for read-heavy, STCS for write-heavy with few deletes
