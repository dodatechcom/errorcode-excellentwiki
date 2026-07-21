---
title: "[Solution] InfluxDB Shard Group Error — How to Fix"
description: "Fix InfluxDB shard group errors when shard groups cannot be created, accessed, or managed properly"
tools: ["influxdb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# InfluxDB Shard Group Error

Shard group errors occur when InfluxDB fails to create, access, or manage shard groups that organize data by time ranges.

## Why It Happens

- Shard group duration is incompatible with retention policy
- Too many shard groups cause excessive file handles
- Shard group creation fails due to disk space
- Clock skew causes data to land in wrong shard group
- Shard group metadata is corrupted in the meta store

## Common Error Messages

```
error: shard group not found for timestamp
```

```
partial write: unable to create new shard group
```

```
error: too many open shards
```

```
shard: unable to locate shard for time range
```

## How to Fix It

### 1. Check Shard Group Configuration

```bash
influx -database mydb -execute 'SHOW SHARD GROUPS'
```

### 2. Adjust Shard Group Duration

```bash
# Create retention policy with appropriate shard duration
influx -execute 'CREATE RETENTION POLICY "30d" ON "mydb" DURATION 30d REPLICATION 1 SHARD DURATION 1d'
```

### 3. Drop Old Shard Groups

```bash
influx -database mydb -execute 'DROP RETENTION POLICY "old_policy" ON "mydb"'
```

### 4. Verify Shard Filesystem State

```bash
ls -la /var/lib/influxdb/data/mydb/autogen/
du -sh /var/lib/influxdb/data/mydb/autogen/*/
```

## Examples

```
$ influx -database mydb -execute 'SHOW SHARD GROUPS'
id  database  retention_policy  shard_group_duration  start_time          end_time
1   mydb      autogen           168h0m0s               2024-01-01T00:00:00Z 2024-01-08T00:00:00Z
2   mydb      autogen           168h0m0s               2024-01-08T00:00:00Z 2024-01-15T00:00:00Z
```

## Prevent It

- Size shard groups based on write rate and retention duration
- Limit total shard count per database
- Monitor shard count with InfluxDB metrics

## Related Pages

- [InfluxDB Shard Error](/tools/influxdb/influxdb-shard-error)
- [InfluxDB Retention Error](/tools/influxdb/influxdb-retention-error)
- [InfluxDB Compaction Error](/tools/influxdb/influxdb-compaction-error)
