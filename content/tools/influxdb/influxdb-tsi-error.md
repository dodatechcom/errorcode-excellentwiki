---
title: "[Solution] InfluxDB TSI (Time Series Index) Error — How to Fix"
description: "Fix InfluxDB TSI errors including index corruption, TSI conversion failures, and TSI configuration issues"
tools: ["influxdb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# InfluxDB TSI Error

TSI (Time Series Index) errors in InfluxDB occur when the inverted index becomes corrupted, the index cannot be built, or TSI-related configuration issues arise.

## Why It Happens

- The TSI index files are corrupted
- The TSI conversion from in-memory index fails
- Disk space is insufficient for TSI files
- The TSI log files are too large
- The index is too large to fit in memory

## Common Error Messages

```
error: TSI index corrupted
```

```
error: failed to build TSI index
```

```
error: TSI log file too large
```

```
error: no space left on device for TSI files
```

## How to Fix It

### 1. Check TSI Status

```bash
# Check TSI files
ls -la /var/lib/influxdb/data/mydb/*/index/
```

### 2. Rebuild TSI Index

```bash
# Stop InfluxDB
sudo systemctl stop influxd

# Rebuild index
influx-inspect rebuild-tsi -db mydb -data-dir /var/lib/influxdb/data -wal-dir /var/lib/influxdb/wal

# Start InfluxDB
sudo systemctl start influxd
```

### 3. Fix TSI Log Files

```bash
# Compact TSI logs
influx-inspect compact-tsi -db mydb -data-dir /var/lib/influxdb/data
```

### 4. Fix TSI Configuration

```bash
# In influxdb.conf
[data]
  index-version = "tsi1"
  cache-max-memory-size = "1g"
  cache-snapshot-memory-size = "256k"
```

## Common Scenarios

- **TSI index corruption after crash**: Rebuild with `influx-inspect rebuild-tsi`.
- **TSI logs too large**: Compact with `influx-inspect compact-tsi`.
- **TSI conversion fails**: Ensure sufficient disk space and restart InfluxDB.

## Prevent It

- Monitor TSI file sizes and disk usage
- Use SSD storage for the index directory
- Regularly compact TSI log files

## Related Pages

- [InfluxDB Shard Error](/tools/influxdb/influxdb-shard-error)
- [InfluxDB Compaction Error](/tools/influxdb/influxdb-compaction-error)
- [InfluxDB TSM Error](/tools/influxdb/influxdb-tsm-error)
