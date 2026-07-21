---
title: "[Solution] InfluxDB Insufficient Disk Error — How to Fix"
description: "Fix InfluxDB insufficient disk errors when available storage drops below minimum required thresholds"
tools: ["influxdb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# InfluxDB Insufficient Disk Error

Insufficient disk errors occur when the available storage on the InfluxDB data partition drops below the minimum threshold required for normal operations.

## Why It Happens

- Continuous writes fill the disk faster than retention policies delete old data
- Compaction creates temporary files that consume additional disk space
- WAL files grow large during sustained write bursts
- Log files are not rotated and consume disk space
- Backup files are stored on the same partition

## Common Error Messages

```
error: insufficient disk space for write operation
```

```
partial write: disk space critically low, rejecting writes
```

```
error: cannot create TSM file: no space left on device
```

```
WARN: disk usage above 95%, entering read-only mode
```

## How to Fix It

### 1. Check Disk Usage

```bash
df -h /var/lib/influxdb
du -sh /var/lib/influxdb/data/* /var/lib/influxdb/wal/*
```

### 2. Delete Unnecessary Data

```bash
# Drop old database
influx -execute 'DROP DATABASE "test_db"'

# Drop specific measurement
influx -database mydb -execute 'DROP MEASUREMENT "old_logs"'
```

### 3. Configure Disk Usage Thresholds

```bash
[data]
  disk-side-max-bytes = 0
  max WAL size = 1073741824
```

### 4. Move Data to Larger Disk

```bash
sudo systemctl stop influxdb
sudo rsync -av /var/lib/influxdb/ /mnt/larger-disk/influxdb/
# Update influxdb.conf data and WAL paths
sudo systemctl start influxdb
```

## Examples

```
$ df -h /var/lib/influxdb
Filesystem      Size  Used Avail Use%
/dev/sdb1       100G  97G   3G   97%
```

## Prevent It

- Set up disk monitoring with alerts at 80% usage
- Configure retention policies to auto-delete old data
- Use separate partitions for data, WAL, and logs

## Related Pages

- [InfluxDB Disk Error](/tools/influxdb/influxdb-disk-error)
- [InfluxDB Disk Space Error](/tools/influxdb/influxdb-disk-space-error)
- [InfluxDB Write Error](/tools/influxdb/influxdb-write-error)
