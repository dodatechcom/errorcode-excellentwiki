---
title: "InfluxDB HTTP Timeout"
description: "HTTP request timeout"
tools:
  - influxdb
error-types: ["tool-error"]
severities: ["error"]
---
## Error Description
HTTP requests are timing out.

## Common Causes
- Server overloaded
- Network latency
- Query too complex

## How to Fix
```yaml
[http]
  write-timeout = 10s
  read-timeout = 10s
  max-concurrent-write-limit = 100
```

## Examples
```bash
# Test HTTP response time
curl -w '@curl-format.txt' -o /dev/null -s http://localhost:8086/health
```

