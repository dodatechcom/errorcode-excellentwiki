---
title: "[Solution] InfluxDB Disk Space Error — How to Fix"
description: "Fix InfluxDB disk space errors when storage fills up and prevents new writes or compaction"
tools: ["influxdb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# InfluxDB Disk Space Error

Disk space errors occur when the InfluxDB data directory runs out of available storage, preventing new writes and compaction operations.

## Why It Happens

- High write throughput generates more data than disk can store
- Retention policies are not configured to auto-delete old data
- Compaction cannot keep up with data generation rate
- WAL files accumulate without being flushed
- Log files grow excessively large

## Common Error Messages

```
error: write failed: no space left on device
```

```
WARN: shard exceeded disk size limit
```

```
error: compaction failed: insufficient disk space
```

```
partial write: disk full, unable to write to shard
```

## How to Fix It

### 1. Check Disk Usage

```bash
df -h /var/lib/influxdb
du -sh /var/lib/influxdb/data/*
du -sh /var/lib/influxdb/wal/*
```

### 2. Remove Old Data

```bash
# Drop old measurements
influx -database mydb -execute 'DROP MEASUREMENT "old_data"'

# Drop entire database if no longer needed
influx -execute 'DROP DATABASE "old_logs"'
```

### 3. Configure Retention Policies

```bash
influx -execute 'CREATE RETENTION POLICY "short" ON "mydb" DURATION 7d REPLICATION 1'
influx -execute 'ALTER RETENTION POLICY "short" ON "mydb" DURATION 7d'
```

### 4. Move Data to Larger Disk

```bash
sudo systemctl stop influxdb
sudo rsync -avz /var/lib/influxdb/ /mnt/larger-disk/influxdb/
sudo sed -i 's|/var/lib/influxdb|/mnt/larger-disk/influxdb|g' /etc/influxdb/influxdb.conf
sudo systemctl start influxdb
```

## Examples

```
$ df -h /var/lib/influxdb
Filesystem      Size  Used Avail Use% Mounted on
/dev/sda1       50G   49G  0G  100% /
```

## Prevent It

- Set up disk usage monitoring with alerts at 80%
- Configure retention policies for all databases
- Use tiered storage for long-term data archival

## Related Pages

- [InfluxDB Disk Error](/tools/influxdb/influxdb-disk-error)
- [InfluxDB Write Error](/tools/influxdb/influxdb-write-error)
- [InfluxDB Retention Error](/tools/influxdb/influxdb-retention-error)
