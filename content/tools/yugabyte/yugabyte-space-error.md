---
title: "[Solution] YugabyteDB Space Error — How to Fix"
description: "Fix YugabyteDB space errors by resolving storage exhaustion, fixing data directory issues, and handling disk space management on tablet servers"
tools: ["yugabyte"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# YugabyteDB Space Error

YugabyteDB space errors occur when tablet servers run low on disk space, preventing writes, compaction, or new tablet creation.

## Why It Happens

- Data volume grows beyond available disk capacity
- WAL files accumulate without proper cleanup
- Tombstone records consume disk space
- Tablet splits create additional storage overhead
- Compaction is not keeping up with write rate
- Backup and snapshot files consume disk space

## Common Error Messages

```
ERROR: disk space critically low
```

```
ERROR: cannot create tablet: insufficient space
```

```
ERROR: RocksDB write stall due to space
```

```
WARNING: disk usage above threshold
```

## How to Fix It

### 1. Check Disk Usage

```bash
# Check disk usage per node
df -h /data/yugabyte

# Check per-tablet space
du -sh /data/yugabyte/yb-data/tserver/data/rocksdb/

# Check total data size
du -sh /data/yugabyte/
```

### 2. Free Up Space

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

### 3. Configure Space Management

```bash
# Set disk space alert thresholds
--fs_wal_dir=/data/yugabyte/yb-data/tserver/wals
--log_min_seconds_to_retain=600

# Reduce WAL retention
--log_min_seconds_to_retain=300
```

### 4. Add Storage Capacity

```bash
# Add new disk to tserver
--fs_data_dirs=/data/yugabyte,/data2/yugabyte

# Restart tserver
sudo systemctl restart yugabyte-tserver
```

## Common Scenarios

- **Tserver goes read-only**: Free up space by dropping data or adding storage.
- **Compaction fails**: Manually trigger compaction after freeing space.
- **New tablet creation fails**: Ensure sufficient space for tablet data.

## Prevent It

- Monitor disk usage with alerts at 70% and 85%
- Set up data retention policies
- Plan storage capacity for data growth

## Related Pages

- [YugabyteDB Disk Full Error](/tools/yugabyte/yugabyte-disk-full-error)
- [YugabyteDB TServer Disk Full](/tools/yugabyte/yugabyte-tserver-disk-full)
- [YugabyteDB Tablet Error](/tools/yugabyte/yugabyte-tablet-error)
