---
title: "InfluxDB Memory Error"
description: "InfluxDB out of memory"
tools:
  - influxdb
error-types: ["tool-error"]
severities: ["error"]
---
## Error Description
InfluxDB process has exhausted available memory.

## Common Causes
- Too many concurrent queries
- Large query result sets
- Memory leak

## How to Fix
```yaml
# influxdb.conf memory limits
[data]
  cache-max-memory-size = 1073741824
  max-concurrent-compactions = 0

[query]
  max-memory-bytes = 0
  initial-memory-bytes = 0
```

## Examples
```bash
# Monitor memory usage
ps aux | grep influxd
# Restart to clear memory
systemctl restart influxdb
```

