---
title: "[Solution] InfluxDB Migration Error — How to Fix"
description: "Fix InfluxDB migration errors when upgrading between major versions fails due to schema or data incompatibilities"
tools: ["influxdb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# InfluxDB Migration Error

Migration errors occur when upgrading InfluxDB from one major version to another, such as from 1.x to 2.x, and the data or schema is incompatible with the new version.

## Why It Happens

- Data format from 1.x is not compatible with 2.x storage engine
- Migration tool cannot parse legacy configuration files
- Insufficient disk space for migration backup
- Custom retention policies conflict with v2 bucket model
- Meta store format has changed between versions

## Common Error Messages

```
error: migration failed: incompatible data format
```

```
influx-migrate: error opening database: invalid TSM version
```

```
migration error: cannot convert retention policy to bucket
```

```
error: backup required before migration, disk space insufficient
```

## How to Fix It

### 1. Backup Before Migration

```bash
influx backup /tmp/influx_backup_$(date +%s)
```

### 2. Use the Official Migration Tool

```bash
influxd upgrade \
  --v1-dir /var/lib/influxdb \
  --v2-dir /var/lib/influxdbv2 \
  --config-path /etc/influxdb/influxdb.conf
```

### 3. Fix Data Incompatibilities

```bash
# Run influx_inspect on all shards
for shard in $(find /var/lib/influxdb/data -name "*.tsm" -exec dirname {} \; | sort -u); do
  influx_inspect check -path "$shard"
done
```

### 4. Manual Bucket Migration

```bash
# Export from v1
influx -database mydb -execute 'SELECT * FROM mydb.cpu' -format csv > cpu_data.csv

# Import to v2
cat cpu_data.csv | influx write --bucket mydb --format csv
```

## Examples

```
$ influxd upgrade --v1-dir /var/lib/influxdb
Error: migration failed: corrupt TSM index in shard 14
Run influx_inspect rebuild-tsm on affected shards before upgrading
```

## Prevent It

- Always backup before migration
- Test migration on a staging environment
- Review the version-specific migration guide

## Related Pages

- [InfluxDB Backup Error](/tools/influxdb/influxdb-backup-error)
- [InfluxDB Restore Error](/tools/influxdb/influxdb-restore-error)
- [InfluxDB Data Recovery Error](/tools/influxdb/influxdb-data-recovery-error)
