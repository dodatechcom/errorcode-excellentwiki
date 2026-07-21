---
title: "[Solution] Prometheus Remote Read Timeout"
description: "How to fix Prometheus remote read timeout errors"
tools: ["prometheus"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Remote storage query taking too long
- Network latency to remote endpoint
- Query time range too large
- Remote storage overloaded

## How to Fix

Increase remote read timeout:

```yaml
remote_read:
  - url: 'http://remote-storage:9201/api/v1/read'
    timeout: 60s
```

Optimize query time range:

```yaml
# Use shorter evaluation intervals
global:
  evaluation_interval: 15s
```

Check network latency:

```bash
curl -o /dev/null -s -w '%{time_total}' http://remote-storage:9201/api/v1/read
```

## Examples

```bash
# Monitor remote read latency
curl -s 'http://localhost:9090/api/v1/query?query=prometheus_remote_read_duration_seconds'

# Check timeout configuration
curl -s http://localhost:9090/api/v1/status/config | grep -A 5 remote_read
```
