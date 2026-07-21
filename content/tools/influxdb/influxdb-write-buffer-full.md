---
title: "InfluxDB Write Buffer Full"
description: "Write buffer overflow"
tools:
  - influxdb
error-types: ["tool-error"]
severities: ["error"]
---
## Error Description
Write buffer is full and rejecting new writes.

## Common Causes
- Write throughput exceeded
- Disk I/O bottleneck
- Buffer size too small

## How to Fix
```yaml
[data]
  max-concurrent-writes = 1000
  max-write-buffer-size = 104857600
```

## Examples
```bash
# Monitor buffer stats
curl -s http://localhost:8086/debug/vars | jq '.WriteReq'
# Check disk I/O
iostat -x 1 5
```

