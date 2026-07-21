---
title: "[Solution] InfluxDB Data Recovery Error — How to Fix"
description: "Fix InfluxDB data recovery errors when restoring from backup or repairing corrupted TSM files"
tools: ["influxdb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# InfluxDB Data Recovery Error

Data recovery errors occur when attempting to restore InfluxDB from backup or repair corrupted data files using influx_inspect or backup utilities.

## Why It Happens

- Backup files are corrupted or incomplete
- TSM files have invalid checksums
- Restore target has insufficient disk space
- Version mismatch between backup and restore versions
- Permission issues on data directories during restore

## Common Error Messages

```
error: restore failed: corrupt TSM file
```

```
influx_inspect: error reading TSM: invalid checksum
```

```
error: backup directory does not contain valid shards
```

```
restore: unable to write to data directory: permission denied
```

## How to Fix It

### 1. Verify Backup Integrity

```bash
influx_inspect verify -path /backup/shard_1234.tsm
```

### 2. Repair Corrupt TSM Files

```bash
influx_inspect rebuild-tsm -path /var/lib/influxdb/data/mydb/autogen/1234
influx_inspect -pattern /var/lib/influxdb/data/mydb/autogen/1234 copy
```

### 3. Restore with Correct Permissions

```bash
sudo chown -R influxdb:influxdb /var/lib/influxdb/
influxd restore -portable -backup /backup/2024-01-15 --db mydb
```

### 4. Match Versions for Restore

```bash
# Check backup version
cat /backup/meta/2024-01-15/meta.json | grep version

# Use matching influxd version for restore
```

## Examples

```
$ influx_inspect verify -path /backup/shard_1234.tsm
Error: invalid checksum for block at offset 1048576
```

## Prevent It

- Regularly verify backup integrity with influx_inspect
- Store backups in geographically separate locations
- Test restore procedures on a staging environment

## Related Pages

- [InfluxDB Backup Error](/tools/influxdb/influxdb-backup-error)
- [InfluxDB Restore Error](/tools/influxdb/influxdb-restore-error)
- [InfluxDB TSM Error](/tools/influxdb/influxdb-tsm-error)
