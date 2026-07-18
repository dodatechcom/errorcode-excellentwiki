---
title: "[Solution] ScyllaDB Disk Error — How to Fix"
description: "Fix ScyllaDB disk errors by freeing storage, resolving I/O errors, and configuring compaction to prevent disk space exhaustion"
tools: ["scylladb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# ScyllaDB Disk Error

ScyllaDB disk errors occur when the database runs out of storage space or encounters I/O errors. Adequate disk space is essential for compaction, commitlog, and SSTable storage.

## Why It Happens

- Disk space is exhausted (no_space_left_on_device)
- I/O errors on the storage device
- Commitlog disk is full
- Compaction fails due to insufficient temporary space
- XFS filesystem corruption
- Disk I/O throughput is saturated

## Common Error Messages

```
IOError: No space left on device
```

```
CommitlogError: Commit log unable to allocate new segment
```

```
CompactionError: Compaction failed - disk full
```

```
DiskError: I/O error reading SSTable
```

## How to Fix It

### 1. Check Disk Usage

```bash
# Check disk space
df -h /var/lib/scylla/data
df -h /var/lib/scylla/commitlog

# Find large tables
du -sh /var/lib/scylla/data/*/

# Check commitlog size
ls -la /var/lib/scylla/commitlog/
```

### 2. Free Disk Space

```bash
# Delete old snapshots
nodetool clearsnapshot --all

# Remove old commitlog segments (if safe)
nodetool cleanup mykeyspace

# Truncate old data
TRUNCATE mykeyspace.old_events_table;

# Drop unused tables
DROP TABLE mykeyspace.archived_data;
```

### 3. Configure Compaction for Disk Management

```bash
# Run full compaction to reclaim space
nodetool compact mykeyspace mytable

# Check compaction statistics
nodetool compactionstats

# Increase compaction throughput for faster cleanup
nodetool setcompactionthroughput 256
```

```cql
-- Use TWCS for time-series to auto-expire data
ALTER TABLE events WITH compaction = {
  'class': 'TimeWindowCompactionStrategy',
  'compaction_window_size': 1,
  'compaction_window_unit': 'DAYS'
};

-- Set GC grace seconds to expire tombstones faster
ALTER TABLE events WITH gc_grace_seconds = 86400;
```

### 4. Monitor and Alert

```bash
# Set up disk monitoring
cat /etc/cron.d/scylla-disk-check
*/5 * * * * root df -h /var/lib/scylla/data | awk 'NR==2{print $5}' | grep -q "9[0-9]%" && echo "Disk critical" | mail -s "ScyllaDB Disk Alert" admin@example.com
```

```yaml
# Prometheus alerting rules
- alert: ScyllaDBDiskSpaceLow
  expr: node_filesystem_avail_bytes{mountpoint="/var/lib/scylla/data"} / node_filesystem_size_bytes{mountpoint="/var/lib/scylla/data"} < 0.1
  for: 5m
  labels:
    severity: critical
```

## Common Scenarios

- **Commitlog fills up**: Increase commitlog disk size or add disk space.
- **Compaction fails**: Run `nodetool compact` to merge SSTables and free space.
- **SSTable writes fail**: Check disk I/O health and free space urgently.

## Prevent It

- Monitor disk usage with alerts at 80% and 90% thresholds
- Use TWCS for time-series data to minimize disk usage
- Schedule regular cleanup and snapshot deletion

## Related Pages

- [ScyllaDB Compaction Error](/tools/scylladb/scylladb-compaction-error)
- [ScyllaDB Commitlog Error](/tools/scylladb/scylladb-commitlog-error)
- [ScyllaDB SSTable Error](/tools/scylladb/scylladb-sstable-error)
