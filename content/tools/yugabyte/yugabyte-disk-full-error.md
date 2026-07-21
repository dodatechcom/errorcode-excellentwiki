---
title: "[Solution] YugabyteDB Disk Full Error — How to Fix"
description: "Fix YugabyteDB disk full errors by resolving storage exhaustion, cleaning up old data, and handling tablet data growth management"
tools: ["yugabyte"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# YugabyteDB Disk Full Error

YugabyteDB disk full errors occur when tablet servers run out of disk space, preventing new writes, tablet splits, or compaction operations.

## Why It Happens

- Data volume grows beyond available disk capacity
- WAL files accumulate without proper cleanup
- Compaction cannot keep up with write throughput
- Tombstone records consume disk space
- Tablet splits create additional storage overhead
- Temporary files from backup or restore operations fill disk

## Common Error Messages

```
ERROR: disk space is critically low
```

```
ERROR: RocksDB write error: no space left on device
```

```
ERROR: tablet cannot flush: disk full
```

```
FATAL: out of disk space
```

## How to Fix It

### 1. Check Disk Usage

```bash
# Check disk usage on each node
df -h /data/yugabyte

# Check data directory size
du -sh /data/yugabyte/

# Check per-tablet disk usage
du -sh /data/yugabyte/yb-data/tserver/data/rocksdb/
```

### 2. Free Up Disk Space

```bash
# Delete old WAL files
find /data/yugabyte -name "*.log" -mtime +7 -delete

# Remove old snapshot files
find /data/yugabyte -name "*.snapshot" -mtime +3 -delete

# Clean up tablet server trash
rm -rf /data/yugabyte/yb-data/tserver/data/trash/*
```

### 3. Drop Unused Data

```sql
-- Drop unused tables
DROP TABLE IF EXISTS old_data;

-- Check table sizes
SELECT
  table_name,
  pg_size_pretty(pg_total_relation_size(table_name::regclass)) AS size
FROM information_schema.tables
WHERE table_schema = 'public'
ORDER BY pg_total_relation_size(table_name::regclass) DESC;
```

### 4. Add Storage Capacity

```bash
# Add a new disk to tserver
# In tserver.gflags:
--fs_data_dirs=/data/yugabyte,/data2/yugabyte

# Restart tserver
sudo systemctl restart yugabyte-tserver
```

## Common Scenarios

- **Tserver disk full**: Drop unused data or add more storage.
- **Compaction fails**: Manually trigger compaction after freeing space.
- **Write operations blocked**: The cluster goes into a read-only state when disk is full.

## Prevent It

- Monitor disk usage with alerts at 70% and 85% thresholds
- Set up data retention policies
- Plan for data growth before disk fills up

## Related Pages

- [YugabyteDB Tablet Error](/tools/yugabyte/yugabyte-tablet-error)
- [YugabyteDB TServer Disk Full](/tools/yugabyte/yugabyte-tserver-disk-full)
- [YugabyteDB Compaction Error](/tools/yugabyte/yugabyte-compaction-error)
