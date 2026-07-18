---
title: "[Solution] InfluxDB Shard Error — How to Fix"
description: "Fix InfluxDB shard errors including shard group issues, compaction failures, and shard deletion problems"
tools: ["influxdb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# InfluxDB Shard Error

Shard errors in InfluxDB occur when shard groups are corrupted, compaction fails, or shards cannot be created due to disk space or configuration issues.

## Why It Happens

- Shard groups are too large and cannot be compacted
- Disk space is full and new shards cannot be created
- The shard duration is incompatible with the retention policy
- Shard files are corrupted due to a crash
- Too many shard groups slow down queries

## Common Error Messages

```
error: shard group full
```

```
write failed: shard is locked
```

```
error: cannot create shard: no space left on device
```

```
WARN: shard 1 may be incomplete, last entry time: ...
```

## How to Fix It

### 1. Check Shard Status

```influxql
SHOW SHARD GROUPS
SHOW SHARDS
```

### 2. Fix Shard Compaction

```bash
# In influxdb.conf
[data]
  max-concurrent-compactions = 2
  compact-throughput = "48m"
  compact-throughput-burst = "48m"
```

### 3. Drop Old Shards

```influxql
-- Drop shard group by ID
DROP SHARD 123
```

### 4. Fix Disk Space

```bash
# Check disk usage
df -h /var/lib/influxdb/data

# Find largest databases and measurements
influx -execute 'SHOW DATABASES'

# Drop old data
influx -execute 'DROP DATABASE olddb'
```

## Common Scenarios

- **Shard compaction is slow**: Increase `max-concurrent-compactions` and `compact-throughput`.
- **Cannot create new shard**: Free disk space or drop old shards.
- **Queries are slow with many shards**: Reduce shard duration or drop old shard groups.

## Prevent It

- Set appropriate shard duration based on write volume and retention period
- Monitor shard count and disk usage regularly
- Configure compact-throughput for faster compaction

## Related Pages

- [InfluxDB Retention Error](/tools/influxdb/influxdb-retention-error)
- [InfluxDB Write Error](/tools/influxdb/influxdb-write-error)
- [InfluxDB TSM Error](/tools/influxdb/influxdb-tsm-error)
