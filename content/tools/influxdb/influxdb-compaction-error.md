---
title: "[Solution] InfluxDB Compaction Error — How to Fix"
description: "Fix InfluxDB compaction errors including TSM file issues, compaction scheduling, and disk I/O problems during compaction"
tools: ["influxdb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# InfluxDB Compaction Error

Compaction errors in InfluxDB occur when the Time-Structured Merge Tree (TSM) engine cannot merge and optimize storage files. Failed compaction leads to degraded read performance and increased disk usage.

## Why It Happens

- Disk I/O is saturated and compaction cannot keep up
- The compaction queue is full due to excessive writes
- TSM files are corrupted and cannot be compacted
- The compaction process runs out of memory
- Too many concurrent compactions compete for resources

## Common Error Messages

```
compaction too slow: queuing full
```

```
error: compact: TSM file corrupt
```

```
WARN: Compaction of shard 123 failed
```

```
compaction exceeded memory limit
```

## How to Fix It

### 1. Tune Compaction Settings

```bash
# In influxdb.conf
[data]
  max-concurrent-compactions = 2
  compact-throughput = "48m"
  compact-throughput-burst = "48m"
  cache-max-memory-size = "1g"
```

### 2. Monitor Compaction Status

```influxql
SHOW SHARD GROUPS
SHOW SHARDS

-- Check compaction metrics via Prometheus or debug endpoint
curl -s 'http://localhost:8086/debug/vars' | grep compaction
```

### 3. Fix Corrupt TSM Files

```bash
# Stop InfluxDB
sudo systemctl stop influxd

# Run repair tool
influx-inspect rebuild-tsm /var/lib/influxdb/data/mydb

# Start InfluxDB
sudo systemctl start influxd
```

### 4. Reduce Write Pressure

```bash
# Batch writes to reduce compaction pressure
# Instead of 1 point per second, batch 1000 points per 10 seconds
```

## Common Scenarios

- **Compaction falls behind after bulk write**: Wait for compaction to catch up or increase resources.
- **TSM corruption after crash**: Use `influx-inspect` to rebuild TSM files.
- **Compaction too slow on HDD**: Move to SSD storage for better I/O performance.

## Prevent It

- Use SSD storage for the InfluxDB data directory
- Monitor compaction metrics and queue depth
- Avoid excessive write rates that overwhelm compaction

## Related Pages

- [InfluxDB TSM Error](/tools/influxdb/influxdb-tsm-error)
- [InfluxDB Shard Error](/tools/influxdb/influxdb-shard-error)
- [InfluxDB Write Error](/tools/influxdb/influxdb-write-error)
