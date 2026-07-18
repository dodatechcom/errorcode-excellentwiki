---
title: "[Solution] Cassandra Commitlog Error - Fix Commit Log Write Failed"
description: "Fix Cassandra commitlog write failures. Resolve commitlog corruption, disk issues, and write path errors in Cassandra."
tools: ["cassandra"]
error-types: ["commitlog-error"]
severities: ["critical"]
weight: 5
---

This error means the Cassandra commitlog cannot write. The commitlog is a write-ahead log that ensures data durability, and failures here prevent all writes.

## What This Error Means

When commitlog writes fail, you see:

```
WriteTimeoutException: Timed out after 2000ms writing to commitlog
# or
IOError: Commit log write failed
# or
CommitLogReplayException: Corrupted commit log
```

The commitlog receives all writes before they are flushed to SSTables. A commitlog failure stops all write operations on the affected node.

## Why It Happens

- The commitlog disk is full or has I/O errors
- The commitlog segment is corrupted
- The filesystem on the commitlog disk is full
- The commitlog directory permissions are incorrect
- The disk is too slow for the write workload
- The commitlog_sync settings are too aggressive

## How to Fix It

### Check commitlog disk space

```bash
df -h /var/lib/cassandra/commitlog
```

Ensure the commitlog directory has sufficient space.

### Monitor commitlog activity

```bash
nodetool tpstats | grep commitlog
```

Check pending and completed commitlog tasks.

### Move commitlog to faster disk

```yaml
# cassandra.yaml
commitlog_directory: /mnt/ssd/cassandra/commitlog
```

SSDs significantly improve commitlog write performance.

### Increase commitlog disk space

```bash
# Find what is consuming space
du -sh /var/lib/cassandra/commitlog/*
```

### Fix commitlog corruption

```bash
# If commitlog is corrupted, remove it (data loss possible)
sudo systemctl stop cassandra
rm /var/lib/cassandra/commitlog/*
sudo systemctl start cassandra
```

Only do this if the node has no unflushed data that matters.

### Adjust commitlog sync settings

```yaml
# cassandra.yaml
# Periodic sync (default)
commitlog_sync: periodic
commitlog_sync_period_in_ms: 10000

# Or batch sync for durability
commitlog_sync: batch
commitlog_sync_batch_window_in_ms: 2
```

### Increase commitlog segment size

```yaml
# cassandra.yaml
commitlog_segment_size_in_mb: 32
```

Larger segments reduce the frequency of segment creation.

### Check commitlog permissions

```bash
ls -la /var/lib/cassandra/commitlog/
# Cassandra user should own the directory
chown -R cassandra:cassandra /var/lib/cassandra/commitlog
```

### Monitor write latency

```bash
nodetool proxyhistograms
```

High write latency may indicate commitlog disk issues.

## Common Mistakes

- Placing the commitlog on the same slow disk as SSTables
- Not monitoring commitlog disk space before it fills up
- Removing commitlog files without understanding data loss implications
- Not using SSDs for the commitlog directory
- Ignoring commitlog write latency warnings

## Related Pages

- [Cassandra Write Timeout]({{< relref "/tools/cassandra/cassandra-write-timeout" >}}) -- write timeouts
- [Cassandra SSTable Error]({{< relref "/tools/cassandra/cassandra-sstable-error" >}}) -- SSTable issues
- [Cassandra Compaction Error]({{< relref "/tools/cassandra/cassandra-compaction-error" >}}) -- compaction problems
