---
title: "[Solution] TiDB Disk Quota Error — How to Fix"
description: "Fix TiDB disk quota errors by resolving storage limits, freeing space on TiKV nodes, and adjusting disk quota thresholds"
tools: ["tidb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# TiDB Disk Quota Error

TiDB disk quota errors occur when TiKV or TiFlash nodes exceed their configured storage limits or when temporary disk usage during large operations exceeds available space.

## Why It Happens

- TiKV store disk usage exceeds the configured quota
- Large import operations consume all available disk space
- WAL files accumulate during heavy write load
- Temporary files from Sort and Hash Join operations overflow disk
- Compaction cannot keep up with write rate
- Snapshot files consume additional disk space

## Common Error Messages

```
ERROR: store is disk full
```

```
ERROR: not enough space for region
```

```
ERROR: TiKV disk quota exceeded
```

```
FATAL: no space left on device
```

## How to Fix It

### 1. Check Disk Usage

```bash
# Check disk usage on each TiKV node
df -h /data/tikv

# Check store size via pd-ctl
pd-ctl store 1 | jq '.status.capacity, .status.used_size'

# List all stores with usage
pd-ctl store all | jq '.stores[] | {id: .store.id, used: .store.status.used_size, capacity: .store.status.capacity}'
```

### 2. Free Up Disk Space

```bash
# Remove old log files
find /data/tikv/log -name "*.log.*" -mtime +7 -delete

# Compact a specific store
pd-ctl operator add compact 1

# Remove tombstone regions
pd-ctl operator add remove-tombstone
```

```sql
-- Drop unused tables to free space
DROP TABLE IF EXISTS old_data;

-- Check table sizes
SELECT table_name,
  ROUND(data_length/1024/1024, 2) AS size_mb
FROM information_schema.tables
WHERE table_schema = 'mydb'
ORDER BY data_length DESC;
```

### 3. Adjust Disk Quota

```toml
# tikv.toml
[storage]
# Set disk space quota in GB
disk-quotas = [{ path = "/data/tikv", capacity = "500GB" }]
```

```bash
# Update disk quota via pd-ctl
pd-ctl config set region-size-limit 1073741824
```

### 4. Prevent Disk Exhaustion

```bash
# Set up disk usage monitoring
# Add to cron
*/5 * * * * df /data/tikv | awk 'NR==2 {if($5+0 > 85) print "Disk usage critical: "$5}'

# Enable auto compaction when disk is full
pd-ctl config set enable-auto-compaction true
```

## Common Scenarios

- **Import fails with disk full**: Pause import, free space, or add a new TiKV node.
- **TiKV store goes read-only**: Increase disk capacity or remove large old data.
- **Snapshot transfer fails**: Check disk space on both source and destination nodes.

## Prevent It

- Monitor disk usage with alerts at 70% and 85% thresholds
- Use dedicated disks for WAL and data
- Schedule regular compaction during low-traffic periods

## Related Pages

- [TiDB TiKV Error](/tools/tidb/tidb-tikv-error)
- [TiDB Import Error](/tools/tidb/tidb-import-error)
- [TiDB Region Error](/tools/tidb/tidb-region-error)
