---
title: "InfluxDB Write Timeout"
description: "Write operations timing out"
tools:
  - influxdb
error-types: ["tool-error"]
severities: ["error"]
---
## Error Description
Write operations are timing out before completion.

## Common Causes
- High write throughput
- Disk I/O bottleneck
- Network latency

## How to Fix
```yaml
[data]
  max-concurrent-writes = 1000
  write-timeout = 10s
```

## Examples
```bash
# Monitor write performance
curl -s http://localhost:8086/debug/vars | jq '.WriteReq'
```

