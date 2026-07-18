---
title: "[Solution] InfluxDB TSM (Time-Structured Merge) Error — How to Fix"
description: "Fix InfluxDB TSM errors including TSM file corruption, merge failures, and TSM configuration issues"
tools: ["influxdb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# InfluxDB TSM Error

TSM errors in InfluxDB occur when the Time-Structured Merge tree encounters corruption, merge failures, or configuration issues that prevent data from being written or read correctly.

## Why It Happens

- TSM files are corrupted due to a crash or disk failure
- The TSM merge process fails due to insufficient memory
- The TSM file format is incompatible with the InfluxDB version
- Too many TSM files slow down queries
- The TSM compression settings are suboptimal

## Common Error Messages

```
error: TSM file corrupted
```

```
error: failed to merge TSM files
```

```
error: TSM file version mismatch
```

```
WARN: TSM file too large for compaction
```

## How to Fix It

### 1. Check TSM File Status

```bash
# List TSM files
ls -la /var/lib/influxdb/data/mydb/*/data/

# Check file sizes
du -sh /var/lib/influxdb/data/mydb/*/data/*.tsm
```

### 2. Repair Corrupt TSM Files

```bash
# Stop InfluxDB
sudo systemctl stop influxd

# Run TSM repair
influx-inspect rebuild-tsm /var/lib/influxdb/data/mydb

# Start InfluxDB
sudo systemctl start influxd
```

### 3. Fix TSM Merge Issues

```bash
# In influxdb.conf
[data]
  max-concurrent-compactions = 2
  compact-throughput = "48m"
  compact-throughput-burst = "48m"
```

### 4. Verify TSM Integrity

```bash
# Check TSM file integrity
influx-inspect verify-tsm -data-dir /var/lib/influxdb/data
```

## Common Scenarios

- **TSM corruption after crash**: Use `influx-inspect rebuild-tsm` to repair.
- **TSM merge is slow**: Increase `compact-throughput`.
- **TSM version mismatch**: Use the correct InfluxDB version for the TSM files.

## Prevent It

- Use SSD storage for the data directory
- Monitor TSM file count and compaction status
- Ensure clean shutdown of InfluxDB

## Related Pages

- [InfluxDB Compaction Error](/tools/influxdb/influxdb-compaction-error)
- [InfluxDB Shard Error](/tools/influxdb/influxdb-shard-error)
- [InfluxDB TSI Error](/tools/influxdb/influxdb-tsi-error)
