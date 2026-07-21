---
title: "InfluxDB Compaction Error Code"
description: "Compaction error with specific code"
tools:
  - influxdb
error-types: ["tool-error"]
severities: ["error"]
---
## Error Description
Compaction returning specific error code.

## Common Causes
- Compaction backlog
- Disk space insufficient
- Compaction thread stuck

## How to Fix
```bash
# Check compaction status
curl -s http://localhost:8086/debug/vars | jq '.Compaction'

# Monitor disk usage
df -h /var/lib/influxdb
```

## Examples
```bash
# Check compaction logs
tail -100 /var/log/influxdb/influxdb.log | grep compaction
```

