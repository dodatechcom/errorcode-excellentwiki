---
title: "InfluxDB Disk Error"
description: "InfluxDB disk I/O failure"
tools:
  - influxdb
error-types: ["tool-error"]
severities: ["error"]
---
## Error Description
InfluxDB encountered a disk I/O error.

## Common Causes
- Disk failure
- Filesystem corruption
- I/O scheduler issues

## How to Fix
```bash
# Check disk health
smartctl -a /dev/sda

# Check filesystem
fsck /dev/sda1

# Check I/O stats
iostat -x 1 5
```

## Examples
```bash
# Monitor disk I/O
iotop -a -d 1
# Check InfluxDB data directory
du -sh /var/lib/influxdb/engine/data/
```

