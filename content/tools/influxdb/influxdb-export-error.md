---
title: "[Solution] InfluxDB Export Error — How to Fix"
description: "Fix InfluxDB export errors when using influx inspect export to dump database content to line protocol"
tools: ["influxdb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# InfluxDB Export Error

Export errors occur when using the influx_inspect export command or API endpoints to export data from InfluxDB to line protocol or other formats.

## Why It Happens

- Data directory has corrupt TSM files that cannot be read
- Output path is not writable or disk is full
- Export filter specifies a non-existent measurement or database
- Memory limit is exceeded during large exports
- Export process interrupted by system shutdown

## Common Error Messages

```
error: failed to export: corrupt TSM index
```

```
export: cannot write to output path: permission denied
```

```
error: measurement not found in database
```

```
influx_inspect export: out of memory during export
```

## How to Fix It

### 1. Export with Limited Scope

```bash
influx_inspect export \
  -database mydb \
  -start 2024-01-01T00:00:00Z \
  -end 2024-01-31T23:59:59Z \
  -out /tmp/export.lp
```

### 2. Fix Output Permissions

```bash
mkdir -p /tmp/influx_export
chmod 777 /tmp/influx_export
influx_inspect export -database mydb -out /tmp/influx_export/data.lp
```

### 3. Export in Chunks

```bash
for shard in $(ls /var/lib/influxdb/data/mydb/autogen/); do
  influx_inspect export \
    -shard "$shard" \
    -out "/tmp/export_shard_${shard}.lp"
done
```

### 4. Increase Memory for Export

```bash
ulimit -v unlimited
influx_inspect export -database mydb -out /tmp/export.lp
```

## Examples

```
$ influx_inspect export -database mydb -out /tmp/export.lp
Exporting database mydb... done (150000 points exported)
```

## Prevent It

- Export data regularly as part of backup strategy
- Test exports on small date ranges before full export
- Monitor disk space before large export operations

## Related Pages

- [InfluxDB Backup Error](/tools/influxdb/influxdb-backup-error)
- [InfluxDB CSV Error](/tools/influxdb/influxdb-csv-error)
- [InfluxDB TSM Error](/tools/influxdb/influxdb-tsm-error)
